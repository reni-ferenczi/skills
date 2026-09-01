"""Deep C++ parsing with tree-sitter.

The GPlates source cannot be compiled without Qt/Boost/CGAL/GDAL/PROJ, so this
module parses it *syntactically* with the official `tree-sitter-cpp` grammar and
recovers declarations, definitions, inheritance, members, variables, macros,
templates and every identifier occurrence with its syntactic role.

Two source transforms run before parsing. Both are strictly **length preserving**
— they overwrite bytes with spaces or same-length replacements — so every byte
offset, line and column in the parse tree still refers to the real file.

1. `neutralise_qt` rewrites Qt's macros (`Q_OBJECT`, `signals:`, `Q_SLOTS:`,
   `SIGNAL(...)`, `SLOT(...)`, `Q_PROPERTY(...)`), which are not valid C++ and
   otherwise wreck the parse of every widget class.
2. `select_branches` keeps the first arm of each `#if/#elif/#else` chain and
   blanks the rest, because tree-sitter sees all arms at once as one token
   stream. `#if 0` is handled the other way round, and include guards are
   unaffected (their first arm is the whole file).

Together these take the share of bytes inside ERROR nodes on GPlates 2.5.0 from
1.36% down to well under 0.5%.
"""

from __future__ import annotations

import importlib
import re
import sys
from pathlib import Path

from .common import DATA_DIR, SkillError

PYLIBS = DATA_DIR / "pylibs"

_PARSER = None
_LANGUAGE = None


def ensure_parser():
    """Import tree-sitter from the skill-local lib directory. Raises SkillError."""
    global _PARSER, _LANGUAGE
    if _PARSER is not None:
        return _PARSER
    if str(PYLIBS) not in sys.path:
        sys.path.insert(0, str(PYLIBS))
    # PYLIBS may have been created/populated after an earlier failed import, and
    # Python caches a finder per directory - drop it or the fresh install is invisible.
    importlib.invalidate_caches()
    try:
        import tree_sitter_cpp
        from tree_sitter import Language, Parser
    except ImportError as exc:
        raise SkillError(
            "tree-sitter is not installed. Run:\n"
            "  python -m pip install --target %s tree_sitter tree_sitter_cpp\n"
            "or re-run scripts/setup_index.py, which installs it automatically.\n"
            "(%s)" % (PYLIBS, exc)
        ) from exc
    _LANGUAGE = Language(tree_sitter_cpp.language())
    _PARSER = Parser(_LANGUAGE)
    return _PARSER


# ---------------------------------------------------------------------------
# Length-preserving source preparation
# ---------------------------------------------------------------------------

_ACCESS = re.compile(rb'\b(public|private|protected)\s+(?:Q_)?slots\s*:', re.I)
_SIGSEC = re.compile(rb'\b(?:Q_SIGNALS|signals)\s*:')
_SLOTSEC = re.compile(rb'\b(?:Q_SLOTS|slots)\s*:')
_QWORDS = re.compile(rb'\b(Q_OBJECT|Q_GADGET|Q_INVOKABLE|Q_SLOT|Q_SIGNAL|Q_SLOTS|Q_SIGNALS'
                     rb'|Q_DECL_[A-Z_]+|Q_UNUSED|emit)\b')
_EXPR_MACRO = re.compile(rb'\b(SIGNAL|SLOT)\s*\(')
_DECL_MACRO = re.compile(rb'\b(Q_PROPERTY|Q_ENUMS|Q_FLAGS|Q_DECLARE_METATYPE'
                         rb'|Q_DECLARE_FLAGS|Q_DECLARE_INTERFACE)\s*\(')
_COND = re.compile(rb'^[ \t]*#[ \t]*(if|ifdef|ifndef|elif|else|endif)\b[^\n]*', re.M)
_IF_ZERO = re.compile(rb'^[ \t]*#[ \t]*if[ \t]+0[ \t]*$')

_KEEP = (b"\n", b"\r")


def _blank(buf, lo, hi):
    """Overwrite buf[lo:hi] with spaces, preserving newlines (and so line numbers)."""
    for j in range(max(lo, 0), min(hi, len(buf))):
        if buf[j:j + 1] not in _KEEP:
            buf[j] = 32


def _pad(replacement: bytes, width: int) -> bytes:
    if len(replacement) > width:
        return b" " * width
    return replacement + b" " * (width - len(replacement))


def _blank_call(src: bytes, buf: bytearray, match, placeholder: bytes | None):
    """Blank a MACRO(...) span, optionally leaving a placeholder expression."""
    depth, i = 0, match.end() - 1
    while i < len(src):
        ch = src[i:i + 1]
        if ch == b"(":
            depth += 1
        elif ch == b")":
            depth -= 1
            if depth == 0:
                break
        i += 1
    end = min(i + 1, len(buf))
    _blank(buf, match.start(), end)
    if placeholder and end > match.start():
        buf[match.start()] = placeholder[0]


def neutralise_qt(data: bytes) -> bytes:
    """Replace Qt's non-C++ macros with same-length valid C++."""
    buf = bytearray(data)
    for m in _ACCESS.finditer(data):
        buf[m.start():m.end()] = _pad(m.group(1) + b":", m.end() - m.start())
    for m in _SIGSEC.finditer(bytes(buf)):
        buf[m.start():m.end()] = _pad(b"public:", m.end() - m.start())
    for m in _SLOTSEC.finditer(bytes(buf)):
        buf[m.start():m.end()] = _pad(b"public:", m.end() - m.start())
    for m in _QWORDS.finditer(bytes(buf)):
        _blank(buf, m.start(), m.end())
    src = bytes(buf)
    for m in _EXPR_MACRO.finditer(src):
        _blank_call(src, buf, m, b"0")     # keep connect(a, 0, b, 0) well formed
    for m in _DECL_MACRO.finditer(src):
        _blank_call(src, buf, m, None)
    return bytes(buf)


def select_branches(data: bytes) -> bytes:
    """Keep the first arm of every #if chain; blank #elif/#else arms and `#if 0` bodies."""
    buf = bytearray(data)
    stack = []
    for m in _COND.finditer(data):
        kw = m.group(1)
        if kw in (b"if", b"ifdef", b"ifndef"):
            # `#if 0` means the *second* arm is the live one; otherwise it is the first.
            zero = kw == b"if" and _IF_ZERO.match(m.group(0)) is not None
            stack.append({"arm": 0, "keep": 1 if zero else 0,
                          "blank_from": m.end() if zero else None})
        elif kw in (b"elif", b"else"):
            if not stack:
                continue
            top = stack[-1]
            if top["blank_from"] is not None:
                _blank(buf, top["blank_from"], m.start())
            top["arm"] += 1
            top["blank_from"] = None if top["arm"] == top["keep"] else m.end()
        elif kw == b"endif":
            if not stack:
                continue
            top = stack.pop()
            if top["blank_from"] is not None:
                _blank(buf, top["blank_from"], m.start())
    return bytes(buf)


def prepare(data: bytes) -> bytes:
    """Full length-preserving preparation applied before parsing."""
    return select_branches(neutralise_qt(data))


def parse(data: bytes):
    """Parse already-prepared bytes; returns a tree-sitter Tree."""
    return ensure_parser().parse(data)


def error_extent(tree) -> int:
    """Bytes covered by ERROR nodes — a per-file parse quality measure."""
    total = 0
    stack = [tree.root_node]
    while stack:
        node = stack.pop()
        if node.type == "ERROR":
            total += node.end_byte - node.start_byte
            continue
        if node.is_missing:
            total += 1
        stack.extend(node.children)
    return total

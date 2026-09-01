"""Extractors and the index builder for the GPlates code index."""

from __future__ import annotations

import re
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

from .common import SkillError

# ----------------------------------------------------------------------------
# File classification
# ----------------------------------------------------------------------------

CPP_EXT = {".cc", ".cpp", ".cxx", ".c", ".h", ".hh", ".hpp", ".hxx",
           ".template_cc", ".template_h"}
TEXT_EXT = CPP_EXT | {
    ".py", ".ui", ".glsl", ".qrc", ".rc", ".xpm", ".xml", ".xsd", ".xsl",
    ".cmake", ".in", ".txt", ".md", ".json", ".csv", ".conf",
    ".gpml", ".cpt", ".xy", ".rot", ".grot", ".sym", ".dat",
    ".linux", ".osx", ".windows",
}
# Extension-less files (or fixed names) worth indexing as text.
TEXT_NAMES = {"CHANGELOG", "AUTHORS", "COPYING", "CREDITS", "README", "LICENSE",
              "CMakeLists.txt"}

SKIP_DIRS = {".git", ".svn", ".idea", ".vs", "build", "__pycache__",
             "node_modules", ".venv"}

MAX_TEXT_BYTES = 4 * 1024 * 1024

# ctags kinds that are pure noise for code navigation.
SKIP_KINDS = {"parameter", "local", "tparam", "macroparam", "label", "name",
              "file", "unknown"}
DECL_KINDS = {"prototype"}


def classify(rel_path: str, ext: str, name: str) -> str:
    if rel_path.startswith("src/qt-resources/gpgim/"):
        return "gpgim"
    if ext in CPP_EXT:
        return "cpp"
    if ext == ".py":
        return "python"
    if ext == ".ui":
        return "ui"
    if ext == ".glsl":
        return "shader"
    if ext in (".qrc", ".rc", ".xpm"):
        return "resource"
    if name == "CMakeLists.txt" or ext in (".cmake", ".in") or name.startswith(("BUILD.", "DEPS.")):
        return "build"
    if rel_path.startswith("sample-data/"):
        return "data"
    if ext in (".md", ".txt", ".conf") or name in ("CHANGELOG", "AUTHORS", "COPYING",
                                                   "CREDITS", "README"):
        return "doc"
    return "other"


def is_text(ext: str, name: str) -> bool:
    return ext in TEXT_EXT or name in TEXT_NAMES


# ----------------------------------------------------------------------------
# ctags
# ----------------------------------------------------------------------------

CTAGS_ARGS = [
    "--output-format=json",
    "--fields=+neKlSstZaiE",
    "--extras=+F",
    "--languages=C,C++,Python",
    "--kinds-C=*",
    "--kinds-Python=*",
    "--recurse",
    "--exclude=.git",
    "--exclude=build",
    "--exclude=__pycache__",
]


def run_ctags(ctags_exe: Path, source_root: Path, out_file: Path, targets) -> int:
    cmd = [str(ctags_exe), *CTAGS_ARGS, "--kinds-C++=*", "-f", str(out_file), *targets]
    proc = subprocess.run(cmd, cwd=str(source_root), capture_output=True, text=True)
    if proc.returncode != 0:
        raise SkillError(
            "ctags failed (exit %d):\n%s" % (proc.returncode, proc.stderr.strip()[:2000])
        )
    if not out_file.exists() or out_file.stat().st_size == 0:
        raise SkillError("ctags produced no output - the source tree may be empty")
    return out_file.stat().st_size


# ----------------------------------------------------------------------------
# Extractors
# ----------------------------------------------------------------------------

INCLUDE_RE = re.compile(r'^\s*#\s*include\s*(?:<([^>]+)>|"([^"]+)")')
CONNECT_RE = re.compile(r'\bconnect\s*\(')
SIGNAL_RE = re.compile(r'\bSIGNAL\s*\(')
SLOT_RE = re.compile(r'\bSLOT\s*\(')


def squash(s):
    return re.sub(r"\s+", " ", s or "").strip()


def extract_includes(text):
    for i, line in enumerate(text.splitlines(), 1):
        m = INCLUDE_RE.match(line)
        if m:
            if m.group(1) is not None:
                yield i, m.group(1), 1
            else:
                yield i, m.group(2), 0


def _balanced_call(text, open_pos, limit=4000):
    """Return the text inside the parentheses that start at open_pos."""
    depth = 0
    for i in range(open_pos, min(len(text), open_pos + limit)):
        ch = text[i]
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                return text[open_pos + 1:i]
    return None


def _macro_arg(body, macro_re):
    """Locate MACRO( ... ) in `body`; return (inner_text, start, end_after_paren)."""
    m = macro_re.search(body)
    if not m:
        return None, -1, -1
    inner = _balanced_call(body, m.end() - 1)
    if inner is None:
        return None, -1, -1
    return inner, m.start(), m.end() + len(inner) + 1


def extract_connections(text):
    """Pull sender/SIGNAL/receiver/SLOT out of Qt connect() calls."""
    for m in CONNECT_RE.finditer(text):
        body = _balanced_call(text, m.end() - 1)
        if not body or "SIGNAL" not in body:
            continue
        line = text.count("\n", 0, m.start()) + 1
        sig, sig_start, sig_end = _macro_arg(body, SIGNAL_RE)
        slot, slot_start, slot_end = _macro_arg(body, SLOT_RE)
        sender = body[:sig_start] if sig_start >= 0 else ""
        receiver = ""
        if sig_end >= 0 and slot_start > sig_end:
            receiver = body[sig_end:slot_start]
        yield (
            line,
            squash(sender).strip(", ")[:200],
            squash(sig)[:200] if sig is not None else None,
            squash(receiver).strip(", ")[:200],
            squash(slot)[:200] if slot is not None else None,
        )


CLASS_RE = re.compile(r'\b(?:bp::)?(class_|enum_)\s*<\s*(.*?)\s*>\s*\(\s*"([^"]+)"', re.S)
# Longest alternatives first: Python's `|` takes the first that matches, so a bare
# `def` listed ahead of `def_readwrite` would shadow it.
DEF_RE = re.compile(r'(?:^|[.\s;(])(?:bp::)?'
                    r'(add_static_property|add_property|def_readwrite|def_readonly'
                    r'|staticmethod|value|def)'
                    r'\s*\(\s*"([^"]+)"\s*(?:,\s*([^,)\n]*))?')
# Constructor overloads carry no Python name; record them as __init__.
INIT_RE = re.compile(r'\.\s*def\s*\(\s*(?:bp::)?init\s*<\s*(.*?)\s*>\s*\(\s*\)\s*\)', re.S)


def extract_py_api(text):
    """Boost.Python bindings: class_<T>("Name").def("member", ...) chains.

    A `class_<>`/`enum_<>` opens an owner scope that stays in effect for every
    following `.def(...)` until the statement ends at the next top-level `;`.
    """
    if ("class_" not in text and "enum_" not in text and "def(" not in text
            and "add_property" not in text and "add_static_property" not in text):
        return
    matches = []
    for m in CLASS_RE.finditer(text):
        matches.append((m.start(), "class", m))
    for m in DEF_RE.finditer(text):
        matches.append((m.start(), "def", m))
    for m in INIT_RE.finditer(text):
        matches.append((m.start(), "init", m))
    matches.sort(key=lambda t: t[0])

    line_of = _line_counter(text)
    owner = ""
    prev_end = 0
    for start, what, m in matches:
        if ";" in text[prev_end:start]:
            owner = ""
        prev_end = m.end()
        if what == "class":
            kind = "class" if m.group(1) == "class_" else "enum"
            owner = m.group(3)
            yield line_of(start), "", owner, kind, squash(m.group(2)).split(",")[0]
            continue
        if what == "init":
            yield (line_of(start), owner, "__init__", "constructor",
                   ("init<%s>" % squash(m.group(1)))[:200])
            continue
        verb, pyname = m.group(1), m.group(2)
        target = squash(m.group(3) or "")[:200]
        if verb == "def":
            kind = "method" if owner else "function"
        elif verb == "value":
            kind = "enum_value"
        elif verb == "staticmethod":
            kind = "staticmethod"
        elif verb == "add_static_property":
            kind = "static_attribute"
        else:
            kind = "attribute"
        yield line_of(start), owner, pyname, kind, target or None


def _line_counter(text):
    """Offset -> 1-based line number, O(log n) per lookup."""
    import bisect
    starts = [0]
    for i, ch in enumerate(text):
        if ch == "\n":
            starts.append(i + 1)

    def lookup(offset):
        return bisect.bisect_right(starts, offset)

    return lookup


def extract_ui(path: Path):
    """Parse a Qt Designer .ui file into ((class, base, title), [(class, name, text)])."""
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError:
        return None, []
    cls = (root.findtext("class") or "").strip()
    top = root.find("widget")
    base = top.get("class") if top is not None else None
    title = None
    widgets = []
    for w in root.iter("widget"):
        wclass = w.get("class") or ""
        wname = w.get("name") or ""
        text = None
        for prop in w.findall("property"):
            pname = prop.get("name")
            if pname in ("text", "title", "windowTitle"):
                val = prop.findtext("string")
                if val:
                    text = squash(val)[:200]
                    if pname == "windowTitle" and w is top:
                        title = text
                    break
        if wname:
            widgets.append((wclass, wname, text))
    for act in root.iter("action"):
        aname = act.get("name") or ""
        atext = None
        for prop in act.findall("property"):
            if prop.get("name") == "text":
                atext = squash(prop.findtext("string") or "")[:200]
                break
        if aname:
            widgets.append(("QAction", aname, atext))
    return (cls, base, title), widgets


def _gp_child_text(elem, tag):
    for child in elem:
        if child.tag.split("}")[-1] == tag:
            return squash("".join(child.itertext()))[:1000]
    return None


def _gp_child_all(elem, tag):
    return [squash("".join(c.itertext())) for c in elem if c.tag.split("}")[-1] == tag]


def extract_gpgim(path: Path):
    """Feature classes and properties from src/qt-resources/gpgim/gpgim.xml."""
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        raise SkillError("could not parse %s: %s" % (path, exc)) from exc

    # ElementTree drops line numbers, so recover them with a forward text scan.
    text_lines = path.read_text(encoding="utf-8", errors="replace").splitlines()

    def find_line(needle, start):
        for i in range(start, len(text_lines)):
            if needle in text_lines[i]:
                return i + 1, i + 1
        return 0, start

    features, properties, feature_properties = [], [], []

    # Global <PropertyList> holds the actual property definitions.
    cursor = 0
    for parent in root:
        if parent.tag.split("}")[-1] != "PropertyList":
            continue
        for prop in parent:
            if prop.tag.split("}")[-1] != "Property":
                continue
            pname = _gp_child_text(prop, "Name")
            if not pname:
                continue
            line, cursor = find_line(">" + pname + "<", cursor)
            properties.append((line, pname,
                               ", ".join(_gp_child_all(prop, "Type")) or None,
                               _gp_child_text(prop, "Multiplicity"),
                               _gp_child_text(prop, "Description")))

    # <FeatureClass> entries reference properties by name.
    cursor = 0
    for fc in root.iter():
        if fc.tag.split("}")[-1] != "FeatureClass":
            continue
        name = _gp_child_text(fc, "Name")
        if not name:
            continue
        line, cursor = find_line(">" + name + "<", cursor)
        default_geom = None
        for key, val in fc.attrib.items():
            if key.split("}")[-1] == "defaultGeometryProperty":
                default_geom = val
        features.append((line, name, _gp_child_text(fc, "ClassType"),
                         ", ".join(_gp_child_all(fc, "Inherits")) or None,
                         _gp_child_text(fc, "Description"), default_geom))
        for pname in _gp_child_all(fc, "Property"):
            if pname:
                feature_properties.append((name, pname))
    return features, properties, feature_properties

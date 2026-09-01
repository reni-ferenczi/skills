"""Paths, config and sanity checks shared by the gplates-code skill scripts.

Fail-early philosophy: every helper here raises SkillError with an actionable
message instead of returning a half-usable value.
"""

from __future__ import annotations

import json
import os
import re
import sqlite3
import sys
from pathlib import Path

# skills/gplates-code/scripts/gplates_index/common.py -> skills/gplates-code
SKILL_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = SKILL_DIR / "data"
TOOLS_DIR = DATA_DIR / "tools"
CONFIG_PATH = DATA_DIR / "config.json"
DB_PATH = DATA_DIR / "gplates.db"

MIN_VERSION = (2, 5, 0)

# Universal Ctags Windows build, pinned. Portable: the zip holds ctags.exe at its root.
CTAGS_VERSION = "v6.1.0"
CTAGS_URL = (
    "https://github.com/universal-ctags/ctags-win32/releases/download/"
    f"{CTAGS_VERSION}/ctags-{CTAGS_VERSION}-x64.zip"
)
CTAGS_EXE = TOOLS_DIR / "ctags.exe"

# Files that must exist for a directory to be a GPlates source tree.
REQUIRED_MARKERS = [
    "CMakeLists.txt",
    "CHANGELOG",
    "cmake/modules/Version.cmake",
    "src/CMakeLists.txt",
    "src/gplates_main.cc",
    "src/app-logic",
    "src/qt-widgets",
    "src/maths",
    "src/model",
    "src/qt-resources/gpgim/gpgim.xml",
]


class SkillError(RuntimeError):
    """Anything the user has to fix before the skill can continue."""


def die(msg: str, code: int = 2):
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(code)


def read_config() -> dict:
    if not CONFIG_PATH.exists():
        raise SkillError(
            "index not set up yet - run:  python scripts/setup_index.py --source <GPLATES_SRC_DIR>"
        )
    with CONFIG_PATH.open(encoding="utf-8") as fh:
        return json.load(fh)


def write_config(cfg: dict) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with CONFIG_PATH.open("w", encoding="utf-8") as fh:
        json.dump(cfg, fh, indent=2, sort_keys=True)
        fh.write("\n")


def parse_version(source_root: Path):
    """Read GPLATES_VERSION_{MAJOR,MINOR,PATCH} out of cmake/modules/Version.cmake."""
    vfile = source_root / "cmake" / "modules" / "Version.cmake"
    if not vfile.is_file():
        raise SkillError(f"missing {vfile} - not a GPlates source tree")
    text = vfile.read_text(encoding="utf-8", errors="replace")
    parts = []
    for part in ("MAJOR", "MINOR", "PATCH"):
        m = re.search(rf"^\s*set\s*\(\s*GPLATES_VERSION_{part}\s+(\d+)\s*\)", text, re.M)
        if not m:
            raise SkillError(f"could not read GPLATES_VERSION_{part} from {vfile}")
        parts.append(int(m.group(1)))
    return parts[0], parts[1], parts[2]


def check_source_root(path):
    """Validate that `path` is a GPlates >= 2.5.0 source tree. Returns (root, version)."""
    root = Path(path).expanduser()
    try:
        root = root.resolve(strict=True)
    except OSError as exc:
        raise SkillError(f"source directory not found: {path} ({exc})") from exc
    if not root.is_dir():
        raise SkillError(f"source path is not a directory: {root}")

    missing = [m for m in REQUIRED_MARKERS if not (root / m).exists()]
    if missing:
        raise SkillError(
            f"{root} does not look like a GPlates source tree - missing: "
            + ", ".join(missing[:5])
            + ("" if len(missing) <= 5 else f" (+{len(missing) - 5} more)")
        )

    version = parse_version(root)
    if version < MIN_VERSION:
        raise SkillError(
            f"GPlates {'.'.join(map(str, version))} found at {root}, "
            f"but this skill requires {'.'.join(map(str, MIN_VERSION))} or later"
        )
    return root, version


def open_db(readonly: bool = True) -> sqlite3.Connection:
    if not DB_PATH.exists():
        raise SkillError(
            "no index found - run:  python scripts/setup_index.py --source <GPLATES_SRC_DIR>"
        )
    if readonly:
        uri = f"file:{DB_PATH.as_posix()}?mode=ro"
        con = sqlite3.connect(uri, uri=True)
    else:
        con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA temp_store = MEMORY")
    return con


def source_root_from_db(con: sqlite3.Connection) -> Path:
    row = con.execute("SELECT value FROM meta WHERE key = 'source_root'").fetchone()
    if row is None:
        raise SkillError("index is missing its source_root - rebuild it")
    return Path(row["value"])

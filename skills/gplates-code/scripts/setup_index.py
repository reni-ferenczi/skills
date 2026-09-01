#!/usr/bin/env python3
"""Set up the gplates-code index.

    python scripts/setup_index.py --source C:\\Dev\\gplates_2.5.0_src
    python scripts/setup_index.py --check        # validate an existing index
    python scripts/setup_index.py --rebuild      # rebuild using the stored source path

Every step fails loudly and early: the source tree is validated before anything is
downloaded, and the finished index is verified against minimum row counts.
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
import tempfile
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gplates_index import indexer  # noqa: E402
from gplates_index.common import (  # noqa: E402
    CTAGS_EXE, CTAGS_URL, CTAGS_VERSION, DATA_DIR, DB_PATH, SkillError,
    TOOLS_DIR, check_source_root, open_db, read_config, write_config,
)


def find_ctags(explicit: str | None, quiet: bool) -> Path:
    """Return a usable ctags executable, downloading the pinned Windows build if needed."""
    if explicit:
        p = Path(explicit)
        if not p.is_file():
            raise SkillError("--ctags %s does not exist" % explicit)
        return p
    if CTAGS_EXE.is_file():
        return CTAGS_EXE
    on_path = shutil.which("ctags")
    if on_path:
        indexer.log(quiet, "using ctags from PATH: %s" % on_path)
        return Path(on_path)
    if os.name != "nt":
        raise SkillError(
            "ctags not found. Install Universal Ctags and re-run, or pass --ctags <path>. "
            "(Automatic download is only wired up for Windows.)"
        )

    TOOLS_DIR.mkdir(parents=True, exist_ok=True)
    indexer.log(quiet, "downloading Universal Ctags %s ..." % CTAGS_VERSION)
    tmp_zip = TOOLS_DIR / "ctags-download.zip"
    try:
        with urllib.request.urlopen(CTAGS_URL, timeout=120) as resp, tmp_zip.open("wb") as out:
            shutil.copyfileobj(resp, out)
    except (urllib.error.URLError, OSError) as exc:
        raise SkillError(
            "could not download ctags from %s (%s).\n"
            "Download it manually and place ctags.exe at %s, or pass --ctags <path>."
            % (CTAGS_URL, exc, CTAGS_EXE)
        ) from exc
    if tmp_zip.stat().st_size < 500_000:
        raise SkillError("downloaded ctags archive looks truncated (%d bytes)"
                         % tmp_zip.stat().st_size)
    with zipfile.ZipFile(tmp_zip) as zf:
        names = [n for n in zf.namelist() if n.lower().endswith("ctags.exe")]
        if not names:
            raise SkillError("ctags.exe not found inside %s" % CTAGS_URL)
        with zf.open(names[0]) as src, CTAGS_EXE.open("wb") as dst:
            shutil.copyfileobj(src, dst)
    tmp_zip.unlink()
    indexer.log(quiet, "  installed %s" % CTAGS_EXE)
    return CTAGS_EXE


def ensure_tree_sitter(quiet: bool):
    """Install tree-sitter into the skill's own lib dir (no venv, no compiler)."""
    from gplates_index import cpp_parse
    try:
        cpp_parse.ensure_parser()
        return
    except SkillError:
        pass
    indexer.log(quiet, "installing tree-sitter into %s ..." % cpp_parse.PYLIBS)
    cpp_parse.PYLIBS.mkdir(parents=True, exist_ok=True)
    import subprocess
    proc = subprocess.run(
        [sys.executable, "-m", "pip", "install", "--quiet", "--disable-pip-version-check",
         "--target", str(cpp_parse.PYLIBS), "tree_sitter", "tree_sitter_cpp"],
        capture_output=True, text=True)
    if proc.returncode != 0:
        raise SkillError(
            "could not install tree-sitter (%s).\nInstall it manually:\n"
            "  python -m pip install --target %s tree_sitter tree_sitter_cpp"
            % (proc.stderr.strip()[:400], cpp_parse.PYLIBS))
    cpp_parse.ensure_parser()
    indexer.log(quiet, "  tree-sitter ready")


def check_ctags(ctags: Path, quiet: bool) -> str:
    import subprocess
    proc = subprocess.run([str(ctags), "--version"], capture_output=True, text=True)
    if proc.returncode != 0:
        raise SkillError("%s is not runnable: %s" % (ctags, proc.stderr.strip()[:400]))
    banner = proc.stdout.splitlines()[0] if proc.stdout else ""
    if "Universal Ctags" not in banner:
        raise SkillError(
            "%s is not Universal Ctags (got %r). Exuberant Ctags cannot emit JSON."
            % (ctags, banner)
        )
    feats = subprocess.run([str(ctags), "--list-features"], capture_output=True, text=True)
    if "json" not in feats.stdout:
        raise SkillError("%s was built without JSON support - install a +json build" % ctags)
    indexer.log(quiet, "ctags: %s" % banner)
    return banner


def do_check(quiet: bool) -> int:
    cfg = read_config()
    root, version = check_source_root(cfg["source_root"])
    con = open_db()
    stats = indexer.collect_stats(con)
    con.close()
    problems = indexer.verify_stats(stats)
    print("source : %s (GPlates %s)" % (root, ".".join(map(str, version))))
    print("index  : %s (%.1f MB)" % (DB_PATH, DB_PATH.stat().st_size / 1048576))
    for key in sorted(stats):
        print("  %-16s %d" % (key, stats[key]))
    if problems:
        print("\nFAILED sanity checks:", file=sys.stderr)
        for p in problems:
            print("  " + p, file=sys.stderr)
        return 1
    print("\nall sanity checks passed")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Build the GPlates code index.")
    ap.add_argument("--source", help="path to an extracted GPlates 2.5.0+ source tree")
    ap.add_argument("--ctags", help="path to a Universal Ctags executable (optional)")
    ap.add_argument("--check", action="store_true", help="verify an existing index and exit")
    ap.add_argument("--rebuild", action="store_true",
                    help="rebuild using the source path stored in data/config.json")
    ap.add_argument("--validate-only", action="store_true",
                    help="validate the source tree only; build nothing")
    ap.add_argument("-q", "--quiet", action="store_true", help="suppress progress output")
    args = ap.parse_args(argv)

    try:
        if args.check:
            return do_check(args.quiet)

        source = args.source
        if source is None:
            if not (args.rebuild or DB_PATH.exists() or (DATA_DIR / "config.json").exists()):
                ap.error("--source is required the first time")
            source = read_config()["source_root"]

        root, version = check_source_root(source)
        indexer.log(args.quiet, "source : %s (GPlates %s)"
                    % (root, ".".join(map(str, version))))
        if args.validate_only:
            print("OK: %s is GPlates %s" % (root, ".".join(map(str, version))))
            return 0

        ctags = find_ctags(args.ctags, args.quiet)
        banner = check_ctags(ctags, args.quiet)
        ensure_tree_sitter(args.quiet)

        with tempfile.TemporaryDirectory(prefix="gplates-tags-") as tmp:
            tags_file = Path(tmp) / "tags.json"
            stats = indexer.build_index(root, version, ctags, tags_file, args.quiet)

        write_config({
            "source_root": str(root),
            "gplates_version": ".".join(map(str, version)),
            "ctags": str(ctags),
            "ctags_banner": banner,
        })

        problems = indexer.verify_stats(stats)
        if problems:
            print("index built but FAILED sanity checks:", file=sys.stderr)
            for p in problems:
                print("  " + p, file=sys.stderr)
            return 1

        print("index ready: %s (%.1f MB)" % (DB_PATH, DB_PATH.stat().st_size / 1048576))
        print("  %d files, %d symbols, %d lines, %d UI widgets, %d GPGIM feature classes"
              % (stats["files"], stats["symbols"], stats["lines"],
                 stats["ui_widgets"], stats["gpgim_features"]))
        print("next: python scripts/gpq.py info")
        return 0
    except SkillError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

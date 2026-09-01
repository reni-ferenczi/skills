#!/usr/bin/env python3
"""Schedule and settle the prose pass.

The writing itself is done by sub-agents; this script owns the bookkeeping, so
an interruption costs at most one wave of agents.

    python scripts/prose_pass.py status
    python scripts/prose_pass.py plan --tier 3 --batch-size 12 --waves 8
    python scripts/prose_pass.py settle

`plan` prints the next batches as JSON (units grouped by tier and component).
`settle` re-reads every page, marks as done the units whose prose blocks are
gone, flags the ones that came back untouched, and merges the per-batch
description files into data/descriptions.jsonl.
"""

from __future__ import annotations

import argparse
import collections
import itertools
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from bookkit import (  # noqa: E402
    BOOK_DIR, BookError, DATA_DIR, DESCRIPTIONS_PATH, PROGRESS_PATH, PROSE_ANY_RE,
    component_page, load_json, load_manifest, save_json,
)

BATCH_DIR = DATA_DIR / "batches"


def page_state(rel_path: str) -> str:
    page = BOOK_DIR / rel_path
    if not page.exists():
        return "missing"
    return "pending" if PROSE_ANY_RE.search(page.read_text(encoding="utf-8")) else "done"


def all_targets(units) -> list[dict]:
    """Unit pages plus the component pages and the TOC, in writing order."""
    targets = [{"id": u["id"], "page": u["page"], "tier": u["tier"],
                "component": u["component"], "kind": "unit"} for u in units]
    components = sorted({u["component"] for u in units} |
                        set(load_json(DATA_DIR / "extras.json", {})))
    targets += [{"id": f"component:{c}", "page": component_page(c), "tier": 1,
                 "component": c, "kind": "component"} for c in components]
    targets.append({"id": "book", "page": "TOC.md", "tier": 1,
                    "component": "*", "kind": "toc"})
    return targets


def cmd_status(args, units) -> int:
    targets = all_targets(units)
    state = {t["id"]: page_state(t["page"]) for t in targets}
    per_tier = collections.Counter()
    for t in targets:
        if t["kind"] == "unit":
            per_tier[(t["tier"], state[t["id"]])] += 1

    print("units by tier")
    for tier in (1, 2, 3):
        done = per_tier[(tier, "done")]
        pending = per_tier[(tier, "pending")]
        total = done + pending + per_tier[(tier, "missing")]
        bar = "#" * round(30 * done / total) if total else ""
        print(f"  tier {tier}: {done:5d}/{total:<5d} done  {bar}")
    comps = [t for t in targets if t["kind"] == "component"]
    print(f"components: {sum(1 for t in comps if state[t['id']] == 'done')}/{len(comps)} done")
    print(f"TOC overview: {state['book']}")

    failed = load_json(PROGRESS_PATH, {}).get("failed", [])
    if failed:
        print(f"flagged after a retry: {len(failed)}")
        for uid in failed[:20]:
            print(f"  {uid}")
    return 0


def cmd_plan(args, units) -> int:
    by_id = {u["id"]: u for u in units}
    targets = [t for t in all_targets(units) if t["kind"] == args.kind]
    if args.tier:
        targets = [t for t in targets if t["tier"] == args.tier]
    if args.component:
        targets = [t for t in targets if t["component"] == args.component]
    pending = [t for t in targets if page_state(t["page"]) == "pending"]
    pending.sort(key=lambda t: (t["component"], t["id"]))

    batches, wanted = [], args.waves * args.parallel if args.waves else None
    for _, group in itertools.groupby(pending, key=lambda t: t["component"]):
        group = list(group)
        for i in range(0, len(group), args.batch_size):
            chunk = group[i:i + args.batch_size]
            batches.append({
                "batch": f"{chunk[0]['component']}-t{chunk[0]['tier']}-"
                         f"{len(batches):03d}",
                "tier": chunk[0]["tier"],
                "component": chunk[0]["component"],
                "units": [{"id": t["id"], "page": t["page"],
                           "files": by_id[t["id"]]["files"] if t["id"] in by_id else [],
                           "lines": by_id[t["id"]]["signals"].get("lines", 0)
                           if t["id"] in by_id else 0}
                          for t in chunk],
            })
            if wanted and len(batches) >= wanted:
                break
        if wanted and len(batches) >= wanted:
            break

    out = {"pending": len(pending), "batches": batches}
    if args.out:
        Path(args.out).write_text(json.dumps(out, indent=1), encoding="utf-8")
        print(f"{len(pending)} pending, wrote {len(batches)} batches to {args.out}")
    else:
        print(json.dumps(out, indent=1))
    return 0


def cmd_settle(args, units) -> int:
    targets = all_targets(units)
    progress = load_json(PROGRESS_PATH, {"units": {}, "failed": []})
    progress.setdefault("units", {})
    progress.setdefault("failed", [])
    run = progress.get("run", 0) + 1
    progress["run"] = run

    still_pending = []
    for t in targets:
        state = page_state(t["page"])
        prev = progress["units"].get(t["id"], {})
        progress["units"][t["id"]] = {"state": state, "run": run,
                                      "attempts": prev.get("attempts", 0) + (state != "done")}
        if state != "done":
            still_pending.append(t["id"])
            if progress["units"][t["id"]]["attempts"] >= 2 and t["id"] not in progress["failed"]:
                progress["failed"].append(t["id"])
        elif t["id"] in progress["failed"]:
            progress["failed"].remove(t["id"])

    merged = merge_descriptions()
    save_json(PROGRESS_PATH, progress)
    print(f"run {run}: {len(targets) - len(still_pending)}/{len(targets)} pages written, "
          f"{len(still_pending)} pending, {len(progress['failed'])} flagged")
    print(f"descriptions: +{merged} lines merged into {DESCRIPTIONS_PATH.name}")
    return 0


def merge_descriptions() -> int:
    """Fold data/batches/*.jsonl into descriptions.jsonl and clear the batch files."""
    if not BATCH_DIR.exists():
        return 0
    added = 0
    with DESCRIPTIONS_PATH.open("a", encoding="utf-8", newline="\n") as out:
        for path in sorted(BATCH_DIR.glob("*.jsonl")):
            for line in path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if rec.get("qname") and rec.get("oneliner"):
                    out.write(json.dumps({"qname": rec["qname"],
                                          "oneliner": " ".join(str(rec["oneliner"]).split())},
                                         sort_keys=True) + "\n")
                    added += 1
            path.unlink()
    return added


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    plan = sub.add_parser("plan")
    plan.add_argument("--tier", type=int, choices=(1, 2, 3))
    plan.add_argument("--component")
    plan.add_argument("--kind", default="unit", choices=("unit", "component", "toc"))
    plan.add_argument("--batch-size", type=int, default=10)
    plan.add_argument("--parallel", type=int, default=10, help="agents per wave")
    plan.add_argument("--waves", type=int, default=0, help="0 = plan everything pending")
    plan.add_argument("--out", help="write the plan to this file instead of stdout")
    sub.add_parser("settle")
    args = ap.parse_args()

    units = load_manifest()
    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    return {"status": cmd_status, "plan": cmd_plan, "settle": cmd_settle}[args.cmd](args, units)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BookError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)

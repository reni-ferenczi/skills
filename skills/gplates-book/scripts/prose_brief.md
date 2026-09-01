# Brief: writing prose for GPlates unit pages

You are filling in the prose of an already-generated reference manual. Every
structural fact on the page — the source files, the type and member tables, the
bases, the fan-in, the cross-links, the `gpq` recipes — was derived from a code
index and is correct. Your job is only the two prose blocks.

**Do the work yourself**, with `Read`, `Edit` and `Bash`. Do not launch a
sub-agent, and do not stop to describe a plan — go straight to the first page.
You are finished only when every page in your batch has both prose blocks
replaced and the batch `.jsonl` file exists on disk.

## Paths

| What | Where |
|---|---|
| Book skill (all page paths are relative to this) | `C:\Dev\skills\skills\gplates-book` |
| Code index skill — run every `gpq` command from here | `C:\Dev\skills\skills\gplates-code` |
| GPlates source tree — read source files directly from here | `C:\Dev\gplates_2.5.0_src` |
| Orientation, 135 lines, read it once before you start | `C:\Dev\skills\skills\gplates-code\references\ARCHITECTURE.md` |

A page listed as `src/app-logic/Foo.md` lives at
`C:\Dev\skills\skills\gplates-book\book\src\app-logic\Foo.md`, and its sources
live under `C:\Dev\gplates_2.5.0_src\src\app-logic\`.

## For each page in your batch

1. **Read the page.** It is complete apart from two placeholder blocks:

   ```
   [[[PROSE overview unit=<unit id> tier=<n>]]]
   ...instructions...
   [[[/PROSE]]]
   ```

   and the same shape with `notes`.

   If a page has **no** `[[[PROSE` markers left, an earlier run already wrote
   it: leave its prose exactly as it is, and only record its one-liners in
   step 5. Re-running a batch must not rewrite finished pages.

2. **Read the real code**, at the depth your tier calls for:

   | Tier | How much to read |
   |---|---|
   | 1 | Both source files end to end. Follow the load-bearing collaborators with `gpq def <Name> --body`, `gpq hier <Class>` and `gpq uses <Name>`. These pages carry the engine, so they earn the time. |
   | 2 | The header in full; skim the `.cc` where the header does not explain itself. One or two `gpq` lookups for the types it hands around. |
   | 3 | The declarations and the Doxygen already quoted on the page. Open a source file only where the page leaves the purpose genuinely unclear. Do not read whole files without a reason. |

3. **Replace each block with your prose**, using `Edit`. The opening
   `[[[PROSE ...]]]` line and the closing `[[[/PROSE]]]` line are part of what
   you replace — delete them. No `[[[PROSE` or `[[[/PROSE]]]` text may survive
   anywhere in the file; a verifier fails the book if it does.

4. **Change nothing else.** Not the heading text, not the tables, not the
   breadcrumb, not the `Explore` commands. That content is regenerated from the
   index and your edits to it would be silently overwritten.

## Prose rules — follow these literally

- Explain purpose, design intent and non-obvious behaviour. Nothing else.
- Never restate what the tables already show. The reader can see the class list,
  the member signatures, the base classes and who calls this unit.
- Never speculate. Every claim must come from code you actually read. If you are
  inferring, say what the code does instead of what you think it is for.
- If there is nothing beyond the tables to say, say nothing.
- Write for a developer about to change this code, answering "what is this, and
  when would I touch it".

**`## Overview`** — one to three paragraphs. Name real collaborators by their
real type names, in backticks. Plain prose: no headings, no tables, at most one
short list.

**`## Notes`** — invariants, ownership and lifetime, threading, error handling,
performance traps, deprecation. Only things a reader would otherwise get wrong.
If there is nothing, replace the whole block with exactly:

```
*None.*
```

That is the right answer for most tier-3 units, and padding it is worse than
leaving it empty.

## Step 5 — record the one-liners

Append one JSON object per line to `data/batches/<your batch id>.jsonl`
(create the file; UTF-8, LF endings, no wrapping array):

- one line for every unit page you finished:

  `{"qname": "unit:app-logic/ReconstructionTree", "oneliner": "..."}`

- one line for each public type, free function or macro on the page you can
  honestly describe in a clause:

  `{"qname": "GPlatesAppLogic::ReconstructionTree", "oneliner": "..."}`

  Use the **exact** qualified name as printed in the page's tables — these lines
  become the by-name index entries, and a name that does not match is dropped.

One-liners are at most about 110 characters, a noun phrase or a single clause,
no trailing full stop needed, and they must not repeat the name itself.

## gpq cheat sheet

Run from `C:\Dev\skills\skills\gplates-code`:

```bash
python scripts/gpq.py file src/app-logic/ReconstructUtils.h
python scripts/gpq.py def ReconstructionTree --kind class --body
python scripts/gpq.py uses LayerProxy --role call --context-symbol
python scripts/gpq.py hier LayerProxy
python scripts/gpq.py members ReconstructionTree --access public
python scripts/gpq.py grep "anchored plate id"
```

## Report

Your final message is the return value, not a note to a human. Emit exactly:

```
<batch id>: <k>/<n> pages written
```

followed by one line per page you could not finish, with the reason. Nothing
else — no summary of the prose you wrote.

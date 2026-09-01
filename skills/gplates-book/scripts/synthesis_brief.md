# Brief: writing a component page or the book's project overview

This runs after the unit pages are written. You are synthesising upwards: the
material you need is already in the book, not in the C++ source. Read the source
only to settle a specific question the pages leave open.

**Do the work yourself**, with `Read`, `Edit`, `Grep` and `Bash`. Do not launch a
sub-agent.

## Paths

| What | Where |
|---|---|
| Book | `C:\Dev\skills\skills\gplates-book\book` |
| Code index skill — run `gpq` from here | `C:\Dev\skills\skills\gplates-code` |
| Source tree | `C:\Dev\gplates_2.5.0_src` |
| Tree map, worth reading once | `C:\Dev\skills\skills\gplates-code\references\ARCHITECTURE.md` |

## If your target is a component page (`book/components/<name>.md`)

1. Read the whole component page. Its `## Units` table already carries a
   one-line description per unit, its `## Depends on` and `## Used by` tables
   already carry the measured cross-component reference counts, and
   `## Other files` lists what has no page of its own.
2. Read the `## Overview` section of the component's **most load-bearing units**
   — the ten to fifteen with the highest fan-in in the unit table, plus any the
   others clearly hang off. Do not read every unit page.
3. Replace the `[[[PROSE component ...]]] ... [[[/PROSE]]]` block, markers
   included, with two to four paragraphs covering:
   - what this component is responsible for, in the reconstruction pipeline's
     own terms;
   - the load-bearing units — five to ten, named, with one clause each on why
     they matter, as prose and not as a list that duplicates the table;
   - how it connects to its neighbours: which components it leans on and which
     lean on it, and *what flows across* the edge. The dependency tables give
     you the direction and weight; you supply the meaning.
4. Change nothing else on the page. The tables are regenerated from the index.
5. Append one line to `data/batches/component-<name>.jsonl`:

   `{"qname": "component:<name>", "oneliner": "..."}`

   That one-liner becomes the component's row in `book/TOC.md` and in
   `book/indexes/Components.md`. At most about 90 characters, a noun phrase,
   no trailing full stop.

## If your target is `book/TOC.md`

1. Read the `## Overview` of every component page in `book/components/`
   (there are 27; read the overview sections, not whole pages).
2. Replace the `[[[PROSE toc ...]]] ... [[[/PROSE]]]` block, markers included,
   with the "read this first" map of GPlates: four to eight paragraphs that let
   a new developer place any file they open.

   Cover, in this order: what GPlates is and what it computes; the feature and
   property data model and the GPGIM that types it; how a reconstruction is
   produced — rotation files to plate circuit to `ReconstructionTree` to layers
   and their lazily-evaluated layer proxies; how results become rendered
   geometry and reach the globe and map; where the Qt widgets, the Python
   bindings and the serialisation framework sit around that spine; and which
   components a newcomer should read first.

   Name real types and components. Link to component pages with relative links
   of the form `[app-logic](components/app-logic.md)`.
3. Change nothing else on the page.
4. Write nothing to `data/batches/` — the TOC has no one-liner.

## Prose rules — the same ones the unit pages follow

- Explain purpose, design intent and non-obvious behaviour. Nothing else.
- Never restate what the tables already show.
- Never speculate. Every claim must trace to a page you read or code you read.
- Plain Markdown prose: no headings, no tables, at most one short list.

## Report

Your final message is the return value. Emit one line:

```
<page path>: written
```

and nothing else, or a one-line reason if you could not finish.

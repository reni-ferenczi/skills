# ScribeExportPyGPlates

[Book TOC](../../TOC.md) · [entry-points](../../components/entry-points.md) · cluster Community 16 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/ScribeExportPyGPlates.cc` | C++ | 44 |

## Overview

[[[PROSE overview unit=entry-points/ScribeExportPyGPlates tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `SCRIBE_EXPORT_PYGPLATES` | macro | `SCRIBE_EXPORT_EXTERNAL` | Group all classes/types to be scribe export registered for the 'pygplates' dynamic/shared library. |

## Notes

[[[PROSE notes unit=entry-points/ScribeExportPyGPlates tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/ScribeExportPyGPlates.cc
```

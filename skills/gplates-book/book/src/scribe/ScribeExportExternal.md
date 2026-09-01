# ScribeExportExternal

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 16 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeExportExternal.h` | C++ | 93 |

## Overview

[[[PROSE overview unit=scribe/ScribeExportExternal tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBEEXPORTEXTERNAL_H` | macro | `None` | — |
| `SCRIBE_EXPORT_EXTERNAL` | macro | `((char, "char")) \ ((signed char, "signed char")) \ ((unsigned char, "unsigned char")) \ \ ((short, "short")) \ ((unsigned short, "unsigned short")) \ \ ((int, "int")) \ ((unsigned ...` | Scribe export registered classes/types for \*external\* libraries. |

## Notes

[[[PROSE notes unit=scribe/ScribeExportExternal tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [entry-points/ScribeExportGPlates](../entry-points/ScribeExportGPlates.md) | entry-points | 1 |
| [entry-points/ScribeExportGPlatesDemoNoGui](../entry-points/ScribeExportGPlatesDemoNoGui.md) | entry-points | 1 |
| [entry-points/ScribeExportGPlatesUnitTest](../entry-points/ScribeExportGPlatesUnitTest.md) | entry-points | 1 |
| [entry-points/ScribeExportPyGPlates](../entry-points/ScribeExportPyGPlates.md) | entry-points | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeExportExternal.h
```

# ScribeExportGPlates

[Book TOC](../../TOC.md) · [entry-points](../../components/entry-points.md) · cluster Community 16 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/ScribeExportGPlates.cc` | C++ | 47 |

## Overview

Defines the set of polymorphic classes and types that the Scribe serialization framework will register as available for transcription in the main GPlates application. The macro combines type export groups from the `data-mining` module with external types, then registers them all at compile time so they can be serialized and deserialized when GPlates saves and loads projects.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `SCRIBE_EXPORT_GPLATES` | macro | `SCRIBE_EXPORT_DATA_MINING \ SCRIBE_EXPORT_EXTERNAL` | Group all classes/types to be scribe export registered for the 'gplates' program. |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/ScribeExportGPlates.cc
```

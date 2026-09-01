# ScribeExportPyGPlates

[Book TOC](../../TOC.md) · [entry-points](../../components/entry-points.md) · cluster Community 16 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/ScribeExportPyGPlates.cc` | C++ | 44 |

## Overview

Defines the set of polymorphic classes and types that the Scribe serialization framework will register as available for transcription in the pyGPlates dynamic library. The macro registers external types, enabling Python scripts using the pyGPlates extension module to load and save project files through the serialization framework.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `SCRIBE_EXPORT_PYGPLATES` | macro | `SCRIBE_EXPORT_EXTERNAL` | Group all classes/types to be scribe export registered for the 'pygplates' dynamic/shared library. |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/ScribeExportPyGPlates.cc
```

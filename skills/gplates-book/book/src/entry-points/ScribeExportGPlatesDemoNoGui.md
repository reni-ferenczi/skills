# ScribeExportGPlatesDemoNoGui

[Book TOC](../../TOC.md) · [entry-points](../../components/entry-points.md) · cluster Community 16 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/ScribeExportGPlatesDemoNoGui.cc` | C++ | 44 |

## Overview

Defines the set of polymorphic classes and types that the Scribe serialization framework will register as available for transcription in the headless GPlates demo application. The macro registers external types only, which the demo application needs to load and save project files, but excludes data-mining types which are not used by the demo.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `SCRIBE_EXPORT_GPLATES_DEMO_NO_GUI` | macro | `SCRIBE_EXPORT_EXTERNAL` | Group all classes/types to be scribe export registered for the 'gplates-demo-no-gui' program. |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/ScribeExportGPlatesDemoNoGui.cc
```

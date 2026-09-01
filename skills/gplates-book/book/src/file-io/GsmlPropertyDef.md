# GsmlPropertyDef

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1413 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GsmlPropertyDef.h` | C++ | 144 |

## Overview

[[[PROSE overview unit=file-io/GsmlPropertyDef tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::PropertyInfo`](#gplatesfileiopropertyinfo) | struct | — | — | 0 | Add new property support. |

## Members

### `GPlatesFileIO::PropertyInfo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `name` | field | `char` | public | — |
| `query` | field | `char` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_GSMLPROPERTYDEF_H` | macro | `None` | — |
| `GeometryProperty` | variable | `PropertyInfo` | geometry property |
| `ObservationMethodProperty` | variable | `PropertyInfo` | observation method property |
| `OccurrenceGeometryProperty` | variable | `PropertyInfo` | occurrence geometry property |
| `GmlName` | variable | `PropertyInfo` | gml name property |
| `GmlDesc` | variable | `PropertyInfo` | gml description property |
| `GmlValidTime` | variable | `PropertyInfo` | gml validTime property |
| `GpmlValidTimeRange` | variable | `PropertyInfo` | gml validTime property |
| `GpmlRockType` | variable | `PropertyInfo` | Props for RockUnit\_\* types from Macrosrtat |
| `GpmlRockMaxThick` | variable | `PropertyInfo` | — |
| `GpmlRockMinThick` | variable | `PropertyInfo` | — |
| `GpmlFossilDiversity` | variable | `PropertyInfo` | Props for FossilCollection\_\* types from Macrosrtat |

## Notes

[[[PROSE notes unit=file-io/GsmlPropertyDef tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GsmlFeaturesDef](GsmlFeaturesDef.md) | file-io | 37 |
| [file-io/GsmlNodeProcessorFactory](GsmlNodeProcessorFactory.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GsmlPropertyDef.h
python scripts/gpq.py def GPlatesFileIO::PropertyInfo --body
python scripts/gpq.py uses PropertyInfo --kind struct
python scripts/gpq.py hier PropertyInfo
```

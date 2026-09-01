# GsmlPropertyDef

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1413 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GsmlPropertyDef.h` | C++ | 144 |

## Overview

This header is the property table for GPlates' GeoSciML (GSML) reader: each
`PropertyInfo` constant pairs an XPath-like query string with the
`GsmlPropertyHandlers` member function that parses the matched element into
GPML property values. `GsmlNodeProcessorFactory` and `GsmlFeaturesDef` build
their per-feature-type property lists by referencing these constants, so
adding support for a new GSML property is a matter of declaring one more
`PropertyInfo` here (as the comment above `PropertyInfo` spells out) and
wiring it into the callback list in `GsmlFeaturesDef.h`.

The queries themselves are simple, single-purpose XPath fragments (`//gml:name`,
`//gsml:shape`, `//gpml:rock_type`, …) rather than a general query language;
`GmlValidTime` and `GpmlValidTimeRange` both carry the description "gml
validTime property" even though they target different elements, reflecting
that the two were added for related but distinct GSML profiles (MapUnits and
Macrostrat rock units).

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

Every `PropertyInfo` here is a file-scope `static const` object, so each
translation unit that includes this header gets its own copy; the constants
are meant to be read, never mutated, and compared only by the handler pointer
or query string.

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

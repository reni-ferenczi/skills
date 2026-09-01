# ScalarCoverageStatistics

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 399 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/ScalarCoverageStatistics.h` | C++ | 57 |

## Overview

`ScalarCoverageStatistics` is a plain aggregate of the four summary values (`minimum`, `maximum`, `mean`, `standard_deviation`) computed over the per-point scalar values of one or more scalar coverages — geometries (points, lines, polygons) that carry a scalar value at each point, such as crustal thickness or age at reconstructed points. Unlike the analogous `RasterStatistics`, all four fields are required, non-optional `double`s, reflecting that these statistics are always computed on demand from an in-memory scalar coverage rather than read (possibly incompletely) from a raster file format.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::ScalarCoverageStatistics`](#gplatespropertyvaluesscalarcoveragestatistics) | struct | — | — | 0 | Contains statistics about one or more scalar coverages (geometries with per-point scalar values). |

## Members

### `GPlatesPropertyValues::ScalarCoverageStatistics`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ScalarCoverageStatistics( const double &minimum_, const double &maximum_, const double &mean_, const double &standard_deviation_)` | constructor | `None` | public | — |
| `minimum` | field | `double` | public | — |
| `maximum` | field | `double` | public | — |
| `mean` | field | `double` | public | — |
| `standard_deviation` | field | `double` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_SCALARCOVERAGESTATISTICS_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructScalarCoverageLayerParams](../app-logic/ReconstructScalarCoverageLayerParams.md) | app-logic | 26 |
| [presentation/ReconstructScalarCoverageVisualLayerParams](../presentation/ReconstructScalarCoverageVisualLayerParams.md) | presentation | 11 |
| [qt-widgets/ReconstructScalarCoverageLayerOptionsWidget](../qt-widgets/ReconstructScalarCoverageLayerOptionsWidget.md) | qt-widgets | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/ScalarCoverageStatistics.h
python scripts/gpq.py def GPlatesPropertyValues::ScalarCoverageStatistics --body
python scripts/gpq.py uses ScalarCoverageStatistics --kind struct
python scripts/gpq.py hier ScalarCoverageStatistics
```

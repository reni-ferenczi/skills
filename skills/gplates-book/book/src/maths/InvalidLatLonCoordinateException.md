# InvalidLatLonCoordinateException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 541 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/InvalidLatLonCoordinateException.h` | C++ | 112 |
| `src/maths/InvalidLatLonCoordinateException.cc` | C++ | 39 |

## Overview

`InvalidLatLonCoordinateException` reports a single bad coordinate found while
converting a flat sequence of doubles into (lat, lon) pairs — the situation
that arises when geometry is built from externally supplied coordinate data
(digitised points, imported files, reconstructed geometry) rather than
constructed programmatically with already-valid values. Unlike the plain
`FunctionDomainException`, it derives from
`GPlatesGlobal::ExternalResourceFailureException`, classing an invalid
coordinate as a data-input problem rather than an internal maths-invariant
violation, which matters for how callers decide whether to catch and report
it versus let it propagate as a bug.

It carries enough detail for a caller or error dialog to pinpoint the problem
precisely: the offending value (`invalid_coord()`), whether it was the
latitude or longitude half of the pair (`coordinate_type()`, a
`LatitudeCoord`/`LongitudeCoord` enum), and the index of the pair within the
input sequence (`coord_index()`). `write_message()` composes these into a
single diagnostic line such as "invalid latitude coordinate 132.5 at index 3
in sequence".

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::InvalidLatLonCoordinateException`](#gplatesmathsinvalidlatloncoordinateexception) | class | [`GPlatesGlobal::ExternalResourceFailureException`](../global/ExternalResourceFailureException.md) | — | 0 | This is the exception thrown when a sequence of doubles, whose elements are to be paired into (lat, lon) coordinate-pairs, contains an invalid latitude coordinate or an invalid longitude coordinate. |

## Members

### `GPlatesMaths::InvalidLatLonCoordinateException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `size_type` | typedef | `unsigned long` | public | — |
| `CoordinateType` | enum | `None` | public | — |
| `InvalidLatLonCoordinateException( const GPlatesUtils::CallStack::Trace &exception_source, const double &invalid_coord_, CoordinateType coordinate_type_, size_type coord_index_)` | constructor | `None` | public | a longitude coord. |
| `~InvalidLatLonCoordinateException()` | destructor | `None` | public | — |
| `coordinate_type()` | method | `CoordinateType` | public | — |
| `coord_index()` | method | `size_type` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_invalid_coord` | field | `double` | private | — |
| `d_coordinate_type` | field | `CoordinateType` | private | — |
| `d_coord_index` | field | `size_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_INVALIDLATLONCOORDINATEEXCEPTION_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ResolvedTopologicalSubSegmentImpl](../app-logic/ResolvedTopologicalSubSegmentImpl.md) | app-logic | 7 |
| [maths/PointOnSphere](PointOnSphere.md) | maths | 7 |
| [opengl/GLReconstructedStaticPolygonMeshes](../opengl/GLReconstructedStaticPolygonMeshes.md) | opengl | 3 |
| [view-operations/GeometryBuilder](../view-operations/GeometryBuilder.md) | view-operations | 3 |
| [app-logic/ReconstructedFeatureGeometryFinder](../app-logic/ReconstructedFeatureGeometryFinder.md) | app-logic | 1 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 1 |
| [maths/PolygonPartitioner](PolygonPartitioner.md) | maths | 1 |
| [maths/PolylineOnSphere](PolylineOnSphere.md) | maths | 1 |
| [maths/deprecated/PolylineIntersections_test](deprecated/PolylineIntersections_test.md) | maths | 1 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](../opengl/GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 1 |
| [qt-widgets/DigitisationWidget](../qt-widgets/DigitisationWidget.md) | qt-widgets | 1 |
| [qt-widgets/LatLonCoordinatesTable](../qt-widgets/LatLonCoordinatesTable.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/InvalidLatLonCoordinateException.h
python scripts/gpq.py def GPlatesMaths::InvalidLatLonCoordinateException --body
python scripts/gpq.py uses InvalidLatLonCoordinateException --kind class
python scripts/gpq.py hier InvalidLatLonCoordinateException
```

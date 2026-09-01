# InvalidLatLonCoordinateException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 541 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/InvalidLatLonCoordinateException.h` | C++ | 112 |
| `src/maths/InvalidLatLonCoordinateException.cc` | C++ | 39 |

## Overview

[[[PROSE overview unit=maths/InvalidLatLonCoordinateException tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/InvalidLatLonCoordinateException tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

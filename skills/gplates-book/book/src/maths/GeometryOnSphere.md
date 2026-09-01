# GeometryOnSphere

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1560 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/GeometryOnSphere.h` | C++ | 112 |

## Overview

[[[PROSE overview unit=maths/GeometryOnSphere tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::GeometryOnSphere`](#gplatesmathsgeometryonsphere) | class | [`GPlatesUtils::ReferenceCount<GeometryOnSphere>`](../utils/ReferenceCount.md) | — | 4 | This class is the abstract base of all geometries on the sphere. |

## Members

### `GPlatesMaths::GeometryOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GeometryOnSphere>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GeometryOnSphere\>. |
| `maybe_null_ptr_to_const_type` | typedef | `boost::intrusive_ptr<const GeometryOnSphere>` | public | A convenience typedef for boost::intrusive\_ptr\<const GeometryOnSphere\>. |
| `~GeometryOnSphere()` | destructor | `None` | public | — |
| `test_proximity( const ProximityCriteria &criteria)` | method | `ProximityHitDetail::maybe_null_ptr_type` | public | Test for a proximity hit. |
| `test_vertex_proximity( const ProximityCriteria &criteria)` | method | `ProximityHitDetail::maybe_null_ptr_type` | public | Test for a proximity hit, but only on the vertices of the geometry. |
| `accept_visitor( ConstGeometryOnSphereVisitor &visitor)` | method | `void` | public | Accept a ConstGeometryOnSphereVisitor instance. |
| `get_non_null_pointer()` | method | `non_null_ptr_to_const_type` | public | Return this instance as a non-null pointer. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_GEOMETRYONSPHERE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/GeometryOnSphere tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 43 |
| [utils/GeometryCreationUtils](../utils/GeometryCreationUtils.md) | utils | 36 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 33 |
| [maths/GeometryDistance](GeometryDistance.md) | maths | 31 |
| [canvas-tools/CanvasTool](../canvas-tools/CanvasTool.md) | canvas-tools | 30 |
| [maths/PolygonPartitioner](PolygonPartitioner.md) | maths | 29 |
| [maths/PolygonMesh](PolygonMesh.md) | maths | 26 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 22 |
| [feature-visitors/GeometryTypeFinder](../feature-visitors/GeometryTypeFinder.md) | feature-visitors | 21 |
| [app-logic/ScalarCoverageFeatureProperties](../app-logic/ScalarCoverageFeatureProperties.md) | app-logic | 20 |
| [file-io/OgrGeometryExporter](../file-io/OgrGeometryExporter.md) | file-io | 20 |
| [maths/PolygonFan](PolygonFan.md) | maths | 20 |
| [maths/GeometryInterpolation](GeometryInterpolation.md) | maths | 19 |
| [file-io/PlatesLineFormatWriter](../file-io/PlatesLineFormatWriter.md) | file-io | 18 |
| [qt-widgets/LatLonCoordinatesTable](../qt-widgets/LatLonCoordinatesTable.md) | qt-widgets | 17 |
| [app-logic/GeometryCookieCutter](../app-logic/GeometryCookieCutter.md) | app-logic | 16 |
| [canvas-tools/MeasureDistanceState](../canvas-tools/MeasureDistanceState.md) | canvas-tools | 16 |
| [file-io/PlatesLineFormatGeometryExporter](../file-io/PlatesLineFormatGeometryExporter.md) | file-io | 14 |
| [maths/PointOnSphere](PointOnSphere.md) | maths | 14 |
| [app-logic/ResolvedSubSegmentRangeInSection](../app-logic/ResolvedSubSegmentRangeInSection.md) | app-logic | 13 |

*... and 130 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/GeometryOnSphere.h
python scripts/gpq.py def GPlatesMaths::GeometryOnSphere --body
python scripts/gpq.py uses GeometryOnSphere --kind class
python scripts/gpq.py hier GeometryOnSphere
```

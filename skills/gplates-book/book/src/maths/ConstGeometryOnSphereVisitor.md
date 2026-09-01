# ConstGeometryOnSphereVisitor

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1639 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/ConstGeometryOnSphereVisitor.h` | C++ | 125 |

## Overview

[[[PROSE overview unit=maths/ConstGeometryOnSphereVisitor tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::ConstGeometryOnSphereVisitor`](#gplatesmathsconstgeometryonspherevisitor) | class | — | — | 45 | This class defines an abstract interface for a Visitor to visit const geometries on the sphere. |

## Members

### `GPlatesMaths::ConstGeometryOnSphereVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~ConstGeometryOnSphereVisitor()` | destructor | `None` | public | We'll make this function pure virtual so that the class is abstract. |
| `visit_multi_point_on_sphere( MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | public | Override this function in your own derived class. |
| `visit_point_on_sphere( PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | public | Override this function in your own derived class. |
| `visit_polygon_on_sphere( PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | public | Override this function in your own derived class. |
| `visit_polyline_on_sphere( PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | public | Override this function in your own derived class. |
| `operator=` | field | `ConstGeometryOnSphereVisitor` | private | This operator should never be defined, because we don't want to allow copy-assignment. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_CONSTGEOMETRYONSPHEREVISITOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/ConstGeometryOnSphereVisitor tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/MeasureDistanceState](../canvas-tools/MeasureDistanceState.md) | canvas-tools | 18 |
| [file-io/PlatesLineFormatGeometryExporter](../file-io/PlatesLineFormatGeometryExporter.md) | file-io | 11 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 10 |
| [file-io/GMTFormatGeometryExporter](../file-io/GMTFormatGeometryExporter.md) | file-io | 10 |
| [view-operations/FocusedFeatureGeometryManipulator](../view-operations/FocusedFeatureGeometryManipulator.md) | view-operations | 8 |
| [app-logic/ReconstructUtils](../app-logic/ReconstructUtils.md) | app-logic | 7 |
| [maths/GeometryDistance](GeometryDistance.md) | maths | 6 |
| [data-mining/deprecated/IsInRegionOfInterestVisitor](../data-mining/deprecated/IsInRegionOfInterestVisitor.md) | data-mining | 5 |
| [data-mining/deprecated/RegionOfInterestAssociationOperator](../data-mining/deprecated/RegionOfInterestAssociationOperator.md) | data-mining | 5 |
| [maths/CubeQuadTreePartition](CubeQuadTreePartition.md) | maths | 5 |
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 5 |
| [qt-widgets/LatLonCoordinatesTable](../qt-widgets/LatLonCoordinatesTable.md) | qt-widgets | 4 |
| [app-logic/CoRegistrationLayerProxy](../app-logic/CoRegistrationLayerProxy.md) | app-logic | 3 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 3 |
| [maths/MultiPointOnSphere](MultiPointOnSphere.md) | maths | 3 |
| [maths/PointOnSphere](PointOnSphere.md) | maths | 3 |
| [maths/PolygonOnSphere](PolygonOnSphere.md) | maths | 3 |
| [maths/PolylineOnSphere](PolylineOnSphere.md) | maths | 3 |
| [view-operations/GeometryBuilder](../view-operations/GeometryBuilder.md) | view-operations | 3 |
| [view-operations/RenderedGeometryFactory](../view-operations/RenderedGeometryFactory.md) | view-operations | 3 |

*... and 16 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/ConstGeometryOnSphereVisitor.h
python scripts/gpq.py def GPlatesMaths::ConstGeometryOnSphereVisitor --body
python scripts/gpq.py uses ConstGeometryOnSphereVisitor --kind class
python scripts/gpq.py hier ConstGeometryOnSphereVisitor
```

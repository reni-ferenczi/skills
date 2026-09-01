# ConstGeometryOnSphereVisitor

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1639 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/ConstGeometryOnSphereVisitor.h` | C++ | 125 |

## Overview

The abstract Visitor base (Gamma95, p.331) for read-only traversal of the four
concrete geometry-on-sphere types: `MultiPointOnSphere`, `PointGeometryOnSphere`,
`PolygonOnSphere` and `PolylineOnSphere`. Every one of the 45 subclasses this
page lists is a piece of code that needs to act differently depending on
which concrete geometry it is holding — exporters, distance calculations,
canvas tools, region-of-interest tests — without those geometry classes
themselves knowing about all their callers.

Each `visit_*` method has an empty default body, so a derived visitor only
overrides the geometry kinds it cares about. The methods are named after
their target type rather than uniformly `visit`, specifically to dodge C++
name hiding: overriding one `visit_*` in a derived class does not hide the
others the way overriding one overload of a single `visit` name would.

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

The destructor is pure virtual purely to force the class to be abstract —
every other member function already has a body — and is still defined
inline immediately below the class so derived destructors can call it.
Copy-assignment is explicitly declared private and left undefined to
suppress it.

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

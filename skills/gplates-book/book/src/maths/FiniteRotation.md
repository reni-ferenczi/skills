# FiniteRotation

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 463 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/FiniteRotation.h` | C++ | 491 |
| `src/maths/FiniteRotation.cc` | C++ | 664 |

## Overview

[[[PROSE overview unit=maths/FiniteRotation tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::RotateGeometryOnSphere`](#anonymousrotategeometryonsphere) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](ConstGeometryOnSphereVisitor.md) | — | 0 | Visits a GeometryOnSphere, rotates it and returns as a GeometryOnSphere. |
| [`GPlatesMaths::FiniteRotation`](#gplatesmathsfiniterotation) | class | [`GPlatesUtils::QtStreamable<FiniteRotation>`](../utils/QtStreamable.md) | — | 0 | This class represents a so-called "finite rotation" of plate tectonics. |

## Members

### `(anonymous)::RotateGeometryOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RotateGeometryOnSphere( const GPlatesMaths::FiniteRotation &finite_rotation)` | constructor | `None` | public | Construct with the FiniteRotation to use for rotating. |
| `rotate( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry)` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | Rotates geometry using FiniteRotation passed into constructor and returns rotated GeometryOnSphere. |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | protected | — |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | protected | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | protected | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | protected | — |
| `d_finite_rotation` | field | `GPlatesMaths::FiniteRotation` | private | — |
| `d_rotated_geometry` | field | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | private | — |

### `GPlatesMaths::FiniteRotation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create_identity_rotation()` | method | `FiniteRotation` | public | Create an identity rotation. |
| `create( const UnitQuaternion3D &uq, const boost::optional<UnitVector3D> &axis_hint_)` | method | `FiniteRotation` | public | Create a finite rotation corresponding to the rotation effected by the unit quaternion uq. |
| `create( const PointOnSphere &pole, const real_t &angle)` | method | `FiniteRotation` | public | Create a finite rotation with the Euler pole pole and rotation angle angle. |
| `create_great_circle_point_rotation( const PointOnSphere &from_point, const PointOnSphere &to_point)` | method | `FiniteRotation` | public | Create a finite rotation that rotates from from\_point to to\_point along the great circle arc connecting them. |
| `create_small_circle_point_rotation( const PointOnSphere &rotation_pole, const PointOnSphere &from_point, const PointOnSphere &to_point)` | method | `FiniteRotation` | public | Create a finite rotation, using the specified rotation pole, that rotates from\_point to to\_point (or at least rotates from\_point to the same longitude as to\_point with respect to the rotation pole). |
| `create_segment_rotation( const PointOnSphere &from_segment_start, const PointOnSphere &from_segment_end, const PointOnSphere &to_segment_start, const PointOnSphere &to_segment_end)` | method | `FiniteRotation` | public | Create a finite rotation that rotates the \*from\* line segment to the \*to\* line segment. |
| `operator*( const UnitVector3D &unit_vect)` | operator | `UnitVector3D` | public | Apply this rotation to a unit vector unit\_vect. |
| `operator*( const Vector3D &vect)` | operator | `Vector3D` | public | Apply this rotation to a vector vect. |
| `operator==( const FiniteRotation &other)` | operator | `bool` | public | — |
| `operator!=( const FiniteRotation &other)` | operator | `bool` | public | — |
| `FiniteRotation( const UnitQuaternion3D &unit_quat_, const boost::optional<UnitVector3D> &axis_hint_)` | constructor | `None` | protected | — |
| `d_unit_quat` | field | `UnitQuaternion3D` | private | This unit-quaternion is used to effect the rotation operation. |
| `d_axis_hint` | field | `boost::optional<UnitVector3D>` | private | This provides a hint as to what the rotation axis might approx be. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator*( const UnitVector3D &unit_vect)` | operator | `GPlatesMaths::UnitVector3D` | — |
| `operator*( const Vector3D &vect)` | operator | `GPlatesMaths::Vector3D` | — |
| `slerp( const GPlatesMaths::UnitQuaternion3D &q1, const GPlatesMaths::UnitQuaternion3D &q2, const GPlatesMaths::real_t &t)` | function | `GPlatesMaths::UnitQuaternion3D` | — |
| `operator*( const FiniteRotation &r, const GPlatesUtils::non_null_intrusive_ptr<const MultiPointOnSphere> &mp)` | operator | `GPlatesUtils::non_null_intrusive_ptr<const GPlatesMaths::MultiPointOnSphere>` | — |
| `operator*( const FiniteRotation &r, const GPlatesUtils::non_null_intrusive_ptr<const PolylineOnSphere> &p)` | operator | `GPlatesUtils::non_null_intrusive_ptr<const GPlatesMaths::PolylineOnSphere>` | — |
| `operator*( const FiniteRotation &r, const GPlatesUtils::non_null_intrusive_ptr<const PolygonOnSphere> &p)` | operator | `GPlatesUtils::non_null_intrusive_ptr<const GPlatesMaths::PolygonOnSphere>` | — |
| `operator*( const FiniteRotation &r, const GPlatesUtils::non_null_intrusive_ptr<const GeometryOnSphere> &g)` | operator | `GPlatesUtils::non_null_intrusive_ptr<const GPlatesMaths::GeometryOnSphere>` | — |
| `operator*( const FiniteRotation &r, const GreatCircleArc &g)` | operator | `GPlatesMaths::GreatCircleArc` | — |
| `operator*( const FiniteRotation &r, const GreatCircle &g)` | operator | `GPlatesMaths::GreatCircle` | — |
| `operator*( const FiniteRotation &r, const SmallCircle &s)` | operator | `GPlatesMaths::SmallCircle` | — |
| `opt_eq( const boost::optional<T> &opt1, const boost::optional<T> &opt2)` | function | `bool` | — |
| `operator==( const FiniteRotation &other)` | operator | `bool` | — |
| `GPLATES_MATHS_FINITEROTATION_H` | macro | `None` | — |
| `get_reverse( const FiniteRotation &r)` | function | `FiniteRotation` | Calculate the reverse of the given finite rotation r. |
| `interpolate( const FiniteRotation &r1, const FiniteRotation &r2, const real_t &t1, const real_t &t2, const real_t &t_target, const boost::optional<UnitVector3D> &axis_hint)` | function | `FiniteRotation` | Calculate the finite rotation which is the interpolation of the finite rotations r1 and r2 according to the interpolation parameters t1, t2 and t\_target. |
| `interpolate( const FiniteRotation &r1, const FiniteRotation &r2, const real_t &interpolate_ratio)` | function | `FiniteRotation` | Calculate a spatial interpolated rotation between two finite rotations r1 and r2, using the interpolate ratio. interpolate\_ratio is in range \[0, 1\] where 0 represents r1 and 1 represents r2. |
| `interpolate( const FiniteRotation &r1, const FiniteRotation &r2, const FiniteRotation &r3, const real_t &w1, const real_t &w2, const real_t &w3)` | function | `FiniteRotation` | Calculate a spatial interpolated rotation between three finite rotations r1, r2 and r3, using associated barycentric coordinate weights w1, w2 and w3. |
| `compose( const FiniteRotation &r1, const FiniteRotation &r2)` | function | `FiniteRotation` | Compose two FiniteRotations. |
| `compose( const Rotation &r, const FiniteRotation &fr)` | function | `FiniteRotation` | Apply a Rotation to a FiniteRotation. |
| `operator*( const FiniteRotation &r, const PointOnSphere &p)` | operator | `PointOnSphere` | Apply the given rotation to the given point-on-sphere. |
| `operator*( const FiniteRotation &r, const GPlatesUtils::non_null_intrusive_ptr<const PointGeometryOnSphere> &p)` | operator | `GPlatesUtils::non_null_intrusive_ptr<const PointGeometryOnSphere>` | Apply the given rotation to the given intrusive-pointer to point-on-sphere. |
| `operator<<` | variable | `std::ostream` | — |

## Notes

[[[PROSE notes unit=maths/FiniteRotation tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 134 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 114 |
| [maths/GreatCircleArc](GreatCircleArc.md) | maths | 100 |
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 97 |
| [app-logic/RotationUtils](../app-logic/RotationUtils.md) | app-logic | 87 |
| [app-logic/FlowlineUtils](../app-logic/FlowlineUtils.md) | app-logic | 81 |
| [app-logic/TopologyReconstruct](../app-logic/TopologyReconstruct.md) | app-logic | 71 |
| [app-logic/FlowlineGeometryPopulator](../app-logic/FlowlineGeometryPopulator.md) | app-logic | 54 |
| [maths/CubeQuadTreePartition](CubeQuadTreePartition.md) | maths | 51 |
| [app-logic/PlateVelocityUtils](../app-logic/PlateVelocityUtils.md) | app-logic | 50 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 49 |
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 48 |
| [maths/CalculateVelocity](CalculateVelocity.md) | maths | 42 |
| [gui/deprecated/GLCanvas](../gui/deprecated/GLCanvas.md) | gui | 41 |
| [app-logic/ReconstructionTree](../app-logic/ReconstructionTree.md) | app-logic | 36 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 31 |
| [maths/SmallCircleBounds](SmallCircleBounds.md) | maths | 30 |
| [property-values/GpmlFiniteRotation](../property-values/GpmlFiniteRotation.md) | property-values | 30 |
| [app-logic/MotionPathGeometryPopulator](../app-logic/MotionPathGeometryPopulator.md) | app-logic | 29 |
| [app-logic/ResolvedVertexSourceInfo](../app-logic/ResolvedVertexSourceInfo.md) | app-logic | 29 |

*... and 131 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/FiniteRotation.h
python scripts/gpq.py def GPlatesMaths::FiniteRotation --body
python scripts/gpq.py uses FiniteRotation --kind class
python scripts/gpq.py hier FiniteRotation
```

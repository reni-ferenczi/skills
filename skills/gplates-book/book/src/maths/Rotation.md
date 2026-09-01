# Rotation

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 816 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/Rotation.h` | C++ | 329 |
| `src/maths/Rotation.cc` | C++ | 367 |

## Overview

[[[PROSE overview unit=maths/Rotation tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::RotateGeometryOnSphere`](#anonymousrotategeometryonsphere) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](ConstGeometryOnSphereVisitor.md) | — | 0 | Visits a GeometryOnSphere, rotates it and returns as a GeometryOnSphere. |
| [`GPlatesMaths::Rotation`](#gplatesmathsrotation) | class | — | — | 0 | Represents a rotation by a particular angle about a particular axis. |

## Members

### `(anonymous)::RotateGeometryOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RotateGeometryOnSphere( const GPlatesMaths::Rotation &rotation)` | constructor | `None` | public | Construct with the Rotation to use for rotating. |
| `rotate( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry)` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | Rotates geometry using Rotation passed into constructor and returns rotated GeometryOnSphere. |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | protected | — |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | protected | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | protected | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | protected | — |
| `d_rotation` | field | `GPlatesMaths::Rotation` | private | — |
| `d_rotated_geometry` | field | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | private | — |

### `GPlatesMaths::Rotation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( const UnitVector3D &rotation_axis, const real_t &rotation_angle)` | method | `Rotation` | public | Create a rotation with the given rotation axis and rotation angle. |
| `create( const PointOnSphere &initial, const PointOnSphere &final)` | method | `Rotation` | public | Create a rotation which transforms initial to final. |
| `create( const UnitVector3D &initial, const UnitVector3D &final)` | method | `Rotation` | public | Create a rotation which transforms initial to final. |
| `create_identity_rotation()` | method | `Rotation` | public | Create an identity rotation. |
| `get_reverse()` | method | `Rotation` | public | Return the reverse of this rotation. |
| `operator*( const UnitVector3D &uv)` | operator | `UnitVector3D` | public | Apply this rotation to a unit vector. |
| `operator*( const Vector3D &v)` | operator | `Vector3D` | public | Apply this rotation to a (not necessarily unit) vector. |
| `create( const UnitQuaternion3D &uq, const UnitVector3D &rotation_axis, const real_t &rotation_angle)` | method | `Rotation` | protected | Create the rotation described by the supplied quaternion. |
| `Rotation( const UnitVector3D &axis_, const real_t &angle_, const UnitQuaternion3D &quat_)` | constructor | `None` | protected | — |
| `d_axis` | field | `UnitVector3D` | private | The axis of the rotation. |
| `d_angle` | field | `real_t` | private | The angle of the rotation, in radians. |
| `d_quat` | field | `UnitQuaternion3D` | private | The unit quaternion which effects the rotation described by the rotation axis and angle. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator*( const UnitVector3D &uv)` | operator | `GPlatesMaths::UnitVector3D` | — |
| `operator*( const Vector3D &v)` | operator | `GPlatesMaths::Vector3D` | — |
| `operator*( const Rotation &r1, const Rotation &r2)` | operator | `GPlatesMaths::Rotation` | — |
| `operator*( const Rotation &r, const GPlatesUtils::non_null_intrusive_ptr<const MultiPointOnSphere> &mp)` | operator | `GPlatesUtils::non_null_intrusive_ptr<const GPlatesMaths::MultiPointOnSphere>` | — |
| `operator*( const Rotation &r, const GPlatesUtils::non_null_intrusive_ptr<const PolylineOnSphere> &p)` | operator | `GPlatesUtils::non_null_intrusive_ptr<const GPlatesMaths::PolylineOnSphere>` | — |
| `operator*( const Rotation &r, const GPlatesUtils::non_null_intrusive_ptr<const PolygonOnSphere> &p)` | operator | `GPlatesUtils::non_null_intrusive_ptr<const GPlatesMaths::PolygonOnSphere>` | — |
| `operator*( const Rotation &r, const GPlatesUtils::non_null_intrusive_ptr<const GeometryOnSphere> &g)` | operator | `GPlatesUtils::non_null_intrusive_ptr<const GPlatesMaths::GeometryOnSphere>` | — |
| `GPLATES_MATHS_ROTATION_H` | macro | `None` | — |
| `operator*( const Rotation &r, const PointOnSphere &p)` | operator | `PointOnSphere` | Apply the given rotation to the given point-on-sphere. |
| `operator*( const Rotation &r, const GPlatesUtils::non_null_intrusive_ptr<const PointGeometryOnSphere> &p)` | operator | `GPlatesUtils::non_null_intrusive_ptr<const PointGeometryOnSphere>` | Apply the given rotation to the given intrusive-pointer to point-on-sphere. |

## Notes

[[[PROSE notes unit=maths/Rotation tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/SimpleGlobeOrientation](../gui/SimpleGlobeOrientation.md) | gui | 45 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 22 |
| [maths/GeometryInterpolation](GeometryInterpolation.md) | maths | 20 |
| [qt-widgets/FiniteRotationCalculatorDialog](../qt-widgets/FiniteRotationCalculatorDialog.md) | qt-widgets | 16 |
| [qt-widgets/ApplyReconstructionPoleAdjustmentDialog](../qt-widgets/ApplyReconstructionPoleAdjustmentDialog.md) | qt-widgets | 14 |
| [maths/EllipseGenerator](EllipseGenerator.md) | maths | 12 |
| [app-logic/PlateVelocityUtils](../app-logic/PlateVelocityUtils.md) | app-logic | 9 |
| [maths/DateLineWrapper](DateLineWrapper.md) | maths | 8 |
| [gui/SceneLightingParameters](../gui/SceneLightingParameters.md) | gui | 6 |
| [maths/GreatCircleArc](GreatCircleArc.md) | maths | 5 |
| [maths/SmallCircle](SmallCircle.md) | maths | 5 |
| [maths/SmallCircleArc](SmallCircleArc.md) | maths | 5 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 5 |
| [app-logic/GenerateVelocityDomainCitcoms](../app-logic/GenerateVelocityDomainCitcoms.md) | app-logic | 4 |
| [qt-widgets/CalculateReconstructionPoleDialog](../qt-widgets/CalculateReconstructionPoleDialog.md) | qt-widgets | 4 |
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 4 |
| [qt-widgets/MapView](../qt-widgets/MapView.md) | qt-widgets | 4 |
| [app-logic/deprecated/PaleomagUtils](../app-logic/deprecated/PaleomagUtils.md) | app-logic | 3 |
| [maths/FiniteRotation](FiniteRotation.md) | maths | 3 |
| [maths/GeneratePoints](GeneratePoints.md) | maths | 3 |

*... and 15 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/Rotation.h
python scripts/gpq.py def GPlatesMaths::Rotation --body
python scripts/gpq.py uses Rotation --kind class
python scripts/gpq.py hier Rotation
```

# Rotation

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 816 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/Rotation.h` | C++ | 329 |
| `src/maths/Rotation.cc` | C++ | 367 |

## Overview

`Rotation` is a time-independent rigid rotation of the sphere: an axis, an angle in radians, and the
`UnitQuaternion3D` that actually effects them, all three stored together. The header opens with the
warning that matters most — this is *not* the class for plate motion. Reconstruction rotations are
`FiniteRotation` and `StageRotation`, which carry the time semantics and the plate circuit;
`Rotation` is the plain geometric operation, and its callers reflect that: `SimpleGlobeOrientation`
dragging the globe, `EllipseGenerator` and `GeneratePoints` laying out shapes, `DateLineWrapper` and
`GreatCircleArc` moving geometry into a convenient frame.

Two things dominate the design. First, application is deliberately asymmetric premultiplication:
`r * v` reads as "apply r to v", and `r1 * r2` means "take r2, then apply r1", following matrix
convention — the header says so twice, because quaternion multiplication does not commute and
getting the order backwards is a silent error. The vector product is not a matrix multiply either;
`operator*(const Vector3D &)` carries the full derivation in comments and evaluates the quaternion
sandwich in expanded closed form directly from the scalar and vector parts. Second, the family of
free `operator*` overloads makes every geometry type rotatable with the same syntax. Point,
multi-point, polyline and polygon each have their own overload that rotates the vertices and calls
`create` to build a fresh geometry; the `GeometryOnSphere` overload dispatches through
`RotateGeometryOnSphere`, a file-local `ConstGeometryOnSphereVisitor` that picks the right one when
only the base type is known.

The static factories carry the awkward cases. `create(initial, final)` has to invent an axis when
the two unit vectors are collinear and therefore define no unique plane: parallel gives a zero-angle
rotation about `initial`, anti-parallel gives a PI rotation about `generate_perpendicular(initial)`.
Composition has the mirror problem — when the composed quaternion is the identity there is no
meaningful axis, so it reuses `r1`'s; otherwise it asks
`UnitQuaternion3D::get_rotation_params` for axis and angle, passing `r1`'s axis as a hint to
disambiguate the sign. A protected `create` overload takes a quaternion together with a matching
axis and angle so these paths can build a `Rotation` without re-deriving anything.

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

**The quaternion is authoritative; axis and angle are a redundant, non-canonical label.** The
protected `create(uq, axis, angle)` states outright that the supplied axis and angle must match the
quaternion and that this will *not* be checked. Several paths supply an arbitrary-but-deterministic
axis on purpose — the identity cases in `create(initial, final)`, in `create_identity_rotation`
(z-basis) and in `operator*` for composed rotations. Two `Rotation` objects can therefore describe
the same transformation with different `axis()` and `angle()` values, and `get_reverse` inverts the
quaternion while merely negating the stored angle and keeping the same axis. Compare rotations
through `quat()`, never through axis and angle.

**Rotating a `UnitVector3D` re-validates it.** `operator*(const UnitVector3D &)` computes in
`Vector3D` and then constructs a `UnitVector3D` with validity checking on, so if accumulated
floating-point error moves the magnitude-squared away from 1 by more than `Real`'s epsilon the call
throws `ViolatedUnitVectorInvariantException`. Long chains of rotations applied one vector at a time
are the way to provoke this; composing the rotations first and applying once is not.

**Rotated geometries are new objects, built through the normal `create` path.** They are fully
revalidated, and they start with an empty calculation cache — every cached area, centroid, bounding
circle or point-in-polygon structure on the source geometry is lost. The rotation overloads use the
default `check_distinct_points = false`, which is the lenient setting the geometry headers describe
precisely so that rotating a tiny polygon does not throw; the price is that a rotated geometry may
contain degenerate, zero-length segments.

**Adding a `GeometryOnSphere` subclass means editing this file.** `RotateGeometryOnSphere::rotate`
asserts that the visitor produced a result, so an unhandled geometry type fails there — as a thrown
`AssertionFailureException` in release, and via `GPlatesGlobal::Abort` in a debug build.

**`Rotation.h` has a namespace-scope `using namespace GPlatesGlobal;`.** Every translation unit that
includes it, directly or transitively, pulls the whole `GPlatesGlobal` namespace into `GPlatesMaths`.
Bear it in mind when a name resolves somewhere you did not expect.

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

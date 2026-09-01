# FiniteRotation

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 463 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/FiniteRotation.h` | C++ | 491 |
| `src/maths/FiniteRotation.cc` | C++ | 664 |

## Overview

This is the value type that carries plate motion through the whole application:
a rotation about an Euler pole by an angle, stored as a `UnitQuaternion3D`. Every
total reconstruction pole read from a `.rot` file becomes one of these, every
edge of `GPlatesAppLogic::ReconstructionTree` caches one as its composed absolute
rotation, and `GPlatesPropertyValues::GpmlFiniteRotation` wraps one for the
model. It is a small, copyable, immutable value with no default constructor —
you go through the `create*` factories or `create_identity_rotation` — and all
of its interesting operations are non-member functions in `GPlatesMaths`, so
`compose`, `get_reverse` and `interpolate` read like the algebra they implement.

Two decisions in the header are worth understanding before you touch anything.
First, the quaternion is the representation and the pole/angle pair is not
stored, because composition and interpolation are cheap and numerically stable
on quaternions; `compose` is a single quaternion multiply, and `interpolate` is
SLERP over the unit quaternions. `compose(r1, r2)` is premultiplication —
`ReconstructionTree` relies on the documented plate-circuit reading of this
(`r1` one branch root-ward of `r2`), and reversing the arguments silently
produces a different, wrong plate circuit.

Second, `d_axis_hint` exists because the quaternion representation is
*lossy about presentation*: `(axis, angle)` and `(-axis, -angle)` map onto the
identical quaternion, so `UnitQuaternion3D::get_rotation_params` cannot recover
which one the user wrote and always returns the positive-angle variant unless
handed a hint. Carrying the originally supplied axis alongside the quaternion is
what makes a pole displayed in the GUI, or written back to a rotation file, match
what was read in. `compose` propagates whichever operand has a hint (preferring
`r1`), and composing a `Rotation` — the interactive drag case — deliberately
keeps only the `FiniteRotation`'s hint.

Applying a rotation is spread over a family of `operator*` overloads covering
unit vectors, `Vector3D`, `PointOnSphere`, each concrete geometry, and
`GreatCircleArc`, `GreatCircle` and `SmallCircle`. The type-erased overload on
`GeometryOnSphere` is implemented by the file-local visitor
`RotateGeometryOnSphere`, which dispatches to the concrete overload and asserts
that some `visit_*` fired. The vector overload is an expanded quaternion sandwich
written out in the comment block rather than a literal `q v q*`, avoiding the
conjugate multiply; the geometry overloads simply rebuild the geometry
point-by-point, with a standing TODO noting that converting the quaternion to a
3×3 matrix would be cheaper past some number of points.

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

- **`operator==` is not "same rotation".** It compares the quaternions
  component-wise (via `UnitQuaternion3D::operator==`) *and* compares the axis
  hints with `opt_eq`. Since `q` and `-q` effect the identical rotation but
  differ component-wise, and since two rotations can agree while one carries a
  hint and the other does not, unequal here does not mean geometrically
  different. Do not use it as a "has the reconstruction changed" test.
- **`compose` is not commutative and the argument order encodes the plate
  circuit.** See the extended comment on the declaration: if `r1` is M1 relative
  to F1 and `r2` is M2 relative to F2, the result is M2 relative to F1, and M1 is
  expected to be F2. Nothing enforces that.
- **Reading back the pole and angle of an identity rotation throws.**
  `UnitQuaternion3D::get_rotation_params` raises
  `GPlatesGlobal::IndeterminateResultException` for an identity quaternion,
  because the axis is genuinely indeterminate. Guard with
  `represents_identity_rotation`, as `operator<<` does.
- **`interpolate` with `t1 == t2` throws `IndeterminateResultException`**; the
  three-rotation barycentric overload asserts (`PreconditionViolationError`) that
  the weights sum to 1, under `Real`'s epsilon-tolerant equality. Its nested
  SLERPs would divide by zero when `w2 + w3` is zero, but that case is absorbed
  by the `cos_theta >= 1.0` early-out in the file-local `slerp`, which returns
  before touching the interpolation parameter. Preserve that early-out.
- **The SLERP takes the shorter path.** It negates an interpolation coefficient
  (not a quaternion) when the dot product is negative, so interpolating between
  poles more than 180° apart will not travel the long way round.
- **`operator*(const UnitVector3D &)` skips the unit-vector validity check on
  purpose.** It renormalises the result itself when the squared magnitude is not
  within the stricter tolerance and then constructs `UnitVector3D` with
  `check_validity = false`; the comment records that the check otherwise dwarfed
  the quaternion multiply. If you change this path, keep the renormalisation.
- **Rotating a geometry can, in principle, still throw.** The polyline and
  polygon overloads call `create` with `check_distinct_points` left at its
  default of `false` precisely so that rotating a very small geometry does not
  raise `InvalidPointsFor…ConstructionError` on points that collapse together
  numerically. Insufficient *total* points is still an error.
- **`RotateGeometryOnSphere` asserts rather than silently ignoring a new geometry
  type.** Because `ConstGeometryOnSphereVisitor`'s `visit_*` functions have empty
  default bodies, a fifth `GeometryOnSphere` subclass would leave
  `d_rotated_geometry` unset; the `GPlatesGlobal::Assert` in `rotate` turns that
  into an `AssertionFailureException` instead of a wrong answer.
- Instances are plain values with no reference counting and no shared state, so
  they are safe to copy between threads; note that `RotateGeometryOnSphere` holds
  the `FiniteRotation` **by reference**, so it must not outlive the rotation it
  was constructed from.

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

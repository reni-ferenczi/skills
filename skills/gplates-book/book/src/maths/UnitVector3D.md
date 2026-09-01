# UnitVector3D

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 799 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/UnitVector3D.h` | C++ | 379 |
| `src/maths/UnitVector3D.cc` | C++ | 232 |

## Overview

The type that carries the sphere. A position on the globe is a direction from
its centre, so `PointOnSphere` is a `UnitVector3D` and so are the small-circle
centres in `SmallCircleBounds`, the rotation axes in `UnitQuaternion3D` and
`Rotation`, and the cube-face frames in `CubeCoordinateFrame`. The class exists
to make "this really is unit length" a type-level guarantee instead of a
convention, so that downstream code can treat a dot product as a cosine and feed
it straight to `acos` without checking anything.

The enforcement is more forgiving than the Doxygen suggests, and the detail
matters. `check_validity()` runs three stages: it throws
`ViolatedUnitVectorInvariantException` if the squared magnitude differs from 1
by more than `EPSILON` (1.0e-12, via `real_t`'s tolerant `!=`); it then clamps
each component into `[-1, 1]`; and it then *silently renormalises* if the
squared magnitude still deviates by more than 1.0e-13. So construction
self-corrects inside a band and is fatal outside it, and a constructed instance
is closer to unit length than the acceptance threshold alone would imply. The
clamping step is what makes the components safe as arguments to `acos`/`asin`,
whose `Real` versions throw `FunctionDomainException` outside `[-1, 1]`.

Both constructors take a `check_validity_` flag that skips all of this. The
header's own guidance is to pass `false` only where the caller can prove the
result is unit — its worked example is negating components of an existing unit
vector. `Vector3D::get_normalisation()` is the normal way in from unconstrained
components; the free operators delegate to the same `GenericVectorOps3D`
templates `Vector3D` uses, and `UnitVector3D.h` and `Vector3D.h` include each
other in the ordering described on the `Vector3D` page.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::UnitVector3D`](#gplatesmathsunitvector3d) | class | [`GPlatesUtils::QtStreamable<UnitVector3D>`](../utils/QtStreamable.md) | — | 0 | A three-dimensional unit vector. |

## Members

### `GPlatesMaths::UnitVector3D`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnitVector3D( const real_t &x_comp, const real_t &y_comp, const real_t &z_comp, bool check_validity_ = true)` | constructor | `None` | public | Create a 3D vector from the specified x, y and z components. |
| `UnitVector3D( const Vector3D &v, bool check_validity_ = true)` | constructor | `None` | public | Construct using a Vector3D. |
| `~UnitVector3D()` | destructor | `None` | public | — |
| `xBasis()` | method | `UnitVector3D` | public | — |
| `yBasis()` | method | `UnitVector3D` | public | — |
| `zBasis()` | method | `UnitVector3D` | public | — |
| `check_validity()` | method | `void` | private | Assert the class invariant. |
| `d_x` | field | `real_t` | private | — |
| `d_y` | field | `real_t` | private | — |
| `d_z` | field | `real_t` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_MATHS_UNITVECTOR3D_H_` | macro | `None` | — |
| `dot( const UnitVector3D &u1, const UnitVector3D &u2)` | function | `real_t` | — |
| `dot( const UnitVector3D &u1, const Vector3D &u2)` | function | `real_t` | — |
| `dot( const Vector3D &u1, const UnitVector3D &u2)` | function | `real_t` | — |
| `operator==( const UnitVector3D &u1, const UnitVector3D &u2)` | operator | `bool` | — |
| `operator!=( const UnitVector3D &u1, const UnitVector3D &u2)` | operator | `bool` | — |
| `perpendicular( const UnitVector3D &u1, const UnitVector3D &u2)` | function | `bool` | — |
| `parallel( const UnitVector3D &u, const Vector3D &v)` | function | `bool` | — |
| `unit_vectors_are_parallel( const UnitVector3D &u1, const UnitVector3D &u2)` | function | `bool` | Evaluate whether the unit-vectors v1 and v2 are parallel. |
| `unit_vectors_are_antiparallel( const UnitVector3D &u1, const UnitVector3D &u2)` | function | `bool` | Evaluate whether the unit-vectors v1 and v2 are antiparallel. |
| `collinear( const UnitVector3D &s1, const UnitVector3D &s2)` | function | `bool` | — |
| `operator-( const UnitVector3D &u)` | operator | `UnitVector3D` | — |
| `operator*( const real_t &s, const UnitVector3D &u)` | operator | `Vector3D` | — |
| `operator*( const UnitVector3D &u, const real_t &s)` | operator | `Vector3D` | — |
| `generate_perpendicular( const UnitVector3D &u)` | function | `UnitVector3D` | Given the unit vector u, generate a unit vector perpendicular to it. |
| `operator<<` | variable | `std::ostream` | — |
| `cross( const UnitVector3D &u1, const UnitVector3D &u2)` | function | `Vector3D` | — |
| `cross( const UnitVector3D &u, const Vector3D &v)` | function | `Vector3D` | — |
| `cross( const Vector3D &v, const UnitVector3D &u)` | function | `Vector3D` | — |

## Notes

**Equality is angular, not componentwise.** `operator==` is `dot(u1, u2) >= 1.0`
under `real_t`'s tolerance, which unfolds to `1 - dot <= 1e-12`; since
`1 - cos θ ≈ θ²/2`, two unit vectors compare equal out to roughly 1.4e-6
radians of separation — around a metre on the Earth's surface, and vastly looser
than the componentwise `EPSILON` test `Vector3D::operator==` performs. Watch for
this when a template or an algorithm is written against both types.
`unit_vectors_are_parallel` is literally the same expression as `operator==`,
and `unit_vectors_are_antiparallel` is its `<= -1.0` mirror.

**`operator-` is not free.** Negation routes through
`GenericVectorOps3D::negate`, which calls the three-argument constructor and so
takes the default `check_validity_ = true` — the full validate-clamp-renormalise
pass runs on every negation, which is precisely the case the constructor's own
comment offers as an example of when to skip validation. If negation shows up in
a profile, that is why.

**Assignment skips validation.** `operator=` copies the three components with no
check and carries a standing `FIXME: Check for accumulated magnitude errs.`
There is no drift in a plain copy, but there is also no self-correction, so an
instance built with `check_validity_ = false` propagates unchecked.

**Cross products widen.** `cross()` returns `Vector3D`, not `UnitVector3D`, for
both unit arguments — correct, since the cross of two unit vectors is only unit
when they are orthogonal. Callers that want a unit result must call
`get_normalisation()`, which will throw for collinear inputs.
`generate_perpendicular()` avoids that by choosing the basis vector with the
smallest `|dot|` (the "most perpendicular" one) before crossing, so the result
is never degenerate; the reasoning is spelled out at length in the `.cc`.

**Other.** `xBasis()`, `yBasis()` and `zBasis()` construct function-local statics
and return them by value, so callers get independent copies. Instances are plain
values with no lazily cached state — const use is thread-safe.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 118 |
| [maths/GeometryDistance](GeometryDistance.md) | maths | 104 |
| [opengl/GLIntersectPrimitives](../opengl/GLIntersectPrimitives.md) | opengl | 84 |
| [maths/PointInPolygon](PointInPolygon.md) | maths | 80 |
| [opengl/GLMultiResolutionRaster](../opengl/GLMultiResolutionRaster.md) | opengl | 70 |
| [maths/CubeCoordinateFrame](CubeCoordinateFrame.md) | maths | 68 |
| [maths/SphericalSubdivision](SphericalSubdivision.md) | maths | 59 |
| [maths/Centroid](Centroid.md) | maths | 50 |
| [maths/DateLineWrapper](DateLineWrapper.md) | maths | 39 |
| [maths/GnomonicProjection](GnomonicProjection.md) | maths | 37 |
| [maths/GeometryInterpolation](GeometryInterpolation.md) | maths | 31 |
| [maths/GreatCircleArc](GreatCircleArc.md) | maths | 29 |
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 29 |
| [maths/Rotation](Rotation.md) | maths | 28 |
| [maths/Vector3D](Vector3D.md) | maths | 26 |
| [gui/SceneLightingParameters](../gui/SceneLightingParameters.md) | gui | 25 |
| [maths/SmallCircleBounds](SmallCircleBounds.md) | maths | 25 |
| [maths/UnitQuaternion3D](UnitQuaternion3D.md) | maths | 25 |
| [maths/GreatCircle](GreatCircle.md) | maths | 20 |
| [maths/deprecated/GridOnSphere](deprecated/GridOnSphere.md) | maths | 20 |

*... and 62 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/UnitVector3D.h
python scripts/gpq.py def GPlatesMaths::UnitVector3D --body
python scripts/gpq.py uses UnitVector3D --kind class
python scripts/gpq.py hier UnitVector3D
```

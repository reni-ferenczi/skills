# UnitVector3D

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 799 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/UnitVector3D.h` | C++ | 379 |
| `src/maths/UnitVector3D.cc` | C++ | 232 |

## Overview

[[[PROSE overview unit=maths/UnitVector3D tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/UnitVector3D tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

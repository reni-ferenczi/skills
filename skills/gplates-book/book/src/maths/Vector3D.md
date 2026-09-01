# Vector3D

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1079 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/Vector3D.h` | C++ | 321 |
| `src/maths/Vector3D.cc` | C++ | 82 |

## Overview

[[[PROSE overview unit=maths/Vector3D tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::Vector3D`](#gplatesmathsvector3d) | class | [`GPlatesUtils::QtStreamable<Vector3D>`](../utils/QtStreamable.md) | — | 0 | A three-dimensional vector. |

## Members

### `GPlatesMaths::Vector3D`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Vector3D()` | constructor | `None` | public | Zero vector. |
| `Vector3D( const real_t& x_, const real_t& y_, const real_t& z_)` | constructor | `None` | public | Create a 3D vector from the specified x, y and z components. |
| `Vector3D( const UnitVector3D &u)` | constructor | `None` | public | — |
| `~Vector3D()` | destructor | `None` | public | — |
| `magSqrd()` | method | `real_t` | public | Returns the square of the magnitude; that is, \\f$ ( x^2 + y^2 + z^2 ) \\f$ |
| `magnitude()` | method | `real_t` | public | Returns the magnitude of the vector; that is, \\f$ \\sqrt{x^2 + y^2 + z^2} \\f$ |
| `is_zero_magnitude()` | method | `bool` | public | Returns true if the magnitude is zero, or close enough to zero that get\_normalisation would throw UnableToNormaliseZeroVectorException. |
| `get_normalisation()` | method | `UnitVector3D` | public | Generate a vector having the same direction as this, but which has unit magnitude. |
| `d_x` | field | `real_t` | protected | — |
| `d_y` | field | `real_t` | protected | — |
| `d_z` | field | `real_t` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_MATHS_VECTOR3D_H_` | macro | `None` | — |
| `dot( const Vector3D &v1, const Vector3D &v2)` | function | `real_t` | — |
| `operator==( const Vector3D &v1, const Vector3D &v2)` | operator | `bool` | — |
| `operator!=( const Vector3D &v1, const Vector3D &v2)` | operator | `bool` | — |
| `operator-( const Vector3D &v)` | operator | `Vector3D` | — |
| `operator*( const real_t &s, const Vector3D &v)` | operator | `Vector3D` | — |
| `operator*( const Vector3D &v, const real_t &s)` | operator | `Vector3D` | — |
| `operator+( const Vector3D &v1, const Vector3D &v2)` | operator | `Vector3D` | — |
| `operator-( const Vector3D &v1, const Vector3D &v2)` | operator | `Vector3D` | — |
| `operator<<` | variable | `std::ostream` | — |
| `parallel( const Vector3D &v1, const Vector3D &v2)` | function | `bool` | This algorithm for testing whether two vectors are parallel is intended to remove the requirements that: - the magnitudes of the vectors are already known - any of the components are non-zero. |
| `perpendicular( const Vector3D &v1, const Vector3D &v2)` | function | `bool` | Test whether two vectors are perpendicular. |
| `collinear( const Vector3D &v1, const Vector3D &v2)` | function | `bool` | This algorithm for testing whether two vectors are collinear (ie. parallel or antiparallel) is intended to remove the requirements that: - the magnitudes of the vectors are already known - any of the components are non-zero. |
| `cross( const Vector3D &v1, const Vector3D &v2)` | function | `Vector3D` | Returns cross product of two vectors. |

## Notes

[[[PROSE notes unit=maths/Vector3D tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/GeometryIntersect](GeometryIntersect.md) | maths | 60 |
| [opengl/GLMultiResolutionRaster](../opengl/GLMultiResolutionRaster.md) | opengl | 20 |
| [maths/CartesianConvMatrix3D](CartesianConvMatrix3D.md) | maths | 17 |
| [maths/GeometryInterpolation](GeometryInterpolation.md) | maths | 14 |
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 12 |
| [maths/GreatCircleArc](GreatCircleArc.md) | maths | 10 |
| [maths/PointInPolygon](PointInPolygon.md) | maths | 10 |
| [opengl/GLCubeSubdivision](../opengl/GLCubeSubdivision.md) | opengl | 10 |
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 9 |
| [maths/FiniteRotation](FiniteRotation.md) | maths | 9 |
| [app-logic/NetRotationUtils](../app-logic/NetRotationUtils.md) | app-logic | 7 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 7 |
| [maths/SphericalSubdivision](SphericalSubdivision.md) | maths | 6 |
| [maths/UnitVector3D](UnitVector3D.md) | maths | 6 |
| [app-logic/TopologyReconstruct](../app-logic/TopologyReconstruct.md) | app-logic | 5 |
| [maths/GreatCircle](GreatCircle.md) | maths | 5 |
| [maths/Centroid](Centroid.md) | maths | 4 |
| [maths/SmallCircle](SmallCircle.md) | maths | 4 |
| [opengl/GLIntersectPrimitives](../opengl/GLIntersectPrimitives.md) | opengl | 4 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 4 |

*... and 35 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/Vector3D.h
python scripts/gpq.py def GPlatesMaths::Vector3D --body
python scripts/gpq.py uses Vector3D --kind class
python scripts/gpq.py hier Vector3D
```

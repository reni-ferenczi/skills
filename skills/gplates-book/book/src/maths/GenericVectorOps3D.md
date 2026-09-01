# GenericVectorOps3D

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 261 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/GenericVectorOps3D.h` | C++ | 111 |

## Overview

This header-only namespace holds the single implementation of 3-D vector
arithmetic shared by `GPlatesMaths::Vector3D` and `GPlatesMaths::UnitVector3D`.
Neither of those classes computes a dot or cross product itself; their free
`dot`, `cross`, `perpendicular`, `parallel`, `operator-` and `operator*`
overloads — including the mixed unit/non-unit combinations — all forward here.
That is the whole point of the unit: `Vector3D` and `UnitVector3D` share no base
class (a unit vector is deliberately *not* a vector, because it must never
inherit an operation that could break its magnitude-1 invariant), so the common
arithmetic has to live somewhere neutral. The templates are duck-typed: any type
with `x()`, `y()` and `z()` returning `real_t` works, which is why they are
reused unchanged for both operand types and for pairs mixing the two.

`ReturnType<R>` exists because the result type of `cross` and `scale` cannot be
deduced from the arguments and is not the same as either of them. The cross
product of two `UnitVector3D`s is a `Vector3D`, not a unit vector — its
magnitude is the sine of the angle between the operands, so it is only unit
length when they happen to be orthogonal — and scaling a unit vector likewise
leaves the unit-vector type. Wrapping the two operations in a struct templated
on the result lets each caller name the type it wants; `UnitVector3D.cc` and
`Vector3D.cc` both instantiate `ReturnType<Vector3D>`.

The function bodies are written the way they are for a measured reason, recorded
in the comments: they unwrap `real_t` to raw `double` via `dval()` and avoid
temporaries, which the author measured as 41 instructions down to 12 for `dot`
and 89 down to 29 for `cross`, and which lets the compiler inline them. These
are the innermost operations of the whole spherical-geometry layer — great-circle
arc construction, point-in-polygon tests, bounding small circles — so a
well-meant rewrite in terms of `real_t` operators would be a measurable
regression.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::GenericVectorOps3D::ReturnType`](#gplatesmathsgenericvectorops3dreturntype) | struct | — | `< typename R >` | 0 | — |

## Members

### `GPlatesMaths::GenericVectorOps3D::ReturnType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `cross( const V1 &v1, const V2 &v2)` | method | `R` | public | — |
| `scale( const real_t s, const V v)` | method | `R` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_GENERICVECTOROPS3D_H` | macro | `None` | — |
| `dot( const V1 &v1, const V2 &v2)` | function | `real_t` | — |
| `negate( const V &v)` | function | `V` | — |
| `perpendicular( const V1 &v1, const V2 &v2)` | function | `bool` | — |

## Notes

- **`perpendicular` is a tolerance test, not an exact one.** It reads
  `abs(dot(v1, v2)) <= 0.0`, but the comparison is `GPlatesMaths::Real`'s, whose
  `operator<` is `r2 - r1 > EPSILON`. So it answers "is the dot product within
  `EPSILON` of zero", which is what makes it usable at all on floating-point
  data.
- **That tolerance is absolute, so it is only meaningful for unit vectors.** The
  dot product of two `Vector3D`s scales with both magnitudes, so a fixed
  `EPSILON` on the product corresponds to a wide angular window for long vectors
  and a narrow one for short ones. `UnitVector3D`'s `perpendicular` is well
  behaved; `Vector3D`'s inherits this trap.
- **`negate` re-validates when `V` is `UnitVector3D`.** It constructs
  `V(-x, -y, -z)`, and `UnitVector3D`'s three-component constructor defaults
  `check_validity_` to `true`, so every negation of a unit vector runs
  `check_validity()` and can in principle throw
  `ViolatedUnitVectorInvariantException`. `UnitVector3D.h`'s own comment names
  sign-flipping as exactly the case where passing `false` would be safe — this
  path does not take that shortcut.
- The templates enforce nothing about their operands. Instantiating them with a
  type whose accessors return plain `double` fails to compile only because of the
  `.dval()` calls; there is no concept or trait guarding the interface.
- `scale` takes `real_t` by value, not by const reference, and its second
  parameter `const V v` is by value as well.

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/GeometryInterpolation](GeometryInterpolation.md) | maths | 56 |
| [qt-widgets/FiniteRotationCalculatorDialog](../qt-widgets/FiniteRotationCalculatorDialog.md) | qt-widgets | 45 |
| [maths/PointInPolygon](PointInPolygon.md) | maths | 43 |
| [maths/GreatCircleArc](GreatCircleArc.md) | maths | 41 |
| [maths/SmallCircleBounds](SmallCircleBounds.md) | maths | 33 |
| [opengl/GLMatrix](../opengl/GLMatrix.md) | opengl | 28 |
| [maths/UnitVector3D](UnitVector3D.md) | maths | 27 |
| [view-operations/ChangeLightDirectionOperation](../view-operations/ChangeLightDirectionOperation.md) | view-operations | 22 |
| [gui/SimpleGlobeOrientation](../gui/SimpleGlobeOrientation.md) | gui | 20 |
| [opengl/GLVertex](../opengl/GLVertex.md) | opengl | 18 |
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 17 |
| [opengl/GLIntersectPrimitives](../opengl/GLIntersectPrimitives.md) | opengl | 17 |
| [gui/SceneLightingParameters](../gui/SceneLightingParameters.md) | gui | 16 |
| [maths/Vector3D](Vector3D.md) | maths | 16 |
| [view-operations/RenderedEllipse](../view-operations/RenderedEllipse.md) | view-operations | 14 |
| [opengl/GLProgramObject](../opengl/GLProgramObject.md) | opengl | 10 |
| [opengl/GLStateSets](../opengl/GLStateSets.md) | opengl | 10 |
| [view-operations/MovePoleOperation](../view-operations/MovePoleOperation.md) | view-operations | 10 |
| [app-logic/NetRotationUtils](../app-logic/NetRotationUtils.md) | app-logic | 9 |
| [maths/FiniteRotation](FiniteRotation.md) | maths | 9 |

*... and 55 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/GenericVectorOps3D.h
python scripts/gpq.py def GPlatesMaths::GenericVectorOps3D::ReturnType --body
python scripts/gpq.py uses ReturnType --kind struct
python scripts/gpq.py hier ReturnType
```

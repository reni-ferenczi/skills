# UnitQuaternion3D

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 382 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/UnitQuaternion3D.h` | C++ | 664 |
| `src/maths/UnitQuaternion3D.cc` | C++ | 324 |

## Overview

The rotation representation that everything in the reconstruction engine
ultimately composes. `FiniteRotation` is little more than a `UnitQuaternion3D`
plus an optional axis hint, and rotation composition along a plate circuit — the
operation `ReconstructionTree` performs for every plate at every reconstruction
time — is quaternion multiplication here. The class stores its four components
as a `real_t` scalar and a `Vector3D`, which is what lets the multiplication in
`operator*` be written directly as the `s1*s2 - dot(v1,v2)` /
`s1*v2 + s2*v1 + cross(v1,v2)` identity rather than as sixteen scalar products.

Construction is funnelled: every route in — `create_rotation`,
`create_identity_rotation`, `create`, `get_conjugate`, `operator-`, `operator*` —
goes through one protected `(real_t, Vector3D)` constructor, and the free
`operator-` and `operator*` are `friend`s specifically so they can reach it. That
constructor calls `renormalise_if_necessary()`, so the unit-norm invariant is
maintained by silent correction rather than by assertion. `assert_invariant()`
exists and would throw `ViolatedClassInvariantException`, but nothing calls it;
its own comment records that invoking it from the constructor is future work.

The `NonUnitQuaternion` nested struct, the scalar `operator*` overloads and the
`operator+` on non-unit quaternions exist for exactly one caller: the
`slerp` helper in `FiniteRotation.cc`, which forms `c1*q1 + c2*q2` as an
explicitly non-unit quaternion and then hands it to `create()` to be normalised
back into the type. Keeping the intermediate in a distinct type is what stops
that half-finished value from being mistaken for a valid rotation.
`get_rotation_params()` is the reverse direction, used by the pole dialogs, the
rotation-file writers and the CLI rotation commands to recover an axis and angle
for display or export.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::UnitQuaternion3D`](#gplatesmathsunitquaternion3d) | class | [`GPlatesUtils::QtStreamable<UnitQuaternion3D>`](../utils/QtStreamable.md) | — | 0 | Since this is a unit quaternion, its magnitude (norm) must always be identical to 1. |

## Members

### `GPlatesMaths::UnitQuaternion3D`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_conjugate()` | method | `UnitQuaternion3D` | public | Return the conjugate of this unit quaternion. |
| `get_inverse()` | method | `UnitQuaternion3D` | public | Return the multiplicative inverse of this unit quaternion. |
| `get_actual_norm_sqrd()` | method | `real_t` | public | Calculate the square of the \<em\>actual\</em\> norm of this quaternion (rather than just assuming it is equal to 1). |
| `renormalise_if_necessary()` | method | `void` | public | Renormalise the quaternion if necessary. |
| `RotationParams` | struct | `None` | public | This struct is used to contain the reverse-engineered rotation parameters of an arbitrary (ie, not necessarily user-specified; possibly machine-calculated by interpolation or other means) unit-quaternion. |
| `get_rotation_params( const boost::optional<UnitVector3D> &axis_hint)` | method | `RotationParams` | public | Calculate the rotation parameters of this unit quaternion. |
| `NonUnitQuaternion` | struct | `None` | public | This struct is used to contain the short-lived in-general,-not-a-unit-quaternion object created during the spherical linear interpolation between two unit-quaternions. |
| `create_rotation( const UnitVector3D &axis, const real_t &angle)` | method | `UnitQuaternion3D` | public | Create a unit quaternion to represent the following rotation around the given unit vector axis, by the given rotation angle angle. |
| `create_identity_rotation()` | method | `UnitQuaternion3D` | public | Create a unit quaternion to represent an identity rotation. |
| `create( const NonUnitQuaternion &q)` | method | `UnitQuaternion3D` | public | Attempt to create a unit quaternion from q. |
| `UnitQuaternion3D( const real_t &s, const Vector3D &v)` | constructor | `None` | protected | Create a unit quaternion composed of the specified (scalar, vector) parts. |
| `assert_invariant()` | method | `void` | protected | Assert the class invariant. |
| `m_scalar_part` | field | `real_t` | private | — |
| `m_vector_part` | field | `Vector3D` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator*( const UnitQuaternion3D &q1, const UnitQuaternion3D &q2)` | operator | `GPlatesMaths::UnitQuaternion3D` | — |
| `GPLATES_MATHS_UNITQUATERNION3D_H` | macro | `None` | — |
| `operator==( const UnitQuaternion3D &q1, const UnitQuaternion3D &q2)` | operator | `bool` | Return whether these two unit quaternions q1 and q2 are equal. |
| `operator!=( const UnitQuaternion3D &q1, const UnitQuaternion3D &q2)` | operator | `bool` | Return whether these two unit quaternions q1 and q2 are not equal. |
| `operator-( const UnitQuaternion3D &q)` | operator | `UnitQuaternion3D` | Return the negative of the unit quaternion q. |
| `represents_identity_rotation( const UnitQuaternion3D &q)` | function | `bool` | Return whether this unit quaternion q represents an identity rotation (ie. a rotation which maps a vector to itself). |
| `represent_equiv_rotations( const UnitQuaternion3D &q1, const UnitQuaternion3D &q2)` | function | `bool` | Return whether these two unit quaternions q1 and q2 represent equivalent rotations. |
| `dot( const UnitQuaternion3D::NonUnitQuaternion &q1, const UnitQuaternion3D::NonUnitQuaternion &q2)` | function | `real_t` | Take the (4D, hypersphere) dot-product of the non-unit-quaternions q1 and q2. |
| `dot( const UnitQuaternion3D &q1, const UnitQuaternion3D &q2)` | function | `real_t` | Take the (4D, hypersphere) dot-product of the unit-quaternions q1 and q2. |
| `operator*( const real_t &c, const UnitQuaternion3D &q)` | operator | `UnitQuaternion3D::NonUnitQuaternion` | Multiply the scalar c by the unit-quaternion q, producing a \<em\>non\</em\>-unit-quaternion result. |
| `operator*( const UnitQuaternion3D &q, const real_t &c)` | operator | `UnitQuaternion3D::NonUnitQuaternion` | Multiply the scalar c by the unit-quaternion q, producing a \<em\>non\</em\>-unit-quaternion result. |
| `operator+( const UnitQuaternion3D::NonUnitQuaternion &q1, const UnitQuaternion3D::NonUnitQuaternion &q2)` | operator | `UnitQuaternion3D::NonUnitQuaternion` | Add the two non-unit-quaternions q1 and q2, producing a non-unit-quaternion result. |
| `operator<<` | variable | `std::ostream` | — |

## Notes

**Equality is not rotation equivalence.** `q` and `-q` denote the same rotation,
and `operator==` compares components, so it will report them unequal. Use
`represent_equiv_rotations()` whenever the question is "same rotation" rather
than "same quaternion" — the header flags this on both operators, and both carry
an open `FIXME` asking whether they should become dot-product comparisons the way
the vector types did. The comparison is componentwise under `real_t`'s
tolerance, so it is an `EPSILON` box, not an angular test.

**The invariant is repaired, not asserted.** `renormalise_if_necessary()` acts
only when the actual norm-squared deviates from 1 by more than 2.0e-14. That
threshold is empirical: the comment records that beyond it, rotating a unit
vector yields one whose magnitude-squared is off by 5.0e-14 — enough to matter
to `UnitVector3D`'s own checks. Composing long plate circuits is exactly the
drift source it exists for. `create()` is separately defensive: its strict
norm check is `#if 0`-ed out ("until precision suckiness is fixed"), so in
practice it renormalises whenever `norm != 1.0` under the tolerance, and throws
`IndeterminateResultException` when the norm compares equal to zero.

**`get_rotation_params()` throws for the identity rotation** — the axis is
genuinely indeterminate there, and the caller must either check
`represents_identity_rotation()` first or be prepared for
`IndeterminateResultException`. Note also that the returned angle is always
non-negative: `acos` yields `[0, PI]`, so `(angle, axis)` and `(-angle, -axis)`
map to the same quaternion and cannot be told apart afterwards. That is the
entire reason `axis_hint` exists as a parameter, and the reason `FiniteRotation`
carries a `boost::optional<UnitVector3D>` axis hint alongside its quaternion and
propagates it through `compose()`. If you drop the hint, exported poles can come
back with the axis flipped and the angle negated relative to what the user
entered.

**Ordering.** Quaternion multiplication is associative but not commutative;
`compose(r1, r2)` is `r1.unit_quat() * r2.unit_quat()`. The inverse is the
conjugate, so `get_inverse()` is free — no division involved.

Instances are plain values with no shared or lazily cached state; const use is
thread-safe.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 42 |
| [maths/FiniteRotation](FiniteRotation.md) | maths | 26 |
| [maths/Rotation](Rotation.md) | maths | 26 |
| [maths/CalculateVelocity](CalculateVelocity.md) | maths | 25 |
| [app-logic/RotationUtils](../app-logic/RotationUtils.md) | app-logic | 17 |
| [maths/deprecated/StageRotation](deprecated/StageRotation.md) | maths | 17 |
| [qt-widgets/ApplyReconstructionPoleAdjustmentDialog](../qt-widgets/ApplyReconstructionPoleAdjustmentDialog.md) | qt-widgets | 17 |
| [gui/ExportStageRotationAnimationStrategy](../gui/ExportStageRotationAnimationStrategy.md) | gui | 16 |
| [cli/CliStageRotationCommand](../cli/CliStageRotationCommand.md) | cli | 13 |
| [qt-widgets/TotalReconstructionPolesDialog](../qt-widgets/TotalReconstructionPolesDialog.md) | qt-widgets | 12 |
| [app-logic/FlowlineUtils](../app-logic/FlowlineUtils.md) | app-logic | 9 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 8 |
| [cli/CliEquivalentTotalRotation](../cli/CliEquivalentTotalRotation.md) | cli | 7 |
| [cli/CliRelativeTotalRotation](../cli/CliRelativeTotalRotation.md) | cli | 7 |
| [file-io/PlatesRotationFormatWriter](../file-io/PlatesRotationFormatWriter.md) | file-io | 7 |
| [app-logic/NetRotationUtils](../app-logic/NetRotationUtils.md) | app-logic | 6 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 6 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](../opengl/GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 6 |
| [opengl/GLReconstructedStaticPolygonMeshes](../opengl/GLReconstructedStaticPolygonMeshes.md) | opengl | 6 |
| [opengl/GLShaderProgramUtils](../opengl/GLShaderProgramUtils.md) | opengl | 6 |

*... and 36 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/UnitQuaternion3D.h
python scripts/gpq.py def GPlatesMaths::UnitQuaternion3D --body
python scripts/gpq.py uses UnitQuaternion3D --kind class
python scripts/gpq.py hier UnitQuaternion3D
```

# UnitQuaternion3D

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 382 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/UnitQuaternion3D.h` | C++ | 664 |
| `src/maths/UnitQuaternion3D.cc` | C++ | 324 |

## Overview

[[[PROSE overview unit=maths/UnitQuaternion3D tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/UnitQuaternion3D tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

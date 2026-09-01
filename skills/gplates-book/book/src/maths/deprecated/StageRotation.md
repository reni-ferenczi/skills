# StageRotation

[Book TOC](../../../TOC.md) · [maths](../../../components/maths.md) · cluster Community 899 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/deprecated/StageRotation.h` | C++ | 215 |
| `src/maths/deprecated/StageRotation.cc` | C++ | 111 |

## Overview

A `StageRotation` represents the difference between two `FiniteRotation` objects, capturing the change in rotation over a change in time. Where a finite rotation maps a point from the present to a past moment, a stage rotation can be viewed as a displacement in rotation-space or as the angular velocity over a time interval. The class holds a `UnitQuaternion3D` and a time delta in millions of years; applying a stage rotation to a finite rotation via `operator*` advances both the quaternion and the time stamp. The free functions compute stage rotations from finite-rotation pairs, rescale them to different time intervals, and support interpolation between finite rotations.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::StageRotation`](#gplatesmathsstagerotation) | class | — | — | 0 | Represents a so-called "stage rotation" of plate tectonics. |

## Members

### `GPlatesMaths::StageRotation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `StageRotation( const UnitQuaternion3D &uq, const real_t &time_delta)` | constructor | `None` | public | Create a stage rotation consisting of the given unit quaternion and the given change in time. |
| `operator*( const FiniteRotation &r)` | operator | `FiniteRotation` | public | Apply this stage rotation to a finite rotation. |
| `m_unit_quat` | field | `UnitQuaternion3D` | private | — |
| `m_time_delta` | field | `real_t` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_STAGEROTATION_H` | macro | `None` | — |
| `subtractFiniteRots( const FiniteRotation &r1, const FiniteRotation &r2)` | function | `StageRotation` | Returns the difference between two finite rotations as a stage rotation. |
| `scaleToNewTimeDelta( const StageRotation &sr, const real_t &new_time_delta)` | function | `StageRotation` | Scale the given stage rotation such that its time delta is equal to the specified new time delta, and return the result. |
| `interpolate( const FiniteRotation &more_recent, const FiniteRotation &more_distant, const real_t &t)` | function | `FiniteRotation` | Calculate and return the finite rotation which is the interpolation of the two finite rotations more\_recent and more\_distant to the time t. |

## Notes

The entire `StageRotation` class and nearly all free functions are disabled via `#if 0 ... #endif` preprocessor blocks and are not compiled into the library. The code is retained for reference but marked for eventual removal. The `subtractFiniteRots()` function performs subtraction in rotation-space via the inverse of `r2` applied to `r1`, resulting in the property that `A == B + C == C * B` (where `+` denotes displacement and `*` denotes premultiplication); this non-symmetric operation is exposed as a named function rather than an operator to avoid confusion over evaluation order. Scaling a stage rotation requires both non-identity rotation and non-zero time delta, otherwise `scaleToNewTimeDelta()` throws `IndeterminateResultException`.

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/deprecated/RotationSequence](RotationSequence.md) | maths | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/deprecated/StageRotation.h
python scripts/gpq.py def GPlatesMaths::StageRotation --body
python scripts/gpq.py uses StageRotation --kind class
python scripts/gpq.py hier StageRotation
```

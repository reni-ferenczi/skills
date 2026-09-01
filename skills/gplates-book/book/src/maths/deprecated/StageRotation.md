# StageRotation

[Book TOC](../../../TOC.md) · [maths](../../../components/maths.md) · cluster Community 899 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/deprecated/StageRotation.h` | C++ | 215 |
| `src/maths/deprecated/StageRotation.cc` | C++ | 111 |

## Overview

[[[PROSE overview unit=maths/deprecated/StageRotation tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/deprecated/StageRotation tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

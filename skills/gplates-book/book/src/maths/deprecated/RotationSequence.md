# RotationSequence

[Book TOC](../../../TOC.md) · [maths](../../../components/maths.md) · cluster Community 506 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/deprecated/RotationSequence.h` | C++ | 412 |
| `src/maths/deprecated/RotationSequence.cc` | C++ | 219 |

## Overview

[[[PROSE overview unit=maths/deprecated/RotationSequence tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::RotationSequence`](#gplatesmathsrotationsequence) | class | — | — | 0 | This class represents a continuous sequence of finite rotations which describe the motion of a moving plate relative to a given fixed plate. |

## Members

### `GPlatesMaths::RotationSequence`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `seq_type` | typedef | `std::list< FiniteRotation >` | private | — |
| `SharedSequence` | class | `None` | private | Since FiniteRotation instances are quite large, and there might be "several" (multiple tens of) FiniteRotations stored in a single rotation sequence, lessen the impact of copying a RotationSequence instance by sharing the actual sequence ... |
| `EdgeType` | enum | `None` | public | The elements of this enumeration represent the possible edge-properties which a rotation sequence may possess at a given point in time. |
| `RotationSequence(const rid_t &fixed_plate, const rid_t &moving_plate, const FiniteRotation &frot)` | constructor | `None` | public | Create a rotation sequence for motion of the given moving plate relative to the given fixed plate, initialising the sequence with a finite rotation. |
| `RotationSequence(const RotationSequence &other)` | constructor | `None` | public | Explicitly define a copy-constructor, since we're doing ref-counting magic. |
| `~RotationSequence()` | destructor | `None` | public | Explicitly define a destructor, since we're doing ref-counting magic. |
| `operator=` | field | `RotationSequence` | public | Explicitly define an assignment operator, since we're doing ref-counting magic. |
| `mostRecentTime()` | method | `real_t` | public | Return the most recent point in time at which this rotation sequence is defined. |
| `mostDistantTime()` | method | `real_t` | public | Return the most distant point in time at which this rotation sequence is defined. |
| `fixedPlate()` | method | `rid_t` | public | Return the plate id of the fixed plate for this rotation sequence. |
| `movingPlate()` | method | `rid_t` | public | Return the plate id of the moving plate for this rotation sequence. |
| `isDefinedAtTime(real_t t)` | method | `bool` | public | Returns whether this rotation sequence is "defined" at a particular point in time t. |
| `edgeProperties(real_t t, EdgeType mode)` | method | `bool` | public | This function is used to query the edge-properties of a rotation sequence at a particular point in time t. |
| `isDefinedInFuture()` | method | `bool` | public | Returns whether this rotation sequence is "defined" in the future. |
| `finiteRotationAtTime(real_t t)` | method | `FiniteRotation` | public | If this rotation sequence is defined at time t, calculate the finite rotation for time t. |
| `insert(const FiniteRotation &frot)` | method | `void` | public | Insert another finite rotation frot into this rotation sequence. |
| `_fixed_plate` | field | `rid_t` | private | — |
| `_moving_plate` | field | `rid_t` | private | — |
| `_most_recent_time` | field | `real_t` | private | — |
| `_most_distant_time` | field | `real_t` | private | — |
| `_shared_seq` | field | `SharedSequence` | private | shared using reference counting |
| `shareOthersSharedSeq(const RotationSequence &other)` | method | `void` | private | "Share" (in the sense of taking part-ownership of) the SharedSequence belonging to other. \[Insert political humour -\> here \<-.\] |
| `relinquish(SharedSequence *ss)` | method | `void` | private | Give up any ownership of SharedSequence ss. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_MATHS_ROTATIONSEQUENCE_H_` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/deprecated/RotationSequence tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/deprecated/RotationHistory](RotationHistory.md) | maths | 7 |
| [deprecated/controls/Reconstruct](../../deprecated/controls/Reconstruct.md) | deprecated | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/deprecated/RotationSequence.h
python scripts/gpq.py def GPlatesMaths::RotationSequence --body
python scripts/gpq.py uses RotationSequence --kind class
python scripts/gpq.py hier RotationSequence
```

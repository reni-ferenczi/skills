# RotationHistory

[Book TOC](../../../TOC.md) · [maths](../../../components/maths.md) · cluster Community 1385 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/deprecated/RotationHistory.h` | C++ | 183 |
| `src/maths/deprecated/RotationHistory.cc` | C++ | 58 |

## Overview

[[[PROSE overview unit=maths/deprecated/RotationHistory tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::RotationHistory`](#gplatesmathsrotationhistory) | class | — | — | 0 | This class represents the rotation history of a moving plate. |

## Members

### `GPlatesMaths::RotationHistory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `seq_type` | typedef | `std::list< RotationSequence >` | public | — |
| `const_iterator` | typedef | `seq_type::const_iterator` | public | — |
| `RotationHistory()` | constructor | `None` | public | Create a rotation history. |
| `isDefinedAtTime(real_t t)` | method | `bool` | public | Returns whether this rotation history is defined at a particular point in time t. |
| `findAtTime(real_t t)` | method | `const_iterator` | public | Return an iterator pointing to the first rotation sequence in the collection which is defined at time t, or an iterator for the end of the collection, if an appropriate rotation sequence is not found. |
| `begin()` | method | `const_iterator` | public | Return an iterator for the first rotation sequence in the collection. |
| `end()` | method | `const_iterator` | public | Return an iterator for the end of the collection. |
| `insert(const RotationSequence &rseq)` | method | `void` | public | Insert another rotation sequence into the collection. |
| `_seq` | field | `seq_type` | private | This member is mutable because its value needs to be changed in the const member function 'ensureSeqSorted'. |
| `_is_modified` | field | `bool` | private | Whether the collection of rotation sequences has been modified since it was last sorted. |
| `ensureSeqSorted()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_MATHS_ROTATIONHISTORY_H_` | macro | `None` | — |
| `compareMRT(const RotationSequence &rs1, const RotationSequence &rs2)` | function | `bool` | Compare two rotation sequences by their most recent time. |

## Notes

[[[PROSE notes unit=maths/deprecated/RotationHistory tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/deprecated/RotationHistory.h
python scripts/gpq.py def GPlatesMaths::RotationHistory --body
python scripts/gpq.py uses RotationHistory --kind class
python scripts/gpq.py hier RotationHistory
```

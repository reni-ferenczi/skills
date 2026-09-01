# RotationHistory

[Book TOC](../../../TOC.md) · [maths](../../../components/maths.md) · cluster Community 1385 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/deprecated/RotationHistory.h` | C++ | 183 |
| `src/maths/deprecated/RotationHistory.cc` | C++ | 58 |

## Overview

A deprecated container for the rotation history of a moving plate. It stores a collection of `RotationSequence` objects, each describing how the plate rotated relative to a fixed reference plate during a specific time interval. The collection is lazily sorted by most-recent time on access via `begin()`, `end()`, or `findAtTime()`, with lazy sorting triggered by a dirty flag (`_is_modified`). Though the class does not enforce temporal continuity or prevent overlaps, comments indicate that design expectations are that sequences should align at cross-over points where one sequence ends and another begins.

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

The collection uses lazy sorting: sequences are kept in insertion order and sorted on-demand when accessed, with a mutable `_is_modified` flag tracking whether re-sorting is needed. Both `_seq` and `_is_modified` are mutable to allow const member functions to maintain cache consistency. The class design assumes but does not enforce that rotation sequences should be continuous at cross-over points (where one sequence ends and another begins) — overlaps at other times are explicitly flagged as "not allowed" in code comments, though the class does not validate this at insert time.

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

# FiniteRotationSnapshotTable

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1672 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/FiniteRotationSnapshotTable.h` | C++ | 60 |

## Overview

[[[PROSE overview unit=maths/FiniteRotationSnapshotTable tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::FiniteRotationSnapshotTable`](#gplatesmathsfiniterotationsnapshottable) | class | — | — | 0 | "Snapshot" of the rotation hierarchy at a particular time. |

## Members

### `GPlatesMaths::FiniteRotationSnapshotTable`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FiniteRotationSnapshotTable()` | constructor | `None` | public | XXX Implement me. |
| `operator[](rot_id_t)` | operator | `FiniteRotation` | public | NULL when there is no rotation defined for rot\_id at the time of the snapshot. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_FINITEROTATIONSNAPSHOTTABLE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/FiniteRotationSnapshotTable tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/FiniteRotationSnapshotTable.h
python scripts/gpq.py def GPlatesMaths::FiniteRotationSnapshotTable --body
python scripts/gpq.py uses FiniteRotationSnapshotTable --kind class
python scripts/gpq.py hier FiniteRotationSnapshotTable
```

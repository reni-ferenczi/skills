# InternalObjectInconsistencyException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 750 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/global/InternalObjectInconsistencyException.h` | C++ | 52 |

## Overview

[[[PROSE overview unit=global/InternalObjectInconsistencyException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::InternalObjectInconsistencyException`](#gplatesglobalinternalobjectinconsistencyexception) | class | [`Exception`](GPlatesException.md) | — | 3 | This is the base class of all exceptions in GPlates which are used to report that an object is internally inconsistent. |

## Members

### `GPlatesGlobal::InternalObjectInconsistencyException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InternalObjectInconsistencyException( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_INTERNALOBJECTINCONSISTENCYEXCEPTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=global/InternalObjectInconsistencyException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [global/IntrusivePointerZeroRefCountException](IntrusivePointerZeroRefCountException.md) | global | 3 |
| [maths/InvalidPolylineContainsOnlyOnePointException](../maths/InvalidPolylineContainsOnlyOnePointException.md) | maths | 3 |
| [maths/InvalidPolylineContainsZeroPointsException](../maths/InvalidPolylineContainsZeroPointsException.md) | maths | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/InternalObjectInconsistencyException.h
python scripts/gpq.py def GPlatesGlobal::InternalObjectInconsistencyException --body
python scripts/gpq.py uses InternalObjectInconsistencyException --kind class
python scripts/gpq.py hier InternalObjectInconsistencyException
```

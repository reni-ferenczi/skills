# IndeterminateArcRotationAxisException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 3 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/IndeterminateArcRotationAxisException.h` | C++ | 81 |

## Overview

[[[PROSE overview unit=maths/IndeterminateArcRotationAxisException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::IndeterminateArcRotationAxisException`](#gplatesmathsindeterminatearcrotationaxisexception) | class | [`GPlatesGlobal::PreconditionViolationError`](../global/PreconditionViolationError.md) | — | 0 | This is the exception thrown when an attempt is made to access the rotation axis of a zero-length great-circle arc (which does not have a determinate rotation axis). |

## Members

### `GPlatesMaths::IndeterminateArcRotationAxisException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `IndeterminateArcRotationAxisException( const GPlatesUtils::CallStack::Trace &exception_source, const GreatCircleArc &arc_)` | constructor | `None` | public | — |
| `~IndeterminateArcRotationAxisException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_arc` | field | `GreatCircleArc` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_INDETERMINATEARCROTATIONAXISEXCEPTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/IndeterminateArcRotationAxisException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/GreatCircleArc](GreatCircleArc.md) | maths | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/IndeterminateArcRotationAxisException.h
python scripts/gpq.py def GPlatesMaths::IndeterminateArcRotationAxisException --body
python scripts/gpq.py uses IndeterminateArcRotationAxisException --kind class
python scripts/gpq.py hier IndeterminateArcRotationAxisException
```

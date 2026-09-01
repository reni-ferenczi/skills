# NullNonNullIntrusivePointerException

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1400 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/NullNonNullIntrusivePointerException.h` | C++ | 70 |

## Overview

[[[PROSE overview unit=utils/NullNonNullIntrusivePointerException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::NullNonNullIntrusivePointerException`](#gplatesutilsnullnonnullintrusivepointerexception) | class | [`GPlatesGlobal::PreconditionViolationError`](../global/PreconditionViolationError.md) | — | 0 | This is the exception thrown by NullIntrusivePointerHandler when an attempt is made to instantiate a non-null intrusive-pointer with a NULL pointer. |

## Members

### `GPlatesUtils::NullNonNullIntrusivePointerException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NullNonNullIntrusivePointerException( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `~NullNonNullIntrusivePointerException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_NULLNONNULLINTRUSIVEPOINTEREXCEPTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=utils/NullNonNullIntrusivePointerException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [utils/NullIntrusivePointerHandler](NullIntrusivePointerHandler.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/NullNonNullIntrusivePointerException.h
python scripts/gpq.py def GPlatesUtils::NullNonNullIntrusivePointerException --body
python scripts/gpq.py uses NullNonNullIntrusivePointerException --kind class
python scripts/gpq.py hier NullNonNullIntrusivePointerException
```

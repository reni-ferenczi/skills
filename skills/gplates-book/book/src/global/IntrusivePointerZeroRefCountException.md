# IntrusivePointerZeroRefCountException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 750 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/global/IntrusivePointerZeroRefCountException.h` | C++ | 83 |

## Overview

[[[PROSE overview unit=global/IntrusivePointerZeroRefCountException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::IntrusivePointerZeroRefCountException`](#gplatesglobalintrusivepointerzerorefcountexception) | class | [`GPlatesGlobal::InternalObjectInconsistencyException`](InternalObjectInconsistencyException.md) | — | 0 | This is the exception thrown when an object has an intrusive-pointer ref-count of zero, when its ref-count should be greater than zero. |

## Members

### `GPlatesGlobal::IntrusivePointerZeroRefCountException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `IntrusivePointerZeroRefCountException( const GPlatesUtils::CallStack::Trace &exception_source, const void *ptr_to_referenced_object_)` | constructor | `None` | public | When this exception is thrown, presumably in a member function of the object whose ref-count has been observed to be zero, the parameters to this constructor should be this, GPLATES\_EXCEPTION\_SOURCE, which indicate the object and the ... |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_ptr_to_referenced_object` | field | `void` | private | — |
| `d_filename` | field | `char` | private | — |
| `d_line_num` | field | `int` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_INTRUSIVEPOINTERZEROREFCOUNTEXCEPTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=global/IntrusivePointerZeroRefCountException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [utils/ReferenceCount](../utils/ReferenceCount.md) | utils | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/IntrusivePointerZeroRefCountException.h
python scripts/gpq.py def GPlatesGlobal::IntrusivePointerZeroRefCountException --body
python scripts/gpq.py uses IntrusivePointerZeroRefCountException --kind class
python scripts/gpq.py hier IntrusivePointerZeroRefCountException
```

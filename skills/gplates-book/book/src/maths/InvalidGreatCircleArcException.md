# InvalidGreatCircleArcException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 83 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/InvalidGreatCircleArcException.h` | C++ | 77 |

## Overview

Exception thrown when an attempt is made to create an invalid `GreatCircleArc` that violates the class invariant. The exception carries a message describing the specific conditions that caused the invariant violation and inherits from `MathematicalException`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::InvalidGreatCircleArcException`](#gplatesmathsinvalidgreatcirclearcexception) | class | [`MathematicalException`](MathematicalException.md) | — | 0 | The Exception thrown when an attempt is made to create an invalid great-circle arc. |

## Members

### `GPlatesMaths::InvalidGreatCircleArcException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InvalidGreatCircleArcException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | which cause the invariant to be violated. |
| `~InvalidGreatCircleArcException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_MATHS_INVALIDGREATCIRCLEARCEXCEPTION_H_` | macro | `None` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/InvalidGreatCircleArcException.h
python scripts/gpq.py def GPlatesMaths::InvalidGreatCircleArcException --body
python scripts/gpq.py uses InvalidGreatCircleArcException --kind class
python scripts/gpq.py hier InvalidGreatCircleArcException
```

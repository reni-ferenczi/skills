# UnableToExtendPointlikeArcException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1640 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/UnableToExtendPointlikeArcException.h` | C++ | 80 |

## Overview

An exception thrown when code attempts to extend a pointlike `GreatCircleArc` to a full great circle. A pointlike arc is one where both endpoints are the same or numerically indistinguishable, which does not uniquely determine the great circle it lies on; therefore, extension is impossible. The exception inherits from `PreconditionViolationError` and carries the arc that violated the requirement, signaling an operation precondition failure rather than a resource error.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::UnableToExtendPointlikeArcException`](#gplatesmathsunabletoextendpointlikearcexception) | class | [`GPlatesGlobal::PreconditionViolationError`](../global/PreconditionViolationError.md) | — | 0 | This is the exception thrown when an attempt is made to extend a pointlike arc to a great-circle (since a pointlike arc does not determine a unique great-circle). |

## Members

### `GPlatesMaths::UnableToExtendPointlikeArcException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnableToExtendPointlikeArcException( const GPlatesUtils::CallStack::Trace &exception_source, const GreatCircleArc &arc_)` | constructor | `None` | public | — |
| `~UnableToExtendPointlikeArcException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_arc` | field | `GreatCircleArc` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_UNABLETOEXTENDPOINTLIKEARCEXCEPTION_H` | macro | `None` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/UnableToExtendPointlikeArcException.h
python scripts/gpq.py def GPlatesMaths::UnableToExtendPointlikeArcException --body
python scripts/gpq.py uses UnableToExtendPointlikeArcException --kind class
python scripts/gpq.py hier UnableToExtendPointlikeArcException
```

# UnableToExtendPointlikeArcException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1640 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/UnableToExtendPointlikeArcException.h` | C++ | 80 |

## Overview

[[[PROSE overview unit=maths/UnableToExtendPointlikeArcException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/UnableToExtendPointlikeArcException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

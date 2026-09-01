# UnableToIntersectEquivalentGreatCirclesException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1586 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/UnableToIntersectEquivalentGreatCirclesException.h` | C++ | 79 |

## Overview

[[[PROSE overview unit=maths/UnableToIntersectEquivalentGreatCirclesException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::UnableToIntersectEquivalentGreatCirclesException`](#gplatesmathsunabletointersectequivalentgreatcirclesexception) | class | [`GPlatesGlobal::PreconditionViolationError`](../global/PreconditionViolationError.md) | — | 0 | This is the exception thrown when an attempt is made to calculate the intersection of two great-circles which are equivalent. |

## Members

### `GPlatesMaths::UnableToIntersectEquivalentGreatCirclesException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnableToIntersectEquivalentGreatCirclesException( const GPlatesUtils::CallStack::Trace &exception_source, const GreatCircleArc &arc1_, const GreatCircleArc &arc2_)` | constructor | `None` | public | — |
| `~UnableToIntersectEquivalentGreatCirclesException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_arc1` | field | `GreatCircleArc` | private | — |
| `d_arc2` | field | `GreatCircleArc` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_UNABLETOINTERSECTEQUIVALENTGREATCIRCLESEXCEPTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/UnableToIntersectEquivalentGreatCirclesException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/UnableToIntersectEquivalentGreatCirclesException.h
python scripts/gpq.py def GPlatesMaths::UnableToIntersectEquivalentGreatCirclesException --body
python scripts/gpq.py uses UnableToIntersectEquivalentGreatCirclesException --kind class
python scripts/gpq.py hier UnableToIntersectEquivalentGreatCirclesException
```

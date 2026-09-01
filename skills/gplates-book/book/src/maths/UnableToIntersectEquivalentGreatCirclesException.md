# UnableToIntersectEquivalentGreatCirclesException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1586 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/UnableToIntersectEquivalentGreatCirclesException.h` | C++ | 79 |

## Overview

An exception thrown when code attempts to calculate the intersection of two great circles that are equivalent—that is, they represent the same great circle on the sphere. Since equivalent great circles intersect everywhere rather than at discrete points, computing a unique intersection is undefined. The exception inherits from `PreconditionViolationError` and carries both arcs that violated the requirement that they be distinct great circles.

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

*None.*

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

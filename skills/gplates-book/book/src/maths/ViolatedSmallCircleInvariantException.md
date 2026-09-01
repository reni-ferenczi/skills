# ViolatedSmallCircleInvariantException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 83 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/ViolatedSmallCircleInvariantException.h` | C++ | 75 |

## Overview

An exception thrown when small circle invariants are violated. Small circles are geometric constructs on a sphere (circles not centered at the pole); they have specific mathematical properties that must be preserved. This exception signals when an operation attempts to create or modify a small circle in a way that would violate these invariants. It follows the same pattern as the other invariant exception classes in the maths module, carrying a message and stack trace.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::ViolatedSmallCircleInvariantException`](#gplatesmathsviolatedsmallcircleinvariantexception) | class | [`MathematicalException`](MathematicalException.md) | — | 0 | The Exception thrown when unit vector invariants are violated. |

## Members

### `GPlatesMaths::ViolatedSmallCircleInvariantException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ViolatedSmallCircleInvariantException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | which cause the invariant to be violated. |
| `~ViolatedSmallCircleInvariantException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_MATHS_VIOLATEDSMALLCIRCLEINVARIANTEXCEPTION_H_` | macro | `None` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/ViolatedSmallCircleInvariantException.h
python scripts/gpq.py def GPlatesMaths::ViolatedSmallCircleInvariantException --body
python scripts/gpq.py uses ViolatedSmallCircleInvariantException --kind class
python scripts/gpq.py hier ViolatedSmallCircleInvariantException
```

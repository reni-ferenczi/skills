# ViolatedDirVectorInvariantException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 83 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/ViolatedDirVectorInvariantException.h` | C++ | 75 |

## Overview

An exception thrown specifically when direction vector invariants are violated. Direction vectors in GPlates mathematics represent normalized directions in 3D space; this exception signals when an operation attempts to create or manipulate a direction vector in a way that would violate the mathematical invariants of that type. Like its sibling exception classes, it carries a message describing the invariant violation and stack trace information.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::ViolatedDirVectorInvariantException`](#gplatesmathsviolateddirvectorinvariantexception) | class | [`MathematicalException`](MathematicalException.md) | — | 0 | The Exception thrown when direction vector invariants are violated. |

## Members

### `GPlatesMaths::ViolatedDirVectorInvariantException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ViolatedDirVectorInvariantException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | which cause the invariant to be violated. |
| `~ViolatedDirVectorInvariantException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_MATHS_VIOLATEDDIRVECTORINVARIANTEXCEPTION_H_` | macro | `None` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/ViolatedDirVectorInvariantException.h
python scripts/gpq.py def GPlatesMaths::ViolatedDirVectorInvariantException --body
python scripts/gpq.py uses ViolatedDirVectorInvariantException --kind class
python scripts/gpq.py hier ViolatedDirVectorInvariantException
```

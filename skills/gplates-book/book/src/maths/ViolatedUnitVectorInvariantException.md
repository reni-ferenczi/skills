# ViolatedUnitVectorInvariantException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 83 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/ViolatedUnitVectorInvariantException.h` | C++ | 74 |

## Overview

An exception thrown when unit vector invariants are violated. A unit vector must have magnitude exactly 1; this exception is thrown when an operation attempts to create or manipulate a `UnitVector3D` in a way that would violate this requirement. The `UnitVector3D` class uses this exception to enforce its preconditions, ensuring that code working with unit vectors can rely on the magnitude invariant.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::ViolatedUnitVectorInvariantException`](#gplatesmathsviolatedunitvectorinvariantexception) | class | [`MathematicalException`](MathematicalException.md) | — | 0 | The Exception thrown when unit vector invariants are violated. |

## Members

### `GPlatesMaths::ViolatedUnitVectorInvariantException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ViolatedUnitVectorInvariantException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | which cause the invariant to be violated. |
| `~ViolatedUnitVectorInvariantException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_MATHS_VIOLATEDUNITVECTORINVARIANTEXCEPTION_H_` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/UnitVector3D](UnitVector3D.md) | maths | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/ViolatedUnitVectorInvariantException.h
python scripts/gpq.py def GPlatesMaths::ViolatedUnitVectorInvariantException --body
python scripts/gpq.py uses ViolatedUnitVectorInvariantException --kind class
python scripts/gpq.py hier ViolatedUnitVectorInvariantException
```

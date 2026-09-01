# InvalidGridException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 83 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/InvalidGridException.h` | C++ | 75 |

## Overview

Exception thrown when an attempt is made to create an invalid grid that violates the grid invariants. The exception carries a message describing the specific conditions that made the grid invalid and inherits from `MathematicalException`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::InvalidGridException`](#gplatesmathsinvalidgridexception) | class | [`MathematicalException`](MathematicalException.md) | — | 0 | The Exception thrown when an attempt is made to create an invalid grid. |

## Members

### `GPlatesMaths::InvalidGridException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InvalidGridException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | which cause the grid to be invalid. |
| `~InvalidGridException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_MATHS_INVALIDGRIDEXCEPTION_H_` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/deprecated/GridOnSphere](deprecated/GridOnSphere.md) | maths | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/InvalidGridException.h
python scripts/gpq.py def GPlatesMaths::InvalidGridException --body
python scripts/gpq.py uses InvalidGridException --kind class
python scripts/gpq.py hier InvalidGridException
```

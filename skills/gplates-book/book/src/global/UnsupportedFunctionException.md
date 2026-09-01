# UnsupportedFunctionException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 17 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/global/UnsupportedFunctionException.h` | C++ | 74 |

## Overview

Exception thrown when code calls a function that is deliberately unsupported. Unlike `NotYetImplementedException` (which indicates work in progress), this signals that a function is intentionally not available — there may be architectural or design reasons why it is not supported. The exception stores the name of the unsupported function for diagnostic purposes.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::UnsupportedFunctionException`](#gplatesglobalunsupportedfunctionexception) | class | [`Exception`](GPlatesException.md) | — | 0 | Should be thrown when a function that has purposely not been implemented is called. |

## Members

### `GPlatesGlobal::UnsupportedFunctionException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnsupportedFunctionException( const GPlatesUtils::CallStack::Trace &exception_source, const char *fname)` | constructor | `None` | public | not supported. |
| `~UnsupportedFunctionException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_fname` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_GLOBAL_UNSUPPORTEDFUNCTIONEXCEPTION_H_` | macro | `None` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/UnsupportedFunctionException.h
python scripts/gpq.py def GPlatesGlobal::UnsupportedFunctionException --body
python scripts/gpq.py uses UnsupportedFunctionException --kind class
python scripts/gpq.py hier UnsupportedFunctionException
```

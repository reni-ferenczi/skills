# UninitialisedSingletonException

[Book TOC](../../../TOC.md) · [global](../../../components/global.md) · cluster Community 215 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/global/deprecated/UninitialisedSingletonException.h` | C++ | 72 |

## Overview

A specific exception type for reporting attempts to use singletons that have not been properly initialised. This exception inherits from the base `Exception` class and carries a custom message describing the situation. It is now deprecated and no longer in active use within the GPlates codebase.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::UninitialisedSingletonException`](#gplatesglobaluninitialisedsingletonexception) | class | [`Exception`](../GPlatesException.md) | — | 0 | Should be thrown when an attempt is made to instantiate a singleton class which has not been initialised. |

## Members

### `GPlatesGlobal::UninitialisedSingletonException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UninitialisedSingletonException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_GLOBAL_UNINITIALISEDSINGLETONEXCEPTION_H_` | macro | `None` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/deprecated/UninitialisedSingletonException.h
python scripts/gpq.py def GPlatesGlobal::UninitialisedSingletonException --body
python scripts/gpq.py uses UninitialisedSingletonException --kind class
python scripts/gpq.py hier UninitialisedSingletonException
```

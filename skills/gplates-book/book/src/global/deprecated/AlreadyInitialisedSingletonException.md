# AlreadyInitialisedSingletonException

[Book TOC](../../../TOC.md) · [global](../../../components/global.md) · cluster Community 215 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/global/deprecated/AlreadyInitialisedSingletonException.h` | C++ | 73 |

## Overview

**Deprecated.** Exception thrown when code attempts to initialize a singleton class that has already been initialized. This is marked deprecated — the singleton pattern it enforces is no longer preferred in modern GPlates code. The exception takes a custom message describing the situation.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::AlreadyInitialisedSingletonException`](#gplatesglobalalreadyinitialisedsingletonexception) | class | [`Exception`](../GPlatesException.md) | — | 0 | Should be thrown when an attempt is made to instantiate a singleton class which has already been initialised. |

## Members

### `GPlatesGlobal::AlreadyInitialisedSingletonException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AlreadyInitialisedSingletonException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_GLOBAL_ALREADYINITIALISEDSINGLETONEXCEPTION_H_` | macro | `None` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/deprecated/AlreadyInitialisedSingletonException.h
python scripts/gpq.py def GPlatesGlobal::AlreadyInitialisedSingletonException --body
python scripts/gpq.py uses AlreadyInitialisedSingletonException --kind class
python scripts/gpq.py hier AlreadyInitialisedSingletonException
```

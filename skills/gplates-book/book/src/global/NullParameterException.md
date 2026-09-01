# NullParameterException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 215 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/global/NullParameterException.h` | C++ | 74 |

## Overview

Exception thrown when a function receives a NULL pointer for a parameter that must not be null. This detects violated preconditions on pointer arguments — callers must ensure they pass valid pointers rather than null. Unlike `NotYetImplementedException`, this exception carries a custom message (passed at construction) that can describe which parameter was null or what the expected value should have been, helping callers diagnose what went wrong.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::NullParameterException`](#gplatesglobalnullparameterexception) | class | [`Exception`](GPlatesException.md) | — | 0 | Should be thrown when a function is invoked with a NULL-pointer parameter when that parameter may not be NULL. |

## Members

### `GPlatesGlobal::NullParameterException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NullParameterException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | — |
| `~NullParameterException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_GLOBAL_NULLPARAMETEREXCEPTION_H_` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [deprecated/controls/Lifetime](../deprecated/controls/Lifetime.md) | deprecated | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/NullParameterException.h
python scripts/gpq.py def GPlatesGlobal::NullParameterException --body
python scripts/gpq.py uses NullParameterException --kind class
python scripts/gpq.py hier NullParameterException
```

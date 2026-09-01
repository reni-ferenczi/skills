# Environment

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1809 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/Environment.h` | C++ | 63 |
| `src/utils/Environment.cc` | C++ | 64 |

## Overview

`Environment` wraps the standard library's `std::getenv()` to return `QString` instead of C strings, eliminating manual conversions and enabling the use of Qt's string operations and locale-aware comparisons. The `getenv()` function returns a null `QString` if the variable is not defined.

An additional `getenv_as_bool()` function interprets environment variable values as boolean, returning the default value if the variable is unset, treating any value except "0", "false", "off", "disabled", or "no" (case-insensitive) as true. This enables users to set flags with simple environment variables like `GPLATES_FEATURE=1`.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_ENVIRONMENT_H` | macro | `None` | — |
| `getenv( const char *variable_name)` | function | `QString` | Wrap a call to std::getenv() so that we return a QString, which is much more friendly to deal with locale-aware upper/lower case transforms without having to use the stupid STL algorithm. |
| `getenv_as_bool( const char *variable_name, bool default_value)` | function | `bool` | Test for an environment variable's "truthiness", to allow users to easily export variables as "1" or "true" or "yes" etc. |

## Notes

`getenv()` returns a null `QString` when the variable is undefined, not an empty string; check with `.isNull()` to distinguish. Passing a null pointer to `getenv()` is handled safely, returning an empty QString. The `getenv_as_bool()` function normalizes values (trimming whitespace, converting to lowercase, applying Unicode normalization) before checking against the set of false values; any other value is treated as true.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/GPlatesQtMsgHandler](../app-logic/GPlatesQtMsgHandler.md) | app-logic | 2 |
| [app-logic/UserPreferences](../app-logic/UserPreferences.md) | app-logic | 2 |
| [file-io/LogToFileHandler](../file-io/LogToFileHandler.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/Environment.h
```

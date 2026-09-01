# StringUtils

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 439 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/StringUtils.h` | C++ | 65 |
| `src/utils/StringUtils.cc` | C++ | 79 |

## Overview

Provides utilities for converting between Qt `QString` and C++ standard library `std::wstring` types. On Windows, where Qt is compiled without `wchar_t` as a native type, `make_qstring_from_wstring()` and `make_wstring_from_qstring()` contain a workaround that reinterprets the strings via UTF-16 encoding. On other platforms, these functions simply delegate to Qt's standard conversion functions.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_STRINGUTILS_H` | macro | `None` | — |
| `make_qstring_from_wstring( const std::wstring &str)` | function | `QString` | Converts a std::wstring instance into a QString instance. |
| `make_wstring_from_qstring( const QString &str)` | function | `std::wstring` | Converts a QString instance into a std::wstring instance. |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [api/PythonRunner](../api/PythonRunner.md) | api | 5 |
| [api/ConsoleReader](../api/ConsoleReader.md) | api | 3 |
| [gui/PythonManager](../gui/PythonManager.md) | gui | 2 |
| [api/PyApplication](../api/PyApplication.md) | api | 1 |
| [api/PythonUtils](../api/PythonUtils.md) | api | 1 |
| [file-io/GpmlReader](../file-io/GpmlReader.md) | file-io | 1 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/StringUtils.h
```

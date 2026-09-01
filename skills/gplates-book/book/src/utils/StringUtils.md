# StringUtils

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 439 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/StringUtils.h` | C++ | 65 |
| `src/utils/StringUtils.cc` | C++ | 79 |

## Overview

[[[PROSE overview unit=utils/StringUtils tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=utils/StringUtils tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

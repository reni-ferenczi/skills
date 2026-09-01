# Environment

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1809 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/Environment.h` | C++ | 63 |
| `src/utils/Environment.cc` | C++ | 64 |

## Overview

[[[PROSE overview unit=utils/Environment tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=utils/Environment tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

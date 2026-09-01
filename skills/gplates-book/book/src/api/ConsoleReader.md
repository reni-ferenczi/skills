# ConsoleReader

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 115 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/ConsoleReader.h` | C++ | 67 |
| `src/api/ConsoleReader.cc` | C++ | 115 |

## Overview

[[[PROSE overview unit=api/ConsoleReader tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::ConsoleReader`](#gplatesapiconsolereader) | class | — | — | 0 | On construction, replaces sys.stdin with this, and on destruction, restores the original sys.stdin. |

## Members

### `GPlatesApi::ConsoleReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConsoleReader( AbstractConsole *console = NULL)` | constructor | `None` | public | — |
| `~ConsoleReader()` | destructor | `None` | public | — |
| `readline()` | method | `boost::python::object` | public | — |
| `d_console` | field | `AbstractConsole` | private | — |
| `d_old_object` | field | `boost::python::object` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `export_console_reader()` | function | `void` | — |
| `GPLATES_API_CONSOLEREADER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=api/ConsoleReader tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 2 |

## Related

**Python bindings**

| Python name | Kind | Owner | C++ |
|---|---|---|---|
| `GPlatesConsoleReader` | class | — | `GPlatesApi::ConsoleReader` |
| `readline` | method | `GPlatesConsoleReader` | `&GPlatesApi::ConsoleReader::readline` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/ConsoleReader.h
python scripts/gpq.py def GPlatesApi::ConsoleReader --body
python scripts/gpq.py uses ConsoleReader --kind class
python scripts/gpq.py hier ConsoleReader
```

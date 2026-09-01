# ConsoleReader

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 115 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/ConsoleReader.h` | C++ | 67 |
| `src/api/ConsoleReader.cc` | C++ | 115 |

## Overview

ConsoleReader is a Python object that intercepts stdin to prevent the Python console from hanging when users try to read from the standard input stream. On construction it replaces `sys.stdin` with itself and restores the original on destruction. The `readline()` method opens a modal dialog to prompt for user input, ensuring the GUI remains responsive even during interactive input operations.

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

Only `readline()` is supported for stdin. The `sys.stdin` replacement is managed by construction and destruction, so the lifetime of a `ConsoleReader` instance controls when the override is active.

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

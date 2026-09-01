# ConsoleWriter

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 115 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/ConsoleWriter.h` | C++ | 69 |
| `src/api/ConsoleWriter.cc` | C++ | 127 |

## Overview

[[[PROSE overview unit=api/ConsoleWriter tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::ConsoleWriter`](#gplatesapiconsolewriter) | class | — | — | 0 | On construction, redirects either of sys.stdout or sys.stderr (depending on the stream argument) to the specified console by replacing it with 'this'. |

## Members

### `GPlatesApi::ConsoleWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConsoleWriter( bool error = false, AbstractConsole *console = NULL)` | constructor | `None` | public | — |
| `~ConsoleWriter()` | destructor | `None` | public | — |
| `write( const boost::python::object &text)` | method | `void` | public | — |
| `d_error` | field | `bool` | private | — |
| `d_console` | field | `AbstractConsole` | private | — |
| `d_old_object` | field | `boost::python::object` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_stream_name( bool error)` | function | `char` | — |
| `export_console_writer()` | function | `void` | — |
| `GPLATES_API_CONSOLEWRITER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=api/ConsoleWriter tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 4 |

## Related

**Python bindings**

| Python name | Kind | Owner | C++ |
|---|---|---|---|
| `GPlatesConsoleWriter` | class | — | `GPlatesApi::ConsoleWriter` |
| `write` | method | `GPlatesConsoleWriter` | `&GPlatesApi::ConsoleWriter::write` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/ConsoleWriter.h
python scripts/gpq.py def GPlatesApi::ConsoleWriter --body
python scripts/gpq.py uses ConsoleWriter --kind class
python scripts/gpq.py hier ConsoleWriter
```

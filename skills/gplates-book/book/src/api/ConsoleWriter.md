# ConsoleWriter

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 115 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/ConsoleWriter.h` | C++ | 69 |
| `src/api/ConsoleWriter.cc` | C++ | 127 |

## Overview

ConsoleWriter captures Python output by redirecting either `sys.stdout` or `sys.stderr` to a GPlates console on construction and restoring the original on destruction. The `write()` method is the only output operation supported, but this is sufficient to capture print output and errors printed via Python's error handlers. The `error` flag on construction selects which stream to redirect.

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

Only `write()` is supported; other stream methods are not implemented. The stream redirection is scoped to the lifetime of the `ConsoleWriter` instance.

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

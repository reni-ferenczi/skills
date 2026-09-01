# AbstractConsole

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 115 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/api/AbstractConsole.h` | C++ | 84 |

## Overview

`GPlatesApi::AbstractConsole` is the interface the embedded Python console talks
to instead of a concrete widget: it decouples the code that runs Python (which
needs to print output and prompt for input) from whatever surface is actually
showing it, whether that is a Qt dialog or a headless stream. `append_text` is
overloaded so callers can hand it either a `QString` they built themselves or a
raw `boost::python::object`, which the implementation stringifies; the `error`
flag lets a caller mark a message as an error without the interface needing a
separate method for it.

Every method is documented as required to be thread-safe, because Python
execution and console I/O do not necessarily happen on the same thread as the
console's own display.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::AbstractConsole`](#gplatesapiabstractconsole) | class | — | — | 1 | The abstract base class for consoles that can display output from Python, and read lines as input. |

## Members

### `GPlatesApi::AbstractConsole`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~AbstractConsole()` | destructor | `None` | public | — |
| `append_text( const QString &text, bool error = false)` | method | `void` | public | Appends the given text to the console. |
| `append_text( const boost::python::object &obj, bool error = false)` | method | `void` | public | Appends the stringified version of obj to the console. |
| `read_line()` | method | `QString` | public | Prompts the user for a line of input. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_API_ABSTRACTCONSOLE_H` | macro | `None` | — |

## Notes

Implementations must make `append_text` and `read_line` thread-safe; the base
class itself enforces nothing beyond declaring the pure virtual interface.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/PythonManager](../gui/PythonManager.md) | gui | 14 |
| [api/ConsoleReader](ConsoleReader.md) | api | 13 |
| [api/ConsoleWriter](ConsoleWriter.md) | api | 13 |
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/AbstractConsole.h
python scripts/gpq.py def GPlatesApi::AbstractConsole --body
python scripts/gpq.py uses AbstractConsole --kind class
python scripts/gpq.py hier AbstractConsole
```

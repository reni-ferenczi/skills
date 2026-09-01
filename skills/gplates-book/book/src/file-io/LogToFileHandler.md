# LogToFileHandler

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1481 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/LogToFileHandler.h` | C++ | 107 |
| `src/file-io/LogToFileHandler.cc` | C++ | 217 |

## Overview

[[[PROSE overview unit=file-io/LogToFileHandler tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::LogToFileHandler`](#gplatesfileiologtofilehandler) | class | [`GPlatesAppLogic::GPlatesQtMsgHandler::MessageHandler`](../app-logic/GPlatesQtMsgHandler.md) | — | 0 | A derivation of GPlatesQtMsgHandler::MessageHandler that logs to a file on disk. |

## Members

### `GPlatesFileIO::LogToFileHandler`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LogToFileHandler( const QString &log_filename = DEFAULT_LOG_FILENAME)` | constructor | `None` | public | Default constructor for LogToFileHandler; optionally takes the filename to log to, which will be dumped into the current working directory unless a full pathname is specified. |
| `LogToFileHandler( FILE *output_file_ptr)` | constructor | `None` | public | Special constructor to allow you to log to stderr. |
| `~LogToFileHandler()` | destructor | `None` | public | — |
| `handle_qt_message( QtMsgType msg_type, const QString &msg)` | method | `void` | public | — |
| `DEFAULT_LOG_FILENAME` | field | `QString` | private | Default filename to log Qt messages to. |
| `d_log_file` | field | `QFile` | private | The file we log to. |
| `d_log_stream` | field | `boost::scoped_ptr<QTextStream>` | private | QTextStream to log with. |
| `d_log_level` | field | `int` | private | QtMsgType log messages of this level and above will be logged to file; those below it will be ignored. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DEFAULT_LOG_FILENAME` | variable | `QString` | — |
| `adjust_default_log_level( int log_level = QtDebugMsg)` | function | `int` | Specify logic for choosing the default loglevel here. |
| `GPLATES_FILEIO_LOGTOFILEHANDLER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/LogToFileHandler tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/GPlatesQtMsgHandler](../app-logic/GPlatesQtMsgHandler.md) | app-logic | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/LogToFileHandler.h
python scripts/gpq.py def GPlatesFileIO::LogToFileHandler --body
python scripts/gpq.py uses LogToFileHandler --kind class
python scripts/gpq.py hier LogToFileHandler
```

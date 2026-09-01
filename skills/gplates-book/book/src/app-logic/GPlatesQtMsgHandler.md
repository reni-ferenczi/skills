# GPlatesQtMsgHandler

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 632 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/GPlatesQtMsgHandler.h` | C++ | 218 |
| `src/app-logic/GPlatesQtMsgHandler.cc` | C++ | 567 |

## Overview

[[[PROSE overview unit=app-logic/GPlatesQtMsgHandler tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::StdOutErrCapture`](#gplatesapplogicstdouterrcapture) | class | `QObject` | — | 0 | Class to capture stdout or stderr (each stream run in a separate QThread) and send captured output back to GPlatesQtMsgHandler so it can pass onto to any registered message handlers. |
| [`GPlatesAppLogic::GPlatesQtMsgHandler`](#gplatesapplogicgplatesqtmsghandler) | class | `QObject`<br>[`GPlatesUtils::Singleton<GPlatesQtMsgHandler>`](../utils/Singleton.md) | — | 0 | A Qt message handler to log qDebug, qWarning, qFatal, etc messages to file and to a log dialog. |

## Members

### `GPlatesAppLogic::StdOutErrCapture`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `StdOutErrCapture()` | constructor | `None` | public | — |
| `~StdOutErrCapture()` | destructor | `None` | public | — |
| `start_capturing( FILE *stream)` | method | `bool` | public | — |
| `capture_messages()` | method | `void` | public | — |
| `stop_capturing()` | method | `void` | public | — |
| `error_reading()` | method | `void` | public | — |
| `output_messages( QStringList)` | method | `void` | public | — |
| `d_is_capturing` | field | `bool` | private | — |
| `d_stream_file_descriptor` | field | `int` | private | — |
| `d_original_stream_file_descriptor` | field | `int` | private | — |
| `d_pipe_read_write_descriptors` | field | `int` | private | — |
| `d_pipe_buffer` | field | `char` | private | — |

### `GPlatesAppLogic::GPlatesQtMsgHandler`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `message_handler_id_type` | typedef | `unsigned int` | private | Typedef for a message handler identifier (so it can be removed after adding). |
| `MessageHandler` | class | `None` | private | Abstract base for a simple handler class that we can use to delegate message handling to a variety of different destinations. |
| `add_log_file_handler( const QString &log_filename = QString())` | method | `void` | private | Convenience function that calls add\_handler with a LogToFileHandler. |
| `add_handler( boost::shared_ptr<MessageHandler> handler)` | method | `message_handler_id_type` | private | Add one of our own MessageHandler derivatives to the list of handlers that can process messages. |
| `remove_handler( message_handler_id_type handler_id)` | method | `void` | private | Remove a message handler added with add\_handler. |
| `s_prev_msg_handler` | field | `QtMessageHandler` | private | Next Qt message handler in the chain of message handlers. |
| `qt_message_handler( QtMsgType msg_type, const QMessageLogContext &context, const QString &msg)` | method | `void` | private | The message handler function called by Qt. |
| `message_handle_list_type` | typedef | `std::list<boost::shared_ptr<MessageHandler> >` | private | Instance member data |
| `d_message_handler_list` | field | `message_handle_list_type` | private | Store all MessageHandler derivations registered with this class, so we can pass the messages to them all. |
| `d_message_handler_iterators` | field | `std::vector<message_handle_list_type::iterator>` | private | Index by message\_handler\_id\_type to find the message handler in d\_message\_handler\_list. |
| `d_stdout_capture_thread` | field | `QThread` | private | — |
| `d_stderr_capture_thread` | field | `QThread` | private | — |
| `handle_qt_message( QtMsgType msg_type, const QString &msg)` | method | `void` | private | This delegates the message to our various MessageHandler derivations. |
| `should_install_message_handler()` | method | `bool` | private | Returns true if should install message handler. |
| `start_capturing_stdout_and_stderr()` | method | `void` | private | Capture low-level stdout and stderr (eg, from our dependency libraries) and log those messages too. |
| `stop_capturing_stdout_and_stderr()` | method | `void` | private | — |
| `handle_stdout_messages( QStringList)` | method | `void` | private | — |
| `handle_stderr_messages( QStringList)` | method | `void` | private | — |
| `handle_stdout_error()` | method | `void` | private | — |
| `handle_stderr_error()` | method | `void` | private | — |
| `capture_stdout_messages()` | method | `void` | public | — |
| `capture_stderr_messages()` | method | `void` | public | — |
| `stop_capturing_stdout()` | method | `void` | public | — |
| `stop_capturing_stderr()` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `s_prev_msg_handler` | variable | `QtMessageHandler` | — |
| `GPLATES_APP_LOGIC_GPLATESQTMSGHANDLER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/GPlatesQtMsgHandler tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/LogModel](LogModel.md) | app-logic | 22 |
| [gui/LogFilterModel](../gui/LogFilterModel.md) | gui | 18 |
| [app-logic/LogToModelHandler](LogToModelHandler.md) | app-logic | 7 |
| [entry-points/gplates_unit_test_main](../entry-points/gplates_unit_test_main.md) | entry-points | 4 |
| [file-io/LogToFileHandler](../file-io/LogToFileHandler.md) | file-io | 4 |
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 3 |

## Related

**Qt signal/slot connections** (12 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_stdout_capture_thread` | `started()` | `stdout_capture.get()` | `capture_messages()` |
| `&d_stderr_capture_thread` | `started()` | `stderr_capture.get()` | `capture_messages()` |
| `&d_stdout_capture_thread` | `finished()` | `stdout_capture.get()` | `deleteLater()` |
| `&d_stderr_capture_thread` | `finished()` | `stderr_capture.get()` | `deleteLater()` |
| `stdout_capture.get()` | `error_reading()` | `this` | `handle_stdout_error()` |
| `stderr_capture.get()` | `error_reading()` | `this` | `handle_stderr_error()` |
| `this` | `stop_capturing_stdout()` | `stdout_capture.get()` | `stop_capturing()` |
| `this` | `stop_capturing_stderr()` | `stderr_capture.get()` | `stop_capturing()` |
| `stdout_capture.get()` | `output_messages(QStringList)` | `this` | `handle_stdout_messages(QStringList)` |
| `stderr_capture.get()` | `output_messages(QStringList)` | `this` | `handle_stderr_messages(QStringList)` |
| `this` | `capture_stdout_messages()` | `stdout_capture.get()` | `capture_messages()` |
| `this` | `capture_stderr_messages()` | `stderr_capture.get()` | `capture_messages()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/GPlatesQtMsgHandler.h
python scripts/gpq.py def GPlatesAppLogic::GPlatesQtMsgHandler --body
python scripts/gpq.py uses GPlatesQtMsgHandler --kind class
python scripts/gpq.py hier GPlatesQtMsgHandler
```

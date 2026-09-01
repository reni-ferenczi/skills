# LogModel

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 848 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/LogModel.h` | C++ | 204 |
| `src/app-logic/LogModel.cc` | C++ | 241 |

## Overview

`LogModel` is a `QAbstractListModel` that backs the application's log viewer: it holds a `QList<LogEntry>` of accumulated messages and exposes them through the standard `data()`/`flags()`/`rowCount()` triad, with `SeverityRole` and `TypeRole` letting a view (`gui/LogFilterModel`, `qt-widgets/LogDialog`) filter and colour entries by `LogEntry::Severity` and `LogEntry::Type` without parsing message text. It deliberately avoids QtGui dependencies so it can sit in app-logic rather than gui/qt-widgets.

On construction it installs a `LogToModelHandler` with `GPlatesQtMsgHandler`, so it becomes the sink for Qt's own debug/warning/critical/fatal message stream in addition to messages appended directly via `append()`; the destructor removes that handler. Because message floods (e.g. from Qt) could otherwise cause a resize/repaint per message, `append()` does not add straight to `d_log`: it queues into `d_buffer` and arms a single-shot `QTimer`, so incoming messages are coalesced into batches (`flush_buffer()`) and further coalesced by `compress_buffer()`, which collapses runs of duplicate messages into a single "repeated N times" placeholder `LogEntry` of type `META`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::LogModel`](#gplatesapplogiclogmodel) | class | `QAbstractListModel`<br>`boost::noncopyable` | — | 0 | Qt Model/View class for a list of log entries. |

## Members

### `GPlatesAppLogic::LogModel`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LogEntry` | class | `None` | public | Inner class to hold details about each entry of the log. |
| `SeverityRole` | field | `int` | public | Roles for data() to use to supply info about the severity and type of log message to a higher-up Qt Model that can filter and colour accordingly. |
| `TypeRole` | field | `int` | public | — |
| `LogModel( QObject *_parent)` | constructor | `None` | public | — |
| `~LogModel()` | destructor | `None` | public | — |
| `append( const LogEntry &entry)` | method | `void` | public | Our accessor for appending new log entries. |
| `data( const QModelIndex &idx, int role = Qt::DisplayRole)` | method | `QVariant` | public | Qt Model/View accessor for data of a LogEntry for assorted roles. |
| `flags( const QModelIndex &idx)` | method | `Qt::ItemFlags` | public | Qt Model/View accessor for item flags of a LogEntry to see how it should behave. |
| `rowCount( const QModelIndex &parent_idx)` | method | `int` | public | Qt Model/View accessor to see how many LogEntries we have. |
| `flush_buffer()` | method | `void` | private | Called after a short period of no further incoming messages, to ensure that large floods of messages get processed as a batch rather than continuous small updates (that can create GUI resize events that slow everything down. |
| `d_log` | field | `QList<LogEntry>` | private | The backend to the model, the log of actual messages. |
| `d_buffer` | field | `QList<LogEntry>` | private | Temporary holding area for inbound messages to protect against flooding. |
| `d_buffer_timeout` | field | `QPointer<QTimer>` | private | Timer used to prevent flooding. |
| `d_message_handler_id` | field | `boost::optional<GPlatesQtMsgHandler::message_handler_id_type>` | private | Handle to the installed message handler so can remove it in destructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `SeverityRole` | variable | `int` | — |
| `TypeRole` | variable | `int` | — |
| `compress_buffer( QList<GPlatesAppLogic::LogModel::LogEntry> &buffer)` | function | `QList<GPlatesAppLogic::LogModel::LogEntry>` | Replace heavily duplicated messages with a single message that indicates how many times the repeat occurred. |
| `GPLATES_APP_LOGIC_LOGMODEL_H` | macro | `None` | — |

## Notes

`append()` does not update the model immediately — an appended entry only becomes visible through `data()`/`rowCount()` after `flush_buffer()` runs (100 ms after the last append, or roughly every 100 ms during a sustained flood once the buffer passes 50 pending entries). Code that appends a message and then expects to read it straight back out of the model will not see it yet.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/LogFilterModel](../gui/LogFilterModel.md) | gui | 53 |
| [app-logic/LogToModelHandler](LogToModelHandler.md) | app-logic | 8 |
| [qt-widgets/LogDialog](../qt-widgets/LogDialog.md) | qt-widgets | 5 |
| [app-logic/PlateVelocityUtils](PlateVelocityUtils.md) | app-logic | 2 |
| [app-logic/ApplicationState](ApplicationState.md) | app-logic | 1 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 1 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_buffer_timeout` | `timeout()` | `this` | `flush_buffer()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/LogModel.h
python scripts/gpq.py def GPlatesAppLogic::LogModel --body
python scripts/gpq.py uses LogModel --kind class
python scripts/gpq.py hier LogModel
```

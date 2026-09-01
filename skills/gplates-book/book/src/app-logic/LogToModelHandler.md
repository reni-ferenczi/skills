# LogToModelHandler

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1679 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/LogToModelHandler.h` | C++ | 70 |
| `src/app-logic/LogToModelHandler.cc` | C++ | 51 |

## Overview

[[[PROSE overview unit=app-logic/LogToModelHandler tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::LogToModelHandler`](#gplatesapplogiclogtomodelhandler) | class | [`GPlatesAppLogic::GPlatesQtMsgHandler::MessageHandler`](GPlatesQtMsgHandler.md) | — | 0 | A derivation of GPlatesQtMsgHandler::MessageHandler that logs messages to the Qt Model GPlatesAppLogic::LogModel, the backend for the GUI Log. |

## Members

### `GPlatesAppLogic::LogToModelHandler`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LogToModelHandler( LogModel &_model)` | constructor | `None` | public | — |
| `~LogToModelHandler()` | destructor | `None` | public | — |
| `handle_qt_message( QtMsgType msg_type, const QString &msg)` | method | `void` | public | — |
| `d_log_model_ptr` | field | `QPointer<LogModel>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_LOGTOMODELHANDLER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/LogToModelHandler tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/LogModel](LogModel.md) | app-logic | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/LogToModelHandler.h
python scripts/gpq.py def GPlatesAppLogic::LogToModelHandler --body
python scripts/gpq.py uses LogToModelHandler --kind class
python scripts/gpq.py hier LogToModelHandler
```

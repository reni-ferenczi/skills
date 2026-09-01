# PythonExecutionMonitorWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 569 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/PythonExecutionMonitorWidget.h` | C++ | 107 |
| `src/qt-widgets/PythonExecutionMonitorWidget.cc` | C++ | 133 |
| `src/qt-widgets/PythonExecutionMonitorWidgetUi.ui` | Qt form | 50 |

## Overview

[[[PROSE overview unit=qt-widgets/PythonExecutionMonitorWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::PythonExecutionMonitorWidget`](#gplatesqtwidgetspythonexecutionmonitorwidget) | class | `QWidget`<br>`Ui_PythonExecutionMonitorWidget` | — | 0 | PythonExecutionMonitorWidget is a widget that appears on screen to allow the user to stop Python execution. |

## Members

### `GPlatesQtWidgets::PythonExecutionMonitorWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PythonExecutionMonitorWidget( GPlatesApi::PythonExecutionThread *python_execution_thread, QWidget *parent_)` | constructor | `None` | public | Constructs a PythonExecutionMonitorWidget with a non-NULL parent\_. |
| `~PythonExecutionMonitorWidget()` | destructor | `None` | public | — |
| `timerEvent( QTimerEvent *ev)` | method | `void` | protected | — |
| `showEvent( QShowEvent *ev)` | method | `void` | protected | — |
| `hideEvent( QHideEvent *ev)` | method | `void` | protected | — |
| `eventFilter( QObject *watched, QEvent *ev)` | method | `bool` | protected | — |
| `handle_cancel_button_clicked()` | method | `void` | private | — |
| `reposition()` | method | `void` | private | — |
| `APPEARANCE_TIME` | field | `int` | private | — |
| `d_python_execution_thread` | field | `GPlatesApi::PythonExecutionThread` | private | — |
| `d_timer` | field | `QBasicTimer` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_PYTHONEXECUTIONMONITORWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/PythonExecutionMonitorWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/PythonConsoleDialog](PythonConsoleDialog.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `PythonExecutionMonitorWidget` | `QWidget` | — | 3 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `cancel_button` | `clicked()` | `this` | `handle_cancel_button_clicked()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/PythonExecutionMonitorWidget.h
python scripts/gpq.py def GPlatesQtWidgets::PythonExecutionMonitorWidget --body
python scripts/gpq.py uses PythonExecutionMonitorWidget --kind class
python scripts/gpq.py hier PythonExecutionMonitorWidget
```

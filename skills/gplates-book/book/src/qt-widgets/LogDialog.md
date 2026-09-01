# LogDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1334 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/LogDialog.h` | C++ | 101 |
| `src/qt-widgets/LogDialog.cc` | C++ | 140 |
| `src/qt-widgets/LogDialogUi.ui` | Qt form | 195 |

## Overview

[[[PROSE overview unit=qt-widgets/LogDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::LogDialog`](#gplatesqtwidgetslogdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_LogDialog` | — | 0 | Simple dialog to show messages which would otherwise go to a terminal window, to aid users who do not start GPlates from a terminal. |

## Members

### `GPlatesQtWidgets::LogDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LogDialog( GPlatesAppLogic::ApplicationState &app_state, QWidget *_parent)` | constructor | `None` | public | — |
| `~LogDialog()` | destructor | `None` | public | — |
| `copy_selection_to_clipboard()` | method | `void` | public | — |
| `handle_filter_typing()` | method | `void` | private | — |
| `handle_filter_changed()` | method | `void` | private | — |
| `handle_selection_changed()` | method | `void` | private | — |
| `d_log_filter_model_ptr` | field | `QPointer<GPlatesGui::LogFilterModel>` | private | This model acts as a proxy between this dialog and the real LogModel. |
| `d_filter_timeout` | field | `QPointer<QTimer>` | private | A find-as-you-type filter that immediately responds to keypresses can be a bit annoying, so we include a small delay before it responds. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_LOGDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/LogDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `LogDialog` | `QDialog` | Log | 10 |

**Qt signal/slot connections** (9 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&app_state.get_log_model()` | `rowsInserted(const QModelIndex &, int, int)` | `listview_log` | `scrollToBottom()` |
| `checkbox_show_debug` | `stateChanged(int)` | `this` | `handle_filter_changed()` |
| `checkbox_show_warning` | `stateChanged(int)` | `this` | `handle_filter_changed()` |
| `checkbox_show_critical` | `stateChanged(int)` | `this` | `handle_filter_changed()` |
| `lineedit_filter` | `textChanged(QString)` | `this` | `handle_filter_typing()` |
| `lineedit_filter` | `returnPressed()` | `this` | `handle_filter_changed()` |
| `d_filter_timeout` | `timeout()` | `this` | `handle_filter_changed()` |
| `listview_log->selectionModel(), // Must come after ->setModel()` | `selectionChanged(const QItemSelection &, const QItemSelection &)` | `this` | `handle_selection_changed()` |
| `button_copy_to_clipboard` | `clicked()` | `this` | `copy_selection_to_clipboard()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/LogDialog.h
python scripts/gpq.py def GPlatesQtWidgets::LogDialog --body
python scripts/gpq.py uses LogDialog --kind class
python scripts/gpq.py hier LogDialog
```

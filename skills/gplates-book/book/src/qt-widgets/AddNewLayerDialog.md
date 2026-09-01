# AddNewLayerDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 682 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/AddNewLayerDialog.h` | C++ | 77 |
| `src/qt-widgets/AddNewLayerDialog.cc` | C++ | 118 |
| `src/qt-widgets/AddNewLayerDialogUi.ui` | Qt form | 80 |

## Overview

[[[PROSE overview unit=qt-widgets/AddNewLayerDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::AddNewLayerDialog`](#gplatesqtwidgetsaddnewlayerdialog) | class | `QDialog`<br>`Ui_AddNewLayerDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::AddNewLayerDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AddNewLayerDialog( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `handle_accept()` | method | `void` | private | — |
| `handle_combobox_index_changed( int index)` | method | `void` | private | — |
| `populate_combobox()` | method | `void` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_ADDNEWLAYERDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/AddNewLayerDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/VisualLayersWidget](VisualLayersWidget.md) | qt-widgets | 6 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `AddNewLayerDialog` | `QDialog` | Add New Layer | 5 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `main_buttonbox` | `accepted()` | `this` | `handle_accept()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |
| `layer_type_combobox` | `currentIndexChanged(int)` | `this` | `handle_combobox_index_changed(int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/AddNewLayerDialog.h
python scripts/gpq.py def GPlatesQtWidgets::AddNewLayerDialog --body
python scripts/gpq.py uses AddNewLayerDialog --kind class
python scripts/gpq.py hier AddNewLayerDialog
```

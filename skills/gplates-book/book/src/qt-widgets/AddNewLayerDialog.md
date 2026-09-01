# AddNewLayerDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 682 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/AddNewLayerDialog.h` | C++ | 77 |
| `src/qt-widgets/AddNewLayerDialog.cc` | C++ | 118 |
| `src/qt-widgets/AddNewLayerDialogUi.ui` | Qt form | 80 |

## Overview

Modal dialog for adding a new visual layer to the reconstruction. The dialog queries `VisualLayerRegistry` for available layer types, populates a combobox with layer names and icons, and displays the description for the currently selected type. On accept, calls `VisualLayerRegistry::create_visual_layer()` with the selected type to instantiate the layer in the layer stack.

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

*None.*

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

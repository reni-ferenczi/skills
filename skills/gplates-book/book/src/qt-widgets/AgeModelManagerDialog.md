# AgeModelManagerDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 330 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/AgeModelManagerDialog.h` | C++ | 103 |
| `src/qt-widgets/AgeModelManagerDialog.cc` | C++ | 311 |
| `src/qt-widgets/AgeModelManagerDialogUi.ui` | Qt form | 113 |

## Overview

Manager dialog for age models used in geological timescale reconstructions. Displays a table of chronostratigraphic intervals (chrons) with ages from one or more loaded age models, allowing users to select which model is active. An Import button loads new age models from `.dat` files via `AgeModelReader`, and changing the active model resets the table and highlights the selected column in yellow. The dialog retrieves the age model collection from `ViewState` and remembers the last-used path via `UserPreferences`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::AgeModelManagerDialog`](#gplatesqtwidgetsagemodelmanagerdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_AgeModelManagerDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::AgeModelManagerDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AgeModelTableFixedColumns` | enum | `None` | public | — |
| `AgeModelManagerDialog( GPlatesPresentation::ViewState &view_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~AgeModelManagerDialog()` | destructor | `None` | public | — |
| `handle_import()` | method | `void` | private | — |
| `handle_combo_box_current_index_changed()` | method | `void` | private | — |
| `setup_widgets()` | method | `void` | private | — |
| `setup_connections()` | method | `void` | private | — |
| `update_dialog()` | method | `void` | private | — |
| `load_file( const QString &filename)` | method | `void` | private | — |
| `d_age_model_collection` | field | `GPlatesAppLogic::AgeModelCollection` | private | — |
| `d_standard_model` | field | `QStandardItemModel` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_open_file_dialog` | field | `boost::scoped_ptr<OpenFileDialog>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `CHRON_COLUMN_WIDTH` | variable | `int` | — |
| `MODEL_COLUMN_WIDTH` | variable | `int` | — |
| `resize_columns( QTableView *table_view, int number_of_models)` | function | `void` | — |
| `add_model_identifiers_to_combo_box( const GPlatesAppLogic::AgeModelCollection &age_model_collection, QComboBox *combo_box)` | function | `void` | — |
| `add_row_to_standard_model( QStandardItemModel *standard_model, const QString &chron, const GPlatesAppLogic::age_model_container_type &models, const GPlatesAppLogic::chron_comment_map_type &chron_comments)` | function | `void` | — |
| `fill_table_model( const GPlatesAppLogic::AgeModelCollection &age_model_collection, QStandardItemModel *standard_model)` | function | `void` | — |
| `highlight_cell( int row, int column, QStandardItemModel *standard_model)` | function | `void` | — |
| `highlight_column( int column, QStandardItemModel *standard_model)` | function | `void` | — |
| `highlight_selected_age_model( QComboBox *combo_box, QStandardItemModel *standard_model)` | function | `void` | — |
| `GPLATES_QTWIDGETS_AGEMODELMANAGERDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `AgeModelManagerDialog` | `QDialog` | Manage Age Models | 8 |

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_import` | `clicked()` | `this` | `handle_import()` |
| `combo_active_model` | `currentIndexChanged(QString)` | `this` | `handle_combo_box_current_index_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/AgeModelManagerDialog.h
python scripts/gpq.py def GPlatesQtWidgets::AgeModelManagerDialog --body
python scripts/gpq.py uses AgeModelManagerDialog --kind class
python scripts/gpq.py hier AgeModelManagerDialog
```

# CoRegistrationResultTableDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 685 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/CoRegistrationResultTableDialog.h` | C++ | 279 |
| `src/qt-widgets/CoRegistrationResultTableDialog.cc` | C++ | 260 |
| `src/qt-widgets/CoRegistrationResultTableDialogUi.ui` | Qt form | 21 |

## Overview

[[[PROSE overview unit=qt-widgets/CoRegistrationResultTableDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ResultTableView`](#gplatesqtwidgetsresulttableview) | class | `QTableView` | — | 0 | — |
| [`GPlatesQtWidgets::ResultTableModel`](#gplatesqtwidgetsresulttablemodel) | class | `QAbstractTableModel` | — | 0 | — |
| [`GPlatesQtWidgets::CoRegistrationResultTableDialog`](#gplatesqtwidgetscoregistrationresulttabledialog) | class | `QDialog`<br>`Ui_CoRegistrationResultTableDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ResultTableView`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ResultTableView( QWidget *_parent)` | constructor | `None` | public | — |
| `contextMenuEvent( QContextMenuEvent *_event)` | method | `void` | public | — |
| `d_highlight_seed_action` | field | `QAction` | protected | — |

### `GPlatesQtWidgets::ResultTableModel`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ResultTableModel( const GPlatesDataMining::DataTable& _data_table, QObject *parent_ = NULL)` | constructor | `None` | public | — |
| `rowCount( const QModelIndex &parent_ = QModelIndex())` | method | `int` | public | — |
| `columnCount( const QModelIndex &parent_ = QModelIndex())` | method | `int` | public | — |
| `flags( const QModelIndex &idx)` | method | `Qt::ItemFlags` | public | — |
| `headerData( int section, Qt::Orientation orientation, int role = Qt::DisplayRole)` | method | `QVariant` | public | — |
| `data( const QModelIndex &idx, int role)` | method | `QVariant` | public | — |
| `d_table` | field | `GPlatesDataMining::DataTable` | protected | — |

### `GPlatesQtWidgets::CoRegistrationResultTableDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CoRegistrationResultTableDialog( GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, boost::weak_ptr<GPlatesPresentation::VisualLayer> visual_layer, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~CoRegistrationResultTableDialog()` | destructor | `None` | public | — |
| `pop_up()` | method | `void` | public | — |
| `set_visual_layer( boost::weak_ptr<GPlatesPresentation::VisualLayer> visual_layer)` | method | `void` | public | — |
| `update()` | method | `void` | public | Retrieves co-registration results from the associated co-registration layer proxy. |
| `reject()` | method | `void` | public | — |
| `highlight_seed()` | method | `void` | public | — |
| `connect_application_state_signals( GPlatesAppLogic::ApplicationState &application_state)` | method | `void` | private | — |
| `update_co_registration_data( const GPlatesDataMining::DataTable &co_registration_data_table)` | method | `void` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_viewport_window` | field | `ViewportWindow` | private | — |
| `d_visual_layer` | field | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | private | — |
| `d_table_model_prt` | field | `boost::scoped_ptr< ResultTableModel >` | private | — |
| `table_view` | field | `QTableView` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_COREGISTRATIONRESULTTABLEDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/CoRegistrationResultTableDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CoRegistrationOptionsWidget](CoRegistrationOptionsWidget.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `CoRegistrationResultTableDialog` | `QDialog` | ResultTableDialog | 1 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_highlight_seed_action` | `triggered()` | `_parent` | `highlight_seed()` |
| `pushButton_close` | `clicked()` | `this` | `reject()` |
| `&application_state` | `reconstructed(GPlatesAppLogic::ApplicationState &)` | `this` | `update()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/CoRegistrationResultTableDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ResultTableModel --body
python scripts/gpq.py uses ResultTableModel --kind class
python scripts/gpq.py hier ResultTableModel
```

# RasterBandPage

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 559 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/RasterBandPage.h` | C++ | 110 |
| `src/qt-widgets/RasterBandPage.cc` | C++ | 248 |
| `src/qt-widgets/RasterBandPageUi.ui` | Qt form | 63 |

## Overview

Wizard page for assigning user-friendly names to raster bands during import. Users enter a name for each band in a table, where edits are managed by a custom `BandNameComboBox` delegate that handles text changes. The page validates that all band names are unique before the wizard can proceed, updating the band names vector passed at construction.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::BandNameDelegate`](#anonymousbandnamedelegate) | class | `QItemDelegate` | — | 0 | — |
| [`GPlatesQtWidgets::RasterBandPage`](#gplatesqtwidgetsrasterbandpage) | class | `QWizardPage`<br>`Ui_RasterBandPage` | — | 0 | — |
| [`GPlatesQtWidgets::RasterBandPageInternals::BandNameComboBox`](#gplatesqtwidgetsrasterbandpageinternalsbandnamecombobox) | class | `QComboBox` | — | 0 | — |

## Members

### `(anonymous)::BandNameDelegate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `BandNameDelegate( QTableWidget *parent_)` | constructor | `None` | public | — |
| `createEditor( QWidget *parent_, const QStyleOptionViewItem &option, const QModelIndex &index)` | method | `QWidget` | public | — |
| `setEditorData( QWidget *editor, const QModelIndex &index)` | method | `void` | public | — |
| `setModelData( QWidget *editor, QAbstractItemModel *model, const QModelIndex &index)` | method | `void` | public | — |
| `d_table` | field | `QTableWidget` | private | — |

### `GPlatesQtWidgets::RasterBandPage`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RasterBandPage( std::vector<QString> &band_names, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `initializePage()` | method | `void` | public | — |
| `isComplete()` | method | `bool` | public | — |
| `handle_table_cell_changed( int row, int column)` | method | `void` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `populate_table()` | method | `void` | private | — |
| `d_band_names` | field | `std::vector<QString>` | private | — |

### `GPlatesQtWidgets::RasterBandPageInternals::BandNameComboBox`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `BandNameComboBox( QTableWidget *table, QWidget *parent_)` | constructor | `None` | public | — |
| `set_model_index( const QModelIndex &model_index)` | method | `void` | public | — |
| `handle_text_changed( const QString &text)` | method | `void` | private | — |
| `d_table` | field | `QTableWidget` | private | — |
| `d_model_index` | field | `QModelIndex` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_RASTERBANDPAGE_H` | macro | `None` | — |

## Notes

The `d_band_names` vector is held by reference; changes persist to the caller's vector. The page validates uniqueness of band names in `isComplete()`; the wizard cannot proceed until all names are distinct.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ImportRasterDialog](ImportRasterDialog.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `RasterBandPage` | `QWizardPage` | WizardPage | 5 |

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `band_names_table` | `cellChanged(int, int)` | `this` | `handle_table_cell_changed(int, int)` |
| `this` | `editTextChanged(const QString &)` | `this` | `handle_text_changed(const QString &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/RasterBandPage.h
python scripts/gpq.py def (anonymous)::BandNameDelegate --body
python scripts/gpq.py uses BandNameDelegate --kind class
python scripts/gpq.py hier BandNameDelegate
```

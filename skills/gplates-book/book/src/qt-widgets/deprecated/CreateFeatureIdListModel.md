# CreateFeatureIdListModel

[Book TOC](../../../TOC.md) · [qt-widgets](../../../components/qt-widgets.md) · cluster Community 652 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/deprecated/CreateFeatureIdListModel.h` | C++ | 104 |
| `src/qt-widgets/deprecated/CreateFeatureIdListModel.cc` | C++ | 134 |

## Overview

A Qt item model that wraps a `QStringList` of feature IDs for display in a list view. The model implements the `QAbstractItemModel` interface with one column showing feature ID strings and supports add, remove, and clear operations. When items are added or removed, the model emits the appropriate Qt signals to notify any attached views.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::CreateFeatureIdListModel`](#gplatesqtwidgetscreatefeatureidlistmodel) | class | `QAbstractItemModel` | — | 0 | — |

## Members

### `GPlatesQtWidgets::CreateFeatureIdListModel`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `index( int row, int column, const QModelIndex &parent = QModelIndex())` | method | `QModelIndex` | public | — |
| `headerData( int section, Qt::Orientation orientation, int role = Qt::DisplayRole)` | method | `QVariant` | public | — |
| `parent( const QModelIndex &child)` | method | `QModelIndex` | public | — |
| `rowCount( const QModelIndex &parent = QModelIndex())` | method | `int` | public | — |
| `columnCount( const QModelIndex &parent = QModelIndex())` | method | `int` | public | — |
| `flags( const QModelIndex &idx)` | method | `Qt::ItemFlags` | public | — |
| `data( const QModelIndex &index, int role = Qt::DisplayRole)` | method | `QVariant` | public | — |
| `add( const QString& feature_id)` | method | `void` | public | — |
| `remove( QModelIndex& index)` | method | `void` | public | — |
| `clear()` | method | `void` | public | — |
| `d_feature_id_list` | field | `QStringList` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_WIDGETS_CREATEFEATUREIDLISTMODEL_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/deprecated/CreateFeatureIdListDialog](CreateFeatureIdListDialog.md) | qt-widgets | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/deprecated/CreateFeatureIdListModel.h
python scripts/gpq.py def GPlatesQtWidgets::CreateFeatureIdListModel --body
python scripts/gpq.py uses CreateFeatureIdListModel --kind class
python scripts/gpq.py hier CreateFeatureIdListModel
```

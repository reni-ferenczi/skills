# CreateFeatureIdListModel

[Book TOC](../../../TOC.md) · [qt-widgets](../../../components/qt-widgets.md) · cluster Community 652 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/deprecated/CreateFeatureIdListModel.h` | C++ | 104 |
| `src/qt-widgets/deprecated/CreateFeatureIdListModel.cc` | C++ | 134 |

## Overview

[[[PROSE overview unit=qt-widgets/deprecated/CreateFeatureIdListModel tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=qt-widgets/deprecated/CreateFeatureIdListModel tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

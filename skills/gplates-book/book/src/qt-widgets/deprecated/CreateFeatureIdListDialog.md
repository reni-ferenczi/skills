# CreateFeatureIdListDialog

[Book TOC](../../../TOC.md) · [qt-widgets](../../../components/qt-widgets.md) · cluster Community 652 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/deprecated/CreateFeatureIdListDialog.h` | C++ | 86 |
| `src/qt-widgets/deprecated/CreateFeatureIdListDialog.cc` | C++ | 176 |
| `src/qt-widgets/deprecated/CreateFeatureIdListDialogUi.ui` | Qt form | 80 |

## Overview

[[[PROSE overview unit=qt-widgets/deprecated/CreateFeatureIdListDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::CreateFeatureIdListDialog`](#gplatesqtwidgetscreatefeatureidlistdialog) | class | `QDialog`<br>`Ui_CreateFeatureIdListDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::CreateFeatureIdListDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CreateFeatureIdListDialog( GPlatesPresentation::ViewState &, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~CreateFeatureIdListDialog()` | destructor | `None` | public | — |
| `handle_add()` | method | `void` | public | — |
| `handle_remove()` | method | `void` | public | — |
| `handle_save()` | method | `void` | public | — |
| `handle_open()` | method | `void` | public | — |
| `handle_selection_change( const QItemSelection &selected, const QItemSelection &deselected)` | method | `void` | public | — |
| `d_current_selection` | field | `QModelIndex` | private | — |
| `d_model` | field | `boost::scoped_ptr< CreateFeatureIdListModel >` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_WIDGETS_CREATEFEATUREIDLISTDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/deprecated/CreateFeatureIdListDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `CreateFeatureIdListDialog` | `QDialog` | Create Feature Id List | 6 |

**Qt signal/slot connections** (5 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `pushButton_add` | `clicked()` | `this` | `handle_add()` |
| `pushButton_remove` | `clicked()` | `this` | `handle_remove()` |
| `pushButton_save_file` | `clicked()` | `this` | `handle_save()` |
| `pushButton_open_file` | `clicked()` | `this` | `handle_open()` |
| `listView->selectionModel()` | `selectionChanged(const QItemSelection &, const QItemSelection &)` | `this` | `handle_selection_change(const QItemSelection &, const QItemSelection &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/deprecated/CreateFeatureIdListDialog.h
python scripts/gpq.py def GPlatesQtWidgets::CreateFeatureIdListDialog --body
python scripts/gpq.py uses CreateFeatureIdListDialog --kind class
python scripts/gpq.py hier CreateFeatureIdListDialog
```

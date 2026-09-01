# ConfigValueDelegate

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 641 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ConfigValueDelegate.h` | C++ | 114 |
| `src/gui/ConfigValueDelegate.cc` | C++ | 135 |

## Overview

[[[PROSE overview unit=gui/ConfigValueDelegate tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ConfigValueDelegate`](#gplatesguiconfigvaluedelegate) | class | `QItemDelegate` | — | 0 | Qt Delegate for use in TableViews created for ConfigBundles and UserPreferences. |

## Members

### `GPlatesGui::ConfigValueDelegate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConfigValueDelegate( QObject *parent_ = NULL)` | constructor | `None` | public | — |
| `~ConfigValueDelegate()` | destructor | `None` | public | — |
| `createEditor( QWidget *parent_widget, const QStyleOptionViewItem &option, const QModelIndex &idx)` | method | `QWidget` | public | The Delegate is used to create an editor widget whenever the user triggers an edit event. |
| `setEditorData( QWidget *editor, const QModelIndex &idx)` | method | `void` | public | Reads data from the Qt model, converting it as appropriate, and writes it to the editor widget. |
| `setModelData( QWidget *editor, QAbstractItemModel *model, const QModelIndex &idx)` | method | `void` | public | Reads data from the edit widget, converting it as appropriate, and writes it to the config model. |
| `updateEditorGeometry( QWidget *editor, const QStyleOptionViewItem &option, const QModelIndex &index)` | method | `void` | public | — |
| `commit_and_close( QWidget *editor)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_CONFIGVALUEDELEGATE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/ConfigValueDelegate tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ConfigGuiUtils](ConfigGuiUtils.md) | gui | 3 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `editor` | `reset_requested(QWidget *)` | `this` | `commit_and_close(QWidget *)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ConfigValueDelegate.h
python scripts/gpq.py def GPlatesGui::ConfigValueDelegate --body
python scripts/gpq.py uses ConfigValueDelegate --kind class
python scripts/gpq.py hier ConfigValueDelegate
```

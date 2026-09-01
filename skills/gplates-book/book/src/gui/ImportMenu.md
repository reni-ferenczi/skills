# ImportMenu

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ImportMenu.h` | C++ | 114 |
| `src/gui/ImportMenu.cc` | C++ | 123 |

## Overview

Manages the Import submenu in the File menu, organizing import operations into sections such as BUILT_IN, RASTER, and SCALAR_FIELD_3D. The submenu is initially hidden and only shown when the first import type is registered. Each import item holds a callback function that is invoked when the menu item is triggered, allowing flexible registration of import operations without hardcoding menu structure.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ImportMenu`](#gplatesguiimportmenu) | class | `QObject` | — | 0 | This class encapsulates operations on the Import submenu on the File menu. |

## Members

### `GPlatesGui::ImportMenu`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Section` | enum | `None` | public | An enumeration of different sections of the Import menu. |
| `ImportMenu( QMenu *import_menu, QMenu *parent_menu, QObject *parent_)` | constructor | `None` | public | Constructs an ImportMenu, given pointers to the import\_menu and its parent\_menu as set up in the ViewportWindow designer. |
| `add_import( Section section, const QString &text, const boost::function< void () > &callback)` | method | `void` | public | Adds an item to the given section of the Import menu, with the given text. |
| `handle_action_triggered( QAction *action)` | method | `void` | private | — |
| `d_import_menu` | field | `QMenu` | private | — |
| `d_parent_menu` | field | `QMenu` | private | — |
| `d_next_action_in_parent_menu` | field | `QAction` | private | Stores the action following the Import menu in its parent menu, so that we know where to reinsert it after we remove it from its parent menu. |
| `d_action_group` | field | `QActionGroup` | private | — |
| `d_section_end_actions` | field | `QAction` | private | An array of actions that are one past the end of the actions for a given section. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_IMPORTMENU_H` | macro | `None` | — |

## Notes

The Import menu is removed from its parent when constructed and only reinserted when the first import item is added; this allows it to remain hidden until needed. All callbacks are stored as `boost::function` objects in the QAction data.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 9 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_action_group` | `triggered(QAction *)` | `this` | `handle_action_triggered(QAction *)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ImportMenu.h
python scripts/gpq.py def GPlatesGui::ImportMenu --body
python scripts/gpq.py uses ImportMenu --kind class
python scripts/gpq.py hier ImportMenu
```

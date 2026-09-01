# UtilitiesMenu

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 870 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/UtilitiesMenu.h` | C++ | 92 |
| `src/gui/UtilitiesMenu.cc` | C++ | 108 |

## Overview

Allows Python scripts to register themselves on the Utilities menu and handles their execution when menu items are selected. The class organizes utilities into category-based submenus managed by `get_category_menu()`; `add_utility()` takes a category, display name, and callback and wires the resulting menu action to `handle_action_triggered()`.

When a user selects a utility from the menu, the class invokes the registered callback, coordinating with `PythonManager` to execute the Python code in the appropriate context.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::UtilitiesMenu`](#gplatesguiutilitiesmenu) | class | `QObject` | — | 0 | This class allows Python scripts to register themselves onto the Utilities menu and handles their execution when a menu item is selected. |

## Members

### `GPlatesGui::UtilitiesMenu`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UtilitiesMenu( QMenu *utilities_menu, QAction *before_action, GPlatesGui::PythonManager& python_manager, QObject *parent_ = NULL)` | constructor | `None` | public | — |
| `~UtilitiesMenu()` | destructor | `None` | public | — |
| `add_utility( const QString &category, const QString &name, const boost::function< void () > &callback)` | method | `void` | public | — |
| `handle_action_triggered()` | method | `void` | private | — |
| `get_category_menu( const QString &category)` | method | `QMenu` | private | — |
| `d_utilities_menu` | field | `QMenu` | private | — |
| `d_before_action` | field | `QAction` | private | — |
| `d_python_manager` | field | `GPlatesGui::PythonManager` | private | — |
| `submenus_map_type` | typedef | `std::map<QString, QMenu *>` | private | — |
| `d_submenus` | field | `submenus_map_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_UTILITIESMENU_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [api/PyApplication](../api/PyApplication.md) | api | 3 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 3 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `new_action` | `triggered()` | `this` | `handle_action_triggered()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/UtilitiesMenu.h
python scripts/gpq.py def GPlatesGui::UtilitiesMenu --body
python scripts/gpq.py uses UtilitiesMenu --kind class
python scripts/gpq.py hier UtilitiesMenu
```

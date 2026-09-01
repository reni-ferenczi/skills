# DockWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 292 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/DockWidget.h` | C++ | 144 |
| `src/qt-widgets/DockWidget.cc` | C++ | 228 |

## Overview

[[[PROSE overview unit=qt-widgets/DockWidget tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::DockWidget`](#gplatesqtwidgetsdockwidget) | class | `QDockWidget` | — | 2 | A wrapper around QDockWidget that adds extra bookkeeping actions that we would otherwise have to add to each dock we create. |

## Members

### `GPlatesQtWidgets::DockWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DockWidget( const QString &title, GPlatesGui::DockState &dock_state, ViewportWindow &main_window, boost::optional<QString> object_name_suffix = boost::none)` | constructor | `None` | public | The object name of this widget is set to "Dock\_" + object\_name\_suffix. |
| `location_changed( GPlatesQtWidgets::DockWidget &self, Qt::DockWidgetArea area, bool floating)` | method | `void` | public | — |
| `dock_at_top()` | method | `void` | public | — |
| `dock_at_bottom()` | method | `void` | public | — |
| `dock_at_left()` | method | `void` | public | — |
| `dock_at_right()` | method | `void` | public | — |
| `tabify_at_top()` | method | `void` | public | — |
| `tabify_at_bottom()` | method | `void` | public | — |
| `tabify_at_left()` | method | `void` | public | — |
| `tabify_at_right()` | method | `void` | public | — |
| `handle_floating_change( bool floating)` | method | `void` | private | — |
| `handle_location_change( Qt::DockWidgetArea area)` | method | `void` | private | — |
| `hide_menu_items_as_appropriate()` | method | `void` | private | Shows/hides dock and 'tabify' menu items based on allowed dock areas and dock configuration state. |
| `set_up_context_menu()` | method | `void` | private | Creates the context menu necessary to help users wrangle their docks into shape. |
| `d_dock_state_ptr` | field | `QPointer<GPlatesGui::DockState>` | private | DockState keeps track of which dock is currently where. |
| `d_action_Dock_At_Top` | field | `QPointer<QAction>` | private | The various context menu actions. |
| `d_action_Dock_At_Bottom` | field | `QPointer<QAction>` | private | — |
| `d_action_Dock_At_Left` | field | `QPointer<QAction>` | private | — |
| `d_action_Dock_At_Right` | field | `QPointer<QAction>` | private | — |
| `d_action_Tabify_At_Top` | field | `QPointer<QAction>` | private | — |
| `d_action_Tabify_At_Bottom` | field | `QPointer<QAction>` | private | — |
| `d_action_Tabify_At_Left` | field | `QPointer<QAction>` | private | — |
| `d_action_Tabify_At_Right` | field | `QPointer<QAction>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_DOCKWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/DockWidget tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/SearchResultsDockWidget](SearchResultsDockWidget.md) | qt-widgets | 7 |
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 6 |
| [qt-widgets/CanvasToolBarDockWidget](CanvasToolBarDockWidget.md) | qt-widgets | 5 |
| [gui/DockState](../gui/DockState.md) | gui | 1 |

## Related

**Qt signal/slot connections** (12 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `this` | `topLevelChanged(bool)` | `this` | `handle_floating_change(bool)` |
| `this` | `dockLocationChanged(Qt::DockWidgetArea)` | `this` | `handle_location_change(Qt::DockWidgetArea)` |
| `d_dock_state_ptr` | `dock_configuration_changed()` | `this` | `hide_menu_items_as_appropriate()` |
| `this` | `allowedAreasChanged(Qt::DockWidgetAreas)` | `this` | `hide_menu_items_as_appropriate()` |
| `d_action_Dock_At_Top` | `triggered()` | `this` | `dock_at_top()` |
| `d_action_Dock_At_Bottom` | `triggered()` | `this` | `dock_at_bottom()` |
| `d_action_Dock_At_Left` | `triggered()` | `this` | `dock_at_left()` |
| `d_action_Dock_At_Right` | `triggered()` | `this` | `dock_at_right()` |
| `d_action_Tabify_At_Top` | `triggered()` | `this` | `tabify_at_top()` |
| `d_action_Tabify_At_Bottom` | `triggered()` | `this` | `tabify_at_bottom()` |
| `d_action_Tabify_At_Left` | `triggered()` | `this` | `tabify_at_left()` |
| `d_action_Tabify_At_Right` | `triggered()` | `this` | `tabify_at_right()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/DockWidget.h
python scripts/gpq.py def GPlatesQtWidgets::DockWidget --body
python scripts/gpq.py uses DockWidget --kind class
python scripts/gpq.py hier DockWidget
```

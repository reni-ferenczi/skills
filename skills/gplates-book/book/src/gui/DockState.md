# DockState

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 866 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/DockState.h` | C++ | 190 |
| `src/gui/DockState.cc` | C++ | 377 |

## Overview

`DockState` keeps `ViewportWindow`'s own bookkeeping about which `GPlatesQtWidgets::DockWidget` currently sits where, out of `ViewportWindow` itself. Qt's `QMainWindow` docking API does not expose which docks are tabified together or which edge each dock occupies, so `DockState` tracks eight `QList<QPointer<DockWidget>>` — one docked list and one tabified list per edge (top, bottom, left, right), plus a floating list — by listening to each registered dock's `location_changed` signal (`register_dock()`) and updating those lists in `react_dockwidget_location_change()`.

`move_dock()` is the intended replacement for calling `ViewportWindow::addDockWidget()`/`tabifyDockWidget()` directly: it consults `can_dock()`/`can_tabify()` and the private `tabify()` helper to decide whether a requested move should tabify the dock with an existing occupant of the target area or simply place it there, falling back to letting Qt resolve the placement when tabification is not applicable. `dock_configuration_changed()` is emitted after every dock move so that menu items reflecting current dock state (e.g. enabling/disabling "move to X" actions) stay in sync.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::DockState`](#gplatesguidockstate) | class | `QObject` | — | 0 | This GUI class tracks all the GPlatesQtWidgets::DockWidget used by GPlates, remembering which docks currently occupy which positions. |

## Members

### `GPlatesGui::DockState`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DockState( GPlatesQtWidgets::ViewportWindow &viewport_window_, QObject *parent_)` | constructor | `None` | public | — |
| `~DockState()` | destructor | `None` | public | — |
| `register_dock( GPlatesQtWidgets::DockWidget &dock)` | method | `void` | public | Adds signal/slot connections to track dock positions. |
| `can_dock( Qt::DockWidgetArea area, const GPlatesQtWidgets::DockWidget &dock)` | method | `bool` | public | Check if docking is possible for given location. |
| `can_tabify( Qt::DockWidgetArea area, const GPlatesQtWidgets::DockWidget &dock)` | method | `bool` | public | Check if tabification with another DockWidget is possible for given location. dock - a reference to the DockWidget that would be tabifying itself into area; this is required since one should not attempt to tabify with oneself. |
| `move_dock( GPlatesQtWidgets::DockWidget &dock, Qt::DockWidgetArea area, bool tabify_as_appropriate)` | method | `void` | public | A replacement for the addDockWidget() etc methods on ViewportWindow (QMainWindow). |
| `dock_configuration_changed()` | method | `void` | public | — |
| `react_dockwidget_location_change( GPlatesQtWidgets::DockWidget &dock, Qt::DockWidgetArea area, bool floating)` | method | `void` | private | — |
| `can_dock( const GPlatesQtWidgets::DockWidget &dock, const QList< QPointer<GPlatesQtWidgets::DockWidget> > &docked_area_list, const QList< QPointer<GPlatesQtWidgets::DockWidget> > &tabified_area_list)` | method | `bool` | private | — |
| `can_tabify( const GPlatesQtWidgets::DockWidget &dock, const QList< QPointer<GPlatesQtWidgets::DockWidget> > &docked_area_list, const QList< QPointer<GPlatesQtWidgets::DockWidget> > &tabified_area_list)` | method | `bool` | private | — |
| `tabify( GPlatesQtWidgets::DockWidget &dock, QList< QPointer<GPlatesQtWidgets::DockWidget> > &docked_area_list, QList< QPointer<GPlatesQtWidgets::DockWidget> > &tabified_area_list)` | method | `bool` | private | — |
| `remove_from_docked_lists( GPlatesQtWidgets::DockWidget *remove)` | method | `void` | private | Remove the given DockWidget from all the 'dock location' lists, typically so that it can be added to a new location. |
| `remove_from_tabified_lists( GPlatesQtWidgets::DockWidget *remove)` | method | `void` | private | Remove the given DockWidget from all the 'tabified' dock area lists. |
| `d_viewport_window_ptr` | field | `QPointer<GPlatesQtWidgets::ViewportWindow>` | private | Pointer to the ViewportWindow so we can access Qt's dock code. |
| `d_floating` | field | `QList< QPointer<GPlatesQtWidgets::DockWidget> >` | private | A list of guarded QPointers to DockWidgets for each area of the main window that docks can reside in. |
| `d_docked_top` | field | `QList< QPointer<GPlatesQtWidgets::DockWidget> >` | private | — |
| `d_docked_bottom` | field | `QList< QPointer<GPlatesQtWidgets::DockWidget> >` | private | — |
| `d_docked_left` | field | `QList< QPointer<GPlatesQtWidgets::DockWidget> >` | private | — |
| `d_docked_right` | field | `QList< QPointer<GPlatesQtWidgets::DockWidget> >` | private | — |
| `d_tabified_top` | field | `QList< QPointer<GPlatesQtWidgets::DockWidget> >` | private | List of dock widgets that are tabified in each dock area. |
| `d_tabified_bottom` | field | `QList< QPointer<GPlatesQtWidgets::DockWidget> >` | private | — |
| `d_tabified_left` | field | `QList< QPointer<GPlatesQtWidgets::DockWidget> >` | private | — |
| `d_tabified_right` | field | `QList< QPointer<GPlatesQtWidgets::DockWidget> >` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_DOCKSTATE_H` | macro | `None` | — |

## Notes

`DockState` does not own the `DockWidget`s it tracks — every list stores `QPointer`s specifically because destruction of a dock is not expected to happen before application exit, but the guarded pointers avoid dangling references if it ever does. `remove_from_tabified_lists()` treats a tabified group of exactly one remaining dock as no longer tabified and clears that list, since tabification is meaningless with a single member. `move_dock()`'s tabify attempt is deliberately tried before the plain-dock fallback, and the actual `tabifyDockWidget()`/`addDockWidget()` call always happens last in each path because it triggers Qt's own `location_changed` signal, which re-enters `DockState` through `react_dockwidget_location_change()` — internal list state must already be consistent before that call.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/DockWidget](../qt-widgets/DockWidget.md) | qt-widgets | 19 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 2 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&dock` | `location_changed( GPlatesQtWidgets::DockWidget &, Qt::DockWidgetArea, bool)` | `this` | `react_dockwidget_location_change( GPlatesQtWidgets::DockWidget &, Qt::DockWidgetArea, bool)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/DockState.h
python scripts/gpq.py def GPlatesGui::DockState --body
python scripts/gpq.py uses DockState --kind class
python scripts/gpq.py hier DockState
```

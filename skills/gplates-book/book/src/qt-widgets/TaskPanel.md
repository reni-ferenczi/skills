# TaskPanel

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 372 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/TaskPanel.h` | C++ | 497 |
| `src/qt-widgets/TaskPanel.cc` | C++ | 550 |

## Overview

[[[PROSE overview unit=qt-widgets/TaskPanel tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::TaskPanel`](#gplatesqtwidgetstaskpanel) | class | `QWidget` | — | 0 | The Xtreme Task Panel - A contextual tabbed interface to expose powerful tasks to manipulate GPlates.... to the XTREME! |

## Members

### `GPlatesQtWidgets::TaskPanel`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Page` | enum | `None` | public | Enumeration of all possible pages (or 'tabs') that the TaskPanel can display. |
| `TaskPanel( GPlatesViewOperations::GeometryBuilder &digitise_geometry_builder, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesCanvasTools::ModifyGeometryState &modify_geometry_state, GPlatesCanvasTools::MeasureDistanceState &measure_distance_state, QAction *undo_action_ptr, QAction *redo_ac ...` | constructor | `None` | public | — |
| `get_clear_action()` | method | `QAction` | public | Gets action shared between all task panel widgets that, when triggered, clears the state of that widget. |
| `choose_tab( GPlatesQtWidgets::TaskPanel::Page page)` | method | `void` | public | Select a particular tab/page and make it visible. |
| `set_tab_enabled( GPlatesQtWidgets::TaskPanel::Page page, bool enabled)` | method | `void` | public | Used to disable (and re-enable) widgets for a particular tab. |
| `choose_feature_tab()` | method | `void` | public | — |
| `choose_digitisation_tab()` | method | `void` | public | — |
| `choose_modify_geometry_tab( bool enable_move_nearby_vertices)` | method | `void` | public | — |
| `choose_modify_pole_tab()` | method | `void` | public | — |
| `choose_move_pole_tab()` | method | `void` | public | — |
| `choose_topology_tools_tab()` | method | `void` | public | — |
| `choose_measure_distance_tab()` | method | `void` | public | — |
| `choose_small_circle_tab()` | method | `void` | public | — |
| `choose_lighting_tab()` | method | `void` | public | — |
| `handle_clear_action_enabled_changed( bool enabled)` | method | `void` | private | — |
| `handle_clear_action_triggered()` | method | `void` | private | — |
| `set_up_ui()` | method | `void` | private | Does the basic tasks that setupUi(this) would do if we were using a Designer-made widget. |
| `set_up_feature_tab( GPlatesPresentation::ViewState &view_state)` | method | `void` | private | Sets up the "Current Feature" tab in the X-Treme Task Panel. |
| `set_up_digitisation_tab()` | method | `void` | private | Sets up the "Digitisation" tab in the eXtreme Task Panel. |
| `set_up_modify_geometry_tab()` | method | `void` | private | Sets up the "Modify Geometry" tab in the eXtreme Task Panel. |
| `set_up_modify_pole_tab()` | method | `void` | private | Sets up the "Modify Pole" tab in the Extr3me Task Panel. |
| `set_up_move_pole_tab()` | method | `void` | private | Sets up the "Move Pole" tab in the Extr3me Task Panel. |
| `set_up_topology_tools_tab()` | method | `void` | private | Sets up the "Topology Tools" tab in the Extra Creamy Task Panel. |
| `set_up_measure_distance_tab()` | method | `void` | private | Sets up the "Measure Distance" tab in the Task Panel. |
| `set_up_small_circle_tab()` | method | `void` | private | Sets up the "Small Circle" tab. |
| `set_up_lighting_tab()` | method | `void` | private | Sets up the "Lighting" tab in the Task Panel. |
| `enable_move_nearby_vertices_widget( bool enable)` | method | `void` | private | Configure the 'modify geometry' tab enable snapping to nearby vertices. |
| `d_stacked_widget_ptr` | field | `QStackedWidget` | private | The QStackedWidget that emulates tab-like behaviour without actual tabs. |
| `d_feature_action_button_box_ptr` | field | `ActionButtonBox` | private | Widget responsible for the buttons in the Feature Tab. |
| `d_snap_nearby_vertices_widget_ptr` | field | `SnapNearbyVerticesWidget` | private | Widget for controls relating to moving nearby vertices |
| `d_clear_action` | field | `QAction` | private | Action shared between all task panel widgets that, when triggered, clears the state of that widget. |
| `(anonymous)` | union | `None` | private | This union allows access to widgets by name and by index. |
| `d_active_widget` | field | `TaskPanelWidget` | private | The task panel widget currently active. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `add_default_layout( QWidget* page)` | function | `QLayout` | For use with set\_up\_xxxx\_tab methods: Adds a standard vertical box layout to the taskpanel page, and returns it for convenience. |
| `add_page_with_title( QStackedWidget* stacked_widget, const QString &title)` | function | `QWidget` | For use with set\_up\_xxxx\_tab methods: Adds a new taskpanel page, and returns it for use. |
| `GPLATES_QTWIDGETS_TASKPANEL_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/TaskPanel tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 19 |
| [gui/GuiDebug](../gui/GuiDebug.md) | gui | 1 |
| [gui/PoleManipulationCanvasToolWorkflow](../gui/PoleManipulationCanvasToolWorkflow.md) | gui | 1 |
| [gui/SmallCircleCanvasToolWorkflow](../gui/SmallCircleCanvasToolWorkflow.md) | gui | 1 |
| [gui/TopologyCanvasToolWorkflow](../gui/TopologyCanvasToolWorkflow.md) | gui | 1 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 1 |
| [gui/ViewCanvasToolWorkflow](../gui/ViewCanvasToolWorkflow.md) | gui | 1 |
| [presentation/Application](../presentation/Application.md) | presentation | 1 |
| [qt-widgets/ReconstructionViewWidget](ReconstructionViewWidget.md) | qt-widgets | 1 |
| [qt-widgets/SnapNearbyVerticesWidget](SnapNearbyVerticesWidget.md) | qt-widgets | 1 |

## Related

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_clear_action` | `triggered()` | `this` | `handle_clear_action_triggered()` |
| `d_active_widget` | `clear_action_enabled_changed(bool)` | `this` | `handle_clear_action_enabled_changed(bool)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/TaskPanel.h
python scripts/gpq.py def GPlatesQtWidgets::TaskPanel --body
python scripts/gpq.py uses TaskPanel --kind class
python scripts/gpq.py hier TaskPanel
```

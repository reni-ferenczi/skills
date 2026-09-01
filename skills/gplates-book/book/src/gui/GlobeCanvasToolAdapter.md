# GlobeCanvasToolAdapter

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 440 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/GlobeCanvasToolAdapter.h` | C++ | 156 |
| `src/gui/GlobeCanvasToolAdapter.cc` | C++ | 399 |

## Overview

An adapter that bridges `GlobeCanvas` mouse signals to the `GlobeCanvasTool` interface. It manages connections and disconnections between the globe canvas and an active canvas tool, and routes mouse events (press, click, drag, release, move) to the appropriate tool methods based on the mouse button and keyboard modifiers (Shift, Ctrl, Shift+Ctrl). Different button/modifier combinations are dispatched to different tool methods: `handle_left_click()`, `handle_shift_left_click()`, `handle_ctrl_left_click()`, and corresponding drag/press/move variants.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::GlobeCanvasToolAdapter`](#gplatesguiglobecanvastooladapter) | class | `QObject`<br>`boost::noncopyable` | — | 0 | This class adapts the interface of GlobeCanvasTool to the interface expected by the mouse-click and mouse-drag signals of GlobeCanvas and directs them to the activate canvas tool. |

## Members

### `GPlatesGui::GlobeCanvasToolAdapter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GlobeCanvasToolAdapter( GPlatesQtWidgets::GlobeCanvas &globe_canvas)` | constructor | `None` | public | Construct a GlobeCanvasToolAdapter instance. |
| `~GlobeCanvasToolAdapter()` | destructor | `None` | public | — |
| `activate_canvas_tool( GlobeCanvasTool &globe_canvas_tool)` | method | `void` | public | Connects mouse signals from GlobeCanvas to the specified canvas tool. |
| `deactivate_canvas_tool()` | method | `void` | public | Disconnects mouse signals from GlobeCanvas to the currently active canvas tool. |
| `handle_press( const GPlatesMaths::PointOnSphere &press_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_press_pos_on_globe, bool is_on_globe, Qt::MouseButton button, Qt::KeyboardModifiers modifiers)` | method | `void` | private | — |
| `handle_click( const GPlatesMaths::PointOnSphere &click_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_click_pos_on_globe, bool is_on_globe, Qt::MouseButton button, Qt::KeyboardModifiers modifiers)` | method | `void` | private | — |
| `handle_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GPlatesMaths::Poin ...` | method | `void` | private | — |
| `handle_release_after_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GPla ...` | method | `void` | private | — |
| `handle_move_without_drag( const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GPlatesMaths::PointOnSphere &oriented_centre_of_viewport)` | method | `void` | private | The mouse position moved but the left mouse button is NOT down. |
| `d_globe_canvas` | field | `GPlatesQtWidgets::GlobeCanvas` | private | — |
| `d_active_globe_canvas_tool` | field | `boost::optional<GlobeCanvasTool &>` | private | — |
| `connect_to_globe_canvas()` | method | `void` | private | Connects to mouse signals from the globe canvas. |
| `disconnect_from_globe_canvas()` | method | `void` | private | Disconnects from mouse signals from the globe canvas. |
| `get_active_globe_canvas_tool` | field | `GlobeCanvasTool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_GLOBECANVASTOOLADAPTER_H` | macro | `None` | — |

## Notes

At most one tool can be active at a time; activating a new tool while one is active replaces the old tool without an explicit deactivate. Connections to the globe canvas are only established when the first tool is activated and are only disconnected when the last tool is deactivated.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/CanvasToolWorkflow](CanvasToolWorkflow.md) | gui | 7 |
| [gui/DigitisationCanvasToolWorkflow](DigitisationCanvasToolWorkflow.md) | gui | 1 |
| [gui/FeatureInspectionCanvasToolWorkflow](FeatureInspectionCanvasToolWorkflow.md) | gui | 1 |
| [gui/HellingerCanvasToolWorkflow](HellingerCanvasToolWorkflow.md) | gui | 1 |
| [gui/PoleManipulationCanvasToolWorkflow](PoleManipulationCanvasToolWorkflow.md) | gui | 1 |
| [gui/SmallCircleCanvasToolWorkflow](SmallCircleCanvasToolWorkflow.md) | gui | 1 |
| [gui/TopologyCanvasToolWorkflow](TopologyCanvasToolWorkflow.md) | gui | 1 |
| [gui/ViewCanvasToolWorkflow](ViewCanvasToolWorkflow.md) | gui | 1 |

## Related

**Qt signal/slot connections** (5 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_globe_canvas` | `mouse_pressed( const GPlatesMaths::PointOnSphere &, const GPlatesMaths::PointOnSphere &, bool, Qt::MouseButton, Qt::KeyboardModifiers)` | `this` | `handle_press( const GPlatesMaths::PointOnSphere &, const GPlatesMaths::PointOnSphere &, bool, Qt::MouseButton, Qt::KeyboardModifiers)` |
| `&d_globe_canvas` | `mouse_clicked( const GPlatesMaths::PointOnSphere &, const GPlatesMaths::PointOnSphere &, bool, Qt::MouseButton, Qt::KeyboardModifiers)` | `this` | `handle_click( const GPlatesMaths::PointOnSphere &, const GPlatesMaths::PointOnSphere &, bool, Qt::MouseButton, Qt::KeyboardModifiers)` |
| `&d_globe_canvas` | `mouse_dragged( const GPlatesMaths::PointOnSphere &, const GPlatesMaths::PointOnSphere &, bool, const GPlatesMaths::PointOnSphere &, const GPlatesMaths::PointOnSphere &, bool, const GPlatesMaths::Point` | `this` | `handle_drag( const GPlatesMaths::PointOnSphere &, const GPlatesMaths::PointOnSphere &, bool, const GPlatesMaths::PointOnSphere &, const GPlatesMaths::PointOnSphere &, bool, const GPlatesMaths::PointOn` |
| `&d_globe_canvas` | `mouse_released_after_drag( const GPlatesMaths::PointOnSphere &, const GPlatesMaths::PointOnSphere &, bool, const GPlatesMaths::PointOnSphere &, const GPlatesMaths::PointOnSphere &, bool, const GPlates` | `this` | `handle_release_after_drag( const GPlatesMaths::PointOnSphere &, const GPlatesMaths::PointOnSphere &, bool, const GPlatesMaths::PointOnSphere &, const GPlatesMaths::PointOnSphere &, bool, const GPlates` |
| `&d_globe_canvas` | `mouse_moved_without_drag( const GPlatesMaths::PointOnSphere &, const GPlatesMaths::PointOnSphere &, bool, const GPlatesMaths::PointOnSphere &)` | `this` | `handle_move_without_drag( const GPlatesMaths::PointOnSphere &, const GPlatesMaths::PointOnSphere &, bool, const GPlatesMaths::PointOnSphere &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/GlobeCanvasToolAdapter.h
python scripts/gpq.py def GPlatesGui::GlobeCanvasToolAdapter --body
python scripts/gpq.py uses GlobeCanvasToolAdapter --kind class
python scripts/gpq.py hier GlobeCanvasToolAdapter
```

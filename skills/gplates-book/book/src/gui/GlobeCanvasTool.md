# GlobeCanvasTool

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 403 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/GlobeCanvasTool.h` | C++ | 578 |
| `src/gui/GlobeCanvasTool.cc` | C++ | 188 |

## Overview

[[[PROSE overview unit=gui/GlobeCanvasTool tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::GlobeCanvasTool`](#gplatesguiglobecanvastool) | class | `boost::noncopyable` | — | 5 | This class is the abstract base of all canvas tools. |

## Members

### `GPlatesGui::GlobeCanvasTool`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GlobeCanvasTool( Globe &globe_, GPlatesQtWidgets::GlobeCanvas &globe_canvas_)` | constructor | `None` | public | Construct a GlobeCanvasTool instance. |
| `~GlobeCanvasTool()` | destructor | `None` | public | — |
| `handle_activation()` | method | `void` | public | Handle the activation (selection) of this tool. |
| `handle_deactivation()` | method | `void` | public | Handle the deactivation of this tool (a different tool has been selected). |
| `handle_left_press( const GPlatesMaths::PointOnSphere &press_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_press_pos_on_globe, bool is_on_globe)` | method | `void` | public | Handle a left mouse-button press. press\_pos\_on\_globe is the position of the click on the globe, without taking the globe-orientation into account: (0, 0) is always in the centre of the canvas; (0, -90) is always on the left-most point of ... |
| `handle_left_click( const GPlatesMaths::PointOnSphere &click_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_click_pos_on_globe, bool is_on_globe)` | method | `void` | public | Handle a left mouse-button click. click\_pos\_on\_globe is the position of the click on the globe, without taking the globe-orientation into account: (0, 0) is always in the centre of the canvas; (0, -90) is always on the left-most point of ... |
| `handle_left_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GPlatesMaths: ...` | method | `void` | public | Handle a mouse drag with the left mouse-button pressed. initial\_pos\_on\_globe is the position on the globe (without taking globe-orientation into account) at which the mouse pointer was located when the mouse button was pressed and held. ... |
| `handle_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const ...` | method | `void` | public | Handle the release of the left-mouse button after a mouse drag. initial\_pos\_on\_globe is the position on the globe (without taking globe-orientation into account) at which the mouse pointer was located when the mouse button was pressed and ... |
| `handle_shift_left_click( const GPlatesMaths::PointOnSphere &click_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_click_pos_on_globe, bool is_on_globe)` | method | `void` | public | Handle a left mouse-button click while a Shift key is held. |
| `handle_shift_left_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GPlates ...` | method | `void` | public | Handle a mouse drag with the left mouse-button pressed while a Shift key is held. |
| `handle_shift_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, ...` | method | `void` | public | Handle the release of the left-mouse button after a mouse drag while a Shift key is held. |
| `handle_ctrl_left_click( const GPlatesMaths::PointOnSphere &click_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_click_pos_on_globe, bool is_on_globe)` | method | `void` | public | Handle a left mouse-button click while a Control key is held. |
| `handle_ctrl_left_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GPlatesM ...` | method | `void` | public | Handle a mouse drag with the left mouse-button pressed while a Control key is held. |
| `handle_ctrl_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, ...` | method | `void` | public | Handle the release of the left-mouse button after a mouse drag while a Control key is held. |
| `handle_shift_ctrl_left_click( const GPlatesMaths::PointOnSphere &click_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_click_pos_on_globe, bool is_on_globe)` | method | `void` | public | Handle a left mouse-button click while a Shift key and a Control key are held. |
| `handle_shift_ctrl_left_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GP ...` | method | `void` | public | Handle a mouse drag with the left mouse-button pressed while a Shift key and a Control key are held. |
| `handle_shift_ctrl_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_g ...` | method | `void` | public | Handle the release of the left-mouse button after a mouse drag while a Shift key and Control key are held. |
| `handle_move_without_drag( const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GPlatesMaths::PointOnSphere &oriented_centre_of_viewport)` | method | `void` | public | Handle a mouse movement when left mouse-button is NOT down. |
| `reorient_globe_by_drag_update( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const ...` | method | `void` | protected | Re-orient the globe by dragging the mouse pointer. |
| `reorient_globe_by_drag_release( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const ...` | method | `void` | protected | Re-orient the globe by dragging the mouse pointer. |
| `rotate_globe_by_drag_update( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GP ...` | method | `void` | protected | Rotate the globe around the centre of the viewport by dragging the mouse pointer. |
| `rotate_globe_by_drag_release( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const G ...` | method | `void` | protected | Rotate the globe around the centre of the viewport by dragging the mouse pointer. |
| `d_globe_ptr` | field | `Globe` | private | The globe which will be re-oriented by globe re-orientation operations. |
| `d_globe_canvas_ptr` | field | `GPlatesQtWidgets::GlobeCanvas` | private | The globe canvas which will need to be updated after globe re-orientation. |
| `d_is_in_reorientation_op` | field | `bool` | private | Whether or not this canvas tool is currently in the midst of a globe re-orientation operation. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_closest_point_on_horizon( const GPlatesMaths::PointOnSphere &oriented_point_within_horizon, const GPlatesMaths::PointOnSphere &oriented_center_of_viewport)` | function | `boost::optional<GPlatesMaths::PointOnSphere>` | — |
| `GPLATES_GUI_GLOBECANVASTOOL_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/GlobeCanvasTool tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/ChangeLightDirectionGlobe](../canvas-tools/ChangeLightDirectionGlobe.md) | canvas-tools | 140 |
| [canvas-tools/ReorientGlobe](../canvas-tools/ReorientGlobe.md) | canvas-tools | 90 |
| [canvas-tools/MovePoleGlobe](../canvas-tools/MovePoleGlobe.md) | canvas-tools | 56 |
| [canvas-tools/ManipulatePole](../canvas-tools/ManipulatePole.md) | canvas-tools | 52 |
| [gui/GlobeCanvasToolAdapter](GlobeCanvasToolAdapter.md) | gui | 51 |
| [canvas-tools/ZoomGlobe](../canvas-tools/ZoomGlobe.md) | canvas-tools | 30 |
| [gui/DigitisationCanvasToolWorkflow](DigitisationCanvasToolWorkflow.md) | gui | 11 |
| [gui/FeatureInspectionCanvasToolWorkflow](FeatureInspectionCanvasToolWorkflow.md) | gui | 10 |
| [gui/TopologyCanvasToolWorkflow](TopologyCanvasToolWorkflow.md) | gui | 8 |
| [canvas-tools/CanvasToolAdapterForGlobe](../canvas-tools/CanvasToolAdapterForGlobe.md) | canvas-tools | 7 |
| [gui/CanvasToolWorkflow](CanvasToolWorkflow.md) | gui | 7 |
| [gui/PoleManipulationCanvasToolWorkflow](PoleManipulationCanvasToolWorkflow.md) | gui | 6 |
| [gui/ViewCanvasToolWorkflow](ViewCanvasToolWorkflow.md) | gui | 6 |
| [gui/HellingerCanvasToolWorkflow](HellingerCanvasToolWorkflow.md) | gui | 5 |
| [gui/SmallCircleCanvasToolWorkflow](SmallCircleCanvasToolWorkflow.md) | gui | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/GlobeCanvasTool.h
python scripts/gpq.py def GPlatesGui::GlobeCanvasTool --body
python scripts/gpq.py uses GlobeCanvasTool --kind class
python scripts/gpq.py hier GlobeCanvasTool
```

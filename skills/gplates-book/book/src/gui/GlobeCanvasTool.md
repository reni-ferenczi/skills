# GlobeCanvasTool

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 403 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/GlobeCanvasTool.h` | C++ | 578 |
| `src/gui/GlobeCanvasTool.cc` | C++ | 188 |

## Overview

`GlobeCanvasTool` is the abstract state in a State pattern: exactly one instance
is active at a time, and it defines what the mouse does on the 3-D globe. The
whole interface is a grid of virtual handlers — press, click, drag and
release-after-drag, crossed with no modifier, Shift, Ctrl, and Shift+Ctrl, plus
activation, deactivation and bare mouse movement — every one of which has a
default body, so a subclass overrides only the gestures it actually cares about.
`GPlatesGui::GlobeCanvasToolAdapter` is what turns Qt mouse signals from
`GPlatesQtWidgets::GlobeCanvas` into these calls: it holds one active tool at a
time and connects or disconnects the canvas signals in
`activate_canvas_tool()` / `deactivate_canvas_tool()`, which the
`CanvasToolWorkflow` classes drive when the user picks a tool from the toolbar.

The parameter convention repeated across the handlers is the important part to get
right when writing a subclass. Every position arrives twice: the unoriented
`*_pos_on_globe`, in which the centre of the canvas is always (0, 0) regardless of
how the globe is turned, and the `oriented_*_pos_on_globe`, which is the same
screen point mapped through the current globe orientation. Hit-testing against
real geometry uses the oriented position; screen-space work such as the proximity
threshold for a click uses the unoriented one. The accompanying `is_on_globe` /
`was_on_globe` flag is false when the pointer is off the sphere, in which case the
positions are the nearest points on the globe rather than nothing — a subclass
that ignores the flag will silently act on the limb of the globe.

The base class is not purely abstract: it also implements globe navigation, which
is why every tool inherits it rather than a bare interface. Ctrl+drag defaults to
`reorient_globe_by_drag_*` and Shift+Ctrl+drag to `rotate_globe_by_drag_*`, so
those two gestures work identically under every tool unless a subclass
deliberately overrides them. Both go through `GPlatesGui::Globe` onto
`GlobeOrientation`, whose model is a "handle" planted on the sphere at the press
point and then dragged: `set_new_handle_at_pos()` once, `move_handle_to_pos()` on
every update. Rotation-about-the-viewport-centre reuses the same machinery by
projecting the mouse position onto the horizon circle with the file-local
`get_closest_point_on_horizon()` and dragging *that* point instead, so a
twist gesture becomes an ordinary handle drag. Subclasses split into two
families: real tools such as `GPlatesCanvasTools::ReorientGlobe`, `ZoomGlobe`,
`MovePoleGlobe` and `ChangeLightDirectionGlobe`, and
`GPlatesCanvasTools::CanvasToolAdapterForGlobe`, which wraps a projection-agnostic
`GPlatesCanvasTools::CanvasTool` so that one tool implementation can serve both
the globe and the map.

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

**The class comment is stale.** It says the active tool is referenced by a
`GlobeCanvasToolChoice`; no such class exists in this tree any more. Activation is
now `GlobeCanvasToolAdapter::activate_canvas_tool()`, called from
`CanvasToolWorkflow::activate_selected_tool()`, which activates the globe and map
tools as a pair.

**Ownership is borrowed, and the base class does not check it.** `Globe` and
`GlobeCanvas` are taken by reference and stored as raw pointers that are never
null-checked and never reseated; both outlive the tool, which lives only as long
as its workflow. The class is `boost::noncopyable` and the destructor is pure
virtual with an out-of-line definition, so it cannot be instantiated but derived
destructors still chain correctly.

**`d_is_in_reorientation_op` is the drag state machine, and it is per-tool.** The
`*_update` functions plant the handle on the first call and leave the flag set;
only the `*_release` functions clear it. Two consequences. First, if a subclass
overrides the Ctrl+drag *update* handler but not the matching *release* handler
(or the reverse), the flag desynchronises and the next drag will move a stale
handle instead of planting a new one — override both halves or neither. Second,
the flag lives on the tool instance, so switching tools mid-drag abandons an
in-progress reorientation with the flag still true.

**The `in_mouse_drag` argument is asymmetric on purpose.**
`reorient_globe_by_drag_update()` passes `true` to `Globe::update_handle_pos()`
while `rotate_globe_by_drag_update()` does not. The in-code reason is that the
flag must only be raised when a release event is guaranteed to lower it again,
otherwise the globe stays stuck in the "orientation changing during mouse drag"
state.

**Rotation silently no-ops at the viewport centre.** `get_closest_point_on_horizon()`
returns `boost::none` when the point is collinear with the centre of the viewport,
and both rotate functions then return without touching the handle *and without
clearing `d_is_in_reorientation_op`*. Dragging out from dead centre therefore does
nothing until the pointer moves off the axis.

**The rotate handlers ignore `oriented_centre_of_viewport`.** They use a
file-static `PointOnSphere` at lat/lon (0, 0) as the viewport centre rather than
the parameter they were passed, which is correct only because the unoriented
coordinate frame is defined with the canvas centre at (0, 0). Any subclass that
reasons about the passed-in centre must use the oriented frame consistently.

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

# MapCanvasTool

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 63 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/MapCanvasTool.h` | C++ | 414 |
| `src/gui/MapCanvasTool.cc` | C++ | 148 |

## Overview

[[[PROSE overview unit=gui/MapCanvasTool tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::MapCanvasTool`](#gplatesguimapcanvastool) | class | `boost::noncopyable` | — | 5 | This class is the abstract base of all map canvas tools. |

## Members

### `GPlatesGui::MapCanvasTool`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MapCanvasTool( GPlatesQtWidgets::MapCanvas &map_canvas_, GPlatesQtWidgets::MapView &map_view_, MapTransform &map_transform_)` | constructor | `None` | public | Construct a MapCanvasTool instance. |
| `~MapCanvasTool()` | destructor | `None` | public | — |
| `handle_activation()` | method | `void` | public | Handle the activation (selection) of this tool. |
| `handle_deactivation()` | method | `void` | public | Handle the deactivation of this tool (a different tool has been selected). |
| `handle_left_press( const QPointF &click_point_on_scene, bool is_on_surface)` | method | `void` | public | Handle a left mouse-button press. click\_point\_on\_scene is the QPointF containing coordinates of the click point in the QGraphicsScene. is\_on\_surface is true if the click point is on the surface of the map. |
| `handle_left_click( const QPointF &click_point_on_scene, bool is_on_surface)` | method | `void` | public | Handle a left mouse-button click. click\_point\_on\_scene is the QPointF containing coordinates of the click point in the QGraphicsScene. is\_on\_surface is true if the click point is on the surface of the map. |
| `handle_left_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation)` | method | `void` | public | Handle a mouse drag with the left mouse-button pressed. |
| `handle_left_release_after_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation)` | method | `void` | public | Handle the release of the left-mouse button after a mouse drag. |
| `handle_shift_left_click( const QPointF &click_point_on_scene, bool is_on_surface)` | method | `void` | public | Handle a left mouse-button click while a Shift key is held. |
| `handle_shift_left_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation)` | method | `void` | public | Handle a mouse drag with the left mouse-button pressed while a Shift key is held. |
| `handle_shift_left_release_after_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface)` | method | `void` | public | Handle the release of the left-mouse button after a mouse drag while a Shift key is held. |
| `handle_ctrl_left_click( const QPointF &click_point_on_scene, bool is_on_surface)` | method | `void` | public | Handle a left mouse-button click while a Control key is held. |
| `handle_ctrl_left_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation)` | method | `void` | public | Handle a mouse drag with the left mouse-button pressed while a Control key is held. |
| `handle_ctrl_left_release_after_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface)` | method | `void` | public | Handle the release of the left-mouse button after a mouse drag while a Control key is held. |
| `handle_shift_ctrl_left_click( const QPointF &click_point_on_scene, bool is_on_surface)` | method | `void` | public | Handle a left mouse-button click while a Shift key and a Control key are held. |
| `handle_shift_ctrl_left_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation)` | method | `void` | public | Handle a mouse drag with the left mouse-button pressed while a Shift key and a Control key are held. |
| `handle_move_without_drag( const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation)` | method | `void` | public | Handle a mouse movement when left mouse-button is NOT down. |
| `qpointf_to_point_on_sphere( const QPointF &point, const GPlatesGui::MapProjection &projection)` | method | `boost::optional<GPlatesMaths::PointOnSphere>` | protected | Converts a QPointF to a PointOnSphere. |
| `rotate_map_by_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation)` | method | `void` | protected | Re-orient the map by dragging the mouse pointer. |
| `d_map_view_ptr` | field | `GPlatesQtWidgets::MapView` | private | The map view. |
| `d_map_canvas_ptr` | field | `GPlatesQtWidgets::MapCanvas` | private | The map canvas. |
| `d_map_transform_ptr` | field | `MapTransform` | private | Used for notifying maps of transformations |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `angle_between_vectors( const QPointF &v1, const QPointF &v2)` | function | `double` | — |
| `GPLATES_GUI_MAPCANVASTOOL_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/MapCanvasTool tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/MapCanvasToolAdapter](MapCanvasToolAdapter.md) | gui | 16 |
| [canvas-tools/MovePoleMap](../canvas-tools/MovePoleMap.md) | canvas-tools | 15 |
| [canvas-tools/CanvasToolAdapterForMap](../canvas-tools/CanvasToolAdapterForMap.md) | canvas-tools | 13 |
| [gui/DigitisationCanvasToolWorkflow](DigitisationCanvasToolWorkflow.md) | gui | 10 |
| [gui/FeatureInspectionCanvasToolWorkflow](FeatureInspectionCanvasToolWorkflow.md) | gui | 9 |
| [gui/TopologyCanvasToolWorkflow](TopologyCanvasToolWorkflow.md) | gui | 8 |
| [gui/PoleManipulationCanvasToolWorkflow](PoleManipulationCanvasToolWorkflow.md) | gui | 6 |
| [gui/ViewCanvasToolWorkflow](ViewCanvasToolWorkflow.md) | gui | 6 |
| [gui/HellingerCanvasToolWorkflow](HellingerCanvasToolWorkflow.md) | gui | 5 |
| [canvas-tools/PanMap](../canvas-tools/PanMap.md) | canvas-tools | 4 |
| [gui/SmallCircleCanvasToolWorkflow](SmallCircleCanvasToolWorkflow.md) | gui | 4 |
| [canvas-tools/ChangeLightDirectionMap](../canvas-tools/ChangeLightDirectionMap.md) | canvas-tools | 3 |
| [canvas-tools/ZoomMap](../canvas-tools/ZoomMap.md) | canvas-tools | 3 |
| [gui/CanvasToolWorkflow](CanvasToolWorkflow.md) | gui | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/MapCanvasTool.h
python scripts/gpq.py def GPlatesGui::MapCanvasTool --body
python scripts/gpq.py uses MapCanvasTool --kind class
python scripts/gpq.py hier MapCanvasTool
```

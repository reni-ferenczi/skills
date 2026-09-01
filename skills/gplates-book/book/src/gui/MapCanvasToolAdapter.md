# MapCanvasToolAdapter

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 525 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/MapCanvasToolAdapter.h` | C++ | 143 |
| `src/gui/MapCanvasToolAdapter.cc` | C++ | 376 |

## Overview

[[[PROSE overview unit=gui/MapCanvasToolAdapter tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::MapCanvasToolAdapter`](#gplatesguimapcanvastooladapter) | class | `QObject` | — | 0 | This class adapts the interface of MapCanvasTool to the interface expected by the mouse-click and mouse-drag signals of MapView and directs them to the activate canvas tool. |

## Members

### `GPlatesGui::MapCanvasToolAdapter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MapCanvasToolAdapter( GPlatesQtWidgets::MapView &map_view)` | constructor | `None` | public | Construct a MapCanvasToolAdapter instance. |
| `~MapCanvasToolAdapter()` | destructor | `None` | public | — |
| `activate_canvas_tool( MapCanvasTool &map_canvas_tool)` | method | `void` | public | Connects mouse signals from MapView to the specified canvas tool. |
| `deactivate_canvas_tool()` | method | `void` | public | Disconnects mouse signals from MapView to the currently active canvas tool. |
| `handle_press( const QPointF &clicked_point_on_scene, bool is_on_surface, Qt::MouseButton button, Qt::KeyboardModifiers modifiers)` | method | `void` | private | — |
| `handle_click( const QPointF &clicked_point_on_scene, bool is_on_surface, Qt::MouseButton button, Qt::KeyboardModifiers modifiers)` | method | `void` | private | — |
| `handle_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, Qt::MouseButton button, Qt::KeyboardModifiers modifiers, const QPointF &translation)` | method | `void` | private | — |
| `handle_release_after_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation, Qt::MouseButton button, Qt::KeyboardModifiers modifiers)` | method | `void` | private | — |
| `handle_move_without_drag( const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation)` | method | `void` | private | The mouse position moved but the left mouse button is NOT down. |
| `d_map_view` | field | `GPlatesQtWidgets::MapView` | private | — |
| `d_active_map_canvas_tool` | field | `boost::optional<MapCanvasTool &>` | private | — |
| `connect_to_map_view()` | method | `void` | private | Connects to mouse signals from the map view. |
| `disconnect_from_map_view()` | method | `void` | private | Disconnects from mouse signals from the map view. |
| `get_active_map_canvas_tool` | field | `MapCanvasTool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_MAPCANVASTOOLADAPTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/MapCanvasToolAdapter tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/MapRenderedGeometryLayerPainter](MapRenderedGeometryLayerPainter.md) | gui | 68 |
| [canvas-tools/CanvasToolAdapterForMap](../canvas-tools/CanvasToolAdapterForMap.md) | canvas-tools | 62 |
| [gui/MapCanvasTool](MapCanvasTool.md) | gui | 42 |
| [qt-widgets/MapView](../qt-widgets/MapView.md) | qt-widgets | 24 |
| [gui/MapProjection](MapProjection.md) | gui | 20 |
| [opengl/GLFilledPolygonsMapView](../opengl/GLFilledPolygonsMapView.md) | opengl | 19 |
| [canvas-tools/MovePoleMap](../canvas-tools/MovePoleMap.md) | canvas-tools | 16 |
| [maths/AzimuthalEqualAreaProjection](../maths/AzimuthalEqualAreaProjection.md) | maths | 13 |
| [canvas-tools/PanMap](../canvas-tools/PanMap.md) | canvas-tools | 12 |
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 11 |
| [maths/GnomonicProjection](../maths/GnomonicProjection.md) | maths | 11 |
| [view-operations/MovePoleOperation](../view-operations/MovePoleOperation.md) | view-operations | 8 |
| [gui/FeedbackOpenGLToQPainter](FeedbackOpenGLToQPainter.md) | gui | 7 |
| [canvas-tools/ZoomMap](../canvas-tools/ZoomMap.md) | canvas-tools | 6 |
| [qt-widgets/KinematicGraphPicker](../qt-widgets/KinematicGraphPicker.md) | qt-widgets | 5 |
| [gui/CanvasToolWorkflow](CanvasToolWorkflow.md) | gui | 3 |
| [maths/PolygonOrientation](../maths/PolygonOrientation.md) | maths | 3 |
| [gui/MapTransform](MapTransform.md) | gui | 2 |
| [qt-widgets/KinematicGraphsDialog](../qt-widgets/KinematicGraphsDialog.md) | qt-widgets | 2 |
| [app-logic/ResolvedTriangulationDelaunay2](../app-logic/ResolvedTriangulationDelaunay2.md) | app-logic | 1 |

*... and 1 more units.*

## Related

**Qt signal/slot connections** (5 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_map_view` | `mouse_pressed( const QPointF &, bool, Qt::MouseButton, Qt::KeyboardModifiers)` | `this` | `handle_press( const QPointF &, bool, Qt::MouseButton, Qt::KeyboardModifiers)` |
| `&d_map_view` | `mouse_clicked( const QPointF &, bool, Qt::MouseButton, Qt::KeyboardModifiers)` | `this` | `handle_click( const QPointF &, bool, Qt::MouseButton, Qt::KeyboardModifiers)` |
| `&d_map_view` | `mouse_dragged( const QPointF &, bool, const QPointF &, bool, Qt::MouseButton, Qt::KeyboardModifiers, const QPointF &)` | `this` | `handle_drag( const QPointF &, bool, const QPointF &, bool, Qt::MouseButton, Qt::KeyboardModifiers, const QPointF &)` |
| `&d_map_view` | `mouse_released_after_drag( const QPointF &, bool, const QPointF &, bool, const QPointF &, Qt::MouseButton, Qt::KeyboardModifiers)` | `this` | `handle_release_after_drag( const QPointF &, bool, const QPointF &, bool, const QPointF &, Qt::MouseButton, Qt::KeyboardModifiers)` |
| `&d_map_view` | `mouse_moved_without_drag( const QPointF &, bool, const QPointF &)` | `this` | `handle_move_without_drag( const QPointF &, bool, const QPointF &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/MapCanvasToolAdapter.h
python scripts/gpq.py def GPlatesGui::MapCanvasToolAdapter --body
python scripts/gpq.py uses MapCanvasToolAdapter --kind class
python scripts/gpq.py hier MapCanvasToolAdapter
```

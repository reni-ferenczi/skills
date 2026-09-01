# MapCanvasToolAdapter

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 525 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/MapCanvasToolAdapter.h` | C++ | 143 |
| `src/gui/MapCanvasToolAdapter.cc` | C++ | 376 |

## Overview

`MapCanvasToolAdapter` is the demultiplexer between raw mouse events and the map
canvas tools. `GPlatesQtWidgets::MapView` emits five untyped mouse signals —
pressed, clicked, dragged, released-after-drag, moved-without-drag — each carrying
the `Qt::MouseButton` and `Qt::KeyboardModifiers` as ordinary parameters. This
class is the only thing that inspects those two parameters: a nested switch turns
each (button, modifier) combination into the corresponding named virtual on
`GPlatesGui::MapCanvasTool`, so `MapCanvasTool` subclasses never see Qt event
plumbing and never test for a Shift key. It is the exact counterpart of
`GPlatesGui::GlobeCanvasToolAdapter` for the globe, and the two are always driven
as a pair by `CanvasToolWorkflow::activate_selected_tool()`, which activates one
globe tool and one map tool for whatever the user picked in the toolbar.

The activation mechanism is signal connection, not a virtual dispatch table. Only
one tool is active at a time (`d_active_map_canvas_tool`, a
`boost::optional<MapCanvasTool &>`), and `activate_canvas_tool()` connects to the
`MapView` signals only on the transition from no-tool to tool — reactivating while
a tool is already active just swaps the reference, which is what keeps duplicate
connections from accumulating. `deactivate_canvas_tool()` tears down every
connection with a blanket `QObject::disconnect(&d_map_view, 0, this, 0)`, so
between tools nothing is listening at all.

Coordinates pass through untranslated: positions are `QPointF` in `QGraphicsScene`
coordinates plus an `is_on_surface` flag, and it is the individual `MapCanvasTool`
that converts to geographic coordinates through the `MapProjection` it holds. Drag
handlers additionally get a `translation` delta. This is where the map path
diverges from the globe path, whose adapter deals in `PointOnSphere` pairs; the
two coordinate conventions are the reason there are two adapters and two tool base
classes at all, with `GPlatesCanvasTools::CanvasToolAdapterForMap` bridging a
projection-agnostic tool onto this side.

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

**Not every gesture is wired up, and the gaps are silent.** The switch statements
fall through to `break` for anything unhandled, so the event is dropped without a
warning. Concretely: right-button and middle-button events do nothing at all;
`handle_press` forwards only unmodified left-press, with the Shift and Ctrl cases
present but empty; and `handle_release_after_drag` has no Shift+Ctrl case even
though `handle_drag` does. If a `MapCanvasTool` override never fires, check here
before debugging the tool — the corresponding case may simply not exist.

**Shift+Ctrl needs the `default` branch.** `Qt::ShiftModifier | Qt::ControlModifier`
is not a constant expression, so it cannot be a `case` label; the combination is
tested with an `if` inside `default:`. Adding another modifier combination means
extending that branch, not adding a case.

**Modifier matching is exact, not a mask test.** The switch compares the whole
`Qt::KeyboardModifiers` value, so a gesture performed with an additional key held
(Alt, or Meta) matches no case and is discarded rather than being treated as the
plain gesture.

**`get_active_map_canvas_tool()` asserts.** It throws
`GPlatesGlobal::PreconditionViolationError` if no tool is active. In practice the
connections only exist while a tool is active, so the slots cannot normally fire
with an empty optional — but calling a handler directly, or leaving a stale
connection, turns into an assertion failure rather than a null dereference.

**The `MapView` reference is borrowed and unowned.** It is stored as a bare
reference and must outlive the adapter; the adapter is also a plain `QObject` with
no parent, owned by value by the `CanvasToolWorkflow` machinery, and the active
tool is likewise held by reference, not by pointer ownership.

**The class comment on `MapCanvasTool` is stale** in the same way as its globe
counterpart: it refers to a `MapCanvasToolChoice` that no longer exists in this
tree. Activation goes through this adapter.

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

# MapView

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 88 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/MapView.h` | C++ | 468 |
| `src/qt-widgets/MapView.cc` | C++ | 921 |

## Overview

[[[PROSE overview unit=qt-widgets/MapView tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::MapView`](#gplatesqtwidgetsmapview) | class | `QGraphicsView`<br>[`SceneView`](SceneView.md)<br>`boost::noncopyable` | — | 0 | — |

## Members

### `GPlatesQtWidgets::MapView`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MousePressInfo` | struct | `None` | public | — |
| `MapView( GPlatesPresentation::ViewState &view_state, GPlatesGui::ColourScheme::non_null_ptr_type colour_scheme, QWidget *parent, const QGLWidget *share_gl_widget, const GPlatesOpenGL::GLContext::non_null_ptr_type &share_gl_context, const GPlatesOpenGL::GLVisualLayers::non_null_ptr_type &share_gl_visual_layers)` | constructor | `None` | public | Constructor. share\_gl\_widget, share\_gl\_context and share\_persistent\_opengl\_objects specify another QGLWidget and associated helper structures that the map view should try to share OpenGL state with. |
| `~MapView()` | destructor | `None` | public | — |
| `set_camera_viewpoint( const GPlatesMaths::LatLonPoint &llp)` | method | `void` | public | Translates the view so that the LatLonPoint llp is centred on the viewport. |
| `set_orientation( const GPlatesMaths::Rotation &rotation /*bool should_emit_external_signal = true*/)` | method | `void` | public | — |
| `orientation()` | method | `boost::optional<GPlatesMaths::Rotation>` | public | bool should\_emit\_external\_signal = true\*/); |
| `move_camera_up()` | method | `void` | public | — |
| `move_camera_down()` | method | `void` | public | — |
| `move_camera_left()` | method | `void` | public | — |
| `move_camera_right()` | method | `void` | public | — |
| `rotate_camera_clockwise()` | method | `void` | public | — |
| `rotate_camera_anticlockwise()` | method | `void` | public | — |
| `reset_camera_orientation()` | method | `void` | public | — |
| `camera_llp()` | method | `boost::optional<GPlatesMaths::LatLonPoint>` | public | Returns the LatLonPoint at the centre of the active view, if the central point is on the surface of the earth. |
| `update_mouse_pointer_pos( QMouseEvent *mouse_event)` | method | `void` | public | — |
| `handle_mouse_pointer_pos_change()` | method | `void` | public | — |
| `get_viewport_size()` | method | `QSize` | public | Returns the dimensions of the viewport in device \*independent\* pixels (ie, widget size). |
| `get_device_independent_pixel_to_map_space_ratio( int paint_device_width_in_device_independent_pixels, int paint_device_height_in_device_independent_pixels, const double &zoom_factor)` | method | `double` | public | Calculate the size of one device-independent pixel in (post projection) map space coordinates. |
| `render_to_qimage( const QSize &image_size_in_device_independent_pixels, const GPlatesGui::Colour &image_clear_colour)` | method | `QImage` | public | Renders the scene to a QImage of the dimensions specified by image\_size. |
| `render_opengl_feedback_to_paint_device( QPaintDevice &feedback_paint_device)` | method | `void` | public | Paint the scene, as best as possible, by re-directing OpenGL rendering to the specified paint device. |
| `map_canvas` | field | `MapCanvas` | public | — |
| `update_canvas()` | method | `void` | public | Redraw geometries on the canvas associated with this view. |
| `current_proximity_inclusion_threshold( const GPlatesMaths::PointOnSphere &click_point)` | method | `double` | public | — |
| `get_gl_context()` | method | `GPlatesOpenGL::GLContext::non_null_ptr_type` | public | Returns the OpenGL context associated with our QGLWidget viewport. |
| `get_gl_visual_layers()` | method | `GPlatesOpenGL::GLVisualLayers::non_null_ptr_type` | public | Returns the OpenGL layers used to filled polygons, render rasters and scalar fields. |
| `width()` | method | `int` | public | — |
| `height()` | method | `int` | public | — |
| `mouseMoveEvent( QMouseEvent *mouse_event)` | method | `void` | protected | — |
| `mousePressEvent( QMouseEvent *mouse_event)` | method | `void` | protected | — |
| `mouseDoubleClickEvent( QMouseEvent *mouse_event)` | method | `void` | protected | — |
| `mouseReleaseEvent( QMouseEvent *mouse_event)` | method | `void` | protected | — |
| `resizeEvent( QResizeEvent* resize_event)` | method | `void` | protected | — |
| `wheelEvent( QWheelEvent *wheel_event)` | method | `void` | protected | — |
| `keyPressEvent( QKeyEvent *key_event)` | method | `void` | protected | — |
| `paintEvent( QPaintEvent *paint_event)` | method | `void` | protected | — |
| `mouse_pointer_position_changed( const boost::optional<GPlatesMaths::LatLonPoint> &, bool is_on_globe)` | method | `void` | public | — |
| `mouse_pressed( const QPointF &point_on_scene, bool is_on_surface, Qt::MouseButton button, Qt::KeyboardModifiers modifiers)` | method | `void` | public | — |
| `mouse_clicked( const QPointF &point_on_scene, bool is_on_surface, Qt::MouseButton button, Qt::KeyboardModifiers modifiers)` | method | `void` | public | — |
| `mouse_dragged( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, Qt::MouseButton button, Qt::KeyboardModifiers modifiers, const QPointF &translation)` | method | `void` | public | — |
| `mouse_released_after_drag( const QPointF &initial_point_on_scene, bool was_on_surface, const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation, Qt::MouseButton button, Qt::KeyboardModifiers modifiers)` | method | `void` | public | — |
| `mouse_moved_without_drag( const QPointF &current_point_on_scene, bool is_on_surface, const QPointF &translation)` | method | `void` | public | — |
| `repainted( bool mouse_down)` | method | `void` | public | — |
| `handle_transform_changed( const GPlatesGui::MapTransform &map_transform)` | method | `void` | private | — |
| `MapViewport` | class | `None` | private | A QGLWidget used as the viewport widget and modified slightly to not automatically swap OpenGL front and back buffers at 'QPainter::end()'. |
| `mouse_pointer_llp()` | method | `boost::optional<GPlatesMaths::LatLonPoint>` | private | Returns the llp of the mouse position, if the mouse is on the surface. |
| `mouse_pointer_scene_coords()` | method | `QPointF` | private | Returns the scene coords of the mouse position. |
| `move_camera( double dx, double dy)` | method | `void` | private | Move camera by dx and dy, both expressed in window coordinates. |
| `mouse_pointer_is_on_surface()` | method | `bool` | private | Returns true if the mouse is over the surface of the earth. |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `d_gl_widget_ptr` | field | `MapViewport` | private | The QGLWidget that we use for this widget's viewport |
| `d_gl_context` | field | `GPlatesOpenGL::GLContext::non_null_ptr_type` | private | Mirrors an OpenGL context and provides a central place to manage low-level OpenGL objects. |
| `d_gl_visual_layers` | field | `GPlatesOpenGL::GLVisualLayers::non_null_ptr_type` | private | Keeps track of OpenGL objects that persist from one render to another. |
| `d_map_canvas_ptr` | field | `boost::scoped_ptr<MapCanvas>` | private | A pointer to the map canvas that this view is associated with. |
| `d_mouse_pointer_is_on_surface` | field | `bool` | private | Whether the mouse pointer is on the surface of the earth. |
| `d_mouse_pointer_screen_pos` | field | `QPoint` | private | The position of the mouse pointer in view coordinates. |
| `d_last_mouse_view_coords` | field | `QPoint` | private | The last position of the mouse in view (screen) coordinates. |
| `d_mouse_press_info` | field | `boost::optional<MousePressInfo>` | private | — |
| `d_map_transform` | field | `GPlatesGui::MapTransform` | private | Translates and rotates maps |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `distance_between_qpointfs( const QPointF &p1, const QPointF &p2)` | function | `double` | — |
| `calc_world_transform_scale_factor( const GPlatesGui::MapTransform &map_transform, int paint_device_width_in_device_independent_pixels, int paint_device_height_in_device_independent_pixels, const double &zoom_factor)` | function | `double` | Calculate the scale factor to map one unit in (post projection) map space coordinates to device-independent pixels. |
| `calc_world_transform( const GPlatesGui::MapTransform &map_transform, unsigned int paint_device_width_in_device_independent_pixels, unsigned int paint_device_height_in_device_independent_pixels)` | function | `QTransform` | Given the scene view's dimensions (eg, canvas dimensions) generate a world transform needed to display the scene. |
| `GPLATES_QTWIDGETS_MAPVIEW_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/MapView tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/CanvasToolAdapterForMap](../canvas-tools/CanvasToolAdapterForMap.md) | canvas-tools | 9 |
| [gui/DigitisationCanvasToolWorkflow](../gui/DigitisationCanvasToolWorkflow.md) | gui | 8 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 7 |
| [gui/TopologyCanvasToolWorkflow](../gui/TopologyCanvasToolWorkflow.md) | gui | 6 |
| [canvas-tools/MovePoleMap](../canvas-tools/MovePoleMap.md) | canvas-tools | 4 |
| [gui/PoleManipulationCanvasToolWorkflow](../gui/PoleManipulationCanvasToolWorkflow.md) | gui | 4 |
| [gui/ViewCanvasToolWorkflow](../gui/ViewCanvasToolWorkflow.md) | gui | 4 |
| [gui/HellingerCanvasToolWorkflow](../gui/HellingerCanvasToolWorkflow.md) | gui | 3 |
| [qt-widgets/GlobeAndMapWidget](GlobeAndMapWidget.md) | qt-widgets | 3 |
| [gui/SmallCircleCanvasToolWorkflow](../gui/SmallCircleCanvasToolWorkflow.md) | gui | 2 |
| [qt-widgets/MapCanvas](MapCanvas.md) | qt-widgets | 2 |
| [qt-widgets/SetProjectionDialog](SetProjectionDialog.md) | qt-widgets | 2 |
| [canvas-tools/ChangeLightDirectionMap](../canvas-tools/ChangeLightDirectionMap.md) | canvas-tools | 1 |
| [canvas-tools/PanMap](../canvas-tools/PanMap.md) | canvas-tools | 1 |
| [canvas-tools/ZoomMap](../canvas-tools/ZoomMap.md) | canvas-tools | 1 |
| [gui/MapCanvasTool](../gui/MapCanvasTool.md) | gui | 1 |
| [gui/MapCanvasToolAdapter](../gui/MapCanvasToolAdapter.md) | gui | 1 |
| [qt-widgets/DrawStyleDialog](DrawStyleDialog.md) | qt-widgets | 1 |
| [qt-widgets/ReconstructionViewWidget](ReconstructionViewWidget.md) | qt-widgets | 1 |
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 1 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_map_transform` | `transform_changed(const GPlatesGui::MapTransform &)` | `this` | `handle_transform_changed(const GPlatesGui::MapTransform &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/MapView.h
python scripts/gpq.py def GPlatesQtWidgets::MapView --body
python scripts/gpq.py uses MapView --kind class
python scripts/gpq.py hier MapView
```

# GlobeCanvas

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 67 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/GlobeCanvas.h` | C++ | 772 |
| `src/qt-widgets/GlobeCanvas.cc` | C++ | 1653 |

## Overview

[[[PROSE overview unit=qt-widgets/GlobeCanvas tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::GlobeCanvas`](#gplatesqtwidgetsglobecanvas) | class | `QGLWidget`<br>[`SceneView`](SceneView.md) | — | 0 | — |

## Members

### `GPlatesQtWidgets::GlobeCanvas`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FRAMING_RATIO` | field | `GLfloat` | public | — |
| `MousePressInfo` | struct | `None` | public | — |
| `centre_of_viewport` | field | `GPlatesMaths::PointOnSphere` | public | The point which corresponds to the centre of the viewport. |
| `GlobeCanvas( GPlatesPresentation::ViewState &view_state, GPlatesGui::ColourScheme::non_null_ptr_type colour_scheme, QWidget *parent_ = 0)` | constructor | `None` | public | — |
| `~GlobeCanvas()` | destructor | `None` | public | — |
| `GlobeCanvas( GlobeCanvas *existing_globe_canvas, GPlatesPresentation::ViewState &view_state_, GPlatesMaths::PointOnSphere &virtual_mouse_pointer_pos_on_globe_, bool mouse_pointer_is_on_globe_, GPlatesGui::Globe &existing_globe_, GPlatesGui::ColourScheme::non_null_ptr_type colour_scheme_, QWidget *parent_ = 0)` | constructor | `None` | private | Private constructor for use by clone() |
| `init()` | method | `void` | private | Common code for both constructors |
| `clone( GPlatesGui::ColourScheme::non_null_ptr_type colour_scheme, QWidget *parent_ = 0)` | method | `GlobeCanvas` | public | — |
| `current_proximity_inclusion_threshold( const GPlatesMaths::PointOnSphere &click_point)` | method | `double` | public | The proximity inclusion threshold is a measure of how close a geometry must be to a click-point be considered "hit" by the click. |
| `mouse_pointer_is_on_globe()` | method | `bool` | public | Return whether the mouse pointer is on the globe. |
| `get_viewport_size()` | method | `QSize` | public | Returns the dimensions of the viewport in device \*independent\* pixels (ie, widget size). |
| `render_to_qimage( const QSize &image_size_in_device_independent_pixels, const GPlatesGui::Colour &image_clear_colour)` | method | `QImage` | public | Renders the scene to a QImage of the dimensions specified by image\_size. |
| `render_opengl_feedback_to_paint_device( QPaintDevice &feedback_paint_device)` | method | `void` | public | Paint the scene, as best as possible, by re-directing OpenGL rendering to the specified paint device. |
| `camera_llp()` | method | `boost::optional<GPlatesMaths::LatLonPoint>` | public | — |
| `set_camera_viewpoint( const GPlatesMaths::LatLonPoint &llp)` | method | `void` | public | — |
| `orientation()` | method | `boost::optional<GPlatesMaths::Rotation>` | public | — |
| `set_orientation( const GPlatesMaths::Rotation &rotation /*bool should_emit_external_signal = true */)` | method | `void` | public | — |
| `get_gl_context()` | method | `GPlatesOpenGL::GLContext::non_null_ptr_type` | public | Returns the OpenGL context associated with this QGLWidget. |
| `get_gl_visual_layers()` | method | `GPlatesOpenGL::GLVisualLayers::non_null_ptr_type` | public | Returns the persistent OpenGL objects associated with this widget's OpenGL context so it can be shared across widgets. |
| `update_canvas()` | method | `void` | public | NOTE: all signals/slots should use namespace scope for all arguments otherwise differences between signals and slots will cause Qt to not be able to connect them at runtime. |
| `notify_of_orientation_change()` | method | `void` | public | — |
| `handle_mouse_pointer_pos_change()` | method | `void` | public | — |
| `force_mouse_pointer_pos_change()` | method | `void` | public | — |
| `initializeGL()` | method | `void` | protected | This is a virtual override of the function in QGLWidget. |
| `resizeGL( int width, int height)` | method | `void` | protected | This is a virtual override of the function in QGLWidget. |
| `paintGL()` | method | `void` | protected | This is a virtual override of the function in QGLWidget. |
| `paintEvent( QPaintEvent *paint_event)` | method | `void` | protected | — |
| `mousePressEvent( QMouseEvent *event)` | method | `void` | protected | This is a virtual override of the function in QWidget. |
| `mouseMoveEvent( QMouseEvent *event)` | method | `void` | protected | This is a virtual override of the function in QWidget. |
| `mouseReleaseEvent( QMouseEvent *event)` | method | `void` | protected | This is a virtual override of the function in QWidget. |
| `keyPressEvent( QKeyEvent *key_event)` | method | `void` | protected | — |
| `move_camera_up()` | method | `void` | protected | — |
| `move_camera_down()` | method | `void` | protected | — |
| `move_camera_left()` | method | `void` | protected | — |
| `move_camera_right()` | method | `void` | protected | — |
| `rotate_camera_clockwise()` | method | `void` | protected | — |
| `rotate_camera_anticlockwise()` | method | `void` | protected | — |
| `reset_camera_orientation()` | method | `void` | protected | — |
| `mouse_pointer_position_changed( const GPlatesMaths::PointOnSphere &new_virtual_pos, bool is_on_globe)` | method | `void` | public | — |
| `mouse_pressed( const GPlatesMaths::PointOnSphere &press_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_press_pos_on_globe, bool is_on_globe, Qt::MouseButton button, Qt::KeyboardModifiers modifiers)` | method | `void` | public | — |
| `mouse_clicked( const GPlatesMaths::PointOnSphere &click_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_click_pos_on_globe, bool is_on_globe, Qt::MouseButton button, Qt::KeyboardModifiers modifiers)` | method | `void` | public | — |
| `mouse_dragged( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GPlatesMaths::Po ...` | method | `void` | public | — |
| `mouse_released_after_drag( const GPlatesMaths::PointOnSphere &initial_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_initial_pos_on_globe, bool was_on_globe, const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GPla ...` | method | `void` | public | — |
| `mouse_moved_without_drag( const GPlatesMaths::PointOnSphere &current_pos_on_globe, const GPlatesMaths::PointOnSphere &oriented_current_pos_on_globe, bool is_on_globe, const GPlatesMaths::PointOnSphere &oriented_centre_of_viewport)` | method | `void` | public | The mouse position moved but the left mouse button is NOT down. |
| `repainted( bool mouse_down)` | method | `void` | public | — |
| `handle_zoom_change()` | method | `void` | public | NOTE: all signals/slots should use namespace scope for all arguments otherwise differences between signals and slots will cause Qt to not be able to connect them at runtime. |
| `MakeGLContextCurrent` | struct | `None` | private | Utility class to make the QGLWidget's OpenGL context current in GlobeCanvas constructor. |
| `cache_handle_type` | typedef | `boost::shared_ptr<void>` | private | Typedef for an opaque object that caches a particular painting. |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_gl_context` | field | `GPlatesOpenGL::GLContext::non_null_ptr_type` | private | Mirrors an OpenGL context and provides a central place to manage low-level OpenGL objects. |
| `d_make_context_current` | field | `MakeGLContextCurrent` | private | Makes the QGLWidget's OpenGL context current in GlobeCanvas constructor so it can call OpenGL. |
| `d_gl_off_screen_context` | field | `boost::optional<GPlatesOpenGL::GLOffScreenContext::non_null_ptr_type>` | private | Used to render to an off-screen frame buffer when outside paint event. |
| `d_initialisedGL` | field | `bool` | private | Is true if OpenGL has been initialised for this canvas. |
| `d_gl_model_view_transform` | field | `GPlatesOpenGL::GLMatrix` | private | The current model-view transform for regular OpenGL rendering. |
| `d_gl_projection_transform_include_front_half_globe` | field | `GPlatesOpenGL::GLMatrix` | private | The current projection transform for OpenGL rendering of the \*front\* visible half of the globe. |
| `d_gl_projection_transform_include_rear_half_globe` | field | `GPlatesOpenGL::GLMatrix` | private | The current projection transform for OpenGL rendering of the \*rear\* half of the globe. |
| `d_gl_projection_transform_include_full_globe` | field | `GPlatesOpenGL::GLMatrix` | private | The current projection transform for OpenGL rendering of the full globe. |
| `d_gl_projection_transform_include_stars` | field | `GPlatesOpenGL::GLMatrix` | private | The current projection transform for rendering stars. |
| `d_gl_projection_transform_text_overlay` | field | `GPlatesOpenGL::GLMatrix` | private | The current projection transform for the screen text overlay. |
| `d_gl_visual_layers` | field | `GPlatesOpenGL::GLVisualLayers::non_null_ptr_type` | private | Keeps track of OpenGL objects that persist from one render to another. |
| `d_gl_frame_cache_handle` | field | `cache_handle_type` | private | Enables frame-to-frame caching of persistent OpenGL resources. |
| `d_virtual_mouse_pointer_pos_on_globe` | field | `GPlatesMaths::PointOnSphere` | private | If the mouse pointer is on the globe, this is the position of the mouse pointer on the globe. |
| `d_mouse_pointer_is_on_globe` | field | `bool` | private | Whether the mouse pointer is on the globe. |
| `d_mouse_pointer_screen_pos_x` | field | `int` | private | The x-coord of the mouse pointer position on the screen. |
| `d_mouse_pointer_screen_pos_y` | field | `int` | private | The y-coord of the mouse pointer position on the screen. |
| `d_smaller_dim` | field | `double` | private | The smaller of the dimensions (width/height) of the screen. |
| `d_larger_dim` | field | `double` | private | The larger of the dimensions (width/height) of the screen. |
| `d_mouse_press_info` | field | `boost::optional<MousePressInfo>` | private | — |
| `d_globe` | field | `GPlatesGui::Globe` | private | — |
| `d_text_overlay` | field | `boost::scoped_ptr<GPlatesGui::TextOverlay>` | private | Paints an optional text overlay onto the globe. |
| `d_velocity_legend_overlay` | field | `boost::scoped_ptr<GPlatesGui::VelocityLegendOverlay>` | private | Paints an optional velocity legend overlay onto the globe. |
| `initializeGL_if_necessary()` | method | `void` | private | Calls 'initializeGL()' if it hasn't already been called. |
| `set_view()` | method | `void` | private | — |
| `render_scene_tile_into_image( GPlatesOpenGL::GLRenderer &renderer, const GPlatesOpenGL::GLTileRender &tile_render, const GPlatesOpenGL::GLMatrix &projection_transform_include_front_half_globe, const GPlatesOpenGL::GLMatrix &projection_transform_include_rear_half_globe, const GPlatesOpenGL::GLMatrix &projection_transfor ...` | method | `cache_handle_type` | private | Render one tile of the scene (as specified by tile\_render). |
| `render_scene( GPlatesOpenGL::GLRenderer &renderer, const GPlatesOpenGL::GLMatrix &projection_transform_include_front_half_globe, const GPlatesOpenGL::GLMatrix &projection_transform_include_rear_half_globe, const GPlatesOpenGL::GLMatrix &projection_transform_include_full_globe, const GPlatesOpenGL::GLMatrix &projection_ ...` | method | `cache_handle_type` | private | Render the scene. |
| `update_mouse_pointer_pos( QMouseEvent *mouse_event)` | method | `void` | private | — |
| `update_dimensions()` | method | `void` | private | — |
| `get_universe_coord_y_of_mouse()` | method | `double` | private | Get the "universe" y-coordinate of the current mouse pointer position. |
| `get_universe_coord_z_of_mouse()` | method | `double` | private | Get the "universe" z-coordinate of the current mouse pointer position. |
| `get_universe_coord_y( int screen_x)` | method | `double` | private | Translate the screen x-coordinate screen\_x to the corresponding "universe" y-coordinate. |
| `get_universe_coord_z( int screen_y)` | method | `double` | private | Translate the screen y-coordinate screen\_y to the corresponding "universe" z-coordinate. |
| `calculate_scale( int paint_device_width_in_device_independent_pixels, int paint_device_height_in_device_independent_pixels)` | method | `float` | private | Calculates scaling for lines, points and text based on size of the paint device. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `FRAMING_RATIO` | variable | `GLfloat` | At the initial zoom, the smaller dimension of the GlobeCanvas will be FRAMING\_RATIO times the diameter of the Globe. |
| `EYE_POSITION` | variable | `GPlatesMaths::Vector3D` | The view is initially oriented such that the global x-axis points out of the screen. |
| `calc_globe_pos_discrim( double y, double z)` | function | `double` | Calculate the globe-position discriminant for the universe coordinates y and z. |
| `discrim_signifies_on_globe( double discrim)` | function | `bool` | Return whether the globe-position discriminant indicates that a position is on the globe. |
| `calc_pos_on_globe( double y, double z, double discrim)` | function | `GPlatesMaths::PointOnSphere` | Given universe coordinates y and z and discriminant discrim, calculate the corresponding position on the globe (x, y, z). |
| `calc_pos_at_intersection_with_globe( double y, double z, double discrim)` | function | `GPlatesMaths::PointOnSphere` | Given universe coordinates y and z and a discriminant discrim which together indicate that a position is not on the globe, calculate the closest position which is on the globe. |
| `calc_virtual_globe_position( double y, double z)` | function | `GPlatesMaths::PointOnSphere` | Given universe coordinates y and z, calculate and return a position which is on the globe (a unit sphere). |
| `calc_device_independent_pixel_to_world_space_ratio( int scene_view_width_in_device_independent_pixels, int scene_view_height_in_device_independent_pixels, const double &zoom_factor)` | function | `double` | Calculate the size of one device-independent pixel in world space coordinates. |
| `calc_scene_projection_transforms( int scene_view_width_in_device_independent_pixels, int scene_view_height_in_device_independent_pixels, const double &zoom_factor, GPlatesOpenGL::GLMatrix &projection_transform_include_front_half_globe, GPlatesOpenGL::GLMatrix &projection_transform_include_rear_half_globe, GPlatesOpenGL ...` | function | `void` | Given the scene view's dimensions (eg, canvas dimensions) generate projection transforms needed to display the scene. |
| `GPLATES_QTWIDGETS_GLOBECANVAS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/GlobeCanvas tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/CanvasToolAdapterForGlobe](../canvas-tools/CanvasToolAdapterForGlobe.md) | canvas-tools | 23 |
| [qt-widgets/GlobeAndMapWidget](GlobeAndMapWidget.md) | qt-widgets | 16 |
| [canvas-tools/ChangeLightDirectionGlobe](../canvas-tools/ChangeLightDirectionGlobe.md) | canvas-tools | 8 |
| [canvas-tools/MovePoleGlobe](../canvas-tools/MovePoleGlobe.md) | canvas-tools | 3 |
| [gui/VelocityLegendOverlay](../gui/VelocityLegendOverlay.md) | gui | 3 |
| [qt-widgets/ReconstructionViewWidget](ReconstructionViewWidget.md) | qt-widgets | 3 |
| [gui/GlobeVisibilityTester](../gui/GlobeVisibilityTester.md) | gui | 2 |
| [qt-widgets/LightingWidget](LightingWidget.md) | qt-widgets | 2 |
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 2 |
| [canvas-tools/BuildTopology](../canvas-tools/BuildTopology.md) | canvas-tools | 1 |
| [canvas-tools/EditTopology](../canvas-tools/EditTopology.md) | canvas-tools | 1 |
| [canvas-tools/ManipulatePole](../canvas-tools/ManipulatePole.md) | canvas-tools | 1 |
| [canvas-tools/ReorientGlobe](../canvas-tools/ReorientGlobe.md) | canvas-tools | 1 |
| [canvas-tools/ZoomGlobe](../canvas-tools/ZoomGlobe.md) | canvas-tools | 1 |
| [gui/DigitisationCanvasToolWorkflow](../gui/DigitisationCanvasToolWorkflow.md) | gui | 1 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 1 |
| [gui/GlobeCanvasTool](../gui/GlobeCanvasTool.md) | gui | 1 |
| [gui/GlobeCanvasToolAdapter](../gui/GlobeCanvasToolAdapter.md) | gui | 1 |
| [gui/HellingerCanvasToolWorkflow](../gui/HellingerCanvasToolWorkflow.md) | gui | 1 |
| [gui/PoleManipulationCanvasToolWorkflow](../gui/PoleManipulationCanvasToolWorkflow.md) | gui | 1 |

*... and 5 more units.*

## Related

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&(d_globe.orientation())` | `orientation_changed()` | `this` | `notify_of_orientation_change()` |
| `&(d_globe.orientation())` | `orientation_changed()` | `this` | `force_mouse_pointer_pos_change()` |
| `&(d_view_state.get_rendered_geometry_collection())` | `collection_was_updated( GPlatesViewOperations::RenderedGeometryCollection &, GPlatesViewOperations::RenderedGeometryCollection::main_layers_update_type)` | `this` | `update_canvas()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/GlobeCanvas.h
python scripts/gpq.py def GPlatesQtWidgets::GlobeCanvas --body
python scripts/gpq.py uses GlobeCanvas --kind class
python scripts/gpq.py hier GlobeCanvas
```

# MapCanvas

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 510 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/MapCanvas.h` | C++ | 275 |
| `src/qt-widgets/MapCanvas.cc` | C++ | 688 |

## Overview

A `QGraphicsScene` subclass that renders the 2D map view using OpenGL. `MapCanvas` paints geometry, overlays (text and velocity legends), and manages viewport transforms. It supports rendering to `QImage` and feedback paint devices for image export and printing. The class maintains an OpenGL context with frame-to-frame caching of persistent resources to avoid unnecessary regeneration, and provides tile-based rendering for large images. Unlike `GlobeCanvas` (which renders the 3D globe), `MapCanvas` is the rendering surface; `MapView` is the container and interaction handler.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::MapCanvas`](#gplatesqtwidgetsmapcanvas) | class | `QGraphicsScene`<br>`boost::noncopyable` | — | 0 | Responsible for invoking the functions to paint items onto the map. |

## Members

### `GPlatesQtWidgets::MapCanvas`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MapCanvas( GPlatesPresentation::ViewState &view_state, GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, MapView *map_view_ptr, QGLWidget *gl_widget, const GPlatesOpenGL::GLContext::non_null_ptr_type &gl_context, const GPlatesOpenGL::GLVisualLayers::non_null_ptr_type &gl_visual_layers, GP ...` | constructor | `None` | public | — |
| `~MapCanvas()` | destructor | `None` | public | — |
| `set_viewport_transform( const QTransform &viewport_transform)` | method | `void` | public | Sets the viewport transform used for rendering this canvas using OpenGL. |
| `render_to_qimage( QPaintDevice &map_canvas_paint_device, const QTransform &viewport_transform, const QSize &image_size_in_device_independent_pixels, const GPlatesGui::Colour &image_clear_colour)` | method | `QImage` | public | Renders the scene to a QImage of the dimensions specified by image\_size. |
| `render_opengl_feedback_to_paint_device( QPaintDevice &map_canvas_paint_device, const QTransform &viewport_transform, QPaintDevice &feedback_paint_device)` | method | `void` | public | Paint the scene, as best as possible, by re-directing OpenGL rendering to the feedback paint device feedback\_paint\_device. map\_canvas\_paint\_device is the map canvas's OpenGL paint device used for OpenGL rendering. viewport\_transform is the ... |
| `update_canvas()` | method | `void` | public | — |
| `drawBackground( QPainter *painter, const QRectF &rect)` | method | `void` | protected | A virtual override of the QGraphicsScene function. |
| `MakeGLContextCurrent` | struct | `None` | private | Utility class to make the OpenGL context current in MapCanvas constructor. |
| `cache_handle_type` | typedef | `boost::shared_ptr<void>` | private | Typedef for an opaque object that caches a particular painting. |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_map_view_ptr` | field | `MapView` | private | — |
| `d_viewport_transform` | field | `QTransform` | private | Viewport transform used for rendering this canvas. |
| `d_gl_context` | field | `GPlatesOpenGL::GLContext::non_null_ptr_type` | private | Mirrors an OpenGL context and provides a central place to manage low-level OpenGL objects. |
| `d_make_context_current` | field | `MakeGLContextCurrent` | private | Makes the OpenGL context current in GlobeCanvas constructor so it can call OpenGL. |
| `d_gl_off_screen_context` | field | `boost::optional<GPlatesOpenGL::GLOffScreenContext::non_null_ptr_type>` | private | Used to render to an off-screen frame buffer when outside paint event. |
| `d_gl_frame_cache_handle` | field | `cache_handle_type` | private | Enables frame-to-frame caching of persistent OpenGL resources. |
| `d_text_overlay` | field | `boost::scoped_ptr<GPlatesGui::TextOverlay>` | private | Paints an optional text overlay onto the map. |
| `d_velocity_legend_overlay` | field | `boost::scoped_ptr<GPlatesGui::VelocityLegendOverlay>` | private | Paints an optional velocity legend overlay onto the map. |
| `d_map` | field | `GPlatesGui::Map` | private | Holds the state |
| `d_rendered_geometry_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | A pointer to the state's RenderedGeometryCollection |
| `initializeGL( QGLWidget *gl_widget)` | method | `void` | private | Do some OpenGL initialisation. |
| `render_scene_tile_into_image( GPlatesOpenGL::GLRenderer &renderer, const GPlatesOpenGL::GLTileRender &tile_render, const GPlatesGui::Colour &image_clear_colour, QImage &image, const GPlatesOpenGL::GLMatrix &projection_matrix_scene, const GPlatesOpenGL::GLMatrix &projection_matrix_text_overlay, const QPaintDevice &map_c ...` | method | `cache_handle_type` | private | Render one tile of the scene (as specified by tile\_render). |
| `render_scene( GPlatesOpenGL::GLRenderer &renderer, const GPlatesOpenGL::GLMatrix &projection_matrix_scene, const GPlatesOpenGL::GLMatrix &projection_matrix_text_overlay, const GPlatesGui::Colour &clear_colour, int paint_device_width_in_device_independent_pixels, int paint_device_height_in_device_independent_pixels, int ...` | method | `cache_handle_type` | private | Render onto the canvas. |
| `calculate_scale( int paint_device_width_in_device_independent_pixels, int paint_device_height_in_device_independent_pixels, int map_canvas_paint_device_width_in_device_independent_pixels, int map_canvas_paint_device_height_in_device_independent_pixels)` | method | `float` | private | Calculate scaling for lines, points and text based on size of view |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_model_view_matrix_from_2D_world_transform( GPlatesOpenGL::GLMatrix &model_view_matrix, const QTransform &world_transform)` | function | `void` | Gets the equivalent OpenGL model-view matrix from the 2D world transform. |
| `get_ortho_projection_matrices_from_dimensions( GPlatesOpenGL::GLMatrix &projection_matrix_scene, GPlatesOpenGL::GLMatrix &projection_matrix_text_overlay, int scene_width, int scene_height)` | function | `void` | Gets the orthographic OpenGL projection matrix from the specified dimensions. |
| `GPLATES_QTWIDGETS_MAPCANVAS_H` | macro | `None` | — |

## Notes

The off-screen OpenGL context is created lazily in `initializeGL`, not in the constructor. The frame cache mechanism holds the previous frame's cached resources while the current frame is being generated, then releases them to prevent old cached resources from being invalidated each frame. The `MakeGLContextCurrent` utility in the constructor enables OpenGL calls during initialization, which would otherwise only be possible in `drawBackground`.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/MapView](MapView.md) | qt-widgets | 8 |
| [canvas-tools/CanvasToolAdapterForMap](../canvas-tools/CanvasToolAdapterForMap.md) | canvas-tools | 1 |
| [canvas-tools/MovePoleMap](../canvas-tools/MovePoleMap.md) | canvas-tools | 1 |
| [canvas-tools/PanMap](../canvas-tools/PanMap.md) | canvas-tools | 1 |
| [qt-widgets/DrawStyleDialog](DrawStyleDialog.md) | qt-widgets | 1 |
| [qt-widgets/GlobeAndMapWidget](GlobeAndMapWidget.md) | qt-widgets | 1 |
| [qt-widgets/ProjectionControlWidget](ProjectionControlWidget.md) | qt-widgets | 1 |
| [qt-widgets/ReconstructionViewWidget](ReconstructionViewWidget.md) | qt-widgets | 1 |
| [qt-widgets/SetProjectionDialog](SetProjectionDialog.md) | qt-widgets | 1 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_rendered_geometry_collection` | `collection_was_updated( GPlatesViewOperations::RenderedGeometryCollection &, GPlatesViewOperations::RenderedGeometryCollection::main_layers_update_type)` | `this` | `update_canvas()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/MapCanvas.h
python scripts/gpq.py def GPlatesQtWidgets::MapCanvas --body
python scripts/gpq.py uses MapCanvas --kind class
python scripts/gpq.py hier MapCanvas
```

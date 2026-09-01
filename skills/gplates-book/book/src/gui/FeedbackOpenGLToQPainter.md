# FeedbackOpenGLToQPainter

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 504 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/FeedbackOpenGLToQPainter.h` | C++ | 286 |
| `src/gui/FeedbackOpenGLToQPainter.cc` | C++ | 876 |

## Overview

`FeedbackOpenGLToQPainter` bridges OpenGL rendering into a `QPainter`, which is how GPlates draws to vector output devices (SVG, PDF, printers) that only understand Qt's own paint model. It has two independent modes, each guarded by a `begin_*`/`end_*` pair (and an RAII `VectorGeometryScope`/`ImageScope` wrapper for each): vector-geometry feedback uses the classic fixed-function OpenGL feedback buffer (`glFeedbackBuffer`/`glRenderMode(GL_FEEDBACK)`) to capture projected points, lines and polygons as a stream of `GL_POINT_TOKEN`/`GL_LINE_TOKEN`/`GL_POLYGON_TOKEN` records, which `draw_feedback_primitives_to_qpainter` then replays as `QPainter` drawing calls; image feedback instead renders arbitrary (including shader-based) content into an off-screen `QImage` sized to the painter's device, optionally split into tiles via `begin_render_image_tile`/`end_render_image_tile` when the target image is larger than the available framebuffer, and hands the finished `QImage` to the `QPainter`.

The feedback-buffer path only works with the fixed-function pipeline, so anything drawn with vertex shaders must go through the `QImage` path instead — a limitation the header flags as a `TODO` pending an OpenGL 2/3 feedback-extension implementation.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::Vertex`](#anonymousvertex) | struct | — | — | 0 | — |
| [`GPlatesGui::FeedbackOpenGLToQPainter`](#gplatesguifeedbackopengltoqpainter) | class | — | — | 0 | Used to feedback OpenGL rendering into a QPainter. |

## Members

### `(anonymous)::Vertex`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `x` | field | `GLfloat` | public | — |
| `y` | field | `GLfloat` | public | — |
| `z` | field | `GLfloat` | public | — |
| `red` | field | `GLfloat` | public | — |
| `green` | field | `GLfloat` | public | — |
| `blue` | field | `GLfloat` | public | — |
| `alpha` | field | `GLfloat` | public | — |

### `GPlatesGui::FeedbackOpenGLToQPainter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `begin_render_vector_geometry( GPlatesOpenGL::GLRenderer &renderer, unsigned int max_num_points, unsigned int max_num_lines, unsigned int max_num_triangles)` | method | `void` | public | Begins OpenGL feedback of (fixed-function pipeline) vector geometries. |
| `end_render_vector_geometry( GPlatesOpenGL::GLRenderer &renderer)` | method | `void` | public | Ends OpenGL feedback of (fixed-function pipeline) vector geometries and renders the projected vector geometry to the QPainter set up on the GLRenderer. |
| `VectorGeometryScope` | class | `None` | public | RAII class to call begin\_render\_vector\_geometry and end\_render\_vector\_geometry over a scope. |
| `begin_render_image( GPlatesOpenGL::GLRenderer &renderer, const double &max_point_size_and_line_width = 0)` | method | `void` | public | Begins arbitrary rendering to an internal QImage of dimensions matching the paint device of the QPainter attached to renderer. |
| `begin_render_image_tile( GPlatesOpenGL::GLRenderer &renderer, bool save_restore_state = true, GPlatesOpenGL::GLViewport *image_tile_viewport = NULL, GPlatesOpenGL::GLViewport *image_tile_scissor_rect = NULL)` | method | `GPlatesOpenGL::GLTransform::non_null_ptr_to_const_type` | public | Begins a tile (sub-region) of the current image. |
| `end_render_image_tile( GPlatesOpenGL::GLRenderer &renderer)` | method | `bool` | public | Ends the current tile (sub-region) of the current image. |
| `end_render_image( GPlatesOpenGL::GLRenderer &renderer)` | method | `void` | public | Ends arbitrary rendering to a QImage. |
| `ImageScope` | class | `None` | public | RAII class to call begin\_render\_image and end\_render\_image over a scope. |
| `VectorRender` | struct | `None` | private | Used when rendering vector geometries. |
| `ImageRender` | struct | `None` | private | Used when performing arbitrary rendering to an image. |
| `d_vector_render` | field | `boost::optional<VectorRender>` | private | — |
| `d_image_render` | field | `boost::optional<ImageRender>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `VERTEX_SIZE` | variable | `int` | — |
| `fill_vertex_data_from_buffer( Vertex *vertex, const GLfloat *position)` | function | `void` | — |
| `parse_and_draw_polygon_vertices( const GLfloat *&buffer_position, const QPointF &offset, QPainter *painter, int paint_device_height)` | function | `void` | — |
| `analyse_feedback_buffer( const GLfloat *feedback_buffer, unsigned int feedback_buffer_size)` | function | `void` | Go through the buffer and count how many of the various token types we have, and send them to std::cerr. |
| `find_bounding_box( const GLfloat *feedback_buffer, unsigned int feedback_buffer_size)` | function | `QRectF` | Go through the buffer to establish the bounding box. |
| `draw_feedback_primitives_to_qpainter( QPainter &painter, const GLfloat *feedback_buffer, unsigned int feedback_buffer_size)` | function | `void` | Go through the feedback buffer and interpret the points/lines as Qt geometrical items, and send them to the QPainter. |
| `GPLATES_GUI_FEEDBACKOPENGLTOQPAINTER_H` | macro | `None` | — |

## Notes

- `end_render_vector_geometry` throws `PreconditionViolationError` if `renderer` has no `QPainter` attached, and `OpenGLException` if the feedback buffer sized by `begin_render_vector_geometry`'s point/line/triangle counts turns out too small for what was actually drawn — callers must size the buffer generously up front, there is no automatic growth.
- Image-tile rendering reuses whatever framebuffer is currently bound (main framebuffer or an FBO) and corrupts its contents; a caller that needs the framebuffer's colour contents preserved across tiling must save and restore it itself.
- `begin_render_image_tile`/`end_render_image_tile` and `begin_render_tile`/`end_render_tile` on `ImageScope` must only be called inside an active `begin_render_image`/`end_render_image` (or `ImageScope`) pair; `end_render_image_tile` returns `false` while more tiles remain to be rendered.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/LayerPainter](LayerPainter.md) | gui | 139 |
| [gui/SphericalGrid](SphericalGrid.md) | gui | 41 |
| [gui/Stars](Stars.md) | gui | 35 |
| [gui/OpaqueSphere](OpaqueSphere.md) | gui | 31 |
| [gui/MapBackground](MapBackground.md) | gui | 29 |
| [gui/MapGrid](MapGrid.md) | gui | 23 |
| [opengl/GLMultiResolutionCubeRaster](../opengl/GLMultiResolutionCubeRaster.md) | opengl | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/FeedbackOpenGLToQPainter.h
python scripts/gpq.py def GPlatesGui::FeedbackOpenGLToQPainter --body
python scripts/gpq.py uses FeedbackOpenGLToQPainter --kind class
python scripts/gpq.py hier FeedbackOpenGLToQPainter
```

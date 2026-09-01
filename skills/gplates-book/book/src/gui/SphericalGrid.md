# SphericalGrid

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1204 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/SphericalGrid.h` | C++ | 95 |
| `src/gui/SphericalGrid.cc` | C++ | 428 |

## Overview

`GPlatesGui::SphericalGrid` draws the latitude/longitude graticule and the globe's circumference outline for the 3D globe view, using settings supplied by a `GraticuleSettings` reference it does not own. Lines of latitude are tessellated as `GPlatesMaths::SmallCircle`s and lines of longitude as great-circle arcs (`stream_line_of_lat`/`stream_line_of_lon`), streamed into vertex buffers via `GPlatesOpenGL::GLDynamicStreamPrimitives` and uploaded once into a compiled OpenGL draw state (`GLCompiledDrawState`) rather than re-issued every frame.

Both `paint()` and `paint_circumference()` cache their compiled draw state and only rebuild it when the graticule settings actually change (`d_last_seen_graticule_settings` tracks what was last compiled), since compiling is comparatively expensive and the grid's shape rarely changes between frames. Rendering can go either straight to the OpenGL framebuffer or through `FeedbackOpenGLToQPainter` to composite onto a `QPainter` paint device (e.g. when exporting to a vector image), which the two paint methods select automatically based on `renderer.rendering_to_context_framebuffer()`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::vertex_type`](#anonymousvertex_type) | typedef | — | — | 0 | — |
| [`(anonymous)::vertex_element_type`](#anonymousvertex_element_type) | typedef | — | — | 0 | — |
| [`(anonymous)::stream_primitives_type`](#anonymousstream_primitives_type) | typedef | — | — | 0 | — |
| [`GPlatesGui::SphericalGrid`](#gplatesguisphericalgrid) | class | `boost::noncopyable` | — | 0 | Renders latitude and longitude grid lines in the 3D globe view. |

## Members

### `(anonymous)::vertex_type`

*None.*

### `(anonymous)::vertex_element_type`

*None.*

### `(anonymous)::stream_primitives_type`

*None.*

### `GPlatesGui::SphericalGrid`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SphericalGrid( GPlatesOpenGL::GLRenderer &renderer, const GraticuleSettings &graticule_settings)` | constructor | `None` | public | — |
| `paint( GPlatesOpenGL::GLRenderer &renderer)` | method | `void` | public | Paints lines of latitude and longitude on the surface of the sphere. |
| `paint_circumference( GPlatesOpenGL::GLRenderer &renderer, const GPlatesMaths::UnitVector3D &axis, double angle_in_deg)` | method | `void` | public | Paints the circumference. |
| `d_graticule_settings` | field | `GraticuleSettings` | private | — |
| `d_last_seen_graticule_settings` | field | `boost::optional<GraticuleSettings>` | private | — |
| `d_grid_vertex_array` | field | `GPlatesOpenGL::GLVertexArray::shared_ptr_type` | private | — |
| `d_grid_num_line_segments` | field | `unsigned int` | private | — |
| `d_grid_compiled_draw_state` | field | `boost::optional<GPlatesOpenGL::GLCompiledDrawState::non_null_ptr_to_const_type>` | private | — |
| `d_circumference_vertex_array` | field | `GPlatesOpenGL::GLVertexArray::shared_ptr_type` | private | — |
| `d_circumference_num_line_segments` | field | `unsigned int` | private | — |
| `d_circumference_compiled_draw_state` | field | `boost::optional<GPlatesOpenGL::GLCompiledDrawState::non_null_ptr_to_const_type>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `LINE_OF_LATITUDE_DELTA_LONGITUDE` | variable | `double` | The angular spacing a points along a line of latitude (small circle). |
| `LINE_OF_LONGITUDE_DELTA_LATITUDE` | variable | `double` | The angular spacing a points along a line of longitude (great circle). |
| `set_line_draw_state( GPlatesOpenGL::GLRenderer &renderer, float line_width_hint)` | function | `void` | Sets the OpenGL state set that defines the appearance of the grid lines. |
| `stream_line_of_lat( stream_primitives_type &stream, const double &lat, const GPlatesGui::rgba8_t &colour)` | function | `void` | Draw a line of latitude for latitude lat. |
| `stream_line_of_lon( stream_primitives_type &stream, const double &lon, const GPlatesGui::rgba8_t &colour)` | function | `void` | Draw a line of longitude for longitude lon from the north pole to the south pole. |
| `undo_rotation( GPlatesOpenGL::GLMatrix &transform, const GPlatesMaths::UnitVector3D &axis, double angle_in_deg)` | function | `void` | — |
| `compile_grid_draw_state( GPlatesOpenGL::GLRenderer &renderer, GPlatesOpenGL::GLVertexArray &vertex_array, unsigned int &num_line_segments, const GPlatesMaths::Real &delta_lat, const GPlatesMaths::Real &delta_lon, const GPlatesGui::rgba8_t &colour, float line_width_hint)` | function | `GPlatesOpenGL::GLCompiledDrawState::non_null_ptr_to_const_type` | — |
| `compile_circumference_draw_state( GPlatesOpenGL::GLRenderer &renderer, GPlatesOpenGL::GLVertexArray &vertex_array, unsigned int &num_line_segments, const GPlatesGui::rgba8_t &colour, float line_width_hint)` | function | `GPlatesOpenGL::GLCompiledDrawState::non_null_ptr_to_const_type` | — |
| `GPLATES_GUI_SPHERICALGRID_H` | macro | `None` | — |

## Notes

`d_graticule_settings` is held by reference, so the referenced `GraticuleSettings` object must outlive the `SphericalGrid`. The grid draw state is invalidated on any settings change, but the circumference draw state only checks the colour (its line width and geometry don't depend on the lat/lon spacing settings) — a change to spacing alone will not recompile the circumference, only the grid.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Globe](Globe.md) | gui | 12 |
| [gui/GlobeCanvasTool](GlobeCanvasTool.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/SphericalGrid.h
python scripts/gpq.py def GPlatesGui::SphericalGrid --body
python scripts/gpq.py uses SphericalGrid --kind class
python scripts/gpq.py hier SphericalGrid
```

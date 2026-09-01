# Stars

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1487 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/Stars.h` | C++ | 79 |
| `src/gui/Stars.cc` | C++ | 331 |

## Overview

Renders a random starfield background for the 3D globe view. Creates two sizes of stars (small and large) placed uniformly on a sphere around the globe, using Marsaglia's method for even distribution on the sphere surface. During construction, generates 4,250 small stars and 3,750 large stars using a fixed random seed so the pattern is consistent across sessions. Uses OpenGL point primitives with alpha blending and anti-aliasing for visual quality, and pre-compiles the draw state for efficient rendering. The starfield is shown or hidden based on the `show_stars` setting in `ViewState`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::vertex_type`](#anonymousvertex_type) | typedef | — | — | 0 | — |
| [`(anonymous)::vertex_element_type`](#anonymousvertex_element_type) | typedef | — | — | 0 | — |
| [`(anonymous)::stream_primitives_type`](#anonymousstream_primitives_type) | typedef | — | — | 0 | — |
| [`GPlatesGui::Stars`](#gplatesguistars) | class | `boost::noncopyable` | — | 0 | Draws a random collection of stars in the background in the 3D globe view. |

## Members

### `(anonymous)::vertex_type`

*None.*

### `(anonymous)::vertex_element_type`

*None.*

### `(anonymous)::stream_primitives_type`

*None.*

### `GPlatesGui::Stars`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Stars( GPlatesOpenGL::GLRenderer &renderer, GPlatesPresentation::ViewState &view_state, const GPlatesGui::Colour &colour, int device_pixel_ratio)` | constructor | `None` | public | — |
| `paint( GPlatesOpenGL::GLRenderer &renderer)` | method | `void` | public | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_vertex_array` | field | `GPlatesOpenGL::GLVertexArray::shared_ptr_type` | private | — |
| `d_num_points` | field | `unsigned int` | private | — |
| `d_compiled_draw_state` | field | `boost::optional<GPlatesOpenGL::GLCompiledDrawState::non_null_ptr_to_const_type>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `SMALL_STARS_SIZE` | variable | `GLfloat` | — |
| `LARGE_STARS_SIZE` | variable | `GLfloat` | — |
| `NUM_SMALL_STARS` | variable | `unsigned int` | — |
| `NUM_LARGE_STARS` | variable | `unsigned int` | — |
| `RADIUS` | variable | `GLfloat` | Points sit on a sphere of this radius. |
| `stream_stars( stream_primitives_type &stream, boost::function< double () > &rand, unsigned int num_stars, const GPlatesGui::rgba8_t &colour)` | function | `void` | — |
| `compile_stars_draw_state( GPlatesOpenGL::GLRenderer &renderer, GPlatesOpenGL::GLVertexArray &vertex_array, unsigned int &num_points, boost::function< double () > &rand, const GPlatesGui::rgba8_t &colour, int device_pixel_ratio)` | function | `GPlatesOpenGL::GLCompiledDrawState::non_null_ptr_to_const_type` | — |
| `GPLATES_GUI_STARS_H` | macro | `None` | — |

## Notes

The star pattern is generated once at construction using a fixed random seed (0) and reused at every paint call. The `paint()` method checks `ViewState` to determine whether stars should be visible and handles both direct OpenGL framebuffer rendering and rendering through QPainter feedback. Point sizes are adjusted by the device pixel ratio to maintain visual appearance on high-DPI displays.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Globe](Globe.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/Stars.h
python scripts/gpq.py def GPlatesGui::Stars --body
python scripts/gpq.py uses Stars --kind class
python scripts/gpq.py hier Stars
```

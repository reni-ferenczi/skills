# Stars

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1487 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/Stars.h` | C++ | 79 |
| `src/gui/Stars.cc` | C++ | 331 |

## Overview

[[[PROSE overview unit=gui/Stars tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=gui/Stars tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

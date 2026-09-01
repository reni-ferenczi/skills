# SphericalGrid

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1204 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/SphericalGrid.h` | C++ | 95 |
| `src/gui/SphericalGrid.cc` | C++ | 428 |

## Overview

[[[PROSE overview unit=gui/SphericalGrid tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=gui/SphericalGrid tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

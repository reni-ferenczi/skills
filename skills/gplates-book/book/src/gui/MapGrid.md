# MapGrid

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 212 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/MapGrid.h` | C++ | 78 |
| `src/gui/MapGrid.cc` | C++ | 420 |

## Overview

[[[PROSE overview unit=gui/MapGrid tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::vertex_type`](#anonymousvertex_type) | typedef | — | — | 0 | Vertex stream. |
| [`(anonymous)::vertex_element_type`](#anonymousvertex_element_type) | typedef | — | — | 0 | — |
| [`(anonymous)::stream_primitives_type`](#anonymousstream_primitives_type) | typedef | — | — | 0 | — |
| [`(anonymous)::projection_coord_type`](#anonymousprojection_coord_type) | typedef | — | — | 0 | Projection coordinates. |
| [`(anonymous)::projection_coord_seq_type`](#anonymousprojection_coord_seq_type) | typedef | — | — | 0 | — |
| [`GPlatesGui::MapGrid`](#gplatesguimapgrid) | class | `boost::noncopyable` | — | 0 | Renders latitude and longitude grid lines in the map view. |

## Members

### `(anonymous)::vertex_type`

*None.*

### `(anonymous)::vertex_element_type`

*None.*

### `(anonymous)::stream_primitives_type`

*None.*

### `(anonymous)::projection_coord_type`

*None.*

### `(anonymous)::projection_coord_seq_type`

*None.*

### `GPlatesGui::MapGrid`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MapGrid( GPlatesOpenGL::GLRenderer &renderer, const MapProjection &map_projection, const GraticuleSettings &graticule_settings)` | constructor | `None` | public | — |
| `paint( GPlatesOpenGL::GLRenderer &renderer)` | method | `void` | public | Paints lines of latitude and longitude on the map. |
| `d_map_projection` | field | `MapProjection` | private | — |
| `d_graticule_settings` | field | `GraticuleSettings` | private | — |
| `d_last_seen_map_projection_settings` | field | `boost::optional<MapProjectionSettings>` | private | — |
| `d_last_seen_graticule_settings` | field | `boost::optional<GraticuleSettings>` | private | — |
| `d_grid_vertex_array` | field | `GPlatesOpenGL::GLVertexArray::shared_ptr_type` | private | — |
| `d_grid_compiled_draw_state` | field | `boost::optional<GPlatesOpenGL::GLCompiledDrawState::non_null_ptr_to_const_type>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `LINE_OF_LATITUDE_NUM_SEGMENTS` | variable | `int` | The number of line segments along a line of latitude. |
| `LINE_OF_LONGITUDE_NUM_SEGMENTS` | variable | `int` | The number of line segments along a line of longitude. |
| `LINE_OF_LATITUDE_DELTA_LONGITUDE` | variable | `double` | The angular spacing a points along a line of latitude. |
| `LINE_OF_LONGITUDE_DELTA_LATITUDE` | variable | `double` | The angular spacing a points along a line of longitude. |
| `project_lat_lon( double lat, double lon, const GPlatesGui::MapProjection &projection)` | function | `projection_coord_type` | Projects the specified latitude/longitude using the specified map projection. |
| `set_line_draw_state( GPlatesOpenGL::GLRenderer &renderer, float line_width_hint)` | function | `void` | Sets the OpenGL state set that defines the appearance of the grid lines. |
| `stream_lines_of_lat( stream_primitives_type &stream, const GPlatesGui::MapProjection &map_projection, const double &lat_0, const double &lon_0, const double &delta_lat, const GPlatesGui::rgba8_t &colour)` | function | `void` | Draw lines of latitude. |
| `stream_lines_of_lon( stream_primitives_type &stream, const GPlatesGui::MapProjection &map_projection, const double &lat_0, const double &lon_0, const double &delta_lon, const GPlatesGui::rgba8_t &colour)` | function | `void` | Draw lines of longitude. |
| `compile_grid_draw_state( GPlatesOpenGL::GLRenderer &renderer, GPlatesOpenGL::GLVertexArray &vertex_array, const GPlatesGui::MapProjection &map_projection, const GPlatesMaths::Real &delta_lat, const GPlatesMaths::Real &delta_lon, const GPlatesGui::rgba8_t &colour, float line_width_hint)` | function | `GPlatesOpenGL::GLCompiledDrawState::non_null_ptr_to_const_type` | — |
| `GPLATES_GUI_MAPGRID_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/MapGrid tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Map](Map.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/MapGrid.h
python scripts/gpq.py def GPlatesGui::MapGrid --body
python scripts/gpq.py uses MapGrid --kind class
python scripts/gpq.py hier MapGrid
```

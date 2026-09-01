# MapBackground

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1324 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/MapBackground.h` | C++ | 98 |
| `src/gui/MapBackground.cc` | C++ | 350 |

## Overview

[[[PROSE overview unit=gui/MapBackground tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::vertex_type`](#anonymousvertex_type) | typedef | — | — | 0 | Vertex stream. |
| [`(anonymous)::vertex_element_type`](#anonymousvertex_element_type) | typedef | — | — | 0 | — |
| [`(anonymous)::stream_primitives_type`](#anonymousstream_primitives_type) | typedef | — | — | 0 | — |
| [`(anonymous)::projection_coord_type`](#anonymousprojection_coord_type) | typedef | — | — | 0 | Projection coordinates. |
| [`GPlatesGui::MapBackground`](#gplatesguimapbackground) | class | `boost::noncopyable` | — | 0 | Renders a coloured background map in the map view. |

## Members

### `(anonymous)::vertex_type`

*None.*

### `(anonymous)::vertex_element_type`

*None.*

### `(anonymous)::stream_primitives_type`

*None.*

### `(anonymous)::projection_coord_type`

*None.*

### `GPlatesGui::MapBackground`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MapBackground( GPlatesOpenGL::GLRenderer &renderer, const MapProjection &map_projection, const Colour &colour)` | constructor | `None` | public | Constructs a background with a fixed colour. |
| `MapBackground( GPlatesOpenGL::GLRenderer &renderer, const MapProjection &map_projection, const GPlatesPresentation::ViewState &view_state)` | constructor | `None` | public | Constructs a background that uses the background colour of view\_state, as it changes from time to time. |
| `paint( GPlatesOpenGL::GLRenderer &renderer)` | method | `void` | public | Paints the map background. |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_map_projection` | field | `MapProjection` | private | — |
| `d_colour` | field | `Colour` | private | — |
| `d_last_seen_map_projection_settings` | field | `boost::optional<MapProjectionSettings>` | private | — |
| `d_vertex_array` | field | `GPlatesOpenGL::GLVertexArray::shared_ptr_type` | private | — |
| `d_compiled_draw_state` | field | `GPlatesOpenGL::GLCompiledDrawState::non_null_ptr_to_const_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `LINE_OF_LATITUDE_NUM_SEGMENTS` | variable | `int` | The number of line segments along a line of latitude. |
| `LINE_OF_LONGITUDE_NUM_SEGMENTS` | variable | `int` | The number of line segments along a line of longitude. |
| `LINE_OF_LATITUDE_DELTA_LONGITUDE` | variable | `double` | The angular spacing a points along a line of latitude. |
| `LINE_OF_LONGITUDE_DELTA_LATITUDE` | variable | `double` | The angular spacing a points along a line of longitude. |
| `project_lat_lon( double lat, double lon, const GPlatesGui::MapProjection &projection)` | function | `projection_coord_type` | Projects the specified latitude/longitude using the specified map projection. |
| `stream_background( stream_primitives_type &stream, const GPlatesGui::MapProjection &projection, const GPlatesGui::rgba8_t &colour)` | function | `void` | — |
| `compile_background_draw_state( GPlatesOpenGL::GLRenderer &renderer, GPlatesOpenGL::GLVertexArray &vertex_array, const GPlatesGui::MapProjection &map_projection, const GPlatesGui::rgba8_t &colour)` | function | `GPlatesOpenGL::GLCompiledDrawState::non_null_ptr_to_const_type` | — |
| `GPLATES_GUI_MAPBACKGROUND_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/MapBackground tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Map](Map.md) | gui | 11 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 2 |
| [qt-widgets/MapView](../qt-widgets/MapView.md) | qt-widgets | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/MapBackground.h
python scripts/gpq.py def GPlatesGui::MapBackground --body
python scripts/gpq.py uses MapBackground --kind class
python scripts/gpq.py hier MapBackground
```

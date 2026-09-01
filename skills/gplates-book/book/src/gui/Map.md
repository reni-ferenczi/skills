# Map

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 992 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/Map.h` | C++ | 163 |
| `src/gui/Map.cc` | C++ | 194 |

## Overview

`GPlatesGui::Map` is the flat-map counterpart to `Gui::Globe`: it holds the
state behind `MapCanvas`/`MapView` and draws the map background, the lat/lon
`MapGrid`, and every visible `RenderedGeometry` (via a
`MapRenderedGeometryCollectionPainter` it owns), analogous to how `Globe`
composes `Stars`/`OpaqueSphere`/`SphericalGrid`/`GlobeRenderedGeometryCollectionPainter`.
Unlike the globe, it also owns a `MapProjection` and exposes
`projection_type()`/`set_projection_type()` and `central_meridian()`/
`set_central_meridian()` so the same rendered-geometry data can be reprojected
(e.g. Mercator, Robinson) and recentred without touching the underlying model.
As with `Globe`, `d_background` and `d_grid` are `boost::optional` because
they wrap OpenGL resources that cannot be built before `initialiseGL()` runs
against a bound context.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::Map`](#gplatesguimap) | class | — | — | 0 | Holds the state for MapCanvas/MapView (analogous to the Globe class). |

## Members

### `GPlatesGui::Map`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `cache_handle_type` | typedef | `boost::shared_ptr<void>` | public | Typedef for an opaque object that caches a particular painting. |
| `Map( GPlatesPresentation::ViewState &view_state, const GPlatesOpenGL::GLVisualLayers::non_null_ptr_type &gl_visual_layers, GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, const GPlatesPresentation::VisualLayers &visual_layers, ViewportZoom &viewport_zoom, const ColourScheme::non_null_pt ...` | constructor | `None` | public | — |
| `initialiseGL( GPlatesOpenGL::GLRenderer &renderer)` | method | `void` | public | Initialise any OpenGL state. |
| `projection` | field | `MapProjection` | public | — |
| `projection_type()` | method | `MapProjection::Type` | public | — |
| `set_projection_type( GPlatesGui::MapProjection::Type projection_type_)` | method | `void` | public | — |
| `central_meridian()` | method | `double` | public | — |
| `set_central_meridian( double central_meridian_)` | method | `void` | public | — |
| `paint( GPlatesOpenGL::GLRenderer &renderer, const double &viewport_zoom_factor, const double &device_independent_pixel_to_map_space_ratio, float scale)` | method | `cache_handle_type` | public | Paint the map and all the visible features and rasters on it. |
| `d_map_projection` | field | `MapProjection::non_null_ptr_type` | private | To do map projections |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_gl_visual_layers` | field | `GPlatesOpenGL::GLVisualLayers::non_null_ptr_type` | private | Keeps track of OpenGL-related objects that persist from one render to the next. |
| `d_rendered_geometry_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | A pointer to the state's RenderedGeometryCollection |
| `d_visual_layers` | field | `GPlatesPresentation::VisualLayers` | private | — |
| `d_viewport_zoom` | field | `GPlatesGui::ViewportZoom` | private | For zoom-dependent rendered objects. |
| `d_colour_scheme` | field | `GPlatesGui::ColourScheme::non_null_ptr_type` | private | For giving colour to RenderedGeometry |
| `d_background` | field | `boost::optional<MapBackground>` | private | The coloured map background (behind the grid and rendered geometry data). |
| `d_grid` | field | `boost::optional<MapGrid>` | private | Lines of lat and lon on the map. |
| `d_rendered_geom_collection_painter` | field | `MapRenderedGeometryCollectionPainter` | private | Painter used to draw rendered geometry layers onto the map. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_MAP_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 15 |
| [qt-widgets/MapView](../qt-widgets/MapView.md) | qt-widgets | 7 |
| [qt-widgets/GlobeAndMapWidget](../qt-widgets/GlobeAndMapWidget.md) | qt-widgets | 2 |
| [qt-widgets/ProjectionControlWidget](../qt-widgets/ProjectionControlWidget.md) | qt-widgets | 2 |
| [canvas-tools/CanvasToolAdapterForMap](../canvas-tools/CanvasToolAdapterForMap.md) | canvas-tools | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/Map.h
python scripts/gpq.py def GPlatesGui::Map --body
python scripts/gpq.py uses Map --kind class
python scripts/gpq.py hier Map
```

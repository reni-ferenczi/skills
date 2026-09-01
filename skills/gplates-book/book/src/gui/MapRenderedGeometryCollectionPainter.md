# MapRenderedGeometryCollectionPainter

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 942 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/MapRenderedGeometryCollectionPainter.h` | C++ | 184 |
| `src/gui/MapRenderedGeometryCollectionPainter.cc` | C++ | 163 |

## Overview

[[[PROSE overview unit=gui/MapRenderedGeometryCollectionPainter tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::MapRenderedGeometryCollectionPainter`](#gplatesguimaprenderedgeometrycollectionpainter) | class | [`GPlatesViewOperations::ConstRenderedGeometryCollectionVisitor< GPlatesPresentation::VisualLayers::rendered_geometry_layer_seq_type>`](../view-operations/RenderedGeometryCollectionVisitor.md)<br>`boost::noncopyable` | — | 0 | Draws rendered geometries (in a RenderedGeometryCollection) onto a map view of the globe using OpenGL. |

## Members

### `GPlatesGui::MapRenderedGeometryCollectionPainter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `cache_handle_type` | typedef | `boost::shared_ptr<void>` | public | Typedef for an opaque object that caches a particular painting. |
| `MapRenderedGeometryCollectionPainter( const MapProjection::non_null_ptr_to_const_type &map_projection, const GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, const GPlatesOpenGL::GLVisualLayers::non_null_ptr_type &gl_visual_layers, const GPlatesPresentation::VisualLayers &visual_layers, ...` | constructor | `None` | public | — |
| `initialise( GPlatesOpenGL::GLRenderer &renderer)` | method | `void` | public | Initialise objects requiring GLRenderer. |
| `paint( GPlatesOpenGL::GLRenderer &renderer, const double &viewport_zoom_factor, const double &device_independent_pixel_to_map_space_ratio)` | method | `cache_handle_type` | public | Draw the rendered geometries. |
| `set_scale( float scale)` | method | `void` | public | — |
| `get_custom_child_layers_order( GPlatesViewOperations::RenderedGeometryCollection::MainLayerType parent_layer)` | method | `boost::optional<GPlatesPresentation::VisualLayers::rendered_geometry_layer_seq_type>` | public | — |
| `visit_main_rendered_layer( const GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, GPlatesViewOperations::RenderedGeometryCollection::MainLayerType main_rendered_layer_type)` | method | `bool` | private | — |
| `visit_rendered_geometry_layer( const GPlatesViewOperations::RenderedGeometryLayer &rendered_geometry_layer)` | method | `bool` | private | — |
| `base_type` | typedef | `GPlatesViewOperations::ConstRenderedGeometryCollectionVisitor< GPlatesPresentation::VisualLayers::rendered_geometry_layer_seq_type>` | private | Typedef for the base class. |
| `PaintParams` | struct | `None` | private | Parameters that are only available when paint is called. |
| `d_paint_params` | field | `boost::optional<PaintParams>` | private | Parameters that are only available when paint is called. |
| `d_map_projection` | field | `MapProjection::non_null_ptr_to_const_type` | private | Used to project vertices of rendered geometries to the map. |
| `d_rendered_geometry_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | — |
| `d_gl_visual_layers` | field | `GPlatesOpenGL::GLVisualLayers::non_null_ptr_type` | private | Keeps track of OpenGL-related objects that persist from one render to the next. |
| `d_visual_layers` | field | `GPlatesPresentation::VisualLayers` | private | — |
| `d_layer_painter` | field | `LayerPainter` | private | Used to paint the layers. |
| `d_colour_scheme` | field | `ColourScheme::non_null_ptr_type` | private | For assigning colours to RenderedGeometry |
| `d_scale` | field | `float` | private | When rendering globes that are meant to be a scale copy of another |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_MAPRENDEREDGEOMETRYCOLLECTIONPAINTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/MapRenderedGeometryCollectionPainter tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Map](Map.md) | gui | 10 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/MapRenderedGeometryCollectionPainter.h
python scripts/gpq.py def GPlatesGui::MapRenderedGeometryCollectionPainter --body
python scripts/gpq.py uses MapRenderedGeometryCollectionPainter --kind class
python scripts/gpq.py hier MapRenderedGeometryCollectionPainter
```

# RenderedResolvedRaster

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1227 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedResolvedRaster.h` | C++ | 138 |

## Overview

A rendered geometry wrapper for a georeferenced raster (grid or image). This class holds a `ResolvedRaster`, a `RasterColourPalette` for colouring integral or floating-point data, a modulation colour, and a height-field scale factor for normal-map lighting effects. Rasters are displayed on the globe after reconstruction, with rendering handled by the painters that consume this class.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedResolvedRaster`](#gplatesviewoperationsrenderedresolvedraster) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | — |

## Members

### `GPlatesViewOperations::RenderedResolvedRaster`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedResolvedRaster( const GPlatesAppLogic::ResolvedRaster::non_null_ptr_to_const_type &resolved_raster, const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &raster_colour_palette, const GPlatesGui::Colour &raster_modulate_colour, float normal_map_height_field_scale_factor)` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `get_resolved_raster()` | method | `GPlatesAppLogic::ResolvedRaster::non_null_ptr_to_const_type` | public | — |
| `get_normal_map_height_field_scale_factor()` | method | `float` | public | — |
| `d_resolved_raster` | field | `GPlatesAppLogic::ResolvedRaster::non_null_ptr_to_const_type` | private | The resolved raster. |
| `d_raster_colour_palette` | field | `GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type` | private | The colour palette used to colour integral and floating-point rasters. |
| `d_raster_modulate_colour` | field | `GPlatesGui::Colour` | private | The modulation colour to multiply the raster with. |
| `d_normal_map_height_field_scale_factor` | field | `float` | private | Alters the surface lighting if a normal map is used. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDRESOLVEDRASTER_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 3 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 3 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedResolvedRaster.h
python scripts/gpq.py def GPlatesViewOperations::RenderedResolvedRaster --body
python scripts/gpq.py uses RenderedResolvedRaster --kind class
python scripts/gpq.py hier RenderedResolvedRaster
```

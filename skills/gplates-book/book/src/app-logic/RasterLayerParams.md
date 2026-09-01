# RasterLayerParams

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 285 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/RasterLayerParams.h` | C++ | 217 |
| `src/app-logic/RasterLayerParams.cc` | C++ | 170 |

## Overview

`RasterLayerParams` is the `LayerParams` subclass a raster layer uses to hold the parts of a raster feature that other layers (and the presentation-side `RasterVisualLayerParams`) need without re-visiting the feature: which band is selected, that band's `GPlatesPropertyValues::RasterStatistics`, the full list of band names and per-band statistics, the raster's `Georeferencing`, `SpatialReferenceSystem` and `RasterType`. `set_raster_feature` re-derives all of this from the feature by running an `ExtractRasterFeatureProperties` visitor at present day, since georeferencing, band names and statistics live in the feature's properties rather than on this object; `set_band_name` only re-selects which already-extracted band's statistics are exposed through `get_band_statistic`, falling back to band index zero when the requested name is not one of the raster's actual bands.

Both setters emit Qt signals — `modified_band_name` plus the inherited `modified` — so that downstream layers and presentation params can react to a raster or band swap, for example to refresh a colour palette built from the previous band's statistics.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::RasterLayerParams`](#gplatesapplogicrasterlayerparams) | class | [`LayerParams`](LayerParams.md) | — | 0 | App-logic parameters for a raster layer. |

## Members

### `GPlatesAppLogic::RasterLayerParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<RasterLayerParams>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const RasterLayerParams>` | public | — |
| `create()` | method | `non_null_ptr_type` | public | — |
| `set_band_name( GPlatesPropertyValues::TextContent band_name)` | method | `void` | public | Sets the name of the band, of the raster, selected for processing. |
| `set_raster_feature( boost::optional<GPlatesModel::FeatureHandle::weak_ref> feature_ref)` | method | `void` | public | Sets (or unsets) the raster feature. |
| `get_band_statistic()` | method | `GPlatesPropertyValues::RasterStatistics` | public | Returns the raster statistics of the band of the raster selected for processing. |
| `get_raster_type()` | method | `GPlatesPropertyValues::RasterType::Type` | public | Returns the raster's type. |
| `accept_visitor( ConstLayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in LayerParams base. |
| `accept_visitor( LayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in LayerParams base. |
| `modified_band_name( GPlatesAppLogic::RasterLayerParams &layer_params)` | method | `void` | public | Emitted when set\_band\_name has been called (if a change detected). |
| `d_raster_feature` | field | `boost::optional<GPlatesModel::FeatureHandle::weak_ref>` | private | The raster feature. |
| `d_band_name` | field | `GPlatesPropertyValues::TextContent` | private | The name of the band of the raster that has been selected for processing. |
| `d_band_names` | field | `GPlatesPropertyValues::GpmlRasterBandNames::band_names_list_type` | private | The list of band names that were in the raster feature the last time we examined it. |
| `d_band_statistic` | field | `GPlatesPropertyValues::RasterStatistics` | private | The raster statistics of the band of the raster selected for processing. |
| `d_band_statistics` | field | `std::vector<GPlatesPropertyValues::RasterStatistics>` | private | The list of raster statistics for the raster bands. |
| `d_georeferencing` | field | `boost::optional<GPlatesPropertyValues::Georeferencing::non_null_ptr_to_const_type>` | private | The georeferencing of the raster. |
| `d_spatial_reference_system` | field | `boost::optional<GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type>` | private | The raster's spatial reference system. |
| `d_raster_type` | field | `GPlatesPropertyValues::RasterType::Type` | private | The raster's type. |
| `RasterLayerParams()` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RASTERLAYERPARAMS_H` | macro | `None` | — |

## Notes

- For time-dependent rasters, `get_band_statistic`/`get_band_statistics` are always the statistics computed at present day, not at the current reconstruction time — `set_raster_feature` visits the feature without specifying a reconstruction time.
- `set_raster_feature` clears every derived field (band names, statistics, georeferencing, spatial reference system, raster type) up front and unconditionally calls `emit_modified()`, even when the new feature turns out to be equivalent to the old one or when there is no feature at all (`boost::none`).
- If the current band name is not among the feature's actual band names, both `set_band_name` and `set_raster_feature` silently fall back to band index 0 rather than leaving the selection unset.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/RasterLayerProxy](RasterLayerProxy.md) | app-logic | 21 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 13 |
| [app-logic/RasterLayerTask](RasterLayerTask.md) | app-logic | 8 |
| [qt-widgets/RasterLayerOptionsWidget](../qt-widgets/RasterLayerOptionsWidget.md) | qt-widgets | 6 |
| [presentation/RasterVisualLayerParams](../presentation/RasterVisualLayerParams.md) | presentation | 5 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/RasterLayerParams.h
python scripts/gpq.py def GPlatesAppLogic::RasterLayerParams --body
python scripts/gpq.py uses RasterLayerParams --kind class
python scripts/gpq.py hier RasterLayerParams
```

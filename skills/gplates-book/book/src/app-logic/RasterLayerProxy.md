# RasterLayerProxy

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 386 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/RasterLayerProxy.h` | C++ | 838 |
| `src/app-logic/RasterLayerProxy.cc` | C++ | 924 |

## Overview

[[[PROSE overview unit=app-logic/RasterLayerProxy tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::RasterLayerProxy`](#gplatesapplogicrasterlayerproxy) | class | [`LayerProxy`](LayerProxy.md) | — | 0 | A layer proxy for resolving, and optionally reconstructing, a raster. |

## Members

### `GPlatesAppLogic::RasterLayerProxy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<RasterLayerProxy>` | public | A convenience typedef for a shared pointer to a non-const RasterLayerProxy. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const RasterLayerProxy>` | public | A convenience typedef for a shared pointer to a const RasterLayerProxy. |
| `create()` | method | `non_null_ptr_type` | public | Creates a RasterLayerProxy object. |
| `get_spatial_reference_system()` | method | `boost::optional<GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type>` | public | Returns the raster's spatial reference system (if any). |
| `get_coordinate_transformation()` | method | `GPlatesPropertyValues::CoordinateTransformation::non_null_ptr_to_const_type` | public | Returns the transform from the raster's spatial reference to the standard WGS84. |
| `get_proxied_raster` | field | `boost::optional<GPlatesPropertyValues::RawRaster::non_null_ptr_type>` | public | Returns the proxied raw raster, for the specified time and specified raster band name. |
| `get_proxied_rasters` | field | `boost::optional<std::vector<GPlatesPropertyValues::RawRaster::non_null_ptr_type> >` | public | Returns the list of proxied rasters, for the specified time, for the raster bands. |
| `get_resolved_raster()` | method | `boost::optional<GPlatesGlobal::PointerTraits<ResolvedRaster>::non_null_ptr_type>` | public | Returns the resolved raster for the current reconstruction time. |
| `get_resolved_raster( const double &reconstruction_time)` | method | `boost::optional<GPlatesGlobal::PointerTraits<ResolvedRaster>::non_null_ptr_type>` | public | Returns the resolved raster for the specified time. |
| `does_raster_band_contain_numerical_data( const GPlatesPropertyValues::TextContent &raster_band_name)` | method | `bool` | public | Returns true if the raster (in the specified band) contains numerical data (such as floating-point or integer pixels, but not RGBA colour pixels). |
| `get_multi_resolution_data_raster( GPlatesOpenGL::GLRenderer &renderer)` | method | `boost::optional<GPlatesOpenGL::GLMultiResolutionRasterInterface::non_null_ptr_type>` | public | Returns the possibly reconstructed (multi-resolution) \*data\* raster for the current reconstruction time and current raster band. |
| `get_multi_resolution_data_raster( GPlatesOpenGL::GLRenderer &renderer, const GPlatesPropertyValues::TextContent &raster_band_name)` | method | `boost::optional<GPlatesOpenGL::GLMultiResolutionRasterInterface::non_null_ptr_type>` | public | Returns the possibly reconstructed (multi-resolution) \*data\* raster, for the current reconstruction time and specified raster band name. |
| `get_multi_resolution_data_raster( GPlatesOpenGL::GLRenderer &renderer, const double &reconstruction_time)` | method | `boost::optional<GPlatesOpenGL::GLMultiResolutionRasterInterface::non_null_ptr_type>` | public | Returns the possibly reconstructed (multi-resolution) \*data\* raster, current raster band name at the specified time. |
| `get_multi_resolution_data_raster( GPlatesOpenGL::GLRenderer &renderer, const double &reconstruction_time, const GPlatesPropertyValues::TextContent &raster_band_name)` | method | `boost::optional<GPlatesOpenGL::GLMultiResolutionRasterInterface::non_null_ptr_type>` | public | Returns the possibly reconstructed (multi-resolution) \*data\* raster, for the specified time and specified raster band name. |
| `get_multi_resolution_data_cube_raster( GPlatesOpenGL::GLRenderer &renderer)` | method | `boost::optional<GPlatesOpenGL::GLMultiResolutionCubeRasterInterface::non_null_ptr_type>` | public | This is the same as get\_multi\_resolution\_data\_raster but returns a \*cube\* version of the raster. |
| `get_multi_resolution_data_cube_raster( GPlatesOpenGL::GLRenderer &renderer, const GPlatesPropertyValues::TextContent &raster_band_name)` | method | `boost::optional<GPlatesOpenGL::GLMultiResolutionCubeRasterInterface::non_null_ptr_type>` | public | Returns the possibly reconstructed (multi-resolution) \*data\* cube raster, for the current reconstruction time and specified raster band name. |
| `get_multi_resolution_data_cube_raster( GPlatesOpenGL::GLRenderer &renderer, const double &reconstruction_time)` | method | `boost::optional<GPlatesOpenGL::GLMultiResolutionCubeRasterInterface::non_null_ptr_type>` | public | Returns the possibly reconstructed (multi-resolution) \*data\* cube raster, current raster band name at the specified time. |
| `get_multi_resolution_data_cube_raster( GPlatesOpenGL::GLRenderer &renderer, const double &reconstruction_time, const GPlatesPropertyValues::TextContent &raster_band_name)` | method | `boost::optional<GPlatesOpenGL::GLMultiResolutionCubeRasterInterface::non_null_ptr_type>` | public | Returns the possibly reconstructed (multi-resolution) \*data\* cube raster, for the specified time and specified raster band name. |
| `get_multi_resolution_age_grid_mask( GPlatesOpenGL::GLRenderer &renderer)` | method | `boost::optional<GPlatesOpenGL::GLMultiResolutionCubeRaster::non_null_ptr_type>` | public | Returns the multi-resolution age grid mask cube raster for the current reconstruction time and current raster band. |
| `get_multi_resolution_age_grid_mask( GPlatesOpenGL::GLRenderer &renderer, const GPlatesPropertyValues::TextContent &raster_band_name)` | method | `boost::optional<GPlatesOpenGL::GLMultiResolutionCubeRaster::non_null_ptr_type>` | public | Returns the multi-resolution age grid mask cube raster for the current reconstruction time and specified raster band. |
| `get_multi_resolution_age_grid_mask( GPlatesOpenGL::GLRenderer &renderer, const double &reconstruction_time)` | method | `boost::optional<GPlatesOpenGL::GLMultiResolutionCubeRaster::non_null_ptr_type>` | public | Returns the multi-resolution age grid mask cube raster for the specified reconstruction time and current raster band. |
| `get_multi_resolution_age_grid_mask( GPlatesOpenGL::GLRenderer &renderer, const double &reconstruction_time, const GPlatesPropertyValues::TextContent &raster_band_name)` | method | `boost::optional<GPlatesOpenGL::GLMultiResolutionCubeRaster::non_null_ptr_type>` | public | Returns the multi-resolution age grid mask cube raster for the specified reconstruction time and specified raster band. |
| `get_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns the subject token that clients can use to determine if this raster layer proxy has changed. |
| `get_proxied_raster_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns the subject token that clients can use to determine if the proxied raster has changed for the specified reconstruction time. |
| `get_raster_feature_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns the subject token that clients can use to determine if the raster feature has changed. |
| `accept_visitor( ConstLayerProxyVisitor &visitor)` | method | `void` | public | Accept a ConstLayerProxyVisitor instance. |
| `accept_visitor( LayerProxyVisitor &visitor)` | method | `void` | public | Accept a LayerProxyVisitor instance. |
| `set_current_reconstruction_time( const double &reconstruction_time)` | method | `void` | public | Sets the current reconstruction time as set by the layer system. |
| `add_current_reconstructed_polygons_layer_proxy( const ReconstructLayerProxy::non_null_ptr_type &reconstructed_polygons_layer_proxy)` | method | `void` | public | Adds the specified reconstructed polygons layer proxy. |
| `remove_current_reconstructed_polygons_layer_proxy( const ReconstructLayerProxy::non_null_ptr_type &reconstructed_polygons_layer_proxy)` | method | `void` | public | Removes the specified reconstructed polygons layer proxy. |
| `set_current_age_grid_raster_layer_proxy( boost::optional<RasterLayerProxy::non_null_ptr_type> age_grid_raster_layer_proxy)` | method | `void` | public | Set the age grid raster layer proxy. |
| `set_current_normal_map_raster_layer_proxy( boost::optional<RasterLayerProxy::non_null_ptr_type> normal_map_raster_layer_proxy)` | method | `void` | public | Set the normal map raster layer proxy. |
| `set_current_raster_feature( boost::optional<GPlatesModel::FeatureHandle::weak_ref> raster_feature, const RasterLayerParams &raster_params)` | method | `void` | public | Specify the raster feature. |
| `set_current_raster_band_name( const RasterLayerParams &raster_params)` | method | `void` | public | The currently selected raster band name has changed. |
| `modified_raster_feature( const RasterLayerParams &raster_params)` | method | `void` | public | The raster feature has been modified. |
| `ResolvedRasterFeatureProperties` | struct | `None` | private | Potentially time-varying feature properties for the currently resolved raster (ie, at the cached reconstruction time). |
| `MultiResolutionDataRaster` | struct | `None` | private | A cached OpenGL multi-resolution \*data\* raster (and its raster data source) containing numerical raster data. |
| `MultiResolutionAgeGridRaster` | struct | `None` | private | A cached OpenGL multi-resolution \*age grid\* raster. |
| `d_current_reconstructed_polygons_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<ReconstructLayerProxy>` | private | The input reconstructed polygons, if any connected to our input. |
| `d_current_age_grid_raster_layer_proxy` | field | `LayerProxyUtils::OptionalInputLayerProxy<RasterLayerProxy>` | private | Optional age grid raster input. |
| `d_current_normal_map_raster_layer_proxy` | field | `LayerProxyUtils::OptionalInputLayerProxy<RasterLayerProxy>` | private | Optional normal map raster input. |
| `d_current_raster_feature` | field | `boost::optional<GPlatesModel::FeatureHandle::weak_ref>` | private | The raster input feature. |
| `d_current_raster_band_name` | field | `GPlatesPropertyValues::TextContent` | private | The selected raster band name. |
| `d_current_raster_band_names` | field | `GPlatesPropertyValues::GpmlRasterBandNames::band_names_list_type` | private | The raster band names. |
| `d_current_georeferencing` | field | `boost::optional<GPlatesPropertyValues::Georeferencing::non_null_ptr_to_const_type>` | private | The georeferencing of the raster. |
| `d_current_spatial_reference_system` | field | `boost::optional<GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type>` | private | The raster's spatial reference system (if any). |
| `d_current_coordinate_transformation` | field | `GPlatesPropertyValues::CoordinateTransformation::non_null_ptr_to_const_type` | private | The coordinate transformation from raster to WGS84. |
| `d_current_reconstruction_time` | field | `double` | private | The current reconstruction time as set by the layer system. |
| `d_cached_resolved_raster_feature_properties` | field | `ResolvedRasterFeatureProperties` | private | Time-varying (potentially) raster feature properties. |
| `d_cached_multi_resolution_data_raster` | field | `MultiResolutionDataRaster` | private | An OpenGL (possibly reconstructed) multi-resolution \*data\* raster containing numerical raster data. |
| `d_cached_multi_resolution_age_grid_raster` | field | `MultiResolutionAgeGridRaster` | private | An OpenGL multi-resolution \*age grid\* raster. |
| `d_subject_token` | field | `GPlatesUtils::SubjectToken` | private | Used to notify polling observers that we've been updated. |
| `d_proxied_raster_subject_token` | field | `GPlatesUtils::SubjectToken` | private | The subject token that clients can use to determine if the proxied raster has changed. |
| `d_raster_feature_subject_token` | field | `GPlatesUtils::SubjectToken` | private | The subject token that clients can use to determine if the raster feature has changed. |
| `RasterLayerProxy()` | constructor | `None` | private | — |
| `invalidate_raster_feature()` | method | `void` | private | — |
| `invalidate_proxied_raster()` | method | `void` | private | — |
| `invalidate()` | method | `void` | private | — |
| `resolve_raster_feature( const double &reconstruction_time, const GPlatesPropertyValues::TextContent &raster_band_name)` | method | `bool` | private | Attempts to resolve a raster. |
| `set_raster_params( const RasterLayerParams &raster_params)` | method | `void` | private | Sets some raster parameters. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RASTERLAYERPROXY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/RasterLayerProxy tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 130 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 76 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 62 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 17 |
| [qt-widgets/MapView](../qt-widgets/MapView.md) | qt-widgets | 16 |
| [app-logic/CoRegistrationLayerProxy](CoRegistrationLayerProxy.md) | app-logic | 14 |
| [app-logic/RasterLayerTask](RasterLayerTask.md) | app-logic | 12 |
| [app-logic/CoRegistrationLayerTask](CoRegistrationLayerTask.md) | app-logic | 5 |
| [gui/Globe](../gui/Globe.md) | gui | 5 |
| [gui/Map](../gui/Map.md) | gui | 5 |
| [gui/GlobeRenderedGeometryCollectionPainter](../gui/GlobeRenderedGeometryCollectionPainter.md) | gui | 4 |
| [presentation/LayerOutputRenderer](../presentation/LayerOutputRenderer.md) | presentation | 3 |
| [view-operations/RenderedResolvedRaster](../view-operations/RenderedResolvedRaster.md) | view-operations | 3 |
| [app-logic/ResolvedRaster](ResolvedRaster.md) | app-logic | 2 |
| [data-mining/DataSelector](../data-mining/DataSelector.md) | data-mining | 2 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 2 |
| [view-operations/RenderedGeometryFactory](../view-operations/RenderedGeometryFactory.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/RasterLayerProxy.h
python scripts/gpq.py def GPlatesAppLogic::RasterLayerProxy --body
python scripts/gpq.py uses RasterLayerProxy --kind class
python scripts/gpq.py hier RasterLayerProxy
```

# RasterLayerProxy

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 386 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/RasterLayerProxy.h` | C++ | 838 |
| `src/app-logic/RasterLayerProxy.cc` | C++ | 924 |

## Overview

The output end of a raster layer. Like every `LayerProxy` it is a pull-model
cache: `RasterLayerTask` pushes in the inputs (the raster feature and its
`RasterLayerParams`, the current reconstruction time, and the connected
`ReconstructLayerProxy` polygon layers, age-grid layer and normal-map layer), and
nothing is computed until a client asks. What a client gets back depends on why it
is asking, and this class serves three distinct answers from three separate
caches.

`get_proxied_raster` / `get_proxied_rasters` is the plain data path: it runs
`ExtractRasterFeatureProperties` over the raster feature at a time and hands back
the proxied `RawRaster` for the selected band — proxied, so the pixels are still
on disk. `get_resolved_raster` is the *visualisation* path, and deliberately
computes nothing: it just packages this proxy plus the connected polygon, age-grid
and normal-map proxies into a `ResolvedRaster` reconstruction geometry, leaving
`GLVisualLayers::render_raster()` in the presentation tier to do the drawing —
app-logic is not supposed to know about colour. `get_multi_resolution_data_raster`
is the *analysis* path, and does build OpenGL objects: a `GLDataRasterSource` over
the proxied raster, a `GLMultiResolutionRaster` over that, and — if reconstructed
polygons or an age grid are connected — a cube raster and a
`GLMultiResolutionStaticPolygonReconstructedRaster` on top. It exists for clients
that need to read numerical values back, principally raster co-registration in
`data-mining` and numerical raster export.

The fourth role is passive: a raster layer can *be* an age grid for some other
raster layer. `get_multi_resolution_age_grid_mask` builds the age-grid pyramid
from this layer's own present-day raster, and the neighbouring raster layer calls
it while reconstructing itself. A single `RasterLayerProxy` can play both roles at
once — visualised as a raster in its own right while also assisting another
layer's reconstruction — which is why the age-grid pyramid lives in its own
`MultiResolutionAgeGridRaster` cache, entirely separate from
`MultiResolutionDataRaster`.

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

**The cache holds exactly one reconstruction time.** All the `get_*` overloads
that take no time simply substitute `d_current_reconstruction_time`, and
`resolve_raster_feature` re-runs whenever the requested time differs from
`cached_reconstruction_time`. For a time-dependent raster, alternating requests
between two times therefore thrashes the cache. Note also that
`set_current_reconstruction_time` deliberately does *not* invalidate anything —
invalidation happens lazily, on the first request at a different time.

**Three subject tokens, three granularities**, and picking the wrong one costs
correctness or performance. `d_subject_token` means "anything about this layer
changed". `d_proxied_raster_subject_token` means "the raw raster for this time
changed", which is what a time-dependent raster moves. `d_raster_feature_subject_token`
is the narrowest and exists specifically for age-grid consumers: they only ever
read the present-day raster, so they must not be woken by time changes.
Invalidation cascades downward — `invalidate_raster_feature` implies
`invalidate_proxied_raster` implies `invalidate` — never upward.

**`get_subject_token()` has a side effect and must be called.** Input layer
proxies are *polled*, not pushed: the method walks each
`InputLayerProxy`/`OptionalInputLayerProxy` wrapper, and invalidates
`d_subject_token` if any input has moved. A client that reads `d_subject_token`
without going through this method will miss upstream changes. The same method
explicitly skips the age-grid and normal-map inputs when they point at `this`,
because a raster layer may legitimately be its own age grid and polling itself
would recurse.

**`get_multi_resolution_*` need a live OpenGL context.** They take a
`GLRenderer &` and must be called from the render thread with the context current;
they are not usable from arbitrary app-logic code. They also fail softly, by
returning `boost::none` after a `qWarning`, for the ordinary runtime conditions:
no floating-point texture support, no georeferencing, or an RGBA (non-numerical)
raster. Callers must handle `boost::none` as normal, not exceptional.

**Cached rasters are deliberately memory-hungry.** Both the data raster and the
age-grid mask are created with
`CACHE_TILE_TEXTURES_ENTIRE_LEVEL_OF_DETAIL_PYRAMID`, because the analysis clients
re-read the whole raster every frame and re-loading tiles from disk would dominate.
The documented mitigation is to let the user choose a lower level of detail, not
to change this flag. Note also that `MultiResolutionDataRaster::invalidate()`
deliberately keeps the unreconstructed `cached_data_raster`, relying on
`cached_proxied_raster_observer` to rebuild it only when the proxied raster
actually changed; only the reconstructed raster and the borrowed objects from
other layers are dropped.

**The age-grid mask has two implementations.** `use_age_grid_data_source` probes
`GLMultiResolutionStaticPolygonReconstructedRaster::supports_age_mask_generation`
once and caches the answer in a `mutable` field: on capable hardware the returned
raster is a floating-point `GLDataRasterSource` holding actual ages, otherwise a
fixed-point `GLAgeGridMaskSource` holding pre-computed comparisons that must be
told the reconstruction time via `update_reconstruction_time`. Code consuming the
returned cube raster must not assume either encoding.

**`get_multi_resolution_data_cube_raster` may hand back shared state.** The
returned cube raster is cached, and a world transform set on it by one caller
persists for the next; the header recommends wrapping
`get_multi_resolution_data_raster` in your own cube raster instead.

**Feature ownership.** `d_current_raster_feature` is a `weak_ref` and is
re-checked with `is_valid()` on every resolve; a deleted feature makes the proxy
return `boost::none` rather than fail. `set_raster_params` re-reads everything
from `RasterLayerParams` and falls back to an identity
`CoordinateTransformation` whenever the raster has no spatial reference system or
one that cannot be turned into a transformation.

The normal-map input is carried here only so it can be forwarded into
`ResolvedRaster`; the header itself flags this as a layering violation, since a
normal map is purely a visualisation concern.

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

# ScalarField3DLayerProxy

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 342 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ScalarField3DLayerProxy.h` | C++ | 556 |
| `src/app-logic/ScalarField3DLayerProxy.cc` | C++ | 725 |

## Overview

The `LayerProxy` for the 3D scalar field layer: it wraps a single scalar-field-carrying feature, resolves it into a `ResolvedScalarField3D` for `GLVisualLayers` to volume-render, and gathers the auxiliary geometry that shapes how that volume is displayed. Two independent kinds of auxiliary input can be plugged in, each from up to three geometry sources (`ReconstructLayerProxy` for reconstructed static features, `TopologyGeometryResolverLayerProxy` for resolved topological boundaries, `TopologyNetworkResolverLayerProxy` for resolved networks): "cross sections" are geometries sliced through the volume, and the "surface polygons mask" limits the region over which the field is rendered. Each kind has its own `add_*`/`remove_*` pair of methods per source type, all tracked via `LayerProxyUtils::InputLayerProxySequence`.

Like other layer proxies, results are computed lazily and cached against a reconstruction time: `ResolvedScalarFieldFeatureProperties`, `CrossSections` and `SurfacePolygonsMask` each cache their own `cached_reconstruction_time` alongside their data, and `resolve_scalar_field_feature` re-extracts the field's properties (currently just its filename) only when the requested time does not match what is cached. `check_input_layer_proxies` compares each connected input proxy's own subject token against a locally-stored copy every time cross sections or the mask are requested, invalidating and re-fetching only the caches whose inputs actually changed.

Three `SubjectToken`s let dependents poll for change at different granularities: `get_subject_token` for any change to this layer at all, `get_scalar_field_subject_token` for changes to the resolved field specifically (useful once fields become time-dependent), and `get_scalar_field_feature_subject_token` for changes to just the input feature reference.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ScalarField3DLayerProxy`](#gplatesapplogicscalarfield3dlayerproxy) | class | [`LayerProxy`](LayerProxy.md) | — | 0 | A layer proxy for a 3D scalar field to be visualised using volume rendering. |

## Members

### `GPlatesAppLogic::ScalarField3DLayerProxy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ScalarField3DLayerProxy>` | public | A convenience typedef for a shared pointer to a non-const ScalarField3DLayerProxy. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ScalarField3DLayerProxy>` | public | A convenience typedef for a shared pointer to a const ScalarField3DLayerProxy. |
| `surface_polygons_mask_seq_type` | typedef | `std::vector<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | public | Typedef for a sequence of surface polygon mask geometries (polylines, polygons). |
| `cross_sections_seq_type` | typedef | `std::vector<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | public | Typedef for a sequence of surface polygon mask geometries (polylines, polygons). |
| `create()` | method | `non_null_ptr_type` | public | Creates a ScalarField3DLayerProxy object. |
| `get_scalar_field_filename` | field | `boost::optional<GPlatesPropertyValues::TextContent>` | public | Returns the scalar field filename at the specified reconstruction time. |
| `get_resolved_scalar_field_3d()` | method | `boost::optional<GPlatesGlobal::PointerTraits<ResolvedScalarField3D>::non_null_ptr_type>` | public | Returns the resolved scalar field for the current reconstruction time. |
| `get_resolved_scalar_field_3d( const double &reconstruction_time)` | method | `boost::optional<GPlatesGlobal::PointerTraits<ResolvedScalarField3D>::non_null_ptr_type>` | public | Returns the resolved scalar field for the specified time. |
| `get_cross_sections( cross_sections_seq_type &cross_sections)` | method | `bool` | public | Returns the cross sections (geometries) for the current reconstruction time. |
| `get_cross_sections( cross_sections_seq_type &cross_sections, const double &reconstruction_time)` | method | `bool` | public | Returns the cross sections (geometries) for the specified time. |
| `get_surface_polygons_mask( surface_polygons_mask_seq_type &surface_polygons_mask)` | method | `bool` | public | Returns the surface polygons mask (geometries) for the current reconstruction time. |
| `get_surface_polygons_mask( surface_polygons_mask_seq_type &surface_polygons_mask, const double &reconstruction_time)` | method | `bool` | public | Returns the surface polygons mask (geometries) for the specified time. |
| `get_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns the subject token that clients can use to determine if this scalar field layer proxy has changed. |
| `get_scalar_field_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns the subject token that clients can use to determine if the scalar field itself has changed for the specified reconstruction time. |
| `get_scalar_field_feature_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns the subject token that clients can use to determine if the scalar field feature has changed. |
| `accept_visitor( ConstLayerProxyVisitor &visitor)` | method | `void` | public | Accept a ConstLayerProxyVisitor instance. |
| `accept_visitor( LayerProxyVisitor &visitor)` | method | `void` | public | Accept a LayerProxyVisitor instance. |
| `set_current_reconstruction_time( const double &reconstruction_time)` | method | `void` | public | Sets the current reconstruction time as set by the layer system. |
| `set_current_scalar_field_feature( boost::optional<GPlatesModel::FeatureHandle::weak_ref> scalar_field_feature, const ScalarField3DLayerParams &scalar_field_params)` | method | `void` | public | Specify the scalar field feature. |
| `modified_scalar_field_feature( const ScalarField3DLayerParams &scalar_field_params)` | method | `void` | public | The scalar field feature has been modified. |
| `add_cross_section_reconstructed_geometries_layer_proxy( const ReconstructLayerProxy::non_null_ptr_type &reconstructed_geometries_layer_proxy)` | method | `void` | public | Add a 'cross section' reconstructed static geometries layer proxy. |
| `remove_cross_section_reconstructed_geometries_layer_proxy( const ReconstructLayerProxy::non_null_ptr_type &reconstructed_geometries_layer_proxy)` | method | `void` | public | Remove a 'cross section' reconstructed static geometries layer proxy. |
| `add_cross_section_topological_boundary_resolver_layer_proxy( const TopologyGeometryResolverLayerProxy::non_null_ptr_type &topological_boundary_resolver_layer_proxy)` | method | `void` | public | Add a 'cross section' topological boundary resolver layer proxy. |
| `remove_cross_section_topological_boundary_resolver_layer_proxy( const TopologyGeometryResolverLayerProxy::non_null_ptr_type &topological_boundary_resolver_layer_proxy)` | method | `void` | public | Remove a 'cross section' topological boundary resolver layer proxy. |
| `add_cross_section_topological_network_resolver_layer_proxy( const TopologyNetworkResolverLayerProxy::non_null_ptr_type &topological_network_resolver_layer_proxy)` | method | `void` | public | Add a 'cross section' topological network resolver layer proxy. |
| `remove_cross_section_topological_network_resolver_layer_proxy( const TopologyNetworkResolverLayerProxy::non_null_ptr_type &topological_network_resolver_layer_proxy)` | method | `void` | public | Remove a 'cross section' topological network resolver layer proxy. |
| `add_surface_polygons_mask_reconstructed_geometries_layer_proxy( const ReconstructLayerProxy::non_null_ptr_type &reconstructed_geometries_layer_proxy)` | method | `void` | public | Add a 'surface polygons mask' reconstructed static geometries layer proxy. |
| `remove_surface_polygons_mask_reconstructed_geometries_layer_proxy( const ReconstructLayerProxy::non_null_ptr_type &reconstructed_geometries_layer_proxy)` | method | `void` | public | Remove a 'surface polygons mask' reconstructed static geometries layer proxy. |
| `add_surface_polygons_mask_topological_boundary_resolver_layer_proxy( const TopologyGeometryResolverLayerProxy::non_null_ptr_type &topological_boundary_resolver_layer_proxy)` | method | `void` | public | Add a 'surface polygons mask' topological boundary resolver layer proxy. |
| `remove_surface_polygons_mask_topological_boundary_resolver_layer_proxy( const TopologyGeometryResolverLayerProxy::non_null_ptr_type &topological_boundary_resolver_layer_proxy)` | method | `void` | public | Remove a 'surface polygons mask' topological boundary resolver layer proxy. |
| `add_surface_polygons_mask_topological_network_resolver_layer_proxy( const TopologyNetworkResolverLayerProxy::non_null_ptr_type &topological_network_resolver_layer_proxy)` | method | `void` | public | Add a 'surface polygons mask' topological network resolver layer proxy. |
| `remove_surface_polygons_mask_topological_network_resolver_layer_proxy( const TopologyNetworkResolverLayerProxy::non_null_ptr_type &topological_network_resolver_layer_proxy)` | method | `void` | public | Remove a 'surface polygons mask' topological network resolver layer proxy. |
| `ResolvedScalarFieldFeatureProperties` | struct | `None` | private | Potentially time-varying feature properties for the currently resolved scalar field (ie, at the cached reconstruction time). |
| `CrossSections` | struct | `None` | private | The cached cross sections (from other layers). |
| `SurfacePolygonsMask` | struct | `None` | private | The cached surface polygons mask (from other layers). |
| `d_current_scalar_field_feature` | field | `boost::optional<GPlatesModel::FeatureHandle::weak_ref>` | private | The scalar field input feature. |
| `d_current_cross_section_reconstructed_geometry_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<ReconstructLayerProxy>` | private | Used to get cross section geometries from reconstructed feature geometries. |
| `d_current_surface_polygons_mask_reconstructed_geometry_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<ReconstructLayerProxy>` | private | Used to get surface polygon mask geometries from reconstructed feature geometries. |
| `d_current_cross_section_topological_boundary_resolver_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<TopologyGeometryResolverLayerProxy>` | private | Used to get cross section geometries from resolved topological boundaries. |
| `d_current_surface_polygons_mask_topological_boundary_resolver_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<TopologyGeometryResolverLayerProxy>` | private | Used to get surface polygon mask geometries from resolved topological boundaries. |
| `d_current_cross_section_topological_network_resolver_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<TopologyNetworkResolverLayerProxy>` | private | Used to get cross section geometries from resolved topological networks. |
| `d_current_surface_polygons_mask_topological_network_resolver_layer_proxies` | field | `LayerProxyUtils::InputLayerProxySequence<TopologyNetworkResolverLayerProxy>` | private | Used to get surface polygon mask geometries from resolved topological networks. |
| `d_current_reconstruction_time` | field | `double` | private | The current reconstruction time as set by the layer system. |
| `d_cached_resolved_scalar_field_feature_properties` | field | `ResolvedScalarFieldFeatureProperties` | private | Time-varying (potentially) scalar field feature properties. |
| `d_cached_cross_sections` | field | `CrossSections` | private | The cached cross sections (from other layers). |
| `d_cached_surface_polygons_mask` | field | `SurfacePolygonsMask` | private | The cached surface polygons mask (from other layers). |
| `d_subject_token` | field | `GPlatesUtils::SubjectToken` | private | Used to notify polling observers that we've been updated. |
| `d_scalar_field_subject_token` | field | `GPlatesUtils::SubjectToken` | private | The subject token that clients can use to determine if the scalar field itself has changed. |
| `d_scalar_field_feature_subject_token` | field | `GPlatesUtils::SubjectToken` | private | The subject token that clients can use to determine if the scalar field feature has changed. |
| `ScalarField3DLayerProxy()` | constructor | `None` | private | — |
| `invalidate_scalar_field_feature()` | method | `void` | private | — |
| `invalidate_scalar_field()` | method | `void` | private | — |
| `invalidate()` | method | `void` | private | — |
| `resolve_scalar_field_feature( const double &reconstruction_time)` | method | `bool` | private | Attempts to resolve a scalar field. |
| `set_scalar_field_params( const ScalarField3DLayerParams &raster_params)` | method | `void` | private | Sets some scalar field parameters. |
| `check_cross_section_input_layer_proxy( InputLayerProxyWrapperType &input_layer_proxy_wrapper)` | method | `void` | private | Checks if the specified cross section input layer proxy has changed. |
| `check_surface_polygons_mask_input_layer_proxy( InputLayerProxyWrapperType &input_layer_proxy_wrapper)` | method | `void` | private | Checks if the specified surface polygons mask input layer proxy has changed. |
| `check_input_layer_proxies()` | method | `void` | private | Checks if any input layer proxies have changed. |
| `check_cross_section_input_layer_proxies()` | method | `void` | private | — |
| `check_surface_polygons_mask_input_layer_proxies()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_SCALARFIELD3DLAYERPROXY_H` | macro | `None` | — |

## Notes

`get_resolved_scalar_field_3d`, `get_cross_sections` and `get_surface_polygons_mask` all return `boost::none`/`false` rather than throwing when nothing is connected or resolution fails (no scalar field feature, missing required properties, or no geometries from the connected input layers) — callers must treat an empty result as a normal, expected outcome, not an error. `resolve_scalar_field_feature` currently only extracts the scalar field filename, so time-dependence of the resolved field is limited to whatever the reader keyed on that filename supports; the per-time caching machinery is already in place for when more time-varying properties are added.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ScalarField3DLayerTask](ScalarField3DLayerTask.md) | app-logic | 17 |
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 15 |
| [app-logic/ResolvedScalarField3D](ResolvedScalarField3D.md) | app-logic | 7 |
| [presentation/LayerOutputRenderer](../presentation/LayerOutputRenderer.md) | presentation | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ScalarField3DLayerProxy.h
python scripts/gpq.py def GPlatesAppLogic::ScalarField3DLayerProxy --body
python scripts/gpq.py uses ScalarField3DLayerProxy --kind class
python scripts/gpq.py hier ScalarField3DLayerProxy
```

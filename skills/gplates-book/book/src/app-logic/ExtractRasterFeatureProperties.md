# ExtractRasterFeatureProperties

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 455 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ExtractRasterFeatureProperties.h` | C++ | 200 |
| `src/app-logic/ExtractRasterFeatureProperties.cc` | C++ | 373 |

## Overview

`ExtractRasterFeatureProperties` is a `GPlatesModel::ConstFeatureVisitor` that pulls the pieces a raster layer needs out of a raster feature: the `Georeferencing`, the `SpatialReferenceSystem`, the proxied `RawRaster` bands, and the `GpmlRasterBandNames`. Because raster properties can be time-dependent (wrapped in a `GpmlPiecewiseAggregation` of `GpmlTimeWindow`s), the visitor is constructed with a reconstruction time and resolves each property against that instant rather than returning every time slice.

The anonymous `CanResolveRasterFeature` visitor is a separate, lighter-weight check used only to answer "is this a raster feature at all", backing the free functions `is_raster_feature()` and `contains_raster_feature()`. Callers such as `FeatureCollectionFileFormatClassify` use it to classify feature collections without needing a reconstruction time.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::CanResolveRasterFeature`](#anonymouscanresolverasterfeature) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Visits a feature collection and determines whether the feature collection contains any raster features. |
| [`GPlatesAppLogic::ExtractRasterFeatureProperties`](#gplatesapplogicextractrasterfeatureproperties) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Visits a raster feature and extracts the following properties from it: - GmlRectifiedGrid inside a GpmlConstantValue inside a gpml:domainSet top level property. - GmlFile inside a GpmlConstantValue or a GpmlPiecewiseAggregation inside a ... |

## Members

### `(anonymous)::CanResolveRasterFeature`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CanResolveRasterFeature()` | constructor | `None` | public | — |
| `has_raster_feature()` | method | `bool` | public | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | public | — |
| `finalise_post_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | public | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | public | — |
| `visit_gpml_piecewise_aggregation( const GPlatesPropertyValues::GpmlPiecewiseAggregation &gpml_piecewise_aggregation)` | method | `void` | public | — |
| `visit_gml_rectified_grid( const GPlatesPropertyValues::GmlRectifiedGrid &gml_rectified_grid)` | method | `void` | public | — |
| `visit_gml_file( const GPlatesPropertyValues::GmlFile &gml_file)` | method | `void` | public | — |
| `visit_gpml_raster_band_names( const GPlatesPropertyValues::GpmlRasterBandNames &gpml_raster_band_names)` | method | `void` | public | — |
| `d_seen_gml_rectified_grid` | field | `bool` | private | — |
| `d_seen_gml_file` | field | `bool` | private | — |
| `d_seen_at_least_one_valid_proxied_raw_raster` | field | `bool` | private | — |
| `d_seen_gpml_raster_band_names` | field | `bool` | private | — |
| `d_inside_constant_value` | field | `bool` | private | — |
| `d_inside_piecewise_aggregation` | field | `bool` | private | — |
| `d_has_raster_feature` | field | `bool` | private | — |

### `GPlatesAppLogic::ExtractRasterFeatureProperties`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ExtractRasterFeatureProperties( const double &reconstruction_time = 0)` | constructor | `None` | public | — |
| `get_georeferencing` | field | `boost::optional<GPlatesPropertyValues::Georeferencing::non_null_ptr_to_const_type>` | public | — |
| `get_spatial_reference_system` | field | `boost::optional<GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type>` | public | FIXME: Currently this is extracted from the (possibly time-dependent) raster at the reconstruction time passed into constructor. |
| `get_proxied_rasters` | field | `boost::optional<std::vector<GPlatesPropertyValues::RawRaster::non_null_ptr_type> >` | public | — |
| `get_raster_band_names` | field | `boost::optional<GPlatesPropertyValues::GpmlRasterBandNames::band_names_list_type>` | public | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | public | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | public | — |
| `visit_gpml_piecewise_aggregation( const GPlatesPropertyValues::GpmlPiecewiseAggregation &gpml_piecewise_aggregation)` | method | `void` | public | — |
| `visit_gml_rectified_grid( const GPlatesPropertyValues::GmlRectifiedGrid &gml_rectified_grid)` | method | `void` | public | — |
| `visit_gml_file( const GPlatesPropertyValues::GmlFile &gml_file)` | method | `void` | public | — |
| `visit_gpml_raster_band_names( const GPlatesPropertyValues::GpmlRasterBandNames &gpml_raster_band_names)` | method | `void` | public | — |
| `d_reconstruction_time` | field | `GPlatesPropertyValues::GeoTimeInstant` | private | The reconstruction time at which properties are extracted. |
| `d_georeferencing` | field | `boost::optional<GPlatesPropertyValues::Georeferencing::non_null_ptr_to_const_type>` | private | The georeferencing for the raster - currently treated as a constant value over time. |
| `d_spatial_reference_system` | field | `boost::optional<GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type>` | private | The raster's spatial reference system. |
| `d_proxied_rasters` | field | `boost::optional<std::vector<GPlatesPropertyValues::RawRaster::non_null_ptr_type> >` | private | The proxied rasters of the first GmlFile encountered. |
| `d_raster_band_names` | field | `boost::optional<GPlatesPropertyValues::GpmlRasterBandNames::band_names_list_type>` | private | The list of band names - one for each proxied raster. |
| `d_inside_constant_value` | field | `bool` | private | — |
| `d_inside_piecewise_aggregation` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_EXTRACTRASTERFEATUREPROPERTIES_H` | macro | `None` | — |
| `is_raster_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `bool` | Returns true if the specified feature is a raster feature. |
| `contains_raster_feature( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection)` | function | `bool` | Returns true if the specified feature collection contains a raster feature. |
| `find_raster_band_name( const GPlatesPropertyValues::GpmlRasterBandNames::band_names_list_type &band_names_list, const GPlatesPropertyValues::TextContent &band_name)` | function | `boost::optional<std::size_t>` | Returns the index of band\_name inside band\_names\_list if present. |

## Notes

- `ExtractRasterFeatureProperties::visit_gpml_piecewise_aggregation()` only descends into the `GpmlTimeWindow` whose `valid_time` contains `d_reconstruction_time`, so one instance extracts a single time slice; a different reconstruction time needs a new instance. `CanResolveRasterFeature`, by contrast, visits every time window regardless of `valid_time` — it treats "is a raster feature" as a property of the whole feature, not of one instant.
- Only the first `GmlFile` encountered contributes to `get_proxied_rasters()`; later matches at the same instant are ignored, since the auto-generated raster colour palette is built from the first frame of a time-dependent sequence.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/RasterLayerProxy](RasterLayerProxy.md) | app-logic | 40 |
| [app-logic/RasterLayerParams](RasterLayerParams.md) | app-logic | 18 |
| [app-logic/RasterLayerTask](RasterLayerTask.md) | app-logic | 17 |
| [presentation/RasterVisualLayerParams](../presentation/RasterVisualLayerParams.md) | presentation | 5 |
| [file-io/FeatureCollectionFileFormatClassify](../file-io/FeatureCollectionFileFormatClassify.md) | file-io | 2 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 2 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ExtractRasterFeatureProperties.h
python scripts/gpq.py def (anonymous)::CanResolveRasterFeature --body
python scripts/gpq.py uses CanResolveRasterFeature --kind class
python scripts/gpq.py hier CanResolveRasterFeature
```

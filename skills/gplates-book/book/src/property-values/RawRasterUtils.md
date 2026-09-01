# RawRasterUtils

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 134 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/RawRasterUtils.h` | C++ | 790 |
| `src/property-values/RawRasterUtils.cc` | C++ | 413 |

## Overview

[[[PROSE overview unit=property-values/RawRasterUtils tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::RawRasterSizeVisitorImpl`](#anonymousrawrastersizevisitorimpl) | class | — | — | 0 | — |
| [`(anonymous)::RawRasterSizeVisitor`](#anonymousrawrastersizevisitor) | typedef | — | — | 0 | This is a visitor that pulls out the size from a RawRaster. |
| [`(anonymous)::RawRasterStatisticsVisitorImpl`](#anonymousrawrasterstatisticsvisitorimpl) | class | — | — | 0 | — |
| [`(anonymous)::RawRasterStatisticsVisitor`](#anonymousrawrasterstatisticsvisitor) | typedef | — | — | 0 | This is a visitor that pulls out statistics from a RawRaster. |
| [`(anonymous)::RawRasterNoDataValueVisitorImpl`](#anonymousrawrasternodatavaluevisitorimpl) | class | — | — | 0 | — |
| [`(anonymous)::RawRasterNoDataValueVisitor`](#anonymousrawrasternodatavaluevisitor) | typedef | — | — | 0 | This is a visitor that pulls out the no-data value from a RawRaster. |
| [`(anonymous)::RawRasterHasDataVisitorImpl`](#anonymousrawrasterhasdatavisitorimpl) | class | — | — | 0 | — |
| [`(anonymous)::RawRasterHasDataVisitor`](#anonymousrawrasterhasdatavisitor) | typedef | — | — | 0 | This is a visitor that determines whether a raster has data / proxied data. |
| [`(anonymous)::RawRasterTypeInfoVisitorImpl`](#anonymousrawrastertypeinfovisitorimpl) | class | — | — | 0 | — |
| [`(anonymous)::RawRasterTypeInfoVisitor`](#anonymousrawrastertypeinfovisitor) | typedef | — | — | 0 | This is a visitor that extracts the data type of a raster as an enumerated value. |
| [`GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::RawRasterCastVisitor`](#gplatespropertyvaluesrawrasterutilsrawrasterutilsinternalsrawrastercastvisitor) | class | [`RawRasterVisitor`](RawRaster.md) | `<class TargetRawRasterType>` | 0 | A visitor that returns a pointer to the raster if its derived type is TargetRawRasterType. |
| [`GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::IntegerToFloat`](#gplatespropertyvaluesrawrasterutilsrawrasterutilsinternalsintegertofloat) | class | — | `<typename IntType, typename FloatType>` | 0 | Helper class to support convert\_integer\_raster\_to\_float\_raster. |
| [`GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::RawRasterTraits<RawRasterImpl< T, RawRasterDataPolicies::WithProxiedData, StatisticsPolicy, NoDataValuePolicy> >`](#gplatespropertyvaluesrawrasterutilsrawrasterutilsinternalsrawrastertraitsrawrasterimpl-t-rawrasterdatapolicieswithproxieddata-statisticspolicy-nodatavaluepolicy-) | struct | — | `< typename T, class StatisticsPolicy, template <class> class NoDataValuePolicy >` | 0 | — |
| [`GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::CreateCoverageRawRaster`](#gplatespropertyvaluesrawrasterutilsrawrasterutilsinternalscreatecoveragerawraster) | class | — | `<class RawRasterType, bool has_no_data_value>` | 0 | Creates a coverage raster from a raster. |
| [`GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::CreateCoverageRawRaster<RawRasterType, true>`](#gplatespropertyvaluesrawrasterutilsrawrasterutilsinternalscreatecoveragerawrasterrawrastertype-true) | class | — | `<class RawRasterType>` | 0 | — |
| [`GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::DoesRasterContainANoDataValue`](#gplatespropertyvaluesrawrasterutilsrawrasterutilsinternalsdoesrastercontainanodatavalue) | class | — | `<class RawRasterType, bool has_no_data_value>` | 0 | Determines if a raster has a no-data value and is not fully opaque. |
| [`GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::DoesRasterContainANoDataValue<RawRasterType, true/*has_no_data_value*/>`](#gplatespropertyvaluesrawrasterutilsrawrasterutilsinternalsdoesrastercontainanodatavaluerawrastertype-truehas_no_data_value) | class | — | `<class RawRasterType>` | 0 | — |
| [`GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::AddNoDataValue`](#gplatespropertyvaluesrawrasterutilsrawrasterutilsinternalsaddnodatavalue) | struct | — | `<class RawRasterType>` | 0 | Adds a no-data value to a raster - also converts no-data pixel values (in raster data) from the value used to load the raster data to the value expected by the raster type. |
| [`GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::AddNoDataValue< RawRasterImpl<T, DataPolicy, StatisticsPolicy, RawRasterNoDataValuePolicies::WithNoDataValue> >`](#gplatespropertyvaluesrawrasterutilsrawrasterutilsinternalsaddnodatavalue-rawrasterimplt-datapolicy-statisticspolicy-rawrasternodatavaluepolicieswithnodatavalue-) | struct | — | `<typename T, template <class> class DataPolicy, class StatisticsPolicy>` | 0 | Specialisation for rasters that have a no-data value that can be set. |
| [`GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::AddNoDataValue< RawRasterImpl<T, RawRasterDataPolicies::WithData, StatisticsPolicy, RawRasterNoDataValuePolicies::WithNoDataValue> >`](#gplatespropertyvaluesrawrasterutilsrawrasterutilsinternalsaddnodatavalue-rawrasterimplt-rawrasterdatapolicieswithdata-statisticspolicy-rawrasternodatavaluepolicieswithnodatavalue-) | struct | — | `<typename T, class StatisticsPolicy>` | 0 | Specialisation for rasters that have a no-data value that can be set \*and\* have data. |
| [`GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::AddNoDataValue< RawRasterImpl<T, RawRasterDataPolicies::WithData, StatisticsPolicy, RawRasterNoDataValuePolicies::NanNoDataValue> >`](#gplatespropertyvaluesrawrasterutilsrawrasterutilsinternalsaddnodatavalue-rawrasterimplt-rawrasterdatapolicieswithdata-statisticspolicy-rawrasternodatavaluepoliciesnannodatavalue-) | struct | — | `<typename T, class StatisticsPolicy>` | 0 | Specialisation for rasters that have data and always use NaN as no-data value. |
| [`GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::AddRasterStatistics`](#gplatespropertyvaluesrawrasterutilsrawrasterutilsinternalsaddrasterstatistics) | struct | — | `<class RawRasterType>` | 0 | Adds statistics to a raster. |
| [`GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::AddRasterStatistics< RawRasterImpl<T, DataPolicy, RawRasterStatisticsPolicies::WithStatistics, NoDataValuePolicy> >`](#gplatespropertyvaluesrawrasterutilsrawrasterutilsinternalsaddrasterstatistics-rawrasterimplt-datapolicy-rawrasterstatisticspolicieswithstatistics-nodatavaluepolicy-) | struct | — | `<typename T, template <class> class DataPolicy, template <class> class NoDataValuePolicy>` | 0 | Specialisation for rasters that have raster statistics. |
| [`GPlatesPropertyValues::RawRasterUtils::ConvertProxiedRasterToUnproxiedRaster`](#gplatespropertyvaluesrawrasterutilsconvertproxiedrastertounproxiedraster) | struct | — | `<class ProxiedRawRasterType>` | 0 | Given a proxied raw raster type converts to the equivalent unproxied raw raster type. |

## Members

### `(anonymous)::RawRasterSizeVisitorImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ExtractRasterSize` | class | `None` | private | — |
| `ExtractRasterSize<RawRasterType, true>` | class | `None` | private | — |
| `do_visit( RawRasterType &raster)` | method | `void` | private | — |
| `d_raster_size` | field | `boost::optional<std::pair<unsigned int, unsigned int> >` | private | — |

### `(anonymous)::RawRasterSizeVisitor`

*None.*

### `(anonymous)::RawRasterStatisticsVisitorImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RawRasterStatisticsVisitorImpl()` | constructor | `None` | public | — |
| `get_raster_statistics()` | method | `RasterStatistics` | public | — |
| `do_visit( RawRasterStatisticsPolicies::WithStatistics &with_statistics)` | method | `void` | private | — |
| `do_visit( RawRasterStatisticsPolicies::WithoutStatistics &without_statistics)` | method | `void` | private | — |
| `d_raster_statistics` | field | `RasterStatistics` | private | — |

### `(anonymous)::RawRasterStatisticsVisitor`

*None.*

### `(anonymous)::RawRasterNoDataValueVisitorImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_no_data_value()` | method | `boost::optional<double>` | public | — |
| `do_visit( RawRasterNoDataValuePolicies::WithNoDataValue<T> &with_no_data_value)` | method | `void` | private | — |
| `do_visit( RawRasterNoDataValuePolicies::NanNoDataValue<T> &nan_no_data_value)` | method | `void` | private | — |
| `do_visit( RawRasterNoDataValuePolicies::WithoutNoDataValue<T> &without_no_data_value)` | method | `void` | private | — |
| `d_no_data_value` | field | `boost::optional<double>` | private | — |

### `(anonymous)::RawRasterNoDataValueVisitor`

*None.*

### `(anonymous)::RawRasterHasDataVisitorImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RawRasterHasDataVisitorImpl()` | constructor | `None` | public | — |
| `has_data()` | method | `bool` | public | — |
| `has_proxied_data()` | method | `bool` | public | — |
| `do_visit( RawRasterType &)` | method | `void` | private | — |
| `d_has_data` | field | `bool` | private | — |
| `d_has_proxied_data` | field | `bool` | private | — |

### `(anonymous)::RawRasterHasDataVisitor`

*None.*

### `(anonymous)::RawRasterTypeInfoVisitorImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RawRasterTypeInfoVisitorImpl()` | constructor | `None` | public | — |
| `get_type()` | method | `RasterType::Type` | public | — |
| `do_visit( RawRasterType &raster)` | method | `void` | private | — |
| `d_type` | field | `RasterType::Type` | private | — |

### `(anonymous)::RawRasterTypeInfoVisitor`

*None.*

### `GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::RawRasterCastVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `raster_ptr_type` | typedef | `typename TargetRawRasterType::non_null_ptr_type` | public | — |
| `visit( TargetRawRasterType &raster)` | method | `void` | public | — |
| `raster_ptr()` | method | `boost::optional<raster_ptr_type>` | public | — |
| `d_raster_ptr` | field | `boost::optional<raster_ptr_type>` | private | — |

### `GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::IntegerToFloat`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `IntegerToFloat( boost::function<bool (IntType)> is_no_data_value)` | constructor | `None` | public | — |
| `operator()( IntType value)` | operator | `FloatType` | public | — |
| `d_is_no_data_value` | field | `boost::function<bool (IntType)>` | private | — |

### `GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::RawRasterTraits<RawRasterImpl< T, RawRasterDataPolicies::WithProxiedData, StatisticsPolicy, NoDataValuePolicy> >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `with_data_type` | typedef | `RawRasterImpl < T, RawRasterDataPolicies::WithData, StatisticsPolicy, NoDataValuePolicy >` | public | Basically, it takes uses the same element\_type, statistics and no data value policies as ExistingRawRasterType, but swaps out the data policy to be WithData (i.e. not proxied). |
| `with_proxied_data_type` | typedef | `RawRasterImpl < T, RawRasterDataPolicies::WithProxiedData, StatisticsPolicy, NoDataValuePolicy >` | public | — |
| `convert_proxied_raster_to_unproxied_raster( typename with_proxied_data_type::non_null_ptr_type proxied_raster, unsigned int region_width, unsigned int region_height, T *data)` | method | `typename with_data_type::non_null_ptr_type` | public | Converts a proxied raw raster to the unproxied raw raster with the same data type. |

### `GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::CreateCoverageRawRaster`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create_coverage_raster( const RawRasterType &raster)` | method | `boost::optional<CoverageRawRaster::non_null_ptr_type>` | public | — |

### `GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::CreateCoverageRawRaster<RawRasterType, true>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CoverageFunctor` | class | `None` | private | — |
| `create_coverage_raster( const RawRasterType &raster)` | method | `boost::optional<CoverageRawRaster::non_null_ptr_type>` | public | — |

### `GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::DoesRasterContainANoDataValue`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `does_raster_contain_a_no_data_value( const RawRasterType &raster)` | method | `bool` | public | — |

### `GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::DoesRasterContainANoDataValue<RawRasterType, true/*has_no_data_value*/>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `does_raster_contain_a_no_data_value( const RawRasterType &raster)` | method | `bool` | public | — |

### `GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::AddNoDataValue`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `raster_element_type` | typedef | `typename RawRasterType::element_type` | public | — |
| `add_no_data_value( RawRasterType &raster, const raster_element_type &no_data_value)` | method | `void` | public | — |

### `GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::AddNoDataValue< RawRasterImpl<T, DataPolicy, StatisticsPolicy, RawRasterNoDataValuePolicies::WithNoDataValue> >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RawRasterType` | typedef | `RawRasterImpl<T, DataPolicy, StatisticsPolicy, RawRasterNoDataValuePolicies::WithNoDataValue>` | public | — |
| `raster_element_type` | typedef | `typename RawRasterType::element_type` | public | — |
| `add_no_data_value( RawRasterType &raster, const raster_element_type &no_data_value)` | method | `void` | public | — |

### `GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::AddNoDataValue< RawRasterImpl<T, RawRasterDataPolicies::WithData, StatisticsPolicy, RawRasterNoDataValuePolicies::WithNoDataValue> >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RawRasterType` | typedef | `RawRasterImpl<T, RawRasterDataPolicies::WithData, StatisticsPolicy, RawRasterNoDataValuePolicies::WithNoDataValue>` | public | — |
| `raster_element_type` | typedef | `typename RawRasterType::element_type` | public | — |
| `add_no_data_value( RawRasterType &raster, const raster_element_type &no_data_value)` | method | `void` | public | — |

### `GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::AddNoDataValue< RawRasterImpl<T, RawRasterDataPolicies::WithData, StatisticsPolicy, RawRasterNoDataValuePolicies::NanNoDataValue> >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RawRasterType` | typedef | `RawRasterImpl<T, RawRasterDataPolicies::WithData, StatisticsPolicy, RawRasterNoDataValuePolicies::NanNoDataValue>` | public | — |
| `raster_element_type` | typedef | `typename RawRasterType::element_type` | public | — |
| `add_no_data_value( RawRasterType &raster, const raster_element_type &no_data_value)` | method | `void` | public | — |

### `GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::AddRasterStatistics`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `add_raster_statistics( RawRasterType &raster, const RasterStatistics &raster_statistics)` | method | `void` | public | — |

### `GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::AddRasterStatistics< RawRasterImpl<T, DataPolicy, RawRasterStatisticsPolicies::WithStatistics, NoDataValuePolicy> >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RawRasterType` | typedef | `RawRasterImpl<T, DataPolicy, RawRasterStatisticsPolicies::WithStatistics, NoDataValuePolicy>` | public | — |
| `raster_element_type` | typedef | `typename RawRasterType::element_type` | public | — |
| `add_raster_statistics( RawRasterType &raster, const RasterStatistics &raster_statistics)` | method | `void` | public | — |

### `GPlatesPropertyValues::RawRasterUtils::ConvertProxiedRasterToUnproxiedRaster`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `unproxied_raster_type` | typedef | `typename RawRasterUtilsInternals::RawRasterTraits<ProxiedRawRasterType> ::with_data_type` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_RAWRASTERUTILS_H` | macro | `None` | — |
| `always_false( T value)` | function | `bool` | A dummy function for use by get\_is\_no\_data\_value\_function. |
| `get_raster_size( RawRaster &raster)` | function | `boost::optional<std::pair<unsigned int, unsigned int> >` | Gets the size (width and height) of the raster. |
| `get_raster_statistics( RawRaster &raster)` | function | `RasterStatistics` | Gets a pointer to the RasterStatistics instance inside raster. |
| `try_raster_cast( RawRaster &raster)` | function | `boost::optional<typename TargetRawRasterType::non_null_ptr_type>` | Returns a pointer to a TargetRawRasterType if the raster is indeed of that derived type. |
| `try_rgba8_raster_cast( RawRaster &raster)` | function | `boost::optional<Rgba8RawRaster::non_null_ptr_type>` | Returns a pointer to a Rgba8RawRaster if raster is indeed a Rgba8RawRaster. |
| `try_proxied_rgba8_raster_cast( RawRaster &raster)` | function | `boost::optional<ProxiedRgba8RawRaster::non_null_ptr_type>` | Returns a pointer to a ProxiedRgba8RawRaster if raster is indeed a ProxiedRgba8RawRaster. |
| `get_no_data_value( RawRaster &raster)` | function | `boost::optional<double>` | Returns the no-data value for raster, if available. |
| `get_is_no_data_value_function( const RawRasterType &raster, typename boost::enable_if_c<RawRasterType::has_no_data_value>::type *dummy = NULL)` | function | `boost::function<bool (typename RawRasterType::element_type)>` | Returns a function that takes one argument and returns a boolean value indicating whether that argument is the no-data value of raster. |
| `get_is_no_data_value_function( const RawRasterType &raster, typename boost::enable_if_c<!RawRasterType::has_no_data_value>::type *dummy = NULL)` | function | `boost::function<bool (typename RawRasterType::element_type)>` | This overload is called if RawRasterType does not have a no-data value. |
| `has_data( RawRaster &raster)` | function | `bool` | Returns whether the raster has data. |
| `has_proxied_data( RawRaster &raster)` | function | `bool` | Returns whether the raster has proxied data. |
| `get_raster_type( RawRaster &raster)` | function | `RasterType::Type` | Returns the data type of the raster as an enumerated value. |
| `does_raster_contain_numerical_data( RawRaster &raster)` | function | `bool` | Returns true if the specified raster contains numerical data such as floating-point or integer pixels (but not RGBA colour pixels). |
| `does_raster_contain_colour_data( RawRaster &raster)` | function | `bool` | Returns true if the specified raster contains colour data such as RGBA pixel (but not numerical data such as floating-point or integer pixels). |
| `convert_integer_raster_to_float_raster( const FromRawRasterType &source_raster)` | function | `typename ToRawRasterType::non_null_ptr_type` | Converts the integer source\_raster into a floating-point raw raster. |
| `create_coverage_raster( const RawRasterType &raster)` | function | `boost::optional<CoverageRawRaster::non_null_ptr_type>` | Returns true if the specified raster has a no-data sentinel value in the raster. |
| `apply_coverage_raster( const Rgba8RawRaster::non_null_ptr_type &source_raster, const CoverageRawRaster::non_null_ptr_type &coverage_raster)` | function | `void` | Applies a coverage raster to an RGBA raster, in place. |
| `has_fully_transparent_pixels( const Rgba8RawRaster::non_null_ptr_type &raster)` | function | `bool` | Returns true if raster has any pixels with an alpha value of 255. |
| `does_raster_contain_a_no_data_value( const RawRasterType &raster)` | function | `bool` | Returns true if the specified raster has a no-data sentinel value in the raster. |
| `add_no_data_value( RawRasterType &raster, const typename RawRasterType::element_type &no_data_value)` | function | `void` | Adds a no-data value to a raster - also converts no-data pixel values (in raster data) from the value used to load the raster data to the value expected by the raster type (this applies to floating-point raster types - they always have NaN ... |
| `add_raster_statistics( RawRasterType &raster, const RasterStatistics &raster_statistics)` | function | `void` | Adds raster statistics to a raster. |
| `convert_proxied_raster_to_unproxied_raster( typename ProxiedRawRasterType::non_null_ptr_type proxied_raw_raster, unsigned int width, unsigned int height, typename ProxiedRawRasterType::element_type *data)` | function | `typename ConvertProxiedRasterToUnproxiedRaster<ProxiedRawRasterType> ::unproxied_raster_type::non_null_ptr_type` | Takes data of specified dimensions and returns it in an unproxied raster of the same element type. |

## Notes

[[[PROSE notes unit=property-values/RawRasterUtils tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Mipmapper](../gui/Mipmapper.md) | gui | 74 |
| [file-io/GdalRasterReader](../file-io/GdalRasterReader.md) | file-io | 46 |
| [opengl/GLNormalMapSource](../opengl/GLNormalMapSource.md) | opengl | 27 |
| [opengl/GLDataRasterSource](../opengl/GLDataRasterSource.md) | opengl | 23 |
| [property-values/ProxiedRasterResolver](ProxiedRasterResolver.md) | property-values | 23 |
| [file-io/GdalRasterWriter](../file-io/GdalRasterWriter.md) | file-io | 21 |
| [opengl/GLScalarFieldDepthLayersSource](../opengl/GLScalarFieldDepthLayersSource.md) | opengl | 21 |
| [file-io/MipmappedRasterFormatWriter](../file-io/MipmappedRasterFormatWriter.md) | file-io | 20 |
| [qt-widgets/RasterPropertiesDialog](../qt-widgets/RasterPropertiesDialog.md) | qt-widgets | 11 |
| [file-io/RasterFileCacheFormatReader](../file-io/RasterFileCacheFormatReader.md) | file-io | 10 |
| [opengl/GLAgeGridMaskSource](../opengl/GLAgeGridMaskSource.md) | opengl | 10 |
| [file-io/MipmappedRasterFormatReader](../file-io/MipmappedRasterFormatReader.md) | file-io | 8 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 7 |
| [file-io/SourceRasterFileCacheFormatReader](../file-io/SourceRasterFileCacheFormatReader.md) | file-io | 5 |
| [opengl/GLVisualRasterSource](../opengl/GLVisualRasterSource.md) | opengl | 5 |
| [app-logic/RasterLayerParams](../app-logic/RasterLayerParams.md) | app-logic | 4 |
| [file-io/RgbaRasterWriter](../file-io/RgbaRasterWriter.md) | file-io | 3 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 3 |
| [app-logic/ExtractRasterFeatureProperties](../app-logic/ExtractRasterFeatureProperties.md) | app-logic | 2 |
| [file-io/RasterFileCache](../file-io/RasterFileCache.md) | file-io | 1 |

*... and 3 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/RawRasterUtils.h
python scripts/gpq.py def GPlatesPropertyValues::RawRasterUtils::RawRasterUtilsInternals::CreateCoverageRawRaster<RawRasterType, true> --body
python scripts/gpq.py uses CreateCoverageRawRaster<RawRasterType, true> --kind class
python scripts/gpq.py hier CreateCoverageRawRaster<RawRasterType, true>
```

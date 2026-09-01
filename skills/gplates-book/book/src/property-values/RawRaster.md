# RawRaster

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 311 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/RawRaster.h` | C++ | 1362 |
| `src/property-values/RawRaster.cc` | C++ | 39 |

## Overview

[[[PROSE overview unit=property-values/RawRaster tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::RawRaster`](#gplatespropertyvaluesrawraster) | class | [`GPlatesUtils::ReferenceCount<RawRaster>`](../utils/ReferenceCount.md) | — | 1 | RawRaster is the abstract base class of classes that encapsulate a raster (a dynamically allocated array of some type) and associated information. |
| [`GPlatesPropertyValues::UninitialisedRawRaster`](#gplatespropertyvaluesuninitialisedrawraster) | typedef | — | — | 0 | A note on types: - The exact-width integer types are said to be optional, but they should be present on all platforms that we're interested in. |
| [`GPlatesPropertyValues::Int8RawRaster`](#gplatespropertyvaluesint8rawraster) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::ProxiedInt8RawRaster`](#gplatespropertyvaluesproxiedint8rawraster) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::UInt8RawRaster`](#gplatespropertyvaluesuint8rawraster) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::ProxiedUInt8RawRaster`](#gplatespropertyvaluesproxieduint8rawraster) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::Int16RawRaster`](#gplatespropertyvaluesint16rawraster) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::ProxiedInt16RawRaster`](#gplatespropertyvaluesproxiedint16rawraster) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::UInt16RawRaster`](#gplatespropertyvaluesuint16rawraster) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::ProxiedUInt16RawRaster`](#gplatespropertyvaluesproxieduint16rawraster) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::Int32RawRaster`](#gplatespropertyvaluesint32rawraster) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::ProxiedInt32RawRaster`](#gplatespropertyvaluesproxiedint32rawraster) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::UInt32RawRaster`](#gplatespropertyvaluesuint32rawraster) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::ProxiedUInt32RawRaster`](#gplatespropertyvaluesproxieduint32rawraster) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::FloatRawRaster`](#gplatespropertyvaluesfloatrawraster) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::ProxiedFloatRawRaster`](#gplatespropertyvaluesproxiedfloatrawraster) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::DoubleRawRaster`](#gplatespropertyvaluesdoublerawraster) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::ProxiedDoubleRawRaster`](#gplatespropertyvaluesproxieddoublerawraster) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::Rgba8RawRaster`](#gplatespropertyvaluesrgba8rawraster) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::ProxiedRgba8RawRaster`](#gplatespropertyvaluesproxiedrgba8rawraster) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::CoverageRawRaster`](#gplatespropertyvaluescoveragerawraster) | typedef | — | — | 0 | A CoverageRawRaster is a raster that can be used to represent the "coverage" at each pixel of a downsampled raster. |
| [`GPlatesPropertyValues::RawRasterStatisticsPolicies::WithStatistics`](#gplatespropertyvaluesrawrasterstatisticspolicieswithstatistics) | class | — | — | 0 | Use WithStatistics if the RawRaster derivation stores statistics. |
| [`GPlatesPropertyValues::RawRasterStatisticsPolicies::WithoutStatistics`](#gplatespropertyvaluesrawrasterstatisticspolicieswithoutstatistics) | class | — | — | 0 | Use WithoutStatistics if the RawRaster derivation does not store statistics. |
| [`GPlatesPropertyValues::RawRasterNoDataValuePolicies::WithNoDataValue`](#gplatespropertyvaluesrawrasternodatavaluepolicieswithnodatavalue) | class | — | `<typename T>` | 0 | Use WithNoDataValue if the RawRaster derivation stores a "no data" value. |
| [`GPlatesPropertyValues::RawRasterNoDataValuePolicies::NanNoDataValue`](#gplatespropertyvaluesrawrasternodatavaluepoliciesnannodatavalue) | class | — | `<typename T>` | 0 | Use NanNoDataValue if the RawRaster derivation uses NaN as a fixed "no data" value. |
| [`GPlatesPropertyValues::RawRasterNoDataValuePolicies::WithoutNoDataValue`](#gplatespropertyvaluesrawrasternodatavaluepolicieswithoutnodatavalue) | class | — | `<typename T>` | 0 | Use WithoutNoDataValue if the RawRaster derivation does not have a "no data" value. |
| [`GPlatesPropertyValues::RawRasterDataPolicies::WithData`](#gplatespropertyvaluesrawrasterdatapolicieswithdata) | class | — | `<typename T>` | 0 | Use WithData if the RawRaster derivation stores a pointer to dynamically allocated memory. |
| [`GPlatesPropertyValues::RawRasterDataPolicies::WithProxiedData`](#gplatespropertyvaluesrawrasterdatapolicieswithproxieddata) | class | — | `<typename T>` | 0 | Use WithProxiedData if the RawRaster derivation stores a reference to a file on disk instead of storing the entire raster data in memory all the time. |
| [`GPlatesPropertyValues::RawRasterDataPolicies::WithoutData`](#gplatespropertyvaluesrawrasterdatapolicieswithoutdata) | class | — | `<typename T>` | 0 | Use WithoutData if the RawRaster derivation does not store a pointer to dynamically allocated memory. |
| [`GPlatesPropertyValues::RawRasterVisitor`](#gplatespropertyvaluesrawrastervisitor) | class | — | — | 3 | RawRasterVisitor is a visitor that visits a RawRaster. |
| [`GPlatesPropertyValues::TemplatedRawRasterVisitor`](#gplatespropertyvaluestemplatedrawrastervisitor) | class | [`RawRasterVisitor`](RawRaster.md)<br>`ImplType` | `<class ImplType>` | 1 | Allows us to write templated visitors to RawRasters. |
| [`GPlatesPropertyValues::RawRasterImpl`](#gplatespropertyvaluesrawrasterimpl) | class | [`RawRaster`](RawRaster.md)<br>`DataPolicy<T>`<br>`StatisticsPolicy`<br>`NoDataValuePolicy<T>` | `< typename T, template <class> class DataPolicy, class StatisticsPolicy, template <class> class NoDataValuePolicy >` | 0 | — |

## Members

### `GPlatesPropertyValues::RawRaster`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<RawRaster>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const RawRaster>` | public | — |
| `~RawRaster()` | destructor | `None` | public | — |
| `accept_visitor( RawRasterVisitor &visitor)` | method | `void` | public | — |

### `GPlatesPropertyValues::UninitialisedRawRaster`

*None.*

### `GPlatesPropertyValues::Int8RawRaster`

*None.*

### `GPlatesPropertyValues::ProxiedInt8RawRaster`

*None.*

### `GPlatesPropertyValues::UInt8RawRaster`

*None.*

### `GPlatesPropertyValues::ProxiedUInt8RawRaster`

*None.*

### `GPlatesPropertyValues::Int16RawRaster`

*None.*

### `GPlatesPropertyValues::ProxiedInt16RawRaster`

*None.*

### `GPlatesPropertyValues::UInt16RawRaster`

*None.*

### `GPlatesPropertyValues::ProxiedUInt16RawRaster`

*None.*

### `GPlatesPropertyValues::Int32RawRaster`

*None.*

### `GPlatesPropertyValues::ProxiedInt32RawRaster`

*None.*

### `GPlatesPropertyValues::UInt32RawRaster`

*None.*

### `GPlatesPropertyValues::ProxiedUInt32RawRaster`

*None.*

### `GPlatesPropertyValues::FloatRawRaster`

*None.*

### `GPlatesPropertyValues::ProxiedFloatRawRaster`

*None.*

### `GPlatesPropertyValues::DoubleRawRaster`

*None.*

### `GPlatesPropertyValues::ProxiedDoubleRawRaster`

*None.*

### `GPlatesPropertyValues::Rgba8RawRaster`

*None.*

### `GPlatesPropertyValues::ProxiedRgba8RawRaster`

*None.*

### `GPlatesPropertyValues::CoverageRawRaster`

*None.*

### `GPlatesPropertyValues::RawRasterStatisticsPolicies::WithStatistics`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `(anonymous enum)` | enum | `None` | public | — |
| `WithStatistics()` | constructor | `None` | public | — |
| `WithStatistics( const RasterStatistics &statistics_)` | constructor | `None` | public | This is intentionally not explicit. |
| `set_statistics( const RasterStatistics &statistics_)` | method | `void` | public | — |
| `~WithStatistics()` | destructor | `None` | protected | — |
| `d_statistics` | field | `RasterStatistics` | private | — |

### `GPlatesPropertyValues::RawRasterStatisticsPolicies::WithoutStatistics`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `(anonymous enum)` | enum | `None` | public | — |
| `~WithoutStatistics()` | destructor | `None` | protected | — |

### `GPlatesPropertyValues::RawRasterNoDataValuePolicies::WithNoDataValue`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `(anonymous enum)` | enum | `None` | public | — |
| `WithNoDataValue()` | constructor | `None` | public | — |
| `WithNoDataValue( const boost::optional<T> &no_data_value_)` | constructor | `None` | public | This is intentionally not explicit. |
| `set_no_data_value( const boost::optional<T> &no_data_value_)` | method | `void` | public | — |
| `is_no_data_value( T value)` | method | `bool` | public | — |
| `~WithNoDataValue()` | destructor | `None` | protected | — |
| `d_no_data_value` | field | `boost::optional<T>` | private | — |

### `GPlatesPropertyValues::RawRasterNoDataValuePolicies::NanNoDataValue`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `(anonymous enum)` | enum | `None` | public | — |
| `is_no_data_value( T value)` | method | `bool` | public | — |
| `~NanNoDataValue()` | destructor | `None` | protected | — |

### `GPlatesPropertyValues::RawRasterNoDataValuePolicies::WithoutNoDataValue`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `(anonymous enum)` | enum | `None` | public | — |
| `~WithoutNoDataValue()` | destructor | `None` | protected | — |

### `GPlatesPropertyValues::RawRasterDataPolicies::WithData`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `(anonymous enum)` | enum | `None` | public | — |
| `WithData( unsigned int width_, unsigned int height_)` | constructor | `None` | public | — |
| `WithData( unsigned int width_, unsigned int height_, T *data_)` | constructor | `None` | public | — |
| `width()` | method | `unsigned int` | public | — |
| `height()` | method | `unsigned int` | public | — |
| `data()` | method | `T` | public | — |
| `~WithData()` | destructor | `None` | protected | — |
| `d_width` | field | `unsigned int` | private | — |
| `d_height` | field | `unsigned int` | private | — |
| `d_data` | field | `boost::scoped_array<T>` | private | — |

### `GPlatesPropertyValues::RawRasterDataPolicies::WithProxiedData`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `(anonymous enum)` | enum | `None` | public | — |
| `WithProxiedData( unsigned int width_, unsigned int height_, const GPlatesFileIO::RasterBandReaderHandle &raster_band_reader_handle)` | constructor | `None` | public | — |
| `width()` | method | `unsigned int` | public | — |
| `height()` | method | `unsigned int` | public | — |
| `~WithProxiedData()` | destructor | `None` | protected | — |
| `d_width` | field | `unsigned int` | private | — |
| `d_height` | field | `unsigned int` | private | — |
| `d_raster_band_reader_handle` | field | `GPlatesFileIO::RasterBandReaderHandle` | private | — |

### `GPlatesPropertyValues::RawRasterDataPolicies::WithoutData`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `(anonymous enum)` | enum | `None` | public | — |
| `~WithoutData()` | destructor | `None` | protected | — |

### `GPlatesPropertyValues::RawRasterVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~RawRasterVisitor()` | destructor | `None` | public | — |
| `visit( UninitialisedRawRaster &raster)` | method | `void` | public | Pure virtual, so that this class is abstract. |
| `visit( Int8RawRaster &raster)` | method | `void` | public | — |
| `visit( ProxiedInt8RawRaster &raster)` | method | `void` | public | — |
| `visit( UInt8RawRaster &raster)` | method | `void` | public | — |
| `visit( ProxiedUInt8RawRaster &raster)` | method | `void` | public | — |
| `visit( Int16RawRaster &raster)` | method | `void` | public | — |
| `visit( ProxiedInt16RawRaster &raster)` | method | `void` | public | — |
| `visit( UInt16RawRaster &raster)` | method | `void` | public | — |
| `visit( ProxiedUInt16RawRaster &raster)` | method | `void` | public | — |
| `visit( Int32RawRaster &raster)` | method | `void` | public | — |
| `visit( ProxiedInt32RawRaster &raster)` | method | `void` | public | — |
| `visit( UInt32RawRaster &raster)` | method | `void` | public | — |
| `visit( ProxiedUInt32RawRaster &raster)` | method | `void` | public | — |
| `visit( FloatRawRaster &raster)` | method | `void` | public | — |
| `visit( ProxiedFloatRawRaster &raster)` | method | `void` | public | — |
| `visit( DoubleRawRaster &raster)` | method | `void` | public | — |
| `visit( ProxiedDoubleRawRaster &raster)` | method | `void` | public | — |
| `visit( Rgba8RawRaster &raster)` | method | `void` | public | — |
| `visit( ProxiedRgba8RawRaster &raster)` | method | `void` | public | — |
| `visit( CoverageRawRaster &raster)` | method | `void` | public | — |

### `GPlatesPropertyValues::TemplatedRawRasterVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TemplatedRawRasterVisitor()` | constructor | `None` | public | — |
| `TemplatedRawRasterVisitor( const Arg1 &arg1)` | constructor | `None` | public | — |
| `TemplatedRawRasterVisitor( const Arg1 &arg1, const Arg2 &arg2)` | constructor | `None` | public | — |
| `TemplatedRawRasterVisitor( const Arg1 &arg1, const Arg2 &arg2, const Arg3 &arg3)` | constructor | `None` | public | — |
| `TemplatedRawRasterVisitor( const Arg1 &arg1, const Arg2 &arg2, const Arg3 &arg3, const Arg4 &arg4)` | constructor | `None` | public | — |
| `TemplatedRawRasterVisitor( const Arg1 &arg1, const Arg2 &arg2, const Arg3 &arg3, const Arg4 &arg4, const Arg5 &arg5)` | constructor | `None` | public | — |
| `TemplatedRawRasterVisitor( const Arg1 &arg1, const Arg2 &arg2, const Arg3 &arg3, const Arg4 &arg4, const Arg5 &arg5, const Arg6 &arg6)` | constructor | `None` | public | — |
| `TemplatedRawRasterVisitor( const Arg1 &arg1, const Arg2 &arg2, const Arg3 &arg3, const Arg4 &arg4, const Arg5 &arg5, const Arg6 &arg6, const Arg7 &arg7)` | constructor | `None` | public | — |
| `TemplatedRawRasterVisitor( const Arg1 &arg1, const Arg2 &arg2, const Arg3 &arg3, const Arg4 &arg4, const Arg5 &arg5, const Arg6 &arg6, const Arg7 &arg7, const Arg8 &arg8)` | constructor | `None` | public | — |
| `TemplatedRawRasterVisitor( const Arg1 &arg1, const Arg2 &arg2, const Arg3 &arg3, const Arg4 &arg4, const Arg5 &arg5, const Arg6 &arg6, const Arg7 &arg7, const Arg8 &arg8, const Arg9 &arg9)` | constructor | `None` | public | — |
| `visit( UninitialisedRawRaster &raster)` | method | `void` | public | — |
| `visit( Int8RawRaster &raster)` | method | `void` | public | — |
| `visit( ProxiedInt8RawRaster &raster)` | method | `void` | public | — |
| `visit( UInt8RawRaster &raster)` | method | `void` | public | — |
| `visit( ProxiedUInt8RawRaster &raster)` | method | `void` | public | — |
| `visit( Int16RawRaster &raster)` | method | `void` | public | — |
| `visit( ProxiedInt16RawRaster &raster)` | method | `void` | public | — |
| `visit( UInt16RawRaster &raster)` | method | `void` | public | — |
| `visit( ProxiedUInt16RawRaster &raster)` | method | `void` | public | — |
| `visit( Int32RawRaster &raster)` | method | `void` | public | — |
| `visit( ProxiedInt32RawRaster &raster)` | method | `void` | public | — |
| `visit( UInt32RawRaster &raster)` | method | `void` | public | — |
| `visit( ProxiedUInt32RawRaster &raster)` | method | `void` | public | — |
| `visit( FloatRawRaster &raster)` | method | `void` | public | — |
| `visit( ProxiedFloatRawRaster &raster)` | method | `void` | public | — |
| `visit( DoubleRawRaster &raster)` | method | `void` | public | — |
| `visit( ProxiedDoubleRawRaster &raster)` | method | `void` | public | — |
| `visit( Rgba8RawRaster &raster)` | method | `void` | public | — |
| `visit( ProxiedRgba8RawRaster &raster)` | method | `void` | public | — |
| `visit( CoverageRawRaster &raster)` | method | `void` | public | — |

### `GPlatesPropertyValues::RawRasterImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `this_type` | typedef | `RawRasterImpl<T, DataPolicy, StatisticsPolicy, NoDataValuePolicy>` | public | — |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<this_type>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const this_type>` | public | — |
| `element_type` | typedef | `T` | public | — |
| `data_policy_base_type` | typedef | `DataPolicy<T>` | public | — |
| `statistics_policy_base_type` | typedef | `StatisticsPolicy` | public | — |
| `no_data_value_policy_base_type` | typedef | `NoDataValuePolicy<T>` | public | — |
| `create()` | method | `non_null_ptr_type` | public | Creates an uninitialised raster with no data. |
| `create( unsigned int width_, unsigned int height_)` | method | `non_null_ptr_type` | public | Creates an uninitialised raster of size width\_ by height\_. |
| `create( unsigned int width_, unsigned int height_, T *data_)` | method | `non_null_ptr_type` | public | Creates a raster that has the given data\_. |
| `create( unsigned int width_, unsigned int height_, const GPlatesFileIO::RasterBandReaderHandle &raster_band_reader_handle_)` | method | `non_null_ptr_type` | public | Creates a proxied raster where the source raster is at source\_filename. |
| `create( unsigned int width_, unsigned int height_, T *data_, const statistics_policy_base_type &statistics_)` | method | `non_null_ptr_type` | public | Creates a raster that has the given data\_ and statistics\_. |
| `create( unsigned int width_, unsigned int height_, const GPlatesFileIO::RasterBandReaderHandle &raster_band_reader_handle_, const statistics_policy_base_type &statistics_)` | method | `non_null_ptr_type` | public | Creates a proxied raster with the given statistics\_, where the source raster is at source\_filename. |
| `create( unsigned int width_, unsigned int height_, T *data_, const no_data_value_policy_base_type &no_data_value_)` | method | `non_null_ptr_type` | public | Creates a raster that has the given data\_ and no\_data\_value\_. |
| `create( unsigned int width_, unsigned int height_, const GPlatesFileIO::RasterBandReaderHandle &raster_band_reader_handle_, const no_data_value_policy_base_type &no_data_value_)` | method | `non_null_ptr_type` | public | Creates a proxied raster that has the given no\_data\_value\_, where the source raster is at source\_filename. |
| `create( unsigned int width_, unsigned int height_, T *data_, const statistics_policy_base_type &statistics_, const no_data_value_policy_base_type &no_data_value_)` | method | `non_null_ptr_type` | public | Creates a raster that has the given data\_, statistics\_ and no\_data\_value\_. |
| `create( unsigned int width_, unsigned int height_, const GPlatesFileIO::RasterBandReaderHandle &raster_band_reader_handle_, const statistics_policy_base_type &statistics_, const no_data_value_policy_base_type &no_data_value_)` | method | `non_null_ptr_type` | public | Creates a proxied raster that has the given statistics\_ and no\_data\_value\_, where the source raster is at source\_filename. |
| `accept_visitor( RawRasterVisitor &visitor)` | method | `void` | public | — |
| `RawRasterImpl()` | constructor | `None` | private | — |
| `RawRasterImpl( unsigned int width_, unsigned int height_)` | constructor | `None` | private | — |
| `RawRasterImpl( unsigned int width_, unsigned int height_, T *data_)` | constructor | `None` | private | — |
| `RawRasterImpl( unsigned int width_, unsigned int height_, const GPlatesFileIO::RasterBandReaderHandle &raster_band_reader_handle_)` | constructor | `None` | private | Proxied data version: |
| `RawRasterImpl( unsigned int width_, unsigned int height_, T *data_, const statistics_policy_base_type &statistics_)` | constructor | `None` | private | — |
| `RawRasterImpl( unsigned int width_, unsigned int height_, const GPlatesFileIO::RasterBandReaderHandle &raster_band_reader_handle_, const statistics_policy_base_type &statistics_)` | constructor | `None` | private | Proxied data version: |
| `RawRasterImpl( unsigned int width_, unsigned int height_, T *data_, const no_data_value_policy_base_type &no_data_value_)` | constructor | `None` | private | — |
| `RawRasterImpl( unsigned int width_, unsigned int height_, const GPlatesFileIO::RasterBandReaderHandle &raster_band_reader_handle_, const no_data_value_policy_base_type &no_data_value_)` | constructor | `None` | private | Proxied data version: |
| `RawRasterImpl( unsigned int width_, unsigned int height_, T *data_, const statistics_policy_base_type &statistics_, const no_data_value_policy_base_type &no_data_value_)` | constructor | `None` | private | — |
| `RawRasterImpl( unsigned int width_, unsigned int height_, const GPlatesFileIO::RasterBandReaderHandle &raster_band_reader_handle_, const statistics_policy_base_type &statistics_, const no_data_value_policy_base_type &no_data_value_)` | constructor | `None` | private | Proxied data version: |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_RAWRASTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/RawRaster tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [property-values/RawRasterUtils](RawRasterUtils.md) | property-values | 182 |
| [gui/Mipmapper](../gui/Mipmapper.md) | gui | 157 |
| [file-io/GdalRasterReader](../file-io/GdalRasterReader.md) | file-io | 62 |
| [opengl/GLDataRasterSource](../opengl/GLDataRasterSource.md) | opengl | 43 |
| [opengl/GLNormalMapSource](../opengl/GLNormalMapSource.md) | opengl | 43 |
| [opengl/GLScalarFieldDepthLayersSource](../opengl/GLScalarFieldDepthLayersSource.md) | opengl | 41 |
| [property-values/ProxiedRasterResolver](ProxiedRasterResolver.md) | property-values | 41 |
| [unit-test/MipmapperTest](../unit-test/MipmapperTest.md) | unit-test | 40 |
| [gui/ColourRawRaster](../gui/ColourRawRaster.md) | gui | 39 |
| [file-io/GdalRasterWriter](../file-io/GdalRasterWriter.md) | file-io | 27 |
| [opengl/GLAgeGridMaskSource](../opengl/GLAgeGridMaskSource.md) | opengl | 17 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 14 |
| [file-io/MipmappedRasterFormatWriter](../file-io/MipmappedRasterFormatWriter.md) | file-io | 14 |
| [file-io/SourceRasterFileCacheFormatReader](../file-io/SourceRasterFileCacheFormatReader.md) | file-io | 11 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 9 |
| [opengl/GLVisualRasterSource](../opengl/GLVisualRasterSource.md) | opengl | 9 |
| [file-io/RgbaRasterWriter](../file-io/RgbaRasterWriter.md) | file-io | 8 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 8 |
| [app-logic/ExtractRasterFeatureProperties](../app-logic/ExtractRasterFeatureProperties.md) | app-logic | 7 |
| [file-io/RasterFileCacheFormatReader](../file-io/RasterFileCacheFormatReader.md) | file-io | 7 |

*... and 19 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/RawRaster.h
python scripts/gpq.py def GPlatesPropertyValues::TemplatedRawRasterVisitor --body
python scripts/gpq.py uses TemplatedRawRasterVisitor --kind class
python scripts/gpq.py hier TemplatedRawRasterVisitor
```

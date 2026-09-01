# ProxiedRasterResolver

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 241 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/ProxiedRasterResolver.h` | C++ | 1051 |
| `src/property-values/ProxiedRasterResolver.cc` | C++ | 119 |

## Overview

`ProxiedRasterResolver` turns a proxied `RawRaster` — one that only records a file path and dimensions until data is actually needed — into real pixel data read from disk, either at native resolution (source raster) or from a mipmap pyramid at a given level. `ProxiedRasterResolver::create()` uses the anonymous `CreateProxiedRasterResolverVisitorImpl` (via `TemplatedRawRasterVisitor`) to dispatch on the raster's concrete element type and build the matching `ProxiedRasterResolverImpl<ProxiedRawRasterType>`; it returns `boost::none` if the given raster has no proxied data to resolve.

`ProxiedRasterResolverInternals::BaseProxiedRasterResolver<ProxiedRawRasterType>` implements the shared machinery: reading level 0 straight from the source file via `RasterBandReaderHandle`, converting it to the mipmap's element type when they differ (integer sources are mipmapped as float), reading levels ≥ 1 from a lazily-created, cached `MipmappedRasterFormatReader`, and colouring regions with a `RasterColourPalette` through `ColourRawRaster`. This "main" mipmap file is shared by RGBA and floating-point rasters and by integer rasters paired with a floating-point palette.

`ProxiedRasterResolverImpl` is partial-specialised on whether the raster's element type is integral. The non-integral specialisation is a thin pass-through to the base. The integral specialisation adds a second, colour-palette-specific mipmap file (via `get_coloured_mipmap_reader()`), because an integer raster combined with an *integer* colour palette needs colours baked into the mipmap itself rather than applied after reading — the base class alone cannot do this correctly, as its own doc comments note. The per-element-type typedefs at the bottom (`Int8ProxiedRasterResolver`, `Rgba8ProxiedRasterResolver`, etc.) are the concrete resolver types client code casts to once it knows a raster's data type via `RawRasterUtils`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::CreateProxiedRasterResolverVisitorImpl`](#anonymouscreateproxiedrasterresolvervisitorimpl) | class | — | — | 0 | — |
| [`(anonymous)::CreateProxiedRasterResolverVisitor`](#anonymouscreateproxiedrasterresolvervisitor) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::ProxiedRasterResolver`](#gplatespropertyvaluesproxiedrasterresolver) | class | [`GPlatesUtils::ReferenceCount<ProxiedRasterResolver>`](../utils/ReferenceCount.md) | — | 3 | ProxiedRasterResolver takes a proxied raw raster and allows you to retrieve actual raster data from disk. |
| [`GPlatesPropertyValues::ProxiedRasterResolverInternals::BaseProxiedRasterResolver`](#gplatespropertyvaluesproxiedrasterresolverinternalsbaseproxiedrasterresolver) | class | [`ProxiedRasterResolver`](ProxiedRasterResolver.md) | `<class ProxiedRawRasterType>` | 2 | BaseProxiedRasterResolver resolves proxied rasters, but only using the "main", not-colour-palette-specific, mipmap file. |
| [`GPlatesPropertyValues::ProxiedRasterResolverImpl<ProxiedRawRasterType, typename boost::enable_if_c<ProxiedRawRasterType::has_proxied_data && !boost::is_integral<typename ProxiedRawRasterType::element_type>::value>::type>`](#gplatespropertyvaluesproxiedrasterresolverimplproxiedrawrastertype-typename-boostenable_if_cproxiedrawrastertypehas_proxied_data--boostis_integraltypename-proxiedrawrastertypeelement_typevaluetype) | class | [`ProxiedRasterResolverInternals::BaseProxiedRasterResolver<ProxiedRawRasterType>`](ProxiedRasterResolver.md) | `<class ProxiedRawRasterType>` | 0 | Specialisation where ProxiedRawRasterType has proxied data that is not integral. |
| [`GPlatesPropertyValues::ProxiedRasterResolverImpl<ProxiedRawRasterType, typename boost::enable_if_c<ProxiedRawRasterType::has_proxied_data && boost::is_integral<typename ProxiedRawRasterType::element_type>::value>::type>`](#gplatespropertyvaluesproxiedrasterresolverimplproxiedrawrastertype-typename-boostenable_if_cproxiedrawrastertypehas_proxied_data--boostis_integraltypename-proxiedrawrastertypeelement_typevaluetype-2) | class | [`ProxiedRasterResolverInternals::BaseProxiedRasterResolver<ProxiedRawRasterType>`](ProxiedRasterResolver.md) | `<class ProxiedRawRasterType>` | 0 | Specialisation where ProxiedRawRasterType has proxied data that is integral. |
| [`GPlatesPropertyValues::Int8ProxiedRasterResolver`](#gplatespropertyvaluesint8proxiedrasterresolver) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::UInt8ProxiedRasterResolver`](#gplatespropertyvaluesuint8proxiedrasterresolver) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::Int16ProxiedRasterResolver`](#gplatespropertyvaluesint16proxiedrasterresolver) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::UInt16ProxiedRasterResolver`](#gplatespropertyvaluesuint16proxiedrasterresolver) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::Int32ProxiedRasterResolver`](#gplatespropertyvaluesint32proxiedrasterresolver) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::UInt32ProxiedRasterResolver`](#gplatespropertyvaluesuint32proxiedrasterresolver) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::FloatProxiedRasterResolver`](#gplatespropertyvaluesfloatproxiedrasterresolver) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::DoubleProxiedRasterResolver`](#gplatespropertyvaluesdoubleproxiedrasterresolver) | typedef | — | — | 0 | — |
| [`GPlatesPropertyValues::Rgba8ProxiedRasterResolver`](#gplatespropertyvaluesrgba8proxiedrasterresolver) | typedef | — | — | 0 | — |

## Members

### `(anonymous)::CreateProxiedRasterResolverVisitorImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `result_type` | typedef | `boost::optional<ProxiedRasterResolver::non_null_ptr_type>` | public | — |
| `get_result()` | method | `result_type` | public | — |
| `Create` | class | `None` | private | — |
| `Create<RawRasterType, true>` | class | `None` | private | — |
| `do_visit( RawRasterType &raster)` | method | `void` | private | — |
| `d_result` | field | `result_type` | private | — |

### `(anonymous)::CreateProxiedRasterResolverVisitor`

*None.*

### `GPlatesPropertyValues::ProxiedRasterResolver`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ProxiedRasterResolver>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ProxiedRasterResolver>` | public | — |
| `~ProxiedRasterResolver()` | destructor | `None` | public | — |
| `create( const RawRaster::non_null_ptr_type &raster)` | method | `boost::optional<non_null_ptr_type>` | public | Creates a ProxiedRasterResolver; the dynamic type is dependent upon the dynamic type of raster. |
| `get_coloured_region_from_level( unsigned int level, unsigned int region_x_offset, unsigned int region_y_offset, unsigned int region_width, unsigned int region_height, const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette = GPlatesGui::RasterColourPalette::create())` | method | `boost::optional<Rgba8RawRaster::non_null_ptr_type>` | public | Returns a region from a mipmap level, coloured using the given colour palette. |
| `get_number_of_levels()` | method | `unsigned int` | public | Returns the number of levels in the mipmap file. |
| `ensure_mipmaps_available( const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette = GPlatesGui::RasterColourPalette::create())` | method | `bool` | public | Checks whether a mipmap file exists, and if not, generates a mipmap file. |
| `get_region_from_level( unsigned int level, unsigned int region_x_offset, unsigned int region_y_offset, unsigned int region_width, unsigned int region_height)` | method | `boost::optional<RawRaster::non_null_ptr_type>` | public | Retrieves a region from a level in the mipmapped raster file, in the data type of the mipmapped raster file (i.e. not coloured into RGBA). |
| `get_coverage_from_level_if_necessary( unsigned int level, unsigned int region_x_offset, unsigned int region_y_offset, unsigned int region_width, unsigned int region_height)` | method | `boost::optional<CoverageRawRaster::non_null_ptr_type>` | public | Retrieves the coverage raster (the raster that specifies, at each pixel, how much of that pixel is not the sentinel value in the source raster) for the given level and the given region. |
| `get_coverage_from_level( unsigned int level, unsigned int region_x_offset, unsigned int region_y_offset, unsigned int region_width, unsigned int region_height)` | method | `boost::optional<CoverageRawRaster::non_null_ptr_type>` | public | Retrieves the coverage raster (the raster that specifies, at each pixel, how much of that pixel is not the sentinel value in the source raster) for the given level and the given region. |
| `get_region_from_source( unsigned int region_x_offset, unsigned int region_y_offset, unsigned int region_width, unsigned int region_height)` | method | `boost::optional<RawRaster::non_null_ptr_type>` | public | Retrieves a region from the source raster, in the data type of the source raster (i.e. not coloured into RGBA). |
| `ProxiedRasterResolver()` | constructor | `None` | protected | — |

### `GPlatesPropertyValues::ProxiedRasterResolverInternals::BaseProxiedRasterResolver`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `source_raster_type` | typedef | `typename RawRasterUtils::ConvertProxiedRasterToUnproxiedRaster<ProxiedRawRasterType> ::unproxied_raster_type` | public | This is the type of raw raster that can be read from the source raster file. |
| `mipmapped_raster_type` | typedef | `typename GPlatesGui::Mipmapper<source_raster_type>::output_raster_type` | public | This is the type of raw raster that can be read from the mipmapped file. |
| `ColourRegionIfNecessary` | struct | `None` | private | Helper struct for get\_coloured\_region\_from\_level() function. |
| `ColourRegionIfNecessary<MipmappedRasterType, /* bool is_rgba8 = */ true>` | struct | `None` | private | — |
| `get_coloured_region_from_level( unsigned int level, unsigned int region_x_offset, unsigned int region_y_offset, unsigned int region_width, unsigned int region_height, const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette = GPlatesGui::RasterColourPalette::create())` | method | `boost::optional<Rgba8RawRaster::non_null_ptr_type>` | public | Implementation of pure virtual function defined in base. |
| `get_number_of_levels()` | method | `unsigned int` | public | Implementation of pure virtual function defined in base. |
| `ensure_mipmaps_available( const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette = GPlatesGui::RasterColourPalette::create())` | method | `bool` | public | Implementation of pure virtual function defined in base. |
| `ConvertLevel0IfNecessary` | struct | `None` | private | Converts level 0 from the raster type stored in the source raster into the raster type stored in the mipmapped raster file. |
| `ConvertLevel0IfNecessary<SourceRasterType, SourceRasterType>` | struct | `None` | private | Template specialisation where SourceRasterType == MipmappedRasterType. |
| `get_region_from_level_as_mipmapped_type( unsigned int level, unsigned int region_x_offset, unsigned int region_y_offset, unsigned int region_width, unsigned int region_height)` | method | `boost::optional<typename mipmapped_raster_type::non_null_ptr_type>` | public | Retrieves a region from a level in the mipmapped raster file, in the data type of the mipmapped raster file (i.e. not coloured into RGBA). |
| `get_region_from_level( unsigned int level, unsigned int region_x_offset, unsigned int region_y_offset, unsigned int region_width, unsigned int region_height)` | method | `boost::optional<RawRaster::non_null_ptr_type>` | public | Implementation of pure virtual function defined in base. |
| `get_coverage_from_level_if_necessary( unsigned int level, unsigned int region_x_offset, unsigned int region_y_offset, unsigned int region_width, unsigned int region_height)` | method | `boost::optional<CoverageRawRaster::non_null_ptr_type>` | public | Implementation of pure virtual function defined in base. |
| `get_coverage_from_level( unsigned int level, unsigned int region_x_offset, unsigned int region_y_offset, unsigned int region_width, unsigned int region_height)` | method | `boost::optional<CoverageRawRaster::non_null_ptr_type>` | public | Implementation of pure virtual function defined in base. |
| `get_region_from_source_as_source_type( unsigned int region_x_offset, unsigned int region_y_offset, unsigned int region_width, unsigned int region_height)` | method | `boost::optional<typename source_raster_type::non_null_ptr_type>` | public | Retrieves a region from the source raster, in the data type of the source raster (i.e. not coloured into RGBA). |
| `get_region_from_source( unsigned int region_x_offset, unsigned int region_y_offset, unsigned int region_width, unsigned int region_height)` | method | `boost::optional<RawRaster::non_null_ptr_type>` | public | Implementation of pure virtual function defined in base. |
| `BaseProxiedRasterResolver( const typename ProxiedRawRasterType::non_null_ptr_type &raster)` | constructor | `None` | protected | — |
| `~BaseProxiedRasterResolver()` | destructor | `None` | protected | — |
| `d_proxied_raw_raster` | field | `typename ProxiedRawRasterType::non_null_ptr_type` | protected | — |
| `get_main_mipmap_reader()` | method | `GPlatesFileIO::MipmappedRasterFormatReader<mipmapped_raster_type>` | private | Returns a pointer to the mipmap reader for the main mipmap file, also ensuring that the mipmap file exists. |
| `d_main_mipmap_reader` | field | `boost::shared_ptr<GPlatesFileIO::MipmappedRasterFormatReader<mipmapped_raster_type> >` | private | Cached so that we don't have to open and close it all the time. |
| `d_error_getting_mipmap_reader` | field | `bool` | private | Prevents repeated attempts to read (or generate) the mipmap file when there's an error. |

### `GPlatesPropertyValues::ProxiedRasterResolverImpl<ProxiedRawRasterType, typename boost::enable_if_c<ProxiedRawRasterType::has_proxied_data && !boost::is_integral<typename ProxiedRawRasterType::element_type>::value>::type>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `this_type` | typedef | `ProxiedRasterResolverImpl<ProxiedRawRasterType>` | public | — |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<this_type>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const this_type>` | public | — |
| `create( const typename ProxiedRawRasterType::non_null_ptr_type &raster)` | method | `non_null_ptr_type` | public | — |
| `base_type` | typedef | `ProxiedRasterResolverInternals::BaseProxiedRasterResolver<ProxiedRawRasterType>` | private | — |
| `ProxiedRasterResolverImpl( const typename ProxiedRawRasterType::non_null_ptr_type &raster)` | method | `None` | private | — |

### `GPlatesPropertyValues::ProxiedRasterResolverImpl<ProxiedRawRasterType, typename boost::enable_if_c<ProxiedRawRasterType::has_proxied_data && boost::is_integral<typename ProxiedRawRasterType::element_type>::value>::type> (2)`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `this_type` | typedef | `ProxiedRasterResolverImpl<ProxiedRawRasterType>` | public | — |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<this_type>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const this_type>` | public | — |
| `create( const typename ProxiedRawRasterType::non_null_ptr_type &raster)` | method | `non_null_ptr_type` | public | — |
| `base_type` | typedef | `ProxiedRasterResolverInternals::BaseProxiedRasterResolver<ProxiedRawRasterType>` | private | — |
| `source_raster_type` | typedef | `typename base_type::source_raster_type` | private | — |
| `get_coloured_region_from_level( unsigned int level, unsigned int region_x_offset, unsigned int region_y_offset, unsigned int region_width, unsigned int region_height, const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette = GPlatesGui::RasterColourPalette::create())` | method | `boost::optional<Rgba8RawRaster::non_null_ptr_type>` | public | — |
| `ensure_mipmaps_available( const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette = GPlatesGui::RasterColourPalette::create())` | method | `bool` | public | — |
| `ProxiedRasterResolverImpl( const typename ProxiedRawRasterType::non_null_ptr_type &raster)` | method | `None` | private | — |
| `get_coloured_mipmap_reader( const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette)` | method | `GPlatesFileIO::MipmappedRasterFormatReader<Rgba8RawRaster>` | private | Returns a pointer to the mipmap reader for the coloured mipmap file for the given colour palette, after checking that the file exists. |
| `d_coloured_mipmap_reader` | field | `boost::shared_ptr<GPlatesFileIO::MipmappedRasterFormatReader<Rgba8RawRaster> >` | private | — |
| `d_colour_palette_id_of_coloured_mipmap_reader` | field | `boost::optional<std::size_t>` | private | — |
| `d_error_getting_mipmap_reader_for_current_colour_palette` | field | `bool` | private | Prevents repeated attempts to read (or generate) the mipmap file when there's an error. |

### `GPlatesPropertyValues::Int8ProxiedRasterResolver`

*None.*

### `GPlatesPropertyValues::UInt8ProxiedRasterResolver`

*None.*

### `GPlatesPropertyValues::Int16ProxiedRasterResolver`

*None.*

### `GPlatesPropertyValues::UInt16ProxiedRasterResolver`

*None.*

### `GPlatesPropertyValues::Int32ProxiedRasterResolver`

*None.*

### `GPlatesPropertyValues::UInt32ProxiedRasterResolver`

*None.*

### `GPlatesPropertyValues::FloatProxiedRasterResolver`

*None.*

### `GPlatesPropertyValues::DoubleProxiedRasterResolver`

*None.*

### `GPlatesPropertyValues::Rgba8ProxiedRasterResolver`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_PROXIEDRASTERRESOLVER_H` | macro | `None` | — |

## Notes

Both `d_error_getting_mipmap_reader` and its coloured-mipmap counterpart latch permanently on the first failure to open or generate a mipmap file, so a resolver never retries an in-process failed mipmap build — the comments explain this is deliberate, since repeated partial builds would slow GPlates down, and callers must surface the failure to the user themselves. The coloured mipmap reader is also invalidated and rebuilt whenever the colour palette's id changes, so switching palettes on the same resolver instance is expected and does not require creating a new resolver.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/RasterReader](../file-io/RasterReader.md) | file-io | 4 |
| [opengl/GLAgeGridMaskSource](../opengl/GLAgeGridMaskSource.md) | opengl | 3 |
| [opengl/GLDataRasterSource](../opengl/GLDataRasterSource.md) | opengl | 3 |
| [opengl/GLNormalMapSource](../opengl/GLNormalMapSource.md) | opengl | 3 |
| [opengl/GLScalarFieldDepthLayersSource](../opengl/GLScalarFieldDepthLayersSource.md) | opengl | 3 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 2 |
| [opengl/GLVisualRasterSource](../opengl/GLVisualRasterSource.md) | opengl | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/ProxiedRasterResolver.h
python scripts/gpq.py def GPlatesPropertyValues::ProxiedRasterResolverInternals::BaseProxiedRasterResolver --body
python scripts/gpq.py uses BaseProxiedRasterResolver --kind class
python scripts/gpq.py hier BaseProxiedRasterResolver
```

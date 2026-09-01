# Mipmapper

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 242 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/Mipmapper.h` | C++ | 1438 |
| `src/gui/Mipmapper.cc` | C++ | 41 |

## Overview

`Mipmapper` builds the mipmap pyramid stored alongside cached rasters (see
`file-io/RasterFileCache`, `file-io/MipmappedRasterFormatWriter`): given a
`RawRasterType`, repeated `generate_next()` calls halve its dimensions (with
one-pixel extension when a dimension is odd) until both are at or below a
threshold, so the renderer can pick an appropriately-sized level instead of
minifying a full-resolution raster every frame. `MipmapperInternals::BasicMipmapper`
is a CRTP-style base supplying the shared public interface
(`generate_next()`, `get_current_mipmap()`, `get_current_coverage()`,
`get_level_infos()`); the primary `Mipmapper` template is declared but never
defined, so only its `boost::enable_if_c` partial specialisations — selected on
`RawRasterType::element_type` and whether the raster has a no-data value — are
ever instantiated. There are three: `rgba8_t` colour rasters, floating-point
rasters with a no-data value, and integral rasters with a no-data value (which
converts to `FloatRawRaster` via `RawRasterUtils::convert_integer_raster_to_float_raster`
and defers to the floating-point specialisation).

The `rgba8_t` specialisation mipmaps in linear colour space rather than on the
raw gamma-corrected bytes: `initialise_linear_rgba_channels()` decodes each
8-bit channel into a separate linear-intensity `FloatRawRaster` (approximating
gamma 2.2 with a cheap square/square-root instead of `pow`, per a comment
calling this a hot path), each `do_generate_next()` averages those, and
`create_gamma_corrected_rgba_raster()` re-encodes back to 8-bit only for the
mipmap that clients actually consume; there is no separate coverage raster
for this specialisation because coverage is carried in the alpha channel. The
floating-point specialisation instead averages pixels weighted by a coverage
raster and a per-pixel "fraction in source raster" value, skipping any input
pixel that is entirely no-data so NaNs never enter the weighted sum, and falls
back to the raster's `no_data_value()` when all four contributing pixels are
no-data. Each specialisation also has a four-way "combine" constructor
(`MipmapperInternals::combine_rasters`) used to stitch up to four sibling
mipmappers' current rasters into one, for building a level that spans a tile
boundary.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::MipmapperInternals::BasicMipmapper`](#gplatesguimipmapperinternalsbasicmipmapper) | class | — | `<class RawRasterType, class MipmapperType>` | 2 | BasicMipmapper contains the basic outlines of a mipmapper. |
| [`GPlatesGui::Mipmapper<RawRasterType, typename boost::enable_if_c<!RawRasterType::has_no_data_value && boost::is_same<typename RawRasterType::element_type, GPlatesGui::rgba8_t>::value>::type >`](#gplatesguimipmapperrawrastertype-typename-boostenable_if_crawrastertypehas_no_data_value--boostis_sametypename-rawrastertypeelement_type-gplatesguirgba8_tvaluetype-) | class | [`MipmapperInternals::BasicMipmapper<RawRasterType, Mipmapper<RawRasterType> >`](Mipmapper.md) | `<class RawRasterType>` | 0 | This specialisation is for rasters that have an element\_type of rgba8\_t and are without a no-data value. |
| [`GPlatesGui::Mipmapper<RawRasterType, typename boost::enable_if_c<RawRasterType::has_no_data_value && boost::is_floating_point<typename RawRasterType::element_type>::value >::type >`](#gplatesguimipmapperrawrastertype-typename-boostenable_if_crawrastertypehas_no_data_value--boostis_floating_pointtypename-rawrastertypeelement_typevalue-type-) | class | [`MipmapperInternals::BasicMipmapper<RawRasterType, Mipmapper<RawRasterType> >`](Mipmapper.md) | `<class RawRasterType>` | 0 | This specialisation is for rasters that have a floating-point element\_type and that have a no-data value. |
| [`GPlatesGui::MipmapperInternals::IgnoreMe`](#gplatesguimipmapperinternalsignoreme) | class | — | — | 0 | MSVC2005 has trouble finding the base class for Mipmapper\<RawRaster\>, where RawRaster is an integer raster (this is the specialisation immediately below this). |
| [`GPlatesGui::Mipmapper<RawRasterType, typename boost::enable_if_c<RawRasterType::has_no_data_value && boost::is_integral<typename RawRasterType::element_type>::value >::type >`](#gplatesguimipmapperrawrastertype-typename-boostenable_if_crawrastertypehas_no_data_value--boostis_integraltypename-rawrastertypeelement_typevalue-type-) | class | `Mipmapper<GPlatesPropertyValues::FloatRawRaster>` | `<class RawRasterType>` | 0 | This specialisation is for rasters that have an integral element\_type and that have a no-data value. |

## Members

### `GPlatesGui::MipmapperInternals::BasicMipmapper`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `output_raster_type` | typedef | `RawRasterType` | public | The type of the raster that is produced as a result of the mipmapping process. |
| `element_type` | typedef | `typename output_raster_type::element_type` | public | The element type of the output raster type. |
| `coverage_element_type` | typedef | `GPlatesPropertyValues::CoverageRawRaster::element_type` | public | The coverage raster element type. |
| `LevelInfo` | struct | `None` | public | Information about each level generated by this mipmapper. |
| `get_level_infos( const unsigned int threshold_size, const unsigned int source_raster_width, const unsigned int source_raster_height, const bool generate_coverage)` | method | `std::vector<LevelInfo>` | public | Returns information for all the mipmap levels in the mipmap pyramid. |
| `generate_next()` | method | `void` | public | Generates the next mipmap in the sequence of mipmaps. |
| `get_current_mipmap()` | method | `typename output_raster_type::non_null_ptr_to_const_type` | public | Returns the current mipmap held by this Mipmapper. |
| `get_current_coverage()` | method | `boost::optional<GPlatesPropertyValues::CoverageRawRaster::non_null_ptr_to_const_type>` | public | Returns the current coverage raster that corresponds to the current mipmap. |
| `BasicMipmapper()` | constructor | `None` | protected | Creates a BasicMipmapper. |
| `~BasicMipmapper()` | destructor | `None` | protected | — |
| `do_generate_next()` | method | `void` | protected | Generate the next mipmap and optionally the coverage mipmap. |
| `d_current_mipmap` | field | `boost::optional<typename output_raster_type::non_null_ptr_to_const_type>` | protected | The raster at the current mipmap level. |
| `d_current_coverage` | field | `boost::optional<GPlatesPropertyValues::CoverageRawRaster::non_null_ptr_to_const_type>` | protected | The coverage raster, if requested, corresponding to the current mipmap. |

### `GPlatesGui::Mipmapper<RawRasterType, typename boost::enable_if_c<!RawRasterType::has_no_data_value && boost::is_same<typename RawRasterType::element_type, GPlatesGui::rgba8_t>::value>::type >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `base_type` | typedef | `MipmapperInternals::BasicMipmapper<RawRasterType, Mipmapper<RawRasterType> >` | private | — |
| `output_raster_type` | typedef | `typename base_type::output_raster_type` | public | — |
| `coverage_element_type` | typedef | `typename base_type::coverage_element_type` | public | — |
| `Mipmapper( const typename RawRasterType::non_null_ptr_to_const_type &source_raster)` | method | `None` | public | MipmapperInternals::BasicMipmapper::BasicMipmapper. |
| `Mipmapper( const Mipmapper &m00, boost::optional<const Mipmapper &> m01, boost::optional<const Mipmapper &> m10, boost::optional<const Mipmapper &> m11)` | method | `None` | public | MipmapperInternals::combine\_mipmappers. |
| `do_generate_next()` | method | `void` | private | — |
| `initialise_linear_rgba_channels( const typename RawRasterType::non_null_ptr_to_const_type &source_raster)` | method | `void` | private | Converts each presumably gamma-corrected R,G,B,A channel of source raster to a linear intensity floating-point raster channel (each channel in a separate float raster). |
| `create_gamma_corrected_rgba_raster()` | method | `typename output_raster_type::non_null_ptr_to_const_type` | private | Gamma-corrects the current linear R,G,B,A float rasters and stores into 8-bit channels - this is the actual mipmap used by our clients. |
| `d_linear_red_raster` | field | `boost::optional<GPlatesPropertyValues::FloatRawRaster::non_null_ptr_to_const_type>` | private | These float rasters store RGBA in linear space (converted from gamma-corrected pixels). |
| `d_linear_green_raster` | field | `boost::optional<GPlatesPropertyValues::FloatRawRaster::non_null_ptr_to_const_type>` | private | — |
| `d_linear_blue_raster` | field | `boost::optional<GPlatesPropertyValues::FloatRawRaster::non_null_ptr_to_const_type>` | private | — |
| `d_linear_alpha_raster` | field | `boost::optional<GPlatesPropertyValues::FloatRawRaster::non_null_ptr_to_const_type>` | private | — |
| `d_fraction_in_source_raster` | field | `GPlatesPropertyValues::CoverageRawRaster::non_null_ptr_to_const_type` | private | For each pixel in the current mipmap, this raster stores the fraction of that pixel that lies within the bounds of the source raster. |

### `GPlatesGui::Mipmapper<RawRasterType, typename boost::enable_if_c<RawRasterType::has_no_data_value && boost::is_floating_point<typename RawRasterType::element_type>::value >::type >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `base_type` | typedef | `MipmapperInternals::BasicMipmapper<RawRasterType, Mipmapper<RawRasterType> >` | private | — |
| `output_raster_type` | typedef | `typename base_type::output_raster_type` | public | — |
| `coverage_element_type` | typedef | `typename base_type::coverage_element_type` | public | — |
| `Mipmapper( const typename RawRasterType::non_null_ptr_to_const_type &source_raster)` | method | `None` | public | MipmapperInternals::BasicMipmapper::BasicMipmapper. |
| `Mipmapper( const Mipmapper &m00, boost::optional<const Mipmapper &> m01, boost::optional<const Mipmapper &> m10, boost::optional<const Mipmapper &> m11)` | method | `None` | public | MipmapperInternals::combine\_mipmappers. |
| `do_generate_next()` | method | `void` | private | — |
| `d_fraction_in_source_raster` | field | `GPlatesPropertyValues::CoverageRawRaster::non_null_ptr_to_const_type` | private | For each pixel in the current mipmap, this raster stores the fraction of that pixel that lies within the bounds of the source raster. |

### `GPlatesGui::MipmapperInternals::IgnoreMe`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `d_mipmapper` | field | `Mipmapper<GPlatesPropertyValues::FloatRawRaster>` | private | — |

### `GPlatesGui::Mipmapper<RawRasterType, typename boost::enable_if_c<RawRasterType::has_no_data_value && boost::is_integral<typename RawRasterType::element_type>::value >::type >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `base_type` | typedef | `Mipmapper<GPlatesPropertyValues::FloatRawRaster>` | private | — |
| `output_raster_type` | typedef | `typename base_type::output_raster_type` | public | — |
| `Mipmapper( const typename RawRasterType::non_null_ptr_to_const_type &source_raster)` | method | `None` | public | MipmapperInternals::BasicMipmapper::BasicMipmapper. |
| `Mipmapper( const Mipmapper &m00, boost::optional<const Mipmapper &> m01, boost::optional<const Mipmapper &> m10, boost::optional<const Mipmapper &> m11)` | method | `None` | public | MipmapperInternals::combine\_mipmappers. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_MIPMAPPER_H` | macro | `None` | — |
| `get_opaque_coverage_raster( unsigned int width, unsigned int height)` | function | `GPlatesPropertyValues::CoverageRawRaster::non_null_ptr_to_const_type` | Returns coverage raster that is fully opaque (all pixels are 1.0). |
| `get_initial_fraction_in_source_raster( unsigned int width, unsigned int height)` | function | `GPlatesPropertyValues::CoverageRawRaster::non_null_ptr_to_const_type` | Returns coverage raster representing initial fractions of pixels in source raster. |
| `extend_raster( const RawRasterType &source_raster, boost::optional<typename RawRasterType::element_type> fill_value = boost::none, // Can only be called if this type of raster has data. typename boost::enable_if_c<RawRasterType::has_data>::type *dummy = 0)` | function | `typename RawRasterType::non_null_ptr_to_const_type` | Extends source\_raster to the right and down by one pixel if its width and height are not multiples of two, respectively. |
| `mipmap_coverage_raster( const CoverageRasterType &coverage_raster, const GPlatesPropertyValues::CoverageRawRaster &fraction_in_source_raster)` | function | `std::pair< // Mipmapped coverage... typename CoverageRasterType::non_null_ptr_to_const_type, // Mipmapped fraction in source raster... GPlatesPropertyValues::CoverageRawRaster::non ...` | Mipmaps the coverage raster coverage\_raster and the raster fraction\_in\_source\_raster containing the fraction of each pixel that lies within the original source raster. |
| `mipmap_main_raster( const RawRasterType &raster, const CoverageRasterType &coverage_raster, const GPlatesPropertyValues::CoverageRawRaster &fraction_in_source_raster, typename boost::enable_if_c<RawRasterType::has_no_data_value>::type *dummy = 0)` | function | `typename RawRasterType::non_null_ptr_to_const_type` | Mipmaps a floating-point raster raster. |
| `combine_rasters( const RawRasterType &raster00, boost::optional<const RawRasterType &> raster01, boost::optional<const RawRasterType &> raster10, boost::optional<const RawRasterType &> raster11)` | function | `typename RawRasterType::non_null_ptr_to_const_type` | Joins up to four rasters into one. \| \| \| \| r00 \| r01\| \| \| \| \| r10 \| r11\| \| \| \| \| r00 \| r01\| \| \| \| \| \| \| r00 \| \| \| \| r10 \| \| \| \| r00 \| \| \| The rasters must join in a non-overlapping manner to fill a rectangular region: - if both 'r01' and ... |

## Notes

- `get_current_mipmap()` asserts (`GPlatesGlobal::Assert`) that `generate_next()`
  has been called at least once; calling it before the first `generate_next()`
  is a programming error, not a recoverable condition.
- The combine constructors assert that every mipmapper passed in has already
  had `do_generate_next()` called — mixing a freshly-constructed mipmapper into
  a combine call is undefined via assertion failure, not a caught error.
- `combine_rasters()` requires its inputs to already tile a rectangle exactly
  (matching widths/heights on shared edges, `r11` present iff both `r01` and
  `r10` are); mismatches trigger a `PreconditionViolationError`.
- The gamma approximation (`x*x` / `sqrt(x)` in place of `pow(x, 2.2)` /
  `pow(x, 1/2.2)`) is an intentional, documented trade of exactness for
  mipmapping throughput — the exact `pow`-based code is left in under `#if 0`.

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/MipmapperTest](../unit-test/MipmapperTest.md) | unit-test | 53 |
| [file-io/MipmappedRasterFormatWriter](../file-io/MipmappedRasterFormatWriter.md) | file-io | 21 |
| [property-values/ProxiedRasterResolver](../property-values/ProxiedRasterResolver.md) | property-values | 12 |
| [file-io/RasterFileCache](../file-io/RasterFileCache.md) | file-io | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/Mipmapper.h
python scripts/gpq.py def GPlatesGui::Mipmapper<RawRasterType,
		typename boost::enable_if_c<!RawRasterType::has_no_data_value &&
		boost::is_same<typename RawRasterType::element_type, GPlatesGui::rgba8_t>::value>::type
	> --body
python scripts/gpq.py uses Mipmapper<RawRasterType,
		typename boost::enable_if_c<!RawRasterType::has_no_data_value &&
		boost::is_same<typename RawRasterType::element_type, GPlatesGui::rgba8_t>::value>::type
	> --kind class
python scripts/gpq.py hier Mipmapper<RawRasterType,
		typename boost::enable_if_c<!RawRasterType::has_no_data_value &&
		boost::is_same<typename RawRasterType::element_type, GPlatesGui::rgba8_t>::value>::type
	>
```

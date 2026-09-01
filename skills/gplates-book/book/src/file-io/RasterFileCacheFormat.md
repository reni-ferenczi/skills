# RasterFileCacheFormat

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 385 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/RasterFileCacheFormat.h` | C++ | 422 |
| `src/file-io/RasterFileCacheFormat.cc` | C++ | 459 |

## Overview

GPlates never reads a large raster directly off disk while painting the globe. Instead it converts each band of each source raster into its own block-encoded binary sidecar file — one file holding the full-resolution band, another holding the downsampled mipmap pyramid — and then serves texture tiles out of those. `RasterFileCacheFormat` is the single header that defines what those sidecar files look like: the `"GPlates\0"` magic number, the format version, the 256×256 block size, the `QDataStream` version used for every read and write, and the `LevelInfo` / `BlockInfo` records that the header of such a file is made of. It declares no reader or writer of its own; it is the shared vocabulary that `GdalRasterReader` and `RgbaRasterReader` (which write the source-level caches), `MipmappedRasterFormatWriter` (which writes the pyramid), and `SourceRasterFileCacheFormatReader`, `MipmappedRasterFormatReader` and `RasterFileCacheFormatReader` (which read them back) all agree on. The file-level Doxygen comment on `RasterFileCacheFormat.h` is the authoritative byte-layout description for both file kinds and is worth reading before changing anything here.

The second half of the unit is the naming and location policy for those sidecar files. `get_writable_mipmap_cache_filename` and `get_writable_source_cache_filename` derive a name from the source raster's own path plus the band number (and, for mipmaps, an optional colour-palette id), and try the source raster's own directory first, falling back to the temporary directory via `TemporaryFileRegistry::make_filename_in_tmp_directory` when the source directory is not writable — so read-only data directories still get caches, they just land in `/tmp` and are cleaned up at exit. `get_existing_*_cache_filename` mirrors that search order for reads. `RasterFileCache` is the client that drives this: it looks for an existing cache, compares modification times against the source raster, and regenerates when the cache is stale, missing, corrupt or carries a version this build cannot read.

The pyramid geometry is defined by two small free functions rather than by any stored metadata. `get_number_of_mipmapped_levels` halves the source dimensions (rounding up, `(w >> 1) + (w & 1)`) until neither exceeds `BLOCK_SIZE`, and `get_mipmap_dimensions` walks the same loop to reach one level; because both derive from the source dimensions alone, a reader can reproduce the writer's level list without trusting the file. `BLOCK_SIZE` is 256 because that is the texture size every OpenGL implementation supports, which is also why the pyramid stops once the largest dimension fits in one block — a raster that small needs no mipmap file at all. `UnsupportedVersion` is the signal raised once the magic number has matched but the version has not: it means "this is our file, from a build we do not understand", and callers treat it as an instruction to delete and rebuild rather than as a hard failure.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::(anonymous)::GetColourPaletteIdVisitor`](#gplatesfileioanonymousgetcolourpaletteidvisitor) | class | `boost::static_visitor<boost::optional<std::size_t> >` | — | 0 | — |
| [`GPlatesFileIO::RasterFileCacheFormat::Type`](#gplatesfileiorasterfilecacheformattype) | enum | — | — | 0 | The type of raster used to store. |
| [`GPlatesFileIO::RasterFileCacheFormat::LevelInfo`](#gplatesfileiorasterfilecacheformatlevelinfo) | struct | — | — | 0 | Information for the size and file location of a level (base or mipmap) of the mipmap pyramid. |
| [`GPlatesFileIO::RasterFileCacheFormat::BlockInfo`](#gplatesfileiorasterfilecacheformatblockinfo) | struct | — | — | 0 | Information for a block of encoded data. |
| [`GPlatesFileIO::RasterFileCacheFormat::BlockInfos`](#gplatesfileiorasterfilecacheformatblockinfos) | class | — | — | 0 | Keeps track of encoded blocks within an image. |
| [`GPlatesFileIO::RasterFileCacheFormat::UnsupportedVersion`](#gplatesfileiorasterfilecacheformatunsupportedversion) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | Thrown when reading a file containing an unrecognised version number. |

## Members

### `GPlatesFileIO::(anonymous)::GetColourPaletteIdVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const GPlatesGui::RasterColourPalette::empty &)` | operator | `boost::optional<std::size_t>` | public | — |
| `operator()( const GPlatesUtils::non_null_intrusive_ptr<ColourPaletteType> &colour_palette)` | operator | `boost::optional<std::size_t>` | public | — |

### `GPlatesFileIO::RasterFileCacheFormat::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RGBA` | enumerator | `None` | — | — |
| `FLOAT` | enumerator | `None` | — | — |
| `DOUBLE` | enumerator | `None` | — | — |
| `UINT8` | enumerator | `None` | — | — |
| `UINT16` | enumerator | `None` | — | — |
| `INT16` | enumerator | `None` | — | — |
| `UINT32` | enumerator | `None` | — | — |
| `INT32` | enumerator | `None` | — | — |
| `NUM_TYPES` | enumerator | `None` | — | — |

### `GPlatesFileIO::RasterFileCacheFormat::LevelInfo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `width` | field | `quint32` | public | — |
| `height` | field | `quint32` | public | — |
| `blocks_file_offset` | field | `quint64` | public | — |
| `num_blocks` | field | `quint32` | public | — |
| `STREAM_SIZE` | field | `unsigned int` | public | Size of sum of individual data members. |

### `GPlatesFileIO::RasterFileCacheFormat::BlockInfo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `x_offset` | field | `quint32` | public | Pixel offsets locating block within the image of the source (or mipmapped) raster. |
| `y_offset` | field | `quint32` | public | Pixel offsets locating block within the image of the source (or mipmapped) raster. |
| `width` | field | `quint32` | public | Most blocks have BLOCK\_SIZE dimensions except those at right and bottom edges of source raster. |
| `height` | field | `quint32` | public | Most blocks have BLOCK\_SIZE dimensions except those at right and bottom edges of source raster. |
| `main_offset` | field | `quint64` | public | Offset within level of encoded data for the source (or mipmapped) raster. |
| `coverage_offset` | field | `quint64` | public | Offset within level of encoded data for the coverage (or mipmapped) raster. |
| `STREAM_SIZE` | field | `unsigned int` | public | Size of sum of individual data members. |

### `GPlatesFileIO::RasterFileCacheFormat::BlockInfos`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `BlockInfos( unsigned int image_width, unsigned int image_height)` | constructor | `None` | public | Constructor allocates \*un-initialised\* BlockInfo structures. |
| `get_num_blocks()` | method | `unsigned int` | public | Returns the number of blocks. |
| `get_block_info` | field | `BlockInfo` | public | Returns specified block. |
| `d_num_blocks_in_x_direction` | field | `unsigned int` | private | — |
| `d_num_blocks_in_y_direction` | field | `unsigned int` | private | — |
| `d_block_infos` | field | `std::vector<BlockInfo>` | private | — |

### `GPlatesFileIO::RasterFileCacheFormat::UnsupportedVersion`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnsupportedVersion( const GPlatesUtils::CallStack::Trace &exception_source, quint32 unrecognised_version)` | constructor | `None` | public | — |
| `unrecognised_version()` | method | `quint32` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_unrecognised_version` | field | `quint32` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `RASTER_FILE_CACHE_EXTENSION` | variable | `QString` | All raster file caches have filenames that end with this. |
| `make_mipmap_filename_in_same_directory( const QString &source_filename, unsigned int band_number, boost::optional<std::size_t> colour_palette_id = boost::none)` | function | `QString` | — |
| `make_mipmap_filename_in_tmp_directory( const QString &source_filename, unsigned int band_number, boost::optional<std::size_t> colour_palette_id = boost::none)` | function | `QString` | — |
| `make_source_filename_in_same_directory( const QString &source_filename, unsigned int band_number)` | function | `QString` | — |
| `make_source_filename_in_tmp_directory( const QString &source_filename, unsigned int band_number)` | function | `QString` | — |
| `get_type_as_enum()` | function | `Type` | — |
| `GPLATES_FILEIO_RASTERFILECACHEFORMAT_H` | macro | `None` | — |
| `MAGIC_NUMBER` | variable | `boost::uint8_t` | The magic number that identifies a file as GPlates. |
| `VERSION_NUMBER` | variable | `boost::uint32_t` | The current version number of the GPlates raster file cache format. |
| `BLOCK_SIZE` | variable | `unsigned int` | The block size is the value is dimension of square blocks of image data, in the raster file cache, containing BLOCK\_SIZE x BLOCK\_SIZE pixels of data. |
| `Q_DATA_STREAM_VERSION` | variable | `int` | The QDataStream serialisation version. |
| `get_number_of_mipmapped_levels( const unsigned int source_raster_width, const unsigned int source_raster_height)` | function | `unsigned int` | Returns the number of mipmapped levels in total needed for a source raster of the specified dimensions. |
| `get_mipmap_dimensions( unsigned int &mipmap_width, unsigned int &mipmap_height, unsigned int mipmap_level, const unsigned int source_raster_width, const unsigned int source_raster_height)` | function | `void` | Returns the mipmap image dimensions for the specified source raster dimensions and mipmap level. |
| `get_writable_mipmap_cache_filename( const QString &source_filename, unsigned int band_number, boost::optional<std::size_t> colour_palette_id = boost::none)` | function | `boost::optional<QString>` | Returns the filename of a file that can be used for writing out a mipmaps file for the given source\_filename. |
| `get_existing_mipmap_cache_filename( const QString &source_filename, unsigned int band_number, boost::optional<std::size_t> colour_palette_id = boost::none)` | function | `boost::optional<QString>` | Returns the filename of an existing mipmap file for the given source\_filename, if any. |
| `get_writable_source_cache_filename( const QString &source_filename, unsigned int band_number)` | function | `boost::optional<QString>` | Returns the filename of a file that can be used for writing out a source raster file cache for the given source\_filename. |
| `get_existing_source_cache_filename( const QString &source_filename, unsigned int band_number)` | function | `boost::optional<QString>` | Returns the filename of an existing source raster file cache for the given source\_filename, if any. |
| `get_colour_palette_id( const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette = GPlatesGui::RasterColourPalette::create())` | function | `boost::optional<std::size_t>` | Gets the colour palette id for the given colour\_palette. |

## Notes

`VERSION_NUMBER` is shared by both file kinds, source-level and mipmap, even though they are separate files with separate layouts. The comment on it is a standing instruction: any breaking change to either layout, or to a block-encoding algorithm, must bump it. Readers cope by testing version sub-ranges — `MipmappedRasterFormatReader` and `SourceRasterFileCacheFormatReaderImpl` both dispatch `version_number == 1` to a `VersionOneReader` and carry a commented-out `>= 3 && <= VERSION_NUMBER` branch as a worked example of how to add a second reader later — so bumping the constant for one file kind does not force any change in the other beyond its accepted range.

Do not persist the value returned by `get_colour_palette_id`: it is `reinterpret_cast<std::size_t>` of the palette object's address, computed by `GetColourPaletteIdVisitor`. It is unique among the palettes alive at that moment and nothing more — it is not stable across runs, and an address freed and reused by a different palette will collide. It exists only to keep concurrently-live palette-specific mipmap files apart within one session. `RasterColourPalette::empty` maps to `boost::none`, which selects the palette-free filename.

`STREAM_SIZE` on `LevelInfo` and `BlockInfo` is deliberately *not* `sizeof` the struct — the comment says so explicitly. It is the sum of the member widths as they appear in the stream, and the struct may be larger because of padding. Header offsets must be computed from `STREAM_SIZE`; using `sizeof` will silently produce files this code cannot read back. In the same spirit the stream is fixed at `Q_DATA_STREAM_VERSION` (`QDataStream::Qt_4_4`) and big-endian, the `QDataStream` default, so caches are portable between platforms; the one portability assumption baked in is that `float` is 32-bit and `double` 64-bit.

`BlockInfos`'s constructor allocates blocks *uninitialised* — the vector is sized from the image dimensions, but the `BlockInfo` values are garbage until a writer fills them or a reader streams them in. Both `get_block_info` overload pairs assert their indices via `GPlatesGlobal::Assert`, and the non-const overloads simply `const_cast` the const result, so the bounds check is never skipped. `get_mipmap_dimensions` calls `GPlatesGlobal::Abort` if the requested level exceeds the pyramid depth rather than returning an error.

The two filename lookups answer different questions and the difference matters. `get_existing_*` checks that the file exists *and* opens for reading, while `get_writable_*` only asks `GPlatesFileIO::is_writable`; neither validates content, so a truncated file from a crashed write still passes both. That check lives in the readers, which compare the file-size field in the header against the actual size and throw `FileFormatNotSupportedException` on a mismatch. Consequently `RasterFileCache` wraps reader construction in a catch-and-rebuild: `UnsupportedVersion` and any other `std::exception` both lead to deleting the file and regenerating it, so a bad cache degrades to a slow first load rather than a failure to display the raster.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GdalRasterReader](GdalRasterReader.md) | file-io | 151 |
| [file-io/MipmappedRasterFormatWriter](MipmappedRasterFormatWriter.md) | file-io | 121 |
| [file-io/RgbaRasterReader](RgbaRasterReader.md) | file-io | 117 |
| [file-io/RasterFileCacheFormatReader](RasterFileCacheFormatReader.md) | file-io | 38 |
| [file-io/MipmappedRasterFormatReader](MipmappedRasterFormatReader.md) | file-io | 32 |
| [file-io/RasterFileCache](RasterFileCache.md) | file-io | 20 |
| [unit-test/MipmapperTest](../unit-test/MipmapperTest.md) | unit-test | 19 |
| [file-io/SourceRasterFileCacheFormatReader](SourceRasterFileCacheFormatReader.md) | file-io | 15 |
| [qt-widgets/ScalarField3DDepthLayersPage](../qt-widgets/ScalarField3DDepthLayersPage.md) | qt-widgets | 11 |
| [property-values/ProxiedRasterResolver](../property-values/ProxiedRasterResolver.md) | property-values | 10 |
| [file-io/RasterReader](RasterReader.md) | file-io | 9 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/RasterFileCacheFormat.h
python scripts/gpq.py def GPlatesFileIO::RasterFileCacheFormat::BlockInfos --body
python scripts/gpq.py uses BlockInfos --kind class
python scripts/gpq.py hier BlockInfos
```

# ScalarField3DFileFormatReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 162 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ScalarField3DFileFormatReader.h` | C++ | 576 |
| `src/file-io/ScalarField3DFileFormatReader.cc` | C++ | 418 |

## Overview

`Reader` opens a file laid out per `GPlatesFileIO::ScalarField3DFileFormat` and validates its header before exposing any data: it checks the file is long enough to hold a header, verifies `MAGIC_NUMBER` byte by byte, compares the stored total file size against the actual size on disk (catching a file left truncated by a GPlates instance that crashed or was killed mid-write), and reads the version number to decide how to parse the rest.

The public interface hides format-versioning behind a small Pimpl/strategy split: the constructor picks a concrete `ReaderImpl` — currently only `VersionOneReader` — based on the version field, and every accessor and `read_*` method on `Reader` simply forwards to `d_impl`. The `.cc` shows this is meant to scale: a comment sketches how a later `VersionThreeReader` could take over for newer versions while `VersionOneReader` keeps serving older ones, without changing `Reader`'s public API. `VersionOneReader::VersionOneReader` reads the fixed-size header fields (tile/depth-layer counts, radii, summary statistics) once at construction and records the file offsets of the field-data, mask-data and tile-metadata blocks that follow; `read_tile_meta_data`, `read_field_data` and `read_mask_data` then `QFile::seek` to the relevant offset on each call rather than streaming sequentially, so callers can request an arbitrary sub-range of layers or tiles (e.g. to stream a scalar field incrementally into `GLScalarField3D` textures).

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ScalarField3DFileFormat::Reader`](#gplatesfileioscalarfield3dfileformatreader) | class | `boost::noncopyable` | — | 1 | Reads 3D scalar field data from a file. |

## Members

### `GPlatesFileIO::ScalarField3DFileFormat::Reader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Reader( const QString &filename)` | constructor | `None` | public | Opens filename for reading as a 3D scalar field file. |
| `get_tile_meta_data_resolution()` | method | `unsigned int` | public | Returns the resolution of the cube texture containing tile metadata. |
| `get_tile_resolution()` | method | `unsigned int` | public | Returns the tile resolution of tiles containing field data (and mask data). |
| `get_num_active_tiles()` | method | `unsigned int` | public | Returns the number of active tiles. |
| `get_num_depth_layers_per_tile()` | method | `unsigned int` | public | Returns the number of depth layers for the tiles containing field data. |
| `get_minimum_depth_layer_radius()` | method | `float` | public | Returns the minimum depth layer radius. |
| `get_maximum_depth_layer_radius()` | method | `float` | public | Returns the maximum depth layer radius. |
| `get_num_layers()` | method | `unsigned int` | public | Returns the total number of layers across all tiles. |
| `get_scalar_min()` | method | `double` | public | Returns the minimum scalar value across the entire scalar field. |
| `get_scalar_max()` | method | `double` | public | Returns the maximum scalar value across the entire scalar field. |
| `get_scalar_mean()` | method | `double` | public | Returns the mean scalar value across the entire scalar field. |
| `get_scalar_standard_deviation()` | method | `double` | public | Returns the standard deviation of scalar values across the entire scalar field. |
| `get_gradient_magnitude_min()` | method | `double` | public | Returns the minimum gradient magnitude across the entire scalar field. |
| `get_gradient_magnitude_max()` | method | `double` | public | Returns the maximum gradient magnitude across the entire scalar field. |
| `get_gradient_magnitude_mean()` | method | `double` | public | Returns the mean gradient magnitude across the entire scalar field. |
| `get_gradient_magnitude_standard_deviation()` | method | `double` | public | Returns the standard deviation of gradient magnitude across the entire scalar field. |
| `read_tile_meta_data()` | method | `boost::shared_array<TileMetaData>` | public | Reads the tile metadata. |
| `read_field_data( unsigned int layer_index, unsigned int num_layers_to_read)` | method | `boost::shared_array<FieldDataSample>` | public | Reads the tile field data (scalar/gradient field samples). |
| `read_mask_data( unsigned int tile_index, unsigned int num_tiles_to_read)` | method | `boost::shared_array<MaskDataSample>` | public | Reads the tile mask data (determines which areas of field data contain valid data used for non-global fields). |
| `get_file_info()` | method | `QFileInfo` | public | Retrieves information about the file that we are reading. |
| `get_filename()` | method | `QString` | public | Returns the filename of the file that we are reading. |
| `ReaderImpl` | class | `None` | private | — |
| `VersionOneReader` | class | `None` | private | A reader for version 1+ files. |
| `d_file` | field | `QFile` | private | — |
| `d_in` | field | `QDataStream` | private | — |
| `d_impl` | field | `boost::scoped_ptr<ReaderImpl>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_SCALARFIELD3DFILEFORMATREADER_H` | macro | `None` | — |

## Notes

The constructor throws `ErrorOpeningFileForReadingException` if the file cannot be opened, `FileFormatNotSupportedException` for a bad magic number, wrong file length, or other header inconsistency, and `ScalarField3DFileFormat::UnsupportedVersion` for a recognised-but-unhandled version number. Each `read_*` method also throws `FileFormatNotSupportedException` if its seek fails. `Reader` is `boost::noncopyable` and keeps the `QFile` open for the object's lifetime, since `read_tile_meta_data`, `read_field_data` and `read_mask_data` seek and read from it lazily on every call rather than buffering the whole file up front; the `boost::shared_array` buffers they return are independent in-memory copies that remain valid after the `Reader` is destroyed.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 102 |
| [file-io/MipmappedRasterFormatReader](MipmappedRasterFormatReader.md) | file-io | 3 |
| [file-io/SourceRasterFileCacheFormatReader](SourceRasterFileCacheFormatReader.md) | file-io | 3 |
| [app-logic/ScalarField3DLayerParams](../app-logic/ScalarField3DLayerParams.md) | app-logic | 2 |
| [presentation/ScalarField3DVisualLayerParams](../presentation/ScalarField3DVisualLayerParams.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ScalarField3DFileFormatReader.h
python scripts/gpq.py def GPlatesFileIO::ScalarField3DFileFormat::Reader --body
python scripts/gpq.py uses Reader --kind class
python scripts/gpq.py hier Reader
```

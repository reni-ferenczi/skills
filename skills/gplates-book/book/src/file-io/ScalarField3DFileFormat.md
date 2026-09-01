# ScalarField3DFileFormat

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 710 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ScalarField3DFileFormat.h` | C++ | 248 |
| `src/file-io/ScalarField3DFileFormat.cc` | C++ | 53 |

## Overview

This header defines the on-disk binary layout for GPlates' 3D scalar field files, rather than any reader or writer logic. A scalar field file is a header (magic number, file size, version, tile and depth-layer counts, per-depth-layer radii, and summary statistics for scalar and gradient magnitude) followed by tile metadata and per-sample data, all stored as little-endian single-precision floats via `QDataStream` at the fixed `Q_DATA_STREAM_VERSION` (Qt 4.4 streams, since GPlates targets that as its Qt baseline).

`TileMetaData`, `FieldDataSample` and `MaskDataSample` describe the three record shapes written per tile: per-tile min/max scalar bounds and a tile ID, per-sample scalar value plus gradient vector, and a per-(x,y) validity mask. Each struct stores its `tile_ID` and `mask` fields as `float` rather than an integer type specifically so the data can be uploaded directly into a floating-point OpenGL texture without conversion; the associated `STREAM_SIZE` constants record the serialised byte size of each struct (which can differ from `sizeof` due to padding) for callers computing file offsets. `GPlatesUtils::Endian::swap` is specialised for all three structs so raw-endian file I/O code can byte-swap them field by field.

`UnsupportedVersion` is the exception a reader throws when the version field in a file it opens does not match `VERSION_NUMBER`, distinguishing "this is a GPlates scalar field file, but a newer one than this build understands" from a corrupt or foreign file (the magic number has already been validated by that point).

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ScalarField3DFileFormat::TileMetaData`](#gplatesfileioscalarfield3dfileformattilemetadata) | struct | — | — | 0 | Information relevant to a particular tile of data (including its depth layers). |
| [`GPlatesFileIO::ScalarField3DFileFormat::FieldDataSample`](#gplatesfileioscalarfield3dfileformatfielddatasample) | struct | — | — | 0 | The scalar value data (and gradient) at a particular field sample location. |
| [`GPlatesFileIO::ScalarField3DFileFormat::MaskDataSample`](#gplatesfileioscalarfield3dfileformatmaskdatasample) | struct | — | — | 0 | The mask data at a particular field sample location (x,y) location. |
| [`GPlatesFileIO::ScalarField3DFileFormat::UnsupportedVersion`](#gplatesfileioscalarfield3dfileformatunsupportedversion) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | Thrown when reading a file containing an unrecognised version number. |

## Members

### `GPlatesFileIO::ScalarField3DFileFormat::TileMetaData`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `tile_ID` | field | `float` | public | Tile ID in half-open range \[0, num\_active\_tiles) or it can be -1 to indicate no tile. |
| `max_scalar_value` | field | `float` | public | Maximum scalar value across entire tile (including all its depth layers). |
| `min_scalar_value` | field | `float` | public | Minimum scalar value across entire tile (including all its depth layers). |
| `STREAM_SIZE` | field | `unsigned int` | public | Size of sum of individual data members. |

### `GPlatesFileIO::ScalarField3DFileFormat::FieldDataSample`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `scalar` | field | `float` | public | The scalar value. |
| `gradient` | field | `float` | public | The scalar field gradient x/y/z vector components. |
| `STREAM_SIZE` | field | `unsigned int` | public | Size of sum of individual data members. |

### `GPlatesFileIO::ScalarField3DFileFormat::MaskDataSample`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `mask` | field | `float` | public | The boolean mask value (0.0 or 1.0). |
| `STREAM_SIZE` | field | `unsigned int` | public | Size of sum of individual data members. |

### `GPlatesFileIO::ScalarField3DFileFormat::UnsupportedVersion`

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
| `GPLATES_FILEIO_SCALARFIELD3DFILEFORMAT_H` | macro | `None` | — |
| `MAGIC_NUMBER` | variable | `boost::uint8_t` | The magic number that identifies a file as GPlates. |
| `VERSION_NUMBER` | variable | `boost::uint32_t` | The current version number of the GPlates scalar field file format. |
| `Q_DATA_STREAM_VERSION` | variable | `int` | The QDataStream serialisation version. |
| `Q_DATA_STREAM_BYTE_ORDER` | variable | `QDataStream::ByteOrder` | The QDataStream byte order (most hardware is little endian so it's more efficient in general). |
| `swap( GPlatesFileIO::ScalarField3DFileFormat::TileMetaData &tile_meta_data)` | function | `void` | — |
| `swap( GPlatesFileIO::ScalarField3DFileFormat::FieldDataSample &field_data_sample)` | function | `void` | — |
| `swap( GPlatesFileIO::ScalarField3DFileFormat::MaskDataSample &mask_data_sample)` | function | `void` | — |

## Notes

`VERSION_NUMBER` must be bumped whenever the file layout changes in a breaking way (e.g. a new header field), since existing readers key their parsing logic off it. The whole format assumes `float` is 32-bit and `double` is 64-bit, and is otherwise OS/CPU independent.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/ScalarField3DFileFormatReader](ScalarField3DFileFormatReader.md) | file-io | 71 |
| [opengl/GLScalarField3DGenerator](../opengl/GLScalarField3DGenerator.md) | opengl | 64 |
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 42 |
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 13 |
| [app-logic/ScalarField3DLayerParams](../app-logic/ScalarField3DLayerParams.md) | app-logic | 4 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ScalarField3DFileFormat.h
python scripts/gpq.py def GPlatesFileIO::ScalarField3DFileFormat::UnsupportedVersion --body
python scripts/gpq.py uses UnsupportedVersion --kind class
python scripts/gpq.py hier UnsupportedVersion
```

# GzipFile

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1090 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GzipFile.h` | C++ | 138 |
| `src/file-io/GzipFile.cc` | C++ | 588 |

## Overview

[[[PROSE overview unit=file-io/GzipFile tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GzipFile::ZStream`](#gplatesfileiogzipfilezstream) | class | — | — | 0 | Wrapper around zlib's z\_stream. |
| [`GPlatesFileIO::GzipFile`](#gplatesfileiogzipfile) | class | `QIODevice` | — | 0 | A QIODevice that can read (decompress) or write (compress) a Gzip data stream. |

## Members

### `GPlatesFileIO::GzipFile::ZStream`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ZStream()` | method | `None` | public | — |
| `stream` | field | `z_stream` | public | — |
| `status` | field | `int` | public | — |

### `GPlatesFileIO::GzipFile`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GzipFile( QIODevice* device, int compression_level = -1, QObject *parent_ = NULL)` | constructor | `None` | public | 0 is no compression, 1 is best speed and 9 is best compression. |
| `~GzipFile()` | destructor | `None` | public | — |
| `open( OpenMode mode)` | method | `bool` | public | — |
| `close()` | method | `void` | public | — |
| `isSequential()` | method | `bool` | public | — |
| `readData( char *data, qint64 maxSize)` | method | `qint64` | protected | — |
| `writeData( const char *data, qint64 maxSize)` | method | `qint64` | protected | — |
| `ZStream` | class | `None` | private | Wrapper around zlib's z\_stream. |
| `STREAM_BUFFER_SIZE` | field | `int` | private | Size of stream buffers used for compressing/decompressing. zlib recommends a decent size if possible, like 128kb. |
| `GZIP_WINDOW_BITS` | field | `int` | private | The 'windowBits' parameter of zlib's 'inflateInit2()' and 'deflateInit2()' functions. |
| `d_device` | field | `QIODevice` | private | — |
| `d_zstream` | field | `boost::scoped_ptr<ZStream>` | private | — |
| `d_stream_input_buffer` | field | `QByteArray` | private | — |
| `d_stream_output_buffer` | field | `QByteArray` | private | — |
| `d_compression_level` | field | `int` | private | Compression level 0-9: 0 is no compression, 1 is best speed and 9 is best compression. |
| `flush_write()` | method | `bool` | private | Flush any unwritten data still inside zlib. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `ZLIB_WINAPI` | macro | `None` | Note that, on Windows, ZLIB\_WINAPI should be defined before including "zlib.h". |
| `GZIP_WINDOW_BITS` | variable | `int` | The 'windowBits' parameter of zlib's 'inflateInit2()' and 'deflateInit2()' functions. |
| `GPLATES_FILE_IO_GZIPFILE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/GzipFile tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlOutputVisitor](GpmlOutputVisitor.md) | file-io | 4 |
| [file-io/GpmlReader](GpmlReader.md) | file-io | 4 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 3 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GzipFile.h
python scripts/gpq.py def GPlatesFileIO::GzipFile --body
python scripts/gpq.py uses GzipFile --kind class
python scripts/gpq.py hier GzipFile
```

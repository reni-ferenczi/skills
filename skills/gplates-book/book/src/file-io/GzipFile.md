# GzipFile

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1090 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GzipFile.h` | C++ | 138 |
| `src/file-io/GzipFile.cc` | C++ | 588 |

## Overview

`GzipFile` adapts zlib's gzip mode to Qt's `QIODevice` interface so gzip-
compressed feature collections and rasters can be read and written through
the same streaming API as any other `QIODevice`. It wraps another
`QIODevice` (the underlying file or buffer) rather than talking to the
filesystem itself, decompressing through `readData` when opened
`ReadOnly` or compressing through `writeData` when opened `WriteOnly`; the
implementation follows the `zpipe.c` example from zlib's own documentation.
The private `ZStream` class exists only to keep `<zlib.h>` out of the header,
so `boost::scoped_ptr<ZStream>` is a pointer to an incomplete type from the
header's point of view.

`GZIP_WINDOW_BITS` is the `windowBits` value passed to `inflateInit2()` and
`deflateInit2()` that selects gzip framing instead of raw zlib framing, and
`STREAM_BUFFER_SIZE` (128 KB) sizes the input/output buffers zlib operates
on, per zlib's own recommendation. Because `isSequential()` always returns
true, callers cannot seek within a `GzipFile` — it must be read or written
strictly forward, as any streaming compressor requires.

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

`GzipFile` does not own the wrapped `d_device`: it opens it (if not already
open) and closes it in `close()`, but never deletes it — the caller is
responsible for the underlying device's lifetime. The destructor calls
`close()` itself and swallows any exception, since `~QIODevice()` does not
call `close()` and a destructor must not let an exception escape.
`compression_level` is validated to be at most 9 in the constructor via
`GPlatesGlobal::Assert`, and only matters when the device is opened for
writing — it is ignored when opened for reading, since the compression level
is a property of how the stream was encoded, not how it is decoded. `open()`
also rejects a mode/device combination where an already-open wrapped device's
mode does not match the requested read or write direction.

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

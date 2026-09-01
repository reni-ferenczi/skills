# TemporaryFileRegistry

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 6 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/TemporaryFileRegistry.h` | C++ | 82 |
| `src/file-io/TemporaryFileRegistry.cc` | C++ | 75 |

## Overview

A singleton registry that tracks temporary files to be deleted at application shutdown, as an alternative to `QTemporaryFile` when you need a file's lifetime to span the entire application run rather than a single object's lifetime. Register filenames with `add_file()`, and the destructor removes them all when the application exits. The unit provides a helper function to generate temp-directory paths and offers a convenience method to make a filename in the system temp directory while preserving the base name.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::TemporaryFileRegistry`](#gplatesfileiotemporaryfileregistry) | class | [`GPlatesUtils::Singleton<TemporaryFileRegistry>`](../utils/Singleton.md) | — | 0 | A singleton that collects filenames of files to be deleted when the application exits. |

## Members

### `GPlatesFileIO::TemporaryFileRegistry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `add_file( const QString &filename)` | method | `void` | private | Registers filename as a temporary file, that will be deleted when the application exits. |
| `make_filename_in_tmp_directory( const QString &filename)` | method | `QString` | private | Takes a filename (which may have a directory path) and returns the absolute filename of a file in the temp directory with the same name. e.g. "../bar/foo.txt" =\> "/tmp/foo.txt" |
| `d_filenames` | field | `std::vector<QString>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `construct_tmp_directory_path()` | function | `QString` | — |
| `GPLATES_FILEIO_TEMPORARYFILEREGISTRY_H` | macro | `None` | — |

## Notes

As a singleton, there is only one instance created at application startup and destroyed at shutdown. Files are deleted in the destructor via `QFile::remove()` in the order they were registered. If a file is deleted externally before shutdown, `QFile::remove()` silently succeeds and continues; missing or already-deleted files do not raise errors. The temp directory path is computed once at first call and cached as a static variable, so changes to the system temp directory during execution are not reflected in subsequent calls.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/RasterFileCacheFormat](RasterFileCacheFormat.md) | file-io | 5 |
| [file-io/RasterFileCache](RasterFileCache.md) | file-io | 3 |
| [file-io/MipmappedRasterFormatWriter](MipmappedRasterFormatWriter.md) | file-io | 1 |
| [file-io/RgbaRasterReader](RgbaRasterReader.md) | file-io | 1 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 1 |
| [property-values/ProxiedRasterResolver](../property-values/ProxiedRasterResolver.md) | property-values | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/TemporaryFileRegistry.h
python scripts/gpq.py def GPlatesFileIO::TemporaryFileRegistry --body
python scripts/gpq.py uses TemporaryFileRegistry --kind class
python scripts/gpq.py hier TemporaryFileRegistry
```

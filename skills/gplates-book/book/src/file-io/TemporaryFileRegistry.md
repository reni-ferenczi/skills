# TemporaryFileRegistry

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 6 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/TemporaryFileRegistry.h` | C++ | 82 |
| `src/file-io/TemporaryFileRegistry.cc` | C++ | 75 |

## Overview

[[[PROSE overview unit=file-io/TemporaryFileRegistry tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=file-io/TemporaryFileRegistry tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

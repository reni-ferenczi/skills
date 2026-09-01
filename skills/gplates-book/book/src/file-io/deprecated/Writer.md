# Writer

[Book TOC](../../../TOC.md) · [file-io](../../../components/file-io.md) · cluster Community 48 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/deprecated/Writer.h` | C++ | 55 |

## Overview

An abstract base class that defines the interface for writing files in a given format. Subclasses implement the `write()` method to serialize feature model data from a `ModelInterface` into a `FileInfo` object. It is used as an optional component within the deprecated `FileFormat` infrastructure, which packages readers and writers together with format metadata.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::Writer`](#gplatesfileiowriter) | class | — | — | 0 | — |

## Members

### `GPlatesFileIO::Writer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `write( FileInfo &fileinfo, GPlatesModel::ModelInterface &model)` | method | `void` | public | — |
| `~Writer()` | destructor | `None` | public | XXX: Include some kind of ErrorAccumulation here. |
| `Writer()` | constructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_WRITER_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/deprecated/FileFormat](FileFormat.md) | file-io | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/deprecated/Writer.h
python scripts/gpq.py def GPlatesFileIO::Writer --body
python scripts/gpq.py uses Writer --kind class
python scripts/gpq.py hier Writer
```

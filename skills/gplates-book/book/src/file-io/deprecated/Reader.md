# Reader

[Book TOC](../../../TOC.md) · [file-io](../../../components/file-io.md) · cluster Community 9 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/deprecated/Reader.h` | C++ | 65 |

## Overview

An abstract base class that defines the interface for file format readers. Subclasses implement `read_file()` to parse a file in a specific format and populate the given `ModelInterface` with the resulting feature collection, accumulating any errors in `ReadErrorAccumulation`. Concrete readers like `GPlatesReader` extend this class to support legacy file formats. This is deprecated infrastructure for the old reader-writer architecture.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::Reader`](#gplatesfileioreader) | class | — | — | 0 | The superclass for each of the classes that will convert some format of input source to the internal GPlates representation. |

## Members

### `GPlatesFileIO::Reader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `read_file( FileInfo &fileinfo, GPlatesModel::ModelInterface &model, ReadErrorAccumulation &read_errors)` | method | `GPlatesModel::FeatureCollectionHandle::weak_ref` | public | — |
| `~Reader()` | destructor | `None` | public | — |
| `Reader()` | constructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_READER_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/deprecated/FileFormat](FileFormat.md) | file-io | 3 |
| [file-io/deprecated/GPlatesReader](GPlatesReader.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/deprecated/Reader.h
python scripts/gpq.py def GPlatesFileIO::Reader --body
python scripts/gpq.py uses Reader --kind class
python scripts/gpq.py hier Reader
```

# Reader

[Book TOC](../../../TOC.md) · [file-io](../../../components/file-io.md) · cluster Community 9 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/deprecated/Reader.h` | C++ | 65 |

## Overview

[[[PROSE overview unit=file-io/deprecated/Reader tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=file-io/deprecated/Reader tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

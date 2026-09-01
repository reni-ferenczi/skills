# Writer

[Book TOC](../../../TOC.md) · [file-io](../../../components/file-io.md) · cluster Community 48 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/deprecated/Writer.h` | C++ | 55 |

## Overview

[[[PROSE overview unit=file-io/deprecated/Writer tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=file-io/deprecated/Writer tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

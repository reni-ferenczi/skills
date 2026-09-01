# FileFormat

[Book TOC](../../../TOC.md) · [file-io](../../../components/file-io.md) · cluster Community 48 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/deprecated/FileFormat.h` | C++ | 92 |

## Overview

[[[PROSE overview unit=file-io/deprecated/FileFormat tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::FileFormat`](#gplatesfileiofileformat) | class | — | — | 0 | FileFormat contains information relevant to a particular file format. |

## Members

### `GPlatesFileIO::FileFormat`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SuffixList` | typedef | `std::list<QString>` | public | — |
| `suffix_const_iterator` | typedef | `SuffixList::const_iterator` | public | — |
| `reader()` | method | `boost::optional<const Reader &>` | public | A Reader that will read in files in this format (if one exists). |
| `writer()` | method | `boost::optional<const Writer &>` | public | A Writer that will write in files in this format (if one exists). |
| `suffixes_begin()` | method | `suffix_const_iterator` | public | @{ Suffix access functions. |
| `suffixes_end()` | method | `suffix_const_iterator` | public | — |
| `d_name` | field | `QString` | private | XXX: This should be made private eventually. |
| `d_suffixes` | field | `SuffixList` | private | — |
| `d_reader` | field | `boost::optional<const Reader &>` | private | — |
| `d_writer` | field | `boost::optional<const Writer &>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_FILEFORMAT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/deprecated/FileFormat tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [entry-points/gplates_demo_no_gui_main](../../entry-points/gplates_demo_no_gui_main.md) | entry-points | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/deprecated/FileFormat.h
python scripts/gpq.py def GPlatesFileIO::FileFormat --body
python scripts/gpq.py uses FileFormat --kind class
python scripts/gpq.py hier FileFormat
```

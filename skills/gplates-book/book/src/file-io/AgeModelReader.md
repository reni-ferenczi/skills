# AgeModelReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1626 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/AgeModelReader.h` | C++ | 55 |
| `src/file-io/AgeModelReader.cc` | C++ | 176 |

## Overview

[[[PROSE overview unit=file-io/AgeModelReader tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::AgeModelReader`](#gplatesfileioagemodelreader) | class | `boost::noncopyable` | — | 0 | — |

## Members

### `GPlatesFileIO::AgeModelReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `read_file( const QString &filename, GPlatesAppLogic::AgeModelCollection &model)` | method | `void` | public | — |
| `s_delimiter` | field | `QString` | private | — |
| `s_geotimescale_marker` | field | `QString` | private | — |
| `s_comment_marker` | field | `QString` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `s_delimiter` | variable | `QString` | — |
| `s_comment_marker` | variable | `QString` | — |
| `s_geotimescale_marker` | variable | `QString` | — |
| `parse_geotimescale( const QString &line, GPlatesAppLogic::AgeModelCollection &model, const QString &geotimescale_marker)` | function | `void` | — |
| `parse_chron_line( const QString &line, GPlatesAppLogic::AgeModelCollection &model, const QString &delimiter, const QString &comment_marker)` | function | `void` | — |
| `parse_line( const QString &line, GPlatesAppLogic::AgeModelCollection &model, const QString &delimiter, const QString &geotimescale_marker, const QString &comment_marker)` | function | `void` | — |
| `AGEMODELREADER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/AgeModelReader tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/AgeModelManagerDialog](../qt-widgets/AgeModelManagerDialog.md) | qt-widgets | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/AgeModelReader.h
python scripts/gpq.py def GPlatesFileIO::AgeModelReader --body
python scripts/gpq.py uses AgeModelReader --kind class
python scripts/gpq.py hier AgeModelReader
```

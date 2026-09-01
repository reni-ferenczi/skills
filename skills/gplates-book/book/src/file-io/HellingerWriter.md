# HellingerWriter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1757 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/HellingerWriter.h` | C++ | 61 |
| `src/file-io/HellingerWriter.cc` | C++ | 233 |

## Overview

[[[PROSE overview unit=file-io/HellingerWriter tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::HellingerWriter`](#gplatesfileiohellingerwriter) | class | — | — | 0 | — |

## Members

### `GPlatesFileIO::HellingerWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HellingerWriter()` | constructor | `None` | public | — |
| `write_pick_file(QString &filename, GPlatesQtWidgets::HellingerModel& hellinger_model, bool export_disabled_picks = true, bool add_missing_pick_extension = false)` | method | `void` | public | — |
| `write_com_file( QString &filename, GPlatesQtWidgets::HellingerModel& hellinger_model)` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_plate_index( const GPlatesQtWidgets::HellingerPlateIndex index, bool enabled)` | function | `GPlatesQtWidgets::HellingerPlateIndex` | — |
| `GPLATES_FILEIO_PICKFILEWRITER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/HellingerWriter tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 138 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/HellingerWriter.h
python scripts/gpq.py def GPlatesFileIO::HellingerWriter --body
python scripts/gpq.py uses HellingerWriter --kind class
python scripts/gpq.py hier HellingerWriter
```

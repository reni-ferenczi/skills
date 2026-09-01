# NetCDFReader

[Book TOC](../../../TOC.md) · [file-io](../../../components/file-io.md) · cluster Community 1024 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/deprecated/NetCDFReader.h` | C++ | 54 |
| `src/file-io/deprecated/NetCDFReader.cc` | C++ | 396 |

## Overview

[[[PROSE overview unit=file-io/deprecated/NetCDFReader tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::NetCDFReader::(anonymous)`](#gplatesfileionetcdfreaderanonymous) | struct | — | — | 0 | — |
| [`GPlatesFileIO::NetCDFReader`](#gplatesfileionetcdfreader) | class | — | — | 0 | NetCDFReader is responsible for converting an input stream in the NetCDF data format into the GPlates internal representation. |

## Members

### `GPlatesFileIO::NetCDFReader::(anonymous)`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `name` | field | `char` | public | — |
| `types` | field | `int` | public | — |
| `min_values` | field | `int` | public | — |

### `GPlatesFileIO::NetCDFReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Read(NcFile *ncf, wxProgressDialog *dlg = 0)` | method | `GPlatesGeo::GridData` | public | Create a GridData object. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `pos(double lat, double lon)` | function | `GPlatesMaths::PointOnSphere` | — |
| `pos(GPlatesMaths::PointOnSphere pos, double &lat, double &lon)` | function | `void` | — |
| `_GPLATES_FILEIO_NETCDFREADER_H_` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/deprecated/NetCDFReader tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/deprecated/NetCDFWriter](NetCDFWriter.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/deprecated/NetCDFReader.h
python scripts/gpq.py def GPlatesFileIO::NetCDFReader --body
python scripts/gpq.py uses NetCDFReader --kind class
python scripts/gpq.py hier NetCDFReader
```

# SymbolFileReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 41 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/SymbolFileReader.h` | C++ | 53 |
| `src/file-io/SymbolFileReader.cc` | C++ | 129 |

## Overview

[[[PROSE overview unit=file-io/SymbolFileReader tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::SymbolFileReader`](#gplatesfileiosymbolfilereader) | class | — | — | 0 | Class for reading a simple symbol file, and using the content to fill the symbol\_map as appropriate. |

## Members

### `GPlatesFileIO::SymbolFileReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `read_file( const QString &filename, GPlatesGui::symbol_map_type &symbol_map)` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `read_line( const QString &line)` | function | `boost::optional<GPlatesGui::feature_type_symbol_pair_type>` | — |
| `GPLATES_FILEIO_SYMBOLFILEREADER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/SymbolFileReader tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/SymbolFileReader.h
python scripts/gpq.py def GPlatesFileIO::SymbolFileReader --body
python scripts/gpq.py uses SymbolFileReader --kind class
python scripts/gpq.py hier SymbolFileReader
```

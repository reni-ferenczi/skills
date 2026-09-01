# SymbolFileReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 41 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/SymbolFileReader.h` | C++ | 53 |
| `src/file-io/SymbolFileReader.cc` | C++ | 129 |

## Overview

Parses a simple text file that maps GPlates feature types to symbol representations. Each non-comment line specifies a feature type name, symbol type, size, and optional fill state (FILLED or UNFILLED). Empty lines and lines starting with `#` are ignored. The reader populates a `symbol_map` that `ViewportWindow` uses to render features on the map view with their configured symbol appearance.

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

The `read_file()` method clears the `symbol_map` at the start, so it replaces any previous contents. Lines must have at least three space-separated fields (feature type, symbol type, size); a fourth field (FILLED/UNFILLED) is optional and defaults to FILLED. Invalid symbol types or non-numeric sizes are silently skipped; size parsing defaults to 1 on error. The helper function `read_line()` is in the unnamed namespace and returns `boost::none` for empty lines, comments, or invalid entries.

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

# CsvExport

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 697 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/CsvExport.h` | C++ | 95 |
| `src/gui/CsvExport.cc` | C++ | 292 |

## Overview

[[[PROSE overview unit=gui/CsvExport tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::CsvExport`](#gplatesguicsvexport) | class | — | — | 0 | Class for exporting data in csv (comma-separated value) format files. |

## Members

### `GPlatesGui::CsvExport`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LineDataType` | typedef | `std::vector<QString>` | public | — |
| `ExportOptions` | struct | `None` | public | This struct is used to specify what variant of CSV to write. |
| `export_table_widget( const QString &filename, const ExportOptions &options, const QTableWidget &table)` | method | `void` | public | Export the contents of the QTableWidget table to the file filename in csv form. |
| `export_table_view( const QString &filename, const ExportOptions &options, const QTableView &table)` | method | `void` | public | Export the contents of the QTableView table to the file filename in csv form. |
| `export_line( std::ofstream &os, const ExportOptions &options, const LineDataType &line_data)` | method | `void` | public | — |
| `export_data( const QString &filename, const ExportOptions &options, const std::vector<LineDataType> &data)` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `csv_quote_if_necessary( QString str, const GPlatesGui::CsvExport::ExportOptions &options)` | function | `QString` | Attempts to apply quoting/escaping rules to a single CSV field as correctly as possible. http://en.wikipedia.org/wiki/Comma-separated\_values#Specification |
| `export_table_view_header( const QTableView &table_view, std::ofstream &os, const GPlatesGui::CsvExport::ExportOptions &options)` | function | `void` | — |
| `GPLATES_GUI_CSVEXPORT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/CsvExport tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportNetRotationAnimationStrategy](ExportNetRotationAnimationStrategy.md) | gui | 63 |
| [gui/ExportStageRotationAnimationStrategy](ExportStageRotationAnimationStrategy.md) | gui | 12 |
| [gui/ExportTotalRotationAnimationStrategy](ExportTotalRotationAnimationStrategy.md) | gui | 12 |
| [data-mining/DataTable](../data-mining/DataTable.md) | data-mining | 11 |
| [qt-widgets/TotalReconstructionPolesDialog](../qt-widgets/TotalReconstructionPolesDialog.md) | qt-widgets | 11 |
| [qt-widgets/KinematicGraphsDialog](../qt-widgets/KinematicGraphsDialog.md) | qt-widgets | 9 |
| [gui/ExportCoRegistrationAnimationStrategy](ExportCoRegistrationAnimationStrategy.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/CsvExport.h
python scripts/gpq.py def GPlatesGui::CsvExport --body
python scripts/gpq.py uses CsvExport --kind class
python scripts/gpq.py hier CsvExport
```

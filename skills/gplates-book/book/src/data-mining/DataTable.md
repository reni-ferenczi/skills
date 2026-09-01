# DataTable

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 389 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/DataTable.h` | C++ | 176 |
| `src/data-mining/DataTable.cc` | C++ | 111 |

## Overview

`DataTable` is the result container `DataSelector::select()` fills: it is a `std::vector<DataRowSharedPtr>` (one `DataRow` per seed feature) plus a `TableHeader` of column names, the `reconstruction_time` the data was computed at, and `data_index` — the column offset at which the co-registration output columns begin, after any seed-identifying columns `fill_seed_info()` writes. Each `DataRow` is itself a plain vector of `OpaqueData` cells, addressable by `operator[]`/`get_cell()`; `get_cell()` degrades to a logged warning rather than throwing when the column index is out of range.

The table knows how to render itself as text: `to_qstring_table()` converts every cell through `ConvertOpaqueDataToString`, `export_as_CSV()` builds on that to write the table (with header) via `GPlatesGui::CsvExport`, and `operator<<` gives a `{ ... }`-per-cell debug dump to an `std::ostream`. These are the paths `CoRegistrationResultTableDialog` and the co-registration CSV export use to show or save co-registration results.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::TableHeader`](#gplatesdataminingtableheader) | typedef | — | — | 0 | — |
| [`GPlatesDataMining::DataRowSharedPtr`](#gplatesdataminingdatarowsharedptr) | typedef | — | — | 0 | — |
| [`GPlatesDataMining::DataRow`](#gplatesdataminingdatarow) | class | — | — | 0 | — |
| [`GPlatesDataMining::DataTable`](#gplatesdataminingdatatable) | class | `std::vector<DataRowSharedPtr>` | — | 0 | — |

## Members

### `GPlatesDataMining::TableHeader`

*None.*

### `GPlatesDataMining::DataRowSharedPtr`

*None.*

### `GPlatesDataMining::DataRow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_cell( unsigned column_index, OpaqueData& ret)` | method | `void` | public | — |
| `append_cell( const OpaqueData& val)` | method | `void` | public | — |
| `append( std::size_t len, const OpaqueData& val)` | method | `void` | public | — |
| `size()` | method | `size_t` | public | — |
| `d_data` | field | `std::vector< OpaqueData >` | protected | — |

### `GPlatesDataMining::DataTable`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `set_table_header( TableHeader& header)` | method | `void` | public | — |
| `reconstruction_time()` | method | `double` | public | — |
| `set_reconstruction_time( double& new_time)` | method | `void` | public | — |
| `export_as_CSV( const QString& filename)` | method | `void` | public | — |
| `data_index()` | method | `std::size_t` | public | — |
| `set_data_index( std::size_t idx)` | method | `void` | public | — |
| `to_qstring_table( std::vector<std::vector<QString> >&)` | method | `void` | public | — |
| `d_table_header` | field | `TableHeader` | protected | — |
| `d_reconstruction_time` | field | `double` | protected | — |
| `d_data_index` | field | `std::size_t` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_DATATABLE_H` | macro | `None` | — |
| `operator<<` | variable | `std::ostream` | — |

## Notes

Inheriting publicly from `std::vector<DataRowSharedPtr>` means callers can use standard vector operations directly on a `DataTable`, but also that it has no virtual destructor — never delete a `DataTable` through a `std::vector` base pointer. Rows are shared via `boost::shared_ptr`, so copying a `DataTable` aliases its rows rather than deep-copying them.

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/DataSelector](DataSelector.md) | data-mining | 26 |
| [unit-test/DataAssociationDataTableTest](../unit-test/DataAssociationDataTableTest.md) | unit-test | 25 |
| [data-mining/GetValueFromPropertyVisitor](GetValueFromPropertyVisitor.md) | data-mining | 21 |
| [api/CoReg](../api/CoReg.md) | api | 16 |
| [qt-widgets/CoRegistrationResultTableDialog](../qt-widgets/CoRegistrationResultTableDialog.md) | qt-widgets | 11 |
| [app-logic/CoRegistrationData](../app-logic/CoRegistrationData.md) | app-logic | 7 |
| [data-mining/deprecated/DistanceDataOperator](deprecated/DistanceDataOperator.md) | data-mining | 4 |
| [data-mining/deprecated/PresenceDataOperator](deprecated/PresenceDataOperator.md) | data-mining | 4 |
| [data-mining/deprecated/SubDataSelector](deprecated/SubDataSelector.md) | data-mining | 4 |
| [data-mining/deprecated/MinDataOperator](deprecated/MinDataOperator.md) | data-mining | 3 |
| [data-mining/deprecated/NumInROIDataOperator](deprecated/NumInROIDataOperator.md) | data-mining | 3 |
| [unit-test/FilterTest](../unit-test/FilterTest.md) | unit-test | 3 |
| [data-mining/deprecated/DataOperator](deprecated/DataOperator.md) | data-mining | 2 |
| [gui/CommandServer](../gui/CommandServer.md) | gui | 2 |
| [gui/ExportCoRegistrationAnimationStrategy](../gui/ExportCoRegistrationAnimationStrategy.md) | gui | 2 |
| [app-logic/CoRegistrationLayerTask](../app-logic/CoRegistrationLayerTask.md) | app-logic | 1 |
| [data-mining/CoRegConfigurationTable](CoRegConfigurationTable.md) | data-mining | 1 |
| [data-mining/RFGToPropertyValueMapper](RFGToPropertyValueMapper.md) | data-mining | 1 |
| [data-mining/deprecated/LookupDataOperator](deprecated/LookupDataOperator.md) | data-mining | 1 |
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 1 |

*... and 2 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/DataTable.h
python scripts/gpq.py def GPlatesDataMining::DataTable --body
python scripts/gpq.py uses DataTable --kind class
python scripts/gpq.py hier DataTable
```

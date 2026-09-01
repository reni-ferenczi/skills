# CoRegConfigurationTable

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 158 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/CoRegConfigurationTable.h` | C++ | 288 |
| `src/data-mining/CoRegConfigurationTable.cc` | C++ | 238 |

## Overview

[[[PROSE overview unit=data-mining/CoRegConfigurationTable tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::ConfigurationTableRow`](#gplatesdataminingconfigurationtablerow) | struct | — | — | 0 | — |
| [`GPlatesDataMining::CoRegCfgTableOptimized`](#gplatesdataminingcoregcfgtableoptimized) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | — |
| [`GPlatesDataMining::CoRegConfigurationTable`](#gplatesdataminingcoregconfigurationtable) | class | `boost::equality_comparable<CoRegConfigurationTable>` | — | 0 | — |
| [`GPlatesScribe::TranscribeContext<GPlatesDataMining::ConfigurationTableRow>`](#gplatesscribetranscribecontextgplatesdataminingconfigurationtablerow) | class | — | `<>` | 0 | Used to convert a layer to a layer index when saving a 'ConfigurationTableRow' and vice versa when loading. |

## Members

### `GPlatesDataMining::ConfigurationTableRow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConfigurationTableRow()` | constructor | `None` | public | — |
| `operator==( const ConfigurationTableRow &rhs)` | operator | `bool` | public | — |
| `target_layer` | field | `GPlatesAppLogic::Layer` | public | — |
| `filter_cfg` | field | `boost::shared_ptr<CoRegFilter::Config>` | public | — |
| `attr_name` | field | `QString` | public | — |
| `layer_name` | field | `QString` | public | — |
| `assoc_name` | field | `QString` | public | — |
| `attr_type` | field | `AttributeType` | public | — |
| `reducer_type` | field | `ReducerType` | public | — |
| `raster_level_of_detail` | field | `unsigned int` | public | — |
| `raster_fill_polygons` | field | `bool` | public | — |
| `index` | field | `unsigned` | public | — |
| `transcribe( GPlatesScribe::Scribe &scribe, bool transcribed_construct_data)` | method | `GPlatesScribe::TranscribeResult` | private | — |

### `GPlatesDataMining::CoRegCfgTableOptimized`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CoRegCfgTableOptimized( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |

### `GPlatesDataMining::CoRegConfigurationTable`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `iterator` | typedef | `std::vector<ConfigurationTableRow>::iterator` | public | — |
| `const_iterator` | typedef | `std::vector<ConfigurationTableRow>::const_iterator` | public | — |
| `begin()` | method | `iterator` | public | — |
| `end()` | method | `iterator` | public | — |
| `operator==( const CoRegConfigurationTable &rhs)` | operator | `bool` | public | 'operator!=()' provided by boost::equality\_comparable. |
| `clear()` | method | `void` | public | — |
| `push_back(const ConfigurationTableRow& row)` | method | `void` | public | — |
| `optimize()` | method | `void` | public | — |
| `is_optimized()` | method | `bool` | public | — |
| `CoRegConfigurationTable()` | constructor | `None` | public | — |
| `size()` | method | `std::size_t` | public | — |
| `group_and_sort()` | method | `void` | protected | — |
| `d_rows` | field | `std::vector< ConfigurationTableRow >` | private | — |
| `d_optimized` | field | `bool` | private | — |
| `transcribe( GPlatesScribe::Scribe &scribe, bool transcribed_construct_data)` | method | `GPlatesScribe::TranscribeResult` | private | — |

### `GPlatesScribe::TranscribeContext<GPlatesDataMining::ConfigurationTableRow>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `layer_seq_type` | typedef | `std::vector<GPlatesAppLogic::Layer>` | public | — |
| `TranscribeContext( const layer_seq_type &layers)` | method | `None` | public | — |
| `d_layers` | field | `layer_seq_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `compare_layer( const ConfigurationTableRow& row_1, const ConfigurationTableRow& row_2)` | function | `bool` | — |
| `compare_filter_type( const ConfigurationTableRow& row_1, const ConfigurationTableRow& row_2)` | function | `bool` | — |
| `compare_filter( const ConfigurationTableRow& row_1, const ConfigurationTableRow& row_2)` | function | `bool` | — |
| `operator==( const ConfigurationTableRow &rhs)` | operator | `bool` | — |
| `GPLATESDATAMINING_COREGCONFIGURATIONTABLE_H` | macro | `None` | — |
| `to_string( const GPlatesDataMining::ConfigurationTableRow& row)` | function | `QString` | — |

## Notes

[[[PROSE notes unit=data-mining/CoRegConfigurationTable tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 140 |
| [data-mining/DataSelector](DataSelector.md) | data-mining | 54 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 47 |
| [api/CoReg](../api/CoReg.md) | api | 41 |
| [data-mining/CoRegFilterCache](CoRegFilterCache.md) | data-mining | 23 |
| [app-logic/CoRegistrationLayerProxy](../app-logic/CoRegistrationLayerProxy.md) | app-logic | 21 |
| [data-mining/DataMiningUtils](DataMiningUtils.md) | data-mining | 19 |
| [data-mining/CoRegFilterMapReduceFactory](CoRegFilterMapReduceFactory.md) | data-mining | 16 |
| [app-logic/CoRegistrationLayerTask](../app-logic/CoRegistrationLayerTask.md) | app-logic | 15 |
| [gui/CommandServer](../gui/CommandServer.md) | gui | 10 |
| [app-logic/CoRegistrationLayerParams](../app-logic/CoRegistrationLayerParams.md) | app-logic | 9 |
| [data-mining/LookupReducer](LookupReducer.md) | data-mining | 6 |
| [data-mining/deprecated/SubDataSelector](deprecated/SubDataSelector.md) | data-mining | 6 |
| [data-mining/RFGToRelationalPropertyMapper](RFGToRelationalPropertyMapper.md) | data-mining | 5 |
| [data-mining/deprecated/DataOperator](deprecated/DataOperator.md) | data-mining | 4 |
| [unit-test/CoregTest](../unit-test/CoregTest.md) | unit-test | 4 |
| [app-logic/LayerTaskRegistry](../app-logic/LayerTaskRegistry.md) | app-logic | 3 |
| [qt-widgets/CoRegistrationResultTableDialog](../qt-widgets/CoRegistrationResultTableDialog.md) | qt-widgets | 3 |
| [data-mining/RFGToPropertyValueMapper](RFGToPropertyValueMapper.md) | data-mining | 2 |
| [data-mining/deprecated/DistanceDataOperator](deprecated/DistanceDataOperator.md) | data-mining | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/CoRegConfigurationTable.h
python scripts/gpq.py def GPlatesDataMining::CoRegConfigurationTable --body
python scripts/gpq.py uses CoRegConfigurationTable --kind class
python scripts/gpq.py hier CoRegConfigurationTable
```

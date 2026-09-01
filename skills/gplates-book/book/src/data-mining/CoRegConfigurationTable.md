# CoRegConfigurationTable

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 158 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/CoRegConfigurationTable.h` | C++ | 288 |
| `src/data-mining/CoRegConfigurationTable.cc` | C++ | 238 |

## Overview

This is the declarative description of a co-registration run: what to co-register against what, and how to collapse the result. One `ConfigurationTableRow` is one association — a target `GPlatesAppLogic::Layer` to sample, a spatial filter described by a `CoRegFilter::Config` (in practice `RegionOfInterestFilter::Config`, carrying a range in km), the name and `AttributeType` of the attribute to extract, and a `ReducerType` that reduces the many matched target features down to one value. `DataSelector` copies the table, then for each reconstructed seed feature walks it row by row and writes one cell per row into the output `DataTable`; the table therefore doubles as the column schema of the result, which is why `DataSelector::populate_table_header()` derives every column heading from `assoc_name`, `attr_name` and `reducer_type`.

The reason this is a class and not a `std::vector<ConfigurationTableRow>` is `optimize()`. `group_and_sort()` first stamps each row with its original position in `index`, then reorders the rows: grouped by target layer, within that grouped by `filter_cfg->filter_name()`, and within that sorted by the filter config itself — note that `compare_filter` passes its arguments to `CoRegFilter::Config::operator<` reversed, so each group ends up widest-first. That ordering exists to feed `CoRegFilterCache`, whose `find()` only reuses a cached result set when the requested config compares *less than* a cached one, i.e. when the new region of interest is contained in an already-computed one. Visiting the widest region first means every narrower row on the same layer re-filters the previous, smaller result instead of the full set of reconstructed target features. The `index` stamped before the sort is what keeps the user's column order intact despite the reordering: results and headers are written at `row.index + DataTable::data_index()`, never at the row's position in the table.

Around the unit, `GPlatesAppLogic::CoRegistrationLayerParams` holds the authoritative table for a co-registration layer, `GPlatesQtWidgets::CoRegistrationLayerConfigurationDialog` rebuilds it from the widgets and optimises it before setting it back, and `GPlatesAppLogic::CoRegistrationLayerProxy::set_current_coregistration_configuration_table()` compares the incoming table with `operator==` to decide whether to drop its cached results and invalidate its subject token — so table equality is the change-detection mechanism for the whole layer. The `GPlatesScribe::TranscribeContext` specialisation is the hook that makes rows storable in a project or session: a `GPlatesAppLogic::Layer` is a weak handle with no serialisable identity, so `GPlatesPresentation::TranscribeSession` installs a context holding the session's layer sequence and the row transcribes an index into it.

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

**Optimised means frozen, but only partly enforced.** Once `optimize()` has set `d_optimized`, the non-`const` `begin()`, `end()`, `clear()` and `push_back()` throw `CoRegCfgTableOptimized`. `group_and_sort()` can still use the non-`const` iterators because `optimize()` sets the flag only after it returns. The `const` overloads and *both* `operator[]` overloads are unguarded, so the non-`const` `operator[]` is an open hole through which an optimised table can still be mutated — including its `index`, on which the result-column mapping depends. `d_optimized` is copied by the implicit copy constructor, so a copy of an optimised table is frozen too; the dialog and `CoRegistrationLayerTask` both build a *fresh* table and re-optimise rather than editing an existing one. `DataSelector`'s constructor calls `optimize()` on its private copy if the caller had not, so anything reaching `DataSelector` is grouped and indexed.

**`CoRegCfgTableOptimized` cannot be caught as a `GPlatesGlobal::Exception`.** The class declaration omits `public:` on its base, so the inheritance is private. Nothing in the tree catches this type, and a `catch (GPlatesGlobal::Exception &)` will not intercept it either — a stray write to an optimised table escapes to the top level.

**Row equality can throw, and can dereference null.** `ConfigurationTableRow::operator==` dereferences `filter_cfg` unconditionally, and the default constructor leaves that `shared_ptr` null. Worse, `CoRegFilter::Config::operator==` and `operator<` are implemented (in `RegionOfInterestFilter::Config`, for example) to throw `GPlatesGlobal::LogException` when the other config is of a different concrete type — so comparing two tables whose rows use different filter types raises rather than returning `false`. `group_and_sort()` sidesteps this by only applying `compare_filter` within an `equal_range` of identical `filter_name()`.

**`index` participates in equality.** Because `operator==` compares the row vectors elementwise and `index` is only assigned by `group_and_sort()`, a table that has not been optimised will not compare equal to an otherwise identical one that has. Every path that hands a table to a client — the dialog, the layer task and the load-side `transcribe()` — calls `optimize()` for exactly that reason. The grouping key `compare_layer` uses `GPlatesAppLogic::Layer::operator<`, which compares `boost::weak_ptr` addresses; that is fine as a grouping key within one process but means the resulting row order is arbitrary and not reproducible across runs, so equality is only meaningful between tables built in the same session.

**Transcription is lenient on load and silent on a bad save.** `CoRegConfigurationTable::transcribe()` skips rows that fail to load and carries on, so a project can come back with fewer associations than were saved — for instance when a row's target layer failed to load, which the row's own `transcribe()` reports as `TRANSCRIBE_INCOMPATIBLE`. `index` is deliberately not transcribed; it is re-derived by the `optimize()` at the end of the load. A row also requires a `TranscribeContext<ConfigurationTableRow>` to be in scope, and on the save side, if `target_layer` is not found in that context's layer list, nothing is written for it at all and the row will fail to load back.

**Enum string ids are part of the file format.** The `transcribe()` overloads for `AttributeType` and `ReducerType` in `Types.h` map each enumerator to a literal string; the header warns that changing those strings breaks backward and forward compatibility of projects and sessions, even if the C++ enumerator is renamed. New enumerators must be added there as well as to the enum.

**Raster rows take a different path.** `raster_level_of_detail` and `raster_fill_polygons` only apply when `attr_type` is `CO_REGISTRATION_RASTER_ATTRIBUTE`, and `DataSelector` skips those rows in its per-seed loop entirely — it batches them per raster layer in a separate code path, so they never touch `CoRegFilterCache` and gain nothing from the widest-first ordering.

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

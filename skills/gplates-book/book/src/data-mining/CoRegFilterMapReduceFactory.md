# CoRegFilterMapReduceFactory

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1258 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/CoRegFilterMapReduceFactory.h` | C++ | 100 |
| `src/data-mining/CoRegFilterMapReduceFactory.cc` | C++ | 115 |

## Overview

[[[PROSE overview unit=data-mining/CoRegFilterMapReduceFactory tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::CoRegFilterFactory`](#gplatesdataminingcoregfilterfactory) | class | — | — | 0 | — |
| [`GPlatesDataMining::CoRegMapperFactory`](#gplatesdataminingcoregmapperfactory) | class | — | — | 0 | — |
| [`GPlatesDataMining::CoRegReducerFactory`](#gplatesdataminingcoregreducerfactory) | class | — | — | 0 | — |

## Members

### `GPlatesDataMining::CoRegFilterFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( const ConfigurationTableRow&, const GPlatesAppLogic::ReconstructContext::ReconstructedFeature &reconstructed_seed_feature)` | method | `CoRegFilter` | public | — |

### `GPlatesDataMining::CoRegMapperFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( const ConfigurationTableRow& row, const GPlatesAppLogic::ReconstructContext::ReconstructedFeature &reconstructed_seed_feature)` | method | `CoRegMapper` | public | — |

### `GPlatesDataMining::CoRegReducerFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( const ConfigurationTableRow& row, const GPlatesAppLogic::ReconstructContext::ReconstructedFeature &reconstructed_seed_feature)` | method | `CoRegReducer` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_COREGFILTERMAPREDUCEFACTORY_H` | macro | `None` | — |
| `create_filter_map_reduce( const ConfigurationTableRow& row, const GPlatesAppLogic::ReconstructContext::ReconstructedFeature &reconstructed_seed_feature)` | function | `boost::tuple< boost::shared_ptr<CoRegFilter>, boost::shared_ptr<CoRegMapper>, boost::shared_ptr<CoRegReducer> >` | — |

## Notes

[[[PROSE notes unit=data-mining/CoRegFilterMapReduceFactory tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/DataSelector](DataSelector.md) | data-mining | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/CoRegFilterMapReduceFactory.h
python scripts/gpq.py def GPlatesDataMining::CoRegFilterFactory --body
python scripts/gpq.py uses CoRegFilterFactory --kind class
python scripts/gpq.py hier CoRegFilterFactory
```

# DataOperator

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 122 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/DataOperator.h` | C++ | 147 |
| `src/data-mining/deprecated/DataOperator.cc` | C++ | 131 |

## Overview

[[[PROSE overview unit=data-mining/deprecated/DataOperator tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::DataOperatorParameters`](#gplatesdataminingdataoperatorparameters) | struct | — | — | 0 | TODO |
| [`GPlatesDataMining::DataOperator`](#gplatesdataminingdataoperator) | class | — | — | 9 | — |

## Members

### `GPlatesDataMining::DataOperatorParameters`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DataOperatorParameters()` | constructor | `None` | public | — |
| `d_is_shape_file_attr` | field | `bool` | public | — |

### `GPlatesDataMining::DataOperator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DataOperatorNameMap` | typedef | `std::map< QString, DataOperatorType >` | public | — |
| `d_data_operator_name_map` | field | `DataOperatorNameMap` | public | — |
| `~DataOperator()` | destructor | `None` | public | — |
| `get_data( const AssociationOperator::AssociatedCollection& input, const QString& attr_name, DataRow& data_row)` | method | `void` | public | — |
| `get_property_by_name( GPlatesModel::FeatureHandle::const_weak_ref feature_ref, QString name)` | method | `boost::optional< GPlatesModel::TopLevelProperty::non_null_ptr_to_const_type >` | protected | Comments |
| `get_value( GPlatesModel::TopLevelProperty::non_null_ptr_to_const_type property, std::vector< DataType >& data)` | method | `void` | protected | Comments |
| `get_value( GPlatesModel::TopLevelProperty::non_null_ptr_to_const_type property, std::vector< QVariant >& data, QString shape_attr_name)` | method | `void` | protected | Comments temporary hacking code for shapefileattribute. |
| `get_closest_features( const AssociationOperator::AssociatedCollection&, std::vector< GPlatesModel::FeatureHandle::const_weak_ref >&)` | method | `void` | protected | Comments |
| `get_closest_feature( const AssociationOperator::AssociatedCollection&)` | method | `boost::optional< GPlatesModel::FeatureHandle::const_weak_ref >` | protected | Comments |
| `get_closest_feature( AssociationOperator::AssociatedCollection&)` | method | `boost::optional< GPlatesModel::FeatureHandle::weak_ref >` | protected | Comments |
| `DataOperator()` | constructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `d_data_operator_name_map` | variable | `DataOperator::DataOperatorNameMap` | — |
| `GPLATESDATAMINING_DATAOPERATOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=data-mining/deprecated/DataOperator tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/deprecated/LookupDataOperator](LookupDataOperator.md) | data-mining | 11 |
| [data-mining/deprecated/MinDataOperator](MinDataOperator.md) | data-mining | 7 |
| [data-mining/deprecated/DataOperatorFactory](DataOperatorFactory.md) | data-mining | 5 |
| [data-mining/deprecated/DistanceDataOperator](DistanceDataOperator.md) | data-mining | 4 |
| [data-mining/deprecated/NumInROIDataOperator](NumInROIDataOperator.md) | data-mining | 4 |
| [data-mining/deprecated/PresenceDataOperator](PresenceDataOperator.md) | data-mining | 4 |
| [data-mining/deprecated/MaxDistanceDataOperator](MaxDistanceDataOperator.md) | data-mining | 2 |
| [data-mining/deprecated/MeanDistanceDataOperator](MeanDistanceDataOperator.md) | data-mining | 2 |
| [data-mining/deprecated/MedianDistanceDataOperator](MedianDistanceDataOperator.md) | data-mining | 2 |
| [data-mining/deprecated/MinDistanceDataOperator](MinDistanceDataOperator.md) | data-mining | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/deprecated/DataOperator.h
python scripts/gpq.py def GPlatesDataMining::DataOperator --body
python scripts/gpq.py uses DataOperator --kind class
python scripts/gpq.py hier DataOperator
```

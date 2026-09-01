# LookupDataOperator

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 937 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/LookupDataOperator.h` | C++ | 84 |
| `src/data-mining/deprecated/LookupDataOperator.cc` | C++ | 140 |

## Overview

A `DataOperator` that retrieves attribute values from associated features and stores them in a data row. The `get_data()` method examines a configuration flag `d_is_shape_file_attr` to determine whether to extract from feature properties or from shapefile attributes. For feature properties, `get_qstring_from_feature()` looks up a property by name, extracts its value, and returns the first value as a `QString`. For shapefile attributes, `get_qstring_from_shape_attr()` queries the special `shapefileAttributes` property. If no value is found or the property is missing, `EmptyData` is recorded instead.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::LookUpDataOperator`](#gplatesdatamininglookupdataoperator) | class | [`DataOperator`](DataOperator.md) | — | 0 | Comments... |

## Members

### `GPlatesDataMining::LookUpDataOperator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~LookUpDataOperator()` | destructor | `None` | public | — |
| `get_data( const AssociationOperator::AssociatedCollection& input, const QString& attr_name, DataRow& data_row)` | method | `void` | public | — |
| `get_qstring_from_feature( const AssociationOperator::AssociatedCollection& input, const QString& attr_name)` | method | `boost::optional< QString >` | protected | — |
| `get_qstring_from_shape_attr( const AssociationOperator::AssociatedCollection& input, const QString& attr_name)` | method | `boost::optional< QString >` | protected | — |
| `d_cfg` | field | `DataOperatorParameters` | protected | — |
| `LookUpDataOperator( DataOperatorParameters& cfg)` | constructor | `None` | protected | — |
| `LookUpDataOperator()` | constructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_LOOKUPDATAOPERATOR_H` | macro | `None` | — |

## Notes

If a property has multiple values, only the first is returned with a debug warning. If a property has no values, or if the property itself does not exist, the lookup returns `boost::none` and `EmptyData` is recorded. The shapefile attribute path is marked as a temporary implementation.

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/deprecated/DataOperatorFactory](DataOperatorFactory.md) | data-mining | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/deprecated/LookupDataOperator.h
python scripts/gpq.py def GPlatesDataMining::LookUpDataOperator --body
python scripts/gpq.py uses LookUpDataOperator --kind class
python scripts/gpq.py hier LookUpDataOperator
```

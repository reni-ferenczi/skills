# GetValueFromPropertyVisitor

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 612 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/GetValueFromPropertyVisitor.h` | C++ | 147 |
| `src/data-mining/GetValueFromPropertyVisitor.cc` | C++ | 161 |

## Overview

A visitor that extracts data from property values during traversal. Handles scalar properties (boolean, integer, double, string) by storing their raw values, and converts geometric and complex properties to string representations. Stores all extracted values in a vector of `OpaqueData` objects. Many property types are not extracted (routed to no-op visits) because they lack meaningful scalar or geometric data to mine.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::GetValueFromPropertyVisitor`](#gplatesdatamininggetvaluefrompropertyvisitor) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Get OpaqueData data from property. |

## Members

### `GPlatesDataMining::GetValueFromPropertyVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit_enumeration(enumeration_type &enumeration)` | method | `void` | public | — |
| `visit_gml_data_block(gml_data_block_type &gml_data_block)` | method | `void` | public | — |
| `visit_gml_line_string(gml_line_string_type &gml_line_string)` | method | `void` | public | — |
| `visit_gml_multi_point(gml_multi_point_type &gml_multi_point)` | method | `void` | public | — |
| `visit_gml_orientable_curve(gml_orientable_curve_type &gml_orientable_curve)` | method | `void` | public | — |
| `visit_gml_point(gml_point_type &gml_point)` | method | `void` | public | — |
| `visit_gml_polygon(gml_polygon_type &gml_polygon)` | method | `void` | public | — |
| `visit_gml_time_instant(gml_time_instant_type &gml_time_instant)` | method | `void` | public | — |
| `visit_gml_time_period(gml_time_period_type &gml_time_period)` | method | `void` | public | — |
| `visit_gpml_plate_id(gpml_plate_id_type &gpml_plate_id)` | method | `void` | public | — |
| `visit_gpml_constant_value(gpml_constant_value_type &gpml_constant_value)` | method | `void` | public | — |
| `visit_gpml_feature_reference(gpml_feature_reference_type &gpml_feature_reference)` | method | `void` | public | — |
| `visit_gpml_feature_snapshot_reference(gpml_feature_snapshot_reference_type &gpml_feature_snapshot_reference)` | method | `void` | public | — |
| `visit_gpml_finite_rotation(gpml_finite_rotation_type &gpml_finite_rotation)` | method | `void` | public | — |
| `visit_gpml_finite_rotation_slerp(gpml_finite_rotation_slerp_type &gpml_finite_rotation_slerp)` | method | `void` | public | — |
| `visit_gpml_hot_spot_trail_mark(gpml_hot_spot_trail_mark_type &gpml_hot_spot_trail_mark)` | method | `void` | public | — |
| `visit_gpml_irregular_sampling(gpml_irregular_sampling_type &gpml_irregular_sampling)` | method | `void` | public | — |
| `visit_gpml_key_value_dictionary(gpml_key_value_dictionary_type &gpml_key_value_dictionary)` | method | `void` | public | — |
| `visit_gpml_measure(gpml_measure_type &gpml_measure)` | method | `void` | public | — |
| `visit_gpml_old_plates_header(gpml_old_plates_header_type &gpml_old_plates_header)` | method | `void` | public | — |
| `visit_gpml_piecewise_aggregation(gpml_piecewise_aggregation_type &gpml_piecewise_aggregation)` | method | `void` | public | — |
| `visit_gpml_polarity_chron_id(gpml_polarity_chron_id_type &gpml_polarity_chron_id)` | method | `void` | public | — |
| `visit_gpml_property_delegate(gpml_property_delegate_type &gpml_property_delegate)` | method | `void` | public | — |
| `visit_gpml_revision_id(gpml_revision_id_type &gpml_revision_id)` | method | `void` | public | — |
| `visit_gpml_topological_polygon(gpml_topological_polygon_type &gpml_topological_polygon)` | method | `void` | public | — |
| `visit_gpml_topological_line_section(gpml_topological_line_section_type &gpml_topological_line_section)` | method | `void` | public | — |
| `visit_gpml_topological_point(gpml_topological_point_type &gpml_topological_point)` | method | `void` | public | — |
| `visit_uninterpreted_property_value(uninterpreted_property_value_type &uninterpreted_prop_val)` | method | `void` | public | — |
| `visit_xs_boolean(xs_boolean_type &xs_boolean)` | method | `void` | public | — |
| `visit_xs_double(xs_double_type &xs_double)` | method | `void` | public | — |
| `visit_xs_integer(xs_integer_type &xs_integer)` | method | `void` | public | — |
| `visit_xs_string(xs_string_type &xs_string)` | method | `void` | public | — |
| `to_qstring( const GPlatesModel::PropertyValue& data)` | method | `QString` | protected | — |
| `d_data` | field | `std::vector<OpaqueData>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_GETVALUEFROMPROPERTYVISITOR_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/deprecated/MinDataOperator](deprecated/MinDataOperator.md) | data-mining | 3 |
| [data-mining/DataMiningUtils](DataMiningUtils.md) | data-mining | 2 |
| [data-mining/deprecated/DataOperator](deprecated/DataOperator.md) | data-mining | 2 |
| [data-mining/deprecated/LookupDataOperator](deprecated/LookupDataOperator.md) | data-mining | 2 |
| [data-mining/OpaqueDataToQString](OpaqueDataToQString.md) | data-mining | 1 |
| [data-mining/RFGToPropertyValueMapper](RFGToPropertyValueMapper.md) | data-mining | 1 |
| [data-mining/deprecated/DistanceDataOperator](deprecated/DistanceDataOperator.md) | data-mining | 1 |
| [data-mining/deprecated/NumInROIDataOperator](deprecated/NumInROIDataOperator.md) | data-mining | 1 |
| [data-mining/deprecated/PresenceDataOperator](deprecated/PresenceDataOperator.md) | data-mining | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/GetValueFromPropertyVisitor.h
python scripts/gpq.py def GPlatesDataMining::GetValueFromPropertyVisitor --body
python scripts/gpq.py uses GetValueFromPropertyVisitor --kind class
python scripts/gpq.py hier GetValueFromPropertyVisitor
```

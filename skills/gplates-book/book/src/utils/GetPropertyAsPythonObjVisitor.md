# GetPropertyAsPythonObjVisitor

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 179 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/GetPropertyAsPythonObjVisitor.h` | C++ | 252 |
| `src/utils/GetPropertyAsPythonObjVisitor.cc` | C++ | 376 |

## Overview

[[[PROSE overview unit=utils/GetPropertyAsPythonObjVisitor tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::GetPropertyAsPythonObjVisitor`](#gplatesutilsgetpropertyaspythonobjvisitor) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Get property value as python object. |

## Members

### `GPlatesUtils::GetPropertyAsPythonObjVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit_enumeration( enumeration_type &enumeration)` | method | `void` | public | — |
| `visit_gml_data_block( gml_data_block_type &v)` | method | `void` | public | — |
| `visit_gml_line_string( gml_line_string_type &gml_line_string)` | method | `void` | public | — |
| `visit_gml_multi_point( gml_multi_point_type &gml_multi_point)` | method | `void` | public | — |
| `visit_gml_orientable_curve( gml_orientable_curve_type &gml_orientable_curve)` | method | `void` | public | — |
| `visit_gml_point( gml_point_type &gml_point)` | method | `void` | public | — |
| `visit_gml_polygon( gml_polygon_type &gml_polygon)` | method | `void` | public | — |
| `visit_gml_time_instant( gml_time_instant_type &gml_time_instant)` | method | `void` | public | — |
| `visit_gml_time_period( gml_time_period_type &gml_time_period)` | method | `void` | public | — |
| `visit_gpml_plate_id( gpml_plate_id_type &gpml_plate_id)` | method | `void` | public | — |
| `visit_gpml_constant_value( gpml_constant_value_type &gpml_constant_value)` | method | `void` | public | — |
| `visit_gpml_feature_reference( gpml_feature_reference_type &v)` | method | `void` | public | — |
| `visit_gpml_feature_snapshot_reference( gpml_feature_snapshot_reference_type &v)` | method | `void` | public | — |
| `visit_gpml_finite_rotation( gpml_finite_rotation_type &v)` | method | `void` | public | — |
| `visit_gpml_finite_rotation_slerp( gpml_finite_rotation_slerp_type &v)` | method | `void` | public | — |
| `visit_gpml_hot_spot_trail_mark( gpml_hot_spot_trail_mark_type &v)` | method | `void` | public | — |
| `visit_gpml_irregular_sampling( gpml_irregular_sampling_type &v)` | method | `void` | public | — |
| `visit_gpml_key_value_dictionary( gpml_key_value_dictionary_type &v)` | method | `void` | public | — |
| `visit_gpml_measure( gpml_measure_type &v)` | method | `void` | public | — |
| `visit_gpml_old_plates_header( gpml_old_plates_header_type &v)` | method | `void` | public | — |
| `visit_gpml_piecewise_aggregation( gpml_piecewise_aggregation_type &v)` | method | `void` | public | — |
| `visit_gpml_polarity_chron_id( gpml_polarity_chron_id_type &v)` | method | `void` | public | — |
| `visit_gpml_property_delegate( gpml_property_delegate_type &v)` | method | `void` | public | — |
| `visit_gpml_revision_id( gpml_revision_id_type &v)` | method | `void` | public | — |
| `visit_gpml_topological_polygon( gpml_topological_polygon_type &v)` | method | `void` | public | — |
| `visit_gpml_topological_line_section( gpml_topological_line_section_type &v)` | method | `void` | public | — |
| `visit_gpml_topological_point( gpml_topological_point_type &v)` | method | `void` | public | — |
| `visit_uninterpreted_property_value( uninterpreted_property_value_type &v)` | method | `void` | public | — |
| `visit_xs_boolean( xs_boolean_type &v)` | method | `void` | public | — |
| `visit_xs_double( xs_double_type &v)` | method | `void` | public | — |
| `visit_xs_integer( xs_integer_type &v)` | method | `void` | public | — |
| `visit_xs_string( xs_string_type &xs_string)` | method | `void` | public | — |
| `get_data()` | method | `bp::object` | public | — |
| `to_qstring( const GPlatesModel::PropertyValue& data)` | method | `QString` | protected | — |
| `d_val` | field | `bp::object` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_GETPROPERTYASPYTHONOBJVISITOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=utils/GetPropertyAsPythonObjVisitor tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [api/PyFeature](../api/PyFeature.md) | api | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/GetPropertyAsPythonObjVisitor.h
python scripts/gpq.py def GPlatesUtils::GetPropertyAsPythonObjVisitor --body
python scripts/gpq.py uses GetPropertyAsPythonObjVisitor --kind class
python scripts/gpq.py hier GetPropertyAsPythonObjVisitor
```

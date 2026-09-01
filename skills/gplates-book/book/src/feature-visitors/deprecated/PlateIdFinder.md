# PlateIdFinder

[Book TOC](../../../TOC.md) · [feature-visitors](../../../components/feature-visitors.md) · cluster Community 1077 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/deprecated/PlateIdFinder.h` | C++ | 116 |
| `src/feature-visitors/deprecated/PlateIdFinder.cc` | C++ | 91 |

## Overview

This deprecated visitor finds and accumulates all plate IDs contained within a feature. It can optionally filter the search to specific property names. The found plate IDs are accumulated in a container and retrievable via iteration. This is deprecated and exists only for legacy compatibility. A FIXME note in the header indicates it should take a reconstruction time to handle time-dependent property values correctly.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFeatureVisitors::PlateIdFinder`](#gplatesfeaturevisitorsplateidfinder) | class | [`GPlatesModel::ConstFeatureVisitor`](../../model/FeatureVisitor.md) | — | 0 | This const feature visitor finds all plate IDs contained within the feature. |

## Members

### `GPlatesFeatureVisitors::PlateIdFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `plate_id_container_type` | typedef | `std::vector<GPlatesModel::integer_plate_id_type>` | public | — |
| `plate_id_container_const_iterator` | typedef | `plate_id_container_type::const_iterator` | public | — |
| `PlateIdFinder()` | constructor | `None` | public | FIXME: We should also pass the current reconstruction time, so we can correctly handle time-dependent property values. |
| `PlateIdFinder( const GPlatesModel::PropertyName &property_name_to_allow)` | constructor | `None` | public | — |
| `~PlateIdFinder()` | destructor | `None` | public | — |
| `add_property_name_to_allow( const GPlatesModel::PropertyName &property_name_to_allow)` | method | `void` | public | — |
| `visit_feature_handle( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | public | — |
| `visit_inline_property_container( const GPlatesModel::InlinePropertyContainer &inline_property_container)` | method | `void` | public | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | public | — |
| `visit_gpml_plate_id( const GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | public | — |
| `found_plate_ids_begin()` | method | `plate_id_container_const_iterator` | public | — |
| `found_plate_ids_end()` | method | `plate_id_container_const_iterator` | public | — |
| `clear_found_plate_ids()` | method | `void` | public | — |
| `d_property_names_to_allow` | field | `std::vector<GPlatesModel::PropertyName>` | private | — |
| `d_found_plate_ids` | field | `plate_id_container_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `contains_elem( const C &container, const E &elem)` | function | `bool` | — |
| `GPLATES_FEATUREVISITORS_PLATEIDFINDER_H` | macro | `None` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/deprecated/PlateIdFinder.h
python scripts/gpq.py def GPlatesFeatureVisitors::PlateIdFinder --body
python scripts/gpq.py uses PlateIdFinder --kind class
python scripts/gpq.py hier PlateIdFinder
```

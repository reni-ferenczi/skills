# GmlTimePeriodFinder

[Book TOC](../../../TOC.md) · [feature-visitors](../../../components/feature-visitors.md) · cluster Community 1139 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/deprecated/GmlTimePeriodFinder.h` | C++ | 110 |
| `src/feature-visitors/deprecated/GmlTimePeriodFinder.cc` | C++ | 84 |

## Overview

[[[PROSE overview unit=feature-visitors/deprecated/GmlTimePeriodFinder tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFeatureVisitors::GmlTimePeriodFinder`](#gplatesfeaturevisitorsgmltimeperiodfinder) | class | [`GPlatesModel::ConstFeatureVisitor`](../../model/FeatureVisitor.md) | — | 0 | This const feature visitor finds all gml:TimePeriods contained within the feature. |

## Members

### `GPlatesFeatureVisitors::GmlTimePeriodFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `time_period_container_type` | typedef | `std::vector<GPlatesPropertyValues::GmlTimePeriod::non_null_ptr_to_const_type>` | public | — |
| `time_period_container_const_iterator` | typedef | `time_period_container_type::const_iterator` | public | — |
| `GmlTimePeriodFinder()` | constructor | `None` | public | — |
| `GmlTimePeriodFinder( const GPlatesModel::PropertyName &property_name_to_allow)` | constructor | `None` | public | — |
| `~GmlTimePeriodFinder()` | destructor | `None` | public | — |
| `add_property_name_to_allow( const GPlatesModel::PropertyName &property_name_to_allow)` | method | `void` | public | — |
| `visit_feature_handle( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | public | — |
| `visit_inline_property_container( const GPlatesModel::InlinePropertyContainer &inline_property_container)` | method | `void` | public | — |
| `visit_gml_time_period( const GPlatesPropertyValues::GmlTimePeriod &gml_time_period)` | method | `void` | public | — |
| `found_time_periods_begin()` | method | `time_period_container_const_iterator` | public | — |
| `found_time_periods_end()` | method | `time_period_container_const_iterator` | public | — |
| `clear_found_time_periods()` | method | `void` | public | — |
| `d_property_names_to_allow` | field | `std::vector<GPlatesModel::PropertyName>` | private | — |
| `d_found_time_periods` | field | `time_period_container_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `contains_elem( const C &container, const E &elem)` | function | `bool` | — |
| `GPLATES_FEATUREVISITORS_GMLTIMEPERIODFINDER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=feature-visitors/deprecated/GmlTimePeriodFinder tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/deprecated/GmlTimePeriodFinder.h
python scripts/gpq.py def GPlatesFeatureVisitors::GmlTimePeriodFinder --body
python scripts/gpq.py uses GmlTimePeriodFinder --kind class
python scripts/gpq.py hier GmlTimePeriodFinder
```

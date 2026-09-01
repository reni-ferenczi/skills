# XsStringFinder

[Book TOC](../../../TOC.md) · [feature-visitors](../../../components/feature-visitors.md) · cluster Community 1140 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/deprecated/XsStringFinder.h` | C++ | 110 |
| `src/feature-visitors/deprecated/XsStringFinder.cc` | C++ | 84 |

## Overview

[[[PROSE overview unit=feature-visitors/deprecated/XsStringFinder tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFeatureVisitors::XsStringFinder`](#gplatesfeaturevisitorsxsstringfinder) | class | [`GPlatesModel::ConstFeatureVisitor`](../../model/FeatureVisitor.md) | — | 0 | This const feature visitor finds one or more string-valued properties contained within the feature. |

## Members

### `GPlatesFeatureVisitors::XsStringFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `string_container_type` | typedef | `std::vector<GPlatesPropertyValues::XsString::non_null_ptr_to_const_type>` | public | — |
| `string_container_const_iterator` | typedef | `string_container_type::const_iterator` | public | — |
| `XsStringFinder()` | constructor | `None` | public | FIXME: Add support to provide details of the desired codeSpace. |
| `XsStringFinder( const GPlatesModel::PropertyName &property_name_to_allow)` | constructor | `None` | public | — |
| `~XsStringFinder()` | destructor | `None` | public | — |
| `add_property_name_to_allow( const GPlatesModel::PropertyName &property_name_to_allow)` | method | `void` | public | — |
| `visit_feature_handle( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | public | — |
| `visit_inline_property_container( const GPlatesModel::InlinePropertyContainer &inline_property_container)` | method | `void` | public | — |
| `visit_xs_string( const GPlatesPropertyValues::XsString &xs_string)` | method | `void` | public | — |
| `found_strings_begin()` | method | `string_container_const_iterator` | public | — |
| `found_strings_end()` | method | `string_container_const_iterator` | public | — |
| `clear_found_strings()` | method | `void` | public | — |
| `d_property_names_to_allow` | field | `std::vector<GPlatesModel::PropertyName>` | private | — |
| `d_found_strings` | field | `string_container_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `contains_elem( const C &container, const E &elem)` | function | `bool` | — |
| `GPLATES_FEATUREVISITORS_XSSTRINGFINDER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=feature-visitors/deprecated/XsStringFinder tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/deprecated/XsStringFinder.h
python scripts/gpq.py def GPlatesFeatureVisitors::XsStringFinder --body
python scripts/gpq.py uses XsStringFinder --kind class
python scripts/gpq.py hier XsStringFinder
```

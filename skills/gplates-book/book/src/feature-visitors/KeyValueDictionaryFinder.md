# KeyValueDictionaryFinder

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 1234 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/KeyValueDictionaryFinder.h` | C++ | 107 |
| `src/feature-visitors/KeyValueDictionaryFinder.cc` | C++ | 73 |

## Overview

[[[PROSE overview unit=feature-visitors/KeyValueDictionaryFinder tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFeatureVisitors::KeyValueDictionaryFinder`](#gplatesfeaturevisitorskeyvaluedictionaryfinder) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | This const feature visitor finds key value dictionaries in the feature collection. |

## Members

### `GPlatesFeatureVisitors::KeyValueDictionaryFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `key_value_dictionary_container_type` | typedef | `std::vector<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type>` | public | — |
| `key_value_dictionary_container_const_iterator` | typedef | `key_value_dictionary_container_type::const_iterator` | public | — |
| `KeyValueDictionaryFinder()` | constructor | `None` | public | — |
| `KeyValueDictionaryFinder( const GPlatesModel::PropertyName &property_name_to_allow)` | constructor | `None` | public | — |
| `~KeyValueDictionaryFinder()` | destructor | `None` | public | — |
| `add_property_name_to_allow( const GPlatesModel::PropertyName &property_name_to_allow)` | method | `void` | public | — |
| `found_key_value_dictionaries_begin()` | method | `key_value_dictionary_container_const_iterator` | public | — |
| `found_key_value_dictionaries_end()` | method | `key_value_dictionary_container_const_iterator` | public | — |
| `number_of_found_dictionaries()` | method | `unsigned int` | public | — |
| `initialise_pre_property_values( const GPlatesModel::TopLevelPropertyInline &top_level_property_inline)` | method | `bool` | protected | — |
| `visit_gpml_key_value_dictionary( const GPlatesPropertyValues::GpmlKeyValueDictionary &gpml_key_value_dictionary)` | method | `void` | protected | — |
| `d_property_names_to_allow` | field | `std::vector<GPlatesModel::PropertyName>` | private | — |
| `d_found_key_value_dictionaries` | field | `key_value_dictionary_container_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `contains_elem( const C &container, const E &elem)` | function | `bool` | — |
| `GPLATES_FEATUREVISITORS_KEYVALUEDICTIONARYFINDER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=feature-visitors/KeyValueDictionaryFinder tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ShapefileAttributeViewerDialog](../qt-widgets/ShapefileAttributeViewerDialog.md) | qt-widgets | 17 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 16 |
| [api/PyFeature](../api/PyFeature.md) | api | 7 |
| [file-io/OgrFormatReconstructedFeatureGeometryExport](../file-io/OgrFormatReconstructedFeatureGeometryExport.md) | file-io | 4 |
| [file-io/OgrFormatResolvedTopologicalGeometryExport](../file-io/OgrFormatResolvedTopologicalGeometryExport.md) | file-io | 4 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/KeyValueDictionaryFinder.h
python scripts/gpq.py def GPlatesFeatureVisitors::KeyValueDictionaryFinder --body
python scripts/gpq.py uses KeyValueDictionaryFinder --kind class
python scripts/gpq.py hier KeyValueDictionaryFinder
```

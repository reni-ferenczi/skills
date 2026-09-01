# ShapefileAttributeFinder

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 893 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/ShapefileAttributeFinder.h` | C++ | 166 |
| `src/feature-visitors/ShapefileAttributeFinder.cc` | C++ | 143 |

## Overview

`ShapefileAttributeFinder` locates one named attribute inside a feature's imported shapefile attributes and returns its value(s) as `QVariant`s, for readers that display or export shapefile-derived data (`OgrReader`, `PyFeature`, `DataMiningUtils`). Unlike `GeometryFinder` and `KeyValueDictionaryFinder`, it does not take a configurable property-name allow-list: `initialise_pre_property_values()` hardcodes the property name `"shapefileAttributes"`, so it only ever looks inside that one `GpmlKeyValueDictionary` property, then scans its elements for the requested key via `find_shapefile_attribute_in_element()`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFeatureVisitors::ShapefileAttributeFinder`](#gplatesfeaturevisitorsshapefileattributefinder) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | The ToQvariantConverter feature-visitor is used to locate specific property values within a Feature and convert them to QVariants, if possible. |

## Members

### `GPlatesFeatureVisitors::ShapefileAttributeFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `qvariant_container_type` | typedef | `std::vector<QVariant>` | public | — |
| `qvariant_container_const_iterator` | typedef | `qvariant_container_type::const_iterator` | public | — |
| `ShapefileAttributeFinder( const QString attribute_name)` | constructor | `None` | public | — |
| `~ShapefileAttributeFinder()` | destructor | `None` | public | — |
| `found_qvariants_begin()` | method | `qvariant_container_const_iterator` | public | — |
| `found_qvariants_end()` | method | `qvariant_container_const_iterator` | public | — |
| `clear_found_qvariants()` | method | `void` | public | — |
| `initialise_pre_property_values( const GPlatesModel::TopLevelPropertyInline &top_level_property_inline)` | method | `bool` | protected | — |
| `visit_gml_time_instant( const GPlatesPropertyValues::GmlTimeInstant &gml_time_instant)` | method | `void` | protected | — |
| `visit_gml_time_period( const GPlatesPropertyValues::GmlTimePeriod &gml_time_period)` | method | `void` | protected | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | protected | — |
| `visit_gpml_key_value_dictionary( const GPlatesPropertyValues::GpmlKeyValueDictionary &dictionary)` | method | `void` | protected | — |
| `visit_gpml_plate_id( const GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | protected | — |
| `visit_gpml_polarity_chron_id( const GPlatesPropertyValues::GpmlPolarityChronId &gpml_polarity_chron_id)` | method | `void` | protected | — |
| `visit_gpml_measure( const GPlatesPropertyValues::GpmlMeasure &gpml_measure)` | method | `void` | protected | — |
| `visit_xs_boolean( const GPlatesPropertyValues::XsBoolean &xs_boolean)` | method | `void` | protected | — |
| `visit_xs_double( const GPlatesPropertyValues::XsDouble &xs_double)` | method | `void` | protected | — |
| `visit_xs_integer( const GPlatesPropertyValues::XsInteger& xs_integer)` | method | `void` | protected | — |
| `visit_xs_string( const GPlatesPropertyValues::XsString &xs_string)` | method | `void` | protected | — |
| `find_shapefile_attribute_in_element( const GPlatesPropertyValues::GpmlKeyValueDictionaryElement &element)` | method | `void` | private | — |
| `d_attribute_name` | field | `QString` | private | — |
| `d_found_qvariants` | field | `qvariant_container_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `contains_elem( const C &container, const E &elem)` | function | `bool` | — |
| `GPLATES_FEATUREVISITORS_SHAPEFILEATTRIBUTEFINDER_H` | macro | `None` | — |

## Notes

Only `XsBoolean`, `XsDouble`, `XsInteger` and `XsString` dictionary values are actually converted; the overrides for `GmlTimeInstant`/`GmlTimePeriod`, `GpmlConstantValue`, `GpmlPlateId`, `GpmlPolarityChronId` and `GpmlMeasure` are wrapped in `#if 0` in the header itself, so despite appearing in the member list they are not compiled in — a matching attribute of one of those types is silently skipped rather than converted.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 77 |
| [api/PyFeature](../api/PyFeature.md) | api | 10 |
| [data-mining/DataMiningUtils](../data-mining/DataMiningUtils.md) | data-mining | 8 |
| [data-mining/deprecated/DataOperator](../data-mining/deprecated/DataOperator.md) | data-mining | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/ShapefileAttributeFinder.h
python scripts/gpq.py def GPlatesFeatureVisitors::ShapefileAttributeFinder --body
python scripts/gpq.py uses ShapefileAttributeFinder --kind class
python scripts/gpq.py hier ShapefileAttributeFinder
```

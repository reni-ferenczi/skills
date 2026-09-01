# GpmlHotSpotTrailMark

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 681 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlHotSpotTrailMark.h` | C++ | 288 |
| `src/property-values/GpmlHotSpotTrailMark.cc` | C++ | 128 |

## Overview

[[[PROSE overview unit=property-values/GpmlHotSpotTrailMark tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlHotSpotTrailMark`](#gplatespropertyvaluesgpmlhotspottrailmark) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::GpmlHotSpotTrailMark`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlHotSpotTrailMark>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlHotSpotTrailMark\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlHotSpotTrailMark>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlHotSpotTrailMark\>. |
| `~GpmlHotSpotTrailMark()` | destructor | `None` | public | — |
| `create( const GmlPoint::non_null_ptr_type &position_, const boost::optional<GpmlMeasure::non_null_ptr_type> &trail_width_, const boost::optional<GmlTimeInstant::non_null_ptr_type> &measured_age_, const boost::optional<GmlTimePeriod::non_null_ptr_type> &measured_age_range_)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `position()` | method | `GmlPoint::non_null_ptr_to_const_type` | public | — |
| `set_position( GmlPoint::non_null_ptr_type pos)` | method | `void` | public | Sets the internal position. |
| `trail_width()` | method | `boost::optional<GpmlMeasure::non_null_ptr_type>` | public | — |
| `set_trail_width( GpmlMeasure::non_null_ptr_type tw)` | method | `void` | public | Sets the internal trail width. |
| `measured_age()` | method | `boost::optional<GmlTimeInstant::non_null_ptr_type>` | public | — |
| `set_measured_age( GmlTimeInstant::non_null_ptr_type ti)` | method | `void` | public | Sets the internal measured age. |
| `measured_age_range()` | method | `boost::optional<GmlTimePeriod::non_null_ptr_type>` | public | — |
| `set_measured_age_range( GmlTimePeriod::non_null_ptr_type tp)` | method | `void` | public | Sets the internal measured age range. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `directly_modifiable_fields_equal( const PropertyValue &other)` | method | `bool` | protected | — |
| `GpmlHotSpotTrailMark( const GmlPoint::non_null_ptr_type &position_, const boost::optional<GpmlMeasure::non_null_ptr_type> &trail_width_, const boost::optional<GmlTimeInstant::non_null_ptr_type> &measured_age_, const boost::optional<GmlTimePeriod::non_null_ptr_type> &measured_age_range_)` | constructor | `None` | protected | — |
| `GpmlHotSpotTrailMark( const GpmlHotSpotTrailMark &other)` | constructor | `None` | protected | — |
| `operator=` | field | `GpmlPlateId` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |
| `d_position` | field | `GmlPoint::non_null_ptr_type` | private | — |
| `d_trail_width` | field | `boost::optional<GpmlMeasure::non_null_ptr_type>` | private | — |
| `d_measured_age` | field | `boost::optional<GmlTimeInstant::non_null_ptr_type>` | private | — |
| `d_measured_age_range` | field | `boost::optional<GmlTimePeriod::non_null_ptr_type>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `opt_eq( const boost::optional<T> &opt1, const boost::optional<T> &opt2)` | function | `bool` | — |
| `GPLATES_PROPERTYVALUES_GPMLHOTSPOTTRAILMARK_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/GpmlHotSpotTrailMark tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 8 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 8 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 3 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlHotSpotTrailMark.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlHotSpotTrailMark --body
python scripts/gpq.py uses GpmlHotSpotTrailMark --kind class
python scripts/gpq.py hier GpmlHotSpotTrailMark
```

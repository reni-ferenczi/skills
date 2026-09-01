# ToQvariantConverter

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 404 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/ToQvariantConverter.h` | C++ | 245 |
| `src/feature-visitors/ToQvariantConverter.cc` | C++ | 330 |

## Overview

[[[PROSE overview unit=feature-visitors/ToQvariantConverter tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFeatureVisitors::ToQvariantConverter`](#gplatesfeaturevisitorstoqvariantconverter) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | The ToQvariantConverter feature-visitor is used to locate specific property values within a Feature and convert them to QVariants, if possible. |

## Members

### `GPlatesFeatureVisitors::ToQvariantConverter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `qvariant_container_type` | typedef | `std::vector<QVariant>` | public | — |
| `qvariant_container_const_iterator` | typedef | `qvariant_container_type::const_iterator` | public | — |
| `ToQvariantConverter()` | constructor | `None` | public | FIXME: We should also pass the current reconstruction time, so we can correctly handle time-dependent property values. |
| `~ToQvariantConverter()` | destructor | `None` | public | — |
| `set_desired_role( int role)` | method | `void` | public | The ToQvariantConverter defaults to Qt::DisplayRole, for returning QVariants suitable for display purposes (e.g. formatted strings or simple numbers). |
| `found_values_begin()` | method | `qvariant_container_const_iterator` | public | — |
| `found_values_end()` | method | `qvariant_container_const_iterator` | public | — |
| `clear_found_values()` | method | `void` | public | — |
| `found_time_dependencies_begin()` | method | `qvariant_container_const_iterator` | public | — |
| `found_time_dependencies_end()` | method | `qvariant_container_const_iterator` | public | — |
| `clear_found_time_dependencies()` | method | `void` | public | — |
| `visit_enumeration( const GPlatesPropertyValues::Enumeration &enumeration)` | method | `void` | protected | — |
| `visit_gml_time_instant( const GPlatesPropertyValues::GmlTimeInstant &gml_time_instant)` | method | `void` | protected | — |
| `visit_gml_time_period( const GPlatesPropertyValues::GmlTimePeriod &gml_time_period)` | method | `void` | protected | — |
| `visit_gpml_age( const GPlatesPropertyValues::GpmlAge &gpml_age)` | method | `void` | protected | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | protected | — |
| `visit_gpml_plate_id( const GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | protected | — |
| `visit_gpml_polarity_chron_id( const GPlatesPropertyValues::GpmlPolarityChronId &gpml_polarity_chron_id)` | method | `void` | protected | — |
| `visit_gpml_measure( const GPlatesPropertyValues::GpmlMeasure &gpml_measure)` | method | `void` | protected | — |
| `visit_gpml_old_plates_header( const GPlatesPropertyValues::GpmlOldPlatesHeader &gpml_old_plates_header)` | method | `void` | protected | — |
| `visit_uninterpreted_property_value( const GPlatesPropertyValues::UninterpretedPropertyValue &uninterpreted_prop_val)` | method | `void` | protected | — |
| `visit_xs_boolean( const GPlatesPropertyValues::XsBoolean &xs_boolean)` | method | `void` | protected | — |
| `visit_xs_double( const GPlatesPropertyValues::XsDouble &xs_double)` | method | `void` | protected | — |
| `visit_xs_integer( const GPlatesPropertyValues::XsInteger& xs_integer)` | method | `void` | protected | — |
| `visit_xs_string( const GPlatesPropertyValues::XsString &xs_string)` | method | `void` | protected | — |
| `d_found_values` | field | `qvariant_container_type` | private | A sequence of values that the ToQvariantConverter has encountered, converted to QVariants where possible. |
| `d_found_time_dependencies` | field | `qvariant_container_type` | private | A sequence of TimeDependentPropertyValues that the ToQvariantConverter has encountered, represented as QVariants. |
| `d_role` | field | `int` | private | The role that is to be used for the returned QVariant. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `contains_elem( const C &container, const E &elem)` | function | `bool` | — |
| `geo_time_instant_to_qvariant( const GPlatesPropertyValues::GeoTimeInstant &time_position, int role)` | function | `QVariant` | — |
| `stringify( const QString &q_str)` | function | `QString` | — |
| `stringify( const double &dbl)` | function | `QString` | — |
| `stringify( const GPlatesUtils::UnicodeString &uni_str)` | function | `QString` | — |
| `stringify( const GPlatesModel::StringContentTypeGenerator<T> &stringcontent)` | function | `QString` | — |
| `stringify( const boost::optional<T> &optional_thing)` | function | `QString` | You know what C++ really needs? |
| `GPLATES_FEATUREVISITORS_TOQVARIANTCONVERTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=feature-visitors/ToQvariantConverter tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FeaturePropertyTableModel](../gui/FeaturePropertyTableModel.md) | gui | 23 |
| [utils/deprecated/FeatureHandleToOldId](../utils/deprecated/FeatureHandleToOldId.md) | utils | 6 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 5 |
| [qt-widgets/CreateFeaturePropertiesPage](../qt-widgets/CreateFeaturePropertiesPage.md) | qt-widgets | 5 |
| [qt-widgets/ShapefileAttributeViewerDialog](../qt-widgets/ShapefileAttributeViewerDialog.md) | qt-widgets | 3 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 1 |
| [file-io/OgrWriter](../file-io/OgrWriter.md) | file-io | 1 |
| [qt-widgets/EditShapefileAttributesWidget](../qt-widgets/EditShapefileAttributesWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/ToQvariantConverter.h
python scripts/gpq.py def GPlatesFeatureVisitors::ToQvariantConverter --body
python scripts/gpq.py uses ToQvariantConverter --kind class
python scripts/gpq.py hier ToQvariantConverter
```

# EditWidgetChooser

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 558 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditWidgetChooser.h` | C++ | 210 |
| `src/qt-widgets/EditWidgetChooser.cc` | C++ | 275 |

## Overview

[[[PROSE overview unit=qt-widgets/EditWidgetChooser tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::EditWidgetChooser`](#gplatesqtwidgetseditwidgetchooser) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | The EditWidgetChooser feature-visitor is used to help identify a widget suitable for editing a given property value (or given a feature reference and a property name) It is used by an EditWidgetGroupBox. |

## Members

### `GPlatesQtWidgets::EditWidgetChooser`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `qvariant_container_type` | typedef | `std::vector<QVariant>` | public | — |
| `EditWidgetChooser( GPlatesQtWidgets::EditWidgetGroupBox &edit_widget_group_box)` | constructor | `None` | public | FIXME: We should also pass the current reconstruction time, so we can correctly handle time-dependent property values. |
| `EditWidgetChooser( GPlatesQtWidgets::EditWidgetGroupBox &edit_widget_group_box, const GPlatesModel::PropertyName &property_name_to_allow)` | constructor | `None` | public | — |
| `~EditWidgetChooser()` | destructor | `None` | public | — |
| `add_property_name_to_allow( const GPlatesModel::PropertyName &property_name_to_allow)` | method | `void` | public | — |
| `initialise_pre_property_values( GPlatesModel::TopLevelPropertyInline &top_level_property_inline)` | method | `bool` | protected | — |
| `visit_enumeration( GPlatesPropertyValues::Enumeration &enumeration)` | method | `void` | protected | — |
| `visit_gml_line_string( GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | protected | — |
| `visit_gml_multi_point( GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | protected | — |
| `visit_gml_orientable_curve( GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | protected | — |
| `visit_gml_point( GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | protected | — |
| `visit_gml_polygon( GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | protected | — |
| `visit_gml_time_instant( GPlatesPropertyValues::GmlTimeInstant &gml_time_instant)` | method | `void` | protected | — |
| `visit_gml_time_period( GPlatesPropertyValues::GmlTimePeriod &gml_time_period)` | method | `void` | protected | — |
| `visit_gpml_age( GPlatesPropertyValues::GpmlAge &gpml_age)` | method | `void` | protected | — |
| `visit_gpml_array( GPlatesPropertyValues::GpmlArray &gpml_array)` | method | `void` | protected | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | protected | — |
| `visit_gpml_irregular_sampling( GPlatesPropertyValues::GpmlIrregularSampling &gpml_irregular_sampling)` | method | `void` | protected | — |
| `visit_gpml_key_value_dictionary( GPlatesPropertyValues::GpmlKeyValueDictionary &gpml_key_value_dictionary)` | method | `void` | protected | — |
| `visit_gpml_plate_id( GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | protected | — |
| `visit_gpml_polarity_chron_id( GPlatesPropertyValues::GpmlPolarityChronId &gpml_polarity_chron_id)` | method | `void` | protected | — |
| `visit_gpml_measure( GPlatesPropertyValues::GpmlMeasure &gpml_measure)` | method | `void` | protected | — |
| `visit_gpml_old_plates_header( GPlatesPropertyValues::GpmlOldPlatesHeader &gpml_old_plates_header)` | method | `void` | protected | — |
| `visit_gpml_string_list( GPlatesPropertyValues::GpmlStringList &gpml_string_list)` | method | `void` | protected | — |
| `visit_xs_boolean( GPlatesPropertyValues::XsBoolean &xs_boolean)` | method | `void` | protected | — |
| `visit_xs_double( GPlatesPropertyValues::XsDouble &xs_double)` | method | `void` | protected | — |
| `visit_xs_integer( GPlatesPropertyValues::XsInteger& xs_integer)` | method | `void` | protected | — |
| `visit_xs_string( GPlatesPropertyValues::XsString &xs_string)` | method | `void` | protected | — |
| `d_edit_widget_group_box_ptr` | field | `GPlatesQtWidgets::EditWidgetGroupBox` | private | — |
| `d_property_names_to_allow` | field | `std::vector<GPlatesModel::PropertyName>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `contains_elem( const C &container, const E &elem)` | function | `bool` | — |
| `GPLATES_QTWIDGETS_EDITWIDGETCHOOSER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/EditWidgetChooser tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditWidgetGroupBox](EditWidgetGroupBox.md) | qt-widgets | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditWidgetChooser.h
python scripts/gpq.py def GPlatesQtWidgets::EditWidgetChooser --body
python scripts/gpq.py uses EditWidgetChooser --kind class
python scripts/gpq.py hier EditWidgetChooser
```

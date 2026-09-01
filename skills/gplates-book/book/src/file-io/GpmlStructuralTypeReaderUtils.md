# GpmlStructuralTypeReaderUtils

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 73 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GpmlStructuralTypeReaderUtils.h` | C++ | 742 |
| `src/file-io/GpmlStructuralTypeReaderUtils.cc` | C++ | 1789 |

## Overview

[[[PROSE overview unit=file-io/GpmlStructuralTypeReaderUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::ValueObjectTemplateVisitor`](#anonymousvalueobjecttemplatevisitor) | class | [`GPlatesModel::XmlNodeVisitor`](../model/XmlNode.md) | — | 0 | — |
| [`GPlatesFileIO::GpmlStructuralTypeReaderUtils::xml_attributes_type`](#gplatesfileiogpmlstructuraltypereaderutilsxml_attributes_type) | typedef | — | — | 0 | — |
| [`GPlatesFileIO::GpmlStructuralTypeReaderUtils::value_component_type`](#gplatesfileiogpmlstructuraltypereaderutilsvalue_component_type) | typedef | — | — | 0 | — |
| [`GPlatesFileIO::GpmlStructuralTypeReaderUtils::composite_value_type`](#gplatesfileiogpmlstructuraltypereaderutilscomposite_value_type) | typedef | — | — | 0 | — |
| [`GPlatesFileIO::GpmlStructuralTypeReaderUtils::coordinate_list_type`](#gplatesfileiogpmlstructuraltypereaderutilscoordinate_list_type) | typedef | — | — | 0 | — |

## Members

### `(anonymous)::ValueObjectTemplateVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit_text_node( const GPlatesModel::XmlTextNode::non_null_ptr_type &text)` | method | `void` | public | — |
| `visit_element_node( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem)` | method | `void` | public | — |
| `d_result` | field | `boost::optional<GPlatesFileIO::GpmlStructuralTypeReaderUtils::value_component_type>` | private | — |

### `GPlatesFileIO::GpmlStructuralTypeReaderUtils::xml_attributes_type`

*None.*

### `GPlatesFileIO::GpmlStructuralTypeReaderUtils::value_component_type`

*None.*

### `GPlatesFileIO::GpmlStructuralTypeReaderUtils::composite_value_type`

*None.*

### `GPlatesFileIO::GpmlStructuralTypeReaderUtils::coordinate_list_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `EXCEPTION_SOURCE` | macro | `BOOST_CURRENT_FUNCTION` | — |
| `parse_integral_value( T (QString::*parse_func)(bool *, int) const, const QString &str, T &out)` | function | `bool` | — |
| `parse_decimal_value( T (QString::*parse_func)(bool *) const, const QString &str, T &out)` | function | `bool` | — |
| `estimate_number_of_points( const QString &str)` | function | `size_t` | — |
| `create_point( const GPlatesModel::XmlElementNode::non_null_ptr_type &parent, PointType (*create_pos_fn)( const GPlatesModel::XmlElementNode::non_null_ptr_type &, const GPlatesModel::GpgimVersion &, GPlatesFileIO::ReadErrorAccumulation &), PointType (*create_coordinates_fn)( const GPlatesModel::XmlElementNode::non_null_ ...` | function | `std::pair<PointType, GPlatesPropertyValues::GmlPoint::GmlProperty>` | Common code used by 'create\_point\_on\_sphere()', 'create\_lon\_lat\_point\_on\_sphere' and 'create\_point\_2d'. |
| `GPLATES_FILEIO_GPMLSTRUCTURALTYPEREADERUTILS_H` | macro | `None` | — |
| `create_feature_id( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesModel::FeatureId` | — |
| `create_revision_id( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesModel::RevisionId` | — |
| `create_gml_composite_value( const GPlatesModel::XmlElementNode::non_null_ptr_type &parent, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `composite_value_type` | Create a gml:CompositeValue structural type consisting of a sequence of 'gml:valueComponent's. |
| `create_gml_grid_envelope( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GmlGridEnvelope::non_null_ptr_type` | — |
| `create_gml_value_component( const GPlatesModel::XmlElementNode::non_null_ptr_type &parent, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `value_component_type` | Extracts out the value object template, i.e. the app:Temperature part of the example on p.253 of the GML book. |
| `create_gpml_finite_rotation_slerp( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlFiniteRotationSlerp::non_null_ptr_type` | — |
| `create_gpml_interpolation_function( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlInterpolationFunction::non_null_ptr_type` | — |
| `create_gpml_key_value_dictionary_element( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GpmlPropertyStructuralTypeReader &structural_type_reader, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlKeyValueDictionaryElement` | — |
| `create_gpml_property_delegate( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlPropertyDelegate::non_null_ptr_type` | — |
| `create_gpml_time_dependent_property_value( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GpmlPropertyStructuralTypeReader &structural_type_reader, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesModel::PropertyValue::non_null_ptr_type` | — |
| `create_gpml_time_sample( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GpmlPropertyStructuralTypeReader &structural_type_reader, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlTimeSample` | — |
| `create_gpml_time_window( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GpmlPropertyStructuralTypeReader &structural_type_reader, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlTimeWindow` | — |
| `create_gpml_topological_network_interior( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlPropertyDelegate::non_null_ptr_type` | — |
| `create_gpml_topological_line_section( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlTopologicalLineSection::non_null_ptr_type` | — |
| `create_gpml_topological_point( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlTopologicalPoint::non_null_ptr_type` | — |
| `create_gpml_topological_section( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlTopologicalSection::non_null_ptr_type` | — |
| `get_structural_type_element( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::XmlElementName &xml_element_name)` | function | `GPlatesModel::XmlElementNode::non_null_ptr_type` | This function will extract the single child of the given elem and return it. |
| `create_template_type_parameter_type( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::StructuralType` | Retrieve the qualified template type. |
| `get_xml_attributes_from_child( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::XmlElementName &xml_element_name)` | function | `xml_attributes_type` | — |
| `find_optional( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::XmlElementName &xml_element_name, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `boost::optional<GPlatesModel::XmlElementNode::non_null_ptr_type>` | — |
| `find_and_create_optional( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, T (*creation_fn)( const GPlatesModel::XmlElementNode::non_null_ptr_type &, const GPlatesModel::GpgimVersion &, GPlatesFileIO::ReadErrorAccumulation &), const GPlatesModel::XmlElementName &xml_element_name, const GPlatesModel::GpgimVe ...` | function | `boost::optional<T>` | — |
| `find_and_create_optional( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, T (*creation_fn)( const GPlatesModel::XmlElementNode::non_null_ptr_type &, const GPlatesFileIO::GpmlPropertyStructuralTypeReader &, const GPlatesModel::GpgimVersion &, GPlatesFileIO::ReadErrorAccumulation &), const GPlatesModel::XmlE ...` | function | `boost::optional<T>` | — |
| `find_one( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::XmlElementName &xml_element_name, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `GPlatesModel::XmlElementNode::non_null_ptr_type` | — |
| `find_and_create_one( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, T (*creation_fn)( const GPlatesModel::XmlElementNode::non_null_ptr_type &, const GPlatesModel::GpgimVersion &, GPlatesFileIO::ReadErrorAccumulation &), const GPlatesModel::XmlElementName &xml_element_name, const GPlatesModel::GpgimVersion ...` | function | `T` | — |
| `find_and_create_one( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, T (*creation_fn)( const GPlatesModel::XmlElementNode::non_null_ptr_type &, const GPlatesFileIO::GpmlPropertyStructuralTypeReader &, const GPlatesModel::GpgimVersion &, GPlatesFileIO::ReadErrorAccumulation &), const GPlatesModel::XmlElemen ...` | function | `T` | — |
| `find_zero_or_more( std::vector<GPlatesModel::XmlElementNode::non_null_ptr_type> &targets, const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::XmlElementName &xml_element_name, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `void` | — |
| `find_and_create_zero_or_more( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, T (*creation_fn)( const GPlatesModel::XmlElementNode::non_null_ptr_type &, const GPlatesModel::GpgimVersion &, GPlatesFileIO::ReadErrorAccumulation &), const GPlatesModel::XmlElementName &xml_element_name, CollectionOfT &destinat ...` | function | `void` | — |
| `find_and_create_zero_or_more( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, T (*creation_fn)( const GPlatesModel::XmlElementNode::non_null_ptr_type &, const GPlatesFileIO::GpmlPropertyStructuralTypeReader &, const GPlatesModel::GpgimVersion &, GPlatesFileIO::ReadErrorAccumulation &), const GPlatesModel:: ...` | function | `void` | — |
| `find_one_or_more( std::vector<GPlatesModel::XmlElementNode::non_null_ptr_type> &targets, const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::XmlElementName &xml_element_name, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `void` | — |
| `find_and_create_one_or_more( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, T (*creation_fn)( const GPlatesModel::XmlElementNode::non_null_ptr_type &, const GPlatesModel::GpgimVersion &, GPlatesFileIO::ReadErrorAccumulation &), const GPlatesModel::XmlElementName &xml_element_name, CollectionOfT &destinati ...` | function | `void` | — |
| `find_and_create_one_or_more( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, T (*creation_fn)( const GPlatesModel::XmlElementNode::non_null_ptr_type &, const GPlatesFileIO::GpmlPropertyStructuralTypeReader &, const GPlatesModel::GpgimVersion &, GPlatesFileIO::ReadErrorAccumulation &), const GPlatesModel::X ...` | function | `void` | — |
| `find_and_create_from_type( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesPropertyValues::StructuralType &type, const GPlatesModel::XmlElementName &xml_element_name, const GPlatesFileIO::GpmlPropertyStructuralTypeReader &structural_type_reader, const GPlatesModel::GpgimVersion &gpml_version, ...` | function | `GPlatesModel::PropertyValue::non_null_ptr_type` | — |
| `find_and_create_one_or_more_from_type( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesPropertyValues::StructuralType &type, const GPlatesModel::XmlElementName &xml_element_name, std::vector<GPlatesModel::PropertyValue::non_null_ptr_type> &members, const GPlatesFileIO::GpmlPropertyStructuralTy ...` | function | `void` | — |
| `create_string_without_trimming( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `QString` | — |
| `create_string( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `QString` | — |
| `create_nonempty_string( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `QString` | — |
| `create_unicode_string( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `GPlatesUtils::UnicodeString` | — |
| `create_boolean( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `bool` | — |
| `create_double( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `double` | — |
| `create_double_list( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `std::vector<double>` | — |
| `create_ulong( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `unsigned long` | — |
| `create_int( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `int` | — |
| `create_int_list( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `std::vector<int>` | — |
| `create_uint( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `unsigned int` | — |
| `create_pos( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `GPlatesMaths::PointOnSphere` | — |
| `create_lon_lat_pos( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `std::pair<double/*lon*/, double/*lat*/>` | Similar to create\_pos but returns it as (lon, lat) pair. |
| `create_pos_2d( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `std::pair<double, double>` | Similar to create\_lon\_lat\_pos but does not assume the position is latitude/longitude and does not check position is in a valid latitude/longitude range. |
| `create_coordinates( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `GPlatesMaths::PointOnSphere` | The same as create\_pos, except that there's a comma between the two values instead of whitespace. |
| `create_lon_lat_coordinates( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `std::pair<double/*lon*/, double/*lat*/>` | Similar to create\_coordinates but returns it as (lon, lat) pair. |
| `create_coordinates_2d( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `std::pair<double, double>` | Similar to create\_lon\_lat\_coordinates but does not assume the position is latitude/longitude and does not check position is in a valid latitude/longitude range. |
| `create_polyline( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | — |
| `create_polygon_ring( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `boost::shared_ptr< std::vector<GPlatesMaths::PointOnSphere> >` | — |
| `create_linear_ring( const GPlatesModel::XmlElementNode::non_null_ptr_type &parent, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `boost::shared_ptr< std::vector<GPlatesMaths::PointOnSphere> >` | This function is used by create\_gml\_polygon to traverse the LinearRing intermediate junk. |
| `create_point_on_sphere( const GPlatesModel::XmlElementNode::non_null_ptr_type &parent, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `std::pair<GPlatesMaths::PointOnSphere, GPlatesPropertyValues::GmlPoint::GmlProperty>` | This function is used by create\_gml\_point and create\_gml\_multi\_point to do the common work of creating a GPlatesMaths::PointOnSphere. |
| `create_lon_lat_point_on_sphere( const GPlatesModel::XmlElementNode::non_null_ptr_type &parent, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `std::pair<std::pair<double/*lon*/, double/*lat*/>, GPlatesPropertyValues::GmlPoint::GmlProperty>` | Similar to create\_point\_on\_sphere but returns it as (lon, lat) pair. |
| `create_point_2d( const GPlatesModel::XmlElementNode::non_null_ptr_type &parent, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `std::pair<std::pair<double, double>, GPlatesPropertyValues::GmlPoint::GmlProperty>` | Similar to create\_lon\_lat\_point\_on\_sphere but does not assume the position is latitude/longitude and does not check position is in a valid latitude/longitude range. |
| `create_geo_time_instant( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GeoTimeInstant` | — |
| `create_topological_sections( const GPlatesModel::XmlElementNode::non_null_ptr_type &parent, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `std::vector<GPlatesPropertyValues::GpmlTopologicalSection::non_null_ptr_type>` | This function is to traverse a 'gpml:TopologicalSections' intermediate XML element. |
| `create_tuple_list( const GPlatesModel::XmlElementNode::non_null_ptr_type &parent, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `std::vector<coordinate_list_type>` | Extracts a sequence of coordinate lists of doubles (one list per tuple element). |

## Notes

[[[PROSE notes unit=file-io/GpmlStructuralTypeReaderUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlPropertyStructuralTypeReaderUtils](GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 160 |
| [file-io/GpmlUpgradeReaderUtils](GpmlUpgradeReaderUtils.md) | file-io | 7 |
| [file-io/GpmlFeatureReaderImpl](GpmlFeatureReaderImpl.md) | file-io | 5 |
| [file-io/GpmlPropertyReader](GpmlPropertyReader.md) | file-io | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GpmlStructuralTypeReaderUtils.h
python scripts/gpq.py def (anonymous)::ValueObjectTemplateVisitor --body
python scripts/gpq.py uses ValueObjectTemplateVisitor --kind class
python scripts/gpq.py hier ValueObjectTemplateVisitor
```

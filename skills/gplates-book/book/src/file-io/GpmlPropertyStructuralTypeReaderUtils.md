# GpmlPropertyStructuralTypeReaderUtils

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 313 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GpmlPropertyStructuralTypeReaderUtils.h` | C++ | 398 |
| `src/file-io/GpmlPropertyStructuralTypeReaderUtils.cc` | C++ | 1243 |

## Overview

[[[PROSE overview unit=file-io/GpmlPropertyStructuralTypeReaderUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `EXCEPTION_SOURCE` | macro | `BOOST_CURRENT_FUNCTION` | — |
| `to_optional_of_ptr_to_const( const boost::optional<GPlatesUtils::non_null_intrusive_ptr<T> > &opt)` | function | `boost::optional<GPlatesUtils::non_null_intrusive_ptr<const T> >` | — |
| `get_attribute_as_double( GPlatesModel::XmlElementNode::non_null_ptr_to_const_type elem, const GPlatesModel::XmlAttributeName &attr_name)` | function | `boost::optional<double>` | Given an XML element and attribute name, look for that attribute and attempt to convert it to a double. |
| `get_attribute_as_qstring( GPlatesModel::XmlElementNode::non_null_ptr_to_const_type elem, const GPlatesModel::XmlAttributeName &attr_name)` | function | `boost::optional<QString>` | Given an XML element and attribute name, look for that attribute and return it as a QString. |
| `GPLATES_FILEIO_GPMLPROPERTYSTRUCTURALTYPEREADERUTILS_H` | macro | `None` | — |
| `create_xs_boolean( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::XsBoolean::non_null_ptr_type` | — |
| `create_xs_double( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::XsDouble::non_null_ptr_type` | — |
| `create_xs_integer( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::XsInteger::non_null_ptr_type` | — |
| `create_xs_string( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::XsString::non_null_ptr_type` | — |
| `create_gml_data_block( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GmlDataBlock::non_null_ptr_type` | — |
| `create_gml_file( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GmlFile::non_null_ptr_type` | — |
| `create_gml_line_string( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GmlLineString::non_null_ptr_type` | — |
| `create_gml_multi_point( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GmlMultiPoint::non_null_ptr_type` | — |
| `create_gml_orientable_curve( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GmlOrientableCurve::non_null_ptr_type` | — |
| `create_gml_point( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GmlPoint::non_null_ptr_type` | — |
| `create_gml_polygon( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GmlPolygon::non_null_ptr_type` | — |
| `create_gml_rectified_grid( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GmlRectifiedGrid::non_null_ptr_type` | — |
| `create_gml_time_instant( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GmlTimeInstant::non_null_ptr_type` | — |
| `create_gml_time_period( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GmlTimePeriod::non_null_ptr_type` | — |
| `create_gpml_age( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlAge::non_null_ptr_type` | — |
| `create_gpml_array( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GpmlPropertyStructuralTypeReader &structural_type_reader, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlArray::non_null_ptr_type` | — |
| `create_gpml_constant_value( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GpmlPropertyStructuralTypeReader &structural_type_reader, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlConstantValue::non_null_ptr_type` | — |
| `create_gpml_enumeration( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimEnumerationType &gpgim_property_enumeration_type, const GPlatesModel::GpgimVersion &gpml_version, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::Enumeration::non_null_ptr_type` | Reads the enumeration of the type specified by gpgim\_property\_enumeration\_type. |
| `create_gpml_feature_reference( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlFeatureReference::non_null_ptr_type` | — |
| `create_gpml_feature_snapshot_reference( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlFeatureSnapshotReference::non_null_ptr_type` | — |
| `create_gpml_finite_rotation( GPlatesModel::XmlElementNode::non_null_ptr_type elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlFiniteRotation::non_null_ptr_type` | — |
| `create_gpml_hot_spot_trail_mark( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlHotSpotTrailMark::non_null_ptr_type` | — |
| `create_gpml_irregular_sampling( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GpmlPropertyStructuralTypeReader &structural_type_reader, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlIrregularSampling::non_null_ptr_type` | — |
| `create_gpml_key_value_dictionary( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GpmlPropertyStructuralTypeReader &structural_type_reader, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type` | — |
| `create_gpml_measure( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlMeasure::non_null_ptr_type` | — |
| `create_gpml_metadata( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlMetadata::non_null_ptr_type` | — |
| `create_gpml_old_plates_header( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type` | — |
| `create_gpml_piecewise_aggregation( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GpmlPropertyStructuralTypeReader &structural_type_reader, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlPiecewiseAggregation::non_null_ptr_type` | — |
| `create_gpml_plate_id( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlPlateId::non_null_ptr_type` | — |
| `create_gpml_polarity_chron_id( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlPolarityChronId::non_null_ptr_type` | — |
| `create_gpml_raster_band_names( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlRasterBandNames::non_null_ptr_type` | — |
| `create_gpml_revision_id( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlRevisionId::non_null_ptr_type` | — |
| `create_gpml_scalar_field_3d_file( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlScalarField3DFile::non_null_ptr_type` | — |
| `create_gpml_string_list( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlStringList::non_null_ptr_type` | — |
| `create_gpml_topological_line( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlTopologicalLine::non_null_ptr_type` | — |
| `create_gpml_topological_network( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlTopologicalNetwork::non_null_ptr_type` | — |
| `create_gpml_topological_polygon( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlTopologicalPolygon::non_null_ptr_type` | — |

## Notes

[[[PROSE notes unit=file-io/GpmlPropertyStructuralTypeReaderUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlPropertyStructuralTypeReader](GpmlPropertyStructuralTypeReader.md) | file-io | 76 |
| [file-io/GsmlPropertyHandlers](GsmlPropertyHandlers.md) | file-io | 34 |
| [file-io/GpmlStructuralTypeReaderUtils](GpmlStructuralTypeReaderUtils.md) | file-io | 13 |
| [file-io/GpmlPropertyReader](GpmlPropertyReader.md) | file-io | 12 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GpmlPropertyStructuralTypeReaderUtils.h
```

# GMTFormatHeader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 180 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GMTFormatHeader.h` | C++ | 449 |
| `src/file-io/GMTFormatHeader.cc` | C++ | 853 |

## Overview

[[[PROSE overview unit=file-io/GMTFormatHeader tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::referenced_files_collection_type`](#gplatesfileioreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |
| [`GPlatesFileIO::GMTFormatHeader`](#gplatesfileiogmtformatheader) | class | — | — | 3 | Interface for formatting of a GMT feature header. |
| [`GPlatesFileIO::GMTHeaderPrinter`](#gplatesfileiogmtheaderprinter) | class | — | — | 0 | Prints lines of header and keeps track of writing starting '\>' character. |
| [`GPlatesFileIO::GMTFormatPlates4StyleHeader`](#gplatesfileiogmtformatplates4styleheader) | class | [`GPlatesFileIO::GMTFormatHeader`](GMTFormatHeader.md) | — | 0 | Formats a header using PLATES4 information if available. |
| [`GPlatesFileIO::GMTFormatVerboseHeader`](#gplatesfileiogmtformatverboseheader) | class | [`GPlatesFileIO::GMTFormatHeader`](GMTFormatHeader.md)<br>[`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Formats a header by printing out the feature's property values as strings. |
| [`GPlatesFileIO::GMTFormatPreferPlates4StyleHeader`](#gplatesfileiogmtformatpreferplates4styleheader) | class | [`GPlatesFileIO::GMTFormatHeader`](GMTFormatHeader.md)<br>[`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Formats PLATES4 style header if feature has an old plates header property. |

## Members

### `GPlatesFileIO::referenced_files_collection_type`

*None.*

### `GPlatesFileIO::GMTFormatHeader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~GMTFormatHeader()` | destructor | `None` | public | — |
| `get_feature_header_lines( const GPlatesModel::FeatureHandle::const_weak_ref &feature, std::vector<QString>& header_lines)` | method | `bool` | public | Format feature into a sequence of header lines (returned as strings). true if there is enough information to print a header. |
| `add_filenames_to_header( std::vector<QString>& header, const referenced_files_collection_type &file_references)` | method | `void` | public | — |

### `GPlatesFileIO::GMTHeaderPrinter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GMTHeaderPrinter()` | constructor | `None` | public | — |
| `print_global_header_lines( QTextStream& output_stream, std::vector<QString>& header_lines)` | method | `void` | public | Prints the header lines at the top of the file. |
| `print_feature_header_lines( QTextStream& output_stream, std::vector<QString>& header_lines)` | method | `void` | public | Prints the header lines at beginning of a feature. |
| `d_is_first_feature_header_in_file` | field | `bool` | private | Is the next feature to be written the first one ? |

### `GPlatesFileIO::GMTFormatPlates4StyleHeader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_feature_header_lines( const GPlatesModel::FeatureHandle::const_weak_ref &feature, std::vector<QString>& header_lines)` | method | `bool` | public | — |
| `format_header_lines( const GPlatesFileIO::OldPlatesHeader& old_plates_header, std::vector<QString>& header_lines)` | method | `void` | private | — |
| `d_plates_header_visitor` | field | `GPlatesFileIO::PlatesLineFormatHeaderVisitor` | private | — |

### `GPlatesFileIO::GMTFormatVerboseHeader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GMTFormatVerboseHeader()` | constructor | `None` | public | — |
| `get_feature_header_lines( const GPlatesModel::FeatureHandle::const_weak_ref &feature, std::vector<QString>& header_lines)` | method | `bool` | public | — |
| `AttributeMap` | typedef | `std::map<GPlatesModel::XmlAttributeName, GPlatesModel::XmlAttributeValue>` | private | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | private | — |
| `initialise_pre_property_values( const GPlatesModel::TopLevelPropertyInline &top_level_property_inline)` | method | `bool` | private | — |
| `finalise_post_property_values( const GPlatesModel::TopLevelPropertyInline &top_level_property_inline)` | method | `void` | private | — |
| `visit_enumeration( const GPlatesPropertyValues::Enumeration &enumeration)` | method | `void` | private | — |
| `visit_gml_line_string( const GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | private | — |
| `visit_gml_multi_point( const GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | private | — |
| `visit_gml_orientable_curve( const GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | private | — |
| `visit_gml_point( const GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gml_polygon( const GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | private | — |
| `visit_gml_time_instant( const GPlatesPropertyValues::GmlTimeInstant &gml_time_instant)` | method | `void` | private | — |
| `visit_gml_time_period( const GPlatesPropertyValues::GmlTimePeriod &gml_time_period)` | method | `void` | private | — |
| `visit_gpml_polarity_chron_id( const GPlatesPropertyValues::GpmlPolarityChronId &gpml_polarity_chron_id)` | method | `void` | private | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `visit_gpml_feature_reference( const GPlatesPropertyValues::GpmlFeatureReference &gpml_feature_reference)` | method | `void` | private | — |
| `visit_gpml_feature_snapshot_reference( const GPlatesPropertyValues::GpmlFeatureSnapshotReference &gpml_feature_snapshot_reference)` | method | `void` | private | — |
| `visit_gpml_property_delegate( const GPlatesPropertyValues::GpmlPropertyDelegate &gpml_property_delegate)` | method | `void` | private | — |
| `visit_gpml_key_value_dictionary( const GPlatesPropertyValues::GpmlKeyValueDictionary &gpml_key_value_dictionary)` | method | `void` | private | — |
| `visit_gpml_piecewise_aggregation( const GPlatesPropertyValues::GpmlPiecewiseAggregation &gpml_piecewise_aggregation)` | method | `void` | private | — |
| `visit_hot_spot_trail_mark( const GPlatesPropertyValues::GpmlHotSpotTrailMark &gpml_hot_spot_trail_mark)` | method | `void` | private | — |
| `visit_gpml_measure( const GPlatesPropertyValues::GpmlMeasure &gpml_measure)` | method | `void` | private | — |
| `visit_gpml_old_plates_header( const GPlatesPropertyValues::GpmlOldPlatesHeader &gpml_old_plates_header)` | method | `void` | private | — |
| `write_gpml_time_window( const GPlatesPropertyValues::GpmlTimeWindow &gpml_time_window)` | method | `void` | private | — |
| `visit_gpml_irregular_sampling( const GPlatesPropertyValues::GpmlIrregularSampling &gpml_irregular_sampling)` | method | `void` | private | — |
| `visit_gpml_plate_id( const GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | private | — |
| `visit_gpml_revision_id( const GPlatesPropertyValues::GpmlRevisionId &gpml_revision_id)` | method | `void` | private | — |
| `write_gpml_time_sample( const GPlatesPropertyValues::GpmlTimeSample &gpml_time_sample)` | method | `void` | private | — |
| `visit_xs_string( const GPlatesPropertyValues::XsString &xs_string)` | method | `void` | private | — |
| `visit_xs_boolean( const GPlatesPropertyValues::XsBoolean &xs_boolean)` | method | `void` | private | — |
| `visit_xs_double( const GPlatesPropertyValues::XsDouble &xs_double)` | method | `void` | private | — |
| `visit_xs_integer( const GPlatesPropertyValues::XsInteger &xs_integer)` | method | `void` | private | — |
| `write_gpml_key_value_dictionary_element( const GPlatesPropertyValues::GpmlKeyValueDictionaryElement &element)` | method | `void` | private | — |
| `format_attributes( const AttributeMap &attribute_map)` | method | `void` | private | — |
| `start_header_line()` | method | `void` | private | — |
| `end_header_line( bool output = true)` | method | `void` | private | — |
| `clear_header_line()` | method | `void` | private | — |
| `PropertyAccumulator` | class | `None` | private | Accumulates information when visiting a property. |
| `d_header_lines` | field | `std::vector<QString>` | private | Output of get\_feature\_header\_lines. |
| `d_current_line` | field | `QString` | private | Current header line being formatted (not used by all methods). |
| `d_line_stream` | field | `QTextStream` | private | Used to write to d\_current\_line. |
| `d_nested_depth` | field | `int` | private | The depth of nesting of property values. |
| `d_property_accumulator` | field | `PropertyAccumulator` | private | Accumulates information about the current property. |

### `GPlatesFileIO::GMTFormatPreferPlates4StyleHeader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_feature_header_lines( const GPlatesModel::FeatureHandle::const_weak_ref &feature, std::vector<QString>& header_lines)` | method | `bool` | public | — |
| `visit_gpml_old_plates_header( const GPlatesPropertyValues::GpmlOldPlatesHeader &/*gpml_old_plates_header*/)` | method | `void` | private | — |
| `d_has_old_plates_header` | field | `bool` | private | — |
| `d_plates4_style_header` | field | `GMTFormatPlates4StyleHeader` | private | — |
| `d_verbose_header` | field | `GMTFormatVerboseHeader` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_GMTFORMATHEADER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/GMTFormatHeader tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GMTFormatResolvedTopologicalGeometryExport](GMTFormatResolvedTopologicalGeometryExport.md) | file-io | 23 |
| [file-io/GMTFormatReconstructedFeatureGeometryExport](GMTFormatReconstructedFeatureGeometryExport.md) | file-io | 14 |
| [file-io/GMTFormatMultiPointVectorFieldExport](GMTFormatMultiPointVectorFieldExport.md) | file-io | 10 |
| [file-io/GMTFormatWriter](GMTFormatWriter.md) | file-io | 9 |
| [file-io/GMTFormatFlowlineExport](GMTFormatFlowlineExport.md) | file-io | 8 |
| [file-io/GMTFormatMotionPathExport](GMTFormatMotionPathExport.md) | file-io | 8 |
| [file-io/OgrReader](OgrReader.md) | file-io | 6 |
| [file-io/PlatesRotationFileProxy](PlatesRotationFileProxy.md) | file-io | 4 |
| [file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport](CitcomsGMTFormatResolvedTopologicalBoundaryExport.md) | file-io | 3 |
| [file-io/GMTFormatReconstructedScalarCoverageExport](GMTFormatReconstructedScalarCoverageExport.md) | file-io | 2 |
| [file-io/GMTFormatDeformationExport](GMTFormatDeformationExport.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GMTFormatHeader.h
python scripts/gpq.py def GPlatesFileIO::GMTFormatVerboseHeader --body
python scripts/gpq.py uses GMTFormatVerboseHeader --kind class
python scripts/gpq.py hier GMTFormatVerboseHeader
```

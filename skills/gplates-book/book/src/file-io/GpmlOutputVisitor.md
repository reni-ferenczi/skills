# GpmlOutputVisitor

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 173 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GpmlOutputVisitor.h` | C++ | 403 |
| `src/file-io/GpmlOutputVisitor.cc` | C++ | 1763 |

## Overview

`GpmlOutputVisitor` is the writer half of the GPML format: a `ConstFeatureVisitor`
that serialises each feature and property value it visits as GPML/GML XML through
an `XmlWriter`. It is the mirror image of `GpmlPropertyReader` and
`GpmlStructuralTypeReaderUtils` — one `visit_*` override per concrete property-value
type, each writing that type's own element structure — so extending GPML to a new
property type means adding a visitor override here as well as a reader.

The class supports two ways of directing output: opening and owning a `QFile` for a
given `FileInfo` (optionally routed through a `GzipFile` when `use_gzip` is set, for
`.gpmlz`/`.gpml.gz`), or writing to a caller-supplied `QIODevice` it does not own.
`start_writing_document` writes the XML prologue and the `gpml:FeatureCollection`
root element, stamping it with the current `Gpgim` version and recording that
version as a tag on the feature collection so later code can tell which GPGIM
schema a collection was last saved against.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::XmlAttribute`](#anonymousxmlattribute) | typedef | — | — | 0 | — |
| [`GPlatesFileIO::GpmlOutputVisitor`](#gplatesfileiogpmloutputvisitor) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | — |

## Members

### `(anonymous)::XmlAttribute`

*None.*

### `GPlatesFileIO::GpmlOutputVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GpmlOutputVisitor( const FileInfo &file_info, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection_ref, bool use_gzip)` | constructor | `None` | public | Creates a GPML writer for the given file. |
| `GpmlOutputVisitor( QIODevice *target, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection_ref)` | constructor | `None` | public | Creates a GPML writer for the given QIODevice. |
| `~GpmlOutputVisitor()` | destructor | `None` | public | — |
| `start_writing_document( XmlWriter &writer, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection_ref)` | method | `void` | public | Start writing the document (via the XML writer) to the output file or device. |
| `visit_feature_handle( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | protected | — |
| `visit_top_level_property_inline( const GPlatesModel::TopLevelPropertyInline &top_level_property_inline)` | method | `void` | protected | — |
| `visit_enumeration( const GPlatesPropertyValues::Enumeration &enumeration)` | method | `void` | protected | — |
| `visit_gml_data_block( const GPlatesPropertyValues::GmlDataBlock &gml_data_block)` | method | `void` | protected | — |
| `visit_gml_file( const GPlatesPropertyValues::GmlFile &gml_file)` | method | `void` | protected | — |
| `visit_gml_grid_envelope( const GPlatesPropertyValues::GmlGridEnvelope &gml_grid_envelope)` | method | `void` | protected | — |
| `visit_gml_line_string( const GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | protected | — |
| `visit_gml_multi_point( const GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | protected | — |
| `visit_gml_orientable_curve( const GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | protected | — |
| `visit_gml_point( const GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | protected | — |
| `visit_gml_polygon( const GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | protected | — |
| `visit_gml_rectified_grid( const GPlatesPropertyValues::GmlRectifiedGrid &gml_rectified_grid)` | method | `void` | protected | — |
| `visit_gml_time_instant( const GPlatesPropertyValues::GmlTimeInstant &gml_time_instant)` | method | `void` | protected | — |
| `visit_gml_time_period( const GPlatesPropertyValues::GmlTimePeriod &gml_time_period)` | method | `void` | protected | — |
| `visit_gpml_age( const GPlatesPropertyValues::GpmlAge &gpml_age)` | method | `void` | protected | — |
| `visit_gpml_array( const GPlatesPropertyValues::GpmlArray &gpml_array)` | method | `void` | protected | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | protected | — |
| `visit_gpml_feature_reference( const GPlatesPropertyValues::GpmlFeatureReference &gpml_feature_reference)` | method | `void` | protected | — |
| `visit_gpml_feature_snapshot_reference( const GPlatesPropertyValues::GpmlFeatureSnapshotReference &gpml_feature_snapshot_reference)` | method | `void` | protected | — |
| `visit_gpml_finite_rotation( const GPlatesPropertyValues::GpmlFiniteRotation &gpml_finite_rotation)` | method | `void` | protected | — |
| `visit_gpml_finite_rotation_slerp( const GPlatesPropertyValues::GpmlFiniteRotationSlerp &gpml_finite_rotation_slerp)` | method | `void` | protected | — |
| `visit_hot_spot_trail_mark( const GPlatesPropertyValues::GpmlHotSpotTrailMark &gpml_hot_spot_trail_mark)` | method | `void` | protected | — |
| `visit_gpml_irregular_sampling( const GPlatesPropertyValues::GpmlIrregularSampling &gpml_irregular_sampling)` | method | `void` | protected | — |
| `visit_gpml_key_value_dictionary( const GPlatesPropertyValues::GpmlKeyValueDictionary &gpml_key_value_dictionary)` | method | `void` | protected | — |
| `visit_gpml_measure( const GPlatesPropertyValues::GpmlMeasure &gpml_measure)` | method | `void` | protected | — |
| `visit_gpml_metadata( const GPlatesPropertyValues::GpmlMetadata &gpml_metadata)` | method | `void` | protected | — |
| `visit_gpml_old_plates_header( const GPlatesPropertyValues::GpmlOldPlatesHeader &gpml_old_plates_header)` | method | `void` | protected | — |
| `visit_gpml_piecewise_aggregation( const GPlatesPropertyValues::GpmlPiecewiseAggregation &gpml_piecewise_aggregation)` | method | `void` | protected | — |
| `visit_gpml_plate_id( const GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | protected | — |
| `visit_gpml_polarity_chron_id( const GPlatesPropertyValues::GpmlPolarityChronId &gpml_polarity_chron_id)` | method | `void` | protected | — |
| `visit_gpml_property_delegate( const GPlatesPropertyValues::GpmlPropertyDelegate &gpml_property_delegate)` | method | `void` | protected | — |
| `visit_gpml_raster_band_names( const GPlatesPropertyValues::GpmlRasterBandNames &gpml_raster_band_names)` | method | `void` | protected | — |
| `visit_gpml_revision_id( const GPlatesPropertyValues::GpmlRevisionId &gpml_revision_id)` | method | `void` | protected | — |
| `visit_gpml_scalar_field_3d_file( const GPlatesPropertyValues::GpmlScalarField3DFile &gpml_scalar_field_3d_file)` | method | `void` | protected | — |
| `visit_gpml_string_list( const GPlatesPropertyValues::GpmlStringList &gpml_string_list)` | method | `void` | protected | — |
| `write_gpml_time_sample( const GPlatesPropertyValues::GpmlTimeSample &gpml_time_sample)` | method | `void` | protected | — |
| `write_gpml_time_window( const GPlatesPropertyValues::GpmlTimeWindow &gpml_time_window)` | method | `void` | protected | — |
| `visit_gpml_topological_network( const GPlatesPropertyValues::GpmlTopologicalNetwork &gpml_topological_network)` | method | `void` | protected | — |
| `visit_gpml_topological_polygon( const GPlatesPropertyValues::GpmlTopologicalPolygon &gpml_topological_polygon)` | method | `void` | protected | — |
| `visit_gpml_topological_line( const GPlatesPropertyValues::GpmlTopologicalLine &gpml_topological_line)` | method | `void` | protected | — |
| `visit_gpml_topological_line_section( const GPlatesPropertyValues::GpmlTopologicalLineSection &gpml_topological_line_section)` | method | `void` | protected | — |
| `visit_gpml_topological_point( const GPlatesPropertyValues::GpmlTopologicalPoint &gpml_topological_point)` | method | `void` | protected | — |
| `visit_old_version_property_value( const GPlatesPropertyValues::OldVersionPropertyValue &old_version_prop_val)` | method | `void` | protected | — |
| `visit_uninterpreted_property_value( const GPlatesPropertyValues::UninterpretedPropertyValue &uninterpreted_prop_val)` | method | `void` | protected | — |
| `visit_xs_boolean( const GPlatesPropertyValues::XsBoolean &xs_boolean)` | method | `void` | protected | — |
| `visit_xs_double( const GPlatesPropertyValues::XsDouble &xs_double)` | method | `void` | protected | — |
| `visit_xs_integer( const GPlatesPropertyValues::XsInteger &xs_integer)` | method | `void` | protected | — |
| `visit_xs_string( const GPlatesPropertyValues::XsString &xs_string)` | method | `void` | protected | — |
| `write_gpml_key_value_dictionary_element( const GPlatesPropertyValues::GpmlKeyValueDictionaryElement &element)` | method | `void` | private | — |
| `d_qfile_ptr` | field | `boost::shared_ptr<QFile>` | private | Keeps track of the file currently being written to. |
| `d_gzip_file` | field | `boost::optional<GzipFile>` | private | Optional Gzip QIODevice to use when saving ".gpmlz" (or ".gpml.gz"). |
| `d_output` | field | `XmlWriter` | private | The destination of the the XML data. |
| `d_output_filename` | field | `QString` | private | The requested output filename. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `writeTemplateTypeParameterType( GPlatesFileIO::XmlWriter &writer, const QualifiedNameType &value_type)` | function | `void` | — |
| `write_gml_linear_ring( GPlatesFileIO::XmlWriter &xml_output, const GPlatesMaths::PolygonOnSphere::ring_vertex_const_iterator &ring_begin, const GPlatesMaths::PolygonOnSphere::ring_vertex_const_iterator &ring_end)` | function | `void` | Convenience function to help write PolygonOnSphere's exterior and interior rings. |
| `write_gml_point_on_sphere( GPlatesFileIO::XmlWriter &xml_output, const GPlatesMaths::PointOnSphere &point, GPlatesPropertyValues::GmlPoint::GmlProperty gml_property)` | function | `void` | Convenience function to help write GmlPoint and GmlMultiPoint. |
| `write_gml_point_2d( GPlatesFileIO::XmlWriter &xml_output, const GPlatesPropertyValues::GmlPoint &gml_point)` | function | `void` | Similar to write\_gml\_point\_on\_sphere() but retrieves the original lat-lon version of the point using GmlPoint::point\_2d(). |
| `write_gml_data_block_value_component_value_object_template( GPlatesFileIO::XmlWriter &xml_output, GPlatesPropertyValues::GmlDataBlockCoordinateList::non_null_ptr_to_const_type coordinate_list)` | function | `void` | Convenience function to help write the value-object templates in the value-component properties in the composite-value in GmlDataBlock. |
| `populate_coordinates_iterator_ranges( std::vector< std::pair<CoordinatesIter, CoordinatesIter> > &coordinates_iterator_ranges, TupleListIter tuple_list_begin, TupleListIter tuple_list_end)` | function | `void` | Convenience function to help write the tuple-list in GmlDataBlock. |
| `write_tuple_list_from_coordinates_iterator_ranges( GPlatesFileIO::XmlWriter &xml_output, RangesIter ranges_begin, RangesIter ranges_end)` | function | `void` | Convenience function to help write the tuple-list in GmlDataBlock. |
| `write_gml_data_block_tuple_list( GPlatesFileIO::XmlWriter &xml_output, GPlatesPropertyValues::GmlDataBlock::tuple_list_type::const_iterator tuple_list_begin, GPlatesPropertyValues::GmlDataBlock::tuple_list_type::const_iterator tuple_list_end)` | function | `void` | Convenience function to help write the tuple-list in GmlDataBlock. |
| `GPLATES_FILEIO_GPMLOUTPUTVISITOR_H` | macro | `None` | — |

## Notes

File ownership depends on which constructor is used: the `FileInfo` constructor
creates and owns `d_qfile_ptr`, opening it for writing (throwing
`ErrorOpeningFileForWritingException` on failure) and closing it when the visitor
is destroyed; the `QIODevice*` constructor leaves `d_qfile_ptr` empty and leaves
device lifetime to the caller. The destructor wraps its cleanup in `try`/`catch(...)`
so no exception escapes from it. When `use_gzip` is true, `d_gzip_file` sits between
the XML writer and `d_qfile_ptr`, compressing at the zlib default level; the header's
comment on `d_qfile_ptr` documents the intended call sequence
(`FileInfo::get_writer()` creates the visitor, the caller visits the feature
collection, then the visitor going out of scope closes the file).

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlFormatDeformationExport](GpmlFormatDeformationExport.md) | file-io | 38 |
| [file-io/GpmlFormatReconstructedScalarCoverageExport](GpmlFormatReconstructedScalarCoverageExport.md) | file-io | 28 |
| [file-io/GpmlFormatMultiPointVectorFieldExport](GpmlFormatMultiPointVectorFieldExport.md) | file-io | 26 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 24 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 3 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GpmlOutputVisitor.h
python scripts/gpq.py def GPlatesFileIO::GpmlOutputVisitor --body
python scripts/gpq.py uses GpmlOutputVisitor --kind class
python scripts/gpq.py hier GpmlOutputVisitor
```

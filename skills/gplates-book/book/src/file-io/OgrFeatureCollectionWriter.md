# OgrFeatureCollectionWriter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 113 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/OgrFeatureCollectionWriter.h` | C++ | 162 |
| `src/file-io/OgrFeatureCollectionWriter.cc` | C++ | 1827 |

## Overview

A feature collection visitor that exports features to an OGR-supported format (such as shapefile, GeoJSON, or other vector formats) determined by the file extension. As it walks the feature tree, it visits geometry properties (`GmlPoint`, `GmlLineString`, `GmlPolygon`, `GmlMultiPoint`, `GmlOrientableCurve`), accumulating them per feature, and visits property values, extracting and mapping GPlates model properties to OGR attributes. A configurable model-to-attribute map controls which model properties map to which shapefile/OGR fields; unmappable properties and special metadata (plate IDs, timing, Old Plates headers) are stored in key-value dictionaries. The accumulated geometries and attributes are written via `OgrWriter` when each feature is finalized.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::OgrFeatureCollectionWriter`](#gplatesfileioogrfeaturecollectionwriter) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Visits a feature collection and exports the contents to an OGR format determined by the file extension. |

## Members

### `GPlatesFileIO::OgrFeatureCollectionWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `OgrFeatureCollectionWriter( File::Reference &file_ref, const boost::shared_ptr<const FeatureCollectionFileFormat::OGRConfiguration> &default_file_configuration)` | constructor | `None` | public | @pre is\_writable(file\_info) is true. |
| `~OgrFeatureCollectionWriter()` | destructor | `None` | public | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | private | — |
| `finalise_post_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | private | — |
| `visit_gml_line_string( const GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | private | — |
| `visit_gml_multi_point( const GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | private | — |
| `visit_gml_orientable_curve( const GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | private | — |
| `visit_gml_point( const GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gml_polygon( const GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | private | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `visit_gpml_key_value_dictionary( const GPlatesPropertyValues::GpmlKeyValueDictionary &gpml_key_value_dictionary)` | method | `void` | private | — |
| `clear_accumulators()` | method | `void` | private | Clears the various geometry accumulators. |
| `d_output_file` | field | `boost::scoped_ptr<QFile>` | private | — |
| `d_key_value_dictionary` | field | `boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type>` | private | The first GpmlKeyValueDictionary encountered while traversing a feature. |
| `d_default_key_value_dictionary` | field | `boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type>` | private | A default KeyValueDictionary used for features for which no KVD is found. |
| `d_model_to_shapefile_map` | field | `QMap< QString,QString >` | private | A model\_to\_shapefile\_attribute map |
| `d_ogr_writer` | field | `boost::scoped_ptr<OgrWriter>` | private | — |
| `d_point_geometries` | field | `std::vector<GPlatesMaths::PointOnSphere>` | private | Store various geometries encountered in each feature. |
| `d_multi_point_geometries` | field | `std::vector<GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type>` | private | — |
| `d_polyline_geometries` | field | `std::vector<GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type>` | private | — |
| `d_polygon_geometries` | field | `std::vector<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_key_string( const model_to_attribute_map_type &model_to_shapefile_map, const ShapefileAttributes::ModelProperties &property_enum)` | function | `QString` | ! get\_key\_string - if a key for the model property given by in attribute name for that property. |
| `find_element_by_key( const QString &key, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary)` | function | `std::vector<GPlatesPropertyValues::GpmlKeyValueDictionaryElement>::iterator` | ! |
| `add_or_replace_kvd_element( const GPlatesPropertyValues::GpmlKeyValueDictionaryElement &new_element, const QString &key_string, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary)` | function | `void` | Adds or replaces new\_element to the kvd dictionary. |
| `add_field_to_kvd( const QString &key_string, GPlatesModel::PropertyValue::non_null_ptr_type value, const GPlatesPropertyValues::StructuralType &type, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary)` | function | `void` | ! add\_field\_to\_kvd - adds the entry given by key key\_string and value value to kvd dictionary. |
| `add_plate_id_key_to_kvd_if_missing( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString, QString > &model_to_shapefile_map)` | function | `void` | — |
| `add_begin_time_key_to_kvd_if_missing( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString, QString > &model_to_shapefile_map)` | function | `void` | — |
| `add_end_time_key_to_kvd_if_missing( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString, QString > &model_to_shapefile_map)` | function | `void` | — |
| `add_name_key_to_kvd_if_missing( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString, QString > &model_to_shapefile_map)` | function | `void` | — |
| `add_description_key_to_kvd_if_missing( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString, QString > &model_to_shapefile_map)` | function | `void` | — |
| `add_feature_type_key_to_kvd_if_missing( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString, QString > &model_to_shapefile_map)` | function | `void` | — |
| `add_feature_id_key_to_kvd_if_missing( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString, QString > &model_to_shapefile_map)` | function | `void` | — |
| `add_conjugate_key_to_kvd_if_missing( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString, QString > &model_to_shapefile_map)` | function | `void` | — |
| `add_left_plate_key_to_kvd_if_missing( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString, QString > &model_to_shapefile_map)` | function | `void` | — |
| `add_right_plate_key_to_kvd_if_missing( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString, QString > &model_to_shapefile_map)` | function | `void` | — |
| `add_reconstruction_method_key_to_kvd_if_missing( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString, QString > &model_to_shapefile_map)` | function | `void` | — |
| `add_spreading_asymmetry_key_to_kvd_if_missing( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString, QString > &model_to_shapefile_map)` | function | `void` | — |
| `add_geometry_import_time_key_to_kvd_if_missing( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString, QString > &model_to_shapefile_map)` | function | `void` | — |
| `add_region_to_kvd( const GPlatesPropertyValues::GpmlOldPlatesHeader *old_plates_header, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary)` | function | `void` | — |
| `add_reference_number_to_kvd( const GPlatesPropertyValues::GpmlOldPlatesHeader *old_plates_header, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary)` | function | `void` | — |
| `add_string_number_to_kvd( const GPlatesPropertyValues::GpmlOldPlatesHeader *old_plates_header, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary)` | function | `void` | — |
| `add_data_type_code_number_to_kvd( const GPlatesPropertyValues::GpmlOldPlatesHeader *old_plates_header, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary)` | function | `void` | — |
| `add_data_type_code_number_additional_to_kvd( const GPlatesPropertyValues::GpmlOldPlatesHeader *old_plates_header, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary)` | function | `void` | — |
| `add_colour_code_to_kvd( const GPlatesPropertyValues::GpmlOldPlatesHeader *old_plates_header, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary)` | function | `void` | — |
| `add_number_of_points_to_kvd( const GPlatesPropertyValues::GpmlOldPlatesHeader *old_plates_header, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary)` | function | `void` | — |
| `add_plates_header_values_to_kvd( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const GPlatesModel::FeatureHandle &feature_handle)` | function | `void` | — |
| `add_missing_fields_to_map( QMap< QString, QString> &model_to_shapefile_map, const GPlatesFileIO::FileInfo &file_info)` | function | `void` | If any of the default mapped fields are not present in the model-to-shapefile-map, they will be added. |
| `add_missing_keys_to_kvd( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type kvd, QMap< QString, QString> &model_to_shapefile_map)` | function | `void` | ! |
| `add_or_replace_model_kvd( const GPlatesModel::FeatureHandle &feature_handle, const GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type kvd)` | function | `void` | ! add\_or\_replace\_model\_kvd - Add kvd to the feature given by feature\_handle. |
| `get_time_from_time_instant( const GPlatesPropertyValues::GmlTimeInstant &time_instant)` | function | `double` | — |
| `fill_kvd_with_plate_id( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString,QString > &model_to_shapefile_map, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `void` | — |
| `fill_kvd_with_conjugate_plate_id( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString,QString > &model_to_shapefile_map, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `void` | — |
| `fill_kvd_with_left_plate_id( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString,QString > &model_to_shapefile_map, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `void` | — |
| `fill_kvd_with_right_plate_id( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString,QString > &model_to_shapefile_map, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `void` | — |
| `fill_kvd_with_recon_method( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString,QString > &model_to_shapefile_map, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `void` | — |
| `fill_kvd_with_spreading_asymmetry( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString,QString > &model_to_shapefile_map, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `void` | — |
| `fill_kvd_with_geometry_import_time( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString,QString > &model_to_shapefile_map, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `void` | — |
| `fill_kvd_with_feature_type( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString,QString > &model_to_shapefile_map, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `void` | — |
| `fill_kvd_with_begin_and_end_time( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString,QString > &model_to_shapefile_map, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `void` | — |
| `fill_kvd_with_name( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString,QString > &model_to_shapefile_map, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `void` | — |
| `fill_kvd_with_description( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString,QString > &model_to_shapefile_map, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `void` | — |
| `fill_kvd_with_feature_id( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, const QMap< QString,QString > &model_to_shapefile_map, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `void` | — |
| `create_default_kvd_from_map( boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type> &default_key_value_dictionary, const QMap< QString,QString > &model_to_shapefile_map)` | function | `void` | — |
| `fill_kvd_values_from_feature( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type dictionary, QMap< QString,QString > &model_to_shapefile_map, const GPlatesModel::FeatureHandle &feature_handle)` | function | `void` | — |
| `create_default_model_to_shapefile_map( QMap< QString, QString > &model_to_shapefile_map)` | function | `void` | — |
| `write_point_geometries( GPlatesFileIO::OgrWriter *ogr_writer, const std::vector<GPlatesMaths::PointOnSphere> &point_geometries, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type> &field_names_key_value_dictionary, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDic ...` | function | `void` | — |
| `write_multi_point_geometries( GPlatesFileIO::OgrWriter *ogr_writer, const std::vector<GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type> &multi_point_geometries, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type> &field_names_key_value_dictionary, const boost::op ...` | function | `void` | — |
| `write_polyline_geometries( GPlatesFileIO::OgrWriter *ogr_writer, const std::vector<GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type> &polyline_geometries, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type> &field_names_key_value_dictionary, const boost::optional<G ...` | function | `void` | — |
| `write_polygon_geometries( GPlatesFileIO::OgrWriter *ogr_writer, const std::vector<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type> &polygon_geometries, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type> &field_names_key_value_dictionary, const boost::optional<GPla ...` | function | `void` | — |
| `GPLATES_FILEIO_OGRFEATURECOLLECTIONWRITER_H` | macro | `None` | — |

## Notes

Geometries and attributes are accumulated per feature during traversal and written out when feature finalization occurs; accumulators are cleared after each feature is finalized. Configuration is provided via the file's attached configuration (if available and compatible) or the supplied default configuration. Property mapping is bidirectional: the model-to-attribute map persists changes made during writing, allowing subsequent writes to preserve customized mappings.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/OgrFeatureCollectionWriter.h
python scripts/gpq.py def GPlatesFileIO::OgrFeatureCollectionWriter --body
python scripts/gpq.py uses OgrFeatureCollectionWriter --kind class
python scripts/gpq.py hier OgrFeatureCollectionWriter
```

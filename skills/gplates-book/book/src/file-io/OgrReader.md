# OgrReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 114 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/OgrReader.h` | C++ | 348 |
| `src/file-io/OgrReader.cc` | C++ | 2451 |

## Overview

`OgrReader` is the GDAL/OGR-backed reader for shapefiles and other vector formats
GDAL supports, historically named `ShapefileReader` before OGR support widened
beyond shapefiles. Its public surface is entirely static (`read_file`,
`read_field_names`, `remap_shapefile_attributes`, `set_property_mapper`); the
constructor is private, and `read_file` creates one short-lived `OgrReader`
instance on the stack to hold per-file OGR state (`d_data_source_ptr`,
`d_layer_ptr`, `d_feature_ptr`, the running geometry counts) for the duration of
the read.

`read_file` opens the datasource with `GdalUtils::open_vector`, validates it via
`check_file_format` (must have at least one layer with at least one feature; only
the first layer is read, and a second layer only produces a warning), reads the
spatial reference system and builds a `CoordinateTransformation` to WGS84 via
`read_srs_and_set_transformation`, then resolves how OGR attribute fields map onto
GPlates model properties. That mapping is looked up first from a sidecar
`.gplates.xml` file (`OgrUtils::make_ogr_xml_filename`); if none exists it falls
back to the shared `PropertyMapper` (typically backed by a Qt dialog) and persists
the result for next time. `handle_geometry` then dispatches each OGR feature's
geometry by `OGRwkbGeometryType` to one of the `handle_point`/`handle_multi_point`/
`handle_linestring`/`handle_multi_linestring`/`handle_polygon`/`handle_multi_polygon`
handlers, which build the corresponding `PointOnSphere`/`PolylineOnSphere`/
`PolygonOnSphere` geometry and a `FeatureHandle` for it, and `add_attributes_to_feature`
converts the OGR attribute row into model properties via `map_attributes_to_properties`.

`remap_shapefile_attributes` reruns the attribute-to-property mapping on an already
loaded feature collection without touching its geometry, for when the user changes
the field mapping after the initial load.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::OgrReader`](#gplatesfileioogrreader) | class | — | — | 0 | — |

## Members

### `GPlatesFileIO::OgrReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `read_file( GPlatesFileIO::File::Reference &file_ref, const boost::shared_ptr<const FeatureCollectionFileFormat::OGRConfiguration> &default_file_configuration, ReadErrorAccumulation &read_errors, bool &contains_unsaved_changes)` | method | `void` | public | Reads file specified by the filename in file\_ref and stores into feature collection in file\_ref. default\_file\_configuration should be the current default shapefile file configuration as determined by ... |
| `set_property_mapper( boost::shared_ptr< PropertyMapper > property_mapper)` | method | `void` | public | — |
| `read_field_names( GPlatesFileIO::File::Reference &file_ref, GPlatesModel::ModelInterface &model, ReadErrorAccumulation &read_errors)` | method | `QStringList` | public | Reads only the field names from the file file\_ref. |
| `remap_shapefile_attributes( GPlatesFileIO::File::Reference &file, GPlatesModel::ModelInterface &model, ReadErrorAccumulation &read_errors)` | method | `void` | public | Remaps the attributes stored in the feature collection of file to the mapped feature properties of the features in the feature collection in file. |
| `OgrReader()` | constructor | `None` | private | — |
| `~OgrReader()` | destructor | `None` | private | — |
| `OgrReader( const OgrReader &other)` | constructor | `None` | private | Make copy constructor private |
| `operator=` | field | `OgrReader` | private | Make assignment private |
| `check_file_format( ReadErrorAccumulation &read_errors)` | method | `bool` | private | Checks that the file represented by OgrReader::d\_filename can be opened, contains at least one layer, and that this layer contains at least one feature with a valid geometry. true if the above conditions are met, otherwise false. |
| `open_file( const QString &filename, ReadErrorAccumulation &read_errors)` | method | `bool` | private | — |
| `get_field_names( ReadErrorAccumulation &read_errors)` | method | `void` | private | — |
| `get_attributes()` | method | `void` | private | — |
| `handle_geometry( const GPlatesModel::FeatureType &feature_type, const OGRwkbGeometryType &type, const boost::optional<GPlatesModel::GpgimProperty::non_null_ptr_to_const_type> &property, const GPlatesModel::FeatureCollectionHandle::weak_ref &collection, ReadErrorAccumulation &read_errors, const boost::shared_ptr<GPlates ...` | method | `void` | private | — |
| `handle_point( const GPlatesModel::FeatureType &feature_type, const boost::optional<GPlatesModel::GpgimProperty::non_null_ptr_to_const_type> &property, const GPlatesModel::FeatureCollectionHandle::weak_ref &collection, ReadErrorAccumulation &read_errors, const boost::shared_ptr<GPlatesFileIO::DataSource> &source, const ...` | method | `void` | private | — |
| `handle_multi_point( const GPlatesModel::FeatureType &feature_type, const boost::optional<GPlatesModel::GpgimProperty::non_null_ptr_to_const_type> &property, const GPlatesModel::FeatureCollectionHandle::weak_ref &collection, ReadErrorAccumulation &read_errors, const boost::shared_ptr<GPlatesFileIO::DataSource> &source, ...` | method | `void` | private | — |
| `handle_linestring( const GPlatesModel::FeatureType &feature_type, const boost::optional<GPlatesModel::GpgimProperty::non_null_ptr_to_const_type> &property, const GPlatesModel::FeatureCollectionHandle::weak_ref &collection, ReadErrorAccumulation &read_errors, const boost::shared_ptr<GPlatesFileIO::DataSource> &source, c ...` | method | `void` | private | — |
| `handle_multi_linestring( const GPlatesModel::FeatureType &feature_type, const boost::optional<GPlatesModel::GpgimProperty::non_null_ptr_to_const_type> &property, const GPlatesModel::FeatureCollectionHandle::weak_ref &collection, ReadErrorAccumulation &read_errors, const boost::shared_ptr<GPlatesFileIO::DataSource> &sou ...` | method | `void` | private | — |
| `handle_polygon( const GPlatesModel::FeatureType &feature_type, const boost::optional<GPlatesModel::GpgimProperty::non_null_ptr_to_const_type> &property, const GPlatesModel::FeatureCollectionHandle::weak_ref &collection, ReadErrorAccumulation &read_errors, const boost::shared_ptr<GPlatesFileIO::DataSource> &source, cons ...` | method | `void` | private | — |
| `handle_multi_polygon( const GPlatesModel::FeatureType &feature_type, const boost::optional<GPlatesModel::GpgimProperty::non_null_ptr_to_const_type> &property, const GPlatesModel::FeatureCollectionHandle::weak_ref &collection, ReadErrorAccumulation &read_errors, const boost::shared_ptr<GPlatesFileIO::DataSource> &source ...` | method | `void` | private | — |
| `read_features( const GPlatesModel::FeatureCollectionHandle::weak_ref &collection, ReadErrorAccumulation &read_errors)` | method | `void` | private | — |
| `create_polygon_feature_from_list( const GPlatesModel::FeatureType &feature_type, const GPlatesModel::FeatureCollectionHandle::weak_ref &collection, const std::vector<GPlatesMaths::PointOnSphere> &exterior_ring, const std::list< std::vector<GPlatesMaths::PointOnSphere> > &interior_rings, const boost::optional<GPlatesMod ...` | method | `GPlatesModel::FeatureHandle::weak_ref` | private | — |
| `create_line_feature_from_list( const GPlatesModel::FeatureType &feature_type, const GPlatesModel::FeatureCollectionHandle::weak_ref &collection, const std::vector<GPlatesMaths::PointOnSphere> &list_of_points, const boost::optional<GPlatesModel::GpgimProperty::non_null_ptr_to_const_type> &property)` | method | `GPlatesModel::FeatureHandle::weak_ref` | private | — |
| `create_point_feature_from_point_on_sphere( const GPlatesModel::FeatureType &feature_type, const GPlatesModel::FeatureCollectionHandle::weak_ref &collection, const GPlatesMaths::PointOnSphere &point, const boost::optional<GPlatesModel::GpgimProperty::non_null_ptr_to_const_type> &property)` | method | `GPlatesModel::FeatureHandle::weak_ref` | private | — |
| `create_multi_point_feature_from_list( const GPlatesModel::FeatureType &feature_type, const GPlatesModel::FeatureCollectionHandle::weak_ref &collection, const std::vector<GPlatesMaths::PointOnSphere> &list_of_points, const boost::optional<GPlatesModel::GpgimProperty::non_null_ptr_to_const_type> &property)` | method | `GPlatesModel::FeatureHandle::weak_ref` | private | — |
| `add_attributes_to_feature( const GPlatesModel::FeatureHandle::weak_ref &, GPlatesFileIO::ReadErrorAccumulation &read_errors, const boost::shared_ptr<GPlatesFileIO::DataSource> &source, const boost::shared_ptr<GPlatesFileIO::LocationInDataSource> &location)` | method | `void` | private | — |
| `transform_and_check_coords( double &x, double &y, ReadErrorAccumulation &read_errors, const boost::shared_ptr<GPlatesFileIO::DataSource> &source, const boost::shared_ptr<GPlatesFileIO::LocationInDataSource> &location)` | method | `bool` | private | — |
| `display_feature_counts()` | method | `void` | private | — |
| `get_OGR_type()` | method | `OGRwkbGeometryType` | private | — |
| `read_srs_and_set_transformation( File::Reference &file_ref, const GPlatesFileIO::FeatureCollectionFileFormat::OGRConfiguration::shared_ptr_to_const_type &default_ogr_file_configuration)` | method | `void` | private | read\_srs\_and\_set\_transformation - set the Configuration's SRS, if one was provided by the OGR source. |
| `add_ring_to_points_list( OGRLinearRing *ring, std::vector<GPlatesMaths::PointOnSphere> &ring_points, ReadErrorAccumulation &read_errors, const boost::shared_ptr<GPlatesFileIO::DataSource> &source, const boost::shared_ptr<GPlatesFileIO::LocationInDataSource> &location)` | method | `void` | private | — |
| `d_filename` | field | `QString` | private | — |
| `d_num_layers` | field | `int` | private | — |
| `d_data_source_ptr` | field | `GdalUtils::vector_data_source_type` | private | — |
| `d_geometry_ptr` | field | `OGRGeometry` | private | — |
| `d_feature_ptr` | field | `OGRFeature` | private | — |
| `d_layer_ptr` | field | `OGRLayer` | private | — |
| `d_type` | field | `OGRwkbGeometryType` | private | The type of the current geometry (e.g. |
| `d_field_names` | field | `QStringList` | private | The shapefile attribute field names. |
| `d_attributes` | field | `std::vector<QVariant>` | private | The shapefile attributes for the current geometry. |
| `d_model_to_attribute_map` | field | `QMap<QString,QString>` | private | Map for associating a model property with a shapefile attribute. |
| `d_feature_type_string` | field | `QString` | private | — |
| `d_feature_id` | field | `boost::optional<GPlatesUtils::UnicodeString>` | private | — |
| `d_total_geometries` | field | `unsigned` | private | The total number of geometries, including those from multi-geometries, in the file. |
| `d_loaded_geometries` | field | `unsigned` | private | The total number of geometries successfully loaded. |
| `d_total_features` | field | `GdalUtils::big_int_type` | private | The total number of features in the file. |
| `s_property_mapper` | field | `boost::shared_ptr< PropertyMapper >` | private | — |
| `d_source_srs` | field | `boost::optional<GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type>` | private | d\_source\_srs - the original SRS of the OGR source, if one was provided. |
| `d_current_coordinate_transformation` | field | `GPlatesPropertyValues::CoordinateTransformation::non_null_ptr_to_const_type` | private | d\_current\_coordinate\_transformation - The coordinate transformation from the provided SRS to WGS84. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `s_property_mapper` | variable | `boost::shared_ptr< GPlatesFileIO::PropertyMapper>` | — |
| `recon_method_is_valid( const QString &recon_method)` | function | `bool` | recon\_method\_is\_valid returns true if recon\_method is "ByPlateID", "HalfStageRotation", "HalfStageRotationVersion2" or "HalfStageRotationVersion3". |
| `create_geo_time_instant( const double &time)` | function | `GPlatesPropertyValues::GeoTimeInstant` | — |
| `create_begin_geo_time_instant( const boost::optional<double> &time)` | function | `GPlatesPropertyValues::GeoTimeInstant` | — |
| `create_end_geo_time_instant( const boost::optional<double> &time)` | function | `GPlatesPropertyValues::GeoTimeInstant` | — |
| `add_polyline_geometry_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const std::vector<GPlatesMaths::PointOnSphere> &list_of_points, const boost::optional<GPlatesModel::GpgimProperty::non_null_ptr_to_const_type> &property)` | function | `void` | Creates a gml line string from list\_of\_points and adds this to feature. |
| `add_polygon_geometry_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const std::vector<GPlatesMaths::PointOnSphere> &exterior_ring, const std::list< std::vector<GPlatesMaths::PointOnSphere> > &interior_rings, const boost::optional<GPlatesModel::GpgimProperty::non_null_ptr_to_const_type> &property)` | function | `void` | Creates a gml polygon from list\_of\_points and adds this to feature. |
| `create_feature( const GPlatesModel::FeatureType &feature_type, const GPlatesModel::FeatureCollectionHandle::weak_ref &collection, const QString &feature_type_qstring, boost::optional<GPlatesUtils::UnicodeString> &feature_id)` | function | `GPlatesModel::FeatureHandle::weak_ref` | Creates a feature of type specified in feature\_creation\_pair, and adds it to collection. a feature handle to the created feature. |
| `get_qvariant_from_finder( QString shapefile_property_name, const GPlatesModel::FeatureHandle::weak_ref &feature)` | function | `QVariant` | Returns a QVariant representing the shapefile\_property\_name from the feature\_handle's shapefile-attribute key-value-dictionary. |
| `append_conjugate_plate_id_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, int conjugate_plate_id_as_int)` | function | `void` | — |
| `append_left_plate_id_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, int left_plate_id_as_int)` | function | `void` | — |
| `append_right_plate_id_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, int right_plate_id_as_int)` | function | `void` | — |
| `append_recon_method_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const QString &recon_method)` | function | `void` | — |
| `append_spreading_asymmetry_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, double spreading_asymmetry)` | function | `void` | — |
| `append_plate_id_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, int plate_id_as_int)` | function | `void` | — |
| `append_geo_times_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const boost::optional<double> &age_of_appearance, const boost::optional<double> &age_of_disappearance)` | function | `void` | — |
| `append_geometry_import_time_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, double geometry_import_time)` | function | `void` | — |
| `append_name_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, QString name)` | function | `void` | — |
| `append_description_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, QString description)` | function | `void` | — |
| `remove_old_properties( const GPlatesModel::FeatureHandle::weak_ref &feature)` | function | `void` | Removes properties with the property names: reconstructionPlateId, validTime, description name conjugatePlateId reconstructionMethod leftPlate rightPlate spreadingAsymmetry geometryImportTime from the feature given by feature\_handle. |
| `map_attributes_to_properties( const GPlatesModel::FeatureHandle::weak_ref &feature, const QMap<QString,QString> &model_to_attribute_map, GPlatesFileIO::ReadErrorAccumulation &read_errors, const boost::shared_ptr<GPlatesFileIO::DataSource> source, const boost::shared_ptr<GPlatesFileIO::LocationInDataSource> location)` | function | `void` | Uses the model\_to\_attribute\_map to create model properties from the feature\_handle's shapefile-attributes key-value-dictionary. |
| `remap_feature_collection( GPlatesFileIO::File::Reference &file, const QMap< QString,QString > &model_to_attribute_map, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `void` | Uses the model\_to\_attribute\_map to create model properties from the shapefile-attributes key-value-dictionary, for each feature in file's feature collection. |
| `fill_attribute_map_with_default_values( QMap< QString, QString > &model_to_attribute_map)` | function | `void` | Fills the QMap\<QString,QString\> model\_to\_attribute\_map with default field names from the list of default\_attribute\_names defined in "PropertyMapper.h" |
| `fill_attribute_map_from_xml_file( QString filename, QMap<QString,QString> &model_to_attribute_map)` | function | `bool` | Fills the QMap\<QString,QString\> model\_to\_attribute\_map from the given xml file filename. |
| `fill_attribute_map_from_dialog( QString filename, QStringList &field_names, QMap<QString,QString> &model_to_attribute_map, boost::shared_ptr< GPlatesFileIO::PropertyMapper > mapper, bool remapping)` | function | `bool` | Allows the user to perform the model-property-to-shapefile-attribute mapping via a dialog. |
| `load_model_to_attribute_map_from_file_reference( QMap<QString, QString> &model_to_attribute_map, GPlatesFileIO::File::Reference &file_ref)` | function | `void` | Loads a model-to-attribute map from the specified file reference object. |
| `store_model_to_attribute_map_in_file_reference( const QMap<QString, QString> &model_to_attribute_map, GPlatesFileIO::File::Reference &file_ref)` | function | `void` | Stores the specified model-to-attribute map in the feature collection of the specified file reference object. |
| `GPLATES_FILEIO_OGRREADER_H` | macro | `None` | — |
| `SHAPE_NO_DATA` | variable | `double` | — |

## Notes

- Only the first OGR layer in a datasource is read; a datasource with more than one
  layer produces a `MultipleLayersInFile` warning and the remaining layers are
  silently ignored.
- The OGR datasource pointer (`d_data_source_ptr`) is closed in the destructor via
  `GdalUtils::close_vector`, wrapped in a `try`/`catch (...)` that swallows any
  exception — a destructor-time close failure is deliberately not surfaced.
- `read_file` throws `ErrorOpeningFileForReadingException` if the file cannot be
  opened or fails `check_file_format`, and `FileLoadAbortedException` if the user
  cancels the attribute-mapping dialog; both leave `file_ref`'s feature collection
  unpopulated.
- The static `s_property_mapper` is process-wide state set once via
  `set_property_mapper` and consulted by every subsequent `read_file` call that
  needs a new attribute mapping.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ManageFeatureCollectionsEditConfigurations](../qt-widgets/ManageFeatureCollectionsEditConfigurations.md) | qt-widgets | 5 |
| [presentation/Application](../presentation/Application.md) | presentation | 3 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 2 |
| [app-logic/FeatureCollectionFileIO](../app-logic/FeatureCollectionFileIO.md) | app-logic | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/OgrReader.h
python scripts/gpq.py def GPlatesFileIO::OgrReader --body
python scripts/gpq.py uses OgrReader --kind class
python scripts/gpq.py hier OgrReader
```

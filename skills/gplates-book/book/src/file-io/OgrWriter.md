# OgrWriter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 145 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/OgrWriter.h` | C++ | 209 |
| `src/file-io/OgrWriter.cc` | C++ | 1387 |

## Overview

`OgrWriter` is the low-level counterpart to `OgrReader`: it turns spherical
geometries (`PointOnSphere`, `MultiPointOnSphere`, `PolylineOnSphere`,
`PolygonOnSphere`) and `GpmlKeyValueDictionary` attributes into OGR features
written through a driver looked up from the target file's extension
(`get_driver_name_from_file_extension`, backed by `create_file_to_driver_map`).
Callers such as `OgrGeometryExporter` and `OgrFeatureCollectionWriter` call one
`write_*_feature` method per feature; `OgrWriter` lazily creates the OGR data
source and layer for each geometry type the first time it is needed
(`d_ogr_point_layer`, `d_ogr_multi_point_layer`, `d_ogr_polyline_layer`,
`d_ogr_polygon_layer` are all `boost::optional` for this reason) and sets the
layer's attribute field names from the first `GpmlKeyValueDictionary` it sees.

Because formats such as Shapefile can only hold one geometry type per file, the
`multiple_layers` constructor flag switches the writer into a mode that creates a
subfolder named after the output file and writes one file per geometry type inside
it (`<basename>/<basename>_point.<ext>`, `..._polyline.<ext>`, etc.); the plain
mode instead writes a single file and deletes or clears any pre-existing layers
in it before writing. `wrap_to_dateline` routes polylines and polygons through
`DateLineWrapper` before conversion to lat/lon, which matters for viewers such as
ArcGIS that render dateline-crossing geometry incorrectly otherwise. The
`original_srs`/`behaviour` pair controls whether output coordinates are
transformed back from WGS84 to the coordinate system the data was originally read
in, via `d_coordinate_transformation`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::element_type`](#anonymouselement_type) | typedef | — | — | 0 | — |
| [`(anonymous)::element_iterator_type`](#anonymouselement_iterator_type) | typedef | — | — | 0 | — |
| [`(anonymous)::file_to_driver_map_type`](#anonymousfile_to_driver_map_type) | typedef | — | — | 0 | — |
| [`(anonymous)::ogr_driver_string`](#anonymousogr_driver_string) | enum | — | — | 0 | — |
| [`(anonymous)::lat_lon_points_seq_type`](#anonymouslat_lon_points_seq_type) | typedef | — | — | 0 | Typedef for a sequence of lat/lon points. |
| [`(anonymous)::LatLonPolyline`](#anonymouslatlonpolyline) | struct | — | — | 0 | A polyline containing a single sequence of points. |
| [`(anonymous)::LatLonPolygon`](#anonymouslatlonpolygon) | struct | — | — | 0 | A polygon containing an exterior ring and optional interior rings. |
| [`GPlatesFileIO::OgrWriter`](#gplatesfileioogrwriter) | class | — | — | 0 | Uses the OGR library to write geometries and attributes to OGR-supported file formats. |

## Members

### `(anonymous)::element_type`

*None.*

### `(anonymous)::element_iterator_type`

*None.*

### `(anonymous)::file_to_driver_map_type`

*None.*

### `(anonymous)::ogr_driver_string`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FORMAT_NAME` | enumerator | `None` | — | — |
| `CODE` | enumerator | `None` | — | — |

### `(anonymous)::lat_lon_points_seq_type`

*None.*

### `(anonymous)::LatLonPolyline`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `line` | field | `lat_lon_points_seq_type` | public | — |

### `(anonymous)::LatLonPolygon`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `exterior_ring` | field | `lat_lon_points_seq_type` | public | — |
| `interior_rings` | field | `std::vector<lat_lon_points_seq_type>` | public | — |

### `GPlatesFileIO::OgrWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `OgrWriter( QString filename, bool multiple_layers, bool wrap_to_dateline, boost::optional<GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type> original_srs = boost::none, const GPlatesFileIO::FeatureCollectionFileFormat::OGRConfiguration::OgrSrsWriteBehaviour &behaviour = GPlatesFileIO::FeatureCol ...` | constructor | `None` | public | filename: target filename for output. multiple\_layers: whether or not the feature of feature collections to be written contain multiple geometry-types. wrap\_to\_dateline whether to wrap/clip polyline/polygon geometries to the dateline (for ... |
| `~OgrWriter()` | destructor | `None` | public | — |
| `write_point_feature( const GPlatesMaths::PointOnSphere &point_on_sphere, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type> &field_names_key_value_dictionary, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type> &field_values_key_ ...` | method | `void` | public | Write a point feature to a point-type layer. |
| `write_multi_point_feature( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type> &field_names_key_value_dictionary, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null ...` | method | `void` | public | — |
| `write_polyline_feature( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type> &field_names_key_value_dictionary, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_ ...` | method | `void` | public | — |
| `write_multi_polyline_feature( const std::vector<GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type> &polyline_on_sphere, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type> &field_names_key_value_dictionary, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDi ...` | method | `void` | public | — |
| `write_polygon_feature( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type> &field_names_key_value_dictionary, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_con ...` | method | `void` | public | — |
| `write_multi_polygon_feature( const std::vector<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type> &polygon_on_sphere, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type> &field_names_key_value_dictionary, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDicti ...` | method | `void` | public | — |
| `d_ogr_driver_ptr` | field | `GdalUtils::vector_data_driver_type` | private | The OGR driver. |
| `d_filename` | field | `QString` | private | Filename used by Ogr library to create a data source. |
| `d_layer_basename` | field | `QString` | private | Filename stripped of any extension for use in naming layers. |
| `d_extension` | field | `QString` | private | File extension |
| `d_multiple_geometry_types` | field | `bool` | private | True if the feature-collection/feature contains more than one geometry type. |
| `d_wrap_to_dateline` | field | `bool` | private | True if polyline/polygon geometries should be wrapped (clipped) to the dateline (for ArcGIS viewing). |
| `d_ogr_data_source_ptr` | field | `GdalUtils::vector_data_source_type` | private | — |
| `d_ogr_point_data_source_ptr` | field | `GdalUtils::vector_data_source_type` | private | Data source for each of the geometry types. |
| `d_ogr_line_data_source_ptr` | field | `GdalUtils::vector_data_source_type` | private | — |
| `d_ogr_polygon_data_source_ptr` | field | `GdalUtils::vector_data_source_type` | private | — |
| `d_ogr_point_layer` | field | `boost::optional<OGRLayer*>` | private | Pointers to the geometry layers. |
| `d_ogr_multi_point_layer` | field | `boost::optional<OGRLayer*>` | private | — |
| `d_ogr_polyline_layer` | field | `boost::optional<OGRLayer*>` | private | — |
| `d_ogr_polygon_layer` | field | `boost::optional<OGRLayer*>` | private | — |
| `d_dateline_wrapper` | field | `GPlatesMaths::DateLineWrapper::non_null_ptr_type` | private | Used to wrap/clip polyline/polygon geometries to the dateline (if enabled). |
| `d_original_srs` | field | `boost::optional<GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type>` | private | SRS of the original feature collection (if appropriate, i.e. if the collection we are writing was derived from an OGR-compatible source which provided an SRS). |
| `d_ogr_srs_write_behaviour` | field | `FeatureCollectionFileFormat::OGRConfiguration::OgrSrsWriteBehaviour` | private | — |
| `d_coordinate_transformation` | field | `GPlatesPropertyValues::CoordinateTransformation::non_null_ptr_to_const_type` | private | d\_current\_coordinate\_transformation - The coordinate transformation from WGS84 to the original SRS. |
| `write_single_or_multi_polyline_feature( const std::vector<GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type> &polylines, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type> &field_names_key_value_dictionary, const boost::optional<GPlatesPropertyValues::GpmlKeyValueD ...` | method | `void` | private | Common method to write a single polyline or multiple polylines. |
| `write_single_or_multi_polygon_feature( const std::vector<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type> &polygons, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type> &field_names_key_value_dictionary, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDict ...` | method | `void` | private | Common method to write a single polygon or multiple polygons. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `POINT_SUFFIX` | variable | `QString` | — |
| `POLYLINE_SUFFIX` | variable | `QString` | — |
| `POLYGON_SUFFIX` | variable | `QString` | — |
| `file_type_does_not_support_mixing_single_and_multi_line_strings_in_layer( const QString &extension)` | function | `bool` | — |
| `file_type_does_not_support_mixing_single_and_multi_polygons_in_layer( const QString &extension)` | function | `bool` | — |
| `file_type_does_not_support_layer_deletion( const QString &extension)` | function | `bool` | — |
| `create_file_to_driver_map()` | function | `file_to_driver_map_type` | Create a map of file extension to OGR driver information. |
| `get_driver_name_from_file_extension( QString file_extension)` | function | `QString` | — |
| `get_ogr_field_type_from_qvariant( QVariant &variant)` | function | `OGRFieldType` | — |
| `set_layer_field_names( OGRLayer *ogr_layer, const GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type &field_names_key_value_dictionary)` | function | `void` | Sets the Ogr attribute field names and types from the key\_value\_dictionary elements. |
| `set_feature_field_values( OGRLayer *ogr_layer, OGRFeature *ogr_feature, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type field_values_key_value_dictionary)` | function | `void` | Set the Ogr attribute field values from the key\_value\_dictionary. |
| `setup_layer( GPlatesFileIO::GdalUtils::vector_data_source_type *&ogr_data_source_ptr, boost::optional<OGRLayer*>& ogr_layer, OGRwkbGeometryType wkb_type, const QString &layer_name, const boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type> &field_names_key_value_dictionary, const b ...` | function | `void` | Creates an OGRLayer of type wkb\_type and adds it to the GdalUtils::vector\_data\_source\_type. |
| `create_data_source( GPlatesFileIO::GdalUtils::vector_data_driver_type *&ogr_driver, GPlatesFileIO::GdalUtils::vector_data_source_type *&data_source_ptr, QString &data_source_name)` | function | `void` | Create an ogr data source. |
| `destroy_ogr_data_source( GPlatesFileIO::GdalUtils::vector_data_source_type *&ogr_data_source)` | function | `void` | — |
| `remove_OGR_layers( GPlatesFileIO::GdalUtils::vector_data_driver_type *&ogr_driver, const QString &filename)` | function | `void` | — |
| `remove_multiple_geometry_type_files( GPlatesFileIO::GdalUtils::vector_data_driver_type *driver, const QString &folder_name, const QString &basename, const QString &extension)` | function | `void` | remove\_multiple\_geometry\_type\_files Shapefiles can only have one geometry type (point, polyline) in the file, hence export of mixed geometry types must be to separate files. |
| `convert_points_to_lat_lon( lat_lon_points_seq_type &lat_lon_points, PointsForwardIter const points_begin, PointsForwardIter const points_end, const unsigned int num_points)` | function | `void` | Converts a sequence of PointOnSphere to LatLonPoint. |
| `convert_polyline_to_lat_lon( LatLonPolyline &lat_lon_polyline, const GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type &polyline)` | function | `void` | Converts the specified PolylineOnSphere to LatLonPolyline. |
| `convert_polygon_to_lat_lon( LatLonPolygon &lat_lon_polygon, const GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type &polygon)` | function | `void` | Converts the specified PolygonOnSphere to LatLonPolygon. |
| `convert_polylines_to_lat_lon( std::vector<LatLonPolyline> &lat_lon_polylines, const std::vector<GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type> &polylines, boost::optional<GPlatesMaths::DateLineWrapper &> dateline_wrapper = boost::none)` | function | `void` | Converts the specified polyline-on-sphere geometries to lat/lon geometries with optional dateline wrapping. |
| `convert_polygons_to_lat_lon( std::vector<LatLonPolygon> &lat_lon_polygons, const std::vector<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type> &polygons, boost::optional<GPlatesMaths::DateLineWrapper &> dateline_wrapper = boost::none)` | function | `void` | Converts the specified polygon-on-sphere geometries to lat/lon geometries with optional dateline wrapping. |
| `add_polyline_to_ogr_line_string( OGRLineString &ogr_line_string, const LatLonPolyline &lat_lon_polyline, const GPlatesPropertyValues::CoordinateTransformation::non_null_ptr_to_const_type &coordinate_transformation)` | function | `void` | — |
| `add_multi_polyline_to_ogr_feature( OGRFeature &ogr_feature, const std::vector<LatLonPolyline> &lat_lon_polylines, const GPlatesPropertyValues::CoordinateTransformation::non_null_ptr_to_const_type &coordinate_transformation)` | function | `void` | — |
| `add_polyline_to_ogr_feature( OGRFeature &ogr_feature, const LatLonPolyline &lat_lon_polyline, const GPlatesPropertyValues::CoordinateTransformation::non_null_ptr_to_const_type &coordinate_transformation)` | function | `void` | — |
| `add_polygon_ring_to_ogr_polygon( OGRPolygon &ogr_polygon, const lat_lon_points_seq_type &lat_lon_polygon_ring, const GPlatesPropertyValues::CoordinateTransformation::non_null_ptr_to_const_type &coordinate_transformation)` | function | `void` | — |
| `add_polygon_to_ogr_polygon( OGRPolygon &ogr_polygon, const LatLonPolygon &lat_lon_polygon, const GPlatesPropertyValues::CoordinateTransformation::non_null_ptr_to_const_type &coordinate_transformation)` | function | `void` | — |
| `add_multi_polygon_to_ogr_feature( OGRFeature &ogr_feature, const std::vector<LatLonPolygon> &lat_lon_polygons, const GPlatesPropertyValues::CoordinateTransformation::non_null_ptr_to_const_type &coordinate_transformation)` | function | `void` | — |
| `add_polygon_to_ogr_feature( OGRFeature &ogr_feature, const LatLonPolygon &lat_lon_polygon, const GPlatesPropertyValues::CoordinateTransformation::non_null_ptr_to_const_type &coordinate_transformation)` | function | `void` | — |
| `GPLATES_FILEIO_OGRWRITER_H` | macro | `None` | — |

## Notes

- The constructor requires the destination directory to already exist — it throws
  `ErrorOpeningFileForWritingException` if not — but will create the per-geometry-type
  subfolder itself when `multiple_layers` is true.
- The destructor closes all four possible data sources
  (`d_ogr_data_source_ptr`, and the point/line/polygon ones) unconditionally via
  `destroy_ogr_data_source`; the `d_ogr_*_layer` pointers are non-owning, since the
  layer's lifetime belongs to its data source.
- Re-running an export to the same non-multi-layer file removes any OGR layers
  already in it first (or deletes the file outright for formats that cannot
  delete individual layers), so a prior export at that path is fully replaced,
  not appended to.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrFeatureCollectionWriter](OgrFeatureCollectionWriter.md) | file-io | 15 |
| [file-io/OgrGeometryExporter](OgrGeometryExporter.md) | file-io | 8 |
| [api/CoReg](../api/CoReg.md) | api | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/OgrWriter.h
python scripts/gpq.py def GPlatesFileIO::OgrWriter --body
python scripts/gpq.py uses OgrWriter --kind class
python scripts/gpq.py hier OgrWriter
```

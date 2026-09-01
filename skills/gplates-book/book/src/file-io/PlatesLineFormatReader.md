# PlatesLineFormatReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 80 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/PlatesLineFormatReader.h` | C++ | 59 |
| `src/file-io/PlatesLineFormatReader.cc` | C++ | 2200 |

## Overview

Reads GPlates feature data from PLATES line-format files and converts them to GPlates GPML features. Maps PLATES4 header data type codes to appropriate GPML feature types (faults, ridges, subduction zones, etc.), parses pen-coded coordinate sequences into geometries (points, polylines, polygons, multipoints), and creates `GpmlOldPlatesHeader` records preserving metadata from the original PLATES format. Supports topology-related features and complex boundary descriptions.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::PlotterCodes::PlotterCode`](#anonymousplottercodesplottercode) | enum | — | — | 0 | These plotter codes are used to pass and return expected and actual pen codes. |
| [`(anonymous)::point_seq_type`](#anonymouspoint_seq_type) | typedef | — | — | 0 | Typedef for a sequence of points. |
| [`(anonymous)::geometry_seq_type`](#anonymousgeometry_seq_type) | typedef | — | — | 0 | Typedef for a sequence of geometries (each containing a sequence of points). |
| [`(anonymous)::old_id_to_new_id_map_type`](#anonymousold_id_to_new_id_map_type) | typedef | — | — | 0 | Typedef for map from old GP8 id to GP9 feature id |
| [`(anonymous)::old_id_to_new_id_map_const_iterator`](#anonymousold_id_to_new_id_map_const_iterator) | typedef | — | — | 0 | — |
| [`(anonymous)::creation_map_type`](#anonymouscreation_map_type) | typedef | — | — | 0 | — |
| [`(anonymous)::creation_map_const_iterator`](#anonymouscreation_map_const_iterator) | typedef | — | — | 0 | — |
| [`(anonymous)::warning_map_type`](#anonymouswarning_map_type) | typedef | — | — | 0 | — |
| [`(anonymous)::warning_map_const_iterator`](#anonymouswarning_map_const_iterator) | typedef | — | — | 0 | — |
| [`GPlatesFileIO::PlatesLineFormatReader`](#gplatesfileioplateslineformatreader) | class | — | — | 0 | — |

## Members

### `(anonymous)::PlotterCodes::PlotterCode`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PEN_DRAW_TO` | enumerator | `None` | — | — |
| `PEN_SKIP_TO` | enumerator | `None` | — | — |
| `PEN_TERMINATING_POINT` | enumerator | `None` | — | — |
| `PEN_EITHER` | enumerator | `None` | — | — |

### `(anonymous)::point_seq_type`

*None.*

### `(anonymous)::geometry_seq_type`

*None.*

### `(anonymous)::old_id_to_new_id_map_type`

*None.*

### `(anonymous)::old_id_to_new_id_map_const_iterator`

*None.*

### `(anonymous)::creation_map_type`

*None.*

### `(anonymous)::creation_map_const_iterator`

*None.*

### `(anonymous)::warning_map_type`

*None.*

### `(anonymous)::warning_map_const_iterator`

*None.*

### `GPlatesFileIO::PlatesLineFormatReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `read_file( File::Reference &file, ReadErrorAccumulation &read_errors, bool &contains_unsaved_changes)` | method | `void` | public | Read the PLATES line-format file specified by fileinfo. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `id_map` | variable | `old_id_to_new_id_map_type` | — |
| `sequence_is_valid_multipoint( const geometry_seq_type &geometry_seq)` | function | `bool` | Checks that geometry\_seq is appropriate for constructing a multipoint. |
| `create_gpml_topological_point( QString old_fid)` | function | `GPlatesPropertyValues::GpmlTopologicalPoint::non_null_ptr_type` | — |
| `create_gpml_topological_line_section( QString old_fid, bool use_reverse)` | function | `GPlatesPropertyValues::GpmlTopologicalLineSection::non_null_ptr_type` | — |
| `create_gpml_topological_sections_vector( GPlatesModel::FeatureHandle::weak_ref feature_ref, const std::vector<QString> &boundary_strings)` | function | `std::vector<GPlatesPropertyValues::GpmlTopologicalSection::non_null_ptr_type>` | — |
| `create_gpml_piecewise_aggregation( GPlatesModel::FeatureHandle::weak_ref feature_ref, const std::vector<QString> &boundary_strings )` | function | `GPlatesPropertyValues::GpmlPiecewiseAggregation::non_null_ptr_type` | — |
| `extract_feature_id_from_header( GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, GPlatesUtils::UnicodeString &feature_id)` | function | `bool` | Attempts to extract a feature id from PLATES header. |
| `create_feature( const GPlatesModel::FeatureType &feature_type, GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header)` | function | `GPlatesModel::FeatureHandle::weak_ref` | Creates a feature of type feature\_type. |
| `append_appropriate_geometry( const point_seq_type &points, const GPlatesModel::PropertyName &property_name, GPlatesModel::FeatureHandle::weak_ref &feature)` | function | `void` | This function assumes that 'create\_feature\_with\_geometries' has ensured that 'points' contains at least one point. |
| `create_geo_time_instant( const double &time)` | function | `GPlatesPropertyValues::GeoTimeInstant` | — |
| `create_common( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq, const GPlatesModel::FeatureType &feature_type, const GPlatesModel::PropertyName &geometry_property_name)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_multi_point_feature( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq, const GPlatesModel::FeatureType &feature_type, const GPlatesModel::PropertyName &geometry_property_name)` | function | `GPlatesModel::FeatureHandle::weak_ref` | Create a multipoint feature. |
| `create_single_point_feature( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq, const GPlatesModel::FeatureType &feature_type, const GPlatesModel::PropertyName &geometry_property_name)` | function | `GPlatesModel::FeatureHandle::weak_ref` | Creates a GPML feature from PLATES data where the GPML feature accepts a single point only. |
| `create_fault( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_normal_fault( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_reverse_fault( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_thrust_fault( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_strike_slip_fault( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_unclassified_feature( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_aseismic_ridge( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_bathymetry( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_basin( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_coastline( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_continental_boundary( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_continental_fragment( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_craton( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_extended_continental_crust( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_fracture_zone( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_gravimetry( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_grid_mark( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_heat_flow( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_hot_spot( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_hot_spot_trail( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_inferred_paleo_boundary( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_island_arc( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq, bool is_active)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_island_arc_active( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_island_arc_inactive( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_isochron( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_isopach( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_geological_lineation( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_magnetics( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_magnetic_pick( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_mid_ocean_ridge( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq, bool is_active)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_ridge_segment( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_extinct_ridge( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_ophiolite_belt( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_orogenic_belt( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_seamount( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_slab( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_subduction_zone( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq, bool is_active, const char *subduction_polarity_enumeration_content = "Unknown")` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_subduction_zone_active( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_subduction_zone_inactive( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_subduction_zone_left( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_subduction_zone_right( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_suture( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_terrane_boundary( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_transitional_crust( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_transform( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_topography( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_volcano( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_pluton( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_political_boundary( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_large_igneous_province( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_navdat_1( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_navdat_2( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_navdat_3( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_navdat_4( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `create_topological_closed_plate_boundary( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, const geometry_seq_type &geometry_seq)` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `null_warning_function( GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, GPlatesFileIO::LineReader &in, const boost::shared_ptr<GPlatesFileIO::DataSource> &source, GPlatesFileIO::ReadErrorAccumulation &errors)` | function | `void` | — |
| `warning_unknown_data_type_code( GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, GPlatesFileIO::LineReader &in, const boost::shared_ptr<GPlatesFileIO::DataSource> &source, GPlatesFileIO::ReadErrorAccumulation &errors)` | function | `void` | — |
| `warning_ice_shelf_ambiguity( GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type &header, GPlatesFileIO::LineReader &in, const boost::shared_ptr<GPlatesFileIO::DataSource> &source, GPlatesFileIO::ReadErrorAccumulation &errors)` | function | `void` | — |
| `read_old_plates_header( GPlatesFileIO::LineReader &in, const QString &first_line)` | function | `GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type` | — |
| `read_polyline_point( GPlatesFileIO::LineReader &in, point_seq_type &points, PlotterCodes::PlotterCode expected_code)` | function | `PlotterCodes::PlotterCode` | — |
| `read_platepolygon_boundary_feature( GPlatesFileIO::LineReader &in, std::vector<QString> &boundary_strings, QString code)` | function | `QString` | This function reads a series of lines from the input file and copies the data to a list of strings |
| `create_feature_with_geometries( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesFileIO::LineReader &in, const boost::shared_ptr<GPlatesFileIO::DataSource> &source, creation_function_type creation_function, GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type old_plates_header, const geometr ...` | function | `void` | — |
| `test_validity_of_points( const point_seq_type &point_seq, GPlatesFileIO::LineReader &in, const boost::shared_ptr<GPlatesFileIO::DataSource> &source, GPlatesFileIO::ReadErrorAccumulation &errors)` | function | `bool` | Checks to make sure valid geometry can be constructed from the points. |
| `add_points_to_new_geometry( geometry_seq_type &geometry_seq, point_seq_type &point_seq, GPlatesFileIO::LineReader &in, const boost::shared_ptr<GPlatesFileIO::DataSource> &source, GPlatesFileIO::ReadErrorAccumulation &errors)` | function | `void` | Add points to a list of geometries for a feature. |
| `read_feature( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, GPlatesFileIO::LineReader &in, const boost::shared_ptr<GPlatesFileIO::DataSource> &source, GPlatesFileIO::ReadErrorAccumulation &errors)` | function | `void` | — |
| `GPLATES_FILEIO_PLATESLINEFORMATREADER_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/PlatesLineFormatReader.h
python scripts/gpq.py def GPlatesFileIO::PlatesLineFormatReader --body
python scripts/gpq.py uses PlatesLineFormatReader --kind class
python scripts/gpq.py hier PlatesLineFormatReader
```

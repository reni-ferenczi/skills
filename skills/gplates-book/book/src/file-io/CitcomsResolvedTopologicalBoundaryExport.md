# CitcomsResolvedTopologicalBoundaryExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 172 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/CitcomsResolvedTopologicalBoundaryExport.h` | C++ | 402 |
| `src/file-io/CitcomsResolvedTopologicalBoundaryExport.cc` | C++ | 1614 |

## Overview

[[[PROSE overview unit=file-io/CitcomsResolvedTopologicalBoundaryExport tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExport::(anonymous)::Output`](#gplatesfileiocitcomsresolvedtopologicalboundaryexportanonymousoutput) | struct | — | — | 0 | The output data to be exported. |
| [`GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExport::Format`](#gplatesfileiocitcomsresolvedtopologicalboundaryexportformat) | enum | — | — | 0 | Formats of files that can export resolved topological boundaries. |
| [`GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExport::OutputOptions`](#gplatesfileiocitcomsresolvedtopologicalboundaryexportoutputoptions) | struct | — | — | 0 | NOTE: check default\_citcoms\_resolved\_topology\_export\_options in gui/ExportAnimationRegistry.cc for the boolean defaults created in the actual gui |

## Members

### `GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExport::(anonymous)::Output`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `all_polygons` | field | `resolved_topologies_seq_type` | public | all polygons |
| `all_boundaries` | field | `sub_segment_group_seq_type` | public | all polygon sub\_segment types |
| `all_boundaries_ridge_transform` | field | `sub_segment_group_seq_type` | public | — |
| `all_boundaries_subduction` | field | `sub_segment_group_seq_type` | public | — |
| `all_boundaries_subduction_left` | field | `sub_segment_group_seq_type` | public | — |
| `all_boundaries_subduction_right` | field | `sub_segment_group_seq_type` | public | — |
| `plate_polygons` | field | `resolved_topologies_seq_type` | public | plate polygons |
| `plate_boundaries` | field | `sub_segment_group_seq_type` | public | plate polygon sub\_segment types |
| `plate_boundaries_ridge_transform` | field | `sub_segment_group_seq_type` | public | — |
| `plate_boundaries_subduction` | field | `sub_segment_group_seq_type` | public | — |
| `plate_boundaries_subduction_left` | field | `sub_segment_group_seq_type` | public | — |
| `plate_boundaries_subduction_right` | field | `sub_segment_group_seq_type` | public | — |
| `network_polygons` | field | `resolved_topologies_seq_type` | public | network polygons |
| `network_boundaries` | field | `sub_segment_group_seq_type` | public | network polygon sub\_segment types |
| `network_boundaries_ridge_transform` | field | `sub_segment_group_seq_type` | public | — |
| `network_boundaries_subduction` | field | `sub_segment_group_seq_type` | public | — |
| `network_boundaries_subduction_left` | field | `sub_segment_group_seq_type` | public | — |
| `network_boundaries_subduction_right` | field | `sub_segment_group_seq_type` | public | — |
| `slab_polygons` | field | `resolved_topologies_seq_type` | public | slab polygons |
| `slab_edges` | field | `sub_segment_group_seq_type` | public | slab polygon sub\_segment types |
| `slab_edges_leading` | field | `sub_segment_group_seq_type` | public | — |
| `slab_edges_leading_left` | field | `sub_segment_group_seq_type` | public | — |
| `slab_edges_leading_right` | field | `sub_segment_group_seq_type` | public | — |
| `slab_edges_trench` | field | `sub_segment_group_seq_type` | public | — |
| `slab_edges_side` | field | `sub_segment_group_seq_type` | public | — |

### `GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExport::Format`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UNKNOWN` | enumerator | `None` | — | — |
| `GMT` | enumerator | `None` | — | — |
| `SHAPEFILE` | enumerator | `None` | — | — |
| `OGRGMT` | enumerator | `None` | — | — |
| `GEOJSON` | enumerator | `None` | — | — |

### `GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExport::OutputOptions`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `OutputOptions( // Wrap polyline/polygon geometries to the dateline (mainly useful for ArcGIS shapefile users)... bool wrap_geometries_to_the_dateline_ = true, // // all polygon options // bool export_plate_polygons_to_all_polygons_file_ = false, bool export_network_polygons_to_all_polygons_file_ = false, bool export_sl ...` | constructor | `None` | public | — |
| `wrap_geometries_to_the_dateline` | field | `bool` | public | Wrap polyline/polygon geometries to the dateline (mainly useful for ArcGIS shapefile users)... |
| `export_plate_polygons_to_all_polygons_file` | field | `bool` | public | all polygon options |
| `export_network_polygons_to_all_polygons_file` | field | `bool` | public | — |
| `export_slab_polygons_to_all_polygons_file` | field | `bool` | public | — |
| `export_plate_boundaries_to_all_boundaries_file` | field | `bool` | public | — |
| `export_network_boundaries_to_all_boundaries_file` | field | `bool` | public | — |
| `export_slab_boundaries_to_all_boundaries_file` | field | `bool` | public | — |
| `export_individual_plate_polygon_files` | field | `bool` | public | plate polygon options |
| `export_plate_polygons_to_a_single_file` | field | `bool` | public | — |
| `export_plate_boundaries` | field | `bool` | public | — |
| `export_individual_network_polygon_files` | field | `bool` | public | network polygon options |
| `export_network_polygons_to_a_single_file` | field | `bool` | public | — |
| `export_network_boundaries` | field | `bool` | public | — |
| `export_individual_slab_polygon_files` | field | `bool` | public | slab polygon options |
| `export_slab_polygons_to_a_single_file` | field | `bool` | public | — |
| `export_slab_boundaries` | field | `bool` | public | — |
| `placeholder_all_polygons` | field | `QString` | public | all polygon place holders |
| `placeholder_all_boundaries` | field | `QString` | public | — |
| `placeholder_all_boundaries_ridge_transform` | field | `QString` | public | — |
| `placeholder_all_boundaries_subduction` | field | `QString` | public | — |
| `placeholder_all_boundaries_subduction_left` | field | `QString` | public | — |
| `placeholder_all_boundaries_subduction_right` | field | `QString` | public | — |
| `placeholder_plate_polygons` | field | `QString` | public | plate polygon place holders |
| `placeholder_plate_boundaries` | field | `QString` | public | — |
| `placeholder_plate_boundaries_ridge_transform` | field | `QString` | public | — |
| `placeholder_plate_boundaries_subduction` | field | `QString` | public | — |
| `placeholder_plate_boundaries_subduction_left` | field | `QString` | public | — |
| `placeholder_plate_boundaries_subduction_right` | field | `QString` | public | — |
| `placeholder_networks` | field | `QString` | public | network placeholder string. |
| `placeholder_network_boundaries` | field | `QString` | public | — |
| `placeholder_network_boundaries_ridge_transform` | field | `QString` | public | — |
| `placeholder_network_boundaries_subduction` | field | `QString` | public | — |
| `placeholder_network_boundaries_subduction_left` | field | `QString` | public | — |
| `placeholder_network_boundaries_subduction_right` | field | `QString` | public | — |
| `placeholder_slab_polygons` | field | `QString` | public | slab polygon subsegments placeholder strings. |
| `placeholder_slab_edges` | field | `QString` | public | — |
| `placeholder_slab_edges_leading` | field | `QString` | public | — |
| `placeholder_slab_edges_leading_left` | field | `QString` | public | — |
| `placeholder_slab_edges_leading_right` | field | `QString` | public | — |
| `placeholder_slab_edges_trench` | field | `QString` | public | — |
| `placeholder_slab_edges_side` | field | `QString` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DISABLE_MSVC_WARNING` | variable | `PUSH_MSVC_WARNINGS` | — |
| `append_suffix_to_template_filebasename( const QFileInfo &original_template_filename, QString suffix)` | function | `QString` | — |
| `substitute_placeholder( const QString &output_filebasename, const QString &placeholder, const QString &placeholder_replacement)` | function | `QString` | — |
| `get_full_output_filename( const QDir &target_dir, const QString &filebasename, const QString &placeholder_string, const QString &placeholder_replacement)` | function | `QString` | — |
| `get_unique_list_of_referenced_files( referenced_files_collection_type &referenced_files, const sub_segment_group_seq_type &sub_segment_groups, const feature_handle_to_collection_map_type &feature_handle_to_collection_map)` | function | `void` | Returns a unique list of files that contain the subsegment features. |
| `add_topological_closed_plate_boundary_sub_segments( const GPlatesAppLogic::ReconstructionGeometry *resolved_geom, const double &reconstruction_time, const OutputOptions &output_options, Output &output)` | function | `void` | — |
| `add_topological_closed_plate_boundary( const GPlatesAppLogic::ReconstructionGeometry *resolved_geom, const double &reconstruction_time, const OutputOptions &output_options, Output &output)` | function | `void` | — |
| `add_topological_network_boundary_sub_segments( const GPlatesAppLogic::ReconstructionGeometry *resolved_geom, const double &reconstruction_time, const OutputOptions &output_options, Output &output)` | function | `void` | — |
| `add_topological_network_boundary( const GPlatesAppLogic::ReconstructionGeometry *resolved_geom, const double &reconstruction_time, const OutputOptions &output_options, Output &output)` | function | `void` | — |
| `add_topological_slab_boundary_sub_segments( const GPlatesAppLogic::ReconstructionGeometry *resolved_geom, const double &reconstruction_time, const OutputOptions &output_options, Output &output)` | function | `void` | — |
| `add_topological_slab_boundary( const GPlatesAppLogic::ReconstructionGeometry *resolved_geom, const double &reconstruction_time, const OutputOptions &output_options, Output &output)` | function | `void` | — |
| `collect_exports( const std::vector<const GPlatesAppLogic::ReconstructionGeometry *> &resolved_geoms, const double &reconstruction_time, const OutputOptions &output_options, Output &output)` | function | `void` | — |
| `export_resolved_topological_boundaries_file( const QString &filename, Format export_format, const resolved_topologies_seq_type &resolved_topologies, const std::vector<const File::Reference *> &referenced_files, const std::vector<const File::Reference *> &active_reconstruction_files, const GPlatesModel::integer_plate_id ...` | function | `void` | Exports a sequence of resolved topological boundaries to the specified export file format. |
| `export_sub_segments_file( const QString &filename, Format export_format, const sub_segment_group_seq_type &sub_segment_groups, const std::vector<const File::Reference *> &referenced_files, const std::vector<const File::Reference *> &active_reconstruction_files, const GPlatesModel::integer_plate_id_type &reconstruction_ ...` | function | `void` | Exports a sequence of subsegments of resolved topological boundaries to the specified export file format. |
| `export_resolved_topological_boundaries( const QDir &target_dir, const QString &file_basename, const QString &placeholder_format_string, Format export_format, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id, const double &reconstruction_time, const QString &placeholder, const resolved_topologie ...` | function | `void` | — |
| `export_sub_segments( const QDir &target_dir, const QString &file_basename, const QString &placeholder_format_string, Format export_format, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id, const double &reconstruction_time, const QString &placeholder, const sub_segment_group_seq_type &sub_segme ...` | function | `void` | — |
| `output_exports( const QDir &target_dir, const QString &file_basename, const QString &placeholder_format_string, Format export_format, const std::vector<const File::Reference *> &loaded_files, const std::vector<const File::Reference *> &active_reconstruction_files, const GPlatesModel::integer_plate_id_type &reconstructi ...` | function | `void` | — |
| `GPLATES_FILE_IO_CITCOMSRESOLVEDTOPOLOGICALBOUNDARYEXPORT_H` | macro | `None` | — |
| `get_export_file_format( const QFileInfo& file_info, const FeatureCollectionFileFormat::Registry &file_format_registry)` | function | `Format` | Determine type of export file format based on filename extension. |
| `export_resolved_topological_boundaries( const QDir &target_dir, const QString &file_basename, const QString &placeholder_format_string, const OutputOptions &output_options, Format export_format, const std::vector<const GPlatesAppLogic::ReconstructionGeometry *> &resolved_topologies, const std::vector<const File::Refere ...` | function | `void` | Exports resolved topologies and associated subsegments as specified by the options in output\_options. |

## Notes

[[[PROSE notes unit=file-io/CitcomsResolvedTopologicalBoundaryExport tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 92 |
| [qt-widgets/ExportCitcomsResolvedTopologyOptionsWidget](../qt-widgets/ExportCitcomsResolvedTopologyOptionsWidget.md) | qt-widgets | 32 |
| [gui/ExportCitcomsResolvedTopologyAnimationStrategy](../gui/ExportCitcomsResolvedTopologyAnimationStrategy.md) | gui | 15 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/CitcomsResolvedTopologicalBoundaryExport.h
python scripts/gpq.py def GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExport::OutputOptions --body
python scripts/gpq.py uses OutputOptions --kind struct
python scripts/gpq.py hier OutputOptions
```

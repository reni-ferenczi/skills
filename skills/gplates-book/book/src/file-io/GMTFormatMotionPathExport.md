# GMTFormatMotionPathExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 987 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GMTFormatMotionPathExport.h` | C++ | 75 |
| `src/file-io/GMTFormatMotionPathExport.cc` | C++ | 362 |

## Overview

Exports reconstructed motion paths to GMT format. A motion path records the trajectory of a plate-motion reference point as it travels through geologic time. This exporter writes `ReconstructedMotionPath` objects to a GMT file with their geometry (seed point and traced path) evaluated at specified time steps. Output includes GMT headers recording source data and reconstruction parameters, with coordinates in GMT xy-format.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::referenced_files_collection_type`](#anonymousreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |
| [`(anonymous)::reconstructed_motion_path_seq_type`](#anonymousreconstructed_motion_path_seq_type) | typedef | — | — | 0 | Convenience typedef for a sequence of ReconstructedMotionPath objects. |
| [`GPlatesFileIO::GMTFormatMotionPathsExport::feature_geometry_group_type`](#gplatesfileiogmtformatmotionpathsexportfeature_geometry_group_type) | typedef | — | — | 0 | Typedef for a feature geometry group of ReconstructedMotionPath objects. |
| [`GPlatesFileIO::GMTFormatMotionPathsExport::referenced_files_collection_type`](#gplatesfileiogmtformatmotionpathsexportreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |

## Members

### `(anonymous)::referenced_files_collection_type`

*None.*

### `(anonymous)::reconstructed_motion_path_seq_type`

*None.*

### `GPlatesFileIO::GMTFormatMotionPathsExport::feature_geometry_group_type`

*None.*

### `GPlatesFileIO::GMTFormatMotionPathsExport::referenced_files_collection_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `print_gmt_coordinate_line( QTextStream &stream, const GPlatesMaths::Real &lat, const GPlatesMaths::Real &lon, const double &time, bool reverse_coordinate_order)` | function | `void` | Adapted from GMTFormatGeometryExporter |
| `write_seed_point_to_stream( QTextStream &text_stream, const GPlatesAppLogic::ReconstructedMotionPath &rf)` | function | `void` | — |
| `write_motion_path_to_stream( QTextStream &text_stream, const GPlatesAppLogic::ReconstructedMotionPath &rmp, const std::vector<double> &times)` | function | `void` | — |
| `get_points_from_multipoint( std::vector<GPlatesMaths::LatLonPoint> &points, GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | function | `void` | — |
| `get_global_header_lines( std::vector<QString> &global_header_lines, const GPlatesFileIO::GMTFormatMotionPathsExport::referenced_files_collection_type referenced_files, const GPlatesFileIO::GMTFormatMotionPathsExport::referenced_files_collection_type active_reconstruction_files, const GPlatesModel::integer_plate_id_type ...` | function | `void` | — |
| `get_feature_header_lines_from_feature_ref( std::vector<QString> &header_lines, const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref, std::vector<double> &times)` | function | `void` | — |
| `GPLATES_FILEIO_GMTFORMATMOTIONPATHSEXPORT_H` | macro | `None` | — |
| `export_motion_paths( const std::list<feature_geometry_group_type> &feature_geometry_group_seq, const QFileInfo &qfile_info, const referenced_files_collection_type &referenced_files, const referenced_files_collection_type &active_reconstruction_files, const GPlatesModel::integer_plate_id_type &anchor_plate_id, const dou ...` | function | `void` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/ReconstructedMotionPathExport](ReconstructedMotionPathExport.md) | file-io | 7 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GMTFormatMotionPathExport.h
python scripts/gpq.py def (anonymous)::referenced_files_collection_type --body
python scripts/gpq.py uses referenced_files_collection_type --kind typedef
```

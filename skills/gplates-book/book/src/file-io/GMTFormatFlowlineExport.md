# GMTFormatFlowlineExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 938 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GMTFormatFlowlineExport.h` | C++ | 73 |
| `src/file-io/GMTFormatFlowlineExport.cc` | C++ | 396 |

## Overview

Exports reconstructed flowlines to GMT format. A flowline is a path traced by a plate-motion reference point as it moves through geologic time; this exporter writes `ReconstructedFlowline` objects to a GMT-compatible file with their geometry (seed point and traced path) at specified time steps. The output includes GMT headers recording the source files and reconstruction parameters, with spatial coordinates in the GMT xy-format.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::referenced_files_collection_type`](#anonymousreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |
| [`(anonymous)::reconstructed_flowline_seq_type`](#anonymousreconstructed_flowline_seq_type) | typedef | — | — | 0 | Convenience typedef for a sequence of ReconstructedFlowline objects. |
| [`GPlatesFileIO::GMTFormatFlowlinesExport::feature_geometry_group_type`](#gplatesfileiogmtformatflowlinesexportfeature_geometry_group_type) | typedef | — | — | 0 | Typedef for a feature geometry group of ReconstructedFlowline objects. |
| [`GPlatesFileIO::GMTFormatFlowlinesExport::referenced_files_collection_type`](#gplatesfileiogmtformatflowlinesexportreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |

## Members

### `(anonymous)::referenced_files_collection_type`

*None.*

### `(anonymous)::reconstructed_flowline_seq_type`

*None.*

### `GPlatesFileIO::GMTFormatFlowlinesExport::feature_geometry_group_type`

*None.*

### `GPlatesFileIO::GMTFormatFlowlinesExport::referenced_files_collection_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `print_gmt_coordinate_line( QTextStream &stream, const GPlatesMaths::Real &lat, const GPlatesMaths::Real &lon, const double &time, bool reverse_coordinate_order)` | function | `void` | Adapted from GMTFormatGeometryExporter |
| `write_seed_point_to_stream( QTextStream &text_stream, const GPlatesAppLogic::ReconstructedFlowline &rf)` | function | `void` | — |
| `write_flowline_to_stream( QTextStream &text_stream, const GPlatesAppLogic::ReconstructedFlowline &rf, const std::vector<double> &times)` | function | `void` | — |
| `get_export_times( std::vector<double> &export_times, const std::vector<double> &times, const double &reconstruction_time)` | function | `void` | — |
| `get_points_from_multipoint( std::vector<GPlatesMaths::LatLonPoint> &points, GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | function | `void` | — |
| `get_global_header_lines( std::vector<QString> &global_header_lines, const GPlatesFileIO::GMTFormatFlowlinesExport::referenced_files_collection_type referenced_files, const GPlatesFileIO::GMTFormatFlowlinesExport::referenced_files_collection_type active_reconstruction_files, const GPlatesModel::integer_plate_id_type &an ...` | function | `void` | — |
| `get_feature_header_lines_from_feature_ref( std::vector<QString> &header_lines, const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref, std::vector<double> &times)` | function | `void` | — |
| `GPLATES_FILEIO_GMTFORMATFLOWLINESEXPORT_H` | macro | `None` | — |
| `export_flowlines( const std::list<feature_geometry_group_type> &feature_geometry_group_seq, const QFileInfo &qfile_info, const referenced_files_collection_type referenced_files, const referenced_files_collection_type active_reconstruction_files, const GPlatesModel::integer_plate_id_type &anchor_plate_id, const double & ...` | function | `void` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/ReconstructedFlowlineExport](ReconstructedFlowlineExport.md) | file-io | 7 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GMTFormatFlowlineExport.h
python scripts/gpq.py def (anonymous)::referenced_files_collection_type --body
python scripts/gpq.py uses referenced_files_collection_type --kind typedef
```

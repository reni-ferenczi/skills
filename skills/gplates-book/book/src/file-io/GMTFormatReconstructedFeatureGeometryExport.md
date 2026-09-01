# GMTFormatReconstructedFeatureGeometryExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 272 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GMTFormatReconstructedFeatureGeometryExport.h` | C++ | 72 |
| `src/file-io/GMTFormatReconstructedFeatureGeometryExport.cc` | C++ | 185 |

## Overview

Exports reconstructed feature geometries to GMT format. The exporter writes `ReconstructedFeatureGeometry` objects (geometric features rotated to a given reconstruction time) to a GMT-compatible file. Each geometry is written as a GMT dataset segment, with optional filtering to exclude certain feature types. Output includes GMT headers recording the source data and reconstruction parameters.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GMTFormatReconstructedFeatureGeometryExport::(anonymous)::reconstructed_feature_geom_seq_type`](#gplatesfileiogmtformatreconstructedfeaturegeometryexportanonymousreconstructed_feature_geom_seq_type) | typedef | — | — | 0 | Convenience typedef for a sequence of RFGs. |
| [`GPlatesFileIO::GMTFormatReconstructedFeatureGeometryExport::feature_geometry_group_type`](#gplatesfileiogmtformatreconstructedfeaturegeometryexportfeature_geometry_group_type) | typedef | — | — | 0 | Typedef for a feature geometry group of ReconstructedFeatureGeometry objects. |
| [`GPlatesFileIO::GMTFormatReconstructedFeatureGeometryExport::referenced_files_collection_type`](#gplatesfileiogmtformatreconstructedfeaturegeometryexportreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |

## Members

### `GPlatesFileIO::GMTFormatReconstructedFeatureGeometryExport::(anonymous)::reconstructed_feature_geom_seq_type`

*None.*

### `GPlatesFileIO::GMTFormatReconstructedFeatureGeometryExport::feature_geometry_group_type`

*None.*

### `GPlatesFileIO::GMTFormatReconstructedFeatureGeometryExport::referenced_files_collection_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `feature_is_of_type_to_exclude( const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref)` | function | `bool` | ! |
| `get_global_header_lines( std::vector<QString>& header_lines, const referenced_files_collection_type &referenced_files, const referenced_files_collection_type &active_reconstruction_files, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id, const double &reconstruction_time)` | function | `void` | Prints GMT format header at top of the exported file containing information about the reconstruction that is not per-feature information. |
| `GPLATES_FILEIO_GMTFORMATRECONSTRUCTEDFEATUREGEOMETRYEXPORT_H` | macro | `None` | — |
| `export_geometries( const std::list<feature_geometry_group_type> &feature_geometry_group_seq, const QFileInfo& file_info, const referenced_files_collection_type &referenced_files, const referenced_files_collection_type &active_reconstruction_files, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_i ...` | function | `void` | Exports ReconstructedFeatureGeometry objects to GMT format. |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/ReconstructedFeatureGeometryExport](ReconstructedFeatureGeometryExport.md) | file-io | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GMTFormatReconstructedFeatureGeometryExport.h
python scripts/gpq.py def GPlatesFileIO::GMTFormatReconstructedFeatureGeometryExport::(anonymous)::reconstructed_feature_geom_seq_type --body
python scripts/gpq.py uses reconstructed_feature_geom_seq_type --kind typedef
```

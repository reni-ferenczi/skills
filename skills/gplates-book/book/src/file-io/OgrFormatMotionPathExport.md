# OgrFormatMotionPathExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1316 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/OgrFormatMotionPathExport.h` | C++ | 77 |
| `src/file-io/OgrFormatMotionPathExport.cc` | C++ | 224 |

## Overview

Exports `ReconstructedMotionPath` objects to ESRI Shapefile format, with motion path geometries and generation metadata (feature name, seed points, anchor plate, reconstruction time) encoded as shapefile attributes. Each reconstructed motion path yields one geometry in the output: the polyline traced by the moving point.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::referenced_files_collection_type`](#anonymousreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |
| [`(anonymous)::reconstructed_motion_path_seq_type`](#anonymousreconstructed_motion_path_seq_type) | typedef | — | — | 0 | Convenience typedef for a sequence of ReconstructedMotionPath objects. |
| [`GPlatesFileIO::OgrFormatMotionPathExport::feature_geometry_group_type`](#gplatesfileioogrformatmotionpathexportfeature_geometry_group_type) | typedef | — | — | 0 | Typedef for a feature geometry group of ReconstructedMotionPath objects. |
| [`GPlatesFileIO::OgrFormatMotionPathExport::referenced_files_collection_type`](#gplatesfileioogrformatmotionpathexportreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |

## Members

### `(anonymous)::referenced_files_collection_type`

*None.*

### `(anonymous)::reconstructed_motion_path_seq_type`

*None.*

### `GPlatesFileIO::OgrFormatMotionPathExport::feature_geometry_group_type`

*None.*

### `GPlatesFileIO::OgrFormatMotionPathExport::referenced_files_collection_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `make_seed_string( const GPlatesAppLogic::ReconstructedMotionPath::seed_point_type &seed_point)` | function | `QString` | — |
| `create_kvd_from_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref, const referenced_files_collection_type &referenced_files, const referenced_files_collection_type &reconstruction_files, const double &reconstruction_time, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id, c ...` | function | `GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type` | Fill a kvd with data describing how the motion\_paths were generated. |
| `GPLATES_FILEIO_SHAPEFILEFORMATMOTIONPATHEXPORT_H` | macro | `None` | — |
| `export_motion_paths( const std::list<feature_geometry_group_type> &feature_geometry_group_seq, const QFileInfo& file_info, const referenced_files_collection_type &referenced_files, const referenced_files_collection_type &active_reconstruction_files, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate ...` | function | `void` | Exports ReconstructedMotionPath objects to ESRI Shapefile format. |

## Notes

Shapefile attribute fields are limited to 10 characters in length; feature names and field names are truncated accordingly.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/ReconstructedMotionPathExport](ReconstructedMotionPathExport.md) | file-io | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/OgrFormatMotionPathExport.h
python scripts/gpq.py def (anonymous)::referenced_files_collection_type --body
python scripts/gpq.py uses referenced_files_collection_type --kind typedef
```

# OgrFormatReconstructedFeatureGeometryExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1311 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/OgrFormatReconstructedFeatureGeometryExport.h` | C++ | 91 |
| `src/file-io/OgrFormatReconstructedFeatureGeometryExport.cc` | C++ | 346 |

## Overview

[[[PROSE overview unit=file-io/OgrFormatReconstructedFeatureGeometryExport tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::referenced_files_collection_type`](#anonymousreferenced_files_collection_type) | typedef | — | — | 0 | Convenience typedef for referenced files. |
| [`(anonymous)::reconstructed_feature_geom_seq_type`](#anonymousreconstructed_feature_geom_seq_type) | typedef | — | — | 0 | Convenience typedef for a sequence of RFGs. |
| [`GPlatesFileIO::OgrFormatReconstructedFeatureGeometryExport::feature_geometry_group_type`](#gplatesfileioogrformatreconstructedfeaturegeometryexportfeature_geometry_group_type) | typedef | — | — | 0 | Typedef for a feature geometry group of ReconstructedFeatureGeometry objects. |
| [`GPlatesFileIO::OgrFormatReconstructedFeatureGeometryExport::referenced_files_collection_type`](#gplatesfileioogrformatreconstructedfeaturegeometryexportreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |

## Members

### `(anonymous)::referenced_files_collection_type`

*None.*

### `(anonymous)::reconstructed_feature_geom_seq_type`

*None.*

### `GPlatesFileIO::OgrFormatReconstructedFeatureGeometryExport::feature_geometry_group_type`

*None.*

### `GPlatesFileIO::OgrFormatReconstructedFeatureGeometryExport::referenced_files_collection_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `feature_is_of_type_to_exclude( const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref)` | function | `bool` | ! |
| `add_feature_fields_to_kvd( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type &output_kvd, const GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type &feature_kvd)` | function | `void` | — |
| `GPLATES_FILEIO_SHAPEFILEFORMATRECONSTRUCTEDFEATUREGEOMETRYEXPORT_H` | macro | `None` | — |
| `export_geometries( const std::list<feature_geometry_group_type> &feature_geometry_group_seq, const QFileInfo& file_info, const referenced_files_collection_type &referenced_files, const referenced_files_collection_type &active_reconstruction_files, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_i ...` | function | `void` | Exports ReconstructedFeatureGeometry objects to ESRI Shapefile format. |
| `export_geometries_per_collection( const std::list<feature_geometry_group_type> &feature_geometry_group_seq, const QFileInfo& file_info, const referenced_files_collection_type &referenced_files, const referenced_files_collection_type &active_reconstruction_files, const GPlatesModel::integer_plate_id_type &reconstruction ...` | function | `void` | Exports ReconstructedFeatureGeometry objects to ESRI Shapefile format. |

## Notes

[[[PROSE notes unit=file-io/OgrFormatReconstructedFeatureGeometryExport tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/ReconstructedFeatureGeometryExport](ReconstructedFeatureGeometryExport.md) | file-io | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/OgrFormatReconstructedFeatureGeometryExport.h
python scripts/gpq.py def (anonymous)::referenced_files_collection_type --body
python scripts/gpq.py uses referenced_files_collection_type --kind typedef
```

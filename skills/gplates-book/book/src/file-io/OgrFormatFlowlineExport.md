# OgrFormatFlowlineExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1315 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/OgrFormatFlowlineExport.h` | C++ | 79 |
| `src/file-io/OgrFormatFlowlineExport.cc` | C++ | 247 |

## Overview

[[[PROSE overview unit=file-io/OgrFormatFlowlineExport tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::referenced_files_collection_type`](#anonymousreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |
| [`(anonymous)::reconstructed_flowline_seq_type`](#anonymousreconstructed_flowline_seq_type) | typedef | — | — | 0 | Convenience typedef for a sequence of ReconstructedFlowline objects. |
| [`GPlatesFileIO::OgrFormatFlowlineExport::feature_geometry_group_type`](#gplatesfileioogrformatflowlineexportfeature_geometry_group_type) | typedef | — | — | 0 | Typedef for a feature geometry group of ReconstructedFlowline objects. |
| [`GPlatesFileIO::OgrFormatFlowlineExport::referenced_files_collection_type`](#gplatesfileioogrformatflowlineexportreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |

## Members

### `(anonymous)::referenced_files_collection_type`

*None.*

### `(anonymous)::reconstructed_flowline_seq_type`

*None.*

### `GPlatesFileIO::OgrFormatFlowlineExport::feature_geometry_group_type`

*None.*

### `GPlatesFileIO::OgrFormatFlowlineExport::referenced_files_collection_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `make_seed_string( const GPlatesAppLogic::ReconstructedFlowline::seed_point_type &seed_point)` | function | `QString` | — |
| `get_export_times( std::vector<double> &export_times, const std::vector<double> &times, const double &reconstruction_time)` | function | `void` | — |
| `create_kvd_from_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref, const referenced_files_collection_type &referenced_files, const referenced_files_collection_type &reconstruction_files, const double &reconstruction_time, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id, c ...` | function | `GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type` | Fill a kvd with data describing how the flowlines were generated. |
| `GPLATES_FILEIO_SHAPEFILEFORMATFLOWLINEEXPORT_H` | macro | `None` | — |
| `export_flowlines( const std::list<feature_geometry_group_type> &feature_geometry_group_seq, const QFileInfo& file_info, const referenced_files_collection_type &referenced_files, const referenced_files_collection_type &active_reconstruction_files, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id ...` | function | `void` | Exports ReconstructedFlowline objects to ESRI Shapefile format. |

## Notes

[[[PROSE notes unit=file-io/OgrFormatFlowlineExport tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/ReconstructedFlowlineExport](ReconstructedFlowlineExport.md) | file-io | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/OgrFormatFlowlineExport.h
python scripts/gpq.py def (anonymous)::referenced_files_collection_type --body
python scripts/gpq.py uses referenced_files_collection_type --kind typedef
```

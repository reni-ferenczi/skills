# GpmlFormatMultiPointVectorFieldExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 6 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GpmlFormatMultiPointVectorFieldExport.h` | C++ | 77 |
| `src/file-io/GpmlFormatMultiPointVectorFieldExport.cc` | C++ | 361 |

## Overview

[[[PROSE overview unit=file-io/GpmlFormatMultiPointVectorFieldExport tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::multi_point_vector_field_seq_type`](#anonymousmulti_point_vector_field_seq_type) | typedef | — | — | 0 | Convenience typedef for a sequence of MPVFs. |
| [`GPlatesFileIO::GpmlFormatMultiPointVectorFieldExport::multi_point_vector_field_group_type`](#gplatesfileiogpmlformatmultipointvectorfieldexportmulti_point_vector_field_group_type) | typedef | — | — | 0 | Typedef for a feature geometry group of MultiPointVectorField objects. |
| [`GPlatesFileIO::GpmlFormatMultiPointVectorFieldExport::referenced_files_collection_type`](#gplatesfileiogpmlformatmultipointvectorfieldexportreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |

## Members

### `(anonymous)::multi_point_vector_field_seq_type`

*None.*

### `GPlatesFileIO::GpmlFormatMultiPointVectorFieldExport::multi_point_vector_field_group_type`

*None.*

### `GPlatesFileIO::GpmlFormatMultiPointVectorFieldExport::referenced_files_collection_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `insert_velocity_field_into_feature_collection( GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection, const GPlatesAppLogic::MultiPointVectorField *velocity_field, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id, const double &reconstruction_time)` | function | `void` | — |
| `GPLATES_FILE_IO_GPMLFORMATMULTIPOINTVECTORFIELDEXPORT_H` | macro | `None` | — |
| `export_velocity_vector_fields( const std::list<multi_point_vector_field_group_type> &velocity_vector_field_group_seq, const QFileInfo& file_info, GPlatesModel::ModelInterface &model, const referenced_files_collection_type &referenced_files, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id, cons ...` | function | `void` | Exports MultiPointVectorField objects containing \*velocities\*. |

## Notes

[[[PROSE notes unit=file-io/GpmlFormatMultiPointVectorFieldExport tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/MultiPointVectorFieldExport](MultiPointVectorFieldExport.md) | file-io | 7 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GpmlFormatMultiPointVectorFieldExport.h
python scripts/gpq.py def (anonymous)::multi_point_vector_field_seq_type --body
python scripts/gpq.py uses multi_point_vector_field_seq_type --kind typedef
```

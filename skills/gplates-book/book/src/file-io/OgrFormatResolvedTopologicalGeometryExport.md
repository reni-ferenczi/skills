# OgrFormatResolvedTopologicalGeometryExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 857 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/OgrFormatResolvedTopologicalGeometryExport.h` | C++ | 155 |
| `src/file-io/OgrFormatResolvedTopologicalGeometryExport.cc` | C++ | 483 |

## Overview

[[[PROSE overview unit=file-io/OgrFormatResolvedTopologicalGeometryExport tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::referenced_files_collection_type`](#anonymousreferenced_files_collection_type) | typedef | — | — | 0 | Convenience typedef for referenced files. |
| [`(anonymous)::resolved_topologies_seq_type`](#anonymousresolved_topologies_seq_type) | typedef | — | — | 0 | Convenience typedef for a sequence of resolved topologies. |
| [`GPlatesFileIO::OgrFormatResolvedTopologicalGeometryExport::feature_geometry_group_type`](#gplatesfileioogrformatresolvedtopologicalgeometryexportfeature_geometry_group_type) | typedef | — | — | 0 | Typedef for a feature geometry group of reconstruction geometries. |
| [`GPlatesFileIO::OgrFormatResolvedTopologicalGeometryExport::referenced_files_collection_type`](#gplatesfileioogrformatresolvedtopologicalgeometryexportreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |

## Members

### `(anonymous)::referenced_files_collection_type`

*None.*

### `(anonymous)::resolved_topologies_seq_type`

*None.*

### `GPlatesFileIO::OgrFormatResolvedTopologicalGeometryExport::feature_geometry_group_type`

*None.*

### `GPlatesFileIO::OgrFormatResolvedTopologicalGeometryExport::referenced_files_collection_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `add_feature_fields_to_kvd( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type &output_kvd, const GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type &feature_kvd)` | function | `void` | — |
| `get_kvd_for_export( const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref, const referenced_files_collection_type &referenced_files, const referenced_files_collection_type &active_reconstruction_files, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id, const double &reconstruction_time, ...` | function | `GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type` | — |
| `GPLATES_FILE_IO_OGRFORMATRESOLVEDTOPOLOGICALGEOMETRYXPORT_H` | macro | `None` | — |
| `export_resolved_topological_geometries( bool export_per_collection, const std::list<feature_geometry_group_type> &feature_geometry_group_seq, const QFileInfo& file_info, const referenced_files_collection_type &referenced_files, const referenced_files_collection_type &active_reconstruction_files, const GPlatesModel::int ...` | function | `void` | Exports resolved topology objects to OGR format. |
| `export_resolved_topological_sections( bool export_per_collection, const std::vector<const GPlatesAppLogic::ResolvedTopologicalSection *> &resolved_topological_sections, const QFileInfo& file_info, const referenced_files_collection_type &referenced_files, const referenced_files_collection_type &active_reconstruction_fil ...` | function | `void` | Exports resolved topological sections to OGR format. |
| `export_citcoms_resolved_topological_boundaries( const CitcomsResolvedTopologicalBoundaryExportImpl::resolved_topologies_seq_type &resolved_topologies, const QFileInfo& file_info, const referenced_files_collection_type &referenced_files, const referenced_files_collection_type &active_reconstruction_files, const GPlatesM ...` | function | `void` | Exports ResolvedTopologicalGeometry objects to OGR format for use by CitcomS software. |
| `export_citcoms_sub_segments( const CitcomsResolvedTopologicalBoundaryExportImpl::sub_segment_group_seq_type &sub_segments, const QFileInfo& file_info, const referenced_files_collection_type &referenced_files, const referenced_files_collection_type &active_reconstruction_files, const GPlatesModel::integer_plate_id_type ...` | function | `void` | Exports subsegments of resolved topological boundaries to OGR format for use by CitcomS software. |

## Notes

[[[PROSE notes unit=file-io/OgrFormatResolvedTopologicalGeometryExport tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/CitcomsResolvedTopologicalBoundaryExport](CitcomsResolvedTopologicalBoundaryExport.md) | file-io | 5 |
| [file-io/ResolvedTopologicalGeometryExport](ResolvedTopologicalGeometryExport.md) | file-io | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/OgrFormatResolvedTopologicalGeometryExport.h
python scripts/gpq.py def (anonymous)::referenced_files_collection_type --body
python scripts/gpq.py uses referenced_files_collection_type --kind typedef
```

# GMTFormatResolvedTopologicalGeometryExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 6 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GMTFormatResolvedTopologicalGeometryExport.h` | C++ | 98 |
| `src/file-io/GMTFormatResolvedTopologicalGeometryExport.cc` | C++ | 307 |

## Overview

[[[PROSE overview unit=file-io/GMTFormatResolvedTopologicalGeometryExport tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GMTFormatResolvedTopologicalGeometryExport::(anonymous)::resolved_topologies_seq_type`](#gplatesfileiogmtformatresolvedtopologicalgeometryexportanonymousresolved_topologies_seq_type) | typedef | — | — | 0 | Convenience typedef for a sequence of RTGs. |
| [`GPlatesFileIO::GMTFormatResolvedTopologicalGeometryExport::feature_geometry_group_type`](#gplatesfileiogmtformatresolvedtopologicalgeometryexportfeature_geometry_group_type) | typedef | — | — | 0 | Typedef for a feature geometry group of resolved topologies. |
| [`GPlatesFileIO::GMTFormatResolvedTopologicalGeometryExport::referenced_files_collection_type`](#gplatesfileiogmtformatresolvedtopologicalgeometryexportreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |

## Members

### `GPlatesFileIO::GMTFormatResolvedTopologicalGeometryExport::(anonymous)::resolved_topologies_seq_type`

*None.*

### `GPlatesFileIO::GMTFormatResolvedTopologicalGeometryExport::feature_geometry_group_type`

*None.*

### `GPlatesFileIO::GMTFormatResolvedTopologicalGeometryExport::referenced_files_collection_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_global_header_lines( std::vector<QString>& header_lines, const referenced_files_collection_type &referenced_files, const referenced_files_collection_type &active_reconstruction_files, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id, const double &reconstruction_time)` | function | `void` | Prints GMT format header at top of the exported file containing information about the reconstruction that is not per-feature information. |
| `GPLATES_FILE_IO_GMTFORMATRESOLVEDTOPOLOGICALGEOMETRYEXPORT_H` | macro | `None` | — |
| `export_resolved_topological_geometries( const std::list<feature_geometry_group_type> &feature_geometry_group_seq, const QFileInfo& file_info, const referenced_files_collection_type &referenced_files, const referenced_files_collection_type &active_reconstruction_files, const GPlatesModel::integer_plate_id_type &reconstr ...` | function | `void` | Exports resolved topology objects to GMT format. |
| `export_resolved_topological_sections( const std::vector<const GPlatesAppLogic::ResolvedTopologicalSection *> &resolved_topological_sections, const QFileInfo& file_info, const referenced_files_collection_type &referenced_files, const referenced_files_collection_type &active_reconstruction_files, const GPlatesModel::inte ...` | function | `void` | Exports resolved topological sections to GMT format. |

## Notes

[[[PROSE notes unit=file-io/GMTFormatResolvedTopologicalGeometryExport tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/ResolvedTopologicalGeometryExport](ResolvedTopologicalGeometryExport.md) | file-io | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GMTFormatResolvedTopologicalGeometryExport.h
python scripts/gpq.py def GPlatesFileIO::GMTFormatResolvedTopologicalGeometryExport::feature_geometry_group_type --body
python scripts/gpq.py uses feature_geometry_group_type --kind typedef
```

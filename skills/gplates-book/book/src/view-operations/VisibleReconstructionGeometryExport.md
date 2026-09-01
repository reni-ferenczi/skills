# VisibleReconstructionGeometryExport

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 925 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/VisibleReconstructionGeometryExport.h` | C++ | 209 |
| `src/view-operations/VisibleReconstructionGeometryExport.cc` | C++ | 602 |

## Overview

[[[PROSE overview unit=view-operations/VisibleReconstructionGeometryExport tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::VisibleReconstructionGeometryExport::(anonymous)::reconstructed_feature_geom_seq_type`](#gplatesviewoperationsvisiblereconstructiongeometryexportanonymousreconstructed_feature_geom_seq_type) | typedef | — | — | 0 | Convenience typedef for sequence of RFGs. |
| [`GPlatesViewOperations::VisibleReconstructionGeometryExport::(anonymous)::reconstructed_flowline_seq_type`](#gplatesviewoperationsvisiblereconstructiongeometryexportanonymousreconstructed_flowline_seq_type) | typedef | — | — | 0 | Convenience typedef for sequence of reconstructed flowline geometries. |
| [`GPlatesViewOperations::VisibleReconstructionGeometryExport::(anonymous)::reconstructed_motion_path_seq_type`](#gplatesviewoperationsvisiblereconstructiongeometryexportanonymousreconstructed_motion_path_seq_type) | typedef | — | — | 0 | Convenience typedef for sequence of reconstructed motion track geometries. |
| [`GPlatesViewOperations::VisibleReconstructionGeometryExport::(anonymous)::resolved_topologies_seq_type`](#gplatesviewoperationsvisiblereconstructiongeometryexportanonymousresolved_topologies_seq_type) | typedef | — | — | 0 | Convenience typedef for sequence of resolved topologies. |
| [`GPlatesViewOperations::VisibleReconstructionGeometryExport::(anonymous)::ExportTopologicalSectionType`](#gplatesviewoperationsvisiblereconstructiongeometryexportanonymousexporttopologicalsectiontype) | enum | — | — | 0 | Export type of resolved topological sections. |
| [`GPlatesViewOperations::VisibleReconstructionGeometryExport::files_collection_type`](#gplatesviewoperationsvisiblereconstructiongeometryexportfiles_collection_type) | typedef | — | — | 0 | Typedef for sequence of feature collection files. |

## Members

### `GPlatesViewOperations::VisibleReconstructionGeometryExport::(anonymous)::reconstructed_feature_geom_seq_type`

*None.*

### `GPlatesViewOperations::VisibleReconstructionGeometryExport::(anonymous)::reconstructed_flowline_seq_type`

*None.*

### `GPlatesViewOperations::VisibleReconstructionGeometryExport::(anonymous)::reconstructed_motion_path_seq_type`

*None.*

### `GPlatesViewOperations::VisibleReconstructionGeometryExport::(anonymous)::resolved_topologies_seq_type`

*None.*

### `GPlatesViewOperations::VisibleReconstructionGeometryExport::(anonymous)::ExportTopologicalSectionType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EXPORT_TOPOLOGICAL_SECTIONS_ALL` | enumerator | `None` | — | — |
| `EXPORT_TOPOLOGICAL_SECTIONS_SUBDUCTION` | enumerator | `None` | — | — |
| `EXPORT_TOPOLOGICAL_SECTIONS_SUBDUCTION_LEFT` | enumerator | `None` | — | — |
| `EXPORT_TOPOLOGICAL_SECTIONS_SUBDUCTION_RIGHT` | enumerator | `None` | — | — |
| `EXPORT_TOPOLOGICAL_SECTIONS_RIDGE_TRANFORM` | enumerator | `None` | — | — |

### `GPlatesViewOperations::VisibleReconstructionGeometryExport::files_collection_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `append_suffix_to_template_filebasename( const QFileInfo &original_template_filename, QString suffix)` | function | `QString` | — |
| `substitute_placeholder( const QString &output_filebasename, const QString &placeholder, const QString &placeholder_replacement)` | function | `QString` | — |
| `get_full_output_filename( const QDir &target_dir, const QString &filebasename, const QString &placeholder_string, const QString &placeholder_replacement)` | function | `QString` | — |
| `export_resolved_topological_sections( const std::vector<GPlatesAppLogic::ResolvedTopologicalSection::non_null_ptr_type> &resolved_topological_sections, const QDir &target_dir, const QString &file_basename, const QString &placeholder_format_string, const QString &placeholder_topological_sections, ExportTopologicalSectio ...` | function | `void` | — |
| `GPLATES_VIEWOPERATIONS_VISIBLERECONSTRUCTIONGEOMETRYEXPORT_H` | macro | `None` | — |
| `export_visible_reconstructed_feature_geometries( const QString &filename, const GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, const GPlatesFileIO::FeatureCollectionFileFormat::Registry &file_format_registry, const files_collection_type &active_files, const files_collection_type &active_re ...` | function | `void` | Collects visible ReconstructedFeatureGeometry objects that are displayed using rendered\_geom\_collection and exports to a file depending on the file extension of filename. |
| `export_visible_reconstructed_flowlines( const QString &filename, const GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, const GPlatesFileIO::FeatureCollectionFileFormat::Registry &file_format_registry, const files_collection_type &active_files, const files_collection_type &active_reconstruct ...` | function | `void` | Collects visible ReconstructedFeatureGeometry objects that are displayed using rendered\_geom\_collection and exports to a file depending on the file extension of filename. |
| `export_visible_reconstructed_motion_paths( const QString &filename, const GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, const GPlatesFileIO::FeatureCollectionFileFormat::Registry &file_format_registry, const files_collection_type &active_files, const files_collection_type &active_reconstr ...` | function | `void` | Collects visible ReconstructedMotionPath objects that are displayed using rendered\_geom\_collection and exports to a file depending on the file extension of filename. |
| `export_visible_resolved_topologies( const QDir &target_dir, const QString &file_basename, const QString &placeholder_format_string, const QString &placeholder_topological_geometries, const QString &placeholder_topological_sections, const QString &placeholder_topological_sections_subduction, const QString &placeholder_t ...` | function | `void` | Collects visible resolved topologies including ResolvedTopologicalLine, ResolvedTopologicalBoundary and ResolvedTopologicalNetwork objects that are displayed using rendered\_geom\_collection and exports to a file depending on the file ... |

## Notes

[[[PROSE notes unit=view-operations/VisibleReconstructionGeometryExport tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportReconstructedGeometryAnimationStrategy](../gui/ExportReconstructedGeometryAnimationStrategy.md) | gui | 9 |
| [gui/ExportResolvedTopologyAnimationStrategy](../gui/ExportResolvedTopologyAnimationStrategy.md) | gui | 9 |
| [gui/ExportDeformationAnimationStrategy](../gui/ExportDeformationAnimationStrategy.md) | gui | 4 |
| [gui/ExportScalarCoverageAnimationStrategy](../gui/ExportScalarCoverageAnimationStrategy.md) | gui | 4 |
| [gui/ExportVelocityAnimationStrategy](../gui/ExportVelocityAnimationStrategy.md) | gui | 4 |
| [gui/ExportFlowlineAnimationStrategy](../gui/ExportFlowlineAnimationStrategy.md) | gui | 3 |
| [gui/ExportMotionPathAnimationStrategy](../gui/ExportMotionPathAnimationStrategy.md) | gui | 3 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/VisibleReconstructionGeometryExport.h
python scripts/gpq.py def GPlatesViewOperations::VisibleReconstructionGeometryExport::(anonymous)::ExportTopologicalSectionType --body
python scripts/gpq.py uses ExportTopologicalSectionType --kind enum
```

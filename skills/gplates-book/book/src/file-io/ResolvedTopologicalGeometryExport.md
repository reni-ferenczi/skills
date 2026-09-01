# ResolvedTopologicalGeometryExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 6 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ResolvedTopologicalGeometryExport.h` | C++ | 159 |
| `src/file-io/ResolvedTopologicalGeometryExport.cc` | C++ | 445 |

## Overview

Exports resolved topological geometries to files in multiple formats: GMT (.xy), Shapefile (.shp), OGR GMT (.gmt), and GeoJSON (.geojson or .json). Resolved topologies are geometries that respect plate boundaries and are precisely joined at shared nodes. This unit exports two kinds: topological geometries (lines, boundaries, and networks) and topological sections (the individual subsegments that compose boundary segments).

Both `export_resolved_topological_geometries()` and `export_resolved_topological_sections()` follow the same pattern: they can export to a single file or grouped by input collection. Topological boundaries and networks can optionally have their polygon orientation forced (clockwise or counter-clockwise), and all exports can optionally wrap geometries to the dateline. Topological sections support granular export of sub-segments from resolved topological lines.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ResolvedTopologicalGeometryExport::(anonymous)::feature_geometry_group_seq_type`](#gplatesfileioresolvedtopologicalgeometryexportanonymousfeature_geometry_group_seq_type) | typedef | — | — | 0 | Typedef for a sequence of FeatureGeometryGroup objects. |
| [`GPlatesFileIO::ResolvedTopologicalGeometryExport::(anonymous)::grouped_features_seq_type`](#gplatesfileioresolvedtopologicalgeometryexportanonymousgrouped_features_seq_type) | typedef | — | — | 0 | Typedef for a sequence of FeatureCollectionFeatureGroup objects. |
| [`GPlatesFileIO::ResolvedTopologicalGeometryExport::Format`](#gplatesfileioresolvedtopologicalgeometryexportformat) | enum | — | — | 0 | Formats of files that can export resolved topological geometries. |

## Members

### `GPlatesFileIO::ResolvedTopologicalGeometryExport::(anonymous)::feature_geometry_group_seq_type`

*None.*

### `GPlatesFileIO::ResolvedTopologicalGeometryExport::(anonymous)::grouped_features_seq_type`

*None.*

### `GPlatesFileIO::ResolvedTopologicalGeometryExport::Format`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UNKNOWN` | enumerator | `None` | — | — |
| `GMT` | enumerator | `None` | — | — |
| `SHAPEFILE` | enumerator | `None` | — | — |
| `OGRGMT` | enumerator | `None` | — | — |
| `GEOJSON` | enumerator | `None` | — | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `export_resolved_topological_geometries_impl( bool export_per_collection, const QString &filename, Format export_format, const feature_geometry_group_seq_type &grouped_recon_geoms_seq, const std::vector<const File::Reference *> &referenced_files, const std::vector<const File::Reference *> &active_reconstruction_files, c ...` | function | `void` | — |
| `export_resolved_topological_sections_impl( bool export_per_collection, const QString &filename, Format export_format, const std::vector<const GPlatesAppLogic::ResolvedTopologicalSection *> &resolved_topological_sections, const std::vector<const File::Reference *> &referenced_files, const std::vector<const File::Referen ...` | function | `void` | — |
| `GPLATES_FILE_IO_RESOLVEDTOPOLOGICALGEOMETRYEXPORT_H` | macro | `None` | — |
| `get_export_file_format( const QFileInfo& file_info, const FeatureCollectionFileFormat::Registry &file_format_registry)` | function | `Format` | Determine type of export file format based on filename extension. |
| `export_resolved_topological_geometries( const QString &filename, Format export_format, const std::vector<const GPlatesAppLogic::ReconstructionGeometry *> &resolved_topologies, const std::vector<const File::Reference *> &active_files, const std::vector<const File::Reference *> &active_reconstruction_files, const GPlates ...` | function | `void` | Exports resolved topology objects (includes ResolvedTopologicalLine, ResolvedTopologicalBoundary and ResolvedTopologicalNetwork). resolved topologies according to the input files their features came from and write to corresponding output ... |
| `export_resolved_topological_sections( const QString &filename, Format export_format, const std::vector<const GPlatesAppLogic::ResolvedTopologicalSection *> &resolved_topological_sections, const std::vector<const File::Reference *> &active_files, const std::vector<const File::Reference *> &active_reconstruction_files, c ...` | function | `void` | Exports resolved topological sections (ResolvedTopologicalSection and its ResolvedTopologicalSharedSubSegment instances). input files their features came from and write to corresponding output files. |

## Notes

Polygon orientation forcing only applies to boundaries and networks (which have polygon boundaries); lines are unaffected. Dateline wrapping is currently ignored by GMT .xy format. The export is grouped by feature before being grouped by collection. Both single-file and per-collection exports can be performed in a single call. The file format is determined from the filename extension via the `FeatureCollectionFileFormat::Registry`.

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/VisibleReconstructionGeometryExport](../view-operations/VisibleReconstructionGeometryExport.md) | view-operations | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ResolvedTopologicalGeometryExport.h
python scripts/gpq.py def GPlatesFileIO::ResolvedTopologicalGeometryExport::Format --body
python scripts/gpq.py uses Format --kind enum
```

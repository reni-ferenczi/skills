# ReconstructedFlowlineExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 6 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ReconstructedFlowlineExport.h` | C++ | 113 |
| `src/file-io/ReconstructedFlowlineExport.cc` | C++ | 255 |

## Overview

[[[PROSE overview unit=file-io/ReconstructedFlowlineExport tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ReconstructedFlowlineExport::(anonymous)::feature_geometry_group_seq_type`](#gplatesfileioreconstructedflowlineexportanonymousfeature_geometry_group_seq_type) | typedef | — | — | 0 | Typedef for a sequence of FeatureGeometryGroup objects. |
| [`GPlatesFileIO::ReconstructedFlowlineExport::(anonymous)::grouped_features_seq_type`](#gplatesfileioreconstructedflowlineexportanonymousgrouped_features_seq_type) | typedef | — | — | 0 | Typedef for a sequence of FeatureCollectionFeatureGroup objects. |
| [`GPlatesFileIO::ReconstructedFlowlineExport::Format`](#gplatesfileioreconstructedflowlineexportformat) | enum | — | — | 0 | Formats of files that can export reconstructed flowlines. |

## Members

### `GPlatesFileIO::ReconstructedFlowlineExport::(anonymous)::feature_geometry_group_seq_type`

*None.*

### `GPlatesFileIO::ReconstructedFlowlineExport::(anonymous)::grouped_features_seq_type`

*None.*

### `GPlatesFileIO::ReconstructedFlowlineExport::Format`

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
| `export_as_single_file( const QString &filename, Format export_format, const feature_geometry_group_seq_type &grouped_recon_geoms_seq, const std::vector<const File::Reference *> &referenced_files, const std::vector<const File::Reference *> &active_reconstruction_files, const GPlatesModel::integer_plate_id_type &reconstr ...` | function | `void` | — |
| `export_per_collection( const QString &filename, Format export_format, const feature_geometry_group_seq_type &grouped_recon_geoms_seq, const std::vector<const File::Reference *> &referenced_files, const std::vector<const File::Reference *> &active_reconstruction_files, const GPlatesModel::integer_plate_id_type &reconstr ...` | function | `void` | — |
| `GPLATES_FILEIO_RECONSTRUCTEDFLOWLINEEXPORT_H` | macro | `None` | — |
| `get_export_file_format( const QFileInfo& file_info, const FeatureCollectionFileFormat::Registry &file_format_registry)` | function | `Format` | Determine type of export file format based on filename extension. |
| `export_reconstructed_flowlines( const QString &filename, Format export_format, const std::vector<const GPlatesAppLogic::ReconstructedFlowline *> &reconstructed_flowline_seq, const std::vector<const File::Reference *> &active_files, const std::vector<const File::Reference *> &active_reconstruction_files, const GPlatesMo ...` | function | `void` | Exports ReconstructedFlowline objects. to a single file. reconstruction geometries according to the input files their features came from and write to corresponding output files. |

## Notes

[[[PROSE notes unit=file-io/ReconstructedFlowlineExport tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/VisibleReconstructionGeometryExport](../view-operations/VisibleReconstructionGeometryExport.md) | view-operations | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ReconstructedFlowlineExport.h
python scripts/gpq.py def GPlatesFileIO::ReconstructedFlowlineExport::Format --body
python scripts/gpq.py uses Format --kind enum
```

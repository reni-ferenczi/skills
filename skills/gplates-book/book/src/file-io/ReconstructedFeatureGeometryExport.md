# ReconstructedFeatureGeometryExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 6 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ReconstructedFeatureGeometryExport.h` | C++ | 114 |
| `src/file-io/ReconstructedFeatureGeometryExport.cc` | C++ | 278 |

## Overview

`ReconstructedFeatureGeometryExport` is the entry point for writing a batch of
`GPlatesAppLogic::ReconstructedFeatureGeometry` objects out to a file in one
of the supported export formats (`Format::GMT`, `SHAPEFILE`, `OGRGMT`,
`GEOJSON`, resolved from the target filename's extension by
`get_export_file_format`). `export_reconstructed_feature_geometries` is the
single public function callers use; internally it groups the input geometries
by feature and by originating input file using the shared
`FeatureGeometryGroup`/`FeatureCollectionFeatureGroup` helpers from
`ReconstructionGeometryExportImpl`, then dispatches to the format-specific
writers (`GMTFormatReconstructedFeatureGeometryExport`,
`OgrFormatReconstructedFeatureGeometryExport`) to actually serialise them.

The function's boolean flags control independent aspects of the output
layout: a single combined file, one file per input file (optionally each in
its own directory named after that input file), and dateline
wrapping/clipping — the first two are not mutually exclusive, so both a
combined file and the per-input-file set can be produced from one call.
`view-operations/VisibleReconstructionGeometryExport`, the Python API and
`cli/CliReconstructCommand` are its three call sites, covering the GUI export
dialogs, pyGPlates, and the headless CLI respectively.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ReconstructedFeatureGeometryExport::(anonymous)::feature_geometry_group_seq_type`](#gplatesfileioreconstructedfeaturegeometryexportanonymousfeature_geometry_group_seq_type) | typedef | — | — | 0 | Typedef for a sequence of FeatureGeometryGroup objects. |
| [`GPlatesFileIO::ReconstructedFeatureGeometryExport::(anonymous)::grouped_features_seq_type`](#gplatesfileioreconstructedfeaturegeometryexportanonymousgrouped_features_seq_type) | typedef | — | — | 0 | Typedef for a sequence of FeatureCollectionFeatureGroup objects. |
| [`GPlatesFileIO::ReconstructedFeatureGeometryExport::Format`](#gplatesfileioreconstructedfeaturegeometryexportformat) | enum | — | — | 0 | Formats of files that can export reconstructed feature geometries. |

## Members

### `GPlatesFileIO::ReconstructedFeatureGeometryExport::(anonymous)::feature_geometry_group_seq_type`

*None.*

### `GPlatesFileIO::ReconstructedFeatureGeometryExport::(anonymous)::grouped_features_seq_type`

*None.*

### `GPlatesFileIO::ReconstructedFeatureGeometryExport::Format`

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
| `GPLATES_FILEIO_RECONSTRUCTEDFEATUREGEOMETRYEXPORT_H` | macro | `None` | — |
| `get_export_file_format( const QFileInfo& file_info, const FeatureCollectionFileFormat::Registry &file_format_registry)` | function | `Format` | Determine type of export file format based on filename extension. |
| `export_reconstructed_feature_geometries( const QString &filename, Format export_format, const std::vector<const GPlatesAppLogic::ReconstructedFeatureGeometry *> &reconstructed_feature_geom_seq, const std::vector<const File::Reference *> &active_files, const std::vector<const File::Reference *> &active_reconstruction_fi ...` | function | `void` | Exports ReconstructedFeatureGeometry objects. to a single file. reconstruction geometries according to the input files their features came from and write to corresponding output files. |

## Notes

`export_reconstructed_feature_geometries` throws
`ErrorOpeningFileForWritingException` if the target file cannot be opened and
`FileFormatNotSupportedException` if `export_format` is not one of the
recognised formats (including `UNKNOWN`) — callers must be prepared to catch
both rather than getting a `bool` success result. `wrap_to_dateline` is
currently ignored by the GMT `.xy` writer.

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/VisibleReconstructionGeometryExport](../view-operations/VisibleReconstructionGeometryExport.md) | view-operations | 14 |
| [api/PyFunctions](../api/PyFunctions.md) | api | 13 |
| [cli/CliReconstructCommand](../cli/CliReconstructCommand.md) | cli | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ReconstructedFeatureGeometryExport.h
python scripts/gpq.py def GPlatesFileIO::ReconstructedFeatureGeometryExport::Format --body
python scripts/gpq.py uses Format --kind enum
```

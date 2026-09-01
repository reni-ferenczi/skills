# ReconstructedMotionPathExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1199 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ReconstructedMotionPathExport.h` | C++ | 112 |
| `src/file-io/ReconstructedMotionPathExport.cc` | C++ | 255 |

## Overview

Exports reconstructed motion paths to files in multiple formats: GMT (.xy), Shapefile (.shp), OGR GMT (.gmt), and GeoJSON (.geojson or .json). A motion path represents the instantaneous displacement or velocity of a point on a plate at a given reconstruction time; this exporter writes those reconstructed paths.

The main entry point, `export_reconstructed_motion_paths()`, can export either to a single output file or to per-collection files grouped by their source. It delegates to format-specific exporters, following the same pattern as `ReconstructedFlowlineExport`. The export can optionally wrap geometries to the antimeridian and tracks the reconstruction anchor plate ID and time.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ReconstructedMotionPathExport::(anonymous)::feature_geometry_group_seq_type`](#gplatesfileioreconstructedmotionpathexportanonymousfeature_geometry_group_seq_type) | typedef | — | — | 0 | Typedef for a sequence of FeatureGeometryGroup objects. |
| [`GPlatesFileIO::ReconstructedMotionPathExport::(anonymous)::grouped_features_seq_type`](#gplatesfileioreconstructedmotionpathexportanonymousgrouped_features_seq_type) | typedef | — | — | 0 | Typedef for a sequence of FeatureCollectionFeatureGroup objects. |
| [`GPlatesFileIO::ReconstructedMotionPathExport::Format`](#gplatesfileioreconstructedmotionpathexportformat) | enum | — | — | 0 | Formats of files that can export reconstructed motion paths. |

## Members

### `GPlatesFileIO::ReconstructedMotionPathExport::(anonymous)::feature_geometry_group_seq_type`

*None.*

### `GPlatesFileIO::ReconstructedMotionPathExport::(anonymous)::grouped_features_seq_type`

*None.*

### `GPlatesFileIO::ReconstructedMotionPathExport::Format`

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
| `GPLATES_FILEIO_RECONSTRUCTEDMOTIONPATHEXPORT_H` | macro | `None` | — |
| `get_export_file_format( const QFileInfo& file_info, const FeatureCollectionFileFormat::Registry &file_format_registry)` | function | `Format` | Determine type of export file format based on filename extension. |
| `export_reconstructed_motion_paths(const QString &filename, Format export_format, const std::vector<const GPlatesAppLogic::ReconstructedMotionPath *> &reconstructed_motion_path_seq, const std::vector<const File::Reference *> &active_files, const std::vector<const File::Reference *> &active_reconstruction_files, const GP ...` | function | `void` | Exports ReconstructedMotionPath objects. to a single file. reconstruction geometries according to the input files their features came from and write to corresponding output files. |

## Notes

The export is grouped by feature before being grouped by collection. Both single-file and per-collection exports can be performed in a single call. The file format is determined from the filename extension via the `FeatureCollectionFileFormat::Registry`.

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/VisibleReconstructionGeometryExport](../view-operations/VisibleReconstructionGeometryExport.md) | view-operations | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ReconstructedMotionPathExport.h
python scripts/gpq.py def GPlatesFileIO::ReconstructedMotionPathExport::Format --body
python scripts/gpq.py uses Format --kind enum
```

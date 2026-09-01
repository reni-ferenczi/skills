# ReconstructedScalarCoverageExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 6 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ReconstructedScalarCoverageExport.h` | C++ | 141 |
| `src/file-io/ReconstructedScalarCoverageExport.cc` | C++ | 220 |

## Overview

Exports reconstructed scalar coverages (scalar fields sampled at points on a sphere) to GPML and GMT formats. A scalar coverage associates a scalar value with each point in a domain point set; this exporter can also include associated deformation scalars: dilatation strain, dilatation strain rate, and second invariant strain rate.

The main entry points are `export_reconstructed_scalar_coverages_to_gpml_format()` for GPML output (preserving the data as features in the model) and `export_reconstructed_scalar_coverages_to_gmt_format()` for GMT format (one point per line with scalars). Both support single-file and per-input-file export modes simultaneously. The GMT exporter can output coordinates as either (lon, lat) or (lat, lon).

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ReconstructedScalarCoverageExport::(anonymous)::reconstructed_scalar_coverage_seq_type`](#gplatesfileioreconstructedscalarcoverageexportanonymousreconstructed_scalar_coverage_seq_type) | typedef | — | — | 0 | Typedef for a sequence of ReconstructedScalarCoverage objects. |
| [`GPlatesFileIO::ReconstructedScalarCoverageExport::(anonymous)::grouped_features_seq_type`](#gplatesfileioreconstructedscalarcoverageexportanonymousgrouped_features_seq_type) | typedef | — | — | 0 | Typedef for a sequence of FeatureCollectionFeatureGroup objects. |

## Members

### `GPlatesFileIO::ReconstructedScalarCoverageExport::(anonymous)::reconstructed_scalar_coverage_seq_type`

*None.*

### `GPlatesFileIO::ReconstructedScalarCoverageExport::(anonymous)::grouped_features_seq_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILE_IO_RECONSTRUCTEDSCALARCOVERAGEEXPORT_H` | macro | `None` | — |
| `export_reconstructed_scalar_coverages_to_gpml_format( const QString &filename, const std::vector<const GPlatesAppLogic::ReconstructedScalarCoverage *> &reconstructed_scalar_coverage_seq, GPlatesModel::ModelInterface &model, const std::vector<const File::Reference *> &active_files, bool include_dilatation_strain, bool i ...` | function | `void` | Exports ReconstructedScalarCoverage objects containing \*scalar coverages\* to the GPML file format. |
| `export_reconstructed_scalar_coverages_to_gmt_format( const QString &filename, const std::vector<const GPlatesAppLogic::ReconstructedScalarCoverage *> &reconstructed_scalar_coverage_seq, const std::vector<const File::Reference *> &active_files, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id, c ...` | function | `void` | Exports ReconstructedScalarCoverage objects containing \*scalar coverages\* to the GMT file format. |

## Notes

The GPML exporter takes a `ModelInterface` to create new features in the model, whereas the GMT exporter writes text. Both support optional inclusion of dilatation strain and strain rate data. Single-file and per-input-file exports can be combined in one call.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GMTFormatReconstructedScalarCoverageExport](GMTFormatReconstructedScalarCoverageExport.md) | file-io | 7 |
| [gui/ExportScalarCoverageAnimationStrategy](../gui/ExportScalarCoverageAnimationStrategy.md) | gui | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ReconstructedScalarCoverageExport.h
python scripts/gpq.py def GPlatesFileIO::ReconstructedScalarCoverageExport::(anonymous)::reconstructed_scalar_coverage_seq_type --body
python scripts/gpq.py uses reconstructed_scalar_coverage_seq_type --kind typedef
```

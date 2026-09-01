# ReconstructedScalarCoverageExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 6 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ReconstructedScalarCoverageExport.h` | C++ | 141 |
| `src/file-io/ReconstructedScalarCoverageExport.cc` | C++ | 220 |

## Overview

[[[PROSE overview unit=file-io/ReconstructedScalarCoverageExport tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=file-io/ReconstructedScalarCoverageExport tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

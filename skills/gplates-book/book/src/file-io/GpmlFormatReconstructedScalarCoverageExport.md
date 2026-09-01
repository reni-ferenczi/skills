# GpmlFormatReconstructedScalarCoverageExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 6 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GpmlFormatReconstructedScalarCoverageExport.h` | C++ | 80 |
| `src/file-io/GpmlFormatReconstructedScalarCoverageExport.cc` | C++ | 384 |

## Overview

[[[PROSE overview unit=file-io/GpmlFormatReconstructedScalarCoverageExport tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::reconstructed_scalar_coverage_seq_type`](#anonymousreconstructed_scalar_coverage_seq_type) | typedef | — | — | 0 | Convenience typedef for a sequence of reconstructed scalar coverages. |
| [`GPlatesFileIO::GpmlFormatReconstructedScalarCoverageExport::reconstructed_scalar_coverage_group_type`](#gplatesfileiogpmlformatreconstructedscalarcoverageexportreconstructed_scalar_coverage_group_type) | typedef | — | — | 0 | Typedef for a feature geometry group of ReconstructedScalarCoverage objects. |

## Members

### `(anonymous)::reconstructed_scalar_coverage_seq_type`

*None.*

### `GPlatesFileIO::GpmlFormatReconstructedScalarCoverageExport::reconstructed_scalar_coverage_group_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_range_associated_with_reconstructed_scalar_coverage( const GPlatesAppLogic::ReconstructedScalarCoverage *reconstructed_scalar_coverage, const GPlatesModel::PropertyName &domain_property_name)` | function | `boost::optional<GPlatesPropertyValues::GmlDataBlockCoordinateList::non_null_ptr_to_const_type>` | — |
| `insert_reconstructed_scalar_coverage_into_feature_collection( GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection, const GPlatesAppLogic::ReconstructedScalarCoverage *reconstructed_scalar_coverage, bool include_dilatation_strain, bool include_dilatation_strain_rate, bool include_second_invariant_strain_ ...` | function | `void` | — |
| `GPLATES_FILE_IO_GPMLFORMATRECONSTRUCTEDSCALARCOVERAGEEXPORT_H` | macro | `None` | — |
| `export_reconstructed_scalar_coverages( const std::list<reconstructed_scalar_coverage_group_type> &reconstructed_scalar_coverage_group_seq, const QFileInfo& file_info, GPlatesModel::ModelInterface &model, bool include_dilatation_strain, bool include_dilatation_strain_rate, bool include_second_invariant_strain_rate)` | function | `void` | Exports ReconstructedScalarCoverage objects. |

## Notes

[[[PROSE notes unit=file-io/GpmlFormatReconstructedScalarCoverageExport tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/ReconstructedScalarCoverageExport](ReconstructedScalarCoverageExport.md) | file-io | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GpmlFormatReconstructedScalarCoverageExport.h
python scripts/gpq.py def GPlatesFileIO::GpmlFormatReconstructedScalarCoverageExport::reconstructed_scalar_coverage_group_type --body
python scripts/gpq.py uses reconstructed_scalar_coverage_group_type --kind typedef
```

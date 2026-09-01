# GMTFormatReconstructedScalarCoverageExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 363 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GMTFormatReconstructedScalarCoverageExport.h` | C++ | 87 |
| `src/file-io/GMTFormatReconstructedScalarCoverageExport.cc` | C++ | 521 |

## Overview

Exports reconstructed scalar coverages to GMT format. A scalar coverage is a field of scalar values (such as temperature or age) sampled at domain points on a reconstructed surface; this exporter writes `ReconstructedScalarCoverage` objects to a GMT file with each line containing the spatial position, optional strain invariants and rates, and the scalar value. Output includes GMT headers with reconstruction metadata, and coordinates follow GMT xy-format conventions with configurable coordinate order.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GMTFormatReconstructedScalarCoverageExport::(anonymous)::reconstructed_scalar_coverage_seq_type`](#gplatesfileiogmtformatreconstructedscalarcoverageexportanonymousreconstructed_scalar_coverage_seq_type) | typedef | — | — | 0 | Convenience typedef for a sequence of reconstructed scalar coverages. |
| [`GPlatesFileIO::GMTFormatReconstructedScalarCoverageExport::reconstructed_scalar_coverage_group_type`](#gplatesfileiogmtformatreconstructedscalarcoverageexportreconstructed_scalar_coverage_group_type) | typedef | — | — | 0 | Typedef for a feature geometry group of ReconstructedScalarCoverage objects. |
| [`GPlatesFileIO::GMTFormatReconstructedScalarCoverageExport::referenced_files_collection_type`](#gplatesfileiogmtformatreconstructedscalarcoverageexportreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |

## Members

### `GPlatesFileIO::GMTFormatReconstructedScalarCoverageExport::(anonymous)::reconstructed_scalar_coverage_seq_type`

*None.*

### `GPlatesFileIO::GMTFormatReconstructedScalarCoverageExport::reconstructed_scalar_coverage_group_type`

*None.*

### `GPlatesFileIO::GMTFormatReconstructedScalarCoverageExport::referenced_files_collection_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `print_gmt_scalar_coverage_line( QTextStream &output_stream, const GPlatesMaths::PointOnSphere &domain_point, bool domain_point_lon_lat_format, boost::optional<const double &> dilatation_strain, boost::optional<const double &> dilatation_strain_rate, boost::optional<const double &> second_invariant_strain_rate, const do ...` | function | `void` | Outputs a scalar coverage line to the GMT output. |
| `print_gmt_scalar_coverage( QTextStream &output_stream, const GPlatesAppLogic::ReconstructedScalarCoverage &reconstructed_scalar_coverage, bool domain_point_lon_lat_format, bool include_dilatation_strain, bool include_dilatation_strain_rate, bool include_second_invariant_strain_rate)` | function | `void` | Write the scalar coverage and optionally strain rates. |
| `GPLATES_FILE_IO_GMTFORMATRECONSTRUCTEDSCALARCOVERAGEEXPORT_H` | macro | `None` | — |
| `export_reconstructed_scalar_coverages( const std::list<reconstructed_scalar_coverage_group_type> &reconstructed_scalar_coverage_group, const QFileInfo& file_info, const referenced_files_collection_type &referenced_files, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id, const double &reconstruc ...` | function | `void` | Exports ReconstructedScalarCoverage objects. |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/ReconstructedScalarCoverageExport](ReconstructedScalarCoverageExport.md) | file-io | 7 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GMTFormatReconstructedScalarCoverageExport.h
python scripts/gpq.py def GPlatesFileIO::GMTFormatReconstructedScalarCoverageExport::(anonymous)::reconstructed_scalar_coverage_seq_type --body
python scripts/gpq.py uses reconstructed_scalar_coverage_seq_type --kind typedef
```

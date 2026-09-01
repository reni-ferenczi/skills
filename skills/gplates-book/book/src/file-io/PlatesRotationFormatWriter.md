# PlatesRotationFormatWriter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 252 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/PlatesRotationFormatWriter.h` | C++ | 205 |
| `src/file-io/PlatesRotationFormatWriter.cc` | C++ | 470 |

## Overview

`PlatesRotationFormatWriter` is a `ConstFeatureVisitor` that serializes total
reconstruction sequence features back out to the PLATES4 `.rot` line format (or
its GROT variant) — the counterpart to `PlatesRotationFormatReader`. As the
feature visitor walks a sequence feature's properties, it accumulates one
`PlatesRotationFormatAccumulator::ReconstructionPoleData` per `GpmlTimeSample`
found inside the `GpmlIrregularSampling` (`visit_gpml_irregular_sampling` /
`write_gpml_time_sample`), picking up the finite rotation, time, comment, disabled
flag and metadata for each sample, plus the moving and fixed plate IDs
(`visit_gpml_plate_id`). `finalise_post_feature_properties` then prints the
accumulated poles as PLATES4 lines only once
`PlatesRotationFormatAccumulator::have_sufficient_info_for_output` confirms every
sample has both a rotation and a time.

The `grot_format` constructor flag distinguishes GROT output, which is allowed to
carry metadata lines without an accompanying rotation pole, from plain PLATES4
`.rot` output, where every line must contain a pole; in PLATES4 mode a metadata-only
line is prefixed with a dummy `"999 0.0 0.0 0.0 0.0 999 !"` pole so the line
still parses as a (disabled) rotation entry.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::PlatesRotationFormatWriter`](#gplatesfileioplatesrotationformatwriter) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 2 | — |

## Members

### `GPlatesFileIO::PlatesRotationFormatWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PlatesRotationFormatWriter( const FileInfo &file_info, bool grot_format = false)` | constructor | `None` | public | If grot\_format is false then the GROT-style metadata (http://www.gplates.org/grot/index.html) is prefixed by "999 0.0 0.0 0.0 0.0 999 !" on lines that don't already contain a rotation pole. |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | protected | — |
| `finalise_post_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | protected | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | protected | — |
| `visit_gpml_finite_rotation( const GPlatesPropertyValues::GpmlFiniteRotation &gpml_finite_rotation)` | method | `void` | protected | — |
| `visit_gpml_irregular_sampling( const GPlatesPropertyValues::GpmlIrregularSampling &gpml_irregular_sampling)` | method | `void` | protected | — |
| `visit_gpml_plate_id( const GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | protected | — |
| `visit_xs_string( const GPlatesPropertyValues::XsString &xs_string)` | method | `void` | protected | — |
| `write_gpml_time_sample( const GPlatesPropertyValues::GpmlTimeSample &gpml_time_sample)` | method | `void` | protected | — |
| `PlatesRotationFormatAccumulator` | struct | `None` | protected | — |
| `d_grot_format` | field | `bool` | protected | Whether the output file is GROT ('.grot') format, or PLATES4('.rot') format. |
| `d_accum` | field | `PlatesRotationFormatAccumulator` | protected | — |
| `d_output_file` | field | `boost::scoped_ptr<QFile>` | protected | — |
| `d_output_stream` | field | `boost::scoped_ptr<QTextStream>` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `print_non_rotation_pole_line( QTextStream &os, const QString &line, bool grot_format)` | function | `void` | Print out a line that does not contain a rotation pole. |
| `print_rotation_pole( QTextStream &os, const GPlatesMaths::FiniteRotation &finite_rotation, int moving_plate_id, int fixed_plate_id, const double &time)` | function | `void` | Print the rotation pole data (with no newline). |
| `GPLATES_FILEIO_PLATESROTATIONFORMATWRITER_H` | macro | `None` | — |

## Notes

- The constructor throws `ErrorOpeningFileForWritingException` if the output file
  cannot be opened, so construction alone can fail before any feature is visited.
- A `ReconstructionPoleData` entry is skipped when writing out if it lacks both a
  finite rotation and a time (`have_sufficient_info_for_output`); an irregular
  sampling with an incomplete time sample therefore silently loses that sample on
  round-trip rather than erroring.
- `d_output_file`/`d_output_stream` are `boost::scoped_ptr`, so the writer owns the
  file for its own lifetime and closes it on destruction; the writer is not
  copyable as a result.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/PlatesRotationFileProxy](PlatesRotationFileProxy.md) | file-io | 32 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 25 |
| [file-io/PlatesRotationFormatReader](PlatesRotationFormatReader.md) | file-io | 21 |
| [feature-visitors/TotalReconstructionSequenceRotationInserter](../feature-visitors/TotalReconstructionSequenceRotationInserter.md) | feature-visitors | 10 |
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 4 |
| [property-values/GpmlIrregularSampling](../property-values/GpmlIrregularSampling.md) | property-values | 3 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 2 |
| [qt-widgets/EditTotalReconstructionSequenceWidget](../qt-widgets/EditTotalReconstructionSequenceWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/PlatesRotationFormatWriter.h
python scripts/gpq.py def GPlatesFileIO::PlatesRotationFormatWriter --body
python scripts/gpq.py uses PlatesRotationFormatWriter --kind class
python scripts/gpq.py hier PlatesRotationFormatWriter
```

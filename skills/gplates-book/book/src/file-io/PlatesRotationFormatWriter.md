# PlatesRotationFormatWriter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 252 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/PlatesRotationFormatWriter.h` | C++ | 205 |
| `src/file-io/PlatesRotationFormatWriter.cc` | C++ | 470 |

## Overview

[[[PROSE overview unit=file-io/PlatesRotationFormatWriter tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=file-io/PlatesRotationFormatWriter tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

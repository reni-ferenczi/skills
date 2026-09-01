# PlatesRotationFormatReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 523 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/PlatesRotationFormatReader.h` | C++ | 65 |
| `src/file-io/PlatesRotationFormatReader.cc` | C++ | 865 |

## Overview

Reads PLATES rotation-format files (simple ASCII format) and materializes them as GPlates features. Each line in a PLATES file contains a total reconstruction pole: moving plate ID, geological age, pole latitude and longitude, rotation angle, fixed plate ID, and an optional comment.

The reader groups poles by reference frame pairs and creates a `TotalReconstructionSequence` feature for each unique (fixed, moving) plate ID pair, with poles stored as an `GpmlIrregularSampling` of `GpmlFiniteRotation` values interpolated with `GpmlFiniteRotationSlerp`. Special handling treats poles with moving plate ID 999 as disabled (commented-out), and detects overlapping sequences with warnings. The reader also adjusts poles to ensure stage rotations take the geodesically short path rather than the long way around the globe.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::PoleParsingException`](#anonymouspoleparsingexception) | struct | — | — | 0 | FIXME: Give this a better name (and do the exception properly). |
| [`(anonymous)::TotalReconSeqProperties`](#anonymoustotalreconseqproperties) | struct | — | — | 0 | — |
| [`(anonymous)::UnexpectedlyNullIrregularSampling`](#anonymousunexpectedlynullirregularsampling) | struct | — | — | 0 | FIXME: Give this a better name (and do the exception properly). |
| [`GPlatesFileIO::PlatesRotationFormatReader`](#gplatesfileioplatesrotationformatreader) | class | — | — | 0 | A PLATES rotation-format reader is used to read the contents of a PLATES rotation-format file and parse it into the contents of a feature collection. |

## Members

### `(anonymous)::PoleParsingException`

*None.*

### `(anonymous)::TotalReconSeqProperties`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TotalReconSeqProperties()` | constructor | `None` | public | — |
| `d_irregular_sampling` | field | `boost::intrusive_ptr<GPlatesPropertyValues::GpmlIrregularSampling>` | public | — |
| `d_irregular_sampling_iter` | field | `GPlatesModel::FeatureHandle::iterator` | public | — |
| `d_fixed_plate_id` | field | `GPlatesModel::integer_plate_id_type` | public | — |
| `d_moving_plate_id` | field | `GPlatesModel::integer_plate_id_type` | public | — |

### `(anonymous)::UnexpectedlyNullIrregularSampling`

*None.*

### `GPlatesFileIO::PlatesRotationFormatReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `read_file( File::Reference &file, ReadErrorAccumulation &read_errors, bool &contains_unsaved_changes)` | method | `void` | public | Read the PLATES rotation-format file specified by fileinfo. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `geo_time_instants_are_approx_equal( const GPlatesPropertyValues::GeoTimeInstant &t1, const GPlatesPropertyValues::GeoTimeInstant &t2)` | function | `bool` | FIXME: Should this use some member function of GeoTimeInstant? |
| `gml_time_instants_are_approx_equal( GPlatesPropertyValues::GmlTimeInstant::non_null_ptr_to_const_type t1, GPlatesPropertyValues::GmlTimeInstant::non_null_ptr_to_const_type t2)` | function | `bool` | FIXME: Should this be some sort of utility function in GPlatesModel::ModelUtils? |
| `extract_comment( QTextStream &line_stream, QString &comment, boost::shared_ptr<GPlatesFileIO::DataSource> data_source, unsigned line_num, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `void` | From the remainder of an input line from a PLATES rotation-format file, strip any leading whitespace, then extract the comment, which is supposed to commence with an exclamation mark ('!'). |
| `parse_pole( QTextStream &line_stream, GPlatesModel::integer_plate_id_type &fixed_plate_id, GPlatesModel::integer_plate_id_type &moving_plate_id, boost::shared_ptr<GPlatesFileIO::DataSource> data_source, unsigned line_num, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::GpmlTimeSample` | Parse a single total reconstruction pole from a line of a PLATES rotation-format file. |
| `warn_user_about_new_overlapping_sequence( const GPlatesPropertyValues::GpmlTimeSample &time_sample, const GPlatesPropertyValues::GpmlTimeSample &prev_time_sample, boost::shared_ptr<GPlatesFileIO::DataSource> data_source, unsigned line_num, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `void` | — |
| `create_total_recon_seq( GPlatesModel::FeatureCollectionHandle::weak_ref &rotations, GPlatesModel::FeatureHandle::weak_ref &current_total_recon_seq, TotalReconSeqProperties &props_in_current_trs, const GPlatesPropertyValues::GpmlTimeSample &time_sample, GPlatesModel::integer_plate_id_type fixed_plate_id, GPlatesModel::i ...` | function | `void` | — |
| `add_time_sample( std::vector<GPlatesPropertyValues::GpmlTimeSample> &time_samples, GPlatesPropertyValues::GpmlTimeSample &time_sample, const boost::shared_ptr<GPlatesFileIO::DataSource> &data_source, unsigned line_num, GPlatesFileIO::ReadErrorAccumulation &read_errors, bool &contains_unsaved_changes)` | function | `void` | Add a time sample to an irregular sequence. |
| `append_pole_to_data_set( GPlatesModel::FeatureCollectionHandle::weak_ref &rotations, GPlatesModel::FeatureHandle::weak_ref &current_total_recon_seq, TotalReconSeqProperties &props_in_current_trs, GPlatesPropertyValues::GpmlTimeSample &time_sample, GPlatesModel::integer_plate_id_type fixed_plate_id, GPlatesModel::intege ...` | function | `void` | — |
| `handle_parsed_pole( GPlatesModel::FeatureCollectionHandle::weak_ref &rotations, GPlatesModel::FeatureHandle::weak_ref &current_total_recon_seq, TotalReconSeqProperties &props_in_current_trs, GPlatesPropertyValues::GpmlTimeSample &time_sample, GPlatesModel::integer_plate_id_type fixed_plate_id, GPlatesModel::integer_pla ...` | function | `void` | — |
| `populate_rotations( GPlatesModel::FeatureCollectionHandle::weak_ref &rotations, GPlatesFileIO::LineReader &line_buffer, boost::shared_ptr<GPlatesFileIO::DataSource> data_source, GPlatesFileIO::ReadErrorAccumulation &read_errors, bool &contains_unsaved_changes)` | function | `void` | Populate the feature collection rotations with the contents of a PLATES rotation-format file contained within line\_buffer. |
| `GPLATES_FILEIO_PLATESROTATIONFORMATREADER_H` | macro | `None` | — |

## Notes

Parsing errors and warnings are accumulated in the `read_errors` parameter rather than thrown; missing or malformed poles are logged but do not stop the read. The reader marks files as containing unsaved changes if it adjusts poles for short-path rotation. The two anonymous helper structs `PoleParsingException` and `UnexpectedlyNullIrregularSampling` are internal exceptions used for control flow.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/PlatesRotationFormatReader.h
python scripts/gpq.py def GPlatesFileIO::PlatesRotationFormatReader --body
python scripts/gpq.py uses PlatesRotationFormatReader --kind class
python scripts/gpq.py hier PlatesRotationFormatReader
```

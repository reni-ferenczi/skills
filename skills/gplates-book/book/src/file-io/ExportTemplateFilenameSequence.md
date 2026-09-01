# ExportTemplateFilenameSequence

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 596 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ExportTemplateFilenameSequence.h` | C++ | 389 |
| `src/file-io/ExportTemplateFilenameSequence.cc` | C++ | 151 |

## Overview

`ExportTemplateFilenameSequence` turns one filename template (a printf-style
string with placeholders such as `%n`, `%u`, `%f`, `%d`, `%R`, `%T`, `%D`,
`%A`) plus a reconstruction time range and increment into a forward-iterable
sequence of concrete filenames, one per exported frame. It exists so the
various export animation strategies in `gui` and the export-configuration
widgets in `qt-widgets` can share one implementation of "expand this template
for frame N at time T" instead of each re-deriving frame counts and format
substitution themselves.

The class itself is a thin, exception-safe front end: the constructor
validates the time increment (non-zero, matching the sign of end minus begin
time) and hands the real work — computing the frame count via
`GPlatesUtils::AnimationSequence::calculate_sequence` and expanding each
template — to `ExportTemplateFilenameSequenceImpl`, held by `boost::shared_ptr`
so cheap copies of the sequence share one implementation.
`ExportTemplateFilenameSequenceIterator` is a minimal forward iterator over
that implementation; `%T` and `%D` are resolved from the wall-clock time at
first dereference and then held fixed for the lifetime of that iterator, so
every filename produced by one iterator carries the same export timestamp.
`ExportTemplateFilename::validate_filename_template` lets callers such as
GUI validators check a template's syntax up front without constructing a
sequence.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ExportTemplateFilenameSequence`](#gplatesfileioexporttemplatefilenamesequence) | class | — | — | 0 | Generates a sequence of filenames given a filename template, a begin reconstruction time, an end reconstruction time and a reconstruction time increment. |
| [`GPlatesFileIO::ExportTemplateFilenameSequenceIterator`](#gplatesfileioexporttemplatefilenamesequenceiterator) | class | `boost::equality_comparable<ExportTemplateFilenameSequenceIterator>`<br>`boost::incrementable<ExportTemplateFilenameSequenceIterator>` | — | 0 | Forward iterator over export template filename sequence. |
| [`GPlatesFileIO::ExportTemplateFilename::TimeIncrementZero`](#gplatesfileioexporttemplatefilenametimeincrementzero) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | — |
| [`GPlatesFileIO::ExportTemplateFilename::IncorrectTimeIncrementSign`](#gplatesfileioexporttemplatefilenameincorrecttimeincrementsign) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | — |
| [`GPlatesFileIO::ExportTemplateFilename::UnrecognisedFormatString`](#gplatesfileioexporttemplatefilenameunrecognisedformatstring) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | — |
| [`GPlatesFileIO::ExportTemplateFilename::NoFilenameVariation`](#gplatesfileioexporttemplatefilenamenofilenamevariation) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | — |

## Members

### `GPlatesFileIO::ExportTemplateFilenameSequence`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `const_iterator` | typedef | `ExportTemplateFilenameSequenceIterator` | public | Typedef for the forward iterator over filenames. |
| `ExportTemplateFilenameSequence( const QString &filename_template, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id, const QString &default_recon_tree_layer_name, const GPlatesMaths::real_t &begin_reconstruction_time, const GPlatesMaths::real_t &end_reconstruction_time, const GPlatesMaths::real_ ...` | constructor | `None` | public | - will be padded to the width of the decimal integer representation of (size - 1). %f - the reconstruction-time instant of the frame, in printf-style %f format. %d - the reconstruction-time instant of the frame, in printf-style %d format, ... |
| `size()` | method | `std::size_t` | public | Returns the length of the sequence. |
| `begin()` | method | `const_iterator` | public | Begin forward iterator over sequence of filenames. |
| `end()` | method | `const_iterator` | public | End forward iterator over sequence of filenames. |
| `impl_ptr_type` | typedef | `boost::shared_ptr<ExportTemplateFilenameSequenceImpl>` | private | Typedef for pointer to implementation. |
| `d_impl` | field | `impl_ptr_type` | private | — |

### `GPlatesFileIO::ExportTemplateFilenameSequenceIterator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `iterator_category` | alias | `std::forward_iterator_tag` | public | Iterator typedefs. |
| `value_type` | alias | `const QString` | public | — |
| `difference_type` | alias | `std::ptrdiff_t` | public | — |
| `pointer` | alias | `const QString *` | public | — |
| `reference` | alias | `const QString &` | public | — |
| `ExportTemplateFilenameSequenceIterator()` | constructor | `None` | public | — |
| `ExportTemplateFilenameSequenceIterator( const ExportTemplateFilenameSequenceImpl *sequence_impl, std::size_t sequence_index)` | constructor | `None` | public | — |
| `operator*()` | operator | `QString` | public | Access current filename in sequence via iterator dereference. |
| `d_sequence_impl` | field | `ExportTemplateFilenameSequenceImpl` | private | — |
| `d_sequence_index` | field | `std::size_t` | private | — |
| `d_date_time` | field | `QDateTime` | private | — |
| `d_first_dereference` | field | `bool` | private | — |

### `GPlatesFileIO::ExportTemplateFilename::TimeIncrementZero`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TimeIncrementZero( const GPlatesUtils::CallStack::Trace &src)` | constructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |

### `GPlatesFileIO::ExportTemplateFilename::IncorrectTimeIncrementSign`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `IncorrectTimeIncrementSign( const GPlatesUtils::CallStack::Trace &src)` | constructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |

### `GPlatesFileIO::ExportTemplateFilename::UnrecognisedFormatString`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnrecognisedFormatString( const GPlatesUtils::CallStack::Trace &src, const QString &format_string)` | constructor | `None` | public | — |
| `~UnrecognisedFormatString()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_format_string` | field | `QString` | private | — |

### `GPlatesFileIO::ExportTemplateFilename::NoFilenameVariation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NoFilenameVariation( const GPlatesUtils::CallStack::Trace &src)` | constructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator*()` | operator | `QString` | — |
| `GPLATES_FILE_IO_EXPORTTEMPLATEFILENAMESEQUENCE_H` | macro | `None` | — |
| `validate_filename_template( const QString &filename_template, bool check_filename_variation = true)` | function | `void` | Tests for validity of parameters in the filename template. |
| `PLACEHOLDER_FORMAT_STRING` | variable | `QString` | Format string reserved for use by the client. |

## Notes

- The constructor throws `TimeIncrementZero` or `IncorrectTimeIncrementSign`
  before it ever touches the filename template, and can also throw
  `UnrecognisedFormatString` or `NoFilenameVariation` while building the
  `ExportTemplateFilenameSequenceImpl`; callers must be prepared to catch all
  four.
- `operator*()` on a default-constructed iterator throws
  `GPlatesGlobal::UninitialisedIteratorException` rather than dereferencing a
  null impl pointer.
- The wall-clock time used for `%T`/`%D` is captured lazily on an iterator's
  first dereference and then cached (`d_first_dereference`, `d_date_time`),
  so two iterators created moments apart from the same sequence can embed
  different timestamps, but repeated dereferences of the *same* iterator are
  stable.
- `ExportTemplateFilename::PLACEHOLDER_FORMAT_STRING` (`"%P"`) is deliberately
  left unexpanded by this class; it is a hook for callers (e.g. resolved
  topology export) to substitute their own per-boundary-type text after
  dereferencing.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/ExportTemplateFilenameSequenceFormats](ExportTemplateFilenameSequenceFormats.md) | file-io | 98 |
| [file-io/ExportTemplateFilenameSequenceImpl](ExportTemplateFilenameSequenceImpl.md) | file-io | 41 |
| [qt-widgets/ExportVelocityOptionsWidget](../qt-widgets/ExportVelocityOptionsWidget.md) | qt-widgets | 18 |
| [qt-widgets/ConfigureExportParametersDialog](../qt-widgets/ConfigureExportParametersDialog.md) | qt-widgets | 13 |
| [qt-widgets/ExportDeformationOptionsWidget](../qt-widgets/ExportDeformationOptionsWidget.md) | qt-widgets | 13 |
| [gui/ExportFileNameTemplateValidationUtils](../gui/ExportFileNameTemplateValidationUtils.md) | gui | 10 |
| [gui/ExportAnimationStrategy](../gui/ExportAnimationStrategy.md) | gui | 8 |
| [gui/ExportVelocityAnimationStrategy](../gui/ExportVelocityAnimationStrategy.md) | gui | 8 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 7 |
| [gui/ExportCitcomsResolvedTopologyAnimationStrategy](../gui/ExportCitcomsResolvedTopologyAnimationStrategy.md) | gui | 5 |
| [gui/ExportCoRegistrationAnimationStrategy](../gui/ExportCoRegistrationAnimationStrategy.md) | gui | 3 |
| [gui/ExportFlowlineAnimationStrategy](../gui/ExportFlowlineAnimationStrategy.md) | gui | 3 |
| [gui/ExportImageAnimationStrategy](../gui/ExportImageAnimationStrategy.md) | gui | 3 |
| [gui/ExportMotionPathAnimationStrategy](../gui/ExportMotionPathAnimationStrategy.md) | gui | 3 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 3 |
| [gui/ExportResolvedTopologyAnimationStrategy](../gui/ExportResolvedTopologyAnimationStrategy.md) | gui | 3 |
| [gui/ExportSvgAnimationStrategy](../gui/ExportSvgAnimationStrategy.md) | gui | 3 |
| [gui/ExportDeformationAnimationStrategy](../gui/ExportDeformationAnimationStrategy.md) | gui | 2 |
| [gui/ExportScalarCoverageAnimationStrategy](../gui/ExportScalarCoverageAnimationStrategy.md) | gui | 2 |
| [gui/ExportReconstructedGeometryAnimationStrategy](../gui/ExportReconstructedGeometryAnimationStrategy.md) | gui | 1 |

*... and 5 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ExportTemplateFilenameSequence.h
python scripts/gpq.py def GPlatesFileIO::ExportTemplateFilenameSequence --body
python scripts/gpq.py uses ExportTemplateFilenameSequence --kind class
python scripts/gpq.py hier ExportTemplateFilenameSequence
```

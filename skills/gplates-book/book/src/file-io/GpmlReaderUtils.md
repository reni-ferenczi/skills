# GpmlReaderUtils

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1427 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GpmlReaderUtils.h` | C++ | 132 |
| `src/file-io/GpmlReaderUtils.cc` | C++ | 134 |

## Overview

`GpmlReaderUtils::ReaderParams` bundles the four pieces of state a GPML parsing
function threads through recursive calls: the `QXmlStreamReader`, the `DataSource`
identifying which file is being read, the `ReadErrorAccumulation` to report into,
and a `contains_unsaved_changes` flag readers set when they had to reinterpret or
repair something in the file. Passing this one struct instead of four separate
parameters keeps the many `create_*`/`visit_*` reader signatures across
`GpmlPropertyReader`, `GpmlUpgradeReaderUtils` and related units manageable.

The `append_warning`/`append_recoverable_error_if`/`append_terminating_error_if`/
`append_failure_to_begin_if` family are thin, uniform wrappers around building a
`ReadErrorOccurrence` (using either an explicit `XmlNode`'s line number or the
stream reader's current position) and pushing it onto the matching bucket in
`params.errors` — warnings, recoverable errors, terminating errors, or
failures-to-begin respectively. Each `_if` variant only records the error when
`condition` is true and always returns `condition`, so call sites can use it
directly as the branch condition for "was this actually a problem".

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GpmlReaderUtils::ReaderParams`](#gplatesfileiogpmlreaderutilsreaderparams) | struct | — | — | 0 | — |

## Members

### `GPlatesFileIO::GpmlReaderUtils::ReaderParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `reader` | field | `QXmlStreamReader` | public | — |
| `source` | field | `boost::shared_ptr<GPlatesFileIO::DataSource>` | public | — |
| `errors` | field | `GPlatesFileIO::ReadErrorAccumulation` | public | — |
| `contains_unsaved_changes` | field | `bool` | public | — |
| `ReaderParams( QXmlStreamReader &reader_, boost::shared_ptr<GPlatesFileIO::DataSource> &source_, GPlatesFileIO::ReadErrorAccumulation &errors_, bool &contains_unsaved_changes_)` | constructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `append_error_if( bool condition, const GPlatesModel::XmlNode::non_null_ptr_type &current_elem, GPlatesFileIO::ReadErrorAccumulation::read_error_collection_type &errors, const GPlatesFileIO::GpmlReaderUtils::ReaderParams &params, GPlatesFileIO::ReadErrors::Description desc, GPlatesFileIO::ReadErrors::Result res)` | function | `bool` | — |
| `append_error_if( bool condition, GPlatesFileIO::ReadErrorAccumulation::read_error_collection_type &errors, const GPlatesFileIO::GpmlReaderUtils::ReaderParams &params, GPlatesFileIO::ReadErrors::Description desc, GPlatesFileIO::ReadErrors::Result res)` | function | `bool` | — |
| `GPLATES_FILEIO_GPMLREADERUTILS_H` | macro | `None` | — |
| `append_warning_if( bool condition, const GPlatesModel::XmlNode::non_null_ptr_type &current_elem, ReaderParams &params, const ReadErrors::Description &desc, const ReadErrors::Result &res)` | function | `bool` | Warning and error logging helper functions. |
| `append_warning( const GPlatesModel::XmlNode::non_null_ptr_type &current_elem, ReaderParams &params, const ReadErrors::Description &desc, const ReadErrors::Result &res)` | function | `bool` | — |
| `append_warning_if( bool condition, ReaderParams &params, const ReadErrors::Description &desc, const ReadErrors::Result &res)` | function | `bool` | — |
| `append_warning( ReaderParams &params, const ReadErrors::Description &desc, const ReadErrors::Result &res)` | function | `bool` | — |
| `append_recoverable_error_if( bool condition, const GPlatesModel::XmlNode::non_null_ptr_type &current_elem, ReaderParams &params, const ReadErrors::Description &desc, const ReadErrors::Result &res)` | function | `bool` | — |
| `append_terminating_error_if( bool condition, const GPlatesModel::XmlNode::non_null_ptr_type &current_elem, ReaderParams &params, const ReadErrors::Description &desc, const ReadErrors::Result &res)` | function | `bool` | — |
| `append_failure_to_begin_if( bool condition, ReaderParams &params, const ReadErrors::Description &desc, const ReadErrors::Result &res)` | function | `bool` | — |

## Notes

`append_failure_to_begin_if` records into the same `d_recoverable_errors` bucket as
`append_recoverable_error_if` despite its distinct name and intended meaning
("failed to begin reading this feature/property") — there is no separate
failures-to-begin collection at this level, so do not assume the two are reported
differently downstream.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlPropertyReader](GpmlPropertyReader.md) | file-io | 29 |
| [file-io/GpmlUpgradeReaderUtils](GpmlUpgradeReaderUtils.md) | file-io | 14 |
| [file-io/deprecated/FeaturePropertiesMap](deprecated/FeaturePropertiesMap.md) | file-io | 12 |
| [file-io/GpmlFeatureReaderImpl](GpmlFeatureReaderImpl.md) | file-io | 9 |
| [file-io/GpmlReader](GpmlReader.md) | file-io | 9 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 1 |
| [file-io/GpmlStructuralTypeReaderUtils](GpmlStructuralTypeReaderUtils.md) | file-io | 1 |
| [qt-widgets/VisualLayersListView](../qt-widgets/VisualLayersListView.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GpmlReaderUtils.h
python scripts/gpq.py def GPlatesFileIO::GpmlReaderUtils::ReaderParams --body
python scripts/gpq.py uses ReaderParams --kind struct
python scripts/gpq.py hier ReaderParams
```

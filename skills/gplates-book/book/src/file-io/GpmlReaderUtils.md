# GpmlReaderUtils

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1427 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GpmlReaderUtils.h` | C++ | 132 |
| `src/file-io/GpmlReaderUtils.cc` | C++ | 134 |

## Overview

[[[PROSE overview unit=file-io/GpmlReaderUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=file-io/GpmlReaderUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

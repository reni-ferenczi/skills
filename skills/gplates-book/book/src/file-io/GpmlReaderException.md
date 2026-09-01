# GpmlReaderException

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1314 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GpmlReaderException.h` | C++ | 94 |

## Overview

[[[PROSE overview unit=file-io/GpmlReaderException tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GpmlReaderException`](#gplatesfileiogpmlreaderexception) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | An exception type used when reading GPML files. |

## Members

### `GPlatesFileIO::GpmlReaderException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GpmlReaderException( const GPlatesUtils::CallStack::Trace &exception_source_, const GPlatesModel::XmlElementNode::non_null_ptr_type &location_, const ReadErrors::Description &description_, const char *source_location_ = "not specified")` | constructor | `None` | public | — |
| `~GpmlReaderException()` | destructor | `None` | public | — |
| `location()` | method | `GPlatesModel::XmlElementNode::non_null_ptr_type` | public | — |
| `description()` | method | `ReadErrors::Description` | public | — |
| `source_location()` | method | `char` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `d_location` | field | `GPlatesModel::XmlElementNode::non_null_ptr_type` | private | — |
| `d_description` | field | `ReadErrors::Description` | private | — |
| `d_source_location` | field | `char` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILE_IO_GPMLREADEREXCEPTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/GpmlReaderException tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlStructuralTypeReaderUtils](GpmlStructuralTypeReaderUtils.md) | file-io | 49 |
| [file-io/GpmlPropertyReader](GpmlPropertyReader.md) | file-io | 10 |
| [file-io/GpmlFeatureReaderImpl](GpmlFeatureReaderImpl.md) | file-io | 7 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GpmlReaderException.h
python scripts/gpq.py def GPlatesFileIO::GpmlReaderException --body
python scripts/gpq.py uses GpmlReaderException --kind class
python scripts/gpq.py hier GpmlReaderException
```

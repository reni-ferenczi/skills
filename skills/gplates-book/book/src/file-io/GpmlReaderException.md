# GpmlReaderException

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1314 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GpmlReaderException.h` | C++ | 94 |

## Overview

`GpmlReaderException` is the exception the GPML structural-type readers throw when
an XML element cannot be parsed as its expected type at all — as opposed to a
recoverable problem, which goes through `ReadErrorAccumulation` instead. It carries
the offending `XmlElementNode`, a `ReadErrors::Description` code identifying what
went wrong, and an optional `source_location` string for the throwing call site, so
a catch site (typically higher up in `GpmlPropertyReader` or
`GpmlFeatureReaderImpl`) can report exactly which element and which reason caused
the read to fail.

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

*None.*

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

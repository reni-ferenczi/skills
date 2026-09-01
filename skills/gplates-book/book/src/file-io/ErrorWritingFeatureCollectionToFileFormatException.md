# ErrorWritingFeatureCollectionToFileFormatException

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 17 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ErrorWritingFeatureCollectionToFileFormatException.h` | C++ | 94 |

## Overview

Exception thrown when file-format-specific constraints prevent writing otherwise valid feature collection data. Examples include plate ID limits in the PLATES line format that conflict with data in the model. Aborts the entire write operation and the file is removed to prevent partial writes.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ErrorWritingFeatureCollectionToFileFormatException`](#gplatesfileioerrorwritingfeaturecollectiontofileformatexception) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | An exception during writing of feature collection data to a file format. |

## Members

### `GPlatesFileIO::ErrorWritingFeatureCollectionToFileFormatException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ErrorWritingFeatureCollectionToFileFormatException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | in which the problem occurs. |
| `~ErrorWritingFeatureCollectionToFileFormatException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILE_IO_ERRORWRITINGFEATURECOLLECTIONTOFILEFORMATEXCEPTION_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/PlatesLineFormatWriter](PlatesLineFormatWriter.md) | file-io | 2 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ErrorWritingFeatureCollectionToFileFormatException.h
python scripts/gpq.py def GPlatesFileIO::ErrorWritingFeatureCollectionToFileFormatException --body
python scripts/gpq.py uses ErrorWritingFeatureCollectionToFileFormatException --kind class
python scripts/gpq.py hier ErrorWritingFeatureCollectionToFileFormatException
```

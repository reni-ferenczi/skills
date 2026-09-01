# FileLoadAbortedException

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1426 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/FileLoadAbortedException.h` | C++ | 90 |

## Overview

Exception thrown when a user cancels a file load operation. Captures both a descriptive message and the filename being loaded when the abort was requested, allowing handlers to report to the user which file was interrupted.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::FileLoadAbortedException`](#gplatesfileiofileloadabortedexception) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | Should be thrown when a file load is aborted by the user. |

## Members

### `GPlatesFileIO::FileLoadAbortedException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FileLoadAbortedException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg, const QString &filename_)` | constructor | `None` | public | — |
| `~FileLoadAbortedException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_msg` | field | `std::string` | private | — |
| `d_filename` | field | `QString` | private | The filename of the file for which loading was aborted. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILE_IO_FILELOADABORTEDEXCEPTION_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrReader](OgrReader.md) | file-io | 2 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 2 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/FileLoadAbortedException.h
python scripts/gpq.py def GPlatesFileIO::FileLoadAbortedException --body
python scripts/gpq.py uses FileLoadAbortedException --kind class
python scripts/gpq.py hier FileLoadAbortedException
```

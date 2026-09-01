# ErrorOpeningPipeFromGzipException

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1577 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ErrorOpeningPipeFromGzipException.h` | C++ | 101 |
| `src/file-io/ErrorOpeningPipeFromGzipException.cc` | C++ | 41 |

## Overview

[[[PROSE overview unit=file-io/ErrorOpeningPipeFromGzipException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ErrorOpeningPipeFromGzipException`](#gplatesfileioerroropeningpipefromgzipexception) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | This exception is thrown when GPlates cannot start the 'gzip' program to do on-the-fly compression to read a compressed GPML file. |

## Members

### `GPlatesFileIO::ErrorOpeningPipeFromGzipException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ErrorOpeningPipeFromGzipException( const GPlatesUtils::CallStack::Trace &exception_source, const QString &command_, const QString &filename_)` | constructor | `None` | public | Instantiate an exception for a file named filename. |
| `~ErrorOpeningPipeFromGzipException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_command` | field | `QString` | private | The command which could not be executed. |
| `d_filename` | field | `QString` | private | The filename of the file which couldn't be opened for reading. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_ERROROPENINGPIPEFROMGZIPEXCEPTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/ErrorOpeningPipeFromGzipException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 2 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 2 |
| [file-io/GpmlReader](GpmlReader.md) | file-io | 1 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 1 |
| [qt-widgets/ManageFeatureCollectionsDialog](../qt-widgets/ManageFeatureCollectionsDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ErrorOpeningPipeFromGzipException.h
python scripts/gpq.py def GPlatesFileIO::ErrorOpeningPipeFromGzipException --body
python scripts/gpq.py uses ErrorOpeningPipeFromGzipException --kind class
python scripts/gpq.py hier ErrorOpeningPipeFromGzipException
```

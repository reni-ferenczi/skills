# ErrorOpeningFileForReadingException

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1628 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ErrorOpeningFileForReadingException.h` | C++ | 91 |
| `src/file-io/ErrorOpeningFileForReadingException.cc` | C++ | 36 |

## Overview

`ErrorOpeningFileForReadingException` is the standard `GPlatesGlobal::Exception` thrown across `file-io` whenever a file cannot be opened for reading (permissions, missing file, locked file, and similar OS-level failures). It carries only the offending filename, retrievable via `filename()`, and its `write_message`/`exception_name` overrides give it a uniform message in the exception hierarchy's reporting. Its very wide fan-in — every format-specific reader in the module, plus consumers such as `Gpgim`, `ProjectSession` and `CommandLineParser` — reflects that it is the one exception type callers are expected to catch when a read operation might fail because the file itself is unreadable, as distinct from parse or format errors reported through `ReadErrorAccumulation`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ErrorOpeningFileForReadingException`](#gplatesfileioerroropeningfileforreadingexception) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | This exception is thrown when an error is encountered while attempting to open a file for reading. |

## Members

### `GPlatesFileIO::ErrorOpeningFileForReadingException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ErrorOpeningFileForReadingException( const GPlatesUtils::CallStack::Trace &exception_source, const QString &filename_)` | constructor | `None` | public | Instantiate an exception for a file named filename. |
| `~ErrorOpeningFileForReadingException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_filename` | field | `QString` | private | The filename of the file which couldn't be opened for reading. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_ERROROPENINGFILEFORREADINGEXCEPTION_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrReader](OgrReader.md) | file-io | 222 |
| [file-io/PlatesLineFormatReader](PlatesLineFormatReader.md) | file-io | 83 |
| [file-io/PlatesRotationFileProxy](PlatesRotationFileProxy.md) | file-io | 67 |
| [file-io/HellingerReader](HellingerReader.md) | file-io | 30 |
| [file-io/GmapReader](GmapReader.md) | file-io | 27 |
| [file-io/RasterReader](RasterReader.md) | file-io | 25 |
| [file-io/PlatesRotationFormatReader](PlatesRotationFormatReader.md) | file-io | 24 |
| [property-values/ProxiedRasterResolver](../property-values/ProxiedRasterResolver.md) | property-values | 16 |
| [file-io/ScalarField3DFileFormatReader](ScalarField3DFileFormatReader.md) | file-io | 10 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 8 |
| [file-io/GpmlReader](GpmlReader.md) | file-io | 7 |
| [utils/CommandLineParser](../utils/CommandLineParser.md) | utils | 7 |
| [file-io/SymbolFileReader](SymbolFileReader.md) | file-io | 3 |
| [model/Gpgim](../model/Gpgim.md) | model | 3 |
| [opengl/GLShaderSource](../opengl/GLShaderSource.md) | opengl | 3 |
| [presentation/ProjectSession](../presentation/ProjectSession.md) | presentation | 3 |
| [file-io/AgeModelReader](AgeModelReader.md) | file-io | 2 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 2 |
| [file-io/MipmappedRasterFormatReader](MipmappedRasterFormatReader.md) | file-io | 2 |
| [file-io/RgbaRasterReader](RgbaRasterReader.md) | file-io | 2 |

*... and 10 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ErrorOpeningFileForReadingException.h
python scripts/gpq.py def GPlatesFileIO::ErrorOpeningFileForReadingException --body
python scripts/gpq.py uses ErrorOpeningFileForReadingException --kind class
python scripts/gpq.py hier ErrorOpeningFileForReadingException
```

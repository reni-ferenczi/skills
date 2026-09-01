# ErrorOpeningFileForWritingException

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1629 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ErrorOpeningFileForWritingException.h` | C++ | 88 |
| `src/file-io/ErrorOpeningFileForWritingException.cc` | C++ | 37 |

## Overview

[[[PROSE overview unit=file-io/ErrorOpeningFileForWritingException tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ErrorOpeningFileForWritingException`](#gplatesfileioerroropeningfileforwritingexception) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | This exception is thrown when an error is encountered while attempting to open a file for writing. |

## Members

### `GPlatesFileIO::ErrorOpeningFileForWritingException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ErrorOpeningFileForWritingException( const GPlatesUtils::CallStack::Trace &exception_source, const QString &filename_)` | constructor | `None` | public | Instantiate an exception for a file named filename. |
| `~ErrorOpeningFileForWritingException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_filename` | field | `QString` | private | The filename of the file which couldn't be opened for writing. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_ERROROPENINGFILEFORWRITINGEXCEPTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/ErrorOpeningFileForWritingException tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlOutputVisitor](GpmlOutputVisitor.md) | file-io | 63 |
| [opengl/GLScalarField3DGenerator](../opengl/GLScalarField3DGenerator.md) | opengl | 41 |
| [file-io/OgrWriter](OgrWriter.md) | file-io | 39 |
| [file-io/PlatesRotationFormatWriter](PlatesRotationFormatWriter.md) | file-io | 14 |
| [file-io/GMTFormatWriter](GMTFormatWriter.md) | file-io | 12 |
| [file-io/PlatesLineFormatWriter](PlatesLineFormatWriter.md) | file-io | 12 |
| [file-io/LogToFileHandler](LogToFileHandler.md) | file-io | 10 |
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 9 |
| [file-io/GMTFormatFlowlineExport](GMTFormatFlowlineExport.md) | file-io | 8 |
| [file-io/GMTFormatMotionPathExport](GMTFormatMotionPathExport.md) | file-io | 8 |
| [file-io/OgrFormatReconstructedFeatureGeometryExport](OgrFormatReconstructedFeatureGeometryExport.md) | file-io | 6 |
| [file-io/ReconstructionGeometryExportImpl](ReconstructionGeometryExportImpl.md) | file-io | 6 |
| [app-logic/GPlatesQtMsgHandler](../app-logic/GPlatesQtMsgHandler.md) | app-logic | 4 |
| [file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport](CitcomsGMTFormatResolvedTopologicalBoundaryExport.md) | file-io | 4 |
| [file-io/CitcomsFormatVelocityVectorFieldExport](CitcomsFormatVelocityVectorFieldExport.md) | file-io | 3 |
| [file-io/GMTFormatResolvedTopologicalGeometryExport](GMTFormatResolvedTopologicalGeometryExport.md) | file-io | 3 |
| [file-io/MipmappedRasterFormatWriter](MipmappedRasterFormatWriter.md) | file-io | 3 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 3 |
| [presentation/ProjectSession](../presentation/ProjectSession.md) | presentation | 3 |
| [app-logic/FeatureCollectionFileIO](../app-logic/FeatureCollectionFileIO.md) | app-logic | 2 |

*... and 13 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ErrorOpeningFileForWritingException.h
python scripts/gpq.py def GPlatesFileIO::ErrorOpeningFileForWritingException --body
python scripts/gpq.py uses ErrorOpeningFileForWritingException --kind class
python scripts/gpq.py hier ErrorOpeningFileForWritingException
```

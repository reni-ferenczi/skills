# FileFormatNotSupportedException

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 17 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/FileFormatNotSupportedException.h` | C++ | 73 |

## Overview

[[[PROSE overview unit=file-io/FileFormatNotSupportedException tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::FileFormatNotSupportedException`](#gplatesfileiofileformatnotsupportedexception) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | Thrown when the user attempts to save a file in a format that is not yet supported. |

## Members

### `GPlatesFileIO::FileFormatNotSupportedException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FileFormatNotSupportedException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | — |
| `~FileFormatNotSupportedException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILE_IO_FILEFORMATNOTSUPPORTEDEXCEPTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/FileFormatNotSupportedException tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/ScalarField3DFileFormatReader](ScalarField3DFileFormatReader.md) | file-io | 14 |
| [app-logic/ScalarField3DLayerParams](../app-logic/ScalarField3DLayerParams.md) | app-logic | 5 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 5 |
| [file-io/MipmappedRasterFormatReader](MipmappedRasterFormatReader.md) | file-io | 5 |
| [file-io/SourceRasterFileCacheFormatReader](SourceRasterFileCacheFormatReader.md) | file-io | 5 |
| [file-io/CitcomsResolvedTopologicalBoundaryExport](CitcomsResolvedTopologicalBoundaryExport.md) | file-io | 3 |
| [file-io/ReconstructedFeatureGeometryExport](ReconstructedFeatureGeometryExport.md) | file-io | 3 |
| [file-io/ReconstructedFlowlineExport](ReconstructedFlowlineExport.md) | file-io | 3 |
| [file-io/ReconstructedMotionPathExport](ReconstructedMotionPathExport.md) | file-io | 3 |
| [file-io/ResolvedTopologicalGeometryExport](ResolvedTopologicalGeometryExport.md) | file-io | 3 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 3 |
| [file-io/DeformationExport](DeformationExport.md) | file-io | 1 |
| [file-io/MultiPointVectorFieldExport](MultiPointVectorFieldExport.md) | file-io | 1 |
| [file-io/RasterFileCacheFormatReader](RasterFileCacheFormatReader.md) | file-io | 1 |
| [file-io/ReconstructedScalarCoverageExport](ReconstructedScalarCoverageExport.md) | file-io | 1 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 1 |
| [qt-widgets/ManageFeatureCollectionsDialog](../qt-widgets/ManageFeatureCollectionsDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/FileFormatNotSupportedException.h
python scripts/gpq.py def GPlatesFileIO::FileFormatNotSupportedException --body
python scripts/gpq.py uses FileFormatNotSupportedException --kind class
python scripts/gpq.py hier FileFormatNotSupportedException
```

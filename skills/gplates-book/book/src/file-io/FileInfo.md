# FileInfo

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1478 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/FileInfo.h` | C++ | 180 |
| `src/file-io/FileInfo.cc` | C++ | 94 |

## Overview

[[[PROSE overview unit=file-io/FileInfo tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::FileInfo`](#gplatesfileiofileinfo) | class | — | — | 0 | Holds information associated with a loaded file. |

## Members

### `GPlatesFileIO::FileInfo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FileInfo( const QString &file_name)` | constructor | `None` | public | Construct a FileInfo for the given file\_name. |
| `FileInfo()` | constructor | `None` | public | Construct an empty FileInfo. |
| `get_display_name( bool use_absolute_path_name)` | method | `QString` | public | Return a string that can be used by the GUI to identify this file. |
| `get_file_name_without_extension()` | method | `QString` | public | Returns the file name up to (but not including) the last '.' character. |
| `d_file_info` | field | `QFileInfo` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_FILEINFO_H` | macro | `None` | — |
| `is_writable( const QString &filename)` | function | `bool` | This function attempts to open the file for writing. |
| `file_exists( const FileInfo &file_info)` | function | `bool` | — |
| `is_writable( const QFileInfo &file_info)` | function | `bool` | — |
| `is_writable( const FileInfo &file_info)` | function | `bool` | — |

## Notes

[[[PROSE notes unit=file-io/FileInfo tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/File](File.md) | file-io | 14 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 9 |
| [file-io/RasterFileCacheFormat](RasterFileCacheFormat.md) | file-io | 5 |
| [qt-widgets/ManageFeatureCollectionsDialog](../qt-widgets/ManageFeatureCollectionsDialog.md) | qt-widgets | 5 |
| [file-io/GmapReader](GmapReader.md) | file-io | 3 |
| [file-io/GpmlOutputVisitor](GpmlOutputVisitor.md) | file-io | 3 |
| [file-io/GpmlReader](GpmlReader.md) | file-io | 3 |
| [file-io/PlatesLineFormatWriter](PlatesLineFormatWriter.md) | file-io | 3 |
| [file-io/PlatesRotationFormatWriter](PlatesRotationFormatWriter.md) | file-io | 3 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 3 |
| [qt-widgets/AssignReconstructionPlateIdsDialog](../qt-widgets/AssignReconstructionPlateIdsDialog.md) | qt-widgets | 3 |
| [qt-widgets/FeatureSummaryWidget](../qt-widgets/FeatureSummaryWidget.md) | qt-widgets | 3 |
| [qt-widgets/VisualLayerWidget](../qt-widgets/VisualLayerWidget.md) | qt-widgets | 3 |
| [app-logic/FeatureCollectionFileIO](../app-logic/FeatureCollectionFileIO.md) | app-logic | 2 |
| [app-logic/FeatureCollectionFileState](../app-logic/FeatureCollectionFileState.md) | app-logic | 2 |
| [app-logic/ReconstructGraph](../app-logic/ReconstructGraph.md) | app-logic | 2 |
| [app-logic/deprecated/PlateVelocityWorkflow](../app-logic/deprecated/PlateVelocityWorkflow.md) | app-logic | 2 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 2 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 2 |
| [file-io/GpmlFormatDeformationExport](GpmlFormatDeformationExport.md) | file-io | 2 |

*... and 47 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/FileInfo.h
python scripts/gpq.py def GPlatesFileIO::FileInfo --body
python scripts/gpq.py uses FileInfo --kind class
python scripts/gpq.py hier FileInfo
```

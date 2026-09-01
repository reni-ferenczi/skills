# FeatureCollectionFileIO

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 247 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/FeatureCollectionFileIO.h` | C++ | 231 |
| `src/app-logic/FeatureCollectionFileIO.cc` | C++ | 382 |

## Overview

[[[PROSE overview unit=app-logic/FeatureCollectionFileIO tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::FeatureCollectionFileIO`](#gplatesapplogicfeaturecollectionfileio) | class | `QObject`<br>`boost::noncopyable` | — | 0 | Handles feature collection file loading/saving. |

## Members

### `GPlatesAppLogic::FeatureCollectionFileIO`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FeatureCollectionFileIO( GPlatesModel::ModelInterface &model, GPlatesFileIO::FeatureCollectionFileFormat::Registry &file_format_registry, FeatureCollectionFileState &file_state)` | constructor | `None` | public | — |
| `load_files( const QStringList &file_names)` | method | `std::vector<FeatureCollectionFileState::file_reference>` | public | Loads feature collections from multiple files named file\_names and adds them to the application state. |
| `load_file( const QString &filename)` | method | `FeatureCollectionFileState::file_reference` | public | Loads a feature collection from the file names file\_name and adds it to the application state. |
| `reload_file( FeatureCollectionFileState::file_reference file)` | method | `void` | public | Given a file\_reference, reloads the data for that file from disk, replacing the feature collection associated with that file\_reference in the application state. |
| `unload_file( FeatureCollectionFileState::file_reference file)` | method | `void` | public | This method simply delegates to FeatureCollectionFileState and removes the file from it. |
| `create_empty_file()` | method | `FeatureCollectionFileState::file_reference` | public | Creates a fresh, empty, FeatureCollection. |
| `create_file( const GPlatesFileIO::File::non_null_ptr_type &file, bool save = true)` | method | `FeatureCollectionFileState::file_reference` | public | Optionally saves the feature collection in file to the filename in file, and registers the file with FeatureCollectionFileState. |
| `save_file( GPlatesFileIO::File::Reference &file_ref, bool clear_unsaved_changes = true)` | method | `void` | public | Write the feature collection in file\_ref to the filename in file\_ref. |
| `count_features_in_xml_data( QByteArray &data)` | method | `int` | public | Returns the number of features in the xml data data; |
| `load_xml_data( const QString& filename, QByteArray &data)` | method | `void` | public | Load xml data in QByteArray. |
| `handle_read_errors( const GPlatesFileIO::ReadErrorAccumulation &read_errors)` | method | `void` | public | NOTE: all signals/slots should use namespace scope for all arguments otherwise differences between signals and slots will cause Qt to not be able to connect them at runtime. |
| `file_seq_type` | typedef | `std::vector<GPlatesFileIO::File::non_null_ptr_type>` | private | Typedef for a sequence of file shared refs. |
| `d_model` | field | `GPlatesModel::ModelInterface` | private | — |
| `d_file_format_registry` | field | `GPlatesFileIO::FeatureCollectionFileFormat::Registry` | private | A registry of the file formats for reading/writing feature collections. |
| `d_file_state` | field | `FeatureCollectionFileState` | private | The loaded feature collection files. |
| `read_feature_collections( const QStringList &filenames)` | method | `file_seq_type` | private | — |
| `read_feature_collection( GPlatesFileIO::File::Reference &file_ref)` | method | `void` | private | Read new features from file into file\_ref. |
| `emit_handle_read_errors_signal( const GPlatesFileIO::ReadErrorAccumulation &read_errors)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_FEATURECOLLECTIONFILEIO_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/FeatureCollectionFileIO tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ChooseFeatureCollectionWidget](../qt-widgets/ChooseFeatureCollectionWidget.md) | qt-widgets | 33 |
| [gui/UnsavedChangesTracker](../gui/UnsavedChangesTracker.md) | gui | 22 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 14 |
| [qt-widgets/ManageFeatureCollectionsDialog](../qt-widgets/ManageFeatureCollectionsDialog.md) | qt-widgets | 12 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 8 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 8 |
| [presentation/DeprecatedSessionRestore](../presentation/DeprecatedSessionRestore.md) | presentation | 5 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 5 |
| [app-logic/FeatureCollectionFileState](FeatureCollectionFileState.md) | app-logic | 3 |
| [presentation/SessionManagement](../presentation/SessionManagement.md) | presentation | 3 |
| [qt-widgets/ConnectWFSDialog](../qt-widgets/ConnectWFSDialog.md) | qt-widgets | 3 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 3 |
| [qt-widgets/CreateSmallCircleFeatureDialog](../qt-widgets/CreateSmallCircleFeatureDialog.md) | qt-widgets | 3 |
| [qt-widgets/CreateVGPDialog](../qt-widgets/CreateVGPDialog.md) | qt-widgets | 3 |
| [qt-widgets/GenerateVelocityDomainCitcomsDialog](../qt-widgets/GenerateVelocityDomainCitcomsDialog.md) | qt-widgets | 3 |
| [qt-widgets/GenerateVelocityDomainLatLonDialog](../qt-widgets/GenerateVelocityDomainLatLonDialog.md) | qt-widgets | 3 |
| [qt-widgets/GenerateVelocityDomainTerraDialog](../qt-widgets/GenerateVelocityDomainTerraDialog.md) | qt-widgets | 3 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 2 |
| [app-logic/ApplicationState](ApplicationState.md) | app-logic | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/FeatureCollectionFileIO.h
python scripts/gpq.py def GPlatesAppLogic::FeatureCollectionFileIO --body
python scripts/gpq.py uses FeatureCollectionFileIO --kind class
python scripts/gpq.py hier FeatureCollectionFileIO
```

# FeatureCollectionFileIO

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 247 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/FeatureCollectionFileIO.h` | C++ | 231 |
| `src/app-logic/FeatureCollectionFileIO.cc` | C++ | 382 |

## Overview

`FeatureCollectionFileIO` is the single entry point the rest of the application uses to load, save, reload and unload feature collection files, delegating the bookkeeping of which files are currently open to `FeatureCollectionFileState` and the actual format-specific reading and writing to `GPlatesFileIO::FeatureCollectionFileFormat::Registry`. It is a `QObject` so it can report read problems asynchronously through the `handle_read_errors` signal rather than forcing every caller to inspect a `GPlatesFileIO::ReadErrorAccumulation` directly.

`load_files()` exists alongside `load_file()` because loading a group of files together lets `FeatureCollectionFileState` send one notification instead of many; this matters for feature collections that reference each other, such as topological boundary features, which must find their referenced features already loaded in the model before they resolve. `create_file()` and `save_file()` cover the write side: `create_file()` registers a feature collection that did not originate from a file (optionally writing it to disk first), while `save_file()` writes an already-registered file's collection without touching `FeatureCollectionFileState`.

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

- `load_files()`, `load_file()`, `reload_file()` and `save_file()` each wrap their model changes in a `GPlatesModel::NotificationGuard` so the model emits a single change event instead of one per feature; `unload_file()` deliberately does not, because the model currently loses a removed feature collection's pending "publisher deactivated" callbacks if the notification is deferred past removal — a known model limitation noted in the source, not a bug in this class.
- `reload_file()` removes every feature from the existing `FeatureCollectionHandle` and re-populates it in place, rather than replacing the handle, so that outstanding `weak_ref`s and model callbacks into that feature collection stay valid across a reload.
- `save_file()` throws `GPlatesGlobal::InvalidFeatureCollectionException` if the file's feature collection is invalid; pass `clear_unsaved_changes = false` when saving a copy so the original file is still flagged as having unsaved changes.

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

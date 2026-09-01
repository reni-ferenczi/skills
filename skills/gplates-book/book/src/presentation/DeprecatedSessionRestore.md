# DeprecatedSessionRestore

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 202 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/DeprecatedSessionRestore.h` | C++ | 54 |
| `src/presentation/DeprecatedSessionRestore.cc` | C++ | 623 |

## Overview

Provides backward-compatibility loading of sessions saved before the scribe serialization framework was introduced. Session files from versions 1–3 stored layers and their connections as XML DOM; this module parses that format, reconstructs layers from their type and parameters, and re-establishes the connections between them and input files. The main entry point `restore_session()` branches on the session version and delegates to helper functions that parse DOM elements into `ReconstructGraph` layers and connections. A RAII class suppresses automatic layer creation during restore so that the recovered state exactly matches the saved state.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::IdLayerMap`](#anonymousidlayermap) | typedef | — | — | 0 | — |
| [`(anonymous)::IdLayerTaskTypeMap`](#anonymousidlayertasktypemap) | typedef | — | — | 0 | — |
| [`(anonymous)::SuppressAutoLayerCreationRAII`](#anonymoussuppressautolayercreationraii) | class | `boost::noncopyable` | — | 0 | Enable RAII style 'lock' on temporarily disabling automatic layer creation within app-state for as long as the current scope holds onto this object. |

## Members

### `(anonymous)::IdLayerMap`

*None.*

### `(anonymous)::IdLayerTaskTypeMap`

*None.*

### `(anonymous)::SuppressAutoLayerCreationRAII`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SuppressAutoLayerCreationRAII( GPlatesAppLogic::ApplicationState &_app_state)` | constructor | `None` | public | — |
| `~SuppressAutoLayerCreationRAII()` | destructor | `None` | public | — |
| `d_app_state_ptr` | field | `GPlatesAppLogic::ApplicationState` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `load_layer_task_type( QDomElement el, int session_version)` | function | `boost::optional<GPlatesAppLogic::LayerTaskType::Type>` | Returns the layer task type id. |
| `get_layer_task_type( GPlatesAppLogic::LayerTaskRegistry &ltr, GPlatesAppLogic::LayerTaskType::Type layer_type)` | function | `GPlatesAppLogic::LayerTaskRegistry::LayerTaskType` | — |
| `load_layer( GPlatesAppLogic::LayerTaskRegistry &ltr, GPlatesAppLogic::ReconstructGraph &rg, QDomElement el, IdLayerMap &idmap, int session_version)` | function | `GPlatesAppLogic::Layer` | Load a Layer into the ReconstructGraph from a QDomElement. |
| `get_input_file_by_id( GPlatesAppLogic::FeatureCollectionFileState &fs, GPlatesAppLogic::ReconstructGraph &rg, const QString &id)` | function | `GPlatesAppLogic::Layer::InputFile` | A bit hackish, probably better to use an \*IdMap style system as we do for the Layers, But for now file path as ID should work fine and is easier. |
| `get_layer_input_channel_name( const QString &layer_input_channel_name)` | function | `boost::optional<GPlatesAppLogic::LayerInputChannelName::Type>` | Layer input channel names are now enumerations (not strings). |
| `load_layer_connection( GPlatesAppLogic::FeatureCollectionFileState &fs, GPlatesAppLogic::LayerTaskRegistry &ltr, GPlatesAppLogic::ReconstructGraph &rg, QDomElement el, IdLayerMap &idmap, int session_version)` | function | `GPlatesAppLogic::Layer::InputConnection` | Load a Layer::InputConnection into the ReconstructGraph from a QDomElement. |
| `load_layers_state( const QDomDocument &dom, int session_version, GPlatesAppLogic::ApplicationState &app_state)` | function | `void` | Convert xml-domified layers state to actual connections in the ReconstructGraph. |
| `strip_bad_filenames( QStringList filenames, QStringList &bad_filenames)` | function | `QStringList` | Since attempting to load some files which do not exist (amongst a list of otherwise-okay files) will currently fail part-way through with an exception, we apply this function to remove any such problematic files from a Session's file-list ... |
| `GPLATES_PRESENTATION_DEPRECATEDSESSIONRESTORE_H` | macro | `None` | — |
| `restore_session( int version, const QDateTime &time, const QStringList &loaded_files, const QString &layers_state)` | function | `void` | Handles the old way of restoring sessions before the general scribe system was introduced. |

## Notes

Deprecated since session version 4; do not use for new code. Files not found during load are reported in the read errors dialog rather than raising an exception. Converts deprecated string-based layer input channel names (e.g. `"Topological boundary section features"`) to their modern enumeration equivalents. Version 1 introduced topological boundary section connections; version 2 deprecated them as redundant, so the loader silently drops those connections on restore from version-1 sessions.

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/InternalSession](InternalSession.md) | presentation | 16 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/DeprecatedSessionRestore.h
python scripts/gpq.py def (anonymous)::SuppressAutoLayerCreationRAII --body
python scripts/gpq.py uses SuppressAutoLayerCreationRAII --kind class
python scripts/gpq.py hier SuppressAutoLayerCreationRAII
```

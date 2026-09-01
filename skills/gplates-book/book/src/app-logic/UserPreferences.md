# UserPreferences

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 198 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/UserPreferences.h` | C++ | 423 |
| `src/app-logic/UserPreferences.cc` | C++ | 570 |

## Overview

[[[PROSE overview unit=app-logic/UserPreferences tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::UserPreferences`](#gplatesapplogicuserpreferences) | class | [`GPlatesUtils::ConfigInterface`](../utils/ConfigInterface.md) | — | 0 | Handles User Preference and internal GPlates state storage via QSettings backend. |

## Members

### `GPlatesAppLogic::UserPreferences`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `KeyValueMap` | typedef | `QMap<QString, QVariant>` | public | — |
| `UserPreferences( QObject *_parent)` | constructor | `None` | public | — |
| `~UserPreferences()` | destructor | `None` | public | — |
| `get_value( const QString &key)` | method | `QVariant` | public | This should be your primary point of access for user preferences. |
| `has_been_set( const QString &key)` | method | `bool` | public | Indicates if this key has been overriden from the defaults by the user (or potentially, by GPlates) and set in the user's platform's 'registry'. |
| `get_default_value( const QString &key)` | method | `QVariant` | public | Fetches default value directly - only useful for user preferences dialog. |
| `exists( const QString &key)` | method | `bool` | public | Indicates if this key exists in any form, from the user profile or GPlates compiled-in defaults. |
| `default_exists( const QString &key)` | method | `bool` | public | Tests the existence of a compiled-in default key/value. |
| `set_value( const QString &key, const QVariant &value)` | method | `void` | public | Sets new user value, overriding any compiled-in defaults. |
| `clear_value( const QString &key)` | method | `void` | public | Clears any user-set value, reverting to a default value if one exists. |
| `clear_prefix( const QString &prefix)` | method | `void` | public | Clears any user-set value for all keys with the given prefix, reverting to a default value if one exists. |
| `subkeys( const QString &prefix = "")` | method | `QStringList` | public | Lists all keys, including sub-keys, from the given prefix. |
| `root_entries( const QString &prefix = "")` | method | `QStringList` | public | Lists all "root entries", or entries available for a given prefix. |
| `extract_keyvalues_as_configbundle( const QString &prefix)` | method | `GPlatesUtils::ConfigBundle` | public | Given a prefix to a set of keys, extract all those keys and values into a GPlatesUtils::ConfigBundle. |
| `insert_keyvalues_from_configbundle( const QString &prefix, const GPlatesUtils::ConfigBundle &bundle)` | method | `void` | public | Given a prefix in the key-value store, and a GPlatesUtils::ConfigBundle, set all the given keys in one pass. |
| `get_keyvalues_as_map( const QString &prefix)` | method | `KeyValueMap` | public | Given a prefix to a set of keys, slurp all those keys and values into a QMap\<QString, QVariant\>. |
| `set_keyvalues_from_map( const QString &prefix, const KeyValueMap &keyvalues)` | method | `void` | public | Given a prefix in the key-value store, and a map of keyname-\>value in a QMap\<QString, QVariant\>, set all the given keys in one pass. |
| `debug_file_locations()` | method | `void` | public | Indicates where settings are stored to console. |
| `debug_key_values()` | method | `void` | public | Writes all keys and values to console. |
| `initialise_versioning()` | method | `void` | private | Configures preference keys for multiple-GPlates-version support. |
| `store_executable_path()` | method | `void` | private | Stores executable path of current application in user settings. |
| `d_key_root` | field | `QString` | private | If this string ! .isNull(), all settings operations will be performed on a 'subdirectory' of the keystore - this is so that we can support simultaneous use of different gplates versions with different settings. |
| `s_defaults` | field | `QPointer<QSettings>` | private | Our default settings, loaded from a compiled-in resource file. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `set_magic_defaults( QSettings &defaults)` | function | `void` | Sets "magic" default preference values that are derived from system calls. |
| `s_defaults` | variable | `QPointer<QSettings>` | — |
| `GPLATES_APP_LOGIC_USERPREFERENCES_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/UserPreferences tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/InternalSession](../presentation/InternalSession.md) | presentation | 37 |
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 31 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 30 |
| [gui/DrawStyleManager](../gui/DrawStyleManager.md) | gui | 19 |
| [qt-widgets/HellingerConfigurationDialog](../qt-widgets/HellingerConfigurationDialog.md) | qt-widgets | 19 |
| [gui/PythonManager](../gui/PythonManager.md) | gui | 13 |
| [presentation/SessionManagement](../presentation/SessionManagement.md) | presentation | 13 |
| [gui/AnimationController](../gui/AnimationController.md) | gui | 12 |
| [gui/FileIODirectoryConfigurations](../gui/FileIODirectoryConfigurations.md) | gui | 10 |
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 8 |
| [qt-widgets/ConnectWFSDialog](../qt-widgets/ConnectWFSDialog.md) | qt-widgets | 6 |
| [qt-widgets/ExportAnimationDialog](../qt-widgets/ExportAnimationDialog.md) | qt-widgets | 6 |
| [qt-widgets/KinematicGraphsDialog](../qt-widgets/KinematicGraphsDialog.md) | qt-widgets | 6 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 6 |
| [api/PythonUtils](../api/PythonUtils.md) | api | 5 |
| [gui/CommandServer](../gui/CommandServer.md) | gui | 5 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 4 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 4 |
| [qt-widgets/AgeModelManagerDialog](../qt-widgets/AgeModelManagerDialog.md) | qt-widgets | 3 |
| [presentation/TopologyGeometryVisualLayerParams](../presentation/TopologyGeometryVisualLayerParams.md) | presentation | 2 |

*... and 13 more units.*

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `reply` | `finished()` | `&loop` | `quit()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/UserPreferences.h
python scripts/gpq.py def GPlatesAppLogic::UserPreferences --body
python scripts/gpq.py uses UserPreferences --kind class
python scripts/gpq.py hier UserPreferences
```

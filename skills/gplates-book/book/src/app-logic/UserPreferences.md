# UserPreferences

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 198 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/UserPreferences.h` | C++ | 423 |
| `src/app-logic/UserPreferences.cc` | C++ | 570 |

## Overview

The application's key/value store, and despite the name it holds far more than user
preferences: recent sessions (`SessionManagement`, `InternalSession`), the last
executable path, drawing styles, dialog geometry, the Python script directories. It is
a `GPlatesUtils::ConfigInterface` implementation backed by `QSettings`, owned by
`ApplicationState` and reached everywhere through
`ApplicationState::get_user_preferences()`. Keys are `/`-separated paths with no
leading slash (`set_value` asserts on one), no values at the root, and `general`
reserved because Qt's `.ini` backend uses it.

Reads fall through two layers. The user layer is whatever `QSettings` chooses for the
platform — registry, `.conf`, or `plist`. Under it sits a read-only defaults layer:
`:/DefaultPreferences.conf`, a compiled-in Qt resource loaded once into the static
`s_defaults`, then topped up by the file-local `set_magic_defaults` with values that
can only be discovered at runtime — the platform's user-data and Documents
directories, the per-platform system script directory, and the HTTP proxy taken from
`QNetworkProxyFactory` or overridden by the `http_proxy` environment variable.
`get_value` returns the user value if the key has been set, otherwise the default,
otherwise a null `QVariant`; `has_been_set`, `default_exists` and `exists` let a
caller distinguish those cases, which is what the preferences dialog needs to show
which settings the user has actually touched.

The bulk operations exist because a subtree of keys is often one logical object. A
stored session is a prefix such as `session/recent/sessions/1` whose subkeys are its
fields, and `get_keyvalues_as_map` / `set_keyvalues_from_map` (and the
`GPlatesUtils::ConfigBundle` pair) move that whole subtree in and out in one pass, with
the prefix stripped. `subkeys` and `root_entries` merge the user keys and the default
keys, so they enumerate every key that *could* be read, not just the ones stored.

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

**There is no cached `QSettings` member — every call builds one on the stack.** Its
destructor syncs, which both flushes writes and re-reads anything another GPlates
process changed, so concurrent instances stay consistent. The price is that every
`get_value` is a registry or file access; `subkeys` and the map/bundle helpers call
`get_value` once per key, so a bulk read of a large prefix is that many accesses.
Read a preference once and keep it, rather than calling this in a loop or per frame.

**Constructing one has side effects, and it is constructed more than once.** The
constructor writes `version/current` and `paths/executables/gplates/last_used`
unconditionally, and on first construction it loads the defaults resource and runs
`set_magic_defaults`. That is why `s_defaults` is `static`: the header's long comment
records that GPlates could not guarantee a single `UserPreferences` instance, and that
re-running the magic defaults re-runs the macOS proxy probe — a nested `QEventLoop`
that waits on a network request (the sole `connect()` in this unit) and can stall
startup by a full network timeout when an interface is up but not working. The
`QPointer` also exists to *delay* that resource load until the application is running,
because loading `:/DefaultPreferences.conf` too early silently yielded zeroed defaults.

**Version sandboxing is declared but not wired up.** `d_key_root` is never assigned
anywhere in the unit, so it is always null and every `if (!d_key_root.isNull())
beginGroup(...)` guard is dead code; `initialise_versioning` only records the current
version. The header says as much ("NOT FULLY IMPLEMENTED") — do not rely on old
versions' settings being isolated.

**`clear_value` can create user-set keys as a side effect.** `QSettings::remove`
deletes an entire subtree, so to clear one leaf the method backs the subtree up with
`get_keyvalues_as_map`, removes, then writes the backup back. But that map is the
*merged* view: any subkey that previously existed only as a compiled-in default is
written into the user scope by the restore, and `has_been_set` will report it as
user-set from then on. `clear_prefix` is the honest way to drop a subtree.

**Signals and lifetimes.** `key_value_updated` is emitted from `set_value` only when
the value actually changed, but unconditionally from `clear_value` and once per call
from `clear_prefix` — the source carries a FIXME noting that one signal for a whole
prefix may not be what listeners want. `extract_keyvalues_as_configbundle` returns a
raw pointer to a `ConfigBundle` parented to the `UserPreferences` object, so it lives
until the application exits unless the caller reparents it; repeated calls accumulate.
Finally, values round-trip through the backend and may come back typed as `QString` —
always convert through `QVariant` rather than testing `type()`.

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

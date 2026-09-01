# ConfigInterface

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1117 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/ConfigInterface.h` | C++ | 303 |

## Overview

`GPlatesUtils::ConfigInterface` is the pure-virtual abstract base shared by
`GPlatesAppLogic::UserPreferences` and `GPlatesUtils::ConfigBundle`, so code
such as `ConfigBundleModel` that needs to treat "the application's real
preferences" and "a standalone bag of key/value settings" the same way can do
so polymorphically instead of duplicating logic per backend. It defines a
hierarchical key-value store with unix-style `/`-delimited keys, `QVariant`
values, and a two-tier user-value/default-value model: `get_value()` returns
whichever is in effect, `has_been_set()` and `default_exists()` distinguish
an explicit user override from a fallback default, and `clear_value()` /
`clear_prefix()` revert to defaults rather than deleting the key outright.

`subkeys()` and `root_entries()` give two different views over the same
prefix-delimited namespace — a flat recursive listing versus one level of
"directory" names — and `get_keyvalues_as_map()` / `set_keyvalues_from_map()`
let a whole subtree of keys be read or written as a single `KeyValueMap`,
which is how composite objects like a `GPlatesUtils::Session` are persisted
under one key prefix. The `key_value_updated` Qt signal lets observers (e.g.
preference-editing UI) react to any change regardless of which concrete
backend made it.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::ConfigInterface`](#gplatesutilsconfiginterface) | class | `QObject`<br>`boost::noncopyable` | — | 2 | This class defines the common interface to both GPlatesAppLogic::UserPreferences and GPlatesUtils::ConfigBundle. |

## Members

### `GPlatesUtils::ConfigInterface`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `KeyValueMap` | typedef | `QMap<QString, QVariant>` | public | — |
| `ConfigInterface( QObject *_parent)` | constructor | `None` | public | Constructor signature is effectively QObject's constructor. |
| `~ConfigInterface()` | destructor | `None` | public | — |
| `get_value( const QString &key)` | method | `QVariant` | public | This should be your primary point of access for key values. |
| `has_been_set( const QString &key)` | method | `bool` | public | Indicates if this key has been overriden from the defaults by the user (or potentially, by GPlates) and set in the config bundle. |
| `get_default_value( const QString &key)` | method | `QVariant` | public | Fetches default value directly - only useful for user interactions. |
| `exists( const QString &key)` | method | `bool` | public | Indicates if this key exists in any form, from this config bundle or some sort of defaults provided from another bundle linked to this one. |
| `default_exists( const QString &key)` | method | `bool` | public | Tests the existence of an assigned default key/value. |
| `set_value( const QString &key, const QVariant &value)` | method | `void` | public | Sets new user value, overriding any default that may or may not exist for that key. |
| `clear_value( const QString &key)` | method | `void` | public | Clears any user-set value, reverting to a default value if one exists. |
| `clear_prefix( const QString &prefix)` | method | `void` | public | Clears any user-set value for all keys with the given prefix, reverting to a default value if one exists. |
| `subkeys( const QString &prefix = "")` | method | `QStringList` | public | Lists all keys, including sub-keys, from the given prefix. |
| `root_entries( const QString &prefix = "")` | method | `QStringList` | public | Lists all "root entries", or entries available for a given prefix. |
| `get_keyvalues_as_map( const QString &prefix)` | method | `KeyValueMap` | public | Given a prefix to a set of keys, slurp all those keys and values into a QMap\<QString, QVariant\>. |
| `set_keyvalues_from_map( const QString &prefix, const KeyValueMap &keyvalues)` | method | `void` | public | Given a prefix in the key-value store, and a map of keyname-\>value in a QMap\<QString, QVariant\>, set all the given keys in one pass. |
| `key_value_updated( QString key)` | method | `void` | public | Signal emitted whenever a specific key's value is changed. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_CONFIGINTERFACE_H` | macro | `None` | — |

## Notes

- `get_value()` returns a null `QVariant` for a nonexistent key rather than
  throwing; that null value converts to `0`, `0.0` or `""` as appropriate, so
  a missing key is easy to miss if the caller doesn't also check `exists()`.
- Keys should be treated as case-sensitive even though a given backend might
  not enforce it, and must not begin with `/`.
- `exists()` returns `false` for a key that is only a "directory" prefix of
  other keys (no value stored at that exact path), even though `subkeys()`
  and `root_entries()` will list entries under it.
- The class derives from `boost::noncopyable`; a subclass must still declare
  `Q_OBJECT` itself for `moc` to wire up its own signals/slots, but can emit
  the base class's `key_value_updated` signal without redeclaring it.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ConfigGuiUtils](../gui/ConfigGuiUtils.md) | gui | 10 |
| [utils/ConfigBundle](ConfigBundle.md) | utils | 10 |
| [gui/ConfigModel](../gui/ConfigModel.md) | gui | 8 |
| [app-logic/UserPreferences](../app-logic/UserPreferences.md) | app-logic | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/ConfigInterface.h
python scripts/gpq.py def GPlatesUtils::ConfigInterface --body
python scripts/gpq.py uses ConfigInterface --kind class
python scripts/gpq.py hier ConfigInterface
```

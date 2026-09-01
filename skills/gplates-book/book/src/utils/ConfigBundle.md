# ConfigBundle

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1062 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/ConfigBundle.h` | C++ | 314 |
| `src/utils/ConfigBundle.cc` | C++ | 227 |

## Overview

[[[PROSE overview unit=utils/ConfigBundle tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::ConfigBundle`](#gplatesutilsconfigbundle) | class | [`ConfigInterface`](ConfigInterface.md) | — | 0 | A small, portable collection of key-value pairs that can be used independently of GPlates' UserPreferences system; changes to keys will emit appropriate update signals but the 'bundle' of key-value pairs may be transient and not ... |

## Members

### `GPlatesUtils::ConfigBundle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConfigBundle( QObject *_parent)` | constructor | `None` | public | Constructor for an empty ConfigBundle. |
| `~ConfigBundle()` | destructor | `None` | public | — |
| `get_value( const QString &key)` | method | `QVariant` | public | This should be your primary point of access for key values. |
| `has_been_set( const QString &key)` | method | `bool` | public | Indicates if this key has been overriden from the defaults by the user (or potentially, by GPlates) and set in the config bundle. |
| `get_default_value( const QString &key)` | method | `QVariant` | public | Fetches default value directly - only useful for user interactions. |
| `exists( const QString &key)` | method | `bool` | public | Indicates if this key exists in any form, from this config bundle or some sort of defaults provided from another bundle linked to this one. |
| `default_exists( const QString &key)` | method | `bool` | public | Tests the existence of an assigned default key/value. |
| `set_value( const QString &key, const QVariant &value)` | method | `void` | public | Sets new user value, overriding any default that may or may not exist for that key. |
| `set_default_value( const QString &key, const QVariant &value)` | method | `void` | public | Sets new default value, which may be shadowed by a 'user set' key. |
| `clear_value( const QString &key)` | method | `void` | public | Clears any user-set value, reverting to a default value if one exists. |
| `clear_prefix( const QString &prefix)` | method | `void` | public | Clears any user-set value for all keys with the given prefix, reverting to a default value if one exists. |
| `subkeys( const QString &prefix = "")` | method | `QStringList` | public | Lists all keys, including sub-keys, from the given prefix. |
| `root_entries( const QString &prefix = "")` | method | `QStringList` | public | Lists all "root entries", or entries available for a given prefix. |
| `get_keyvalues_as_map( const QString &prefix)` | method | `KeyValueMap` | public | Given a prefix to a set of keys, slurp all those keys and values into a QMap\<QString, QVariant\>. |
| `set_keyvalues_from_map( const QString &prefix, const KeyValueMap &keyvalues)` | method | `void` | public | Given a prefix in the key-value store, and a map of keyname-\>value in a QMap\<QString, QVariant\>, set all the given keys in one pass. |
| `d_map` | field | `KeyValueMap` | private | Our insternal storage for the config. |
| `d_defaults` | field | `KeyValueMap` | private | Some defaults to fall back to - optional. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_CONFIGBUNDLE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=utils/ConfigBundle tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/UserPreferences](../app-logic/UserPreferences.md) | app-logic | 1 |
| [gui/DrawStyleManager](../gui/DrawStyleManager.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/ConfigBundle.h
python scripts/gpq.py def GPlatesUtils::ConfigBundle --body
python scripts/gpq.py uses ConfigBundle --kind class
python scripts/gpq.py hier ConfigBundle
```

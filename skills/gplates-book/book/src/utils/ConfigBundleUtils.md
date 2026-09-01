# ConfigBundleUtils

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1604 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/ConfigBundleUtils.h` | C++ | 97 |
| `src/utils/ConfigBundleUtils.cc` | C++ | 83 |

## Overview

`ConfigBundleUtils` provides utility functions for manipulating hierarchical key names in `ConfigBundle` and `UserPreferences`. The functions handle the "/" delimited path structure that both classes use: filtering keys by prefix, stripping prefixes from key lists, extracting root components, and composing full key names from components.

These utilities were formerly private helper functions but are exposed here for callers that need to perform advanced manipulation of hierarchical key structures—for example, when displaying key hierarchies in a UI or when dynamically constructing key paths from user input.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_CONFIGBUNDLEUTILS_H` | macro | `None` | — |
| `sanitise_key( const QString &key_with_slashes)` | function | `QString` | Necessary when dealing with generated key names. |
| `match_prefix( const QStringList &keys, const QString &prefix)` | function | `QStringList` | Returns a new list of only those key names that match a given prefix. |
| `strip_prefix( QStringList &keys, const QString &prefix)` | function | `void` | Modifies a list of key names to strip off a given prefix. |
| `strip_all_except_root( QStringList &keys)` | function | `void` | Modifies a list of key names to strip off everything past the first '/' character, if any. |
| `compose_keyname( const QString &prefix, const QString &subkey)` | function | `QString` | Intelligently concatenates a prefix with a (part of a) key name, inserting a '/' only if appropriate. |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [utils/ConfigBundle](ConfigBundle.md) | utils | 8 |
| [app-logic/UserPreferences](../app-logic/UserPreferences.md) | app-logic | 7 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/ConfigBundleUtils.h
```

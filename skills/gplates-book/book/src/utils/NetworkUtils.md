# NetworkUtils

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1296 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/NetworkUtils.h` | C++ | 62 |
| `src/utils/NetworkUtils.cc` | C++ | 96 |

## Overview

[[[PROSE overview unit=utils/NetworkUtils tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `build_proxy_type_map()` | function | `QMap<QNetworkProxy::ProxyType, QString>` | Defines a mapping between Qt proxy type enum and string, unique to GPlates (i.e. not useful outside of GPlates although 'http' and 'ftp' will probably be at least recognisable). |
| `url_scheme_for_proxy_type( QNetworkProxy::ProxyType type)` | function | `QString` | — |
| `proxy_type_for_url_scheme( const QString &scheme)` | function | `QNetworkProxy::ProxyType` | — |
| `GPLATES_UTILS_NETWORKUTILS_H` | macro | `None` | — |
| `get_url_for_proxy( const QNetworkProxy &proxy)` | function | `QUrl` | Returns a url which approximates the parameters of a QNetworkProxy. |
| `get_proxy_for_url( const QUrl &url)` | function | `QNetworkProxy` | Returns a QNetworkProxy object constructed from a url. |

## Notes

[[[PROSE notes unit=utils/NetworkUtils tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ConnectWFSDialog](../qt-widgets/ConnectWFSDialog.md) | qt-widgets | 5 |
| [app-logic/UserPreferences](../app-logic/UserPreferences.md) | app-logic | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/NetworkUtils.h
```

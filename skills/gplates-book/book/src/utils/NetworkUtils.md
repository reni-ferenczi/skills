# NetworkUtils

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1296 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/NetworkUtils.h` | C++ | 62 |
| `src/utils/NetworkUtils.cc` | C++ | 96 |

## Overview

Provides utilities for bidirectional conversion between `QNetworkProxy` objects and URL-like strings. The primary use is to serialize proxy settings into a form that can be stored in user preferences and later reconstructed. `get_url_for_proxy()` takes a proxy object and builds a URL with the scheme derived from the proxy type (e.g. "socks5", "http") and the user, password, hostname, and port fields set accordingly; `get_proxy_for_url()` reverses this process. Helper functions `build_proxy_type_map()`, `url_scheme_for_proxy_type()`, and `proxy_type_for_url_scheme()` maintain the mapping between Qt proxy type enums and their string representations.

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

*None.*

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

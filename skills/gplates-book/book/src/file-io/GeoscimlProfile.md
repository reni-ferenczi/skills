# GeoscimlProfile

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 986 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GeoscimlProfile.h` | C++ | 84 |
| `src/file-io/GeoscimlProfile.cc` | C++ | 160 |

## Overview

A parser for the GeoSciML XML format. `GeoscimlProfile` inherits from both `ArbitraryXmlProfile` and Qt's `QObject`, implementing the interface to extract features from GeoSciML documents and populate a `FeatureCollectionHandle` with them. It uses XQuery to locate feature members in the XML and dispatches them through factory handlers to create the GPlates feature model objects.

The class supports reading from either a file on disk or raw XML data in memory. It displays a progress dialog during parsing that can be cancelled by the user via the Qt slot mechanism. The `count_features` method allows clients to inspect the number of parseable features before attempting a full parse.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GeoscimlProfile`](#gplatesfileiogeoscimlprofile) | class | `QObject`<br>[`ArbitraryXmlProfile`](ArbitraryXmlProfile.md) | — | 0 | — |

## Members

### `GPlatesFileIO::GeoscimlProfile`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GeoscimlProfile()` | constructor | `None` | public | — |
| `GeoscimlProfile( const QString& profile_name)` | constructor | `None` | public | — |
| `populate( File::Reference& xml_file)` | method | `void` | public | — |
| `populate( QByteArray& xml_data, GPlatesModel::FeatureCollectionHandle::weak_ref fch)` | method | `void` | public | — |
| `count_features( QByteArray& xml_data)` | method | `int` | public | check for features, return the number |
| `cancel()` | method | `void` | public | — |
| `GeoscimlProfile( const GeoscimlProfile&)` | constructor | `None` | protected | — |
| `d_cancel` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_GEOSCIMLPROFILE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/FeatureCollectionFileIO](../app-logic/FeatureCollectionFileIO.md) | app-logic | 3 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 2 |
| [qt-widgets/ConnectWFSDialog](../qt-widgets/ConnectWFSDialog.md) | qt-widgets | 1 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `pd` | `canceled()` | `this` | `cancel()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GeoscimlProfile.h
python scripts/gpq.py def GPlatesFileIO::GeoscimlProfile --body
python scripts/gpq.py uses GeoscimlProfile --kind class
python scripts/gpq.py hier GeoscimlProfile
```

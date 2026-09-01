# GeoscimlProfile

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 986 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GeoscimlProfile.h` | C++ | 84 |
| `src/file-io/GeoscimlProfile.cc` | C++ | 160 |

## Overview

[[[PROSE overview unit=file-io/GeoscimlProfile tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=file-io/GeoscimlProfile tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

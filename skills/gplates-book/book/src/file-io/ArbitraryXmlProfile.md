# ArbitraryXmlProfile

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 986 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ArbitraryXmlProfile.h` | C++ | 67 |

## Overview

[[[PROSE overview unit=file-io/ArbitraryXmlProfile tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ArbitraryXmlProfile`](#gplatesfileioarbitraryxmlprofile) | class | — | — | 1 | — |

## Members

### `GPlatesFileIO::ArbitraryXmlProfile`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `populate( File::Reference&)` | method | `void` | public | — |
| `populate( QByteArray& xml_data, GPlatesModel::FeatureCollectionHandle::weak_ref fch)` | method | `void` | public | — |
| `count_features( QByteArray& xml_data)` | method | `int` | public | — |
| `~ArbitraryXmlProfile()` | destructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_ARBITRARYXMLPROFILE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/ArbitraryXmlProfile tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GsmlPropertyHandlers](GsmlPropertyHandlers.md) | file-io | 14 |
| [file-io/ArbitraryXmlReader](ArbitraryXmlReader.md) | file-io | 13 |
| [file-io/GeoscimlProfile](GeoscimlProfile.md) | file-io | 6 |
| [app-logic/FeatureCollectionFileIO](../app-logic/FeatureCollectionFileIO.md) | app-logic | 3 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ArbitraryXmlProfile.h
python scripts/gpq.py def GPlatesFileIO::ArbitraryXmlProfile --body
python scripts/gpq.py uses ArbitraryXmlProfile --kind class
python scripts/gpq.py hier ArbitraryXmlProfile
```

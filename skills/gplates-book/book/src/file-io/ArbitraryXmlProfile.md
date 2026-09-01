# ArbitraryXmlProfile

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 986 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ArbitraryXmlProfile.h` | C++ | 67 |

## Overview

`ArbitraryXmlProfile` is a small abstract interface for plugging a schema-specific XML parsing strategy into `ArbitraryXmlReader`. It declares no state of its own, only three pure virtual operations: populate a `File::Reference` in place, populate an already-created `FeatureCollectionHandle::weak_ref` from an in-memory `QByteArray` of XML, and count the features a chunk of XML would produce without fully loading it. The one concrete implementation, `GeoscimlProfile`, supplies the GeoSciML-specific logic for turning arbitrary XML documents into GPlates features; `ArbitraryXmlReader` holds a profile through this interface and delegates to it, so the reader itself stays independent of any particular XML vocabulary.

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

*None.*

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

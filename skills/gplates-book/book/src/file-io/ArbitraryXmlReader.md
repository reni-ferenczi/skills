# ArbitraryXmlReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1088 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ArbitraryXmlReader.h` | C++ | 152 |
| `src/file-io/ArbitraryXmlReader.cc` | C++ | 81 |

## Overview

[[[PROSE overview unit=file-io/ArbitraryXmlReader tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ArbitraryXmlReader`](#gplatesfileioarbitraryxmlreader) | class | — | — | 0 | — |

## Members

### `GPlatesFileIO::ArbitraryXmlReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AccessedOutsideXmlProfileMethodException` | class | `None` | public | — |
| `instance()` | method | `ArbitraryXmlReader` | public | TODO: This is not thread-safe. |
| `read_file( File::Reference &file, boost::shared_ptr<ArbitraryXmlProfile> profile, ReadErrorAccumulation &read_errors, bool &contains_unsaved_changes)` | method | `void` | public | — |
| `read_xml_data( File::Reference &file, boost::shared_ptr<ArbitraryXmlProfile> profile, QByteArray& data, ReadErrorAccumulation &read_errors)` | method | `void` | public | — |
| `count_features( boost::shared_ptr<ArbitraryXmlProfile> profile, QByteArray& data, ReadErrorAccumulation &read_errors)` | method | `int` | public | — |
| `get_read_error_accumulation()` | method | `ReadErrorAccumulation` | public | Throws exception if called while not inside read\_file, read\_xml\_data or count\_features. |
| `ArbitraryXmlReader()` | constructor | `None` | private | — |
| `ArbitraryXmlReader( const ArbitraryXmlReader&)` | constructor | `None` | private | — |
| `SetXmlProfileAccess` | class | `None` | private | — |
| `d_read_errors` | field | `ReadErrorAccumulation` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `ACCESSED_OUTSIDE_XML_PROFILE_METHOD_EXCEPTION_NAME` | variable | `char` | — |
| `GPLATES_FILEIO_ARBITRARYXMLREADER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/ArbitraryXmlReader tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 11 |
| [file-io/GsmlPropertyHandlers](GsmlPropertyHandlers.md) | file-io | 11 |
| [app-logic/FeatureCollectionFileIO](../app-logic/FeatureCollectionFileIO.md) | app-logic | 6 |
| [qt-widgets/ConnectWFSDialog](../qt-widgets/ConnectWFSDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ArbitraryXmlReader.h
python scripts/gpq.py def GPlatesFileIO::ArbitraryXmlReader --body
python scripts/gpq.py uses ArbitraryXmlReader --kind class
python scripts/gpq.py hier ArbitraryXmlReader
```

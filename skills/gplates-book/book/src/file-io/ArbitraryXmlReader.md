# ArbitraryXmlReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1088 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ArbitraryXmlReader.h` | C++ | 152 |
| `src/file-io/ArbitraryXmlReader.cc` | C++ | 81 |

## Overview

`ArbitraryXmlReader` is a singleton driver that reads XML into a `FeatureCollectionHandle` by delegating the schema-specific work to an injected `ArbitraryXmlProfile`. Each of its three entry points — `read_file`, `read_xml_data` and `count_features` — installs the caller's `ReadErrorAccumulation` for the duration of the call via the RAII helper `SetXmlProfileAccess`, then calls straight through to the matching `ArbitraryXmlProfile` method; the reader itself never inspects the XML.

The error accumulation is exposed to the profile only while a read is in progress: `get_read_error_accumulation` throws `AccessedOutsideXmlProfileMethodException` if a profile implementation calls it outside that window, which keeps profile code from holding onto a stale accumulator between reads. The `TODO` comment on `instance()` records that the singleton is not thread-safe and that per-thread instances were the intended fix.

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

- `instance()` is a lazily-constructed, non-thread-safe singleton (documented `TODO` in the header) — do not call it concurrently from multiple threads.
- `get_read_error_accumulation()` throws unless called from within `read_file`, `read_xml_data` or `count_features`, since `d_read_errors` is only non-null while `SetXmlProfileAccess` holds it for the duration of one of those calls.

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

# ScribeXmlArchiveWriter

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 383 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeXmlArchiveWriter.h` | C++ | 151 |
| `src/scribe/ScribeXmlArchiveWriter.cc` | C++ | 451 |

## Overview

`XmlArchiveWriter` is the `ArchiveWriter` implementation that serialises a `Transcription` to XML, the write-side counterpart of `XmlArchiveReader`. Like the reader, it wraps a caller-owned `QXmlStreamWriter` instead of a file, so it can be nested inside another XML document.

`write_transcription()` opens the root archive element with the archive signature, XML format version and current `Scribe` version as attributes, then recursively serialises the transcription's `Transcription::CompositeObject` tree with the protected `write()` overloads for each primitive type. As in the reader, all numeric conversions go through a fixed `C_LOCALE` ("C" locale) so the archive is portable across systems with different locale settings. `close()` writes the closing root element; the destructor calls `close()` itself if the caller has not, swallowing any exception since destructors must not propagate them, but a caller that wants write errors to surface should call `close()` explicitly.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::XmlArchiveWriter`](#gplatesscribexmlarchivewriter) | class | [`ArchiveWriter`](ScribeArchiveWriter.md) | — | 0 | XML scribe archiver writer. |

## Members

### `GPlatesScribe::XmlArchiveWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<XmlArchiveWriter>` | public | Convenience typedefs for a shared pointer to a XmlArchiveWriter. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const XmlArchiveWriter>` | public | — |
| `create( QXmlStreamWriter &xml_stream_writer)` | method | `non_null_ptr_type` | public | Create an archive writer that writes to the specified output. |
| `~XmlArchiveWriter()` | destructor | `None` | public | — |
| `write_transcription( const Transcription &transcription)` | method | `void` | public | Writes a Transcription to the archive. |
| `close()` | method | `void` | public | Close the archive. |
| `XmlArchiveWriter( QXmlStreamWriter &xml_stream_writer)` | constructor | `None` | protected | — |
| `write( const Transcription::CompositeObject &composite_object)` | method | `void` | protected | Write Transcription composite object. |
| `write( const Transcription::int32_type object)` | method | `void` | protected | Write Transcription primitives to the archive. |
| `write( const Transcription::uint32_type object)` | method | `void` | protected | — |
| `write( const float object)` | method | `void` | protected | — |
| `write( const double &object)` | method | `void` | protected | — |
| `write( const std::string &object)` | method | `void` | protected | — |
| `C_LOCALE` | field | `QLocale` | protected | Use the "C" locale to convert numbers to and from the archive. |
| `d_output_stream` | field | `QXmlStreamWriter` | protected | Writes the XML data. |
| `d_closed` | field | `bool` | protected | Have we finished writing? |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBEXMLARCHIVEWRITER_H` | macro | `None` | — |

## Notes

- The destructor calls `close()` if it has not already been called, but discards any exception `close()` throws — relying on the destructor to close the archive hides errors that an explicit `close()` call would surface.
- `write_transcription()` can be called multiple times to write several transcriptions into the same archive before `close()`.

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeXmlArchiveWriter.h
python scripts/gpq.py def GPlatesScribe::XmlArchiveWriter --body
python scripts/gpq.py uses XmlArchiveWriter --kind class
python scripts/gpq.py hier XmlArchiveWriter
```

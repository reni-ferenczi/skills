# ScribeXmlArchiveReader

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 409 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeXmlArchiveReader.h` | C++ | 189 |
| `src/scribe/ScribeXmlArchiveReader.cc` | C++ | 664 |

## Overview

`XmlArchiveReader` is the `ArchiveReader` implementation that reconstructs a `Transcription` from XML, the counterpart to `XmlArchiveWriter`. It drives a caller-supplied `QXmlStreamReader` rather than owning its own file or device, so the same reader can sit inside a larger XML document (a project file, a session) that embeds a scribe archive as one element among others.

Construction reads and validates the archive's root element: the archive signature, the XML archive format version and the `Scribe` version that wrote it, rejecting anything from a future, unsupported version via `Exceptions::UnsupportedVersion`. `read_transcription()` then walks the element structure back into a `Transcription::CompositeObject` tree using the protected `read_composite()`/`read_signed()`/`read_unsigned()`/`read_float()`/`read_double()`/`read_string()` primitives, with `read_start_element()`/`read_end_element()` handling the XML tag matching underneath. Numbers are parsed with a fixed `C_LOCALE` ("C" locale) rather than the system locale, so an archive written on one machine's locale reads back correctly on another.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::XmlArchiveReader`](#gplatesscribexmlarchivereader) | class | [`ArchiveReader`](ScribeArchiveReader.md) | — | 0 | XML scribe archiver reader. |

## Members

### `GPlatesScribe::XmlArchiveReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<XmlArchiveReader>` | public | Convenience typedefs for a shared pointer to a XmlArchiveReader. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const XmlArchiveReader>` | public | — |
| `create( QXmlStreamReader &xml_stream_reader)` | method | `non_null_ptr_type` | public | Create an archive reader that reads from the specified input stream. |
| `read_transcription()` | method | `Transcription::non_null_ptr_type` | public | Reads a Transcription from the archive. |
| `close()` | method | `void` | public | Close the archive. |
| `XmlArchiveReader( QXmlStreamReader &xml_stream_reader)` | constructor | `None` | protected | — |
| `read_composite( Transcription::CompositeObject &composite_object)` | method | `void` | protected | Read Transcription composite object. |
| `read_signed()` | method | `int` | protected | Write Transcription primitives to the archive. |
| `read_unsigned()` | method | `unsigned int` | protected | — |
| `read_float()` | method | `float` | protected | — |
| `read_double()` | method | `double` | protected | — |
| `read_string()` | method | `std::string` | protected | — |
| `read_object_id_attribute()` | method | `Transcription::object_id_type` | protected | Read the object id attribute of the current XML element. |
| `read_start_element( const QString &element_name, bool require = false)` | method | `bool` | protected | Read the start of an XML element named element\_name. |
| `read_start_element( const QStringList &element_names, bool require = false)` | method | `bool` | protected | Read the start of an XML element named any names in element\_names. |
| `read_end_element( const QString &element_name, bool require = false)` | method | `bool` | protected | Read the end of an XML element named element\_name. |
| `read_end_element( const QStringList &element_names, bool require = false)` | method | `bool` | protected | Read the end of an XML element named any names in element\_names. |
| `read_next_token()` | method | `void` | protected | A wrapper around QXmlStreamReader::readNext() to detect errors. |
| `C_LOCALE` | field | `QLocale` | protected | Use the "C" locale to convert numbers to and from the archive. |
| `d_input_stream` | field | `QXmlStreamReader` | protected | Reads the XML data. |
| `d_closed` | field | `bool` | protected | Have we finished reading? |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBEXMLARCHIVEREADER_H` | macro | `None` | — |

## Notes

- The `QXmlStreamReader` passed to `create()` must already be positioned at the start of the XML element holding the archived stream; the reader does not seek to it itself.
- `close()` requires the reader to be at the end of the root archive element, so it must only be called after every `Transcription` written to the archive has been read — closing early throws.
- A mismatched or unrecognised archive signature, or an archive/format version newer than this build supports, throws `Exceptions::InvalidArchiveSignature`/`Exceptions::UnsupportedVersion` from the constructor itself, before any transcription is read.

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 11 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeXmlArchiveReader.h
python scripts/gpq.py def GPlatesScribe::XmlArchiveReader --body
python scripts/gpq.py uses XmlArchiveReader --kind class
python scripts/gpq.py hier XmlArchiveReader
```

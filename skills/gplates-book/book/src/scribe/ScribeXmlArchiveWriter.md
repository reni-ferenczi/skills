# ScribeXmlArchiveWriter

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 383 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeXmlArchiveWriter.h` | C++ | 151 |
| `src/scribe/ScribeXmlArchiveWriter.cc` | C++ | 451 |

## Overview

[[[PROSE overview unit=scribe/ScribeXmlArchiveWriter tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=scribe/ScribeXmlArchiveWriter tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

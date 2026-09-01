# ScribeXmlArchiveReader

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 409 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeXmlArchiveReader.h` | C++ | 189 |
| `src/scribe/ScribeXmlArchiveReader.cc` | C++ | 664 |

## Overview

[[[PROSE overview unit=scribe/ScribeXmlArchiveReader tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=scribe/ScribeXmlArchiveReader tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

# ScribeArchiveCommon

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 1724 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeArchiveCommon.h` | C++ | 258 |
| `src/scribe/ScribeArchiveCommon.cc` | C++ | 93 |

## Overview

[[[PROSE overview unit=scribe/ScribeArchiveCommon tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `is_valid_xml_name_start_char( char c)` | function | `bool` | These validation functions are based on http://www.w3.org/TR/REC-xml/#NT-NameChar |
| `is_valid_xml_name_char( char c)` | function | `bool` | — |
| `GPLATES_SCRIBE_SCRIBEARCHIVECOMMON_H` | macro | `None` | — |
| `TEXT_ARCHIVE_SIGNATURE` | variable | `std::string` | The signature string that's written/read to a text archive to ensure it's a GPlates archive. |
| `BINARY_ARCHIVE_SIGNATURE` | variable | `std::string` | The signature string that's written/read to a binary archive to ensure it's a GPlates archive. |
| `XML_ARCHIVE_SIGNATURE` | variable | `std::string` | The signature string that's written/read to a XML archive to ensure it's a GPlates archive. |
| `TEXT_ARCHIVE_FORMAT_VERSION` | variable | `unsigned int` | Version of the \*text\* archive format. |
| `BINARY_ARCHIVE_FORMAT_VERSION` | variable | `unsigned int` | Version of the \*binary\* archive format. |
| `XML_ARCHIVE_FORMAT_VERSION` | variable | `unsigned int` | Version of the \*XML\* archive format. |
| `SIGNED_INTEGER_CODE` | variable | `unsigned int` | Integer codes for the primitive types (and composite type). |
| `UNSIGNED_INTEGER_CODE` | variable | `unsigned int` | — |
| `FLOAT_CODE` | variable | `unsigned int` | — |
| `DOUBLE_CODE` | variable | `unsigned int` | — |
| `STRING_CODE` | variable | `unsigned int` | — |
| `COMPOSITE_CODE` | variable | `unsigned int` | — |
| `XML_SIGNED_OBJECT_ELEMENT_NAME` | variable | `QString` | XML element names for the primitive types (and composite type). |
| `XML_UNSIGNED_OBJECT_ELEMENT_NAME` | variable | `QString` | — |
| `XML_FLOAT_OBJECT_ELEMENT_NAME` | variable | `QString` | — |
| `XML_DOUBLE_OBJECT_ELEMENT_NAME` | variable | `QString` | — |
| `XML_STRING_OBJECT_ELEMENT_NAME` | variable | `QString` | — |
| `XML_COMPOSITE_OBJECT_ELEMENT_NAME` | variable | `QString` | — |
| `XML_OBJECT_ELEMENT_NAMES` | variable | `QStringList` | All the above element names in a list. |
| `BINARY_ARCHIVE_QT_STREAM_VERSION` | variable | `unsigned int` | The QDataStream serialisation version used for binary archives. |
| `BINARY_ARCHIVE_QT_STREAM_BYTE_ORDER` | variable | `QDataStream::ByteOrder` | The QDataStream byte order used for binary archives. |
| `XML_ROOT_ELEMENT_NAME` | variable | `QString` | The name of the root XML element containing the serialization stream. |
| `XML_ARCHIVE_SIGNATURE_ATTRIBUTE_NAME` | variable | `QString` | The name of the XML attribute containing the archive signature. |
| `XML_ARCHIVE_FORMAT_VERSION_ATTRIBUTE_NAME` | variable | `QString` | The name of the XML attribute containing the XML archive format version. |
| `XML_SCRIBE_VERSION_ATTRIBUTE_NAME` | variable | `QString` | The name of the XML attribute containing the archive signature. |
| `XML_TRANSCRIPTION_ELEMENT_NAME` | variable | `QString` | The name of the root XML element containing a transcription stream. |
| `XML_OBJECT_TAG_GROUP_ELEMENT_NAME` | variable | `QString` | The name of the XML element containing the group of object tags. |
| `XML_OBJECT_TAG_ELEMENT_NAME` | variable | `QString` | The name of the XML element containing a single object tag. |
| `XML_STRING_GROUP_ELEMENT_NAME` | variable | `QString` | The name of the XML element containing the group of unique strings. |
| `XML_STRING_ELEMENT_NAME` | variable | `QString` | The name of the XML element containing a single unique string. |
| `XML_OBJECT_GROUP_ELEMENT_NAME` | variable | `QString` | The name of the XML element containing the group of objects. |
| `XML_OBJECT_KEY_ELEMENT_NAME` | variable | `QString` | The name of the XML element containing a single object key. |
| `XML_OBJECT_TAG_ID_ELEMENT_NAME` | variable | `QString` | The name of the XML element containing a single object tag id. |
| `XML_OBJECT_TAG_VERSION_ELEMENT_NAME` | variable | `QString` | The name of the XML element containing a single object tag version. |
| `XML_OBJECT_ID` | variable | `QString` | Used to read/write the object id element name and attribute from/to XML archive. |
| `XML_POSITIVE_INFINITY_VALUE` | variable | `QString` | Used to read/write positive infinity floating-point value from/to XML archive. |
| `XML_NEGATIVE_INFINITY_VALUE` | variable | `QString` | Used to read/write positive infinity floating-point value from/to XML archive. |
| `XML_NAN_VALUE` | variable | `QString` | Used to read/write NaN floating-point value from/to XML archive. |
| `TEXT_POSITIVE_INFINITY_VALUE` | variable | `std::string` | Used to read/write positive infinity floating-point value from/to text archive. |
| `TEXT_NEGATIVE_INFINITY_VALUE` | variable | `std::string` | Used to read/write positive infinity floating-point value from/to text archive. |
| `TEXT_NAN_VALUE` | variable | `std::string` | Used to read/write NaN floating-point value from/to text archive. |
| `get_xml_element_name( std::string xml_element_name, bool validate_all_chars = false)` | function | `QString` | Converts a string to an XML element name and optionally checks XML name validity. |

## Notes

[[[PROSE notes unit=scribe/ScribeArchiveCommon tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/ScribeXmlArchiveReader](ScribeXmlArchiveReader.md) | scribe | 86 |
| [scribe/ScribeXmlArchiveWriter](ScribeXmlArchiveWriter.md) | scribe | 70 |
| [scribe/ScribeTextArchiveReader](ScribeTextArchiveReader.md) | scribe | 30 |
| [scribe/ScribeTextArchiveWriter](ScribeTextArchiveWriter.md) | scribe | 30 |
| [scribe/ScribeBinaryArchiveReader](ScribeBinaryArchiveReader.md) | scribe | 22 |
| [scribe/ScribeBinaryArchiveWriter](ScribeBinaryArchiveWriter.md) | scribe | 22 |
| [scribe/ScribeArchiveReader](ScribeArchiveReader.md) | scribe | 1 |
| [scribe/ScribeArchiveWriter](ScribeArchiveWriter.md) | scribe | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeArchiveCommon.h
```

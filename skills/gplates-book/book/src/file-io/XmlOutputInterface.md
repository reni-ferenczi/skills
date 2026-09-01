# XmlOutputInterface

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 174 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/XmlOutputInterface.h` | C++ | 477 |
| `src/file-io/XmlOutputInterface.cc` | C++ | 274 |

## Overview

[[[PROSE overview unit=file-io/XmlOutputInterface tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::XmlOutputInterface`](#gplatesfileioxmloutputinterface) | class | — | — | 0 | This class provides a convenient interface for XML output. |

## Members

### `GPlatesFileIO::XmlOutputInterface`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Status` | enum | `None` | public | Elements of this enumeration represent the possible status of the interface. |
| `ElementPairStackFrame` | class | `None` | public | This class provides a convenient means to automate the closing of opened elements (and maintain the correct nesting of elements) using a mechanism similar to RAII. |
| `create_for_stdout( const GPlatesUtils::UnicodeString &indentation_unit = "\t")` | method | `XmlOutputInterface` | public | Create a new interface instance which will write to the standard output stream. |
| `create_for_stream( std::ostream &output_stream, const GPlatesUtils::UnicodeString &indentation_unit = "\t")` | method | `XmlOutputInterface` | public | Create a new interface instance which will write to an output stream. |
| `status()` | method | `Status` | public | Return the status of this instance. |
| `set_status( Status new_status)` | method | `void` | public | Set the status of this instance. |
| `write_opening_element( const GPlatesUtils::UnicodeString &elem_name)` | method | `void` | public | Write an opening element. |
| `write_opening_element_with_attributes( const GPlatesUtils::UnicodeString &elem_name, F attrs_pair_begin, F attrs_pair_end)` | method | `void` | public | Write an opening XML element which contains attributes. |
| `write_closing_element( const GPlatesUtils::UnicodeString &elem_name)` | method | `void` | public | Write a closing element. |
| `write_empty_element( const GPlatesUtils::UnicodeString &elem_name)` | method | `void` | public | Write an empty element. |
| `write_line_of_string_content( const GPlatesUtils::UnicodeString &content)` | method | `void` | public | Write a line of string content. |
| `write_line_of_single_integer_content( const long &content)` | method | `void` | public | Write a line of content consisting of a single integer. |
| `write_line_of_single_decimal_content( const double &content)` | method | `void` | public | Write a line of content consisting of a single decimal. |
| `write_line_of_decimal_duple_content( const double &first, const double &second)` | method | `void` | public | Write a line of content consisting of a duple of decimals. |
| `write_line_of_multi_decimal_content( F content_begin, F content_end)` | method | `void` | public | Write a line of content consisting of multiple decimals. |
| `write_line_of_boolean_content( const bool &content)` | method | `void` | public | Write a line of content which is the string version of the boolean value given. |
| `flush_underlying_stream()` | method | `void` | public | Flush the underlying stream. |
| `~XmlOutputInterface()` | destructor | `None` | public | The destructor of XmlOutputInterface flushes the underlying stream but does not close it (since XmlOutputInterface is not responsible for the output stream as a resource). |
| `XmlOutputInterface( std::ostream &os, const GPlatesUtils::UnicodeString &indentation_unit)` | constructor | `None` | protected | — |
| `write_indentation()` | method | `void` | protected | — |
| `write_unicode_string( const GPlatesUtils::UnicodeString &s)` | method | `void` | protected | — |
| `write_attribute_name( const GPlatesModel::XmlAttributeName &xan)` | method | `void` | protected | — |
| `write_attribute_value( const GPlatesModel::XmlAttributeValue &xav)` | method | `void` | protected | — |
| `write_decimal_content( const double &content)` | method | `void` | protected | — |
| `d_os_ptr` | field | `std::ostream` | private | This pointer (rather than its target) can (and should) be copied in copy-constructors and copy-assignment operators. |
| `d_indentation_unit` | field | `GPlatesUtils::UnicodeString` | private | This is the string which is output for indentation of the XML output, once per level of indentation. |
| `d_indentation_level` | field | `unsigned` | private | This is the current indentation level of the XML output. |
| `d_status` | field | `Status` | private | This is the current status of the interface. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `write_xml_header_line(std::ostream *os)` | function | `void` | — |
| `GPLATES_FILEIO_XMLOUTPUTINTERFACE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/XmlOutputInterface tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/deprecated/GpmlOnePointFiveOutputVisitor](deprecated/GpmlOnePointFiveOutputVisitor.md) | file-io | 138 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/XmlOutputInterface.h
python scripts/gpq.py def GPlatesFileIO::XmlOutputInterface --body
python scripts/gpq.py uses XmlOutputInterface --kind class
python scripts/gpq.py hier XmlOutputInterface
```

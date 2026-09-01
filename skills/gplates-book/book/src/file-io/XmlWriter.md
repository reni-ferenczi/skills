# XmlWriter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 381 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/XmlWriter.h` | C++ | 415 |
| `src/file-io/XmlWriter.cc` | C++ | 219 |

## Overview

[[[PROSE overview unit=file-io/XmlWriter tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::XmlWriter`](#gplatesfileioxmlwriter) | class | — | — | 0 | XmlWriter is a wrapper around a QXmlStreamWriter that takes care of ensuring that the namespace aliases emitted in the output are as close as possible to any that were declared in the originating document. |

## Members

### `GPlatesFileIO::XmlWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NamespaceDeclaration` | typedef | `std::pair< GPlatesUtils::StringSet::SharedIterator, GPlatesUtils::StringSet::SharedIterator>` | public | pair::first is the namespace uri, pair::second is the alias. |
| `NamespaceStack` | typedef | `std::vector<NamespaceDeclaration>` | public | — |
| `XmlWriter()` | constructor | `None` | public | Constructs the XmlWriter without specifying a QIODevice. |
| `setDevice( QIODevice *target)` | method | `void` | public | Sets the output device, using QXmlStreamWriter::setDevice(). |
| `device()` | method | `QIODevice` | public | Gets the output device, using QXmlStreamWriter::device(). |
| `XmlWriter( QIODevice *target)` | constructor | `None` | public | Constructs the XmlWriter with a QIODevice target. |
| `writeNamespace( const QString &namespace_uri, const QString &namespace_alias)` | method | `void` | public | — |
| `getAliasForNamespace( const GPlatesUtils::StringSet::SharedIterator namespace_uri)` | method | `GPlatesUtils::UnicodeString` | public | — |
| `writeStartDocument()` | method | `void` | public | — |
| `writeEndDocument()` | method | `void` | public | — |
| `writeEmptyElement( const GPlatesModel::QualifiedXmlName<SingletonType> &elem_name)` | method | `void` | public | — |
| `writeEmptyGpmlElement( const QString &name)` | method | `void` | public | — |
| `writeEmptyGmlElement( const QString &name)` | method | `void` | public | — |
| `writeStartElement( const GPlatesModel::QualifiedXmlName<SingletonType> &elem_name)` | method | `bool` | public | Start a new element with name name. |
| `writeStartGpmlElement( const QString &elem_name)` | method | `void` | public | — |
| `writeStartGmlElement( const QString &elem_name)` | method | `void` | public | — |
| `writeEndElement( bool pop_ns_stack = false)` | method | `void` | public | — |
| `writeText( const QString &text)` | method | `void` | public | — |
| `writeText( const GPlatesUtils::UnicodeString &text)` | method | `void` | public | — |
| `writeText( const GPlatesModel::StringContentTypeGenerator<T> &text)` | method | `void` | public | — |
| `writeDecimal( double val)` | method | `void` | public | — |
| `writeDecimalPair( double val1, double val2)` | method | `void` | public | — |
| `writeCommaSeparatedDecimalPair( double val1, double val2)` | method | `void` | public | — |
| `writeInteger( const IntegerType &val)` | method | `void` | public | — |
| `writeBoolean( bool val)` | method | `void` | public | — |
| `writeNumericalSequence( const DecimalIterator &begin, const DecimalIterator &end)` | method | `void` | public | Dereferencing a DecimalIterator should return an int or double, or something that can be upcast to such. |
| `writeStringSequence( const StringIterator &begin, const StringIterator &end)` | method | `void` | public | Dereferencing a StringIterator should return a QString, or something that can be upcast to such. |
| `writeAttribute( const QString &namespace_uri, const QString &name, const QString &value)` | method | `void` | public | — |
| `writeAttribute( const GPlatesModel::QualifiedXmlName<SingletonType> &name, const QString &value)` | method | `void` | public | — |
| `writeAttributes( const AttributeIterator &begin, const AttributeIterator &end)` | method | `void` | public | Dereferencing an AttributeIterator should return a pair consisting of a QualifiedXmlName and an XmlAttributeValue. |
| `writeGpmlAttribute( const QString &name, const QString &value)` | method | `void` | public | — |
| `writeGmlAttribute( const QString &name, const QString &value)` | method | `void` | public | — |
| `writeRelativeFilePath( const QString &absolute_file_path)` | method | `void` | public | Writes the absolute\_file\_path as a path relative to the directory that contains the file that we are outputting XML to (if any). |
| `writeRelativeFilePath( const GPlatesUtils::UnicodeString &absolute_file_path)` | method | `void` | public | — |
| `d_ns_stack` | field | `NamespaceStack` | private | — |
| `d_writer` | field | `QXmlStreamWriter` | private | — |
| `declare_namespace_if_necessary( const NamespaceDeclaration &ns_decl)` | method | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `compare_ns_decls( const GPlatesFileIO::XmlWriter::NamespaceDeclaration &ns_decl_1, const GPlatesFileIO::XmlWriter::NamespaceDeclaration &ns_decl_2)` | function | `bool` | — |
| `compare_ns_and_decl( const GPlatesUtils::StringSet::SharedIterator &namespace_uri, const GPlatesFileIO::XmlWriter::NamespaceDeclaration &ns_decl)` | function | `bool` | — |
| `compare_aliases( const GPlatesUtils::StringSet::SharedIterator &namespace_alias, const GPlatesFileIO::XmlWriter::NamespaceDeclaration &ns_decl)` | function | `bool` | — |
| `GPLATES_FILEIO_XMLWRITER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/XmlWriter tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlOutputVisitor](GpmlOutputVisitor.md) | file-io | 402 |
| [model/Metadata](../model/Metadata.md) | model | 41 |
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 10 |
| [model/XmlNode](../model/XmlNode.md) | model | 5 |
| [file-io/MipmappedRasterFormatWriter](MipmappedRasterFormatWriter.md) | file-io | 4 |
| [file-io/ShapefileXmlWriter](ShapefileXmlWriter.md) | file-io | 3 |
| [property-values/GpmlMetadata](../property-values/GpmlMetadata.md) | property-values | 3 |
| [file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport](CitcomsGMTFormatResolvedTopologicalBoundaryExport.md) | file-io | 2 |
| [file-io/GpmlReader](GpmlReader.md) | file-io | 2 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 1 |
| [file-io/GdalRasterReader](GdalRasterReader.md) | file-io | 1 |
| [file-io/RgbaRasterReader](RgbaRasterReader.md) | file-io | 1 |
| [file-io/ShapefileXmlReader](ShapefileXmlReader.md) | file-io | 1 |
| [gui/FeedbackOpenGLToQPainter](../gui/FeedbackOpenGLToQPainter.md) | gui | 1 |
| [gui/VelocityLegendOverlay](../gui/VelocityLegendOverlay.md) | gui | 1 |
| [model/Gpgim](../model/Gpgim.md) | model | 1 |
| [opengl/GLRenderer](../opengl/GLRenderer.md) | opengl | 1 |
| [opengl/GLText](../opengl/GLText.md) | opengl | 1 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/XmlWriter.h
python scripts/gpq.py def GPlatesFileIO::XmlWriter --body
python scripts/gpq.py uses XmlWriter --kind class
python scripts/gpq.py hier XmlWriter
```

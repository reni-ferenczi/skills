# XmlWriter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 381 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/XmlWriter.h` | C++ | 415 |
| `src/file-io/XmlWriter.cc` | C++ | 219 |

## Overview

This is the output half of the native GPML pipeline: a thin façade over a
`QXmlStreamWriter` member, plus one piece of real logic. That logic is namespace
prefix continuity. A `GPlatesModel::QualifiedXmlName` carries three
`GPlatesUtils::StringSet::SharedIterator`s — namespace URI, namespace alias and
local name — and the alias is whatever prefix the *originating* document used
(the reader stores it; `set_namespace_alias()` falls back to
`GPlatesUtils::XmlNamespaces::get_standard_alias_for_namespace` only when the
file did not say). `QXmlStreamWriter` on its own would invent prefixes (`n1`,
`n2`, …) for any namespace it has not been told about, so a round trip through
GPlates would silently rewrite every prefix in the file. `XmlWriter` keeps its
own `NamespaceStack` of (URI, alias) pairs and re-emits declarations so the
output keeps the document's own spelling. Everything else on the class —
`writeDecimal`, `writeNumericalSequence`, the `*GpmlElement` / `*GmlElement`
shortcuts — is convenience formatting layered on the same `QXmlStreamWriter`.

The mechanism has two directions. Downwards, `writeStartElement` calls the
private `declare_namespace_if_necessary`, which walks the stack from the top and
emits a fresh `xmlns` declaration in three cases: the URI has not been declared
at all, it was declared under a *different* alias, or it was declared under this
alias but a nearer declaration has since rebound that alias to something else
(the `compare_aliases` search bounded by the first hit). It returns whether it
declared anything, and that `bool` is the value the caller is expected to thread
back into `writeEndElement` — this is why the two calls are paired by a local
`pop` variable throughout `GpmlOutputVisitor`. Upwards, `getAliasForNamespace`
answers "what prefix is currently in scope for this URI", which Qt cannot
answer: `QXmlStreamWriter` exposes no read access to the declarations it is
holding. That matters because GPML puts qualified names inside *character data*
— a `gml:ValueType` element's text is literally `gpml:something` — so
`GpmlOutputVisitor::writeTemplateTypeParameterType` has to build the prefix by
hand from this stack.

In practice `XmlWriter` has one serious client. `GpmlOutputVisitor` holds one by
value, points it at either the plain `QFile` or the `GzipFile` chosen for
`.gpml` versus `.gpmlz`, and drives every element of the document through it;
the remaining callers use a handful of the formatting helpers or, in the case of
`GPlatesModel::FeatureCollectionMetadata::serialize`, reach past the class
entirely via `get_writer()`. Note that the `writeStartGpmlElement` /
`writeStartGmlElement` / `writeGpmlAttribute` family does *not* consult the
namespace stack at all — those hand the fixed URIs from
`GPlatesUtils::XmlNamespaces` straight to `QXmlStreamWriter`, and are correct
only because `GpmlOutputVisitor::start_writing_document` declares gpml, gml and
xsi with their standard aliases before the root element.

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

**The namespace stack is only half-maintained.** `writeNamespace` pushes;
`declare_namespace_if_necessary` emits an `xmlns` declaration but *does not*
push. So `d_ns_stack` records what callers explicitly declared, not what the
writer actually emitted — a second element in a not-yet-stacked namespace will
be re-declared, and `writeEndElement(true)` pops an entry that
`writeStartElement` never pushed, discarding an older, unrelated declaration.
For ordinary GPML output the path is not reached: gpml, gml and xsi are on the
stack with their standard aliases before the root element, so
`writeStartElement` returns `false` and every `pop` in `GpmlOutputVisitor` is
`false`. Anything that does trip it also writes `"Popping namespace stack."` to
`std::cout` unconditionally — an "XXX: temporary" debug line still in the 2.5
source — and, on an empty stack, writes to `std::cerr` instead of throwing (the
`FIXME` is unresolved). In a headless or pyGPlates run that is stdout
pollution, not a log message.

**Bypassing the class breaks its only invariant.** `get_writer()` hands out the
raw `QXmlStreamWriter`, and `FeatureCollectionMetadata::serialize` uses it to
write literal `"gpml:"`-prefixed element names and its own `writeNamespace`.
After that, `d_ns_stack` no longer describes what is in scope in the document.
Treat `get_writer()` as an escape hatch, not an extension point.

**Device ownership is entirely the caller's.** `XmlWriter` never opens, closes
or deletes the `QIODevice`, and it does not check that one was set — the
default constructor exists only so `GpmlOutputVisitor` can construct the member
before it has decided between a `QFile` and a `GzipFile`, and writing before
`setDevice()` is undefined rather than diagnosed. `GpmlOutputVisitor` declares
`d_output` *after* its file members precisely so the writer is destroyed first.
Because `QXmlStreamWriter` is non-copyable, so is `XmlWriter`; it is always
passed by reference.

**There is no error reporting.** Neither device write failures nor
`QXmlStreamWriter::hasError()` are surfaced anywhere on this class, so a
truncated or failed save is silent from here. `GpmlOutputVisitor` closes the
root element and the document from its *destructor*, inside a catch-all, which
compounds this: a failure at end-of-document has nowhere to go.

**Formatting details that are load-bearing for the file format.**
`writeDecimal` uses `QString::number(val, 'g', 17)` — 17 significant digits,
enough to round-trip an IEEE double exactly; changing it changes every
coordinate in every file GPlates has ever written. `writeNumericalSequence` and
`writeStringSequence` append the separator *after* every item including the
last, so `gml:posList` and `gml:tupleList` content always ends in a trailing
space and readers must tolerate it. Auto-formatting is switched on in both
constructors and is not exposed as an option, so output is always indented —
byte-for-byte comparisons against reference files are formatting-sensitive.

**A missing declaration degrades silently.** `getAliasForNamespace` returns the
namespace URI itself when the URI is not on the stack, so the caller writes the
whole URI where a prefix belongs (`http://www.gplates.org/gplates:something`)
rather than failing. Stack lookups are linear `std::find_if` scans, which is
fine only because the stack holds a handful of entries; the comparisons
themselves are cheap `SharedIterator` identity checks, and holding those
iterators also keeps the strings alive in the
`GPlatesModel::StringSetSingletons` namespace sets.

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

# QualifiedXmlName

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 567 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/QualifiedXmlName.h` | C++ | 461 |

## Overview

Every name that GPlates reads out of a GPML, GML or GPGIM document — feature types,
property names, structural types, XML element and attribute names — is one of these. A
`QualifiedXmlName` is three `GPlatesUtils::StringSet::SharedIterator`s: the namespace URI,
the namespace alias, and the local name. The strings themselves live once each in
process-wide `StringSet` pools, so a document with a hundred thousand
`gpml:reconstructionPlateId` properties holds one copy of that text and a hundred thousand
iterator triples. Comparing two names for equality is then a pair of iterator comparisons
rather than a character-by-character string compare, which is what makes it cheap to key
`std::map`s and to switch on property names in the visitors and readers.

The `SingletonType` template parameter is a tag class whose only job is a static
`instance()` returning the `StringSet` that this kind of name is interned in. There are
seven instantiations in the tree — `PropertyName`, `FeatureType`, `XmlAttributeName`,
`XmlElementName` in `model`, and `StructuralType`, `EnumerationType`, `ValueObjectType` in
`property-values` — each with its own pool, so names of different kinds cannot be confused
even when their text is identical. The namespace and alias pools, by contrast, are shared
by all instantiations (`StringSetSingletons::xml_namespace_instance()` and
`xml_namespace_alias_instance()`), which is why namespace iterators can be handed straight
from one instantiation to another.

The named constructors bind the four namespaces that `GPlatesUtils::XmlNamespaces` knows
about; the constructors that take only a URI derive the alias from it with
`XmlNamespaces::get_standard_alias_for_namespace`. The `GPlatesUtils::Parse`
specialisation at the bottom of the header lets generic string-to-value code (widget
input, command-line arguments) produce these names, and the two `transcribe` members hook
them into `GPlatesScribe` for session and project files — deliberately declared here and
defined in `TranscribeQualifiedXmlName.h` so that this very widely included header does
not drag in `Scribe.h`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::QualifiedXmlName`](#gplatesmodelqualifiedxmlname) | class | `boost::less_than_comparable<QualifiedXmlName<SingletonType>, boost::equality_comparable<QualifiedXmlName<SingletonType> > >` | `<typename SingletonType>` | 0 | This class provides an efficient means of containing the qualifed name of an element or attribute occuring in an XML document Since many elements and attributes share the same name, this class minimises memory usage for the storage of all ... |
| [`GPlatesUtils::Parse<GPlatesModel::QualifiedXmlName<SingletonType> >`](#gplatesutilsparsegplatesmodelqualifiedxmlnamesingletontype-) | struct | — | `<typename SingletonType>` | 0 | Specialisation of Parse for the QualifiedXmlName. |

## Members

### `GPlatesModel::QualifiedXmlName`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create_gpgim( const QString &name)` | method | `QualifiedXmlName` | public | NOTE: The GPGIM namespace is not part of the feature readers but is placed here in order to re-use a lot of the XML parsing machinery when reading the GPGIM XML file. |
| `create_gpgim( const QString &namespace_alias, const QString &name)` | method | `QualifiedXmlName` | public | NOTE: The GPGIM namespace is not part of the feature readers but is placed here in order to re-use a lot of the XML parsing machinery when reading the GPGIM XML file. |
| `create_gpml( const QString &name)` | method | `QualifiedXmlName` | public | — |
| `create_gpml( const QString &namespace_alias, const QString &name)` | method | `QualifiedXmlName` | public | — |
| `create_gml( const QString &name)` | method | `QualifiedXmlName` | public | — |
| `create_gml( const QString &namespace_alias, const QString &name)` | method | `QualifiedXmlName` | public | — |
| `create_xsi( const QString &name)` | method | `QualifiedXmlName` | public | — |
| `QualifiedXmlName( const QualifiedXmlName<U> &other)` | constructor | `None` | public | Constructor for when other QualifiedXmlName\<U\> type is different to 'this'. |
| `QualifiedXmlName( const QualifiedXmlName &other)` | constructor | `None` | public | Copy constructor for when other type is same as 'this'. |
| `QualifiedXmlName( const QString &namespace_uri, const QString &name)` | constructor | `None` | public | Instantiate a new QualifiedXmlName instance for the given namespace and name. |
| `QualifiedXmlName( const GPlatesUtils::UnicodeString &namespace_uri, const GPlatesUtils::UnicodeString &name)` | constructor | `None` | public | — |
| `QualifiedXmlName( const QString &namespace_uri, const QString &namespace_alias, const QString &name)` | constructor | `None` | public | Instantiate a new QualifiedXmlName instance for the given namespace, alias and name. |
| `QualifiedXmlName( const GPlatesUtils::UnicodeString &namespace_uri, boost::optional<const GPlatesUtils::UnicodeString &> namespace_alias, const GPlatesUtils::UnicodeString &name)` | constructor | `None` | public | — |
| `get_namespace_iterator()` | method | `GPlatesUtils::StringSet::SharedIterator` | public | Access the underlying StringSet iterator of the namespace. |
| `get_namespace_alias_iterator()` | method | `GPlatesUtils::StringSet::SharedIterator` | public | Access the underlying StringSet iterator of the namespace alias for this instance. |
| `build_aliased_name()` | method | `GPlatesUtils::UnicodeString` | public | Return a copy of this qualified name in the form of a string "alias:name" where alias is the result of get\_namespace\_alias() and name is the result of get\_name(). |
| `is_equal_to( const QualifiedXmlName<SingletonType> &other)` | method | `bool` | public | Determine whether another QualifiedXmlName instance contains the same qualified name as this instance. |
| `operator==( const QualifiedXmlName &other)` | operator | `bool` | public | Equality comparison operator - inequality operator provided by 'boost::equality\_comparable'. |
| `operator<( const QualifiedXmlName &other)` | operator | `bool` | public | Less-than operator - provided so QualifiedXmlName can be used as a key in std::map. |
| `d_namespace` | field | `GPlatesUtils::StringSet::SharedIterator` | private | — |
| `d_namespace_alias` | field | `GPlatesUtils::StringSet::SharedIterator` | private | — |
| `d_name` | field | `GPlatesUtils::StringSet::SharedIterator` | private | — |
| `set_namespace_alias()` | method | `void` | private | — |
| `transcribe_construct_data( GPlatesScribe::Scribe &scribe, GPlatesScribe::ConstructObject< QualifiedXmlName<SingletonType> > &qualified_xml_name)` | method | `GPlatesScribe::TranscribeResult` | private | NOTE: Implementation is in "TranscribeQualifiedXmlName.h" to avoid including "Scribe.h" here. |
| `transcribe( GPlatesScribe::Scribe &scribe, bool transcribed_construct_data)` | method | `GPlatesScribe::TranscribeResult` | private | NOTE: Implementation is in "TranscribeQualifiedXmlName.h" to avoid including "Scribe.h" here. |

### `GPlatesUtils::Parse<GPlatesModel::QualifiedXmlName<SingletonType> >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `qualified_xml_name_type` | typedef | `GPlatesModel::QualifiedXmlName<SingletonType>` | public | — |
| `operator()( const QString &s)` | operator | `qualified_xml_name_type` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_QUALIFIEDXMLNAME_H` | macro | `None` | — |
| `convert_qualified_xml_name_to_qstring( const QualifiedXmlNameType &qualified_xml_name)` | function | `QString` | Convenience function to convert a QualifiedXmlName to a QString as: "\<namespace\_alias\>:\<name\>". |
| `convert_qstring_to_qualified_xml_name( const QString &qualified_string)` | function | `boost::optional<QualifiedXmlNameType>` | Converts a QString, represented as "\<namespace\_alias\>:\<name\>", to a QualifiedXmlName. |

## Notes

- **The alias is not part of identity.** `is_equal_to` compares the local name and the
  namespace URI only, so two names that differ purely in their alias are equal. `operator<`
  orders on (namespace URI, local name) to match, and takes the fast iterator-comparison
  path only when both namespace iterators are already identical; when they are not it
  falls back to a full ICU comparison of the two URI strings. The header explains why the
  short alias cannot be substituted there.
- **Construction is the expensive operation.** Every constructor inserts into a
  `std::set`, at O(L log N) in the length of the string. Equality afterwards is O(1). The
  idiomatic response, used throughout `property-values` in `get_structural_type()`, is to
  hoist a repeatedly used name into a function-scope `static`.
- **The cross-type constructor re-interns.** `QualifiedXmlName(const QualifiedXmlName<U>&)`
  is `explicit` and calls `SingletonType::instance().insert(other.get_name())`; only the
  namespace and alias iterators are shared. It is a conversion with a set insertion in it,
  not a reinterpretation.
- **`build_aliased_name()` throws away the benefit.** It, and
  `convert_qualified_xml_name_to_qstring()`, materialise a new string on every call. Do not
  put them inside a loop over features or properties, and never use them to compare names.
- **`convert_qstring_to_qualified_xml_name()` almost never fails.** It returns
  `boost::none` only when the string does not split into one or two colon-separated
  tokens. An unrecognised prefix is not an error: `XmlNamespaces::get_namespace_for_standard_alias`
  falls back to the gpml namespace, so a typo'd or unknown prefix silently yields a gpml
  name. Only the `GPlatesUtils::Parse` specialisation turns the `boost::none` case into a
  `ParseError`.
- **Lifetime and threading.** A pool entry survives exactly as long as some
  `SharedIterator` references it, so the three iterators a name holds keep its strings
  alive; a name is safe to copy and store anywhere. The pools themselves are
  `GPlatesUtils::Singleton`s, and that template compiles its mutex only when
  `GPLATES_SINGLETON_THREADSAFE` is defined, which nothing in this tree does — constructing
  qualified names concurrently on several threads is a data race on the shared `std::set`.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/deprecated/FeaturePropertiesMap](../file-io/deprecated/FeaturePropertiesMap.md) | file-io | 280 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 131 |
| [model/Gpgim](Gpgim.md) | model | 116 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 114 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 103 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 61 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 60 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 53 |
| [model/XmlNode](XmlNode.md) | model | 52 |
| [file-io/XmlWriter](../file-io/XmlWriter.md) | file-io | 50 |
| [app-logic/ReconstructionGeometryUtils](../app-logic/ReconstructionGeometryUtils.md) | app-logic | 48 |
| [model/FeatureVisitor](FeatureVisitor.md) | model | 44 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 32 |
| [model/ModelUtils](ModelUtils.md) | model | 29 |
| [qt-widgets/EditWidgetGroupBox](../qt-widgets/EditWidgetGroupBox.md) | qt-widgets | 23 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 20 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 20 |
| [file-io/PlatesLineFormatHeaderVisitor](../file-io/PlatesLineFormatHeaderVisitor.md) | file-io | 20 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 18 |
| [file-io/XmlOutputInterface](../file-io/XmlOutputInterface.md) | file-io | 18 |

*... and 165 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/QualifiedXmlName.h
python scripts/gpq.py def GPlatesModel::QualifiedXmlName --body
python scripts/gpq.py uses QualifiedXmlName --kind class
python scripts/gpq.py hier QualifiedXmlName
```

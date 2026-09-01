# Gpgim

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 128 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/Gpgim.h` | C++ | 625 |
| `src/model/Gpgim.cc` | C++ | 1992 |

## Overview

GPlates does not hard-code its schema. What feature types exist, which
properties each may carry, what structural types those property values may take,
which properties are geometry, and which may be wrapped in a time-dependent
wrapper is all declared in `gpgim.xml`, compiled into the executable as the Qt
resource `:/gpgim/gpgim.xml`. This class is the parser and the query point for
that file. On construction it reads the document once and turns it into
`GpgimStructuralType`, `GpgimTemplateStructuralType`, `GpgimEnumerationType`,
`GpgimProperty` and `GpgimFeatureClass` objects, together with the lookup maps
that answer the questions the rest of GPlates asks by name. It is a
`GPlatesUtils::Singleton`, so all of that happens on the first
`Gpgim::instance()` call and there is exactly one copy of the model definition
in the process.

The three big consumers are the GPML reader, the create/edit dialogs, and
`ModelUtils`. `GpmlFeatureReaderFactory` builds a reader per feature type from
the feature class and its properties, so the parser knows what to expect rather
than guessing from the XML it is handed. `CreateFeatureDialog`,
`AddPropertyDialog`, `ChoosePropertyWidget` and friends populate their lists
straight from `get_concrete_feature_types` and the feature class's properties —
abstract classes such as `gpml:TangibleFeature` are excluded from that list
precisely because they are never instantiated. `ModelUtils` uses
`get_property_template_structural_type` when it needs to instantiate a template
type such as `gpml:Array<gml:TimePeriod>`. `GpmlOutputVisitor` stamps
`get_version()` onto every file it writes, and `GpmlReader` warns when it reads a
file whose GPGIM version is newer than this build's.

Loading proceeds in dependency order, and the code says so: structural types
first, then properties (which reference structural types), then feature classes
(which reference properties). Feature classes are the awkward step, because a
class may inherit from one defined later in the file. The loader therefore reads
all feature class elements into a temporary feature-type-to-XML-element map
first, then walks the inheritance chain on demand — `create_feature_class` calls
`create_feature_class_if_necessary` for its parent before building itself, so
the XML file's ordering does not matter. `gpml:UnclassifiedFeature` is
synthesised at the end rather than declared: it clones every property in the
GPGIM with the multiplicity forced to `ZERO_OR_MORE`, which the comment defends
as preferable to scattering special cases through the application.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::Gpgim`](#gplatesmodelgpgim) | class | [`GPlatesUtils::Singleton<Gpgim>`](../utils/Singleton.md) | — | 0 | The GPlates Geological Information Model (GPGIM) main query point. |

## Members

### `GPlatesModel::Gpgim`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<Gpgim>` | public | A convenience typedef for a shared pointer to a non-const Gpgim. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const Gpgim>` | public | A convenience typedef for a shared pointer to a const Gpgim. |
| `feature_type_seq_type` | typedef | `std::vector<FeatureType>` | public | Typedef for a sequence of feature types. |
| `property_structural_type_seq_type` | typedef | `std::vector<GpgimStructuralType::non_null_ptr_to_const_type>` | public | Typedef for a sequence of property structural types. |
| `property_template_structural_type_seq_type` | typedef | `std::vector<GpgimTemplateStructuralType::non_null_ptr_to_const_type>` | public | Typedef for a sequence of property \*template\* structural types (instantiations). |
| `property_enumeration_type_seq_type` | typedef | `std::vector<GpgimEnumerationType::non_null_ptr_to_const_type>` | public | Typedef for a sequence of property enumeration (structural) types. |
| `property_seq_type` | typedef | `std::vector<GpgimProperty::non_null_ptr_to_const_type>` | public | Typedef for a sequence of properties. |
| `get_version` | field | `GpgimVersion` | public | Returns the GPGIM version. |
| `get_feature_class( const FeatureType &feature_type)` | method | `boost::optional<GpgimFeatureClass::non_null_ptr_to_const_type>` | public | Returns the feature class associated with the specified feature type. |
| `get_feature_property( const FeatureType &feature_type, const PropertyName &property_name)` | method | `boost::optional<GpgimProperty::non_null_ptr_to_const_type>` | public | Convenience method returns the GPGIM property of the specified property name in the specified feature type. |
| `get_feature_properties( const FeatureType &feature_type, const GPlatesPropertyValues::StructuralType &property_type, boost::optional<property_seq_type &> feature_properties = boost::none)` | method | `bool` | public | Convenience method returns the GPGIM property(s) of the specified property type in the specified feature type. |
| `get_property( const PropertyName &property_name)` | method | `boost::optional<GpgimProperty::non_null_ptr_to_const_type>` | public | Returns the property associated with the specified property name. |
| `get_property_structural_type( const GPlatesPropertyValues::StructuralType &structural_type)` | method | `boost::optional<GpgimStructuralType::non_null_ptr_to_const_type>` | public | Returns the property structural type associated with the specified structural type. |
| `get_property_template_structural_type( const GPlatesPropertyValues::StructuralType &structural_type, const GPlatesPropertyValues::StructuralType &value_type)` | method | `boost::optional<GpgimTemplateStructuralType::non_null_ptr_to_const_type>` | public | Returns the property \*template\* structural type associated with the specified structural type and value type (template parameter). |
| `get_property_enumeration_type( const GPlatesPropertyValues::StructuralType &structural_type)` | method | `boost::optional<GpgimEnumerationType::non_null_ptr_to_const_type>` | public | Returns the property enumeration (structural) type associated with the specified structural type. |
| `CORE_GPGIM_RESOURCE_FILENAME` | field | `QString` | private | The filename for the 'core' GPGIM resource XML file. |
| `feature_class_xml_element_node_map_type` | typedef | `std::map<FeatureType, XmlElementNode::non_null_ptr_type>` | private | Typedef for mapping from feature type to associated feature class XML element nodes. |
| `feature_class_map_type` | typedef | `std::map<FeatureType, GpgimFeatureClass::non_null_ptr_to_const_type>` | private | Typedef for a map of feature type to feature class. |
| `property_structural_type_map_type` | typedef | `std::map< GPlatesPropertyValues::StructuralType, GpgimStructuralType::non_null_ptr_to_const_type>` | private | Typedef for a map of structural type to GPGIM structural type. |
| `property_template_structural_type_map_type` | typedef | `std::map< boost::tuple<GPlatesPropertyValues::StructuralType, GPlatesPropertyValues::StructuralType/*value type*/>, GpgimTemplateStructuralType::non_null_ptr_to_const_type>` | private | Typedef for a map of \*template\* structural type to GPGIM structural type. |
| `property_enumeration_type_map_type` | typedef | `std::map< GPlatesPropertyValues::StructuralType, GpgimEnumerationType::non_null_ptr_to_const_type>` | private | Typedef for a map of enumeration (structural) type to GPGIM structural type. |
| `property_map_type` | typedef | `std::map< PropertyName, GpgimProperty::non_null_ptr_to_const_type>` | private | Typedef for a map of property name to GPGIM property. |
| `d_version` | field | `boost::optional<GpgimVersion>` | private | The GPGIM version. |
| `d_property_structural_types` | field | `property_structural_type_seq_type` | private | The list of all supported property structural types. |
| `d_property_structural_type_map` | field | `property_structural_type_map_type` | private | Used to retrieve GPGIM structural type from structural type. |
| `d_geometry_property_structural_types` | field | `property_structural_type_seq_type` | private | The list of all supported \*geometry\* property structural types. |
| `d_property_template_structural_types` | field | `property_template_structural_type_seq_type` | private | The list of all supported property \*template\* structural types (instantiations). |
| `d_property_template_structural_type_map` | field | `property_template_structural_type_map_type` | private | Used to retrieve GPGIM \*template\* structural type from a structural type and value type. |
| `d_property_enumeration_types` | field | `property_enumeration_type_seq_type` | private | The list of all supported property \*enumeration\* types. |
| `d_property_enumeration_type_map` | field | `property_enumeration_type_map_type` | private | Used to retrieve GPGIM enumeration (structural) type from structural type. |
| `d_properties` | field | `property_seq_type` | private | The list of all supported properties. |
| `d_property_map` | field | `property_map_type` | private | Used to retrieve GPGIM property from property name. |
| `d_geometry_properties` | field | `property_seq_type` | private | The list of all supported \*geometry\* properties. |
| `d_feature_class_map` | field | `feature_class_map_type` | private | Used to retrieve feature class from feature type. |
| `d_concrete_feature_types` | field | `feature_type_seq_type` | private | Those subset of feature types that are concrete (not abstract). |
| `load_gpgim_resource( const QString &gpgim_resource_filename)` | method | `void` | private | Loads a GPGIM resource XML file. |
| `read_gpgim_element( boost::optional<XmlElementNode::non_null_ptr_type> &property_type_list_xml_element, boost::optional<XmlElementNode::non_null_ptr_type> &property_list_xml_element, boost::optional<XmlElementNode::non_null_ptr_type> &feature_class_list_xml_element, QXmlStreamReader &xml_reader, const QString &gpgim_re ...` | method | `GpgimVersion` | private | Reads the root 'gpgim:GPGIM' element in the GPGIM XML document and returns the GPGIM version. |
| `create_property_structural_types( const XmlElementNode::non_null_ptr_type &property_type_list_xml_element, const QString &gpgim_resource_filename)` | method | `void` | private | Compiles the property structural type definitions from their respective XML element nodes. |
| `create_property_structural_type( const XmlElementNode::non_null_ptr_type &property_type_xml_element, bool is_enumeration, const QString &gpgim_resource_filename)` | method | `GpgimStructuralType::non_null_ptr_to_const_type` | private | Compiles a property structural type from the specified XML element node. |
| `create_properties( const XmlElementNode::non_null_ptr_type &property_list_xml_element, const QString &gpgim_resource_filename)` | method | `void` | private | Create the GPGIM feature properties listed in (children of) the specified XML element node. |
| `create_property( const XmlElementNode::non_null_ptr_type &property_xml_element, const QString &gpgim_resource_filename)` | method | `GpgimProperty::non_null_ptr_type` | private | Create the GPGIM feature property associated with the specified XML element node. |
| `read_feature_property_name( const XmlElementNode::non_null_ptr_type &property_xml_element, const QString &gpgim_resource_filename)` | method | `PropertyName` | private | Reads the feature property name from the specified property XML element. |
| `read_feature_property_user_friendly_name( const XmlElementNode::non_null_ptr_type &property_xml_element, const PropertyName &property_name, const QString &gpgim_resource_filename)` | method | `QString` | private | Reads the feature property user-friendly name from the specified property XML element. |
| `read_feature_property_description( const XmlElementNode::non_null_ptr_type &property_xml_element, const QString &gpgim_resource_filename)` | method | `QString` | private | Reads the feature property description from the specified property XML element. |
| `read_feature_property_multiplicity( const XmlElementNode::non_null_ptr_type &property_xml_element, const QString &gpgim_resource_filename)` | method | `GpgimProperty::MultiplicityType` | private | Reads the feature property multiplicity from the specified property XML element. |
| `read_feature_property_structural_types( GpgimProperty::structural_type_seq_type &gpgim_property_structural_types, const XmlElementNode::non_null_ptr_type &property_xml_element, const QString &gpgim_resource_filename)` | method | `unsigned int` | private | Reads the feature property structural types from the specified property XML element. |
| `read_feature_property_non_template_structural_type( GpgimProperty::structural_type_seq_type &gpgim_property_structural_types, const XmlElementNode::non_null_ptr_type &property_type_element, const QString &gpgim_resource_filename)` | method | `GpgimStructuralType::non_null_ptr_to_const_type` | private | Reads the non-template structural type from the specified property type XML element. |
| `read_feature_property_template_structural_type( GpgimProperty::structural_type_seq_type &gpgim_property_structural_types, const XmlElementNode::non_null_ptr_type &property_template_type_element, const QString &gpgim_resource_filename)` | method | `GpgimTemplateStructuralType::non_null_ptr_to_const_type` | private | Reads the template structural type from the specified property type XML element. |
| `read_default_feature_property_structural_type( const XmlElementNode::non_null_ptr_type &property_xml_element, const QString &gpgim_resource_filename)` | method | `GPlatesPropertyValues::StructuralType` | private | Reads the default feature property structural type as an attribute of the specified property XML element. |
| `read_feature_property_time_dependent_types( const XmlElementNode::non_null_ptr_type &property_xml_element, const QString &gpgim_resource_filename)` | method | `GpgimProperty::time_dependent_flags_type` | private | Reads the feature property time-dependent types from the specified property XML element. |
| `read_feature_class_default_geometry_property_name( const XmlElementNode::non_null_ptr_type &feature_class_xml_element, const QString &gpgim_resource_filename)` | method | `boost::optional<GPlatesModel::PropertyName>` | private | — |
| `read_feature_class_xml_elements( feature_class_xml_element_node_map_type &feature_class_xml_element_node_map, const XmlElementNode::non_null_ptr_type &feature_class_list_xml_element, const QString &gpgim_resource_filename)` | method | `void` | private | Reads the GPGIM feature class definitions in the GPGIM XML document. |
| `create_feature_classes( const feature_class_xml_element_node_map_type &feature_class_xml_element_node_map, const QString &gpgim_resource_filename)` | method | `void` | private | Compiles the feature class definitions from their respective XML element nodes. |
| `create_unclassified_feature_class( const QString &gpgim_resource_filename)` | method | `GpgimFeatureClass::non_null_ptr_to_const_type` | private | Creates the special-case feature class 'gpml:UnclassifiedFeature'. |
| `create_feature_class_if_necessary( const FeatureType &feature_type, const XmlElementNode::non_null_ptr_type &feature_class_reference_xml_element, const feature_class_xml_element_node_map_type &feature_class_xml_element_node_map, const QString &gpgim_resource_filename)` | method | `GpgimFeatureClass::non_null_ptr_to_const_type` | private | Compiles a feature class definition from the specified XML element node, if it hasn't already been. |
| `create_feature_class( const FeatureType &feature_type, const XmlElementNode::non_null_ptr_type &feature_class_xml_element, const feature_class_xml_element_node_map_type &feature_class_xml_element_node_map, const QString &gpgim_resource_filename)` | method | `GpgimFeatureClass::non_null_ptr_to_const_type` | private | Compiles a feature class definition from the specified XML element node. |
| `create_feature_properties( GpgimFeatureClass::gpgim_property_seq_type &gpgim_feature_properties, const XmlElementNode::non_null_ptr_type &feature_class_xml_element, const QString &gpgim_resource_filename)` | method | `void` | private | Create GPGIM feature properties for the feature class associated with the specified XML element node. |
| `is_concrete_feature_class( const XmlElementNode::non_null_ptr_type &feature_class_xml_element, const QString &gpgim_resource_filename)` | method | `bool` | private | Returns true if the feature class (associated with the specified XML element) is concrete. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `qualified_names_are_equal( const QXmlStreamReader &reader, const QString &namespaceUri, const QString &name)` | function | `bool` | Returns true if the given namespaceUri and name match reader.namespaceUri() and reader.name(), false otherwise. |
| `get_qualified_xml_name( const XmlElementNode::non_null_ptr_type &xml_element, const QString &gpgim_resource_filename)` | function | `QualifiedXmlNameType` | Returns the qualified name from the text in the specified XML element node, or throws exception. |
| `get_text( const XmlElementNode::non_null_ptr_type &xml_element, const QString &gpgim_resource_filename)` | function | `QString` | Returns the text string in the specified XML element node, or throws exception. |
| `find_zero_or_one_child_xml_elements( const XmlElementNode::non_null_ptr_type &xml_element, const XmlElementName &child_xml_element_name, const QString &gpgim_resource_filename)` | function | `boost::optional<XmlElementNode::non_null_ptr_type>` | Find zero or one child elements, of xml\_element, with element name child\_xml\_element\_name. |
| `find_one_child_xml_element( const XmlElementNode::non_null_ptr_type &xml_element, const XmlElementName &child_xml_element_name, const QString &gpgim_resource_filename)` | function | `XmlElementNode::non_null_ptr_type` | Find exactly one child element, of xml\_element, with element name child\_xml\_element\_name. |
| `find_zero_or_more_child_xml_elements( std::vector<XmlElementNode::non_null_ptr_type> &child_xml_elements, const XmlElementNode::non_null_ptr_type &xml_element, const XmlElementName &child_xml_element_name, const QString &gpgim_resource_filename)` | function | `void` | Find zero or more child elements, of xml\_element, with element name child\_xml\_element\_name. |
| `find_one_or_more_child_xml_elements( std::vector<XmlElementNode::non_null_ptr_type> &child_xml_elements, const XmlElementNode::non_null_ptr_type &xml_element, const XmlElementName &child_xml_element_name, const QString &gpgim_resource_filename)` | function | `void` | Find one or more child elements, of xml\_element, with element name child\_xml\_element\_name. |
| `CORE_GPGIM_RESOURCE_FILENAME` | variable | `QString` | — |
| `GPLATES_MODEL_GPGIM_H` | macro | `None` | — |

## Notes

All of the parsing work happens in the constructor, so a malformed `gpgim.xml`
throws out of the first `Gpgim::instance()` call — `GpgimInitialisationException`
for any structural problem (carrying the resource filename and the offending XML
line number), or `ErrorOpeningFileForReadingException` if the Qt resource cannot
be opened. Since that first call typically happens deep inside startup, a broken
GPGIM resource is a fatal startup failure rather than a degraded mode. There is
no reload: only the current version is supported, `d_version` is set once, and
`get_version()` asserts it was set.

The object is effectively immutable after construction, but nothing enforces it
and nothing synchronises it. Every accessor is `const` and returns
`non_null_ptr_to_const_type`, so the safe reading is: treat the GPGIM as
read-only global state, and never mutate a `GpgimProperty` obtained from it —
the same instance is shared by every feature class that inherits the property
(`create_feature_properties` looks each one up in `d_property_map` and stores the
pointer). `create_unclassified_feature_class` is the exception that proves the
rule: it clones before changing multiplicity, and its comment flags the
consequence, that the unclassified feature class holds properties which are
*not* in the global property list returned by `get_properties()`.

`create_feature_class_if_necessary` has no cycle detection. A feature class is
inserted into `d_feature_class_map` only after it and its ancestors are fully
built, so a circular `gpgim:Inherits` chain in the XML recurses until the stack
runs out rather than raising `GpgimInitialisationException`. Anything else
missing or duplicated in the file is diagnosed properly.

Note the "uninstantiated" versus "instantiated" template distinction, which is
easy to trip over. `get_property_structural_types` and
`get_property_structural_type` deal in bare structural types (`gpml:Array`) and
deliberately exclude instantiations; `get_property_template_structural_type`,
keyed on the structural type *and* the value type, is the only way to reach
`gpml:Array<gml:TimePeriod>`. Enumerations are a subset of the structural types,
so they appear in both `get_property_structural_types` and
`get_property_enumeration_types`.

`get_feature_property` and `get_feature_properties` are thin conveniences that
delegate to `GpgimFeatureClass`, which is where inherited properties are
resolved. Both return `boost::none` / `false` for an unrecognised feature type
and for a recognised type that lacks the property, so a negative result does not
distinguish "no such feature type" from "no such property on it".

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 36 |
| [file-io/GpmlFeatureReaderFactory](../file-io/GpmlFeatureReaderFactory.md) | file-io | 18 |
| [model/ModelUtils](ModelUtils.md) | model | 15 |
| [qt-widgets/AddPropertyDialog](../qt-widgets/AddPropertyDialog.md) | qt-widgets | 11 |
| [qt-widgets/ChoosePropertyWidget](../qt-widgets/ChoosePropertyWidget.md) | qt-widgets | 11 |
| [qt-widgets/CreateFeaturePropertiesPage](../qt-widgets/CreateFeaturePropertiesPage.md) | qt-widgets | 11 |
| [file-io/GpmlPropertyStructuralTypeReader](../file-io/GpmlPropertyStructuralTypeReader.md) | file-io | 7 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 7 |
| [qt-widgets/ChooseFeatureTypeWidget](../qt-widgets/ChooseFeatureTypeWidget.md) | qt-widgets | 6 |
| [qt-widgets/EditEnumerationWidget](../qt-widgets/EditEnumerationWidget.md) | qt-widgets | 6 |
| [qt-widgets/GpgimVersionWarningDialog](../qt-widgets/GpgimVersionWarningDialog.md) | qt-widgets | 5 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 4 |
| [gui/FeatureTypeColourPalette](../gui/FeatureTypeColourPalette.md) | gui | 4 |
| [gui/Palette](../gui/Palette.md) | gui | 4 |
| [qt-widgets/EditWidgetGroupBox](../qt-widgets/EditWidgetGroupBox.md) | qt-widgets | 4 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 3 |
| [file-io/GpmlReader](../file-io/GpmlReader.md) | file-io | 3 |
| [qt-widgets/AboutDialog](../qt-widgets/AboutDialog.md) | qt-widgets | 3 |
| [qt-widgets/ChangeFeatureTypeDialog](../qt-widgets/ChangeFeatureTypeDialog.md) | qt-widgets | 3 |
| [qt-widgets/ChangePropertyWidget](../qt-widgets/ChangePropertyWidget.md) | qt-widgets | 3 |

*... and 5 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/Gpgim.h
python scripts/gpq.py def GPlatesModel::Gpgim --body
python scripts/gpq.py uses Gpgim --kind class
python scripts/gpq.py hier Gpgim
```

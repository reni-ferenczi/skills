# StringSetSingletons

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 1208 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/StringSetSingletons.h` | C++ | 100 |
| `src/model/StringSetSingletons.cc` | C++ | 166 |

## Overview

This unit is the interning backend for the model's qualified-name and short-string types: `FeatureType`, `PropertyName`, `StructuralType`, `XmlAttributeName`, `XmlElementName`, `XmlNamespace`, `EnumerationContent`, `EnumerationType`, and similar types all resolve, through their factory classes, to one of the accessor functions declared here. Each accessor lazily creates and returns a process-wide `GPlatesUtils::StringSet` (or, for feature IDs, `GPlatesUtils::IdStringSet`) via `GPlatesUtils::Singleton`, so equal strings anywhere in the loaded model share one interned entry.

The empty tag structs (`FeatureTypeInstance`, `PropertyNameInstance`, and so on) exist purely as distinct template arguments to `GPlatesUtils::Singleton`. Because `Singleton<GPlatesUtils::StringSet, ..., Tag>` instantiates a separate static instance per `Tag`, one otherwise-identical template gives every string category (feature types, property names, XML attribute names, and the rest) its own independent `StringSet`, rather than all of them sharing a single global one.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::StringSetSingletons::FeatureTypeInstance`](#gplatesmodelstringsetsingletonsfeaturetypeinstance) | struct | — | — | 0 | Empty structs just so we can get different instances of StringSet returned from different \*\_instance() functions. |
| [`GPlatesModel::StringSetSingletons::PropertyNameInstance`](#gplatesmodelstringsetsingletonspropertynameinstance) | struct | — | — | 0 | — |
| [`GPlatesModel::StringSetSingletons::StructuralTypeInstance`](#gplatesmodelstringsetsingletonsstructuraltypeinstance) | struct | — | — | 0 | — |
| [`GPlatesModel::StringSetSingletons::TextContentInstance`](#gplatesmodelstringsetsingletonstextcontentinstance) | struct | — | — | 0 | — |
| [`GPlatesModel::StringSetSingletons::TimescaleBandInstance`](#gplatesmodelstringsetsingletonstimescalebandinstance) | struct | — | — | 0 | — |
| [`GPlatesModel::StringSetSingletons::TimescaleNameInstance`](#gplatesmodelstringsetsingletonstimescalenameinstance) | struct | — | — | 0 | — |
| [`GPlatesModel::StringSetSingletons::XMLAttributeNameInstance`](#gplatesmodelstringsetsingletonsxmlattributenameinstance) | struct | — | — | 0 | — |
| [`GPlatesModel::StringSetSingletons::XMLAttributeValueInstance`](#gplatesmodelstringsetsingletonsxmlattributevalueinstance) | struct | — | — | 0 | — |
| [`GPlatesModel::StringSetSingletons::XMLNamespaceInstance`](#gplatesmodelstringsetsingletonsxmlnamespaceinstance) | struct | — | — | 0 | — |
| [`GPlatesModel::StringSetSingletons::XMLNamespaceAliasInstance`](#gplatesmodelstringsetsingletonsxmlnamespacealiasinstance) | struct | — | — | 0 | — |
| [`GPlatesModel::StringSetSingletons::XMLElementNameInstance`](#gplatesmodelstringsetsingletonsxmlelementnameinstance) | struct | — | — | 0 | — |
| [`GPlatesModel::StringSetSingletons::EnumerationContentInstance`](#gplatesmodelstringsetsingletonsenumerationcontentinstance) | struct | — | — | 0 | — |
| [`GPlatesModel::StringSetSingletons::EnumerationTypeInstance`](#gplatesmodelstringsetsingletonsenumerationtypeinstance) | struct | — | — | 0 | — |

## Members

### `GPlatesModel::StringSetSingletons::FeatureTypeInstance`

*None.*

### `GPlatesModel::StringSetSingletons::PropertyNameInstance`

*None.*

### `GPlatesModel::StringSetSingletons::StructuralTypeInstance`

*None.*

### `GPlatesModel::StringSetSingletons::TextContentInstance`

*None.*

### `GPlatesModel::StringSetSingletons::TimescaleBandInstance`

*None.*

### `GPlatesModel::StringSetSingletons::TimescaleNameInstance`

*None.*

### `GPlatesModel::StringSetSingletons::XMLAttributeNameInstance`

*None.*

### `GPlatesModel::StringSetSingletons::XMLAttributeValueInstance`

*None.*

### `GPlatesModel::StringSetSingletons::XMLNamespaceInstance`

*None.*

### `GPlatesModel::StringSetSingletons::XMLNamespaceAliasInstance`

*None.*

### `GPlatesModel::StringSetSingletons::XMLElementNameInstance`

*None.*

### `GPlatesModel::StringSetSingletons::EnumerationContentInstance`

*None.*

### `GPlatesModel::StringSetSingletons::EnumerationTypeInstance`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_STRINGSETSINGLETONS_H` | macro | `None` | — |
| `feature_id_instance` | variable | `GPlatesUtils::IdStringSet` | — |
| `feature_type_instance` | variable | `GPlatesUtils::StringSet` | — |
| `property_name_instance` | variable | `GPlatesUtils::StringSet` | — |
| `structural_type_instance` | variable | `GPlatesUtils::StringSet` | — |
| `text_content_instance` | variable | `GPlatesUtils::StringSet` | — |
| `timescale_band_instance` | variable | `GPlatesUtils::StringSet` | — |
| `timescale_name_instance` | variable | `GPlatesUtils::StringSet` | — |
| `xml_attribute_name_instance` | variable | `GPlatesUtils::StringSet` | — |
| `xml_attribute_value_instance` | variable | `GPlatesUtils::StringSet` | — |
| `xml_namespace_instance` | variable | `GPlatesUtils::StringSet` | — |
| `xml_namespace_alias_instance` | variable | `GPlatesUtils::StringSet` | — |
| `xml_element_name_instance` | variable | `GPlatesUtils::StringSet` | — |
| `enumeration_content_instance` | variable | `GPlatesUtils::StringSet` | — |
| `enumeration_type_instance` | variable | `GPlatesUtils::StringSet` | — |

## Notes

Each `*_instance()` function returns a singleton with process lifetime (`GPlatesUtils::DefaultLifetime`); the returned `StringSet`/`IdStringSet` is never destroyed until the corresponding `Singleton` decides to, so entries interned here persist for the life of the application even after every `QualifiedXmlName` referencing them goes away.

## Used by

| Unit | Component | References |
|---|---|---|
| [model/QualifiedXmlName](QualifiedXmlName.md) | model | 13 |
| [file-io/GpmlReaderUtils](../file-io/GpmlReaderUtils.md) | file-io | 9 |
| [utils/XmlNamespaces](../utils/XmlNamespaces.md) | utils | 7 |
| [file-io/XmlWriter](../file-io/XmlWriter.md) | file-io | 5 |
| [model/TranscribeQualifiedXmlName](TranscribeQualifiedXmlName.md) | model | 4 |
| [model/XmlAttributeValue](XmlAttributeValue.md) | model | 3 |
| [property-values/EnumerationContent](../property-values/EnumerationContent.md) | property-values | 3 |
| [property-values/TextContent](../property-values/TextContent.md) | property-values | 3 |
| [property-values/TimescaleBand](../property-values/TimescaleBand.md) | property-values | 3 |
| [property-values/TimescaleName](../property-values/TimescaleName.md) | property-values | 3 |
| [model/FeatureId](FeatureId.md) | model | 2 |
| [model/FeatureType](FeatureType.md) | model | 2 |
| [model/PropertyName](PropertyName.md) | model | 2 |
| [model/XmlAttributeName](XmlAttributeName.md) | model | 2 |
| [model/XmlElementName](XmlElementName.md) | model | 2 |
| [property-values/EnumerationType](../property-values/EnumerationType.md) | property-values | 2 |
| [property-values/StructuralType](../property-values/StructuralType.md) | property-values | 2 |
| [property-values/ValueObjectType](../property-values/ValueObjectType.md) | property-values | 2 |
| [model/IdTypeGenerator](IdTypeGenerator.md) | model | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/StringSetSingletons.h
python scripts/gpq.py def GPlatesModel::StringSetSingletons::FeatureTypeInstance --body
python scripts/gpq.py uses FeatureTypeInstance --kind struct
python scripts/gpq.py hier FeatureTypeInstance
```

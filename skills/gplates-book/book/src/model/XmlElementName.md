# XmlElementName

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 138 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/XmlElementName.h` | C++ | 53 |

## Overview

`GPlatesModel::XmlElementName` is the type used to hold the name of an XML element (namespace, namespace alias and local name together) throughout GPML parsing and writing. It is a `typedef` for `QualifiedXmlName<XmlElementNameFactory>`, which stores each of the three parts as an iterator into a shared `GPlatesUtils::StringSet` rather than as its own `QString`, so element names that recur across a document — or across every document of a given feature type — share one interned copy and compare in constant time.

`XmlElementNameFactory` exists only to give `QualifiedXmlName` the singleton it interns into, by forwarding `instance()` to `StringSetSingletons::xml_element_name_instance()`; it is never itself instantiated. The counterpart for attribute values is `XmlAttributeValue`, which uses the same `StringSet`-backed sharing but without the namespace/alias structure, since an attribute's value has no qualified name.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::XmlElementNameFactory`](#gplatesmodelxmlelementnamefactory) | class | — | — | 0 | — |
| [`GPlatesModel::XmlElementName`](#gplatesmodelxmlelementname) | typedef | — | — | 0 | — |

## Members

### `GPlatesModel::XmlElementNameFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `XmlElementNameFactory()` | constructor | `None` | private | — |

### `GPlatesModel::XmlElementName`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_XMLELEMENTNAME_H` | macro | `None` | — |

## Notes

As with `XmlAttributeValue`, the underlying `StringSet` entries are reference-counted, so an interned namespace, alias or local name is freed once the last `XmlElementName` referencing it goes away rather than persisting for the whole process.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 129 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 87 |
| [model/Gpgim](Gpgim.md) | model | 74 |
| [file-io/GpmlPropertyReader](../file-io/GpmlPropertyReader.md) | file-io | 15 |
| [model/XmlNode](XmlNode.md) | model | 12 |
| [file-io/GpmlFeatureReaderImpl](../file-io/GpmlFeatureReaderImpl.md) | file-io | 6 |
| [file-io/GpmlReader](../file-io/GpmlReader.md) | file-io | 4 |
| [model/XmlNodeUtils](XmlNodeUtils.md) | model | 4 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 3 |
| [model/Metadata](Metadata.md) | model | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/XmlElementName.h
python scripts/gpq.py def GPlatesModel::XmlElementNameFactory --body
python scripts/gpq.py uses XmlElementNameFactory --kind class
python scripts/gpq.py hier XmlElementNameFactory
```

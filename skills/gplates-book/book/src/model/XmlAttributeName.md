# XmlAttributeName

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 138 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/XmlAttributeName.h` | C++ | 54 |

## Overview

`XmlAttributeName` is one of the small interned-string types built on `QualifiedXmlName`: the header itself is a thin instantiation, `typedef QualifiedXmlName<XmlAttributeNameFactory> XmlAttributeName`, that represents the name of an XML attribute (namespace plus local part) attached to a property or element. `XmlAttributeNameFactory` exists only to plug the right backing store into `QualifiedXmlName`'s template: its `instance()` method returns the process-wide `GPlatesUtils::StringSet` from `StringSetSingletons::xml_attribute_name_instance()`, so every `XmlAttributeName` with the same qualified name shares one interned entry.

Following the same pattern as `XmlElementName`, `PropertyName`, and `FeatureType`, the private, never-defined constructor on the factory class exists solely to prevent it from ever being instantiated — it is used purely as a namespace-like carrier for `instance()`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::XmlAttributeNameFactory`](#gplatesmodelxmlattributenamefactory) | class | — | — | 0 | — |
| [`GPlatesModel::XmlAttributeName`](#gplatesmodelxmlattributename) | typedef | — | — | 0 | — |

## Members

### `GPlatesModel::XmlAttributeNameFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `XmlAttributeNameFactory()` | constructor | `None` | private | — |

### `GPlatesModel::XmlAttributeName`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_XMLATTRIBUTENAME_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [model/ModelUtils](ModelUtils.md) | model | 13 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 9 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 7 |
| [model/Gpgim](Gpgim.md) | model | 6 |
| [property-values/GmlOrientableCurve](../property-values/GmlOrientableCurve.md) | property-values | 6 |
| [property-values/GpmlMeasure](../property-values/GpmlMeasure.md) | property-values | 6 |
| [file-io/GpmlFormatDeformationExport](../file-io/GpmlFormatDeformationExport.md) | file-io | 5 |
| [file-io/XmlOutputInterface](../file-io/XmlOutputInterface.md) | file-io | 5 |
| [file-io/GpmlFormatReconstructedScalarCoverageExport](../file-io/GpmlFormatReconstructedScalarCoverageExport.md) | file-io | 4 |
| [model/XmlNode](XmlNode.md) | model | 4 |
| [qt-widgets/EditAngleWidget](../qt-widgets/EditAngleWidget.md) | qt-widgets | 4 |
| [file-io/GpmlReaderException](../file-io/GpmlReaderException.md) | file-io | 3 |
| [file-io/deprecated/GpmlOnePointFiveOutputVisitor](../file-io/deprecated/GpmlOnePointFiveOutputVisitor.md) | file-io | 3 |
| [property-values/GmlTimeInstant](../property-values/GmlTimeInstant.md) | property-values | 3 |
| [qt-widgets/CreateSmallCircleFeatureDialog](../qt-widgets/CreateSmallCircleFeatureDialog.md) | qt-widgets | 3 |
| [file-io/GpmlFormatMultiPointVectorFieldExport](../file-io/GpmlFormatMultiPointVectorFieldExport.md) | file-io | 2 |
| [model/TopLevelProperty](TopLevelProperty.md) | model | 2 |
| [model/TopLevelPropertyInline](TopLevelPropertyInline.md) | model | 2 |
| [property-values/GmlDataBlockCoordinateList](../property-values/GmlDataBlockCoordinateList.md) | property-values | 2 |
| [property-values/GmlFile](../property-values/GmlFile.md) | property-values | 2 |

*... and 8 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/XmlAttributeName.h
python scripts/gpq.py def GPlatesModel::XmlAttributeNameFactory --body
python scripts/gpq.py uses XmlAttributeNameFactory --kind class
python scripts/gpq.py hier XmlAttributeNameFactory
```

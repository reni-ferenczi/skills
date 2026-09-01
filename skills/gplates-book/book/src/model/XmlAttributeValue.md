# XmlAttributeValue

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 138 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/XmlAttributeValue.h` | C++ | 55 |

## Overview

`GPlatesModel::XmlAttributeValue` is the type used to hold the text of an XML attribute value while parsing or building a GPML/XML document tree. Rather than defining its own class, the header instantiates `StringContentTypeGenerator<XmlAttributeValueFactory>`: each `XmlAttributeValue` stores an iterator into a single shared `GPlatesUtils::StringSet`, so equal attribute values (which recur constantly across a loaded feature collection — enumerations, `"true"`/`"false"`, common IDs) are interned once and compared by iterator rather than by string content.

`XmlAttributeValueFactory` supplies the one piece `StringContentTypeGenerator` needs from its template parameter: a way to reach the process-wide `StringSet` to intern into. It does this by forwarding to `StringSetSingletons::xml_attribute_value_instance()`; the factory itself is never constructed.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::XmlAttributeValueFactory`](#gplatesmodelxmlattributevaluefactory) | class | — | — | 0 | — |
| [`GPlatesModel::XmlAttributeValue`](#gplatesmodelxmlattributevalue) | typedef | — | — | 0 | — |

## Members

### `GPlatesModel::XmlAttributeValueFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `XmlAttributeValueFactory()` | constructor | `None` | private | — |

### `GPlatesModel::XmlAttributeValue`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_XMLATTRIBUTEVALUE_H` | macro | `None` | — |

## Notes

The shared `StringSet` singleton reference-counts each interned string: an entry is only removed once the last `XmlAttributeValue` holding it is destroyed, so equality between two `XmlAttributeValue`s reduces to comparing the underlying iterators rather than the string contents.

## Used by

| Unit | Component | References |
|---|---|---|
| [model/ModelUtils](ModelUtils.md) | model | 9 |
| [property-values/GmlOrientableCurve](../property-values/GmlOrientableCurve.md) | property-values | 6 |
| [property-values/GpmlMeasure](../property-values/GpmlMeasure.md) | property-values | 6 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 5 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 5 |
| [file-io/GpmlFormatDeformationExport](../file-io/GpmlFormatDeformationExport.md) | file-io | 3 |
| [file-io/XmlOutputInterface](../file-io/XmlOutputInterface.md) | file-io | 3 |
| [model/Gpgim](Gpgim.md) | model | 3 |
| [model/XmlNode](XmlNode.md) | model | 3 |
| [property-values/GmlTimeInstant](../property-values/GmlTimeInstant.md) | property-values | 3 |
| [qt-widgets/EditAngleWidget](../qt-widgets/EditAngleWidget.md) | qt-widgets | 3 |
| [file-io/GpmlFormatReconstructedScalarCoverageExport](../file-io/GpmlFormatReconstructedScalarCoverageExport.md) | file-io | 2 |
| [file-io/deprecated/GpmlOnePointFiveOutputVisitor](../file-io/deprecated/GpmlOnePointFiveOutputVisitor.md) | file-io | 2 |
| [model/TopLevelProperty](TopLevelProperty.md) | model | 2 |
| [property-values/GmlDataBlockCoordinateList](../property-values/GmlDataBlockCoordinateList.md) | property-values | 2 |
| [property-values/GmlFile](../property-values/GmlFile.md) | property-values | 2 |
| [property-values/GmlRectifiedGrid](../property-values/GmlRectifiedGrid.md) | property-values | 2 |
| [qt-widgets/CreateSmallCircleFeatureDialog](../qt-widgets/CreateSmallCircleFeatureDialog.md) | qt-widgets | 2 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 1 |
| [file-io/GpmlFormatMultiPointVectorFieldExport](../file-io/GpmlFormatMultiPointVectorFieldExport.md) | file-io | 1 |

*... and 7 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/XmlAttributeValue.h
python scripts/gpq.py def GPlatesModel::XmlAttributeValueFactory --body
python scripts/gpq.py uses XmlAttributeValueFactory --kind class
python scripts/gpq.py hier XmlAttributeValueFactory
```

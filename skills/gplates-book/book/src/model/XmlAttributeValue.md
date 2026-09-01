# XmlAttributeValue

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 138 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/XmlAttributeValue.h` | C++ | 55 |

## Overview

[[[PROSE overview unit=model/XmlAttributeValue tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=model/XmlAttributeValue tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

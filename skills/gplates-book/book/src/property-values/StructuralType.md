# StructuralType

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 7 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/StructuralType.h` | C++ | 55 |

## Overview

[[[PROSE overview unit=property-values/StructuralType tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::StructuralTypeFactory`](#gplatespropertyvaluesstructuraltypefactory) | class | — | — | 0 | — |
| [`GPlatesPropertyValues::StructuralType`](#gplatespropertyvaluesstructuraltype) | typedef | — | — | 0 | — |

## Members

### `GPlatesPropertyValues::StructuralTypeFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `StructuralTypeFactory()` | constructor | `None` | private | — |

### `GPlatesPropertyValues::StructuralType`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_STRUCTURALTYPE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/StructuralType tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [model/Gpgim](../model/Gpgim.md) | model | 64 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 50 |
| [file-io/GpmlPropertyStructuralTypeReader](../file-io/GpmlPropertyStructuralTypeReader.md) | file-io | 46 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 37 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 31 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 24 |
| [qt-widgets/EditWidgetGroupBox](../qt-widgets/EditWidgetGroupBox.md) | qt-widgets | 22 |
| [model/GpgimStructuralType](../model/GpgimStructuralType.md) | model | 21 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 18 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 16 |
| [model/GpgimTemplateStructuralType](../model/GpgimTemplateStructuralType.md) | model | 16 |
| [app-logic/TopologyUtils](../app-logic/TopologyUtils.md) | app-logic | 13 |
| [qt-widgets/ChangePropertyWidget](../qt-widgets/ChangePropertyWidget.md) | qt-widgets | 12 |
| [file-io/GpmlPropertyReader](../file-io/GpmlPropertyReader.md) | file-io | 10 |
| [property-values/GpmlConstantValue](GpmlConstantValue.md) | property-values | 10 |
| [property-values/GpmlIrregularSampling](GpmlIrregularSampling.md) | property-values | 10 |
| [qt-widgets/EditGeometryWidget](../qt-widgets/EditGeometryWidget.md) | qt-widgets | 10 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 9 |
| [qt-widgets/AddPropertyDialog](../qt-widgets/AddPropertyDialog.md) | qt-widgets | 9 |
| [qt-widgets/ChoosePropertyWidget](../qt-widgets/ChoosePropertyWidget.md) | qt-widgets | 9 |

*... and 80 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/StructuralType.h
python scripts/gpq.py def GPlatesPropertyValues::StructuralTypeFactory --body
python scripts/gpq.py uses StructuralTypeFactory --kind class
python scripts/gpq.py hier StructuralTypeFactory
```

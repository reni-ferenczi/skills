# ValueObjectType

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 7 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/ValueObjectType.h` | C++ | 53 |

## Overview

[[[PROSE overview unit=property-values/ValueObjectType tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::ValueObjectTypeFactory`](#gplatespropertyvaluesvalueobjecttypefactory) | class | — | — | 0 | — |
| [`GPlatesPropertyValues::ValueObjectType`](#gplatespropertyvaluesvalueobjecttype) | typedef | — | — | 0 | — |

## Members

### `GPlatesPropertyValues::ValueObjectTypeFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ValueObjectTypeFactory()` | constructor | `None` | private | — |

### `GPlatesPropertyValues::ValueObjectType`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_VALUEOBJECTTYPE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/ValueObjectType tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ScalarCoverageEvolution](../app-logic/ScalarCoverageEvolution.md) | app-logic | 34 |
| [app-logic/ReconstructScalarCoverageLayerProxy](../app-logic/ReconstructScalarCoverageLayerProxy.md) | app-logic | 21 |
| [presentation/ReconstructScalarCoverageVisualLayerParams](../presentation/ReconstructScalarCoverageVisualLayerParams.md) | presentation | 20 |
| [file-io/GpmlFormatDeformationExport](../file-io/GpmlFormatDeformationExport.md) | file-io | 16 |
| [app-logic/ReconstructScalarCoverageLayerParams](../app-logic/ReconstructScalarCoverageLayerParams.md) | app-logic | 14 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 13 |
| [property-values/GmlDataBlockCoordinateList](GmlDataBlockCoordinateList.md) | property-values | 9 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 9 |
| [app-logic/ReconstructedScalarCoverage](../app-logic/ReconstructedScalarCoverage.md) | app-logic | 6 |
| [file-io/GpmlFormatReconstructedScalarCoverageExport](../file-io/GpmlFormatReconstructedScalarCoverageExport.md) | file-io | 6 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 6 |
| [qt-widgets/ReconstructScalarCoverageLayerOptionsWidget](../qt-widgets/ReconstructScalarCoverageLayerOptionsWidget.md) | qt-widgets | 6 |
| [file-io/GpmlFormatMultiPointVectorFieldExport](../file-io/GpmlFormatMultiPointVectorFieldExport.md) | file-io | 4 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 3 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 2 |
| [property-values/GmlFile](GmlFile.md) | property-values | 2 |
| [app-logic/ScalarCoverageTimeSpan](../app-logic/ScalarCoverageTimeSpan.md) | app-logic | 1 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/ValueObjectType.h
python scripts/gpq.py def GPlatesPropertyValues::ValueObjectTypeFactory --body
python scripts/gpq.py uses ValueObjectTypeFactory --kind class
python scripts/gpq.py hier ValueObjectTypeFactory
```

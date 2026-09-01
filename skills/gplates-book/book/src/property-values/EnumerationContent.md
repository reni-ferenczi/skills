# EnumerationContent

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 756 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/EnumerationContent.h` | C++ | 53 |

## Overview

[[[PROSE overview unit=property-values/EnumerationContent tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::EnumerationContentFactory`](#gplatespropertyvaluesenumerationcontentfactory) | class | — | — | 0 | — |
| [`GPlatesPropertyValues::EnumerationContent`](#gplatespropertyvaluesenumerationcontent) | typedef | — | — | 0 | — |

## Members

### `GPlatesPropertyValues::EnumerationContentFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EnumerationContentFactory()` | constructor | `None` | private | — |

### `GPlatesPropertyValues::EnumerationContent`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_ENUMERATIONCONTENT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/EnumerationContent tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/RotationUtils](../app-logic/RotationUtils.md) | app-logic | 7 |
| [app-logic/ReconstructMethodHalfStageRotation](../app-logic/ReconstructMethodHalfStageRotation.md) | app-logic | 6 |
| [file-io/PlatesFormatUtils](../file-io/PlatesFormatUtils.md) | file-io | 5 |
| [file-io/CitcomsResolvedTopologicalBoundaryExportImpl](../file-io/CitcomsResolvedTopologicalBoundaryExportImpl.md) | file-io | 4 |
| [property-values/Enumeration](Enumeration.md) | property-values | 4 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 3 |
| [view-operations/VisibleReconstructionGeometryExport](../view-operations/VisibleReconstructionGeometryExport.md) | view-operations | 3 |
| [app-logic/ReconstructionFeatureProperties](../app-logic/ReconstructionFeatureProperties.md) | app-logic | 2 |
| [qt-widgets/EditEnumerationWidget](../qt-widgets/EditEnumerationWidget.md) | qt-widgets | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/EnumerationContent.h
python scripts/gpq.py def GPlatesPropertyValues::EnumerationContentFactory --body
python scripts/gpq.py uses EnumerationContentFactory --kind class
python scripts/gpq.py hier EnumerationContentFactory
```

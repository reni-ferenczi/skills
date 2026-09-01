# EnumerationType

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 567 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/EnumerationType.h` | C++ | 55 |

## Overview

[[[PROSE overview unit=property-values/EnumerationType tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::EnumerationTypeFactory`](#gplatespropertyvaluesenumerationtypefactory) | class | — | — | 0 | — |
| [`GPlatesPropertyValues::EnumerationType`](#gplatespropertyvaluesenumerationtype) | typedef | — | — | 0 | — |

## Members

### `GPlatesPropertyValues::EnumerationTypeFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EnumerationTypeFactory()` | constructor | `None` | private | — |

### `GPlatesPropertyValues::EnumerationType`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_ENUMERATIONTYPE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/EnumerationType tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/PlatesFormatUtils](../file-io/PlatesFormatUtils.md) | file-io | 6 |
| [property-values/Enumeration](Enumeration.md) | property-values | 5 |
| [file-io/CitcomsResolvedTopologicalBoundaryExportImpl](../file-io/CitcomsResolvedTopologicalBoundaryExportImpl.md) | file-io | 4 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 4 |
| [view-operations/VisibleReconstructionGeometryExport](../view-operations/VisibleReconstructionGeometryExport.md) | view-operations | 3 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 2 |
| [qt-widgets/EditEnumerationWidget](../qt-widgets/EditEnumerationWidget.md) | qt-widgets | 2 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 1 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 1 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/EnumerationType.h
python scripts/gpq.py def GPlatesPropertyValues::EnumerationTypeFactory --body
python scripts/gpq.py uses EnumerationTypeFactory --kind class
python scripts/gpq.py hier EnumerationTypeFactory
```

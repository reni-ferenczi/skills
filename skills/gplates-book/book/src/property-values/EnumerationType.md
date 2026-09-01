# EnumerationType

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 567 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/EnumerationType.h` | C++ | 55 |

## Overview

`EnumerationType` identifies *which* GPML enumeration a given `Enumeration` property
value belongs to (e.g. `gpml:SubductionZoneType`), as opposed to `EnumerationContent`
which holds the selected member of that enumeration. It is
`GPlatesModel::QualifiedXmlName<EnumerationTypeFactory>` — a namespace-qualified XML
name whose factory supplies the dedicated
`GPlatesModel::StringSetSingletons::enumeration_type_instance()` string pool, so every
`EnumerationType` value is interned separately from other qualified-name kinds
(structural types, property names, feature types) even though they all share the same
`QualifiedXmlName` template.

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

*None.*

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

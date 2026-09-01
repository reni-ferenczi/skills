# ValueObjectType

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 7 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/ValueObjectType.h` | C++ | 53 |

## Overview

`ValueObjectType` is a `GPlatesModel::QualifiedXmlName<ValueObjectTypeFactory>` instantiation, giving namespace-qualified XML names (namespace, alias and local name, each interned) to the "value objects" that appear inside `GmlDataBlockCoordinateList` and related scalar-coverage machinery — for example the type tag identifying which named scalar a coordinate list holds. `ValueObjectTypeFactory` is never instantiated; its only role is to bind `QualifiedXmlName` to a `GPlatesUtils::StringSet` singleton, again with a private constructor.

Notably, `ValueObjectTypeFactory::instance()` returns `GPlatesModel::StringSetSingletons::property_name_instance()` — the same interning pool used for property names — rather than a pool dedicated to value-object types, so `ValueObjectType` values share their interned-string space with `GPlatesModel::PropertyName`.

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

`ValueObjectType` interns into the same `StringSet` singleton (`property_name_instance()`) as `GPlatesModel::PropertyName`, so the two conceptually distinct name kinds share one underlying string pool even though `QualifiedXmlName`'s comparison operators only ever compare same-typed values.

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

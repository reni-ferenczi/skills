# PropertyName

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 138 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/PropertyName.h` | C++ | 55 |

## Overview

[[[PROSE overview unit=model/PropertyName tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::PropertyNameFactory`](#gplatesmodelpropertynamefactory) | class | — | — | 0 | — |
| [`GPlatesModel::PropertyName`](#gplatesmodelpropertyname) | typedef | — | — | 0 | — |

## Members

### `GPlatesModel::PropertyNameFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PropertyNameFactory()` | constructor | `None` | private | — |

### `GPlatesModel::PropertyName`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_PROPERTYNAME_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=model/PropertyName tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/deprecated/FeaturePropertiesMap](../file-io/deprecated/FeaturePropertiesMap.md) | file-io | 194 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 73 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 72 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 36 |
| [app-logic/ScalarCoverageFeatureProperties](../app-logic/ScalarCoverageFeatureProperties.md) | app-logic | 28 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 27 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 27 |
| [model/ModelUtils](ModelUtils.md) | model | 25 |
| [file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport](../file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport.md) | file-io | 24 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 24 |
| [feature-visitors/FeatureClassifier](../feature-visitors/FeatureClassifier.md) | feature-visitors | 23 |
| [file-io/GpmlFeatureReaderFactory](../file-io/GpmlFeatureReaderFactory.md) | file-io | 22 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 21 |
| [model/Gpgim](Gpgim.md) | model | 21 |
| [app-logic/ExtractRasterFeatureProperties](../app-logic/ExtractRasterFeatureProperties.md) | app-logic | 18 |
| [file-io/GpmlFormatMultiPointVectorFieldExport](../file-io/GpmlFormatMultiPointVectorFieldExport.md) | file-io | 18 |
| [app-logic/deprecated/PaleomagUtils](../app-logic/deprecated/PaleomagUtils.md) | app-logic | 17 |
| [app-logic/ReconstructionFeatureProperties](../app-logic/ReconstructionFeatureProperties.md) | app-logic | 15 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](../app-logic/deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 14 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 13 |

*... and 105 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/PropertyName.h
python scripts/gpq.py def GPlatesModel::PropertyNameFactory --body
python scripts/gpq.py uses PropertyNameFactory --kind class
python scripts/gpq.py hier PropertyNameFactory
```

# ReconstructMethodType

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 2 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructMethodType.h` | C++ | 58 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructMethodType tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructMethod::Type`](#gplatesapplogicreconstructmethodtype) | enum | — | — | 0 | An enumeration of different ways to generate ReconstructedFeatureGeometry objects from features. |

## Members

### `GPlatesAppLogic::ReconstructMethod::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `BY_PLATE_ID` | enumerator | `None` | — | — |
| `HALF_STAGE_ROTATION` | enumerator | `None` | — | — |
| `SMALL_CIRCLE` | enumerator | `None` | — | — |
| `VIRTUAL_GEOMAGNETIC_POLE` | enumerator | `None` | — | — |
| `FLOWLINE` | enumerator | `None` | — | — |
| `MOTION_PATH` | enumerator | `None` | — | — |
| `NUM_TYPES` | enumerator | `None` | — | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTMETHODTYPE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructMethodType tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructMethodRegistry](ReconstructMethodRegistry.md) | app-logic | 53 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 43 |
| [file-io/FeatureCollectionFileFormatRegistry](../file-io/FeatureCollectionFileFormatRegistry.md) | file-io | 26 |
| [app-logic/ReconstructedFeatureGeometry](ReconstructedFeatureGeometry.md) | app-logic | 21 |
| [app-logic/ReconstructMethodHalfStageRotation](ReconstructMethodHalfStageRotation.md) | app-logic | 18 |
| [app-logic/PlateVelocityUtils](PlateVelocityUtils.md) | app-logic | 16 |
| [app-logic/TopologyInternalUtils](TopologyInternalUtils.md) | app-logic | 16 |
| [app-logic/ReconstructMethodByPlateId](ReconstructMethodByPlateId.md) | app-logic | 14 |
| [app-logic/ResolvedTriangulationNetwork](ResolvedTriangulationNetwork.md) | app-logic | 14 |
| [app-logic/ResolvedVertexSourceInfo](ResolvedVertexSourceInfo.md) | app-logic | 14 |
| [app-logic/ReconstructMethodInterface](ReconstructMethodInterface.md) | app-logic | 12 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 12 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 11 |
| [file-io/FeatureCollectionFileFormatClassify](../file-io/FeatureCollectionFileFormatClassify.md) | file-io | 11 |
| [app-logic/ReconstructContext](ReconstructContext.md) | app-logic | 9 |
| [app-logic/ScalarField3DLayerTask](ScalarField3DLayerTask.md) | app-logic | 8 |
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 8 |
| [app-logic/TopologyGeometryResolverLayerTask](TopologyGeometryResolverLayerTask.md) | app-logic | 7 |
| [app-logic/TopologyNetworkResolverLayerTask](TopologyNetworkResolverLayerTask.md) | app-logic | 7 |
| [app-logic/RasterLayerTask](RasterLayerTask.md) | app-logic | 6 |

*... and 20 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructMethodType.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructMethod::Type --body
python scripts/gpq.py uses Type --kind enum
```

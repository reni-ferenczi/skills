# ReconstructHandle

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 2 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructHandle.h` | C++ | 79 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructHandle tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructHandle::type`](#gplatesapplogicreconstructhandletype) | typedef | — | — | 0 | Typedef for a global handle that is stored in ReconstructionGeometry instances to identity them, for example, as belonging to a particular group of reconstructed feature geometries. |

## Members

### `GPlatesAppLogic::ReconstructHandle::type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTHANDLE_H` | macro | `None` | — |
| `get_next_reconstruct_handle()` | function | `type` | Returns the next global reconstruct handle by incrementing the integer handle returned by the last call to get\_next\_reconstruct\_handle. |

## Notes

[[[PROSE notes unit=app-logic/ReconstructHandle tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 109 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 80 |
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 73 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 59 |
| [app-logic/ReconstructContext](ReconstructContext.md) | app-logic | 57 |
| [app-logic/ReconstructUtils](ReconstructUtils.md) | app-logic | 32 |
| [app-logic/TopologyGeometryResolver](TopologyGeometryResolver.md) | app-logic | 31 |
| [app-logic/ReconstructedFeatureGeometryFinder](ReconstructedFeatureGeometryFinder.md) | app-logic | 30 |
| [app-logic/ReconstructedFeatureGeometry](ReconstructedFeatureGeometry.md) | app-logic | 26 |
| [app-logic/ReconstructScalarCoverageLayerProxy](ReconstructScalarCoverageLayerProxy.md) | app-logic | 23 |
| [app-logic/ReconstructionGeometryFinder](ReconstructionGeometryFinder.md) | app-logic | 19 |
| [app-logic/LayerProxyUtils](LayerProxyUtils.md) | app-logic | 18 |
| [view-operations/RenderedGeometryUtils](../view-operations/RenderedGeometryUtils.md) | view-operations | 18 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 15 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 11 |
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 10 |
| [app-logic/ReconstructMethodInterface](ReconstructMethodInterface.md) | app-logic | 9 |
| [app-logic/SmallCircleGeometryPopulator](SmallCircleGeometryPopulator.md) | app-logic | 9 |
| [app-logic/ReconstructMethodByPlateId](ReconstructMethodByPlateId.md) | app-logic | 8 |
| [app-logic/ReconstructMethodHalfStageRotation](ReconstructMethodHalfStageRotation.md) | app-logic | 8 |

*... and 42 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructHandle.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructHandle::type --body
python scripts/gpq.py uses type --kind typedef
```

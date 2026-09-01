# LayerTaskType

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1742 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/LayerTaskType.h` | C++ | 71 |
| `src/app-logic/LayerTaskType.cc` | C++ | 58 |

## Overview

[[[PROSE overview unit=app-logic/LayerTaskType tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::LayerTaskType::Type`](#gplatesapplogiclayertasktypetype) | enum | — | — | 0 | — |

## Members

### `GPlatesAppLogic::LayerTaskType::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RECONSTRUCTION` | enumerator | `None` | — | — |
| `RECONSTRUCT` | enumerator | `None` | — | — |
| `RASTER` | enumerator | `None` | — | — |
| `SCALAR_FIELD_3D` | enumerator | `None` | — | — |
| `TOPOLOGY_GEOMETRY_RESOLVER` | enumerator | `None` | — | — |
| `TOPOLOGY_NETWORK_RESOLVER` | enumerator | `None` | — | — |
| `VELOCITY_FIELD_CALCULATOR` | enumerator | `None` | — | — |
| `CO_REGISTRATION` | enumerator | `None` | — | — |
| `RECONSTRUCT_SCALAR_COVERAGE` | enumerator | `None` | — | — |
| `NUM_TYPES` | enumerator | `None` | — | NOTE: Any new values should also be added to transcribe. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_LAYERTASKTYPE_H` | macro | `None` | — |
| `transcribe( GPlatesScribe::Scribe &scribe, Type &layer_task_type, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |

## Notes

[[[PROSE notes unit=app-logic/LayerTaskType tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 43 |
| [presentation/VisualLayerRegistry](../presentation/VisualLayerRegistry.md) | presentation | 37 |
| [presentation/DeprecatedSessionRestore](../presentation/DeprecatedSessionRestore.md) | presentation | 19 |
| [app-logic/LayerTaskRegistry](LayerTaskRegistry.md) | app-logic | 14 |
| [app-logic/ScalarField3DLayerTask](ScalarField3DLayerTask.md) | app-logic | 9 |
| [app-logic/VelocityFieldCalculatorLayerTask](VelocityFieldCalculatorLayerTask.md) | app-logic | 9 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 8 |
| [app-logic/ReconstructLayerTask](ReconstructLayerTask.md) | app-logic | 6 |
| [app-logic/CoRegistrationLayerTask](CoRegistrationLayerTask.md) | app-logic | 5 |
| [app-logic/LayerInputChannelType](LayerInputChannelType.md) | app-logic | 5 |
| [app-logic/TopologyGeometryResolverLayerTask](TopologyGeometryResolverLayerTask.md) | app-logic | 5 |
| [app-logic/TopologyNetworkResolverLayerTask](TopologyNetworkResolverLayerTask.md) | app-logic | 5 |
| [app-logic/RasterLayerTask](RasterLayerTask.md) | app-logic | 4 |
| [app-logic/ReconstructScalarCoverageLayerTask](ReconstructScalarCoverageLayerTask.md) | app-logic | 4 |
| [qt-widgets/AddNewLayerDialog](../qt-widgets/AddNewLayerDialog.md) | qt-widgets | 4 |
| [app-logic/Layer](Layer.md) | app-logic | 3 |
| [app-logic/ReconstructGraph](ReconstructGraph.md) | app-logic | 3 |
| [app-logic/ReconstructionLayerTask](ReconstructionLayerTask.md) | app-logic | 3 |
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 3 |
| [presentation/VisualLayerType](../presentation/VisualLayerType.md) | presentation | 3 |

*... and 23 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/LayerTaskType.h
python scripts/gpq.py def GPlatesAppLogic::LayerTaskType::Type --body
python scripts/gpq.py uses Type --kind enum
```

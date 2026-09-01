# LayerTaskType

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1742 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/LayerTaskType.h` | C++ | 71 |
| `src/app-logic/LayerTaskType.cc` | C++ | 58 |

## Overview

`LayerTaskType::Type` is the closed enumeration of the nine kinds of layer that exist in the reconstruct graph (reconstruction, reconstruct, raster, scalar field 3D, the two topology resolvers, velocity field calculator, co-registration, reconstruct scalar coverage). It is the tag that `LayerTaskRegistry` and `LayerTask::get_layer_type()` use to identify a layer's kind to the GUI — for example to pick the right visual layer widget — without exposing or switching on the concrete `LayerTask` subclass.

`transcribe()` serializes a `Type` value by name (via `GPlatesScribe::transcribe_enum_protocol`) rather than by its numeric value, so sessions and projects saved by one version stay readable even if the enumerators are reordered.

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

`NUM_TYPES` must stay the last enumerator, and any new value added before it must also get an entry in `transcribe()`'s `enum_values` table (keyed by a fixed string id) — the header comment flags this explicitly, and forgetting it breaks loading of existing sessions/projects for the new type. The string ids themselves must never be changed once shipped, since they are the on-disk/session format, even if an enumerator's C++ name changes later.

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

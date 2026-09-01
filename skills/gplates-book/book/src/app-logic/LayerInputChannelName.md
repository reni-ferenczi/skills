# LayerInputChannelName

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1741 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/LayerInputChannelName.h` | C++ | 85 |
| `src/app-logic/LayerInputChannelName.cc` | C++ | 71 |

## Overview

[[[PROSE overview unit=app-logic/LayerInputChannelName tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::LayerInputChannelName::Type`](#gplatesapplogiclayerinputchannelnametype) | enum | — | — | 0 | The layer input channel names. |

## Members

### `GPlatesAppLogic::LayerInputChannelName::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RECONSTRUCTION_FEATURES` | enumerator | `None` | — | — |
| `RECONSTRUCTABLE_FEATURES` | enumerator | `None` | — | — |
| `TOPOLOGICAL_GEOMETRY_FEATURES` | enumerator | `None` | — | — |
| `TOPOLOGICAL_NETWORK_FEATURES` | enumerator | `None` | — | — |
| `RASTER_FEATURE` | enumerator | `None` | — | — |
| `SCALAR_FIELD_FEATURE` | enumerator | `None` | — | — |
| `RECONSTRUCTION_TREE` | enumerator | `None` | — | — |
| `TOPOLOGY_SURFACES` | enumerator | `None` | — | — |
| `TOPOLOGICAL_SECTION_LAYERS` | enumerator | `None` | — | — |
| `VELOCITY_DOMAIN_LAYERS` | enumerator | `None` | — | — |
| `VELOCITY_SURFACE_LAYERS` | enumerator | `None` | — | — |
| `RECONSTRUCTED_POLYGONS` | enumerator | `None` | — | — |
| `AGE_GRID_RASTER` | enumerator | `None` | — | — |
| `NORMAL_MAP_RASTER` | enumerator | `None` | — | — |
| `CROSS_SECTIONS` | enumerator | `None` | — | — |
| `SURFACE_POLYGONS_MASK` | enumerator | `None` | — | — |
| `CO_REGISTRATION_SEED_GEOMETRIES` | enumerator | `None` | — | — |
| `CO_REGISTRATION_TARGET_GEOMETRIES` | enumerator | `None` | — | — |
| `RECONSTRUCTED_SCALAR_COVERAGE_DOMAINS` | enumerator | `None` | — | — |
| `UNUSED` | enumerator | `None` | — | NOTE: Any new values should also be added to transcribe. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_LAYERINPUTCHANNELNAME_H` | macro | `None` | — |
| `transcribe( GPlatesScribe::Scribe &scribe, Type &layer_input_channel_name, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |

## Notes

[[[PROSE notes unit=app-logic/LayerInputChannelName tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/VisualLayerInputChannelName](../presentation/VisualLayerInputChannelName.md) | presentation | 64 |
| [app-logic/ReconstructLayerTask](ReconstructLayerTask.md) | app-logic | 48 |
| [app-logic/RasterLayerTask](RasterLayerTask.md) | app-logic | 47 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 46 |
| [presentation/DeprecatedSessionRestore](../presentation/DeprecatedSessionRestore.md) | presentation | 45 |
| [app-logic/ScalarField3DLayerTask](ScalarField3DLayerTask.md) | app-logic | 41 |
| [app-logic/TopologyGeometryResolverLayerTask](TopologyGeometryResolverLayerTask.md) | app-logic | 41 |
| [app-logic/Layer](Layer.md) | app-logic | 35 |
| [app-logic/TopologyNetworkResolverLayerTask](TopologyNetworkResolverLayerTask.md) | app-logic | 35 |
| [app-logic/CoRegistrationLayerTask](CoRegistrationLayerTask.md) | app-logic | 32 |
| [app-logic/VelocityFieldCalculatorLayerTask](VelocityFieldCalculatorLayerTask.md) | app-logic | 32 |
| [app-logic/ReconstructionLayerTask](ReconstructionLayerTask.md) | app-logic | 27 |
| [app-logic/ReconstructScalarCoverageLayerTask](ReconstructScalarCoverageLayerTask.md) | app-logic | 26 |
| [presentation/VisualLayerRegistry](../presentation/VisualLayerRegistry.md) | presentation | 25 |
| [app-logic/ReconstructGraphImpl](ReconstructGraphImpl.md) | app-logic | 23 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 23 |
| [app-logic/LayerInputChannelType](LayerInputChannelType.md) | app-logic | 19 |
| [app-logic/LayerTask](LayerTask.md) | app-logic | 14 |
| [qt-widgets/VisualLayerWidget](../qt-widgets/VisualLayerWidget.md) | qt-widgets | 14 |
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 8 |

*... and 29 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/LayerInputChannelName.h
python scripts/gpq.py def GPlatesAppLogic::LayerInputChannelName::Type --body
python scripts/gpq.py uses Type --kind enum
```

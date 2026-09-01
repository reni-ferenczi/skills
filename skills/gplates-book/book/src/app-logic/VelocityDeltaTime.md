# VelocityDeltaTime

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1622 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/VelocityDeltaTime.h` | C++ | 86 |
| `src/app-logic/VelocityDeltaTime.cc` | C++ | 107 |

## Overview

[[[PROSE overview unit=app-logic/VelocityDeltaTime tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::VelocityDeltaTime::Type`](#gplatesapplogicvelocitydeltatimetype) | enum | — | — | 0 | The time range (given a delta time) relative to a specific time that a velocity is calculated using. |

## Members

### `GPlatesAppLogic::VelocityDeltaTime::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `T_PLUS_DELTA_T_TO_T` | enumerator | `None` | — | — |
| `T_TO_T_MINUS_DELTA_T` | enumerator | `None` | — | — |
| `T_PLUS_MINUS_HALF_DELTA_T` | enumerator | `None` | — | — |
| `NUM_TYPES` | enumerator | `None` | — | NOTE: Any new values should also be added to transcribe. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_VELOCITYDELTATIME_H` | macro | `None` | — |
| `get_time_range( Type delta_time_type, const double &time, const double &delta_time = 1.0, bool allow_negative_range = true)` | function | `std::pair<double, double>` | Returns the time range giving a time, delta time and delta time type. |
| `transcribe( GPlatesScribe::Scribe &scribe, Type &velocity_delta_time, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |

## Notes

[[[PROSE notes unit=app-logic/VelocityDeltaTime tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 37 |
| [app-logic/ResolvedTriangulationNetwork](ResolvedTriangulationNetwork.md) | app-logic | 35 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 33 |
| [app-logic/PlateVelocityUtils](PlateVelocityUtils.md) | app-logic | 29 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 24 |
| [qt-widgets/ExportVelocityCalculationOptionsWidget](../qt-widgets/ExportVelocityCalculationOptionsWidget.md) | qt-widgets | 21 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 17 |
| [app-logic/ResolvedVertexSourceInfo](ResolvedVertexSourceInfo.md) | app-logic | 14 |
| [app-logic/VelocityParams](VelocityParams.md) | app-logic | 14 |
| [qt-widgets/VelocityFieldCalculatorLayerOptionsWidget](../qt-widgets/VelocityFieldCalculatorLayerOptionsWidget.md) | qt-widgets | 14 |
| [app-logic/ResolvedTriangulationDelaunay2](ResolvedTriangulationDelaunay2.md) | app-logic | 13 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 10 |
| [app-logic/CoRegistrationLayerTask](CoRegistrationLayerTask.md) | app-logic | 7 |
| [gui/ExportOptionsUtils](../gui/ExportOptionsUtils.md) | gui | 7 |
| [app-logic/ReconstructContext](ReconstructContext.md) | app-logic | 5 |
| [app-logic/ReconstructMethodInterface](ReconstructMethodInterface.md) | app-logic | 4 |
| [app-logic/ReconstructMethodFlowline](ReconstructMethodFlowline.md) | app-logic | 3 |
| [app-logic/ReconstructMethodHalfStageRotation](ReconstructMethodHalfStageRotation.md) | app-logic | 3 |
| [app-logic/ReconstructMethodByPlateId](ReconstructMethodByPlateId.md) | app-logic | 2 |
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/VelocityDeltaTime.h
python scripts/gpq.py def GPlatesAppLogic::VelocityDeltaTime::Type --body
python scripts/gpq.py uses Type --kind enum
```

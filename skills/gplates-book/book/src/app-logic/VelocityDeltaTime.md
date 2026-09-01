# VelocityDeltaTime

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1622 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/VelocityDeltaTime.h` | C++ | 86 |
| `src/app-logic/VelocityDeltaTime.cc` | C++ | 107 |

## Overview

`VelocityDeltaTime` defines how a velocity is turned from an instantaneous quantity into a finite-difference one: velocity is computed from the positional change between two nearby reconstruction times, and `Type` selects which two times relative to the target time (`t + delta_t -> t`, `t -> t - delta_t`, or the centred `t + delta_t/2 -> t - delta_t/2`) are used to form that pair. `get_time_range()` turns a `Type`, a time and a delta time into the actual `(older, younger)` pair of times that a caller — such as `PlateVelocityUtils` or a `LayerProxy` computing a velocity field — should reconstruct at and difference.

This is a small, self-contained utility rather than a class: the enum plus one pure function plus a `transcribe()` so the choice of delta-time type can be saved and restored with a project or session.

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

When `allow_negative_range` is false and the younger end of the range would fall below time 0, `get_time_range()` does not clamp that end to 0 while keeping the older end fixed — it instead returns the fixed-width range `(delta_time, 0.0)` for both `T_TO_T_MINUS_DELTA_T` and `T_PLUS_MINUS_HALF_DELTA_T`, so the interval width is always exactly `delta_time` regardless of how close `time` is to 0.

The enumerators in `transcribe()`'s string table are serialised by name and must never be renamed once shipped, even if the C++ enumerator name changes, or saved projects/sessions referencing the old name will fail to load. Any new `Type` value must be added both before `NUM_TYPES` and to that table — `get_time_range()` has a `BOOST_STATIC_ASSERT(NUM_TYPES == 3)` that only catches the C++ side of this.

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

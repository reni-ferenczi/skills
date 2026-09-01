# VelocityParams

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 279 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/VelocityParams.h` | C++ | 210 |
| `src/app-logic/VelocityParams.cc` | C++ | 185 |

## Overview

`VelocityParams` is the plain-data configuration bundle for a velocity layer: which of the two `SolveVelocitiesMethodType` strategies to use, the `VelocityDeltaTime::Type` and delta time to difference over, and whether/how to smooth velocities across plate and network boundaries. `VelocityFieldCalculatorLayerParams` stores one and `VelocityFieldCalculatorLayerProxy` reads it (and uses it as a cache key) to decide how to compute each `MultiPointVectorField`.

The two `SolveVelocitiesMethodType` values distinguish computing the velocity of the domain geometry's own reconstructed motion (`SOLVE_VELOCITIES_OF_DOMAIN_POINTS`) from intersecting the domain geometry with a separate rigid or deforming surface and reporting that surface's velocity at the intersection point (`SOLVE_VELOCITIES_OF_SURFACES_AT_DOMAIN_POINTS`, the original and still-default behaviour). Boundary smoothing, when enabled, blends a domain point's calculated velocity with the average velocity either side of a nearby plate/network boundary, over an angular half-extent in degrees, optionally excluding deforming regions from that averaging.

The class provides value semantics (`operator==`, `operator<` via `boost::equality_comparable`/`boost::less_than_comparable`) so it can be used directly as a map/cache key, and a private `transcribe()` so its settings persist in saved sessions and projects.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::VelocityParams`](#gplatesapplogicvelocityparams) | class | `boost::less_than_comparable<VelocityParams>`<br>`boost::equality_comparable<VelocityParams>` | — | 0 | VelocityParams is used to store additional parameters for calculating velocities in VelocityFieldCalculatorLayerTask layers. |

## Members

### `GPlatesAppLogic::VelocityParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SolveVelocitiesMethodType` | enum | `None` | public | How to calculate velocities. |
| `VelocityParams()` | constructor | `None` | public | — |
| `get_solve_velocities_method()` | method | `SolveVelocitiesMethodType` | public | — |
| `set_solve_velocities_method( SolveVelocitiesMethodType solve_velocities_method)` | method | `void` | public | — |
| `get_delta_time_type()` | method | `VelocityDeltaTime::Type` | public | — |
| `set_delta_time_type( VelocityDeltaTime::Type delta_time_calculation)` | method | `void` | public | — |
| `get_delta_time()` | method | `double` | public | — |
| `set_delta_time( const double &delta_time)` | method | `void` | public | — |
| `get_is_boundary_smoothing_enabled()` | method | `bool` | public | — |
| `set_is_boundary_smoothing_enabled( bool is_boundary_smoothing_enabled = true)` | method | `void` | public | — |
| `get_boundary_smoothing_angular_half_extent_degrees()` | method | `double` | public | Specifies the angular distance (radians) over which velocities are smoothed across a plate/network boundary. |
| `set_boundary_smoothing_angular_half_extent_degrees( const double &boundary_smoothing_angular_half_extent_degrees)` | method | `void` | public | — |
| `get_exclude_deforming_regions_from_smoothing()` | method | `bool` | public | — |
| `set_exclude_deforming_regions_from_smoothing( bool exclude_deforming_regions_from_smoothing = true)` | method | `void` | public | — |
| `operator==( const VelocityParams &rhs)` | operator | `bool` | public | Equality comparison operator. |
| `operator<( const VelocityParams &rhs)` | operator | `bool` | public | Less than comparison operator. |
| `d_solve_velocities_method` | field | `SolveVelocitiesMethodType` | private | — |
| `d_delta_time_type` | field | `VelocityDeltaTime::Type` | private | — |
| `d_delta_time` | field | `GPlatesMaths::Real` | private | — |
| `d_is_boundary_smoothing_enabled` | field | `bool` | private | — |
| `d_boundary_smoothing_angular_half_extent_degrees` | field | `GPlatesMaths::Real` | private | — |
| `d_exclude_deforming_regions_from_smoothing` | field | `bool` | private | — |
| `transcribe( GPlatesScribe::Scribe &scribe, bool transcribed_construct_data)` | method | `GPlatesScribe::TranscribeResult` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator==( const VelocityParams &rhs)` | operator | `bool` | — |
| `operator<( const VelocityParams &rhs)` | operator | `bool` | — |
| `GPLATES_APP_LOGIC_VELOCITYPARAMS_H` | macro | `None` | — |
| `transcribe( GPlatesScribe::Scribe &scribe, VelocityParams::SolveVelocitiesMethodType &solve_velocities_method_type, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |

## Notes

The default constructor picks `SOLVE_VELOCITIES_OF_SURFACES_AT_DOMAIN_POINTS` (kept for backward compatibility with how GPlates originally calculated velocities) rather than the simpler `SOLVE_VELOCITIES_OF_DOMAIN_POINTS`, a 1.0 delta time with `T_PLUS_DELTA_T_TO_T`, boundary smoothing disabled, a 1-degree half-extent, and `exclude_deforming_regions_from_smoothing` set true. As with `VelocityDeltaTime::Type`, the `SolveVelocitiesMethodType` enumerator names are persisted by string in `transcribe()` and must not be renamed once shipped; any new value must be added both before `NUM_SOLVE_VELOCITY_METHODS` and to that transcribe table.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/VelocityFieldCalculatorLayerOptionsWidget](../qt-widgets/VelocityFieldCalculatorLayerOptionsWidget.md) | qt-widgets | 47 |
| [app-logic/VelocityFieldCalculatorLayerProxy](VelocityFieldCalculatorLayerProxy.md) | app-logic | 34 |
| [gui/ExportVelocityAnimationStrategy](../gui/ExportVelocityAnimationStrategy.md) | gui | 7 |
| [app-logic/VelocityFieldCalculatorLayerParams](VelocityFieldCalculatorLayerParams.md) | app-logic | 5 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 1 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/VelocityParams.h
python scripts/gpq.py def GPlatesAppLogic::VelocityParams --body
python scripts/gpq.py uses VelocityParams --kind class
python scripts/gpq.py hier VelocityParams
```

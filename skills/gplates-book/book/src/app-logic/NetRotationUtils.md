# NetRotationUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1193 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/NetRotationUtils.h` | C++ | 115 |
| `src/app-logic/NetRotationUtils.cc` | C++ | 228 |

## Overview

`NetRotationUtils` is the point-by-point math behind a net-rotation calculation. `calc_net_rotation_contribution` takes one sample point together with the `GPlatesMaths::FiniteRotation` stage pole that applies to its plate, and turns the stage pole's rotation angle and axis into a per-point rotation vector plus a cos-latitude weighting factor, packaged as a `NetRotationResult`. `sum_net_rotations` folds a stream of these per-point results into a running total keyed by plate id (`net_rotation_map_type`), and `convert_net_rotation_xyz_to_pole`/`convert_net_rotation_pole_to_xyz` convert between the Cartesian `GPlatesMaths::Vector3D` form used during accumulation and the pole-and-angle (`GPlatesMaths::LatLonPoint` plus degrees/Ma) form used to report a result.

The module is a set of stateless free functions with no owned data; it does not itself iterate over a plate's points or a reconstruction's plates. That driving loop, and ownership of the accumulated `net_rotation_map_type`, belongs to the caller — currently `ExportNetRotationAnimationStrategy` in `gui`, which is the only unit that uses this one.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::NetRotationUtils::NetRotationResult`](#gplatesapplogicnetrotationutilsnetrotationresult) | struct | — | — | 0 | The NetRotationResult struct - used for storing intermediate results during point-by-point net-rotation calculations. |
| [`GPlatesAppLogic::NetRotationUtils::net_rotation_map_type`](#gplatesapplogicnetrotationutilsnet_rotation_map_type) | typedef | — | — | 0 | — |

## Members

### `GPlatesAppLogic::NetRotationUtils::NetRotationResult`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NetRotationResult( const GPlatesMaths::Vector3D &rotation_component, const double &weighting_factor, const double &plate_area_component, const double &plate_angular_velocity)` | constructor | `None` | public | — |
| `NetRotationResult()` | constructor | `None` | public | — |
| `d_rotation_component` | field | `GPlatesMaths::Vector3D` | public | — |
| `d_weighting_factor` | field | `double` | public | — |
| `d_plate_area_component` | field | `double` | public | — |
| `d_plate_angular_velocity` | field | `double` | public | — |

### `GPlatesAppLogic::NetRotationUtils::net_rotation_map_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `display_net_rotation_output_( const GPlatesAppLogic::NetRotationUtils::net_rotation_map_type &results, const double &time, bool also_by_plate = true)` | function | `void` | — |
| `GPLATES_APP_LOGIC_NETROTATIONUTILS_H` | macro | `None` | — |
| `calc_net_rotation_contribution( const GPlatesMaths::PointOnSphere &point, const GPlatesMaths::FiniteRotation &stage_pole, double time_interval)` | function | `NetRotationResult` | calc\_net\_rotation\_components - calculate the contribution to the plate net-rotation for the point point - Vector3D: the cartesian form of the rotation for the point - double: the weighting factor for the point |
| `sum_net_rotations( const NetRotationUtils::net_rotation_map_type::value_type &net_rotation, NetRotationUtils::net_rotation_map_type &net_rotations)` | function | `void` | sum\_net\_rotations - keeps a running total of net-rotation per plate-id. |
| `display_net_rotation_output( const GPlatesAppLogic::NetRotationUtils::net_rotation_map_type &results, const double &time, bool also_by_plate = true)` | function | `void` | display\_net\_rotation\_output - for debug output |
| `convert_net_rotation_xyz_to_pole( const GPlatesMaths::Vector3D v)` | function | `std::pair<GPlatesMaths::LatLonPoint, double>` | — |
| `convert_net_rotation_pole_to_xyz( const GPlatesMaths::LatLonPoint &llp, const double &angle)` | function | `GPlatesMaths::Vector3D` | — |

## Notes

- `calc_net_rotation_contribution` returns a zero-valued `NetRotationResult` early when the stage pole is an identity rotation or when `time_interval` is (almost) zero, to avoid dividing by zero when converting the rotation angle to degrees/Ma.
- The per-point weighting factor is `(x² + y²) · cos(latitude)` of the sample point, not a plate area; `sum_net_rotations` simply adds these weights, so the caller is responsible for normalising by the total weight (as `display_net_rotation_output` does) to get a meaningful average.
- `display_net_rotation_output` is debug-only (`qDebug` output) and silently swallows any `std::exception` it catches.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 61 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/NetRotationUtils.h
python scripts/gpq.py def GPlatesAppLogic::NetRotationUtils::NetRotationResult --body
python scripts/gpq.py uses NetRotationResult --kind struct
python scripts/gpq.py hier NetRotationResult
```

# RotationUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 2 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/RotationUtils.h` | C++ | 154 |
| `src/app-logic/RotationUtils.cc` | C++ | 536 |

## Overview

Free-function helpers for deriving rotations that are not simple lookups in a `ReconstructionTree` — half-stage (mid-ocean-ridge spreading) rotations, stage poles between two reconstruction times, and short-path adjustment of a total rotation. Plain reconstruction-geometry math belongs in `ReconstructUtils` instead; this header is reserved for rotation-specific calculations.

`get_half_stage_rotation` computes the rotation of a spreading ridge between a `left_plate_id` and `right_plate_id`, given a `spreading_asymmetry` in `[-1,1]` and a `spreading_start_time`. Because the interval from spreading start to the reconstruction time can be long, the calculation is chopped into sub-intervals of `DEFAULT_TIME_INTERVAL_HALF_STAGE_ROTATION` (10 My) each, using a `ReconstructionTreeCreator` to build the intermediate `ReconstructionTree`s it needs. The overload taking a `ReconstructionFeatureProperties` dispatches to one of three historical formulas (a single-interval symmetric-spreading version, a multi-interval version with asymmetry, and a version that adds the spreading start time) depending on which properties are present on the feature, preserving compatibility with rotations authored under older GPlates versions.

`get_stage_pole` derives the stage rotation of one plate relative to another between two already-resolved `ReconstructionTree` instants. `calculate_short_path_final_rotation` exists because interpolated total rotations always take the short path by construction, but the *stage* rotation implied by two total rotations can still work out to the long way around the globe; it flips `final_rotation` to the equivalent short-path rotation so that a subsequently derived stage pole is well-behaved.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_ROTATIONUTILS_H` | macro | `None` | — |
| `DEFAULT_TIME_INTERVAL_HALF_STAGE_ROTATION` | variable | `double` | The default time interval for calculating half-stage rotations (see get\_half\_stage\_rotation). |
| `get_half_stage_rotation( const ReconstructionTreeCreator &reconstruction_tree_creator, const double &reconstruction_time, GPlatesModel::integer_plate_id_type left_plate_id, GPlatesModel::integer_plate_id_type right_plate_id, const double &spreading_asymmetry = 0.0, const double &spreading_start_time = 0.0, const double ...` | function | `GPlatesMaths::FiniteRotation` | Returns the half-stage rotation between left\_plate\_id and right\_plate\_id at the reconstruction time. spreading\_asymmetry is in the range \[-1,1\] where the value 0 represents half-stage rotation, the value 1 represents full-stage rotation ... |
| `get_half_stage_rotation( const double &reconstruction_time, const ReconstructionFeatureProperties &reconstruction_params, const ReconstructionTreeCreator &reconstruction_tree_creator)` | function | `GPlatesMaths::FiniteRotation` | Calculate the half-stage rotation at the specified time using the specified reconstruction properties. |
| `get_stage_pole( const ReconstructionTree &reconstruction_tree_ptr_1, const ReconstructionTree &reconstruction_tree_ptr_2, const GPlatesModel::integer_plate_id_type &moving_plate_id, const GPlatesModel::integer_plate_id_type &fixed_plate_id)` | function | `GPlatesMaths::FiniteRotation` | Returns the stage-pole for moving\_plate\_id wrt fixed\_plate\_id, between the times represented by reconstruction\_tree\_ptr\_1 and reconstruction\_tree\_ptr\_2 |
| `calculate_short_path_final_rotation( const GPlatesMaths::FiniteRotation &final_rotation, const GPlatesMaths::FiniteRotation &initial_rotation)` | function | `boost::optional<GPlatesMaths::FiniteRotation>` | Returns an adjusted version of final\_rotation such that the relative rotation from initial\_rotation to final\_rotation takes the short path around the globe (instead of long path), or returns none if it's already the short path. |

## Notes

`get_half_stage_rotation` throws `PreconditionViolationError` if `half_stage_rotation_interval` is not greater than zero. The three-version dispatch in the `ReconstructionFeatureProperties` overload means results for the same feature can change depending on which optional properties (spreading asymmetry, spreading start time) were recorded when the feature was authored — do not assume a single formula applies across all data.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructMethodHalfStageRotation](ReconstructMethodHalfStageRotation.md) | app-logic | 9 |
| [app-logic/ReconstructUtils](ReconstructUtils.md) | app-logic | 8 |
| [app-logic/FlowlineUtils](FlowlineUtils.md) | app-logic | 7 |
| [app-logic/ReconstructMethodFlowline](ReconstructMethodFlowline.md) | app-logic | 7 |
| [app-logic/FlowlineGeometryPopulator](FlowlineGeometryPopulator.md) | app-logic | 5 |
| [app-logic/ResolvedVertexSourceInfo](ResolvedVertexSourceInfo.md) | app-logic | 5 |
| [file-io/PlatesRotationFormatReader](../file-io/PlatesRotationFormatReader.md) | file-io | 4 |
| [app-logic/ResolvedTriangulationNetwork](ResolvedTriangulationNetwork.md) | app-logic | 3 |
| [cli/CliStageRotationCommand](../cli/CliStageRotationCommand.md) | cli | 3 |
| [gui/ExportStageRotationAnimationStrategy](../gui/ExportStageRotationAnimationStrategy.md) | gui | 3 |
| [qt-widgets/CreateSmallCircleDialog](../qt-widgets/CreateSmallCircleDialog.md) | qt-widgets | 3 |
| [qt-widgets/MovePoleWidget](../qt-widgets/MovePoleWidget.md) | qt-widgets | 3 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 2 |
| [app-logic/NetRotationUtils](NetRotationUtils.md) | app-logic | 1 |
| [qt-widgets/KinematicGraphsDialog](../qt-widgets/KinematicGraphsDialog.md) | qt-widgets | 1 |
| [qt-widgets/deprecated/CalculateStagePoleDialog](../qt-widgets/deprecated/CalculateStagePoleDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/RotationUtils.h
```

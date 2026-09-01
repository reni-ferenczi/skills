# RotationUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 2 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/RotationUtils.h` | C++ | 154 |
| `src/app-logic/RotationUtils.cc` | C++ | 536 |

## Overview

[[[PROSE overview unit=app-logic/RotationUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=app-logic/RotationUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

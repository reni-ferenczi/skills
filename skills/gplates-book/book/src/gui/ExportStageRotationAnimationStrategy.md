# ExportStageRotationAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 274 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportStageRotationAnimationStrategy.h` | C++ | 183 |
| `src/gui/ExportStageRotationAnimationStrategy.cc` | C++ | 279 |

## Overview

`ExportStageRotationAnimationStrategy` writes finite *stage* rotations — the rotation from time `t + delta_t` back to `t` — at each animation frame, rather than the total rotations from present day. `Configuration::RotationType` selects both the rotation kind (`RELATIVE`, between a moving/fixed plate pair, or `EQUIVALENT`, relative to the anchor plate) and the output field separator (comma, semicolon or tab) in one enum; the shared `ExportOptionsUtils::ExportRotationOptions` and `ExportOptionsUtils::ExportStageRotationOptions` supply the identity/Euler-pole formatting and the `time_interval` used as `delta_t`.

`do_export_iteration` builds two `GPlatesAppLogic::ReconstructionTree`s from the same reconstruction-tree creator, one at the current view time and one at `view_time + time_interval`, then calls `get_relative_stage_rotation` or `get_equivalent_stage_rotation` to derive the `GPlatesMaths::UnitQuaternion3D` stage rotation between them for the configured plate(s) before writing it out.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ExportStageRotationAnimationStrategy`](#gplatesguiexportstagerotationanimationstrategy) | class | [`GPlatesGui::ExportAnimationStrategy`](ExportAnimationStrategy.md) | — | 0 | Concrete implementation of the ExportAnimationStrategy class for writing \*stage\* (t + delta\_t -\> t) rotation poles at each timestep 't' for either: (1) equivalent (to anchor plate), or (2) relative (fixed/moving pairs). |

## Members

### `GPlatesGui::ExportStageRotationAnimationStrategy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportStageRotationAnimationStrategy>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportStageRotationAnimationStrategy\>. |
| `Configuration` | class | `None` | public | Configuration options. |
| `const_configuration_ptr` | typedef | `boost::shared_ptr<const Configuration>` | public | Typedef for a shared pointer to const Configuration. |
| `create( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | method | `non_null_ptr_type` | public | — |
| `~ExportStageRotationAnimationStrategy()` | destructor | `None` | public | — |
| `do_export_iteration( std::size_t frame_index)` | method | `bool` | public | Does one frame of export. |
| `ExportStageRotationAnimationStrategy( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | constructor | `None` | protected | Protected constructor to prevent instantiation on the stack. |
| `d_configuration` | field | `const_configuration_ptr` | private | Export configuration parameters. |
| `get_relative_stage_rotation( const GPlatesAppLogic::ReconstructionTree &tree1, const GPlatesAppLogic::ReconstructionTree &tree2, GPlatesModel::integer_plate_id_type moving_plate_id, GPlatesModel::integer_plate_id_type fixed_plate_id)` | method | `GPlatesMaths::UnitQuaternion3D` | private | Calculates the relative stage rotation for the specified fixed/moving plate pair from time t2 -\> t1. |
| `get_equivalent_stage_rotation( const GPlatesAppLogic::ReconstructionTree &tree1, const GPlatesAppLogic::ReconstructionTree &tree2, GPlatesModel::integer_plate_id_type plate_id)` | method | `GPlatesMaths::UnitQuaternion3D` | private | Calculates the equivalent stage rotation for the specified plate id from time t2 -\> t1. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_EXPORTSTAGEROTATIONSTRATEGY_H` | macro | `None` | — |

## Notes

The two reconstruction trees are built at `view_time` and `view_time + stage_rotation_options.time_interval`; `get_relative_stage_rotation`/`get_equivalent_stage_rotation` compute the rotation from the second tree's time back to the first, so a positive `time_interval` looks forward in time from the current frame.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 43 |
| [qt-widgets/ExportStageRotationOptionsWidget](../qt-widgets/ExportStageRotationOptionsWidget.md) | qt-widgets | 15 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportStageRotationAnimationStrategy.h
python scripts/gpq.py def GPlatesGui::ExportStageRotationAnimationStrategy --body
python scripts/gpq.py uses ExportStageRotationAnimationStrategy --kind class
python scripts/gpq.py hier ExportStageRotationAnimationStrategy
```

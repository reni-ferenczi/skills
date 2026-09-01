# ExportStageRotationAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 274 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportStageRotationAnimationStrategy.h` | C++ | 183 |
| `src/gui/ExportStageRotationAnimationStrategy.cc` | C++ | 279 |

## Overview

[[[PROSE overview unit=gui/ExportStageRotationAnimationStrategy tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=gui/ExportStageRotationAnimationStrategy tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

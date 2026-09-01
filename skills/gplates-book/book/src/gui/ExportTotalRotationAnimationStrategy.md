# ExportTotalRotationAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 251 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportTotalRotationAnimationStrategy.h` | C++ | 149 |
| `src/gui/ExportTotalRotationAnimationStrategy.cc` | C++ | 216 |

## Overview

`ExportTotalRotationAnimationStrategy` writes finite *total* rotations — from the current reconstruction time back to present day — at each animation frame, as opposed to `ExportStageRotationAnimationStrategy`'s stage-to-stage rotations. Like the stage variant, `Configuration::RotationType` folds together whether the rotation is `RELATIVE` (moving-to-fixed plate pair) or `EQUIVALENT` (to the anchor plate) with the output field separator, and it reuses `ExportOptionsUtils::ExportRotationOptions` for identity/Euler-pole formatting.

`do_export_iteration` walks every edge of the default reconstruction layer's `GPlatesAppLogic::ReconstructionTree`, taking each edge's `get_relative_rotation()` (relative) or `get_composed_absolute_rotation()` (equivalent), and writes one line per plate id via `GPlatesGui::CsvExport`. It always exports the tree from the *default* reconstruction layer, not a layer the user selects.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ExportTotalRotationAnimationStrategy`](#gplatesguiexporttotalrotationanimationstrategy) | class | [`GPlatesGui::ExportAnimationStrategy`](ExportAnimationStrategy.md) | — | 0 | Concrete implementation of the ExportAnimationStrategy class for writing \*total\* (to present day) rotation poles at each timestep for either: (1) equivalent (to anchor plate), or (2) relative (fixed/moving pairs). |

## Members

### `GPlatesGui::ExportTotalRotationAnimationStrategy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportTotalRotationAnimationStrategy>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportReconstructedGeometryAnimationStrategy\>. |
| `Configuration` | class | `None` | public | Configuration options. |
| `const_configuration_ptr` | typedef | `boost::shared_ptr<const Configuration>` | public | Typedef for a shared pointer to const Configuration. |
| `create( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | method | `non_null_ptr_type` | public | — |
| `~ExportTotalRotationAnimationStrategy()` | destructor | `None` | public | — |
| `do_export_iteration( std::size_t frame_index)` | method | `bool` | public | Does one frame of export. |
| `ExportTotalRotationAnimationStrategy( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | constructor | `None` | protected | Protected constructor to prevent instantiation on the stack. |
| `d_configuration` | field | `const_configuration_ptr` | private | Export configuration parameters. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_EXPORTTOTALROTATIONANIMATIONSTRATEGY_H` | macro | `None` | — |

## Notes

When a reconstruction has more than one reconstruction-tree-producing layer, this strategy always exports the default layer's tree; there is no way to export a different one (noted as a FIXME in the implementation).

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 31 |
| [qt-widgets/ExportTotalRotationOptionsWidget](../qt-widgets/ExportTotalRotationOptionsWidget.md) | qt-widgets | 13 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportTotalRotationAnimationStrategy.h
python scripts/gpq.py def GPlatesGui::ExportTotalRotationAnimationStrategy --body
python scripts/gpq.py uses ExportTotalRotationAnimationStrategy --kind class
python scripts/gpq.py hier ExportTotalRotationAnimationStrategy
```

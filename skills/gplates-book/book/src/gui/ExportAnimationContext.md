# ExportAnimationContext

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 694 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportAnimationContext.h` | C++ | 291 |
| `src/gui/ExportAnimationContext.cc` | C++ | 182 |

## Overview

[[[PROSE overview unit=gui/ExportAnimationContext tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ExportAnimationContext`](#gplatesguiexportanimationcontext) | class | [`GPlatesUtils::ReferenceCount<ExportAnimationContext>`](../utils/ReferenceCount.md) | — | 0 | ExportAnimationContext manages the iteration steps and progress bar updates while we are exporting an animation via the ExportAnimationDialog. |

## Members

### `GPlatesGui::ExportAnimationContext`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportAnimationContext>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportAnimationContext\>. |
| `ExportAnimationContext( GPlatesQtWidgets::ExportAnimationDialog &export_animation_dialog_, GPlatesGui::AnimationController &animation_controller_, GPlatesPresentation::ViewState &view_state_, GPlatesQtWidgets::ViewportWindow &viewport_window_)` | constructor | `None` | public | — |
| `~ExportAnimationContext()` | destructor | `None` | public | — |
| `view_time` | field | `double` | public | — |
| `get_export_dialog()` | method | `GPlatesQtWidgets::ExportAnimationDialog` | public | — |
| `is_running()` | method | `bool` | public | — |
| `set_target_dir( const QDir &dir)` | method | `void` | public | — |
| `add_export_animation_strategy( ExportAnimationType::ExportID, const ExportAnimationStrategy::const_configuration_base_ptr &cfg)` | method | `void` | public | — |
| `clear_export_animation_strategies()` | method | `void` | public | — |
| `animation_controller` | field | `GPlatesGui::AnimationController` | public | — |
| `get_sequence()` | method | `GPlatesUtils::AnimationSequence::SequenceInfo` | public | The SequenceInfo configured by the export dialog may be different from the global one configured in the AnimationController, due to export dialogs being smushed together. |
| `set_sequence( const GPlatesUtils::AnimationSequence::SequenceInfo &seq)` | method | `void` | public | The SequenceInfo configured by the export dialog may be different from the global one configured in the AnimationController, due to export dialogs being smushed together. |
| `view_state` | field | `GPlatesPresentation::ViewState` | public | — |
| `viewport_window` | field | `GPlatesQtWidgets::ViewportWindow` | public | — |
| `abort()` | method | `void` | public | Used by ExportAnimationDialog in response to user. |
| `do_export()` | method | `bool` | public | Prepares filename template, calls suitable functions for each export iteration, updates progress bar. |
| `update_status_message( const QString &message)` | method | `void` | public | — |
| `EXPORT_ITEMS` | enum | `None` | public | — |
| `exporter_multimap_type` | typedef | `std::multimap< ExportAnimationType::ExportID, ExportAnimationStrategy::non_null_ptr_type>` | private | Typedef to multimap export ID to an ExportAnimationStrategy. |
| `d_export_animation_dialog_ptr` | field | `GPlatesQtWidgets::ExportAnimationDialog` | private | Pointer back to the ExportAnimationDialog, so that we can update the progress bar and status message during export. |
| `d_animation_controller_ptr` | field | `GPlatesGui::AnimationController` | private | This is the animation controller, which holds the state of any animation set up in the application. |
| `d_sequence_info` | field | `GPlatesUtils::AnimationSequence::SequenceInfo` | private | And this is just the currently-set-up animation sequence, which now may differ from the global animation in the AnimationController because the Export Snapshot/Sequence dialogs were smushed together. |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | View State pointer, which needs to be accessible to the various strategies so that they can get access to things like the current anchored plate ID and the Reconstruction. |
| `d_viewport_window` | field | `GPlatesQtWidgets::ViewportWindow` | private | Temporary access point for some view state. |
| `d_abort_now` | field | `bool` | private | Flag that gets set when the user requests, nay demands, that we stop what we are doing. |
| `d_export_running` | field | `bool` | private | Flag set while we are in the do\_export() loop. |
| `d_target_dir` | field | `QDir` | private | The target output directory where all the files get written to. |
| `d_exporter_multimap` | field | `exporter_multimap_type` | private | A multimap of export ID to exporters. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_EXPORTANIMATIONCONTEXT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/ExportAnimationContext tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportAnimationDialog](../qt-widgets/ExportAnimationDialog.md) | qt-widgets | 71 |
| [qt-widgets/ConfigureExportParametersDialog](../qt-widgets/ConfigureExportParametersDialog.md) | qt-widgets | 42 |
| [gui/ExportVelocityAnimationStrategy](ExportVelocityAnimationStrategy.md) | gui | 24 |
| [qt-widgets/ExportVelocityOptionsWidget](../qt-widgets/ExportVelocityOptionsWidget.md) | qt-widgets | 22 |
| [gui/ExportDeformationAnimationStrategy](ExportDeformationAnimationStrategy.md) | gui | 21 |
| [gui/ExportScalarCoverageAnimationStrategy](ExportScalarCoverageAnimationStrategy.md) | gui | 21 |
| [gui/ExportNetRotationAnimationStrategy](ExportNetRotationAnimationStrategy.md) | gui | 20 |
| [qt-widgets/EditExportParametersDialog](../qt-widgets/EditExportParametersDialog.md) | qt-widgets | 20 |
| [qt-widgets/ExportScalarCoverageOptionsWidget](../qt-widgets/ExportScalarCoverageOptionsWidget.md) | qt-widgets | 14 |
| [gui/ExportRasterAnimationStrategy](ExportRasterAnimationStrategy.md) | gui | 13 |
| [gui/ExportCitcomsResolvedTopologyAnimationStrategy](ExportCitcomsResolvedTopologyAnimationStrategy.md) | gui | 11 |
| [gui/ExportFlowlineAnimationStrategy](ExportFlowlineAnimationStrategy.md) | gui | 10 |
| [gui/ExportMotionPathAnimationStrategy](ExportMotionPathAnimationStrategy.md) | gui | 10 |
| [gui/ExportReconstructedGeometryAnimationStrategy](ExportReconstructedGeometryAnimationStrategy.md) | gui | 10 |
| [gui/ExportResolvedTopologyAnimationStrategy](ExportResolvedTopologyAnimationStrategy.md) | gui | 10 |
| [qt-widgets/ExportImageResolutionOptionsWidget](../qt-widgets/ExportImageResolutionOptionsWidget.md) | qt-widgets | 10 |
| [qt-widgets/ExportRotationOptionsWidget](../qt-widgets/ExportRotationOptionsWidget.md) | qt-widgets | 10 |
| [gui/ExportAnimationStrategy](ExportAnimationStrategy.md) | gui | 8 |
| [qt-widgets/ExportSvgOptionsWidget](../qt-widgets/ExportSvgOptionsWidget.md) | qt-widgets | 8 |
| [gui/ExportImageAnimationStrategy](ExportImageAnimationStrategy.md) | gui | 7 |

*... and 20 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportAnimationContext.h
python scripts/gpq.py def GPlatesGui::ExportAnimationContext --body
python scripts/gpq.py uses ExportAnimationContext --kind class
python scripts/gpq.py hier ExportAnimationContext
```

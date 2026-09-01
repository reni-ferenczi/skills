# ExportAnimationContext

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 694 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportAnimationContext.h` | C++ | 291 |
| `src/gui/ExportAnimationContext.cc` | C++ | 182 |

## Overview

This is the driver of the whole animation-export feature: the loop that steps the
application through a range of geological times and asks each configured exporter to
write one frame. The header names it as the Context of a textbook Strategy pattern,
with `ExportAnimationStrategy` as the abstract Strategy and one concrete subclass per
kind of output (reconstructed geometries, resolved topologies, velocities, rasters,
SVG snapshots, and so on). The Context holds the strategies; the strategies hold a
raw back-pointer to the Context, and that back-pointer is how they reach everything
they need — `ViewState`, `ViewportWindow`, the target directory, the current view
time and the sequence definition. The header cites the same book for that decision
too, so the back-reference is deliberate rather than accidental coupling.

Using it is a three-phase protocol driven by `ExportAnimationDialog`. First
`set_target_dir()` and `set_sequence()`; then one
`add_export_animation_strategy()` call per row the user configured, each of which
delegates construction to the `ExportAnimationRegistry` held by `ViewState` —
looked up by `ExportAnimationType::ExportID` and handed the per-row configuration
object. Finally `do_export()`. The ordering matters and the header says why: each
concrete strategy builds its `GPlatesFileIO::ExportTemplateFilenameSequence` in its
constructor from `get_sequence()`, so a sequence set after the strategies exist is
ignored by their filename templates.

`do_export()` itself is small. For each frame it computes the time from the
`SequenceInfo`, pushes it into `AnimationController::set_view_time()` — which is what
actually drives the application to reconstruct — and then walks the multimap calling
`check_filename_sequence()` and `do_export_iteration(frame_index)` on every strategy.
Filenames are the strategies' business, not the Context's: each pulls the next name
off its own filename iterator and joins it to `target_dir()`. The one piece of state
the Context keeps for its own sake is `d_sequence_info`, which deliberately does *not*
track the `AnimationController`'s global animation sequence — the header explains
that the snapshot (single-frame) and sequence export dialogs were merged, so the
export range is set independently and strategies must read it from `get_sequence()`
rather than from the controller.

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

`do_export()` runs synchronously on the GUI thread and blocks for the entire
export — there is no worker thread. Abort works only because
`ExportAnimationDialog::update_progress_bar()` and `update_status_message()` both
call `QCoreApplication::processEvents()` after repainting, which is what lets the
Abort button's click be delivered and set `d_abort_now`. That has two consequences
worth knowing before writing a new strategy. A strategy that runs a long frame
without calling `update_status_message()` makes the application unresponsive and
delays abort for that whole frame. And because events *are* processed mid-export,
arbitrary other slots can run between frames; `ExportAnimationDialog::setVisible()`
relies on this, calling abort if the user closes the dialog while `is_running()`.

`d_abort_now` is tested once per frame, at the top of the loop, so aborting is
granular to a whole frame and never interrupts a strategy mid-iteration. On the
failure path the `ok = ok && check_filename_sequence() && do_export_iteration(...)`
chain short-circuits, so once one strategy fails, the remaining strategies for that
frame are skipped entirely rather than run and ignored — then every strategy gets
`wrap_up(false)` and `do_export()` returns false. On success every strategy gets
`wrap_up(true)`. Either way the view time is left wherever the last exported frame
put it; nothing restores the time the user was viewing before the export.

Ownership is strictly nested but held with raw pointers in both directions. The
Context is reference counted and owned by `ExportAnimationDialog`, but keeps
unguarded raw pointers to the dialog, the `AnimationController`, the `ViewState` and
the `ViewportWindow` — all of which outlive it in practice. It owns its strategies
(`non_null_ptr_type` values in the multimap), and each strategy points back at it
raw, so no strategy may outlive the Context. `ExportAnimationDialog` calls
`clear_export_animation_strategies()` immediately after `do_export()` returns, so
strategies are freshly constructed for every export run and cannot carry state
between runs — anything a strategy caches in its constructor (loaded file lists, for
instance) is a snapshot of the moment the user pressed Export.

The multimap is keyed rather than a plain list because the same `ExportID` can appear
more than once: the user may configure two exports of the same type and format with
different options. Iteration order within a frame is therefore the map's key order,
not the order the user added the rows.

One thing the member table above overstates: `EXPORT_ITEMS` is inside an `#if 0`
block, with a comment saying it appears obsolete. It is not compiled and nothing
refers to it.

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

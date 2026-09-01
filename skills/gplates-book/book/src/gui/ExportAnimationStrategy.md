# ExportAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 251 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportAnimationStrategy.h` | C++ | 201 |
| `src/gui/ExportAnimationStrategy.cc` | C++ | 114 |

## Overview

The abstract Strategy half of the export-animation design whose Context is
`ExportAnimationContext`. A subclass answers one question — how do I write one frame
of one kind of output — and the fifteen that exist cover reconstructed geometries,
resolved topologies, flowlines, motion paths, velocities, net rotations, stage and
total rotations, deformation, scalar coverages, rasters, images, SVG snapshots and
co-registration results. The base contributes three things they all share: the
filename sequence, the back-pointer to the Context through which everything else is
reached, and the per-frame call contract.

The filename machinery is the substantial part. `set_template_filename()` takes the
user's template string and builds a `GPlatesFileIO::ExportTemplateFilenameSequence`
from it, supplying the four things the template's format codes need that a strategy
cannot know on its own: the current anchored plate ID from `ApplicationState` (`%A`),
the name of the visual layer for the default reconstruction tree layer (`%R`, found by
taking `ReconstructGraph::get_default_reconstruction_tree_layer()` and looking it up
through `VisualLayers`; empty if no rotation layer is loaded), and the start time, end
time, increment and trailing-frame flag from the Context's `get_sequence()`. It then
parks an iterator at the beginning. Every concrete strategy calls this from its own
constructor with `d_configuration->get_filename_template()`, so the sequence is fixed
at the moment the export is configured, not when it runs. Several strategies override
`set_template_filename()` to massage the template first and then delegate to this
implementation.

Configuration is a parallel hierarchy rather than a set of constructor arguments.
`ConfigurationBase` carries only the filename template; each concrete strategy nests a
`Configuration` deriving from it that adds its own format enum, file options and flags,
and implements the virtual `clone()`. This is what lets
`ConfigureExportParametersDialog` and `EditExportParametersDialog` hold, copy and edit
a configuration for an export type they know nothing about, and what lets
`ExportAnimationRegistry` store a default configuration per `ExportID` and pass a
`const_configuration_base_ptr` through a generic factory template that
`boost::dynamic_pointer_cast`s it down to the strategy's own nested `Configuration`
before calling that strategy's `create()`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ExportAnimationStrategy`](#gplatesguiexportanimationstrategy) | class | [`GPlatesUtils::ReferenceCount<ExportAnimationStrategy>`](../utils/ReferenceCount.md) | — | 15 | Base class for the different Export Animation strategies. |

## Members

### `GPlatesGui::ExportAnimationStrategy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportAnimationStrategy>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportAnimationStrategy\>. |
| `~ExportAnimationStrategy()` | destructor | `None` | public | — |
| `const_configuration_base_ptr` | typedef | `boost::shared_ptr<const ConfigurationBase>` | public | Typedef for a shared pointer to const ConfigurationBase. |
| `configuration_base_ptr` | typedef | `boost::shared_ptr<ConfigurationBase>` | public | Typedef for a shared pointer to ConfigurationBase. |
| `ConfigurationBase` | class | `None` | public | Configuration parameters for an ExportAnimationStrategy. |
| `create( GPlatesGui::ExportAnimationContext &export_animation_context)` | method | `non_null_ptr_type` | public | Creates an export animation strategy that doesn't do anything. |
| `set_template_filename( const QString &filename)` | method | `void` | public | Sets the internal ExportTemplateFilenameSequence. |
| `do_export_iteration( std::size_t frame_index)` | method | `bool` | public | Does one frame of export. |
| `wrap_up( bool export_successful)` | method | `void` | public | Allows Strategy objects to do any housekeeping that might be necessary after all export iterations are completed. |
| `check_filename_sequence()` | method | `bool` | public | — |
| `ExportAnimationStrategy( GPlatesGui::ExportAnimationContext &export_animation_context)` | constructor | `None` | protected | Protected constructor to prevent instantiation on the stack. |
| `d_export_animation_context_ptr` | field | `GPlatesGui::ExportAnimationContext` | protected | Pointer back to the Context, as an easy way to get at all kinds of state. |
| `d_filename_sequence_opt` | field | `boost::optional<GPlatesFileIO::ExportTemplateFilenameSequence>` | protected | The filename sequence to use when exporting. |
| `d_filename_iterator_opt` | field | `boost::optional<GPlatesFileIO::ExportTemplateFilenameSequence::const_iterator>` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_EXPORTANIMATIONSTRATEGY_H` | macro | `None` | — |

## Notes

The base class is not abstract, and that is deliberate but easy to trip over.
`do_export_iteration()` has a body returning `false` rather than being pure virtual,
because `ExportAnimationStrategy::create()` builds a do-nothing instance for
`ExportAnimationRegistry` to return when an unknown `ExportID` is requested — a null
object that keeps the return type a `non_null_ptr_type`. The cost is that a subclass
which fails to override `do_export_iteration()` compiles cleanly and then fails the
entire export on the first frame, since `ExportAnimationContext::do_export()` treats
a `false` return as fatal. `wrap_up()`'s empty default is genuinely optional by
contrast.

The filename iterator is checked by the base and advanced by the subclass.
`check_filename_sequence()` only verifies that both optionals are engaged and that the
iterator has not reached the end; each `do_export_iteration()` is expected to
dereference and post-increment `*d_filename_iterator_opt` itself, then join the result
to `d_export_animation_context_ptr->target_dir()`. Omitting the increment silently
writes every frame to the same file. Omitting the `set_template_filename()` call in the
constructor leaves both optionals disengaged, which
`check_filename_sequence()` reports as a not-properly-initialised error and fails the
run before frame zero.

`set_template_filename()` does not validate and does not catch. The
`ExportTemplateFilenameSequence` constructor throws `UnrecognisedFormatString`,
`TimeIncrementZero` or `IncorrectTimeIncrementSign`, and since every strategy calls
it from its own constructor, a bad template propagates out of
`ExportAnimationContext::add_export_animation_strategy()` — before any export starts.
The intended guard is the separate `validate_filename_template` function the registry
holds per exporter, which the configure dialogs call first. Two template codes have
deferred semantics worth knowing: `%T` and `%D` capture the wall-clock time and date at
which the iterator is *first dereferenced*, and `%P` is left unexpanded by design for
the strategy to substitute after dereferencing —
`ExportCitcomsResolvedTopologyAnimationStrategy` passes it down into
`CitcomsResolvedTopologicalBoundaryExport` so that one frame fans out into several
files, one per boundary type.

Error handling is by return value, not exception. The convention every concrete
strategy follows is to wrap its writing in `try`/`catch`, report through
`d_export_animation_context_ptr->update_status_message()` and return `false`; letting
an exception escape into `do_export()` would skip the `wrap_up(false)` cleanup on
every strategy.

Ownership runs one way. The strategy is intrusively reference counted and owned by the
Context's multimap; the `d_export_animation_context_ptr` back-pointer is raw and never
checked, so a strategy must never outlive its Context. The protected constructor
enforces heap allocation through the subclasses' static `create()`. Everything runs on
the GUI thread inside the Context's blocking export loop, so a strategy that does slow
work without calling `update_status_message()` freezes the interface and delays the
user's abort.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 48 |
| [gui/ExportVelocityAnimationStrategy](ExportVelocityAnimationStrategy.md) | gui | 34 |
| [gui/ExportNetRotationAnimationStrategy](ExportNetRotationAnimationStrategy.md) | gui | 30 |
| [qt-widgets/ConfigureExportParametersDialog](../qt-widgets/ConfigureExportParametersDialog.md) | qt-widgets | 30 |
| [qt-widgets/ExportAnimationDialog](../qt-widgets/ExportAnimationDialog.md) | qt-widgets | 26 |
| [gui/ExportDeformationAnimationStrategy](ExportDeformationAnimationStrategy.md) | gui | 24 |
| [gui/ExportScalarCoverageAnimationStrategy](ExportScalarCoverageAnimationStrategy.md) | gui | 24 |
| [gui/ExportRasterAnimationStrategy](ExportRasterAnimationStrategy.md) | gui | 22 |
| [qt-widgets/EditExportParametersDialog](../qt-widgets/EditExportParametersDialog.md) | qt-widgets | 21 |
| [gui/ExportCitcomsResolvedTopologyAnimationStrategy](ExportCitcomsResolvedTopologyAnimationStrategy.md) | gui | 20 |
| [gui/ExportFlowlineAnimationStrategy](ExportFlowlineAnimationStrategy.md) | gui | 20 |
| [gui/ExportMotionPathAnimationStrategy](ExportMotionPathAnimationStrategy.md) | gui | 20 |
| [gui/ExportReconstructedGeometryAnimationStrategy](ExportReconstructedGeometryAnimationStrategy.md) | gui | 20 |
| [gui/ExportResolvedTopologyAnimationStrategy](ExportResolvedTopologyAnimationStrategy.md) | gui | 20 |
| [gui/ExportImageAnimationStrategy](ExportImageAnimationStrategy.md) | gui | 16 |
| [gui/ExportSvgAnimationStrategy](ExportSvgAnimationStrategy.md) | gui | 16 |
| [gui/ExportCoRegistrationAnimationStrategy](ExportCoRegistrationAnimationStrategy.md) | gui | 13 |
| [gui/ExportStageRotationAnimationStrategy](ExportStageRotationAnimationStrategy.md) | gui | 12 |
| [gui/ExportTotalRotationAnimationStrategy](ExportTotalRotationAnimationStrategy.md) | gui | 12 |
| [gui/ExportAnimationContext](ExportAnimationContext.md) | gui | 11 |

*... and 15 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportAnimationStrategy.h
python scripts/gpq.py def GPlatesGui::ExportAnimationStrategy --body
python scripts/gpq.py uses ExportAnimationStrategy --kind class
python scripts/gpq.py hier ExportAnimationStrategy
```

# ExportScalarCoverageAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 585 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportScalarCoverageAnimationStrategy.h` | C++ | 265 |
| `src/gui/ExportScalarCoverageAnimationStrategy.cc` | C++ | 310 |

## Overview

`ExportScalarCoverageAnimationStrategy` writes reconstructed scalar coverages (per-point scalar values attached to reconstructed geometries, such as crustal thickness or strain) to file at each animation frame, in either `GPML` or `GMT` format. Unlike the sibling export strategies, its `Configuration` is abstract for the shared fields (file options, and whether to include dilatation strain, dilatation strain rate and the second invariant of strain rate); callers must actually construct one of the two subclasses, `GpmlConfiguration` or `GMTConfiguration` — the latter adding a `DomainPointFormatType` for whether domain points are written lon/lat or lat/lon — matching the `file_format` they set.

`do_export_iteration` collects the currently visible `GPlatesAppLogic::ReconstructedScalarCoverage` objects via `populate_visible_reconstructed_scalar_coverage_seq`, `dynamic_cast`s the configuration to the subclass matching `file_format`, and forwards to `GPlatesFileIO::ReconstructedScalarCoverageExport::export_reconstructed_scalar_coverages_to_gpml_format` or `..._to_gmt_format` accordingly.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::reconstructed_scalar_coverage_seq_type`](#anonymousreconstructed_scalar_coverage_seq_type) | typedef | — | — | 0 | Typedef for a sequence of ReconstructedScalarCoverage pointers. |
| [`GPlatesGui::ExportScalarCoverageAnimationStrategy`](#gplatesguiexportscalarcoverageanimationstrategy) | class | [`GPlatesGui::ExportAnimationStrategy`](ExportAnimationStrategy.md) | — | 0 | Concrete implementation of the ExportAnimationStrategy class for writing scalar coverages. |

## Members

### `(anonymous)::reconstructed_scalar_coverage_seq_type`

*None.*

### `GPlatesGui::ExportScalarCoverageAnimationStrategy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportScalarCoverageAnimationStrategy>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportScalarCoverageAnimationStrategy\>. |
| `Configuration` | class | `None` | public | Configuration options. |
| `const_configuration_ptr` | typedef | `boost::shared_ptr<const Configuration>` | public | Typedef for a shared pointer to const Configuration. |
| `configuration_ptr` | typedef | `boost::shared_ptr<Configuration>` | public | Typedef for a shared pointer to Configuration. |
| `GpmlConfiguration` | class | `None` | public | GPML format configuration options. |
| `GMTConfiguration` | class | `None` | public | GMT format configuration options. |
| `create( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | method | `non_null_ptr_type` | public | — |
| `~ExportScalarCoverageAnimationStrategy()` | destructor | `None` | public | — |
| `do_export_iteration( std::size_t frame_index)` | method | `bool` | public | Does one frame of export. |
| `wrap_up( bool export_successful)` | method | `void` | public | Allows Strategy objects to do any housekeeping that might be necessary after all export iterations are completed. false if there was any kind of interruption. |
| `set_template_filename( const QString &)` | method | `void` | public | — |
| `ExportScalarCoverageAnimationStrategy( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | constructor | `None` | protected | Protected constructor to prevent instantiation on the stack. |
| `d_loaded_files` | field | `GPlatesViewOperations::VisibleReconstructionGeometryExport::files_collection_type` | private | The list of currently loaded files that are active. |
| `d_configuration` | field | `const_configuration_ptr` | private | Export configuration parameters. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_visible_reconstruct_scalar_coverage_visual_layers( std::vector< boost::shared_ptr<const GPlatesPresentation::VisualLayer> > &visible_reconstruct_scalar_coverage_visual_layers, const GPlatesPresentation::ViewState &view_state)` | function | `void` | Get the visible scalar coverage visual layers. |
| `get_visible_reconstruct_scalar_coverage_layer_proxies( std::vector<GPlatesAppLogic::ReconstructScalarCoverageLayerProxy::non_null_ptr_type> &visible_reconstruct_scalar_coverage_outputs, const GPlatesPresentation::ViewState &view_state)` | function | `void` | — |
| `get_reconstructed_scalar_coverage_seq( reconstructed_scalar_coverage_seq_type &reconstructed_scalar_coverage_seq, const std::vector<GPlatesAppLogic::ReconstructedScalarCoverage::non_null_ptr_type> &reconstructed_scalar_coverages)` | function | `void` | — |
| `populate_visible_reconstructed_scalar_coverage_seq( reconstructed_scalar_coverage_seq_type &reconstructed_scalar_coverage_seq, const GPlatesPresentation::ViewState &view_state)` | function | `void` | — |
| `GPLATES_GUI_EXPORTSCALARCOVERAGEANIMATIONSTRATEGY_H` | macro | `None` | — |

## Notes

`d_configuration->file_format` must agree with the runtime type of the `Configuration` object passed in: `do_export_iteration` `dynamic_cast`s to `GpmlConfiguration` for `GPML` and to `GMTConfiguration` for `GMT`, and a mismatch throws `std::bad_cast`. `wrap_up` is currently a no-op placeholder for any finishing step a future export format might need.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportScalarCoverageOptionsWidget](../qt-widgets/ExportScalarCoverageOptionsWidget.md) | qt-widgets | 71 |
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 10 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportScalarCoverageAnimationStrategy.h
python scripts/gpq.py def GPlatesGui::ExportScalarCoverageAnimationStrategy --body
python scripts/gpq.py uses ExportScalarCoverageAnimationStrategy --kind class
python scripts/gpq.py hier ExportScalarCoverageAnimationStrategy
```

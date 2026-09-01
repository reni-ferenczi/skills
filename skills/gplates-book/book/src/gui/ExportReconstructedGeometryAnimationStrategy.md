# ExportReconstructedGeometryAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1433 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportReconstructedGeometryAnimationStrategy.h` | C++ | 163 |
| `src/gui/ExportReconstructedGeometryAnimationStrategy.cc` | C++ | 156 |

## Overview

`ExportReconstructedGeometryAnimationStrategy` is the concrete `ExportAnimationStrategy` that writes reconstructed feature geometries (RFGs) to file at each animation frame, in one of `SHAPEFILE`, `OGRGMT`, `GMT` or `GEOJSON` format. Its `Configuration` reuses `ExportOptionsUtils::ExportFileOptions` for the single-file/multiple-file/per-directory choices, and adds `wrap_to_dateline` for geometries that cross the antimeridian.

At construction it snapshots two file lists from the current `GPlatesAppLogic::ApplicationState`: every currently loaded feature collection file (`d_loaded_files`), and the input files feeding the active `RECONSTRUCTION`-type layers in the `ReconstructGraph` (`d_loaded_reconstruction_files`). `do_export_iteration` passes these lists, along with the current rendered geometry collection, anchored plate id and view time, straight through to `GPlatesViewOperations::VisibleReconstructionGeometryExport::export_visible_reconstructed_feature_geometries`, which does the actual geometry extraction and file writing.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ExportReconstructedGeometryAnimationStrategy`](#gplatesguiexportreconstructedgeometryanimationstrategy) | class | [`GPlatesGui::ExportAnimationStrategy`](ExportAnimationStrategy.md) | — | 0 | Concrete implementation of the ExportAnimationStrategy class for writing reconstructed feature geometries at each timestep. |

## Members

### `GPlatesGui::ExportReconstructedGeometryAnimationStrategy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportReconstructedGeometryAnimationStrategy>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportReconstructedGeometryAnimationStrategy\>. |
| `Configuration` | class | `None` | public | Configuration options. |
| `const_configuration_ptr` | typedef | `boost::shared_ptr<const Configuration>` | public | Typedef for a shared pointer to const Configuration. |
| `create( ExportAnimationContext &export_animation_context, const const_configuration_ptr &cfg)` | method | `non_null_ptr_type` | public | — |
| `~ExportReconstructedGeometryAnimationStrategy()` | destructor | `None` | public | — |
| `do_export_iteration( std::size_t frame_index)` | method | `bool` | public | Does one frame of export. |
| `ExportReconstructedGeometryAnimationStrategy( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &cfg)` | constructor | `None` | protected | Protected constructor to prevent instantiation on the stack. |
| `d_loaded_files` | field | `GPlatesViewOperations::VisibleReconstructionGeometryExport::files_collection_type` | private | The list of currently loaded files. |
| `d_loaded_reconstruction_files` | field | `GPlatesViewOperations::VisibleReconstructionGeometryExport::files_collection_type` | private | — |
| `d_configuration` | field | `const_configuration_ptr` | private | Export configuration parameters. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_EXPORTRECONSTRUCTEDGEOMETRYANIMATIONSTRATEGY_H` | macro | `None` | — |

## Notes

`d_loaded_files` and `d_loaded_reconstruction_files` are captured once, in the constructor, from the file state at strategy-creation time; files loaded or unloaded after that are not reflected in later frames of the same export run.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 21 |
| [qt-widgets/ExportReconstructedGeometryOptionsWidget](../qt-widgets/ExportReconstructedGeometryOptionsWidget.md) | qt-widgets | 15 |
| [gui/ExportAnimationContext](ExportAnimationContext.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportReconstructedGeometryAnimationStrategy.h
python scripts/gpq.py def GPlatesGui::ExportReconstructedGeometryAnimationStrategy --body
python scripts/gpq.py uses ExportReconstructedGeometryAnimationStrategy --kind class
python scripts/gpq.py hier ExportReconstructedGeometryAnimationStrategy
```

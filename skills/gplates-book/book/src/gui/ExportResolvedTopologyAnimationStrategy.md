# ExportResolvedTopologyAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 48 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportResolvedTopologyAnimationStrategy.h` | C++ | 180 |
| `src/gui/ExportResolvedTopologyAnimationStrategy.cc` | C++ | 168 |

## Overview

`ExportResolvedTopologyAnimationStrategy` writes resolved topological geometries — lines, polygons, networks and (optionally) their boundary sub-segments — to file at each animation frame, in a general format rather than the CitcomS-specific one used elsewhere. Its `Configuration` mirrors `ExportReconstructedGeometryAnimationStrategy`'s file-format and `ExportOptionsUtils::ExportFileOptions` fields, and adds independent toggles for exporting topological lines, polygons, networks, sections and line sub-segments, plus an optional forced `GPlatesMaths::PolygonOrientation` that applies only when polygons or networks are exported.

Like its reconstructed-geometry counterpart, the constructor snapshots the currently loaded feature collection files and the input files of the active reconstruction layers into `d_loaded_files` and `d_loaded_reconstruction_files`; `do_export_iteration` passes these, together with the configuration flags, to `GPlatesViewOperations::VisibleReconstructionGeometryExport::export_visible_resolved_topologies`, which resolves and writes the topologies for the current frame.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ExportResolvedTopologyAnimationStrategy`](#gplatesguiexportresolvedtopologyanimationstrategy) | class | [`GPlatesGui::ExportAnimationStrategy`](ExportAnimationStrategy.md) | — | 0 | Concrete implementation of the ExportAnimationStrategy class for exporting resolved topologies in a general manner (as opposed to the CitcomS-specific manner). |

## Members

### `GPlatesGui::ExportResolvedTopologyAnimationStrategy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportResolvedTopologyAnimationStrategy>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportResolvedTopologyAnimationStrategy\>. |
| `Configuration` | class | `None` | public | Configuration options. |
| `const_configuration_ptr` | typedef | `boost::shared_ptr<const Configuration>` | public | Typedef for a shared pointer to const Configuration. |
| `create( ExportAnimationContext &export_animation_context, const const_configuration_ptr &cfg)` | method | `non_null_ptr_type` | public | — |
| `~ExportResolvedTopologyAnimationStrategy()` | destructor | `None` | public | — |
| `do_export_iteration( std::size_t frame_index)` | method | `bool` | public | Does one frame of export. |
| `ExportResolvedTopologyAnimationStrategy( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &cfg)` | constructor | `None` | protected | Protected constructor to prevent instantiation on the stack. |
| `d_loaded_files` | field | `GPlatesViewOperations::VisibleReconstructionGeometryExport::files_collection_type` | private | The list of currently loaded files. |
| `d_loaded_reconstruction_files` | field | `GPlatesViewOperations::VisibleReconstructionGeometryExport::files_collection_type` | private | The active and loaded reconstruction file(s) used in the reconstruction. |
| `d_configuration` | field | `const_configuration_ptr` | private | Export configuration parameters. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_EXPORTRESOLVEDTOPOLOGYANIMATIONSTRATEGY_H` | macro | `None` | — |

## Notes

`Configuration::force_polygon_orientation` is only consulted when `export_topological_polygons` or `export_topological_networks` is true; otherwise it has no effect. As with `ExportReconstructedGeometryAnimationStrategy`, the loaded-file lists are captured once at construction and do not track files loaded or unloaded mid-export.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportResolvedTopologyOptionsWidget](../qt-widgets/ExportResolvedTopologyOptionsWidget.md) | qt-widgets | 46 |
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 21 |
| [file-io/GMTFormatResolvedTopologicalGeometryExport](../file-io/GMTFormatResolvedTopologicalGeometryExport.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportResolvedTopologyAnimationStrategy.h
python scripts/gpq.py def GPlatesGui::ExportResolvedTopologyAnimationStrategy --body
python scripts/gpq.py uses ExportResolvedTopologyAnimationStrategy --kind class
python scripts/gpq.py hier ExportResolvedTopologyAnimationStrategy
```

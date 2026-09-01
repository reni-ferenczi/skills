# ExportCitcomsResolvedTopologyAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 251 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportCitcomsResolvedTopologyAnimationStrategy.h` | C++ | 206 |
| `src/gui/ExportCitcomsResolvedTopologyAnimationStrategy.cc` | C++ | 268 |

## Overview

`ExportCitcomsResolvedTopologyAnimationStrategy` is the concrete `ExportAnimationStrategy` that writes resolved topological boundaries and networks in the file layout expected by the external CitcomS workflow, as opposed to the general-purpose `ExportResolvedTopologyAnimationStrategy`. It plays the Strategy role from Gamma et al. under `ExportAnimationContext`, which drives it one `do_export_iteration()` call per animation frame.

At construction it snapshots the currently loaded feature collection files and, separately, the input files feeding any active `RECONSTRUCTION`-type layer in the `ReconstructGraph`, since the CitcomS export format records both sets. Each `do_export_iteration()` call collects the `ResolvedTopologicalBoundary` and `ResolvedTopologicalNetwork` objects currently visible in the `RenderedGeometryCollection` and hands them, together with the snapshotted file lists and the current anchored plate ID, to `GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExport::export_resolved_topological_boundaries()`, which does the actual file writing.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ExportCitcomsResolvedTopologyAnimationStrategy`](#gplatesguiexportcitcomsresolvedtopologyanimationstrategy) | class | [`GPlatesGui::ExportAnimationStrategy`](ExportAnimationStrategy.md) | — | 0 | Concrete implementation of the ExportAnimationStrategy class for exporting resolved topologies in a CitcomS-specific manner. |

## Members

### `GPlatesGui::ExportCitcomsResolvedTopologyAnimationStrategy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportCitcomsResolvedTopologyAnimationStrategy>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportCitcomsResolvedTopologyAnimationStrategy\>. |
| `const_configuration_ptr` | typedef | `boost::shared_ptr<const Configuration>` | public | Typedef for a shared pointer to const Configuration. |
| `configuration_ptr` | typedef | `boost::shared_ptr<Configuration>` | public | Typedef for a shared pointer to Configuration. |
| `Configuration` | class | `None` | public | Configuration options.. |
| `create( ExportAnimationContext &export_animation_context, const const_configuration_ptr &cfg)` | method | `non_null_ptr_type` | public | Creates an export animation strategy. |
| `~ExportCitcomsResolvedTopologyAnimationStrategy()` | destructor | `None` | public | — |
| `set_template_filename( const QString &filename)` | method | `void` | public | Sets the internal ExportTemplateFilenameSequence. |
| `do_export_iteration( std::size_t frame_index)` | method | `bool` | public | Does one frame of export. |
| `wrap_up( bool export_successful)` | method | `void` | public | Allows Strategy objects to do any housekeeping that might be necessary after all export iterations are completed. false if there was any kind of interruption. |
| `ExportCitcomsResolvedTopologyAnimationStrategy( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &cfg)` | constructor | `None` | protected | Protected constructor to prevent instantiation on the stack. |
| `resolved_geom_seq_type` | typedef | `std::vector<const GPlatesAppLogic::ReconstructionGeometry *>` | private | Typedef for a sequence of resolved topological geometries. |
| `d_loaded_files` | field | `std::vector<const GPlatesFileIO::File::Reference *>` | private | The list of currently loaded files. |
| `d_loaded_reconstruction_files` | field | `std::vector<const GPlatesFileIO::File::Reference *>` | private | The active and loaded reconstruction file(s) used in the reconstruction. |
| `d_configuration` | field | `const_configuration_ptr` | private | Export configuration parameters. |
| `export_files( const resolved_geom_seq_type &resolved_geom_seq, const double &recon_time, const QString &filebasename)` | method | `void` | private | Export to the various files. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_EXPORTCITCOMSRESOLVEDTOPOLOGYSTRATEGY_H` | macro | `None` | — |

## Notes

The list of loaded files and reconstruction input files is captured once, in the constructor; it is not refreshed between frames, so files loaded or unloaded mid-animation will not be reflected in the exported metadata. `do_export_iteration()` catches `std::exception` and all other exceptions around the actual export call and reports failure through the return value rather than propagating, so `ExportAnimationContext` can continue or abort the batch cleanly.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 71 |
| [qt-widgets/ExportCitcomsResolvedTopologyOptionsWidget](../qt-widgets/ExportCitcomsResolvedTopologyOptionsWidget.md) | qt-widgets | 44 |
| [gui/ExportAnimationContext](ExportAnimationContext.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportCitcomsResolvedTopologyAnimationStrategy.h
python scripts/gpq.py def GPlatesGui::ExportCitcomsResolvedTopologyAnimationStrategy --body
python scripts/gpq.py uses ExportCitcomsResolvedTopologyAnimationStrategy --kind class
python scripts/gpq.py hier ExportCitcomsResolvedTopologyAnimationStrategy
```

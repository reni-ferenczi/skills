# ExportFlowlineAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1321 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportFlowlineAnimationStrategy.h` | C++ | 196 |
| `src/gui/ExportFlowlineAnimationStrategy.cc` | C++ | 198 |

## Overview

`ExportFlowlineAnimationStrategy` is the `ExportAnimationStrategy` (Gamma et al. Strategy role, driven by `ExportAnimationContext`) that writes flowline geometries per animation frame, in GMT, shapefile, OGR-GMT or GeoJSON format according to `Configuration::file_format`. Like the sibling reconstructed-geometry and CitcomS strategies it snapshots, in its constructor, both the currently loaded feature collection files and the input files feeding any active `RECONSTRUCTION`-type layer, for inclusion in the exported output's metadata.

The anonymous-namespace helpers `substitute_placeholder()` and `calculate_output_basename()` build each frame's output filename by substituting the loaded flowlines feature collection's filename into the export template's `%P` placeholder, so a single template can fan out into one file per source flowlines file.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ExportFlowlineAnimationStrategy`](#gplatesguiexportflowlineanimationstrategy) | class | [`GPlatesGui::ExportAnimationStrategy`](ExportAnimationStrategy.md) | — | 0 | Concrete implementation of the ExportAnimationStrategy class for writing plate velocity meshes. |

## Members

### `GPlatesGui::ExportFlowlineAnimationStrategy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportFlowlineAnimationStrategy>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportFlowlinesAnimationStrategy\>. |
| `Configuration` | class | `None` | public | Configuration options. |
| `const_configuration_ptr` | typedef | `boost::shared_ptr<const Configuration>` | public | Typedef for a shared pointer to const Configuration. |
| `create( ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | method | `non_null_ptr_type` | public | — |
| `~ExportFlowlineAnimationStrategy()` | destructor | `None` | public | — |
| `do_export_iteration( std::size_t frame_index)` | method | `bool` | public | Does one frame of export. |
| `wrap_up( bool export_successful)` | method | `void` | public | Allows Strategy objects to do any housekeeping that might be necessary after all export iterations are completed. false if there was any kind of interruption. |
| `set_template_filename( const QString &)` | method | `void` | public | — |
| `ExportFlowlineAnimationStrategy( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | constructor | `None` | protected | Protected constructor to prevent instantiation on the stack. |
| `files_collection_type` | typedef | `std::vector<const GPlatesFileIO::File::Reference *>` | private | For storing files referenced in the current reconstruction. |
| `d_loaded_files` | field | `files_collection_type` | private | The reconstruction file(s) used to create this reconstruction. |
| `d_loaded_reconstruction_files` | field | `files_collection_type` | private | The active and loaded reconstruction file(s) used in the reconstruction. |
| `d_configuration` | field | `const_configuration_ptr` | private | Export configuration parameters. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `substitute_placeholder( const QString &output_filebasename, const QString &placeholder, const QString &placeholder_replacement)` | function | `QString` | — |
| `calculate_output_basename( const QString &output_filename, const QString &flowlines_filename)` | function | `QString` | — |
| `GPLATES_GUI_EXPORTFLOWLINEANIMATIONSTRATEGY_H` | macro | `None` | — |

## Notes

The class's own Doxygen comment ("writing plate velocity meshes") is stale — the code exports flowlines, not velocity meshes.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 21 |
| [qt-widgets/ExportFlowlineOptionsWidget](../qt-widgets/ExportFlowlineOptionsWidget.md) | qt-widgets | 13 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportFlowlineAnimationStrategy.h
python scripts/gpq.py def GPlatesGui::ExportFlowlineAnimationStrategy --body
python scripts/gpq.py uses ExportFlowlineAnimationStrategy --kind class
python scripts/gpq.py hier ExportFlowlineAnimationStrategy
```

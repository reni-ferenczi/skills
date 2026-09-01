# ExportMotionPathAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1322 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportMotionPathAnimationStrategy.h` | C++ | 196 |
| `src/gui/ExportMotionPathAnimationStrategy.cc` | C++ | 199 |

## Overview

`ExportMotionPathAnimationStrategy` is the `ExportAnimationStrategy` (Gamma et al. Strategy role, driven by `ExportAnimationContext`) that writes motion path geometries per animation frame, in GMT, shapefile, OGR-GMT or GeoJSON format according to `Configuration::file_format`. It is structured identically to `ExportFlowlineAnimationStrategy` — same constructor logic for snapshotting loaded feature-collection files and active reconstruction input files, same `substitute_placeholder()`/`calculate_output_basename()` filename-templating helpers — with motion paths substituted for flowlines as the exported geometry type.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ExportMotionPathAnimationStrategy`](#gplatesguiexportmotionpathanimationstrategy) | class | [`GPlatesGui::ExportAnimationStrategy`](ExportAnimationStrategy.md) | — | 0 | Concrete implementation of the ExportAnimationStrategy class for writing plate velocity meshes. |

## Members

### `GPlatesGui::ExportMotionPathAnimationStrategy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportMotionPathAnimationStrategy>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportMotionPathsAnimationStrategy\>. |
| `Configuration` | class | `None` | public | Configuration options. |
| `const_configuration_ptr` | typedef | `boost::shared_ptr<const Configuration>` | public | Typedef for a shared pointer to const Configuration. |
| `create( ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | method | `non_null_ptr_type` | public | — |
| `~ExportMotionPathAnimationStrategy()` | destructor | `None` | public | — |
| `do_export_iteration( std::size_t frame_index)` | method | `bool` | public | Does one frame of export. |
| `wrap_up( bool export_successful)` | method | `void` | public | Allows Strategy objects to do any housekeeping that might be necessary after all export iterations are completed. false if there was any kind of interruption. |
| `set_template_filename( const QString &)` | method | `void` | public | — |
| `ExportMotionPathAnimationStrategy( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | constructor | `None` | protected | Protected constructor to prevent instantiation on the stack. |
| `files_collection_type` | typedef | `std::vector<const GPlatesFileIO::File::Reference *>` | private | For storing files referenced in the current reconstruction. |
| `d_loaded_files` | field | `files_collection_type` | private | The reconstruction file(s) used to create this reconstruction. |
| `d_loaded_reconstruction_files` | field | `files_collection_type` | private | The active and loaded reconstruction file(s) used in the reconstruction. |
| `d_configuration` | field | `const_configuration_ptr` | private | Export configuration parameters. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `substitute_placeholder( const QString &output_filebasename, const QString &placeholder, const QString &placeholder_replacement)` | function | `QString` | — |
| `calculate_output_basename( const QString &output_filename, const QString &flowlines_filename)` | function | `QString` | — |
| `GPLATES_GUI_EXPORTMOTIONPATHANIMATIONSTRATEGY_H` | macro | `None` | — |

## Notes

The class's own Doxygen comment ("writing plate velocity meshes") is stale, copy-pasted from another export strategy — the code exports motion paths, not velocity meshes.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 21 |
| [qt-widgets/ExportMotionPathOptionsWidget](../qt-widgets/ExportMotionPathOptionsWidget.md) | qt-widgets | 13 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportMotionPathAnimationStrategy.h
python scripts/gpq.py def GPlatesGui::ExportMotionPathAnimationStrategy --body
python scripts/gpq.py uses ExportMotionPathAnimationStrategy --kind class
python scripts/gpq.py hier ExportMotionPathAnimationStrategy
```

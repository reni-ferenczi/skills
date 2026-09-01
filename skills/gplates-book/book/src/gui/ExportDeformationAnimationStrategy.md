# ExportDeformationAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 110 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportDeformationAnimationStrategy.h` | C++ | 289 |
| `src/gui/ExportDeformationAnimationStrategy.cc` | C++ | 316 |

## Overview

[[[PROSE overview unit=gui/ExportDeformationAnimationStrategy tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::deformed_feature_geometry_seq_type`](#anonymousdeformed_feature_geometry_seq_type) | typedef | — | — | 0 | Typedef for a sequence of TopologyReconstructedFeatureGeometry pointers. |
| [`GPlatesGui::ExportDeformationAnimationStrategy`](#gplatesguiexportdeformationanimationstrategy) | class | [`GPlatesGui::ExportAnimationStrategy`](ExportAnimationStrategy.md) | — | 0 | Concrete implementation of the ExportAnimationStrategy class for writing deformation. |

## Members

### `(anonymous)::deformed_feature_geometry_seq_type`

*None.*

### `GPlatesGui::ExportDeformationAnimationStrategy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportDeformationAnimationStrategy>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportDeformationAnimationStrategy\>. |
| `Configuration` | class | `None` | public | Configuration options. |
| `const_configuration_ptr` | typedef | `boost::shared_ptr<const Configuration>` | public | Typedef for a shared pointer to const Configuration. |
| `configuration_ptr` | typedef | `boost::shared_ptr<Configuration>` | public | Typedef for a shared pointer to Configuration. |
| `GpmlConfiguration` | class | `None` | public | GPML format configuration options. |
| `GMTConfiguration` | class | `None` | public | GMT format configuration options. |
| `create( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | method | `non_null_ptr_type` | public | — |
| `~ExportDeformationAnimationStrategy()` | destructor | `None` | public | — |
| `do_export_iteration( std::size_t frame_index)` | method | `bool` | public | Does one frame of export. |
| `wrap_up( bool export_successful)` | method | `void` | public | Allows Strategy objects to do any housekeeping that might be necessary after all export iterations are completed. false if there was any kind of interruption. |
| `set_template_filename( const QString &)` | method | `void` | public | — |
| `ExportDeformationAnimationStrategy( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | constructor | `None` | protected | Protected constructor to prevent instantiation on the stack. |
| `d_loaded_files` | field | `GPlatesViewOperations::VisibleReconstructionGeometryExport::files_collection_type` | private | The list of currently loaded files that are active. |
| `d_configuration` | field | `const_configuration_ptr` | private | Export configuration parameters. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_visible_reconstruct_visual_layers( std::vector< boost::shared_ptr<const GPlatesPresentation::VisualLayer> > &visible_reconstruct_visual_layers, const GPlatesPresentation::ViewState &view_state)` | function | `void` | Get the visible reconstruct visual layers. |
| `get_visible_reconstruct_layer_proxies( std::vector<GPlatesAppLogic::ReconstructLayerProxy::non_null_ptr_type> &visible_reconstruct_outputs, const GPlatesPresentation::ViewState &view_state)` | function | `void` | — |
| `populate_visible_deformed_feature_geometry_seq( deformed_feature_geometry_seq_type &deformed_feature_geometry_seq, const GPlatesPresentation::ViewState &view_state)` | function | `void` | — |
| `GPLATES_GUI_EXPORTDEFORMATIONANIMATIONSTRATEGY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/ExportDeformationAnimationStrategy tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportDeformationOptionsWidget](../qt-widgets/ExportDeformationOptionsWidget.md) | qt-widgets | 91 |
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 22 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportDeformationAnimationStrategy.h
python scripts/gpq.py def GPlatesGui::ExportDeformationAnimationStrategy --body
python scripts/gpq.py uses ExportDeformationAnimationStrategy --kind class
python scripts/gpq.py hier ExportDeformationAnimationStrategy
```

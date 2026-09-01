# ExportVelocityAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 85 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportVelocityAnimationStrategy.h` | C++ | 358 |
| `src/gui/ExportVelocityAnimationStrategy.cc` | C++ | 403 |

## Overview

`ExportVelocityAnimationStrategy` is the concrete `ExportAnimationStrategy` for writing velocity mesh output during an animation export, playing the concrete Strategy role from Gamma et al. against `ExportAnimationContext`. Each animation frame, `do_export_iteration` gathers the visible `VELOCITY_FIELD_CALCULATOR` layers from `GPlatesPresentation::VisualLayers`, pulls their `VelocityFieldCalculatorLayerProxy` output as `MultiPointVectorField` objects (overriding delta-time and boundary-smoothing parameters from the export options), and dispatches to one of four `GPlatesFileIO::MultiPointVectorFieldExport` functions chosen by `Configuration::file_format`.

The nested `Configuration` hierarchy (`GpmlConfiguration`, `GMTConfiguration`, `TerraTextConfiguration`, `CitcomsGlobalConfiguration`) captures the per-format export options as immutable, cloneable value objects handed in at construction; `TerraTextConfiguration` and `CitcomsGlobalConfiguration` additionally expose static placeholder tokens (`%MT`, `%NT`, `%ND`, `%NP`, `%D`, `%C`) used to pattern-match parameters embedded in Terra and CitcomS velocity-domain grid filenames.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::vector_field_seq_type`](#anonymousvector_field_seq_type) | typedef | — | — | 0 | Typedef for a sequence of MultiPointVectorField pointers. |
| [`GPlatesGui::ExportVelocityAnimationStrategy`](#gplatesguiexportvelocityanimationstrategy) | class | [`GPlatesGui::ExportAnimationStrategy`](ExportAnimationStrategy.md) | — | 0 | Concrete implementation of the ExportAnimationStrategy class for writing plate velocity meshes. |

## Members

### `(anonymous)::vector_field_seq_type`

*None.*

### `GPlatesGui::ExportVelocityAnimationStrategy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportVelocityAnimationStrategy>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportVelocityAnimationStrategy\>. |
| `Configuration` | class | `None` | public | Configuration options. |
| `const_configuration_ptr` | typedef | `boost::shared_ptr<const Configuration>` | public | Typedef for a shared pointer to const Configuration. |
| `configuration_ptr` | typedef | `boost::shared_ptr<Configuration>` | public | Typedef for a shared pointer to Configuration. |
| `GpmlConfiguration` | class | `None` | public | GPML format configuration options. |
| `GMTConfiguration` | class | `None` | public | GMT format configuration options. |
| `TerraTextConfiguration` | class | `None` | public | Terra text format configuration options. |
| `CitcomsGlobalConfiguration` | class | `None` | public | CitcomS global format configuration options. |
| `create( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | method | `non_null_ptr_type` | public | — |
| `~ExportVelocityAnimationStrategy()` | destructor | `None` | public | — |
| `do_export_iteration( std::size_t frame_index)` | method | `bool` | public | Does one frame of export. |
| `wrap_up( bool export_successful)` | method | `void` | public | Allows Strategy objects to do any housekeeping that might be necessary after all export iterations are completed. false if there was any kind of interruption. |
| `set_template_filename( const QString &)` | method | `void` | public | — |
| `vector_field_seq_type` | typedef | `std::vector<const GPlatesAppLogic::MultiPointVectorField *>` | protected | — |
| `ExportVelocityAnimationStrategy( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | constructor | `None` | protected | Protected constructor to prevent instantiation on the stack. |
| `d_loaded_files` | field | `GPlatesViewOperations::VisibleReconstructionGeometryExport::files_collection_type` | private | The list of currently loaded files that are active. |
| `d_configuration` | field | `const_configuration_ptr` | private | Export configuration parameters. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_velocity_field_calculator_visual_layers( std::vector< boost::shared_ptr<const GPlatesPresentation::VisualLayer> > &velocity_field_calculator_visual_layers, const GPlatesPresentation::ViewState &view_state)` | function | `void` | Get the velocity visual layers. |
| `get_velocity_field_calculator_layer_proxies( std::vector<GPlatesAppLogic::VelocityFieldCalculatorLayerProxy::non_null_ptr_type> &velocity_field_outputs, const GPlatesPresentation::ViewState &view_state)` | function | `void` | — |
| `get_vector_field_seq( vector_field_seq_type &vector_field_seq, const std::vector<GPlatesAppLogic::MultiPointVectorField::non_null_ptr_type> &multi_point_velocity_fields)` | function | `void` | — |
| `populate_vector_field_seq( vector_field_seq_type &vector_field_seq, const GPlatesPresentation::ViewState &view_state, const GPlatesGui::ExportOptionsUtils::ExportVelocityCalculationOptions &velocity_calculation_options)` | function | `void` | — |
| `MT_PLACE_HOLDER` | variable | `QString` | — |
| `NT_PLACE_HOLDER` | variable | `QString` | — |
| `ND_PLACE_HOLDER` | variable | `QString` | — |
| `PROCESSOR_PLACE_HOLDER` | variable | `QString` | — |
| `DENSITY_PLACE_HOLDER` | variable | `QString` | — |
| `CAP_NUM_PLACE_HOLDER` | variable | `QString` | — |
| `GPLATES_GUI_EXPORTVELOCITYANIMATIONSTRATEGY_H` | macro | `None` | — |

## Notes

- Construction is protected; instances are created only through the per-`Configuration`-subclass `create()` factory, which returns a `non_null_ptr_type`, matching the pattern used by sibling `ExportAnimationStrategy` subclasses.
- All visual layers of type `VELOCITY_FIELD_CALCULATOR` are exported regardless of visibility — a deliberate compatibility choice with GPlates 1.5, noted in the code as something a future per-export layer-selection UI should revisit.
- `d_loaded_files` and the general export-file bookkeeping are copied from `ExportReconstructedGeometryAnimationStrategy.h`, so the two strategies should be kept in sync if that logic changes.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportVelocityOptionsWidget](../qt-widgets/ExportVelocityOptionsWidget.md) | qt-widgets | 237 |
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 38 |
| [gui/ExportAnimationContext](ExportAnimationContext.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportVelocityAnimationStrategy.h
python scripts/gpq.py def GPlatesGui::ExportVelocityAnimationStrategy --body
python scripts/gpq.py uses ExportVelocityAnimationStrategy --kind class
python scripts/gpq.py hier ExportVelocityAnimationStrategy
```

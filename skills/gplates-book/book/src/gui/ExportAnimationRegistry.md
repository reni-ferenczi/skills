# ExportAnimationRegistry

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 112 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportAnimationRegistry.h` | C++ | 264 |
| `src/gui/ExportAnimationRegistry.cc` | C++ | 1962 |

## Overview

`ExportAnimationRegistry` is a type-erased factory table that decouples the export-animation UI from the many concrete `ExportAnimationStrategy` subclasses (reconstructed geometries, rasters, rotations, velocities, topologies, and so on). For each `ExportAnimationType::ExportID` it stores a default configuration plus three `boost::function` callbacks — one to create the strategy, one to create its `GPlatesQtWidgets::ExportOptionsWidget`, and one to validate a filename template — so that dialog code such as `qt-widgets/ConfigureExportParametersDialog` can enumerate and drive every exporter through one interface without depending on any of their headers.

The `.cc` file supplies the registration side: a `create_animation_strategy<ExportAnimationStrategyType>()` template wraps each strategy's static `create()` in the common function signature, and `dynamic_cast_export_configuration<>()` recovers the concrete configuration type from the stored `const_configuration_base_ptr` inside each strategy's own creation callback. `register_default_export_animation_types()` is the single entry point called at startup; it just delegates, one call per export category, to the per-category `register_default_export_*_animation_types()` free functions that actually call `register_exporter()` with the strategy- and widget-specific callbacks bound via `boost::bind`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ExportAnimationRegistry`](#gplatesguiexportanimationregistry) | class | `boost::noncopyable` | — | 0 | Stores information required to create ExportAnimationStrategy objects. |

## Members

### `GPlatesGui::ExportAnimationRegistry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create_export_animation_strategy_function_signature_type` | typedef | `ExportAnimationStrategy::non_null_ptr_type` | public | Convenience typedef for a function that creates a ExportAnimationStrategy. |
| `create_export_animation_strategy_function_type` | typedef | `boost::function<create_export_animation_strategy_function_signature_type>` | public | The boost::function typedef that creates a ExportAnimationStrategy. |
| `create_export_options_widget_function_signature_type` | typedef | `GPlatesQtWidgets::ExportOptionsWidget` | public | Convenience typedef for a function that creates a ExportOptionsWidget. |
| `create_export_options_widget_function_type` | typedef | `boost::function<create_export_options_widget_function_signature_type>` | public | The boost::function typedef that creates a ExportOptionsWidget. |
| `validate_filename_template_function_signature_type` | typedef | `bool` | public | Convenience typedef for a function that validates a filename template. |
| `validate_filename_template_function_type` | typedef | `boost::function<validate_filename_template_function_signature_type>` | public | The boost::function typedef that validates a filename template. |
| `register_exporter( ExportAnimationType::ExportID export_id_, const ExportAnimationStrategy::const_configuration_base_ptr &export_configuration, //const QString &filename_template_description_, const create_export_animation_strategy_function_type &create_export_animation_strategy_function_, const create_export_options_w ...` | method | `void` | public | Stores information about the given export\_id\_. |
| `unregister_exporter( ExportAnimationType::ExportID export_id)` | method | `void` | public | Unregisters the specified export ID. |
| `get_registered_exporters()` | method | `std::vector<ExportAnimationType::ExportID>` | public | Returns a list of export IDs of all registered exporters. |
| `get_default_export_configuration( ExportAnimationType::ExportID export_id)` | method | `ExportAnimationStrategy::const_configuration_base_ptr` | public | Returns the default export configuration for the specified export ID. |
| `get_default_filename_template` | field | `QString` | public | Returns the default filename template for the specified export ID. |
| `get_filename_template_description` | field | `QString` | public | Returns the filename template description for the specified export ID. |
| `create_export_animation_strategy( ExportAnimationType::ExportID export_id, ExportAnimationContext &export_animation_context, const ExportAnimationStrategy::const_configuration_base_ptr &export_configuration)` | method | `ExportAnimationStrategy::non_null_ptr_type` | public | Causes a new export animation strategy of the given type to be created; the export ID must have been already registered. |
| `create_export_options_widget( ExportAnimationType::ExportID export_id, QWidget *parent, ExportAnimationContext &export_animation_context, boost::optional<ExportAnimationStrategy::const_configuration_base_ptr> export_configuration = boost::none)` | method | `boost::optional<GPlatesQtWidgets::ExportOptionsWidget *>` | public | Returns a widget to allow the user to specify export animation options for the specified export ID. |
| `validate_filename_template( ExportAnimationType::ExportID export_id, const QString &filename_template, QString &filename_template_validation_message, bool check_filename_variation = true)` | method | `bool` | public | Returns true if filename\_template is valid for the specified export ID. filename\_template\_validation\_message is set to the valid message, if any. |
| `ExporterInfo` | struct | `None` | private | — |
| `exporter_info_map_type` | typedef | `std::map<ExportAnimationType::ExportID, ExporterInfo>` | private | — |
| `d_exporter_info_map` | field | `exporter_info_map_type` | private | Stores a struct of information for each export ID. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `dynamic_cast_export_configuration( const ExportAnimationStrategy::const_configuration_base_ptr &export_configuration)` | function | `typename ExportAnimationStrategyType::const_configuration_ptr` | Convenience function to cast a ExportAnimationStrategy::const\_configuration\_base\_ptr into a derived class 'ExportAnimationStrategyType::const\_configuration\_ptr'. |
| `create_animation_strategy( ExportAnimationContext &export_animation_context, const ExportAnimationStrategy::const_configuration_base_ptr &export_configuration)` | function | `ExportAnimationStrategy::non_null_ptr_type` | Function to create an ExportAnimationStrategy derived type ExportAnimationStrategyType. |
| `create_export_options_widget( QWidget *parent, ExportAnimationContext &export_animation_context, const ExportAnimationStrategy::const_configuration_base_ptr &export_configuration)` | function | `GPlatesQtWidgets::ExportOptionsWidget` | Function to create an ExportOptionsWidget derived type ExportOptionsWidgetType passing in an export configuration. |
| `create_export_options_widget( QWidget *parent, ExportAnimationContext &export_animation_context, const ExportAnimationStrategy::const_configuration_base_ptr &export_configuration, const A1 &arg1)` | function | `GPlatesQtWidgets::ExportOptionsWidget` | Same as the other overload of create\_export\_options\_widget but has an extra parameter. |
| `create_null_export_options_widget( QWidget *, ExportAnimationContext &, const ExportAnimationStrategy::const_configuration_base_ptr &)` | function | `GPlatesQtWidgets::ExportOptionsWidget` | A function that returns a NULL ExportOptionsWidget. |
| `add_export_filename_extension( QString file_basename, ExportAnimationType::Format export_format)` | function | `QString` | Adds the export filename extension to the basename if there is an extension for the specified format. |
| `register_default_export_reconstructed_geometry_animation_types( ExportAnimationRegistry &registry)` | function | `void` | Registers information about the default reconstructed geometry export animation types with the given registry. |
| `register_default_export_projected_geometry_animation_types( ExportAnimationRegistry &registry)` | function | `void` | Registers information about the default projected geometry export animation types with the given registry. |
| `register_default_export_deformation_animation_types( ExportAnimationRegistry &registry)` | function | `void` | Registers information about the default deformation export animation types with the given registry. |
| `register_default_export_scalar_coverage_animation_types( ExportAnimationRegistry &registry)` | function | `void` | Registers information about the default scalar coverage export animation types with the given registry. |
| `register_default_export_velocity_animation_types( ExportAnimationRegistry &registry)` | function | `void` | Registers information about the default velocity export animation types with the given registry. |
| `register_default_export_resolved_topology_animation_types( ExportAnimationRegistry &registry)` | function | `void` | Registers information about the default resolved topology export animation types with the given registry. |
| `register_default_export_citcoms_resolved_topology_animation_types( ExportAnimationRegistry &registry)` | function | `void` | Registers information about the default CitcomS resolved topology export animation types with the given registry. |
| `register_default_export_rotation_animation_types( ExportAnimationRegistry &registry)` | function | `void` | Registers information about the default rotation export animation types with the given registry. |
| `register_default_export_net_rotation_animation_types( ExportAnimationRegistry &registry)` | function | `void` | Registers information about the default net rotation export animation types with the given registry. |
| `register_default_export_image_animation_types( ExportAnimationRegistry &registry)` | function | `void` | Registers information about the default image (screenshots) export animation types with the given registry. |
| `register_default_export_colour_raster_animation_types( ExportAnimationRegistry &registry)` | function | `void` | Registers information about the default colour raster export animation types with the given registry. |
| `register_default_export_numerical_raster_animation_types( ExportAnimationRegistry &registry)` | function | `void` | Registers information about the default numerical raster export animation types with the given registry. |
| `register_default_export_flowline_animation_types( ExportAnimationRegistry &registry)` | function | `void` | Registers information about the default flowline export animation types with the given registry. |
| `register_default_export_motion_path_animation_types( ExportAnimationRegistry &registry)` | function | `void` | Registers information about the default motion path export animation types with the given registry. |
| `register_default_export_co_registration_animation_types( ExportAnimationRegistry &registry)` | function | `void` | Registers information about the default co-registration export animation types with the given registry. |
| `GPLATES_GUI_EXPORTANIMATIONREGISTRY_H` | macro | `None` | — |
| `register_default_export_animation_types( ExportAnimationRegistry &registry)` | function | `void` | Registers information about the default export animation types with the given registry. |

## Notes

`create_export_animation_strategy()`, `create_export_options_widget()` and `validate_filename_template()` all require the export ID to have been registered first via `register_exporter()`; calling them for an unregistered ID either returns `boost::none`/empty results or trips the internal `GPlatesGlobal::Assert` in the cast helper, depending on which path is taken. `dynamic_cast_export_configuration()` asserts rather than failing gracefully if the stored configuration is not of the expected derived type, since a mismatch there indicates a registration bug, not a runtime condition.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ConfigureExportParametersDialog](../qt-widgets/ConfigureExportParametersDialog.md) | qt-widgets | 19 |
| [qt-widgets/EditExportParametersDialog](../qt-widgets/EditExportParametersDialog.md) | qt-widgets | 8 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 5 |
| [gui/ExportAnimationContext](ExportAnimationContext.md) | gui | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportAnimationRegistry.h
python scripts/gpq.py def GPlatesGui::ExportAnimationRegistry --body
python scripts/gpq.py uses ExportAnimationRegistry --kind class
python scripts/gpq.py hier ExportAnimationRegistry
```

# TranscribeSession

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 56 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/TranscribeSession.h` | C++ | 141 |
| `src/presentation/TranscribeSession.cc` | C++ | 3664 |

## Overview

[[[PROSE overview unit=presentation/TranscribeSession tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::TranscribeSession::SuppressAutoLayerCreationRAII`](#gplatespresentationtranscribesessionsuppressautolayercreationraii) | class | `boost::noncopyable` | — | 0 | Enable RAII style 'lock' on temporarily disabling automatic layer creation within app-state for as long as the current scope holds onto this object. |
| [`GPlatesPresentation::TranscribeSession::const_file_reference_seq_type`](#gplatespresentationtranscribesessionconst_file_reference_seq_type) | typedef | — | — | 0 | — |
| [`GPlatesPresentation::TranscribeSession::file_reference_on_load_seq_type`](#gplatespresentationtranscribesessionfile_reference_on_load_seq_type) | typedef | — | — | 0 | — |
| [`GPlatesPresentation::TranscribeSession::layer_seq_type`](#gplatespresentationtranscribesessionlayer_seq_type) | typedef | — | — | 0 | — |
| [`GPlatesPresentation::TranscribeSession::SaveLayerParamsVisitor`](#gplatespresentationtranscribesessionsavelayerparamsvisitor) | class | [`GPlatesAppLogic::ConstLayerParamsVisitor`](../app-logic/LayerParamsVisitor.md) | — | 0 | Saves the app-logic LayerParams of a layer. |
| [`GPlatesPresentation::TranscribeSession::LoadLayerParamsVisitor`](#gplatespresentationtranscribesessionloadlayerparamsvisitor) | class | [`GPlatesAppLogic::LayerParamsVisitor`](../app-logic/LayerParamsVisitor.md) | — | 0 | Loads the app-logic LayerParams of a layer. |
| [`GPlatesPresentation::TranscribeSession::DrawStyleCfgItemValue`](#gplatespresentationtranscribesessiondrawstylecfgitemvalue) | class | `boost::equality_comparable<DrawStyleCfgItemValue>` | — | 0 | The value in a mapping of draw style configuration item name/type to value. |
| [`GPlatesPresentation::TranscribeSession::draw_style_cfg_item_map_type`](#gplatespresentationtranscribesessiondraw_style_cfg_item_map_type) | typedef | — | — | 0 | Typedef for a mapping of draw style configuration item name/type to value. |
| [`GPlatesPresentation::TranscribeSession::SaveVisualLayerParamsVisitor`](#gplatespresentationtranscribesessionsavevisuallayerparamsvisitor) | class | [`ConstVisualLayerParamsVisitor`](VisualLayerParamsVisitor.md) | — | 0 | Saves the VisualLayerParams of a layer. |
| [`GPlatesPresentation::TranscribeSession::LoadVisualLayerParamsVisitor`](#gplatespresentationtranscribesessionloadvisuallayerparamsvisitor) | class | [`VisualLayerParamsVisitor`](VisualLayerParamsVisitor.md) | — | 0 | Loads the VisualLayerParams of a layer. |
| [`GPlatesPresentation::TranscribeSession::UnsupportedVersion`](#gplatespresentationtranscribesessionunsupportedversion) | class | [`GPlatesScribe::Exceptions::BaseException`](../scribe/ScribeExceptions.md) | — | 0 | Exception that's thrown if a session's archive stream (being read) was written using a version of GPlates that is either too old (no longer supported due to breaking changes in the way some of GPlates objects are currently transcribed) or ... |

## Members

### `GPlatesPresentation::TranscribeSession::SuppressAutoLayerCreationRAII`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SuppressAutoLayerCreationRAII( GPlatesAppLogic::ApplicationState &application_state)` | constructor | `None` | public | — |
| `~SuppressAutoLayerCreationRAII()` | destructor | `None` | public | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | public | — |

### `GPlatesPresentation::TranscribeSession::const_file_reference_seq_type`

*None.*

### `GPlatesPresentation::TranscribeSession::file_reference_on_load_seq_type`

*None.*

### `GPlatesPresentation::TranscribeSession::layer_seq_type`

*None.*

### `GPlatesPresentation::TranscribeSession::SaveLayerParamsVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SaveLayerParamsVisitor( const GPlatesScribe::ObjectTag &layer_params_tag, GPlatesScribe::Scribe &scribe, const layer_seq_type &layers)` | constructor | `None` | public | — |
| `visit_co_registration_layer_params( co_registration_layer_params_type &params)` | method | `void` | public | — |
| `visit_raster_layer_params( raster_layer_params_type &params)` | method | `void` | public | — |
| `visit_reconstruction_layer_params( reconstruction_layer_params_type &params)` | method | `void` | public | — |
| `visit_reconstruct_layer_params( reconstruct_layer_params_type &params)` | method | `void` | public | — |
| `visit_reconstruct_scalar_coverage_layer_params( reconstruct_scalar_coverage_layer_params_type &params)` | method | `void` | public | — |
| `visit_scalar_field_3d_layer_params( scalar_field_3d_layer_params_type &params)` | method | `void` | public | — |
| `visit_topology_network_layer_params( topology_network_layer_params_type &params)` | method | `void` | public | — |
| `visit_velocity_field_calculator_layer_params( velocity_field_calculator_layer_params_type &params)` | method | `void` | public | — |
| `d_layer_params_tag` | field | `GPlatesScribe::ObjectTag` | private | — |
| `d_scribe` | field | `GPlatesScribe::Scribe` | private | — |
| `d_layers` | field | `layer_seq_type` | private | — |

### `GPlatesPresentation::TranscribeSession::LoadLayerParamsVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LoadLayerParamsVisitor( const GPlatesScribe::ObjectTag &layer_params_tag, GPlatesScribe::Scribe &scribe, const layer_seq_type &layers)` | constructor | `None` | public | — |
| `visit_co_registration_layer_params( co_registration_layer_params_type &params)` | method | `void` | public | — |
| `visit_raster_layer_params( raster_layer_params_type &params)` | method | `void` | public | — |
| `visit_reconstruction_layer_params( reconstruction_layer_params_type &params)` | method | `void` | public | — |
| `visit_reconstruct_layer_params( reconstruct_layer_params_type &params)` | method | `void` | public | — |
| `visit_reconstruct_scalar_coverage_layer_params( reconstruct_scalar_coverage_layer_params_type &params)` | method | `void` | public | — |
| `visit_scalar_field_3d_layer_params( scalar_field_3d_layer_params_type &params)` | method | `void` | public | — |
| `visit_topology_network_layer_params( topology_network_layer_params_type &params)` | method | `void` | public | — |
| `visit_velocity_field_calculator_layer_params( velocity_field_calculator_layer_params_type &params)` | method | `void` | public | — |
| `d_layer_params_tag` | field | `GPlatesScribe::ObjectTag` | private | — |
| `d_scribe` | field | `GPlatesScribe::Scribe` | private | — |
| `d_layers` | field | `layer_seq_type` | private | — |

### `GPlatesPresentation::TranscribeSession::DrawStyleCfgItemValue`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DrawStyleCfgItemValue()` | constructor | `None` | public | — |
| `set_value( const QString &string_value)` | method | `void` | public | — |
| `set_value( const GPlatesScribe::TranscribeUtils::FilePath &file_path_value)` | method | `void` | public | — |
| `get_value()` | method | `QString` | public | — |
| `operator==( const DrawStyleCfgItemValue &rhs)` | operator | `bool` | public | — |
| `d_value` | field | `boost::variant<QString, GPlatesScribe::TranscribeUtils::FilePath>` | private | — |
| `transcribe( GPlatesScribe::Scribe &scribe, bool transcribed_construct_data)` | method | `GPlatesScribe::TranscribeResult` | private | — |

### `GPlatesPresentation::TranscribeSession::draw_style_cfg_item_map_type`

*None.*

### `GPlatesPresentation::TranscribeSession::SaveVisualLayerParamsVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SaveVisualLayerParamsVisitor( const GPlatesScribe::ObjectTag &layer_params_tag, GPlatesScribe::Scribe &scribe)` | constructor | `None` | public | — |
| `visit_raster_visual_layer_params( raster_visual_layer_params_type &params)` | method | `void` | public | — |
| `visit_reconstruct_scalar_coverage_visual_layer_params( reconstruct_scalar_coverage_visual_layer_params_type &params)` | method | `void` | public | — |
| `visit_reconstruct_visual_layer_params( reconstruct_visual_layer_params_type &params)` | method | `void` | public | — |
| `visit_scalar_field_3d_visual_layer_params( scalar_field_3d_visual_layer_params_type &params)` | method | `void` | public | — |
| `visit_topology_geometry_visual_layer_params( topology_geometry_visual_layer_params_type &params)` | method | `void` | public | — |
| `visit_topology_network_visual_layer_params( topology_network_visual_layer_params_type &params)` | method | `void` | public | — |
| `visit_velocity_field_calculator_visual_layer_params( velocity_field_calculator_visual_layer_params_type &params)` | method | `void` | public | — |
| `d_layer_params_tag` | field | `GPlatesScribe::ObjectTag` | private | — |
| `d_scribe` | field | `GPlatesScribe::Scribe` | private | — |

### `GPlatesPresentation::TranscribeSession::LoadVisualLayerParamsVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LoadVisualLayerParamsVisitor( const GPlatesScribe::ObjectTag &layer_params_tag, GPlatesScribe::Scribe &scribe, boost::shared_ptr<VisualLayer> visual_layer, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | constructor | `None` | public | — |
| `visit_raster_visual_layer_params( raster_visual_layer_params_type &params)` | method | `void` | public | — |
| `visit_reconstruct_scalar_coverage_visual_layer_params( reconstruct_scalar_coverage_visual_layer_params_type &params)` | method | `void` | public | — |
| `visit_reconstruct_visual_layer_params( reconstruct_visual_layer_params_type &params)` | method | `void` | public | — |
| `visit_scalar_field_3d_visual_layer_params( scalar_field_3d_visual_layer_params_type &params)` | method | `void` | public | — |
| `visit_topology_geometry_visual_layer_params( topology_geometry_visual_layer_params_type &params)` | method | `void` | public | — |
| `visit_topology_network_visual_layer_params( topology_network_visual_layer_params_type &params)` | method | `void` | public | — |
| `visit_velocity_field_calculator_visual_layer_params( velocity_field_calculator_visual_layer_params_type &params)` | method | `void` | public | — |
| `d_layer_params_tag` | field | `GPlatesScribe::ObjectTag` | private | — |
| `d_scribe` | field | `GPlatesScribe::Scribe` | private | — |
| `d_visual_layer` | field | `boost::shared_ptr<VisualLayer>` | private | — |
| `d_read_errors` | field | `GPlatesFileIO::ReadErrorAccumulation` | private | — |

### `GPlatesPresentation::TranscribeSession::UnsupportedVersion`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnsupportedVersion( const GPlatesUtils::CallStack::Trace &exception_source, boost::optional< std::vector<GPlatesUtils::CallStack::Trace> > transcribe_incompatible_call_stack = boost::none)` | constructor | `None` | public | — |
| `~UnsupportedVersion()` | destructor | `None` | public | — |
| `get_transcribe_incompatible_trace()` | method | `boost::optional< std::vector<GPlatesUtils::CallStack::Trace> >` | public | Returns the transcribe-incompatible call stack trace, if any. |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_transcribe_incompatible_call_stack` | field | `boost::optional< std::vector<GPlatesUtils::CallStack::Trace> >` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `save_feature_collection_filenames( const GPlatesScribe::ObjectTag &session_state_tag, GPlatesScribe::Scribe &scribe, const_file_reference_seq_type &file_references, QStringList &feature_collection_filenames, const GPlatesAppLogic::ApplicationState &application_state)` | function | `void` | Save the feature collection filenames. |
| `load_feature_collection_filenames( const GPlatesScribe::ObjectTag &session_state_tag, GPlatesScribe::Scribe &scribe, QStringList &feature_collection_filenames)` | function | `void` | Load the feature collection filenames. |
| `load_feature_collection_files( const QStringList &feature_collection_filenames, file_reference_on_load_seq_type &file_references_on_load)` | function | `void` | Load the feature collection files and return any files not loaded (eg, due to file not existing). |
| `save_default_reconstruction_tree_layer( const GPlatesScribe::ObjectTag &session_state_tag, GPlatesScribe::Scribe &scribe, const layer_seq_type &layers, const GPlatesAppLogic::ApplicationState &application_state)` | function | `void` | — |
| `load_default_reconstruction_tree_layer( const GPlatesScribe::ObjectTag &session_state_tag, GPlatesScribe::Scribe &scribe, const layer_seq_type &layers, GPlatesAppLogic::ApplicationState &application_state)` | function | `void` | — |
| `save_layers_visual_order( const GPlatesScribe::ObjectTag &session_state_tag, GPlatesScribe::Scribe &scribe, const layer_seq_type &layers, const ViewState &view_state)` | function | `void` | — |
| `load_layers_visual_order( const GPlatesScribe::ObjectTag &session_state_tag, GPlatesScribe::Scribe &scribe, const layer_seq_type &layers, ViewState &view_state)` | function | `void` | — |
| `save_layer_connection( const GPlatesScribe::ObjectTag &connection_tag, GPlatesScribe::Scribe &scribe, const GPlatesAppLogic::Layer::InputConnection &input_connection, const const_file_reference_seq_type &file_references, const layer_seq_type &layers)` | function | `void` | — |
| `load_layer_connection( const GPlatesScribe::ObjectTag &connection_tag, GPlatesScribe::Scribe &scribe, GPlatesAppLogic::Layer layer, bool &main_input_channel_file_not_loaded, const file_reference_on_load_seq_type &file_references_on_load, const layer_seq_type &layers, GPlatesAppLogic::ReconstructGraph &reconstruct_graph ...` | function | `void` | — |
| `save_remapped_colour_palette_parameters( const GPlatesScribe::ObjectTag &colour_palette_params_tag, GPlatesScribe::Scribe &scribe, const RemappedColourPaletteParameters &colour_palette_params)` | function | `void` | — |
| `load_remapped_colour_palette_parameters( const GPlatesScribe::ObjectTag &colour_palette_params_tag, GPlatesScribe::Scribe &scribe, RemappedColourPaletteParameters &colour_palette_params, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `void` | — |
| `DRAW_STYLE_NAME_VARIANT_REGEXP` | variable | `QRegExp` | Regular expression for a variant of a draw style name that ends with an underscore and a number (eg, "\_1"). |
| `get_draw_style_base_name( const QString &draw_style_name)` | function | `QString` | Return the draw style name with any integer suffixes (eg, "\_1") removed. |
| `DRAW_STYLE_PYTHON_CFG_COLOR_TYPE` | variable | `QString` | Strings representing the derived class types of 'GPlatesGui::ConfigurationItem'. |
| `DRAW_STYLE_PYTHON_CFG_STRING_TYPE` | variable | `QString` | — |
| `DRAW_STYLE_PYTHON_CFG_PALETTE_TYPE` | variable | `QString` | — |
| `get_draw_style_cfg_item_map( draw_style_cfg_item_map_type &draw_style_cfg_item_map, const GPlatesGui::Configuration &configuration)` | function | `void` | Convert the draw style configuration to a map of configuration item name/type to value. |
| `is_draw_style_compatible_with_template( const draw_style_cfg_item_map_type &draw_style_cfg_item_map, const GPlatesGui::StyleAdapter *template_draw_style)` | function | `bool` | See if the template draw style has configuration item names and types matching the specified draw style configuration mapping. |
| `get_new_draw_style_name( const QString &draw_style_name, const GPlatesGui::DrawStyleManager::StyleContainer &draw_styles)` | function | `QString` | Find a new draw style name (based on the specified style name) that doesn't match any style names in draw\_styles. |
| `emit_read_errors_for_missing_palette_files( const GPlatesGui::Configuration &configuration, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `void` | Add a 'ReadErrors::ErrorOpeningFileForReading' read error for any palette files in the draw style configuration that are missing. |
| `set_draw_style_on_layer( const GPlatesGui::StyleAdapter *draw_style, GPlatesPresentation::VisualLayerParams &visual_layer_params, boost::shared_ptr<VisualLayer> visual_layer, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `void` | — |
| `save_draw_style( const GPlatesScribe::ObjectTag &draw_style_tag, GPlatesScribe::Scribe &scribe, const GPlatesPresentation::VisualLayerParams &visual_layer_params)` | function | `void` | — |
| `load_draw_style( const GPlatesScribe::ObjectTag &draw_style_tag, GPlatesScribe::Scribe &scribe, GPlatesPresentation::VisualLayerParams &visual_layer_params, boost::shared_ptr<VisualLayer> visual_layer, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `void` | — |
| `save_layer_params( const GPlatesScribe::ObjectTag &layer_params_tag, GPlatesScribe::Scribe &scribe, const GPlatesAppLogic::Layer &layer, const VisualLayer &visual_layer, const layer_seq_type &layers)` | function | `void` | — |
| `load_layer_params( const GPlatesScribe::ObjectTag &layer_params_tag, GPlatesScribe::Scribe &scribe, GPlatesAppLogic::Layer &layer, const layer_seq_type &layers, VisualLayers &visual_layers, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `void` | — |
| `save_layer( const GPlatesScribe::ObjectTag &layer_tag, GPlatesScribe::Scribe &scribe, const GPlatesAppLogic::Layer &layer, const layer_seq_type &layers, const VisualLayers &visual_layers)` | function | `void` | — |
| `load_layer( const GPlatesScribe::ObjectTag &layer_tag, GPlatesScribe::Scribe &scribe, const std::vector<GPlatesAppLogic::LayerTaskRegistry::LayerTaskType> &layer_task_types, GPlatesAppLogic::ReconstructGraph &reconstruct_graph, VisualLayers &visual_layers)` | function | `GPlatesAppLogic::Layer` | Loads and returns layer if successful (otherwise returns an invalid layer). |
| `save_layers( const GPlatesScribe::ObjectTag &session_state_tag, GPlatesScribe::Scribe &scribe, const const_file_reference_seq_type &file_references, const GPlatesAppLogic::ApplicationState &application_state, const ViewState &view_state)` | function | `void` | — |
| `load_layers( const GPlatesScribe::ObjectTag &session_state_tag, GPlatesScribe::Scribe &scribe, const file_reference_on_load_seq_type &file_references_on_load, GPlatesFileIO::ReadErrorAccumulation &read_errors, GPlatesAppLogic::ApplicationState &application_state, ViewState &view_state)` | function | `void` | — |
| `save_application_state( const GPlatesScribe::ObjectTag &session_state_tag, GPlatesScribe::Scribe &scribe, const GPlatesAppLogic::ApplicationState &application_state)` | function | `void` | — |
| `load_application_state( const GPlatesScribe::ObjectTag &session_state_tag, GPlatesScribe::Scribe &scribe, GPlatesAppLogic::ApplicationState &application_state)` | function | `void` | — |
| `save_geometry_visibility( const GPlatesScribe::ObjectTag &geometry_visibility_tag, GPlatesScribe::Scribe &scribe, const GPlatesGui::RenderSettings &render_settings)` | function | `void` | — |
| `load_geometry_visibility( const GPlatesScribe::ObjectTag &geometry_visibility_tag, GPlatesScribe::Scribe &scribe, GPlatesGui::RenderSettings &render_settings)` | function | `void` | — |
| `save_animation_configuration( const GPlatesScribe::ObjectTag &animation_configuration_tag, GPlatesScribe::Scribe &scribe, const GPlatesGui::AnimationController &animation_controller)` | function | `void` | — |
| `load_animation_configuration( const GPlatesScribe::ObjectTag &animation_configuration_tag, GPlatesScribe::Scribe &scribe, GPlatesGui::AnimationController &animation_controller)` | function | `void` | — |
| `save_reconstruction_layer_geometry_parameters( const GPlatesScribe::ObjectTag &reconstruction_layer_geometry_parameters_tag, GPlatesScribe::Scribe &scribe, const GPlatesViewOperations::RenderedGeometryParameters &rendered_geometry_parameters)` | function | `void` | — |
| `load_reconstruction_layer_geometry_parameters( const GPlatesScribe::ObjectTag &reconstruction_layer_geometry_parameters_tag, GPlatesScribe::Scribe &scribe, GPlatesViewOperations::RenderedGeometryParameters &rendered_geometry_parameters)` | function | `void` | — |
| `save_view_state( const GPlatesScribe::ObjectTag &session_state_tag, GPlatesScribe::Scribe &scribe, const ViewState &view_state)` | function | `void` | — |
| `load_view_state( const GPlatesScribe::ObjectTag &session_state_tag, GPlatesScribe::Scribe &scribe, ViewState &view_state)` | function | `void` | — |
| `save_session( const GPlatesScribe::ObjectTag &session_state_tag, GPlatesScribe::Scribe &scribe, const_file_reference_seq_type &file_references, QStringList &feature_collection_filenames)` | function | `void` | Save the session using the specified Scribe. |
| `load_session( const GPlatesScribe::ObjectTag &session_state_tag, GPlatesScribe::Scribe &scribe, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `void` | Load the session using the specified Scribe. |
| `save_session_gplates_1_5( const GPlatesScribe::ObjectTag &session_state_tag, GPlatesScribe::Scribe &scribe, const const_file_reference_seq_type &file_references)` | function | `void` | Unfortunately due to a mistake (in GPlates 1.5) we also need to save the deprecated session state required to support GPlates 1.5. |
| `load_session_gplates_1_5( const GPlatesScribe::ObjectTag &session_state_tag, GPlatesScribe::Scribe &scribe, const QStringList &feature_collection_filenames, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | function | `void` | — |
| `GPLATES_PRESENTATION_TRANSCRIBESESSION_H` | macro | `None` | — |
| `save( GPlatesScribe::Scribe &scribe, boost::optional<GPlatesScribe::Scribe &> scribe_gplates_1_5 = boost::none)` | function | `QStringList` | Save the session using the specified Scribe. |
| `load( GPlatesScribe::Scribe &scribe, const QStringList &feature_collection_filenames)` | function | `void` | Load the session using the specified Scribe. |

## Notes

[[[PROSE notes unit=presentation/TranscribeSession tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/InternalSession](InternalSession.md) | presentation | 76 |
| [presentation/ProjectSession](ProjectSession.md) | presentation | 75 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/TranscribeSession.h
python scripts/gpq.py def GPlatesPresentation::TranscribeSession::LoadVisualLayerParamsVisitor --body
python scripts/gpq.py uses LoadVisualLayerParamsVisitor --kind class
python scripts/gpq.py hier LoadVisualLayerParamsVisitor
```

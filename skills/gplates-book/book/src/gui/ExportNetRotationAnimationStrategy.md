# ExportNetRotationAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 473 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportNetRotationAnimationStrategy.h` | C++ | 242 |
| `src/gui/ExportNetRotationAnimationStrategy.cc` | C++ | 937 |

## Overview

[[[PROSE overview unit=gui/ExportNetRotationAnimationStrategy tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::resolved_topological_geom_seq_type`](#anonymousresolved_topological_geom_seq_type) | typedef | — | — | 0 | Convenience typedef for sequence of resolved topological geometries. |
| [`(anonymous)::resolved_topological_network_seq_type`](#anonymousresolved_topological_network_seq_type) | typedef | — | — | 0 | Convenience typedef for sequence of resolved topological networks. |
| [`(anonymous)::csv_data_type`](#anonymouscsv_data_type) | typedef | — | — | 0 | — |
| [`(anonymous)::feature_handle_to_collection_map_type`](#anonymousfeature_handle_to_collection_map_type) | typedef | — | — | 0 | Typedef for mapping from FeatureHandle to the feature collection file it came from and the order in which is occurs relative to other features in the feature collections. |
| [`(anonymous)::velocity_field_calculator_layer_proxy_seq_type`](#anonymousvelocity_field_calculator_layer_proxy_seq_type) | typedef | — | — | 0 | Typedef for sequence of velocity field calculator layer proxies. |
| [`(anonymous)::vector_field_seq_type`](#anonymousvector_field_seq_type) | typedef | — | — | 0 | Typedef for a sequence of MultiPointVectorField pointers. |
| [`GPlatesGui::ExportNetRotationAnimationStrategy`](#gplatesguiexportnetrotationanimationstrategy) | class | [`GPlatesGui::ExportAnimationStrategy`](ExportAnimationStrategy.md) | — | 0 | Concrete implementation of the ExportAnimationStrategy class for writing net rotations. |

## Members

### `(anonymous)::resolved_topological_geom_seq_type`

*None.*

### `(anonymous)::resolved_topological_network_seq_type`

*None.*

### `(anonymous)::csv_data_type`

*None.*

### `(anonymous)::feature_handle_to_collection_map_type`

*None.*

### `(anonymous)::velocity_field_calculator_layer_proxy_seq_type`

*None.*

### `(anonymous)::vector_field_seq_type`

*None.*

### `GPlatesGui::ExportNetRotationAnimationStrategy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportNetRotationAnimationStrategy>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportNetRotationAnimationStrategy\>. |
| `file_collection_type` | typedef | `std::vector<const GPlatesFileIO::File::Reference *>` | public | — |
| `Configuration` | class | `None` | public | Configuration options. |
| `const_configuration_ptr` | typedef | `boost::shared_ptr<const Configuration>` | public | Typedef for a shared pointer to const Configuration. |
| `configuration_ptr` | typedef | `boost::shared_ptr<Configuration>` | public | Typedef for a shared pointer to Configuration. |
| `create( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | method | `non_null_ptr_type` | public | — |
| `~ExportNetRotationAnimationStrategy()` | destructor | `None` | public | — |
| `do_export_iteration( std::size_t frame_index)` | method | `bool` | public | Does one frame of export. |
| `wrap_up( bool export_successful)` | method | `void` | public | Allows Strategy objects to do any housekeeping that might be necessary after all export iterations are completed. false if there was any kind of interruption. |
| `set_template_filename( const QString &)` | method | `void` | public | — |
| `pole_type` | typedef | `std::pair<GPlatesMaths::LatLonPoint, double>` | public | Is public since used by anonymous functions in cpp file. |
| `vector_field_seq_type` | typedef | `std::vector<const GPlatesAppLogic::MultiPointVectorField *>` | protected | Required only if using existing velocity mesh for calculations. |
| `ExportNetRotationAnimationStrategy( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | constructor | `None` | protected | Protected constructor to prevent instantiation on the stack. |
| `export_iteration_using_existing_velocity_mesh( std::size_t frame_index)` | method | `bool` | private | export\_iteration\_using\_existing\_velocity\_mesh - calculates net-rotations using the velocities of an existing velocity mesh layer. |
| `export_iteration( std::size_t frame_index)` | method | `bool` | private | export\_iteration - calculates net-rotations based on a hard-coded 1-degree lat-lon grid. |
| `time_pole_pair_type` | typedef | `std::pair<double, pole_type>` | private | — |
| `d_loaded_files` | field | `file_collection_type` | private | The list of currently loaded files that are active. |
| `d_loaded_reconstruction_files` | field | `file_collection_type` | private | The active and loaded reconstruction file(s) used in the reconstruction. |
| `d_configuration` | field | `const_configuration_ptr` | private | Export configuration parameters. |
| `d_total_poles` | field | `std::vector<time_pole_pair_type>` | private | — |
| `d_referenced_files_set` | field | `std::set<const GPlatesFileIO::File::Reference *>` | private | d\_referenced\_files\_set - Set of the referenced geometry files encountered during the whole export sequence. |
| `d_anchor_plate_id` | field | `GPlatesModel::integer_plate_id_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `area_conversion_to_km2` | variable | `double` | The numerator here is the surface area of the earth in square kilometers; the denominator is the total area of a sphere for which a 1-degree grid "square" at the equator has area equal to one. |
| `get_older_and_younger_times( const GPlatesQtWidgets::VelocityMethodWidget::VelocityMethod &velocity_method, const double &delta_time, const double &current_time, double &time_older, double &time_younger, GPlatesAppLogic::VelocityDeltaTime::Type &velocity_delta_time_type)` | function | `void` | get\_older\_and\_younger\_times - on return @time\_older and @time\_younger will hold the appropriate times for the velocity calculation at the @current\_time. |
| `get_velocity_field_calculator_layer_proxies( velocity_field_calculator_layer_proxy_seq_type &velocity_field_outputs, const GPlatesAppLogic::ApplicationState &application_state)` | function | `void` | get\_velocity\_field\_calculator\_layer\_proxies - this is used only when net-rotations are calculated using points and velocities from any existing velocity mesh. |
| `get_vector_field_seq( vector_field_seq_type &vector_field_seq, const std::vector<GPlatesAppLogic::MultiPointVectorField::non_null_ptr_type> &multi_point_velocity_fields)` | function | `void` | get\_vector\_field\_seq - this is used only when net-rotations are calculated using points and velocities from any existing velocity mesh. |
| `populate_vector_field_seq( vector_field_seq_type &vector_field_seq, const GPlatesAppLogic::ApplicationState &application_state, GPlatesAppLogic::NetRotationUtils::net_rotation_map_type &net_rotation_output)` | function | `void` | populate\_vector\_field\_seq - - this is used only when net-rotations are calculated using points and velocities from any existing velocity mesh. |
| `write_file_collection_to_csv_data( csv_data_type &csv_data, const GPlatesGui::ExportNetRotationAnimationStrategy::file_collection_type &files, const QString &description)` | function | `void` | — |
| `write_reconstruction_info_to_csv_data( csv_data_type &csv_data, const GPlatesModel::integer_plate_id_type &anchor_plate, const GPlatesGui::ExportNetRotationAnimationStrategy::file_collection_type &referenced_files, const GPlatesGui::ExportNetRotationAnimationStrategy::file_collection_type &reconstruction_files)` | function | `void` | — |
| `write_header_to_csv_data( csv_data_type &csv_data, const double &time, const GPlatesModel::integer_plate_id_type &anchor_plate, const GPlatesGui::ExportNetRotationAnimationStrategy::file_collection_type &referenced_files, const GPlatesGui::ExportNetRotationAnimationStrategy::file_collection_type &reconstruction_files)` | function | `void` | — |
| `write_net_rotation_to_csv_data( csv_data_type &csv_data, const GPlatesGui::ExportNetRotationAnimationStrategy::pole_type &net_rotation)` | function | `void` | — |
| `GPLATES_GUI_EXPORTNETROTATIONANIMATIONSTRATEGY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/ExportNetRotationAnimationStrategy tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 16 |
| [qt-widgets/ExportNetRotationOptionsWidget](../qt-widgets/ExportNetRotationOptionsWidget.md) | qt-widgets | 12 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportNetRotationAnimationStrategy.h
python scripts/gpq.py def GPlatesGui::ExportNetRotationAnimationStrategy --body
python scripts/gpq.py uses ExportNetRotationAnimationStrategy --kind class
python scripts/gpq.py hier ExportNetRotationAnimationStrategy
```

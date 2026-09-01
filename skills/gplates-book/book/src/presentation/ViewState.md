# ViewState

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 74 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/ViewState.h` | C++ | 541 |
| `src/presentation/ViewState.cc` | C++ | 633 |

## Overview

[[[PROSE overview unit=presentation/ViewState tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::ViewState`](#gplatespresentationviewstate) | class | `QObject`<br>`boost::noncopyable` | — | 0 | — |

## Members

### `GPlatesPresentation::ViewState`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ViewState( GPlatesAppLogic::ApplicationState &application_state)` | constructor | `None` | public | — |
| `~ViewState()` | destructor | `None` | public | — |
| `get_application_state` | field | `GPlatesAppLogic::ApplicationState` | public | — |
| `set_other_view_state( GPlatesQtWidgets::ViewportWindow &viewport_window)` | method | `void` | public | — |
| `get_animation_controller` | field | `GPlatesGui::AnimationController` | public | — |
| `get_session_management` | field | `SessionManagement` | public | Stores/Loads loaded file information to and from persistent storage. |
| `get_rendered_geometry_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | public | — |
| `get_feature_focus` | field | `GPlatesGui::FeatureFocus` | public | — |
| `get_feature_table_model` | field | `GPlatesGui::FeatureTableModel` | public | — |
| `get_viewport_zoom` | field | `GPlatesGui::ViewportZoom` | public | — |
| `get_viewport_projection` | field | `GPlatesGui::ViewportProjection` | public | — |
| `get_digitise_geometry_builder` | field | `GPlatesViewOperations::GeometryBuilder` | public | — |
| `get_focused_feature_geometry_builder` | field | `GPlatesViewOperations::GeometryBuilder` | public | — |
| `get_colour_scheme_container` | field | `GPlatesGui::ColourSchemeContainer` | public | Returns all loaded colour schemes, sorted by category. |
| `get_colour_scheme()` | method | `GPlatesGlobal::PointerTraits<GPlatesGui::ColourScheme>::non_null_ptr_type` | public | Returns the current colour scheme. |
| `get_colour_scheme_delegator()` | method | `GPlatesGlobal::PointerTraits<GPlatesGui::ColourSchemeDelegator>::non_null_ptr_type` | public | — |
| `get_render_settings` | field | `GPlatesGui::RenderSettings` | public | — |
| `get_rendered_geometry_parameters` | field | `GPlatesViewOperations::RenderedGeometryParameters` | public | — |
| `get_scene_lighting_parameters` | field | `GPlatesGui::SceneLightingParameters` | public | — |
| `get_visual_layers` | field | `VisualLayers` | public | — |
| `get_visual_layer_registry` | field | `VisualLayerRegistry` | public | — |
| `get_map_transform` | field | `GPlatesGui::MapTransform` | public | — |
| `get_last_open_directory` | field | `QString` | public | TODO: the get\_last\_open\_directory methods should be obsolete now, but retain until the FileIODirectoryConfiguration stuff has been tested further. |
| `get_show_stars()` | method | `bool` | public | — |
| `set_show_stars( bool show_stars = false)` | method | `void` | public | — |
| `get_feature_type_symbol_map` | field | `GPlatesGui::symbol_map_type` | public | — |
| `get_background_colour` | field | `GPlatesGui::Colour` | public | — |
| `set_background_colour( const GPlatesGui::Colour &colour)` | method | `void` | public | — |
| `get_graticule_settings` | field | `GPlatesGui::GraticuleSettings` | public | — |
| `get_text_overlay_settings` | field | `GPlatesGui::TextOverlaySettings` | public | — |
| `get_velocity_legend_overlay_settings` | field | `GPlatesGui::VelocityLegendOverlaySettings` | public | — |
| `get_export_animation_registry` | field | `GPlatesGui::ExportAnimationRegistry` | public | — |
| `get_topology_boundary_sections_container` | field | `GPlatesGui::TopologySectionsContainer` | public | — |
| `get_topology_interior_sections_container` | field | `GPlatesGui::TopologySectionsContainer` | public | — |
| `get_file_io_directory_configurations` | field | `GPlatesGui::FileIODirectoryConfigurations` | public | — |
| `handle_zoom_change()` | method | `void` | private | — |
| `connect_to_viewport_zoom()` | method | `void` | private | — |
| `connect_to_feature_focus()` | method | `void` | private | — |
| `setup_rendered_geometry_collection()` | method | `void` | private | — |
| `initialise_from_user_preferences()` | method | `void` | private | Overrides some ViewState settings' defaults based on UserPreferences. |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | NOTE: Most of these are boost::scoped\_ptr's to avoid having to include header files. |
| `d_other_view_state` | field | `GPlatesQtWidgets::ViewportWindow` | private | FIXME: remove this when refactored |
| `d_animation_controller` | field | `boost::scoped_ptr<GPlatesGui::AnimationController>` | private | Handles logic for animating the reconstruction time (for time slider and export). |
| `d_session_management_ptr` | field | `boost::scoped_ptr<SessionManagement>` | private | Manages saving and restoring sessions. |
| `d_rendered_geometry_collection` | field | `boost::scoped_ptr<GPlatesViewOperations::RenderedGeometryCollection>` | private | Contains all rendered geometries for this view state. |
| `d_feature_focus` | field | `boost::scoped_ptr<GPlatesGui::FeatureFocus>` | private | Tracks the currently focused feature (if any). |
| `d_feature_table_model_ptr` | field | `boost::scoped_ptr<GPlatesGui::FeatureTableModel>` | private | The 'Clicked' table. |
| `d_colour_scheme_container` | field | `boost::scoped_ptr<GPlatesGui::ColourSchemeContainer>` | private | Holds all loaded colour schemes, sorted by category. |
| `d_colour_scheme` | field | `GPlatesGlobal::PointerTraits<GPlatesGui::ColourSchemeDelegator>::non_null_ptr_type` | private | Keeps track of the currently selected colour scheme. |
| `d_viewport_zoom` | field | `boost::scoped_ptr<GPlatesGui::ViewportZoom>` | private | The viewport zoom state. |
| `d_viewport_projection` | field | `boost::scoped_ptr<GPlatesGui::ViewportProjection>` | private | The viewport projection state. |
| `d_digitise_geometry_builder` | field | `boost::scoped_ptr<GPlatesViewOperations::GeometryBuilder>` | private | Builds geometry for digitised geometry. |
| `d_focused_feature_geometry_builder` | field | `boost::scoped_ptr<GPlatesViewOperations::GeometryBuilder>` | private | Builds geometry for the focused feature. |
| `d_focused_feature_geom_manipulator` | field | `boost::scoped_ptr<GPlatesViewOperations::FocusedFeatureGeometryManipulator>` | private | Depends on d\_focused\_feature\_geometry\_builder and d\_feature\_focus. |
| `d_feature_type_symbol_map` | field | `GPlatesGui::symbol_map_type` | private | Holds map of feature type to symbol. |
| `d_render_settings` | field | `boost::scoped_ptr<GPlatesGui::RenderSettings>` | private | What geometry types get rendered and what don't. |
| `d_rendered_geometry_parameters` | field | `boost::scoped_ptr<GPlatesViewOperations::RenderedGeometryParameters>` | private | Render parameters (point/line sizes, colours, etc) of geometries (mostly in canvas tools). |
| `d_scene_lighting_parameters` | field | `boost::scoped_ptr<GPlatesGui::SceneLightingParameters>` | private | Parameters used when lighting the scene during OpenGL rendering. |
| `d_visual_layers` | field | `boost::scoped_ptr<VisualLayers>` | private | Manages the various layers (usually corresponding to each loaded feature collection) whose output results are drawn into child layers of the RECONSTRUCTION main rendered geometry layer. |
| `d_visual_layer_registry` | field | `boost::scoped_ptr<VisualLayerRegistry>` | private | Stores information about the available visual layer types. |
| `d_map_transform` | field | `boost::scoped_ptr<GPlatesGui::MapTransform>` | private | Sends signals to transform maps |
| `d_last_open_directory` | field | `QString` | private | Stores the directory containing the files last opened, or the last opened directory. |
| `d_file_io_directory_configurations` | field | `boost::scoped_ptr<GPlatesGui::FileIODirectoryConfigurations>` | private | Stores last-used directories, preferred behaviour etc for various file types |
| `d_show_stars` | field | `bool` | private | Whether to draw stars behind the 3D globe. |
| `d_background_colour` | field | `boost::scoped_ptr<GPlatesGui::Colour>` | private | The colour of the background sphere or plane in 3D globe or map view respectively. |
| `d_graticule_settings` | field | `boost::scoped_ptr<GPlatesGui::GraticuleSettings>` | private | Settings related to the graticules displayed on the map and the globe. |
| `d_text_overlay_settings` | field | `boost::scoped_ptr<GPlatesGui::TextOverlaySettings>` | private | Settings related to the overlay of text on top the map and the globe. |
| `d_velocity_legend_overlay_settings` | field | `boost::scoped_ptr<GPlatesGui::VelocityLegendOverlaySettings>` | private | Settings related to the overlay of a velocity scale legend. |
| `d_export_animation_registry` | field | `boost::scoped_ptr<GPlatesGui::ExportAnimationRegistry>` | private | Stores information about the export animation types. |
| `d_topology_boundary_sections_container_ptr` | field | `boost::scoped_ptr<GPlatesGui::TopologySectionsContainer>` | private | The data behind the Topology Sections table (containing boundary sections). |
| `d_topology_interior_sections_container_ptr` | field | `boost::scoped_ptr<GPlatesGui::TopologySectionsContainer>` | private | The data behind the Topology Sections table (containing interior sections). |
| `d_python_manager_ptr` | field | `GPlatesGui::PythonManager` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_default_background_colour()` | function | `GPlatesGui::Colour` | — |
| `GPLATES_PRESENTATION_VIEWSTATE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=presentation/ViewState tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ScalarField3DLayerOptionsWidget](../qt-widgets/ScalarField3DLayerOptionsWidget.md) | qt-widgets | 92 |
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 71 |
| [qt-widgets/KinematicGraphsDialog](../qt-widgets/KinematicGraphsDialog.md) | qt-widgets | 65 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 63 |
| [qt-widgets/MapView](../qt-widgets/MapView.md) | qt-widgets | 61 |
| [qt-widgets/AssignReconstructionPlateIdsDialog](../qt-widgets/AssignReconstructionPlateIdsDialog.md) | qt-widgets | 56 |
| [presentation/TranscribeSession](TranscribeSession.md) | presentation | 47 |
| [gui/CommandServer](../gui/CommandServer.md) | gui | 46 |
| [qt-widgets/GlobeAndMapWidget](../qt-widgets/GlobeAndMapWidget.md) | qt-widgets | 46 |
| [qt-widgets/EditWidgetGroupBox](../qt-widgets/EditWidgetGroupBox.md) | qt-widgets | 45 |
| [qt-widgets/EditTimeSequenceWidget](../qt-widgets/EditTimeSequenceWidget.md) | qt-widgets | 44 |
| [presentation/VisualLayers](VisualLayers.md) | presentation | 43 |
| [qt-widgets/EditGeometryWidget](../qt-widgets/EditGeometryWidget.md) | qt-widgets | 39 |
| [qt-widgets/TotalReconstructionPolesDialog](../qt-widgets/TotalReconstructionPolesDialog.md) | qt-widgets | 38 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 34 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 32 |
| [qt-widgets/MovePoleWidget](../qt-widgets/MovePoleWidget.md) | qt-widgets | 30 |
| [gui/DigitisationCanvasToolWorkflow](../gui/DigitisationCanvasToolWorkflow.md) | gui | 25 |
| [gui/TopologyCanvasToolWorkflow](../gui/TopologyCanvasToolWorkflow.md) | gui | 25 |
| [qt-widgets/AddNewLayerDialog](../qt-widgets/AddNewLayerDialog.md) | qt-widgets | 24 |

*... and 121 more units.*

## Related

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_viewport_zoom.get()` | `zoom_changed()` | `this` | `handle_zoom_change()` |
| `&get_feature_focus()` | `focused_feature_modified(GPlatesGui::FeatureFocus &)` | `&get_application_state()` | `reconstruct()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/ViewState.h
python scripts/gpq.py def GPlatesPresentation::ViewState --body
python scripts/gpq.py uses ViewState --kind class
python scripts/gpq.py hier ViewState
```

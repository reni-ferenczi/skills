# VisualLayerRegistry

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 442 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/VisualLayerRegistry.h` | C++ | 301 |
| `src/presentation/VisualLayerRegistry.cc` | C++ | 579 |

## Overview

[[[PROSE overview unit=presentation/VisualLayerRegistry tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::CreateAppLogicLayer`](#anonymouscreateapplogiclayer) | class | — | — | 0 | A helper functor for use with create\_visual\_layer\_function. |
| [`GPlatesPresentation::VisualLayerRegistry`](#gplatespresentationvisuallayerregistry) | class | `boost::noncopyable` | — | 0 | Stores user interface-related information about visual layers. |

## Members

### `(anonymous)::CreateAppLogicLayer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CreateAppLogicLayer( GPlatesAppLogic::ReconstructGraph &reconstruct_graph, GPlatesAppLogic::LayerTaskRegistry &layer_task_registry, GPlatesAppLogic::LayerTaskType::Type layer_type)` | constructor | `None` | public | — |
| `operator()()` | operator | `void` | public | — |
| `d_reconstruct_graph` | field | `GPlatesAppLogic::ReconstructGraph` | private | — |
| `d_layer_task_type` | field | `GPlatesAppLogic::LayerTaskRegistry::LayerTaskType` | private | — |

### `GPlatesPresentation::VisualLayerRegistry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create_visual_layer_function_type` | typedef | `boost::function< void () >` | public | Convenience typedef for a function that causes a visual layer to be added to the VisualLayers. |
| `create_options_widget_function_type` | typedef | `boost::function< GPlatesQtWidgets::LayerOptionsWidget *( GPlatesAppLogic::ApplicationState &, GPlatesPresentation::ViewState &, GPlatesQtWidgets::ViewportWindow *, QWidget *) >` | public | Convenience typedef for a function that creates a widget for editing the visual layer's options. |
| `create_visual_layer_params_function_type` | typedef | `boost::function< VisualLayerParams::non_null_ptr_type (GPlatesAppLogic::LayerParams::non_null_ptr_type) >` | public | Convenience typedef for a function that takes a layer params argument and creates a non-null intrusive pointer to an instance of VisualLayerParams (or one of its derived classes). |
| `register_visual_layer_type( VisualLayerType::Type visual_layer_type_, VisualLayerGroup::Type group_, const QString &name_, const QString &description_, const GPlatesGui::Colour &colour_, const create_visual_layer_function_type &create_visual_layer_function_, const create_options_widget_function_type &create_options_wid ...` | method | `void` | public | Stores information about the given visual\_layer\_type\_. |
| `unregister_visual_layer_type( VisualLayerType::Type visual_layer_type)` | method | `void` | public | — |
| `visual_layer_type_seq_type` | typedef | `std::vector<VisualLayerType::Type>` | public | — |
| `get_visual_layer_types_in_order` | field | `visual_layer_type_seq_type` | public | Retrieves visual layer types sorted by group. |
| `visual_layer_type_order_map_type` | typedef | `std::map<VisualLayerType::Type, std::size_t>` | public | — |
| `get_visual_layer_type_order_map` | field | `visual_layer_type_order_map_type` | public | Returns a map of visual layer types to their corresponding index in the sequence returned by get\_visual\_layer\_types\_in\_order. |
| `get_group( VisualLayerType::Type visual_layer_type)` | method | `VisualLayerGroup::Type` | public | Returns the group to which the given visual layer type belongs, or VisualLayerGroup::NUM\_GROUPS if the given type has not been registered. |
| `get_name` | field | `QString` | public | Returns a human-readable name for the given visual layer type, or the empty string if the given type has not been registered. |
| `get_description` | field | `QString` | public | Returns a human-readable description for the given visual layer type, or the empty string if the given type has not been registered. |
| `get_colour` | field | `GPlatesGui::Colour` | public | Returns the colour associated with the given visual layer type, or black if the given type has not been registered. |
| `get_icon` | field | `QIcon` | public | Returns an icon associated with the given visual layer type, or an uninitialised icon if the given type has not been registered. |
| `create_visual_layer( VisualLayerType::Type visual_layer_type)` | method | `void` | public | Causes a new visual layer of the given type to be created; the visual layer type must have been already registered. |
| `create_options_widget( VisualLayerType::Type visual_layer_type, GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, GPlatesQtWidgets::ViewportWindow *viewport_window, QWidget *parent)` | method | `GPlatesQtWidgets::LayerOptionsWidget` | public | Returns a widget for editing the given visual layer type's options. |
| `create_visual_layer_params( VisualLayerType::Type visual_layer_type, GPlatesAppLogic::LayerParams::non_null_ptr_type layer_params)` | method | `VisualLayerParams::non_null_ptr_type` | public | Returns an object suitable for holding visualisation-related parameters and options for the given visual layer type. |
| `produces_rendered_geometries( VisualLayerType::Type visual_layer_type)` | method | `bool` | public | Returns whether the given visual\_layer\_type ever produces rendered geometries. |
| `VisualLayerInfo` | struct | `None` | private | — |
| `invalidate_order_cache()` | method | `void` | private | — |
| `visual_layer_info_map_type` | typedef | `std::map<VisualLayerType::Type, VisualLayerInfo>` | private | — |
| `d_visual_layer_info_map` | field | `visual_layer_info_map_type` | private | Stores a struct of information for each visual layer type. |
| `d_visual_layer_type_order` | field | `visual_layer_type_seq_type` | private | For each visual layer group, stores the order of visual layer types within it. |
| `d_cached_combined_visual_layer_type_order` | field | `boost::optional<visual_layer_type_seq_type>` | private | Each element of d\_visual\_layer\_type\_order combined in order. |
| `d_cached_visual_layer_type_order_map` | field | `boost::optional<visual_layer_type_order_map_type>` | private | Map of visual layer type to index in d\_cached\_combined\_visual\_layer\_type\_order. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_filled_pixmap( int width, int height, const GPlatesGui::Colour &colour)` | function | `QPixmap` | — |
| `do_nothing()` | function | `void` | A do-nothing function for use with create\_visual\_layer\_function. |
| `no_widget( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, GPlatesQtWidgets::ViewportWindow *viewport_window, QWidget *parent)` | function | `GPlatesQtWidgets::LayerOptionsWidget` | A function that always returns NULL for use with create\_options\_widget\_function. |
| `default_visual_layer_params( GPlatesAppLogic::LayerParams::non_null_ptr_type layer_params)` | function | `GPlatesPresentation::VisualLayerParams::non_null_ptr_type` | A function that instantiates the base VisualLayerParams class for use with create\_visual\_layer\_params\_function. |
| `GPLATES_PRESENTATION_VISUALLAYERREGISTRY_H` | macro | `None` | — |
| `register_default_visual_layers( VisualLayerRegistry &registry, GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state)` | function | `void` | Registers information about the default, built-in visual layers with the given registry. |

## Notes

[[[PROSE notes unit=presentation/VisualLayerRegistry tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/VisualLayerWidget](../qt-widgets/VisualLayerWidget.md) | qt-widgets | 19 |
| [qt-widgets/AddNewLayerDialog](../qt-widgets/AddNewLayerDialog.md) | qt-widgets | 11 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 10 |
| [qt-widgets/VisualLayersComboBox](../qt-widgets/VisualLayersComboBox.md) | qt-widgets | 10 |
| [presentation/VisualLayers](VisualLayers.md) | presentation | 4 |
| [presentation/VisualLayer](VisualLayer.md) | presentation | 3 |
| [presentation/ViewState](ViewState.md) | presentation | 2 |
| [qt-widgets/AnimateControlWidget](../qt-widgets/AnimateControlWidget.md) | qt-widgets | 2 |
| [qt-widgets/AssignReconstructionPlateIdsDialog](../qt-widgets/AssignReconstructionPlateIdsDialog.md) | qt-widgets | 2 |
| [qt-widgets/TotalReconstructionPolesDialog](../qt-widgets/TotalReconstructionPolesDialog.md) | qt-widgets | 2 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 2 |
| [qt-widgets/CanvasToolBarDockWidget](../qt-widgets/CanvasToolBarDockWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/VisualLayerRegistry.h
python scripts/gpq.py def GPlatesPresentation::VisualLayerRegistry --body
python scripts/gpq.py uses VisualLayerRegistry --kind class
python scripts/gpq.py hier VisualLayerRegistry
```

# VisualLayer

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 441 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/VisualLayer.h` | C++ | 308 |
| `src/presentation/VisualLayer.cc` | C++ | 334 |

## Overview

[[[PROSE overview unit=presentation/VisualLayer tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::VisualLayer`](#gplatespresentationvisuallayer) | class | `QObject`<br>`boost::noncopyable` | — | 0 | Represents a layer that processes inputs (such as a feature collection) to an output (such as reconstruction geometries) and determines how to visualise the output. |

## Members

### `GPlatesPresentation::VisualLayer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `WidgetSection` | enum | `None` | public | An enumeration of sections in the widgets that display visual layers. |
| `VisualLayer( ViewState &view_state, VisualLayers &visual_layers, GPlatesAppLogic::Layer &layer, int layer_number)` | constructor | `None` | public | Constructor wraps a visual layer around layer created in ReconstructGraph. |
| `get_rendered_geometry_layer_index()` | method | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_index_type` | public | — |
| `get_layer_type()` | method | `VisualLayerType::Type` | public | Returns the type of the visual layer as an enumeration. |
| `create_rendered_geometries()` | method | `void` | public | Creates rendered geometries for this visual layer. |
| `is_expanded( WidgetSection section)` | method | `bool` | public | Returns whether the given section of the visual layer is expanded in the user interface. |
| `set_expanded( WidgetSection section, bool expanded = true)` | method | `void` | public | Sets whether the given section of the visual layer is expanded in the user interface. |
| `toggle_expanded( WidgetSection section)` | method | `void` | public | Toggles whether the given section of the visual layer is expanded in the user interface or not. |
| `is_visible()` | method | `bool` | public | Returns whether the visual layer is rendered onto the viewport. |
| `set_visible( bool visible = true)` | method | `void` | public | Sets whether the visual layer is rendered onto the viewport. |
| `toggle_visible()` | method | `void` | public | Toggles whether the visual layer is rendered onto the viewport. |
| `get_generated_name()` | method | `QString` | public | Returns the automatically generated name for this layer. |
| `get_custom_name` | field | `boost::optional<QString>` | public | Returns the custom name explicitly given to this layer. |
| `set_custom_name( const boost::optional<QString> &custom_name)` | method | `void` | public | Sets the custom name for this layer. |
| `get_name()` | method | `QString` | public | Returns the custom name if it is set, or the automatically generated name if the custom name is not set. |
| `get_visual_layer_params()` | method | `VisualLayerParams::non_null_ptr_type` | public | Returns a non-const pointer to parameters and options specific to this type of visual layer. |
| `handle_params_modified()` | method | `void` | private | — |
| `emit_layer_modified()` | method | `void` | private | — |
| `d_visual_layers` | field | `VisualLayers` | private | — |
| `d_visual_layer_registry` | field | `VisualLayerRegistry` | private | — |
| `d_rendered_geometry_parameters` | field | `GPlatesViewOperations::RenderedGeometryParameters` | private | — |
| `d_render_settings` | field | `GPlatesGui::RenderSettings` | private | — |
| `d_symbol_map` | field | `GPlatesGui::symbol_map_type` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_layer` | field | `GPlatesAppLogic::Layer` | private | The reconstruct graph layer for which this is the counterpart in the presentation application tier. |
| `d_rendered_geometry_layer_index` | field | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_index_type` | private | The index of the rendered geometry layer to which this visual layer will place rendered geometries. |
| `d_rendered_geometry_layer` | field | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type` | private | A pointer to the rendered geometry layer to which this visual layer will place rendered geometries. |
| `d_widget_sections_expanded` | field | `bool` | private | Whether different sections of the visual layer are expanded in the user interface. |
| `d_visible` | field | `bool` | private | Whether this visual layer is rendered onto the viewport. |
| `d_custom_name` | field | `boost::optional<QString>` | private | The name that the user has explicitly given to this layer, if any. |
| `d_layer_number` | field | `int` | private | Each visual layer has a unique number that is used as a last resort to generate a name for the visual layer, if the usual methods for generating a name fail. |
| `d_visual_layer_params` | field | `VisualLayerParams::non_null_ptr_type` | private | Additional parameters or options specific to the visual layer type that this VisualLayer instance represents. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PRESENTATION_VISUALLAYER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=presentation/VisualLayer tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ScalarField3DLayerOptionsWidget](../qt-widgets/ScalarField3DLayerOptionsWidget.md) | qt-widgets | 84 |
| [presentation/VisualLayers](VisualLayers.md) | presentation | 44 |
| [qt-widgets/VisualLayersComboBox](../qt-widgets/VisualLayersComboBox.md) | qt-widgets | 42 |
| [qt-widgets/RasterLayerOptionsWidget](../qt-widgets/RasterLayerOptionsWidget.md) | qt-widgets | 34 |
| [qt-widgets/VisualLayerWidget](../qt-widgets/VisualLayerWidget.md) | qt-widgets | 29 |
| [presentation/TranscribeSession](TranscribeSession.md) | presentation | 26 |
| [qt-widgets/ReconstructScalarCoverageLayerOptionsWidget](../qt-widgets/ReconstructScalarCoverageLayerOptionsWidget.md) | qt-widgets | 25 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 24 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 22 |
| [presentation/VisualLayerRegistry](VisualLayerRegistry.md) | presentation | 20 |
| [qt-widgets/VelocityFieldCalculatorLayerOptionsWidget](../qt-widgets/VelocityFieldCalculatorLayerOptionsWidget.md) | qt-widgets | 15 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 12 |
| [gui/GlobeRenderedGeometryCollectionPainter](../gui/GlobeRenderedGeometryCollectionPainter.md) | gui | 10 |
| [qt-widgets/MergeReconstructionLayersDialog](../qt-widgets/MergeReconstructionLayersDialog.md) | qt-widgets | 10 |
| [qt-widgets/TotalReconstructionPolesDialog](../qt-widgets/TotalReconstructionPolesDialog.md) | qt-widgets | 10 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 9 |
| [qt-widgets/AssignReconstructionPlateIdsDialog](../qt-widgets/AssignReconstructionPlateIdsDialog.md) | qt-widgets | 9 |
| [gui/VelocityLegendOverlay](../gui/VelocityLegendOverlay.md) | gui | 7 |
| [gui/ExportDeformationAnimationStrategy](../gui/ExportDeformationAnimationStrategy.md) | gui | 6 |
| [gui/ExportScalarCoverageAnimationStrategy](../gui/ExportScalarCoverageAnimationStrategy.md) | gui | 6 |

*... and 18 more units.*

## Related

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_layer.get_layer_params().get()` | `modified(GPlatesAppLogic::LayerParams &)` | `this` | `handle_params_modified()` |
| `d_visual_layer_params.get()` | `modified()` | `this` | `handle_params_modified()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/VisualLayer.h
python scripts/gpq.py def GPlatesPresentation::VisualLayer --body
python scripts/gpq.py uses VisualLayer --kind class
python scripts/gpq.py hier VisualLayer
```

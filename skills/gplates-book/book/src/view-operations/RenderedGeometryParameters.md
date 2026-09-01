# RenderedGeometryParameters

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 240 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedGeometryParameters.h` | C++ | 481 |

## Overview

[[[PROSE overview unit=view-operations/RenderedGeometryParameters tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedGeometryParameters`](#gplatesviewoperationsrenderedgeometryparameters) | class | `QObject` | — | 0 | Parameters that specify how to draw geometry in the various canvas tools, and also some aspects (not covered by symboling/colouring/etc) of drawing the main reconstruction rendered layer. |

## Members

### `GPlatesViewOperations::RenderedGeometryParameters`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedGeometryParameters()` | constructor | `None` | public | Constructor sets the default parameter values. |
| `get_reconstruction_layer_point_size_hint()` | method | `float` | public | Point size for reconstruction layer. |
| `set_reconstruction_layer_point_size_hint( float reconstruction_layer_point_size_hint)` | method | `void` | public | — |
| `get_reconstruction_layer_line_width_hint()` | method | `float` | public | Line width for reconstruction layer. |
| `set_reconstruction_layer_line_width_hint( float reconstruction_layer_line_width_hint)` | method | `void` | public | — |
| `get_reconstruction_layer_topology_size_multiplier()` | method | `float` | public | Line width for topologies in reconstruction layer. |
| `set_reconstruction_layer_topology_size_multiplier( float reconstruction_layer_topology_size_multiplier)` | method | `void` | public | — |
| `get_reconstruction_layer_ratio_arrow_unit_vector_direction_to_globe_radius()` | method | `float` | public | Scaling for arrow bodies in reconstruction layer. |
| `set_reconstruction_layer_ratio_arrow_unit_vector_direction_to_globe_radius( float reconstruction_layer_ratio_arrow_unit_vector_direction_to_globe_radius)` | method | `void` | public | — |
| `get_reconstruction_layer_ratio_arrowhead_size_to_globe_radius()` | method | `float` | public | Scaling for arrowheads in reconstruction layer. |
| `set_reconstruction_layer_ratio_arrowhead_size_to_globe_radius( float reconstruction_layer_ratio_arrowhead_size_to_globe_radius)` | method | `void` | public | — |
| `get_reconstruction_layer_arrow_spacing()` | method | `float` | public | The screen-space spacing of rendered arrows in reconstruction layer. |
| `set_reconstruction_layer_arrow_spacing( float reconstruction_layer_arrow_spacing)` | method | `void` | public | — |
| `get_choose_feature_tool_point_size_hint()` | method | `float` | public | Point size for rendering the actual focus geometry clicked by user. |
| `set_choose_feature_tool_point_size_hint( float point_size)` | method | `void` | public | — |
| `get_choose_feature_tool_line_width_hint()` | method | `float` | public | Line width for rendering the actual focus geometry clicked by user. |
| `set_choose_feature_tool_line_width_hint( float line_width)` | method | `void` | public | — |
| `set_choose_feature_tool_clicked_geometry_of_focused_feature_colour( const GPlatesGui::Colour &colour)` | method | `void` | public | — |
| `set_choose_feature_tool_non_clicked_geometry_of_focused_feature_colour( const GPlatesGui::Colour &colour)` | method | `void` | public | — |
| `set_topology_tool_focused_geometry_colour( const GPlatesGui::Colour &colour)` | method | `void` | public | — |
| `get_topology_tool_focused_geometry_point_size_hint()` | method | `float` | public | Point size for rendering focus geometry in topology tools. |
| `set_topology_tool_focused_geometry_point_size_hint( float point_size_hint)` | method | `void` | public | — |
| `get_topology_tool_focused_geometry_line_width_hint()` | method | `float` | public | Line width for rendering focus geometry in topology tools. |
| `set_topology_tool_focused_geometry_line_width_hint( float line_width_hint)` | method | `void` | public | — |
| `set_topology_tool_topological_sections_colour( const GPlatesGui::Colour &colour)` | method | `void` | public | — |
| `get_topology_tool_topological_sections_point_size_hint()` | method | `float` | public | Point size for rendering topological sections in topology tools. |
| `set_topology_tool_topological_sections_point_size_hint( float point_size_hint)` | method | `void` | public | — |
| `get_topology_tool_topological_sections_line_width_hint()` | method | `float` | public | Line width for rendering topological sections in topology tools. |
| `set_topology_tool_topological_sections_line_width_hint( float line_width_hint)` | method | `void` | public | — |
| `parameters_changed( GPlatesViewOperations::RenderedGeometryParameters &)` | method | `void` | public | — |
| `d_reconstruction_layer_point_size_hint` | field | `float` | private | — |
| `d_reconstruction_layer_line_width_hint` | field | `float` | private | — |
| `d_reconstruction_layer_topology_size_multiplier` | field | `float` | private | — |
| `d_reconstruction_layer_ratio_arrow_unit_vector_direction_to_globe_radius` | field | `float` | private | — |
| `d_reconstruction_layer_ratio_arrowhead_size_to_globe_radius` | field | `float` | private | — |
| `d_reconstruction_layer_arrow_spacing` | field | `float` | private | — |
| `d_choose_feature_tool_point_size_hint` | field | `float` | private | — |
| `d_choose_feature_tool_line_width_hint` | field | `float` | private | — |
| `d_choose_feature_tool_clicked_geometry_of_focused_feature_colour` | field | `GPlatesGui::Colour` | private | — |
| `d_choose_feature_tool_non_clicked_geometry_of_focused_feature_colour` | field | `GPlatesGui::Colour` | private | — |
| `d_topology_tool_focused_geometry_colour` | field | `GPlatesGui::Colour` | private | — |
| `d_topology_tool_focused_geometry_point_size_hint` | field | `float` | private | — |
| `d_topology_tool_focused_geometry_line_width_hint` | field | `float` | private | — |
| `d_topology_tool_topological_sections_colour` | field | `GPlatesGui::Colour` | private | — |
| `d_topology_tool_topological_sections_point_size_hint` | field | `float` | private | — |
| `d_topology_tool_topological_sections_line_width_hint` | field | `float` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYPARAMETERS_H` | macro | `None` | — |
| `DEFAULT_POINT_SIZE_HINT` | variable | `float` | Default point size hint used by most (or all) layers. |
| `DEFAULT_LINE_WIDTH_HINT` | variable | `float` | Default line width hint used by most (or all) layers. |
| `POLE_MANIPULATION_POINT_SIZE_HINT` | variable | `float` | Point size for reconstruction layer. |
| `POLE_MANIPULATION_LINE_WIDTH_HINT` | variable | `float` | Line width for reconstruction layer. |
| `TOPOLOGY_TOOL_LINE_WIDTH_HINT` | variable | `float` | Line width for reconstruction layer. |
| `LINE_WIDTH_HINT` | variable | `float` | Width of lines to render in the most general case. |
| `HIGHLIGHT_LINE_WIDTH_HINT` | variable | `float` | Width of lines for rendering those parts of geometry that need highlighting to indicate, to the user, that an operation is possible. |
| `SECONDARY_LINE_WIDTH_HINT` | variable | `float` | Line width for move-vertex secondary geometries. |
| `REGULAR_POINT_SIZE_HINT` | variable | `float` | Regular size of point to render at each point/vertex. |
| `LARGE_POINT_SIZE_HINT` | variable | `float` | Large size of point to render at each point/vertex. |
| `EXTRA_LARGE_POINT_SIZE_HINT` | variable | `float` | Extra large size of point to render at each point/vertex. |
| `FOCUS_COLOUR` | variable | `GPlatesGui::Colour` | Colour to use for rendering those parts of geometry that are in focus. |
| `SPLIT_FEATURE_START_POINT_COLOUR` | variable | `GPlatesGui::Colour` | Colour to be used for rendering points for "split feature" tool. |
| `SPLIT_FEATURE_MIDDLE_POINT_COLOUR` | variable | `GPlatesGui::Colour` | — |
| `SPLIT_FEATURE_END_POINT_COLOUR` | variable | `GPlatesGui::Colour` | — |
| `NOT_IN_FOCUS_COLOUR` | variable | `GPlatesGui::Colour` | Colour to use for rendering those parts of geometry that are not in focus. |
| `HIGHLIGHT_COLOUR` | variable | `GPlatesGui::Colour` | Colour to use for rendering those parts of geometry that need highlighting to indicate, to the user, that an operation is possible. |
| `DELETE_COLOUR` | variable | `GPlatesGui::Colour` | Colour to use for rendering those parts of geometry that can be deleted. |

## Notes

[[[PROSE notes unit=view-operations/RenderedGeometryParameters tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/MoveVertexGeometryOperation](MoveVertexGeometryOperation.md) | view-operations | 36 |
| [qt-widgets/ConfigureCanvasToolGeometryRenderParametersDialog](../qt-widgets/ConfigureCanvasToolGeometryRenderParametersDialog.md) | qt-widgets | 31 |
| [view-operations/SplitFeatureGeometryOperation](SplitFeatureGeometryOperation.md) | view-operations | 25 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 24 |
| [view-operations/AddPointGeometryOperation](AddPointGeometryOperation.md) | view-operations | 21 |
| [view-operations/DeleteVertexGeometryOperation](DeleteVertexGeometryOperation.md) | view-operations | 19 |
| [view-operations/InsertVertexGeometryOperation](InsertVertexGeometryOperation.md) | view-operations | 17 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 13 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 9 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 6 |
| [presentation/VelocityFieldCalculatorVisualLayerParams](../presentation/VelocityFieldCalculatorVisualLayerParams.md) | presentation | 6 |
| [gui/GeometryFocusHighlight](../gui/GeometryFocusHighlight.md) | gui | 3 |
| [qt-widgets/deprecated/CreateTopologyWidget](../qt-widgets/deprecated/CreateTopologyWidget.md) | qt-widgets | 3 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 1 |
| [gui/PoleManipulationCanvasToolWorkflow](../gui/PoleManipulationCanvasToolWorkflow.md) | gui | 1 |
| [gui/TopologyCanvasToolWorkflow](../gui/TopologyCanvasToolWorkflow.md) | gui | 1 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 1 |
| [presentation/VisualLayer](../presentation/VisualLayer.md) | presentation | 1 |
| [presentation/VisualLayers](../presentation/VisualLayers.md) | presentation | 1 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 1 |

*... and 2 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedGeometryParameters.h
python scripts/gpq.py def GPlatesViewOperations::RenderedGeometryParameters --body
python scripts/gpq.py uses RenderedGeometryParameters --kind class
python scripts/gpq.py hier RenderedGeometryParameters
```

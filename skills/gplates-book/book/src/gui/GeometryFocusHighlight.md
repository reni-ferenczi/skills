# GeometryFocusHighlight

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 16 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/GeometryFocusHighlight.h` | C++ | 80 |
| `src/gui/GeometryFocusHighlight.cc` | C++ | 171 |

## Overview

A utility namespace that renders the geometry of a focused feature into a specified rendered geometry layer. If there is a focused geometry, the function renders all reconstruction geometries of the focused feature across all geometry properties; the clicked geometry is highlighted in white and all other geometries of the same feature are rendered in grey. Non-clicked geometries are rendered first to avoid occluding the clicked geometry. If no geometry is focused, the layer is cleared.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_GEOMETRYFOCUSHIGHLIGHT_H` | macro | `None` | — |
| `draw_focused_geometry( FeatureFocus &feature_focus, GPlatesViewOperations::RenderedGeometryLayer &render_geom_layer, GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, const GPlatesViewOperations::RenderedGeometryParameters &rendered_geometry_parameters, const GPlatesGui::RenderSettings &rende ...` | function | `void` | Draw the focused geometry (if there is one) into the specified rendered geometry layer. |

## Notes

Renders all reconstruction geometries of the focused feature across all layers, not just those from the layer that contains the clicked geometry. This handles cases where a feature is reconstructed in multiple layers and the user may click on a geometry from any layer. The function assumes the caller is responsible for activating and deactivating the specified rendered geometry layer.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FeatureInspectionCanvasToolWorkflow](FeatureInspectionCanvasToolWorkflow.md) | gui | 3 |
| [gui/PoleManipulationCanvasToolWorkflow](PoleManipulationCanvasToolWorkflow.md) | gui | 3 |
| [gui/TopologyCanvasToolWorkflow](TopologyCanvasToolWorkflow.md) | gui | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/GeometryFocusHighlight.h
```

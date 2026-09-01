# GeometryFocusHighlight

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 16 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/GeometryFocusHighlight.h` | C++ | 80 |
| `src/gui/GeometryFocusHighlight.cc` | C++ | 171 |

## Overview

[[[PROSE overview unit=gui/GeometryFocusHighlight tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=gui/GeometryFocusHighlight tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

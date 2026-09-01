# VelocityFieldCalculatorVisualLayerParams

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 465 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/VelocityFieldCalculatorVisualLayerParams.h` | C++ | 146 |

## Overview

[[[PROSE overview unit=presentation/VelocityFieldCalculatorVisualLayerParams tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::VelocityFieldCalculatorVisualLayerParams`](#gplatespresentationvelocityfieldcalculatorvisuallayerparams) | class | [`VisualLayerParams`](VisualLayerParams.md) | — | 0 | — |

## Members

### `GPlatesPresentation::VelocityFieldCalculatorVisualLayerParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<VelocityFieldCalculatorVisualLayerParams>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const VelocityFieldCalculatorVisualLayerParams>` | public | — |
| `create( GPlatesAppLogic::LayerParams::non_null_ptr_type layer_params, const GPlatesViewOperations::RenderedGeometryParameters &rendered_geometry_parameters)` | method | `non_null_ptr_type` | public | — |
| `get_arrow_body_scale()` | method | `float` | public | — |
| `set_arrow_body_scale( float arrow_body_scale)` | method | `void` | public | Set the arrow body scale of rendered arrows. |
| `get_arrowhead_scale()` | method | `float` | public | — |
| `set_arrowhead_scale( float arrowhead_scale)` | method | `void` | public | Set the arrowhead scale of rendered arrows. |
| `get_arrow_spacing()` | method | `float` | public | — |
| `set_arrow_spacing( float arrow_spacing)` | method | `void` | public | Set the screen-space spacing of rendered arrows. |
| `accept_visitor( ConstVisualLayerParamsVisitor &visitor)` | method | `void` | public | — |
| `accept_visitor( VisualLayerParamsVisitor &visitor)` | method | `void` | public | — |
| `VelocityFieldCalculatorVisualLayerParams( GPlatesAppLogic::LayerParams::non_null_ptr_type layer_params, const GPlatesViewOperations::RenderedGeometryParameters &rendered_geometry_parameters)` | constructor | `None` | protected | — |
| `d_arrow_spacing` | field | `float` | private | — |
| `d_arrow_body_scale` | field | `float` | private | — |
| `d_arrowhead_scale` | field | `float` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PRESENTATION_VELOCITYFIELDCALCULATORVISAULLAYERPARAMS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=presentation/VelocityFieldCalculatorVisualLayerParams tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/VelocityFieldCalculatorLayerOptionsWidget](../qt-widgets/VelocityFieldCalculatorLayerOptionsWidget.md) | qt-widgets | 15 |
| [gui/VelocityLegendOverlay](../gui/VelocityLegendOverlay.md) | gui | 7 |
| [presentation/TranscribeSession](TranscribeSession.md) | presentation | 7 |
| [presentation/ReconstructionGeometryRenderer](ReconstructionGeometryRenderer.md) | presentation | 5 |
| [presentation/VisualLayerRegistry](VisualLayerRegistry.md) | presentation | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/VelocityFieldCalculatorVisualLayerParams.h
python scripts/gpq.py def GPlatesPresentation::VelocityFieldCalculatorVisualLayerParams --body
python scripts/gpq.py uses VelocityFieldCalculatorVisualLayerParams --kind class
python scripts/gpq.py hier VelocityFieldCalculatorVisualLayerParams
```

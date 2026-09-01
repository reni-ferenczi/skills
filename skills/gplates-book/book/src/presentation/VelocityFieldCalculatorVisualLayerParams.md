# VelocityFieldCalculatorVisualLayerParams

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 465 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/VelocityFieldCalculatorVisualLayerParams.h` | C++ | 146 |

## Overview

`GPlatesPresentation::VelocityFieldCalculatorVisualLayerParams` is the `VisualLayerParams` for a velocity-field-calculator layer, and it is deliberately thin: three `float`s describing how the velocity arrows should look, with the velocity computation left entirely to the app-logic layer and its `LayerParams`. There is no logic in the header beyond storing the values and calling `emit_modified()`, so the interesting behaviour lives in what consumes them — `ReconstructionGeometryRenderer` feeds `get_arrow_spacing()` straight into `ratio_zoom_dependent_bin_dimension_to_globe_radius`, making it a binning parameter rather than a cosmetic one (see Notes).

The three values are seeded, not defaulted in-class: the constructor pulls them from the `GPlatesViewOperations::RenderedGeometryParameters` passed to `create()`, taking the global reconstruction-layer arrow spacing and the two arrow-to-globe-radius ratios. A layer therefore starts out matching the application-wide arrow appearance and diverges only once the user edits it in `VelocityFieldCalculatorLayerOptionsWidget`.

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

- **`set_arrow_spacing()` is the one call here with teeth.** The header
  (VelocityFieldCalculatorVisualLayerParams.h:91-99) documents two things the
  signature does not: a value of **zero is a special case meaning unlimited
  density** — no cap on the number of arrows — and **small non-zero values can
  cause large memory usage**. Zero is not "no spacing"; it disables the limit
  altogether. The options widget exposes this explicitly, with a dedicated
  "unlimited" button that sets the spinbox to 0.
- The memory warning follows from where the value ends up: it becomes
  `ratio_zoom_dependent_bin_dimension_to_globe_radius` in
  `ReconstructionGeometryRenderer`, i.e. the size of the bins used to thin out
  arrows. Halving the spacing quarters the bin area, so the bin count — and the
  arrows retained — grows quadratically as the value shrinks. Nothing in this
  class clamps or validates the argument.
- No accessor here validates or clamps anything; every setter simply assigns and
  calls `emit_modified()`. Negative or absurd scales are accepted and left for
  the renderer to deal with.

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

# VisualLayerParams

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 245 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/VisualLayerParams.h` | C++ | 167 |

## Overview

`VisualLayerParams` is the base class for parameters and options that are specific to visualising a particular type of layer, kept separate from `GPlatesAppLogic::LayerParams` so that presentation-only settings (colouring, symbology, display toggles) never leak into the app-logic layer that actually computes reconstructions. Each visual layer type that needs its own options derives from this class; the seven subclasses correspond to the layer types registered in `VisualLayerRegistry`.

The class wraps a `GPlatesAppLogic::LayerParams::non_null_ptr_type`, giving derived classes access to the underlying layer's own parameters through the protected `get_layer_params()`, and an optional `GPlatesGui::StyleAdapter` used to override the default drawing style. Double dispatch onto a subclass is done through `accept_visitor`, which takes either a `ConstVisualLayerParamsVisitor` or a `VisualLayerParamsVisitor` (see `VisualLayerParamsVisitor`); the base implementations are no-ops, so a subclass that does not override `accept_visitor` is simply invisible to visitors.

`handle_layer_modified` is the hook by which a `VisualLayerParams` learns that its owning app-logic layer's input connections changed; the base implementation does nothing, and it is guaranteed to also be called once right after construction so a subclass can initialise itself from the current layer state.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::VisualLayerParams`](#gplatespresentationvisuallayerparams) | class | `QObject`<br>[`GPlatesUtils::ReferenceCount<VisualLayerParams>`](../utils/ReferenceCount.md) | — | 7 | This is the base class of classes that store parameters and options specific to particular types of visual layers. |

## Members

### `GPlatesPresentation::VisualLayerParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<VisualLayerParams>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const VisualLayerParams>` | public | — |
| `create( GPlatesAppLogic::LayerParams::non_null_ptr_type layer_params)` | method | `non_null_ptr_type` | public | — |
| `~VisualLayerParams()` | destructor | `None` | public | — |
| `accept_visitor( ConstVisualLayerParamsVisitor &visitor)` | method | `void` | public | — |
| `accept_visitor( VisualLayerParamsVisitor &visitor)` | method | `void` | public | — |
| `handle_layer_modified( const GPlatesAppLogic::Layer &layer)` | method | `void` | public | Subclasses should override this to get notified when the app-logic layer corresponding to the parent visual layer has had an input connection added or removed. |
| `set_style_adapter( const GPlatesGui::StyleAdapter* adapter)` | method | `void` | public | — |
| `style_adapter()` | method | `GPlatesGui::StyleAdapter` | public | — |
| `modified()` | method | `void` | public | Emitted when any aspect of the parameters has been modified. |
| `VisualLayerParams( GPlatesAppLogic::LayerParams::non_null_ptr_type layer_params, const GPlatesGui::StyleAdapter* style = NULL)` | constructor | `None` | protected | — |
| `get_layer_params()` | method | `GPlatesAppLogic::LayerParams::non_null_ptr_type` | protected | — |
| `emit_modified()` | method | `void` | protected | Subclasses should call this method to cause the modified() signal to be emitted. |
| `d_layer_params` | field | `GPlatesAppLogic::LayerParams::non_null_ptr_type` | private | — |
| `d_style` | field | `GPlatesGui::StyleAdapter` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PRESENTATION_VISUALLAYERPARAMS_H` | macro | `None` | — |

## Notes

Subclasses should call `emit_modified()` (not `Q_EMIT modified()` directly) whenever they change a parameter, so that listeners are notified consistently through the one signal.

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/ReconstructVisualLayerParams](ReconstructVisualLayerParams.md) | presentation | 15 |
| [presentation/ReconstructScalarCoverageVisualLayerParams](ReconstructScalarCoverageVisualLayerParams.md) | presentation | 8 |
| [presentation/VisualLayer](VisualLayer.md) | presentation | 8 |
| [presentation/VisualLayerRegistry](VisualLayerRegistry.md) | presentation | 7 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 7 |
| [presentation/ScalarField3DVisualLayerParams](ScalarField3DVisualLayerParams.md) | presentation | 6 |
| [presentation/TranscribeSession](TranscribeSession.md) | presentation | 5 |
| [presentation/RasterVisualLayerParams](RasterVisualLayerParams.md) | presentation | 4 |
| [presentation/TopologyNetworkVisualLayerParams](TopologyNetworkVisualLayerParams.md) | presentation | 4 |
| [presentation/TopologyGeometryVisualLayerParams](TopologyGeometryVisualLayerParams.md) | presentation | 3 |
| [presentation/VelocityFieldCalculatorVisualLayerParams](VelocityFieldCalculatorVisualLayerParams.md) | presentation | 3 |
| [gui/VelocityLegendOverlay](../gui/VelocityLegendOverlay.md) | gui | 2 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/VisualLayerParams.h
python scripts/gpq.py def GPlatesPresentation::VisualLayerParams --body
python scripts/gpq.py uses VisualLayerParams --kind class
python scripts/gpq.py hier VisualLayerParams
```

# LayerParams

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 399 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/LayerParams.h` | C++ | 99 |

## Overview

A layer's configuration is split in two along the app-logic / presentation line.
Anything that changes what a layer *computes* — the band of a raster, the
velocity delta time, the deformation options — lives in a `LayerParams`
subclass owned by the layer's `LayerTask`; anything that only changes how the
result is *drawn* lives in the parallel `GPlatesPresentation::VisualLayerParams`
hierarchy. This class is the app-logic half's root, and it exists mainly to give
that half a common type: `Layer::get_layer_params()` returns it, the eight
concrete subclasses supply the actual fields, and `LayerParamsVisitor` /
`ConstLayerParamsVisitor` recover the derived type for code that needs it.

Its one real behaviour is the change notification. `ReconstructGraph::add_layer`
connects each new layer's params `modified()` signal to its own
`handle_layer_params_changed` slot, which finds the owning layer and re-emits it
as the graph-level `layer_params_changed(Layer &, LayerParams &)`; that is how a
settings edit made in a layer options widget becomes a reconstruction. A
subclass mutator therefore has one obligation — call `emit_modified()` when it
actually changes something — and gets the whole invalidation chain for free.

The base is directly instantiable via `create()`, and its `accept_visitor`
overrides do nothing. That is the parameterless case: a layer type with no
options still hands out a `LayerParams` so that callers never have to test for
absence.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::LayerParams`](#gplatesapplogiclayerparams) | class | `QObject`<br>[`GPlatesUtils::ReferenceCount<LayerParams>`](../utils/ReferenceCount.md) | — | 8 | This is the base class of classes that store parameters and options specific to particular types of layers (layer task types). |

## Members

### `GPlatesAppLogic::LayerParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<LayerParams>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const LayerParams>` | public | — |
| `create()` | method | `non_null_ptr_type` | public | — |
| `~LayerParams()` | destructor | `None` | public | — |
| `accept_visitor( ConstLayerParamsVisitor &visitor)` | method | `void` | public | — |
| `accept_visitor( LayerParamsVisitor &visitor)` | method | `void` | public | — |
| `modified( GPlatesAppLogic::LayerParams &layer_params)` | method | `void` | public | Emitted when any aspect of the parameters has been modified. |
| `emit_modified()` | method | `void` | protected | Subclasses should call this method to cause the modified() signal to be emitted. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_LAYERPARAMS_H` | macro | `None` | — |

## Notes

- **Double ownership: `QObject` parent *and* intrusive refcount.** The object is
  reference-counted through `GPlatesUtils::ReferenceCount` and passed around as
  `non_null_ptr_type`, but it is also a `QObject` — created with no parent, so
  Qt does not delete it. Lifetime is the refcount's alone, held via the
  `LayerTask` that `ReconstructGraphImpl::Layer::get_layer_params()` forwards to.
  Never give one a `QObject` parent, and never hold a raw pointer past the
  layer's removal.
- **`emit_modified()` is the whole contract for subclasses.** Nothing polls
  these objects; if a setter changes state without emitting, the layer proxy is
  never invalidated and the change silently does not take effect. Subclasses
  that also define their own finer-grained signals — `RasterLayerParams` emits
  `modified_band_name` — still emit the base `modified()` alongside them.
- **Not every base-class virtual is meaningful in the base.** `accept_visitor`
  has empty bodies rather than being pure, so a subclass that forgets to
  override it compiles and links, and simply never dispatches. When adding a
  `LayerParams` subclass you must also add its forward declaration and
  `visit_*` method to `LayerParamsVisitorBase` — those are likewise empty
  by default, so the compiler will not remind you.
- `ReconstructGraph::handle_layer_params_changed` locates the owning layer by
  scanning `d_layers` and comparing raw pointers, and deliberately does nothing
  if no match is found (the comment covers params modified while the layer is
  being removed). A params object detached from its layer therefore produces no
  graph-level signal rather than an error.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 97 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 59 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 51 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 49 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 43 |
| [app-logic/TopologyGeometryResolverLayerTask](TopologyGeometryResolverLayerTask.md) | app-logic | 34 |
| [gui/FeatureTableModel](../gui/FeatureTableModel.md) | gui | 34 |
| [presentation/VisualLayerRegistry](../presentation/VisualLayerRegistry.md) | presentation | 31 |
| [presentation/TopologyNetworkVisualLayerParams](../presentation/TopologyNetworkVisualLayerParams.md) | presentation | 30 |
| [app-logic/TopologyNetworkResolverLayerTask](TopologyNetworkResolverLayerTask.md) | app-logic | 28 |
| [qt-widgets/CreateVGPDialog](../qt-widgets/CreateVGPDialog.md) | qt-widgets | 28 |
| [app-logic/ReconstructLayerTask](ReconstructLayerTask.md) | app-logic | 27 |
| [presentation/ScalarField3DVisualLayerParams](../presentation/ScalarField3DVisualLayerParams.md) | presentation | 27 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 27 |
| [app-logic/LayerProxyUtils](LayerProxyUtils.md) | app-logic | 26 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 21 |
| [view-operations/FocusedFeatureGeometryManipulator](../view-operations/FocusedFeatureGeometryManipulator.md) | view-operations | 19 |
| [presentation/ReconstructScalarCoverageVisualLayerParams](../presentation/ReconstructScalarCoverageVisualLayerParams.md) | presentation | 18 |
| [app-logic/ReconstructGraphImpl](ReconstructGraphImpl.md) | app-logic | 16 |
| [qt-widgets/CreateSmallCircleFeatureDialog](../qt-widgets/CreateSmallCircleFeatureDialog.md) | qt-widgets | 16 |

*... and 95 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/LayerParams.h
python scripts/gpq.py def GPlatesAppLogic::LayerParams --body
python scripts/gpq.py uses LayerParams --kind class
python scripts/gpq.py hier LayerParams
```

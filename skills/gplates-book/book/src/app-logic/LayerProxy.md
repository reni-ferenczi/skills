# LayerProxy

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1671 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/LayerProxy.h` | C++ | 110 |

## Overview

This tiny header declares the root of the pull model that the whole
reconstruction pipeline is built on. The class comment states the history
plainly: layers used to be *executed*, each pushing its results (typically
`ReconstructionGeometry` objects) into its output; now every layer instead
exposes one long-lived `LayerProxy` object at its output, and nothing is
computed until a client — a painter, an exporter, or a downstream layer that
has this one connected as an input — actually asks for it. `Layer::get_layer_output()`
is the door into that world, and the nine concrete proxies (one per layer kind:
reconstruction, reconstruct, raster, scalar field, the two topology resolvers,
velocity, scalar coverage, co-registration) each define their own rich,
type-specific query interface rather than sharing a generic "execute" signature.

The base itself deliberately declares almost nothing. Because the interesting
methods live only on the derived types, every consumer has to recover the
derived type first — either by `accept_visitor` against the `LayerProxyVisitor`
/ `ConstLayerProxyVisitor` hierarchy, or through the `LayerProxyUtils` helpers
and the templated `Layer::get_layer_output<Derived>()` that wrap the same
downcast in a `boost::optional`.

`LayerProxyHandle` is the other half of the design and exists for a specific
reason given in its comment: sometimes you need a stable pointer *identifying*
a layer's output without being allowed to use it. `Layer::get_layer_output()`
withholds the `LayerProxy` when the layer is inactive, but
`Layer::get_layer_proxy_handle()` always returns the handle — which is why
`GLVisualLayers::handle_layer_about_to_be_removed` uses the handle as the key
for evicting a removed layer's cached OpenGL resources.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::LayerProxyHandle`](#gplatesapplogiclayerproxyhandle) | class | [`GPlatesUtils::ReferenceCount<LayerProxyHandle>`](../utils/ReferenceCount.md) | — | 10 | A handle to a layer proxy. |
| [`GPlatesAppLogic::LayerProxy`](#gplatesapplogiclayerproxy) | class | [`LayerProxyHandle`](LayerProxy.md) | — | 9 | Base class for layer proxies. |

## Members

### `GPlatesAppLogic::LayerProxyHandle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<LayerProxyHandle>` | public | Convenience typedefs for a shared pointer to a LayerProxyHandle. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const LayerProxyHandle>` | public | — |
| `~LayerProxyHandle()` | destructor | `None` | public | — |

### `GPlatesAppLogic::LayerProxy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<LayerProxy>` | public | Convenience typedefs for a shared pointer to a LayerProxy. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const LayerProxy>` | public | — |
| `~LayerProxy()` | destructor | `None` | public | — |
| `accept_visitor( ConstLayerProxyVisitor &visitor)` | method | `void` | public | Accept a ConstLayerProxyVisitor instance. |
| `accept_visitor( LayerProxyVisitor &visitor)` | method | `void` | public | Accept a LayerProxyVisitor instance. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_LAYERPROXY_H` | macro | `None` | — |

## Notes

- **Caching is a subclass obligation, not something the base provides.** The
  class comment requires derived proxies to cache their results, because in a
  pull model the same computation is otherwise redone for every client that
  asks. There is no shared cache, no shared invalidation, and no base-class hook
  — each proxy rolls its own, and if you add one that does not, the cost shows
  up as repeated work per frame rather than as a bug.
- **Invalidation runs on `GPlatesUtils::SubjectToken`, not on Qt signals.**
  Each concrete proxy owns a `SubjectToken` exposed through `get_subject_token()`;
  a downstream proxy keeps a matching `ObserverToken` and compares them to decide
  whether its own cache is stale. The token is just a 64-bit counter, so an
  observer created fresh is *out of date by construction* (`SubjectToken`'s
  constructor invalidates by default) and will always recompute once. Add
  `invalidate()` calls to every mutator you add to a proxy; a missed one silently
  serves stale geometry.
- **A proxy outlives any single reconstruction.** It is reference-counted via
  `GPlatesUtils::ReferenceCount` and held by the layer's
  `ReconstructGraphImpl::Data`, so it persists across reconstruction times and
  parameter edits, accumulating cached state. Holding a `non_null_ptr_type` keeps
  it alive after its layer is removed from the graph — which is exactly why
  `GLVisualLayers` must explicitly evict on `layer_about_to_be_removed` rather
  than relying on the pointer dying.
- `LayerProxy::accept_visitor` is pure virtual (unlike its counterpart on
  `LayerParams`), so a new proxy subclass cannot silently skip visitor
  dispatch — but you must still add the corresponding `visit()` overload to
  `LayerProxyVisitor` for anything to receive it.
- Everything here is single-threaded: computation happens synchronously inside
  the caller's `get_*` call, on whichever thread asked. There is no locking in
  the proxies or in `SubjectToken`.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 56 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 45 |
| [app-logic/RasterLayerProxy](RasterLayerProxy.md) | app-logic | 38 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 38 |
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 32 |
| [app-logic/PartitionFeatureUtils](PartitionFeatureUtils.md) | app-logic | 30 |
| [app-logic/ScalarField3DLayerProxy](ScalarField3DLayerProxy.md) | app-logic | 28 |
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 26 |
| [app-logic/DependentTopologicalSectionLayers](DependentTopologicalSectionLayers.md) | app-logic | 25 |
| [feature-visitors/ViewFeatureGeometriesWidgetPopulator](../feature-visitors/ViewFeatureGeometriesWidgetPopulator.md) | feature-visitors | 23 |
| [app-logic/VelocityFieldCalculatorLayerProxy](VelocityFieldCalculatorLayerProxy.md) | app-logic | 21 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 18 |
| [app-logic/TopologyGeometryResolver](TopologyGeometryResolver.md) | app-logic | 16 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 16 |
| [app-logic/ReconstructGraphImpl](ReconstructGraphImpl.md) | app-logic | 12 |
| [app-logic/ReconstructScalarCoverageLayerProxy](ReconstructScalarCoverageLayerProxy.md) | app-logic | 12 |
| [app-logic/RasterLayerTask](RasterLayerTask.md) | app-logic | 10 |
| [app-logic/ReconstructionGeometryFinder](ReconstructionGeometryFinder.md) | app-logic | 10 |
| [app-logic/VelocityFieldCalculatorLayerTask](VelocityFieldCalculatorLayerTask.md) | app-logic | 10 |
| [app-logic/ReconstructionLayerProxy](ReconstructionLayerProxy.md) | app-logic | 9 |

*... and 23 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/LayerProxy.h
python scripts/gpq.py def GPlatesAppLogic::LayerProxy --body
python scripts/gpq.py uses LayerProxy --kind class
python scripts/gpq.py hier LayerProxy
```

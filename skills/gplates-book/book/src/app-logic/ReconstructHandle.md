# ReconstructHandle

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 2 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructHandle.h` | C++ | 79 |

## Overview

A header-only ticket dispenser. It exists to solve one problem in the
reconstruction pipeline: a single `FeatureHandle` can be reconstructed many
times over, in different layers and different situations, and each run leaves a
`ReconstructedFeatureGeometry` attached to the feature as a weak observer. When
a client later walks a feature's observers it needs to tell *its own* results
apart from everybody else's. A reconstruct handle is the tag that does that.
`ReconstructionGeometry` stores one as a `boost::optional<ReconstructHandle::type>`
member, and finders such as `ReconstructedFeatureGeometryFinder` filter on it.

The workflow is: whoever is about to produce a group of reconstruction
geometries calls `get_next_reconstruct_handle()` once, stamps every geometry in
the group with the value it got back, and hands the handle to whoever needs to
find that group again. The heavy fan-in on this header — the layer proxies, the
topology resolvers, `ReconstructContext`, `ReconstructUtils` — is almost
entirely of that shape.

The header notes explicitly why there is no `get_current_reconstruct_handle()`:
with a getter for the last-issued value, a client could stamp its geometries
with a handle another client is already using and silently pollute that group.
Issuing is therefore the only operation, and a handle is opaque — the underlying
`GPlatesUtils::Counter64` supports only increment and comparison, never
arithmetic or decrement.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructHandle::type`](#gplatesapplogicreconstructhandletype) | typedef | — | — | 0 | Typedef for a global handle that is stored in ReconstructionGeometry instances to identity them, for example, as belonging to a particular group of reconstructed feature geometries. |

## Members

### `GPlatesAppLogic::ReconstructHandle::type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTHANDLE_H` | macro | `None` | — |
| `get_next_reconstruct_handle()` | function | `type` | Returns the next global reconstruct handle by incrementing the integer handle returned by the last call to get\_next\_reconstruct\_handle. |

## Notes

**Not thread-safe.** `get_next_reconstruct_handle()` increments a function-local
`static` with no synchronisation. The source carries a TODO saying it will need
protecting, or converting to a singleton, if GPlates ever becomes
multi-threaded. Any change that introduces concurrent reconstruction has to deal
with this line first.

**Handles are process-global and never reused.** The counter is monotonic and
64-bit specifically so it cannot wrap: `GPlatesUtils::Counter64` documents that
at one increment per cycle on a 3 GHz machine wraparound takes around 195 years,
whereas a 32-bit counter would wrap in seconds. Correctness of every
handle-based lookup rests on that, so do not narrow the type. There is no
release or recycle step — handles are simply spent.

**Call it once per group, not once per geometry.** Each call yields a distinct
value, so calling it inside the loop that creates geometries gives every
geometry its own group and breaks any subsequent lookup by handle.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 109 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 80 |
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 73 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 59 |
| [app-logic/ReconstructContext](ReconstructContext.md) | app-logic | 57 |
| [app-logic/ReconstructUtils](ReconstructUtils.md) | app-logic | 32 |
| [app-logic/TopologyGeometryResolver](TopologyGeometryResolver.md) | app-logic | 31 |
| [app-logic/ReconstructedFeatureGeometryFinder](ReconstructedFeatureGeometryFinder.md) | app-logic | 30 |
| [app-logic/ReconstructedFeatureGeometry](ReconstructedFeatureGeometry.md) | app-logic | 26 |
| [app-logic/ReconstructScalarCoverageLayerProxy](ReconstructScalarCoverageLayerProxy.md) | app-logic | 23 |
| [app-logic/ReconstructionGeometryFinder](ReconstructionGeometryFinder.md) | app-logic | 19 |
| [app-logic/LayerProxyUtils](LayerProxyUtils.md) | app-logic | 18 |
| [view-operations/RenderedGeometryUtils](../view-operations/RenderedGeometryUtils.md) | view-operations | 18 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 15 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 11 |
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 10 |
| [app-logic/ReconstructMethodInterface](ReconstructMethodInterface.md) | app-logic | 9 |
| [app-logic/SmallCircleGeometryPopulator](SmallCircleGeometryPopulator.md) | app-logic | 9 |
| [app-logic/ReconstructMethodByPlateId](ReconstructMethodByPlateId.md) | app-logic | 8 |
| [app-logic/ReconstructMethodHalfStageRotation](ReconstructMethodHalfStageRotation.md) | app-logic | 8 |

*... and 42 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructHandle.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructHandle::type --body
python scripts/gpq.py uses type --kind typedef
```

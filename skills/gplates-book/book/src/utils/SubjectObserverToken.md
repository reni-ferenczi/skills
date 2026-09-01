# SubjectObserverToken

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 838 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/SubjectObserverToken.h` | C++ | 147 |

## Overview

`ObserverToken` and `SubjectToken` implement a polling variant of the
subject-observer pattern, used as a cache-invalidation primitive instead of Qt
signals or callback lists. A `SubjectToken` holds a 64-bit `Counter64` that its
owner increments (via `invalidate()`) whenever its state changes; each
`ObserverToken` records the counter value it last saw. A cache checks
`is_observer_up_to_date()` before trusting its own state and calls
`update_observer()` after refreshing it, avoiding the ordering and circular-
dependency problems that signal/slot wiring can introduce between layers.

The pattern is used pervasively across `app-logic` and `opengl` to let one
object (for example a `LayerProxy` or a `GLMultiResolutionRaster`) know
without a subscription that an upstream input has moved on, so it can lazily
recompute derived state on next access rather than being pushed updates
eagerly.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::ObserverToken`](#gplatesutilsobservertoken) | class | — | — | 0 | Used to effect a simple polling version of the subject-observer pattern. |
| [`GPlatesUtils::SubjectToken`](#gplatesutilssubjecttoken) | class | — | — | 0 | The complement of the ObserverToken. |

## Members

### `GPlatesUtils::ObserverToken`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ObserverToken()` | constructor | `None` | public | — |
| `reset()` | method | `void` | public | Resets this observer such that is \*not\* up-to-date with its subject. |
| `d_invalidate_counter` | field | `Counter64` | private | — |

### `GPlatesUtils::SubjectToken`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SubjectToken( bool invalidate_ = true)` | constructor | `None` | public | If invalidate is 'true' then call invalidate on construction. |
| `is_observer_up_to_date( const ObserverToken &observer)` | method | `bool` | public | Returns true if the specified observer is up-to-date with this subject. |
| `update_observer( ObserverToken &observer)` | method | `void` | public | Updates the specified observer so it is valid with respect to this subject. |
| `invalidate()` | method | `void` | public | Invalidates this subject. |
| `d_invalidate_counter` | field | `Counter64` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_SUBJECTOBSERVERTOKEN_H` | macro | `None` | — |

## Notes

Relies on `Counter64` being genuinely 64-bit: at the fastest conceivable
increment rate (one per CPU cycle on a 3 GHz machine) the counter would take
195 years to wrap around, whereas a 32-bit counter could wrap in seconds. A
default-constructed `SubjectToken` invalidates itself immediately unless
`invalidate_` is passed as `false`, so that any observer created afterwards is
forced to update itself once before being considered up to date.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](../opengl/GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 19 |
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 18 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 14 |
| [app-logic/deprecated/PaleomagUtils](../app-logic/deprecated/PaleomagUtils.md) | app-logic | 13 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 12 |
| [app-logic/ReconstructLayerProxy](../app-logic/ReconstructLayerProxy.md) | app-logic | 11 |
| [app-logic/ScalarField3DLayerProxy](../app-logic/ScalarField3DLayerProxy.md) | app-logic | 11 |
| [gui/TopologyCanvasToolWorkflow](../gui/TopologyCanvasToolWorkflow.md) | gui | 10 |
| [opengl/GLMultiResolutionCubeRaster](../opengl/GLMultiResolutionCubeRaster.md) | opengl | 10 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](../opengl/GLMultiResolutionCubeReconstructedRaster.md) | opengl | 10 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](../app-logic/deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 8 |
| [app-logic/LayerProxyUtils](../app-logic/LayerProxyUtils.md) | app-logic | 7 |
| [app-logic/TopologyGeometryResolverLayerProxy](../app-logic/TopologyGeometryResolverLayerProxy.md) | app-logic | 7 |
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 7 |
| [app-logic/ReconstructScalarCoverageLayerParams](../app-logic/ReconstructScalarCoverageLayerParams.md) | app-logic | 6 |
| [opengl/GLBuffer](../opengl/GLBuffer.md) | opengl | 6 |
| [opengl/GLMultiResolutionRaster](../opengl/GLMultiResolutionRaster.md) | opengl | 5 |
| [opengl/GLVisualRasterSource](../opengl/GLVisualRasterSource.md) | opengl | 5 |
| [app-logic/CoRegistrationLayerProxy](../app-logic/CoRegistrationLayerProxy.md) | app-logic | 4 |
| [app-logic/ReconstructScalarCoverageLayerProxy](../app-logic/ReconstructScalarCoverageLayerProxy.md) | app-logic | 4 |

*... and 14 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/SubjectObserverToken.h
python scripts/gpq.py def GPlatesUtils::SubjectToken --body
python scripts/gpq.py uses SubjectToken --kind class
python scripts/gpq.py hier SubjectToken
```

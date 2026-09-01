# ReconstructionLayerProxy

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 497 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionLayerProxy.h` | C++ | 341 |
| `src/app-logic/ReconstructionLayerProxy.cc` | C++ | 288 |

## Overview

`ReconstructionLayerProxy` is the `LayerProxy` for a rotation-file layer: it turns the connected rotation `GPlatesModel::FeatureCollectionHandle`s into `ReconstructionTree` objects on demand, for whatever reconstruction time and anchor plate ID a caller asks for. Trees are built lazily and cached by a `CachedReconstructionTreeCreatorImpl` (`d_cached_reconstruction_trees`), which is constructed on first use and can hold up to `DEFAULT_MAX_NUM_RECONSTRUCTION_TREES_IN_CACHE` (512) trees — sized that large specifically so flowlines, which query many distinct reconstruction times, do not thrash the cache; the header documents the roughly 370MB memory cost of a fully-populated cache versus 150MB for the ordinary size-64 case.

Because other code needs to hold onto a `ReconstructionTreeCreator` across time even though this proxy's internal cache is destroyed and rebuilt whenever its inputs change, `get_reconstruction_tree_creator()` never returns that internal cache directly. Instead it wraps `this` in the anonymous-namespace `DelegateReconstructionTreeCreator`, which forwards every call back through the proxy's own `get_reconstruction_tree` methods — so a client's cached `ReconstructionTreeCreator` handle stays valid and picks up later changes (new feature collections, a different anchor plate, a larger cache-size hint) without the client having to requery the layer graph.

Mutators like `set_current_anchor_plate_id`, `set_current_reconstruction_params`, `add_reconstruction_feature_collection` and `remove_reconstruction_feature_collection` all route through the private `invalidate()`, which drops the cached trees, resets the cache size back to its default, and fires `d_subject_token` so polling observers (typically downstream layers) know to recompute. `set_current_reconstruction_time`, by contrast, deliberately does *not* invalidate anything: an uncached time simply builds a new tree on request, and notifying observers on every time change would force them to discard time-keyed caches of their own for no benefit.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::(anonymous)::DelegateReconstructionTreeCreator`](#gplatesapplogicanonymousdelegatereconstructiontreecreator) | class | [`ReconstructionTreeCreatorImpl`](ReconstructionTreeCreator.md) | — | 0 | A reconstruction tree creator that delegates to ReconstructionLayerProxy. |
| [`GPlatesAppLogic::ReconstructionLayerProxy`](#gplatesapplogicreconstructionlayerproxy) | class | [`LayerProxy`](LayerProxy.md) | — | 0 | A layer proxy for creating reconstruction trees at desired reconstruction times. |

## Members

### `GPlatesAppLogic::(anonymous)::DelegateReconstructionTreeCreator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DelegateReconstructionTreeCreator( const ReconstructionLayerProxy::non_null_ptr_type &reconstruction_layer_proxy)` | constructor | `None` | public | — |
| `get_reconstruction_tree( const double &reconstruction_time, GPlatesModel::integer_plate_id_type anchor_plate_id)` | method | `ReconstructionTree::non_null_ptr_to_const_type` | public | Returns the reconstruction tree for the specified time and anchored plate id. |
| `get_reconstruction_tree_default_anchored_plate_id( const double &reconstruction_time)` | method | `ReconstructionTree::non_null_ptr_to_const_type` | public | Returns the reconstruction tree for the specified time and the \*default\* anchored plate id. |
| `get_default_anchor_plate_id()` | method | `GPlatesModel::integer_plate_id_type` | public | Returns the default anchor plate ID; |
| `d_reconstruction_layer_proxy` | field | `ReconstructionLayerProxy::non_null_ptr_type` | private | — |

### `GPlatesAppLogic::ReconstructionLayerProxy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructionLayerProxy>` | public | A convenience typedef for a shared pointer to a non-const ReconstructionLayerProxy. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructionLayerProxy>` | public | A convenience typedef for a shared pointer to a const ReconstructionLayerProxy. |
| `DEFAULT_MAX_NUM_RECONSTRUCTION_TREES_IN_CACHE` | field | `unsigned int` | public | The maximum number of reconstruction trees to cache for different reconstruction times. |
| `create( unsigned int default_max_num_reconstruction_trees_in_cache = DEFAULT_MAX_NUM_RECONSTRUCTION_TREES_IN_CACHE, GPlatesModel::integer_plate_id_type initial_anchored_plate_id = 0)` | method | `non_null_ptr_type` | public | Creates a ReconstructionLayerProxy object. default\_max\_num\_reconstruction\_trees\_in\_cache specifies the default cache size to use unless a cache size hint is requested via get\_reconstruction\_tree\_creator. |
| `get_reconstruction_tree()` | method | `ReconstructionTree::non_null_ptr_to_const_type` | public | Returns the reconstruction tree for the current reconstruction time and current anchor plate id. |
| `get_reconstruction_tree( const double &reconstruction_time)` | method | `ReconstructionTree::non_null_ptr_to_const_type` | public | Returns the reconstruction tree for the specified time - can be any reconstruction time. |
| `get_reconstruction_tree( GPlatesModel::integer_plate_id_type anchor_plate_id)` | method | `ReconstructionTree::non_null_ptr_to_const_type` | public | Returns the reconstruction tree for the specified anchor plate id. |
| `get_reconstruction_tree( const double &reconstruction_time, GPlatesModel::integer_plate_id_type anchor_plate_id)` | method | `ReconstructionTree::non_null_ptr_to_const_type` | public | Returns the reconstruction tree for the specified reconstruction time and anchor plate id. |
| `get_reconstruction_tree_creator( boost::optional<unsigned int> max_num_reconstruction_trees_in_cache_hint = boost::none)` | method | `ReconstructionTreeCreator` | public | An alternative to two overloaded versions of get\_reconstruction\_tree - provides an easy to pass them to other code sections that shouldn't know about layers. |
| `get_current_reconstruction_time()` | method | `double` | public | Gets the current reconstruction time as set by the layer system. |
| `get_current_anchor_plate_id()` | method | `GPlatesModel::integer_plate_id_type` | public | Gets the current anchor plate id. |
| `accept_visitor( ConstLayerProxyVisitor &visitor)` | method | `void` | public | Accept a ConstLayerProxyVisitor instance. |
| `accept_visitor( LayerProxyVisitor &visitor)` | method | `void` | public | Accept a LayerProxyVisitor instance. |
| `set_current_reconstruction_time( const double &reconstruction_time)` | method | `void` | public | Sets the current reconstruction time as set by the layer system. |
| `set_current_anchor_plate_id( GPlatesModel::integer_plate_id_type anchor_plate_id)` | method | `void` | public | Sets the current anchor plate id as set by the layer system. |
| `set_current_reconstruction_params( const ReconstructionParams &reconstruction_params)` | method | `void` | public | Sets the parameters used for creating reconstruction trees. |
| `add_reconstruction_feature_collection( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | Add to the list of feature collections that are used to build reconstruction trees. |
| `remove_reconstruction_feature_collection( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | Remove from the list of feature collections that are used to build reconstruction trees. |
| `modified_reconstruction_feature_collection( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | A reconstruction feature collection was modified. |
| `d_current_reconstruction_feature_collections` | field | `std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref>` | private | The input feature collections used to generate reconstruction trees at reconstruction times specified by clients. |
| `d_current_reconstruction_time` | field | `GPlatesMaths::real_t` | private | The current reconstruction time as set by the layer system. |
| `d_current_anchor_plate_id` | field | `GPlatesModel::integer_plate_id_type` | private | The current anchored plate id as set by the layer system. |
| `d_current_reconstruction_params` | field | `ReconstructionParams` | private | The current reconstruction parameters as set by the layer system. |
| `d_cached_reconstruction_trees` | field | `boost::optional<CachedReconstructionTreeCreatorImpl::non_null_ptr_type>` | private | Manages cached reconstruction trees for the most-recently requested reconstruction time/anchors. |
| `d_subject_token` | field | `GPlatesUtils::SubjectToken` | private | Used to notify polling observers that we've been updated. |
| `d_default_max_num_reconstruction_trees_in_cache` | field | `unsigned int` | private | The default value for the maximum number of reconstruction trees in the cache. |
| `d_current_max_num_reconstruction_trees_in_cache` | field | `unsigned int` | private | The current maximum number of reconstruction trees in the cache before we start evicting. |
| `ReconstructionLayerProxy( unsigned int default_max_num_reconstruction_trees_in_cache, GPlatesModel::integer_plate_id_type initial_anchored_plate_id)` | constructor | `None` | private | — |
| `invalidate()` | method | `void` | private | Called when we are updated. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_delegate_reconstruction_tree_creator( const ReconstructionLayerProxy::non_null_ptr_type &reconstruction_layer_proxy)` | function | `ReconstructionTreeCreator` | Returns a ReconstructionTreeCreator that delegates to reconstruction\_layer\_proxy. |
| `GPLATES_APP_LOGIC_RECONSTRUCTIONLAYERPROXY_H` | macro | `None` | — |

## Notes

- The cache size hint passed to `get_reconstruction_tree_creator` can only raise the cache above `d_default_max_num_reconstruction_trees_in_cache`, never below it; a smaller hint is silently clamped back to the default so one caller cannot degrade caching for others.
- Any call that invalidates the cache (anchor plate change, reconstruction params change, feature-collection add/remove/modify) also resets the current cache size to the default, so a previously granted larger-cache hint must be re-requested after invalidation.
- `set_current_reconstruction_time` skips both cache invalidation and the subject-token notification by design — see the `#if 0`-guarded comment in the `.cc` explaining why notifying on every time change would be counterproductive for observers that cache per-time results.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructionLayerTask](ReconstructionLayerTask.md) | app-logic | 8 |
| [qt-widgets/EditTimeSequenceWidget](../qt-widgets/EditTimeSequenceWidget.md) | qt-widgets | 5 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 4 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 4 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 4 |
| [app-logic/ReconstructGraph](ReconstructGraph.md) | app-logic | 3 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 3 |
| [qt-widgets/AssignReconstructionPlateIdsDialog](../qt-widgets/AssignReconstructionPlateIdsDialog.md) | qt-widgets | 3 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 3 |
| [qt-widgets/TotalReconstructionPolesDialog](../qt-widgets/TotalReconstructionPolesDialog.md) | qt-widgets | 3 |
| [app-logic/PropertyExtractors](PropertyExtractors.md) | app-logic | 2 |
| [gui/AnimationController](../gui/AnimationController.md) | gui | 2 |
| [qt-widgets/FlowlinePropertiesWidget](../qt-widgets/FlowlinePropertiesWidget.md) | qt-widgets | 2 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 2 |
| [api/PyApplication](../api/PyApplication.md) | api | 1 |
| [api/PyCoregistrationLayerProxy](../api/PyCoregistrationLayerProxy.md) | api | 1 |
| [app-logic/CoRegistrationLayerProxy](CoRegistrationLayerProxy.md) | app-logic | 1 |
| [app-logic/Reconstruction](Reconstruction.md) | app-logic | 1 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 1 |
| [app-logic/VelocityFieldCalculatorLayerProxy](VelocityFieldCalculatorLayerProxy.md) | app-logic | 1 |

*... and 13 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructionLayerProxy.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructionLayerProxy --body
python scripts/gpq.py uses ReconstructionLayerProxy --kind class
python scripts/gpq.py hier ReconstructionLayerProxy
```

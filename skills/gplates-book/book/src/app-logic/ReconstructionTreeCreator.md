# ReconstructionTreeCreator

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 933 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionTreeCreator.h` | C++ | 445 |
| `src/app-logic/ReconstructionTreeCreator.cc` | C++ | 355 |

## Overview

This is the handle almost every consumer of rotations actually holds. A `ReconstructionTree` is fixed to one reconstruction time and one anchor plate, but the code that reconstructs geometry, resolves topologies or builds flowlines needs trees at many times — so instead of passing trees around, GPlates passes a `ReconstructionTreeCreator`: a cheap, copyable, value-semantics wrapper over a reference-counted `ReconstructionTreeCreatorImpl`. Copying one copies a pointer, so it can be stored in functors and passed by value freely, and the caller never has to know whether the trees behind it are freshly built, served from a cache, or fetched from a `ReconstructionLayerProxy`.

Two implementations ship here. `UncachedReconstructionTreeCreatorImpl` (file-local, in the anonymous namespace) builds a `ReconstructionGraph` once at construction and calls `ReconstructionTree::create()` on every request. `CachedReconstructionTreeCreatorImpl` fronts the same operation with a `GPlatesUtils::KeyValueCache` keyed on `(GPlatesMaths::real_t reconstruction_time, integer_plate_id_type anchor_plate_id)` and evicting least-recently-used. It has two modes, selected by which `create()` overload is used and expressed as a `boost::function` bound at construction: build trees from an owned graph, or *adapt* another `ReconstructionTreeCreator` by putting a cache in front of it. The adaptor mode is how a caller that will sweep many times gives itself a bigger cache without disturbing the shared creator it borrowed. Even the default cache size of one is worth having, because it collapses the common pattern of asking repeatedly for the same time and anchor.

`create_reconstruction_graph()` is the other half of the file and the actual bridge from data to engine: it runs a `ReconstructionGraphPopulator` over the supplied rotation feature collections via `AppLogicUtils::visit_feature_collections`, feeding a `ReconstructionGraphBuilder`, and returns the finished graph. Its `extend_total_reconstruction_poles_to_distant_past` flag extends each moving plate's oldest sequence back to infinity so that geometries older than the rotation model do not snap back to their present-day positions — that flag is threaded unchanged through every `create_*` function in this header.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::(anonymous)::UncachedReconstructionTreeCreatorImpl`](#gplatesapplogicanonymousuncachedreconstructiontreecreatorimpl) | class | [`ReconstructionTreeCreatorImpl`](ReconstructionTreeCreator.md) | — | 0 | An uncached reconstruction tree creator implementation that simply creates a new reconstruction tree whenever a reconstruction tree is requested. |
| [`GPlatesAppLogic::ReconstructionTreeCreator`](#gplatesapplogicreconstructiontreecreator) | class | — | — | 0 | A wrapper around an implementation for creating reconstruction trees. |
| [`GPlatesAppLogic::ReconstructionTreeCreatorImpl`](#gplatesapplogicreconstructiontreecreatorimpl) | class | [`GPlatesUtils::ReferenceCount<ReconstructionTreeCreatorImpl>`](../utils/ReferenceCount.md) | — | 4 | Base implementation class for ReconstructionTreeCreator. |
| [`GPlatesAppLogic::CachedReconstructionTreeCreatorImpl`](#gplatesapplogiccachedreconstructiontreecreatorimpl) | class | [`ReconstructionTreeCreatorImpl`](ReconstructionTreeCreator.md) | — | 0 | A reconstruction tree creator implementation that caches the most-recently requested reconstruction trees. |

## Members

### `GPlatesAppLogic::(anonymous)::UncachedReconstructionTreeCreatorImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UncachedReconstructionTreeCreatorImpl( const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &reconstruction_feature_collections, bool extend_total_reconstruction_poles_to_distant_past, GPlatesModel::integer_plate_id_type default_anchor_plate_id)` | constructor | `None` | public | — |
| `get_reconstruction_tree( const double &reconstruction_time, GPlatesModel::integer_plate_id_type anchor_plate_id)` | method | `ReconstructionTree::non_null_ptr_to_const_type` | public | Returns the reconstruction tree for the specified time and anchored plate id. |
| `get_reconstruction_tree_default_anchored_plate_id( const double &reconstruction_time)` | method | `ReconstructionTree::non_null_ptr_to_const_type` | public | Returns the reconstruction tree for the specified time and the \*default\* anchored plate id. |
| `get_default_anchor_plate_id()` | method | `GPlatesModel::integer_plate_id_type` | public | Returns the default anchor plate ID; |
| `d_reconstruction_graph` | field | `ReconstructionGraph::non_null_ptr_to_const_type` | private | — |
| `d_default_anchor_plate_id` | field | `GPlatesModel::integer_plate_id_type` | private | — |

### `GPlatesAppLogic::ReconstructionTreeCreator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ReconstructionTreeCreator( const GPlatesUtils::non_null_intrusive_ptr<ReconstructionTreeCreatorImpl> &impl)` | constructor | `None` | public | — |
| `~ReconstructionTreeCreator()` | destructor | `None` | public | — |
| `get_reconstruction_tree( const double &reconstruction_time, GPlatesModel::integer_plate_id_type anchor_plate_id)` | method | `ReconstructionTree::non_null_ptr_to_const_type` | public | Returns the reconstruction tree for the specified time and anchored plate id. |
| `get_reconstruction_tree( const double &reconstruction_time)` | method | `ReconstructionTree::non_null_ptr_to_const_type` | public | Returns the reconstruction tree for the specified time and the \*default\* anchored plate id that 'this' ReconstructionTreeCreator was created with. |
| `get_default_anchor_plate_id()` | method | `GPlatesModel::integer_plate_id_type` | public | Returns the default anchor plate ID; |
| `d_impl` | field | `GPlatesUtils::non_null_intrusive_ptr<ReconstructionTreeCreatorImpl>` | private | — |

### `GPlatesAppLogic::ReconstructionTreeCreatorImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructionTreeCreatorImpl>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructionTreeCreatorImpl>` | public | — |
| `~ReconstructionTreeCreatorImpl()` | destructor | `None` | public | — |
| `get_reconstruction_tree( const double &reconstruction_time, GPlatesModel::integer_plate_id_type anchor_plate_id)` | method | `ReconstructionTree::non_null_ptr_to_const_type` | public | Returns the reconstruction tree for the specified time and anchored plate id. |
| `get_reconstruction_tree_default_anchored_plate_id( const double &reconstruction_time)` | method | `ReconstructionTree::non_null_ptr_to_const_type` | public | Returns the reconstruction tree for the specified time and the \*default\* anchored plate id. |
| `get_default_anchor_plate_id()` | method | `GPlatesModel::integer_plate_id_type` | public | Returns the default anchor plate ID; |

### `GPlatesAppLogic::CachedReconstructionTreeCreatorImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<CachedReconstructionTreeCreatorImpl>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const CachedReconstructionTreeCreatorImpl>` | public | — |
| `create( const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &reconstruction_feature_collections, bool extend_total_reconstruction_poles_to_distant_past, GPlatesModel::integer_plate_id_type default_anchor_plate_id, unsigned int reconstruction_tree_cache_size)` | method | `non_null_ptr_type` | public | Creates a cache that will generate reconstruction trees. |
| `create( const ReconstructionTreeCreator &reconstruction_tree_creator, boost::optional<GPlatesModel::integer_plate_id_type> default_anchor_plate_id, unsigned int reconstruction_tree_cache_size)` | method | `non_null_ptr_type` | public | Creates a cache that will generate reconstruction trees. |
| `set_maximum_cache_size( unsigned int maximum_num_cache_size)` | method | `void` | public | Sets the maximum number of cached reconstruction trees. |
| `clear_cache()` | method | `void` | public | Clears any cached reconstruction trees. |
| `get_reconstruction_tree( const double &reconstruction_time, GPlatesModel::integer_plate_id_type anchor_plate_id)` | method | `ReconstructionTree::non_null_ptr_to_const_type` | public | Returns the reconstruction tree for the specified time and anchored plate id. |
| `get_reconstruction_tree_default_anchored_plate_id( const double &reconstruction_time)` | method | `ReconstructionTree::non_null_ptr_to_const_type` | public | Returns the reconstruction tree for the specified time and the \*default\* anchored plate id. |
| `get_default_anchor_plate_id()` | method | `GPlatesModel::integer_plate_id_type` | public | Returns the default anchor plate ID; |
| `cache_key_type` | typedef | `std::pair<GPlatesMaths::real_t, GPlatesModel::integer_plate_id_type>` | private | Typedef for the key in the reconstruction tree cache. |
| `cache_value_type` | typedef | `ReconstructionTree::non_null_ptr_to_const_type` | private | Typedef for the value in the reconstruction tree cache. |
| `cache_type` | typedef | `GPlatesUtils::KeyValueCache<cache_key_type, cache_value_type>` | private | Typedef for the reconstruction tree cache. |
| `create_reconstruction_tree_function_type` | typedef | `boost::function< cache_value_type (const cache_key_type &) >` | private | Typedef for a function accepting a cache key and returning a reconstruction tree. |
| `get_default_anchor_plate_id_function_type` | typedef | `boost::function< GPlatesModel::integer_plate_id_type () >` | private | Typedef for a function returning a default anchor plate ID. |
| `d_create_reconstruction_tree_function` | field | `create_reconstruction_tree_function_type` | private | — |
| `d_get_default_anchor_plate_id_function` | field | `get_default_anchor_plate_id_function_type` | private | — |
| `d_cache` | field | `cache_type` | private | — |
| `CachedReconstructionTreeCreatorImpl( const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &reconstruction_feature_collections, bool extend_total_reconstruction_poles_to_distant_past, GPlatesModel::integer_plate_id_type default_anchor_plate_id, unsigned int reconstruction_tree_cache_size)` | constructor | `None` | private | — |
| `CachedReconstructionTreeCreatorImpl( const ReconstructionTreeCreator &reconstruction_tree_creator, boost::optional<GPlatesModel::integer_plate_id_type> default_anchor_plate_id, unsigned int reconstruction_tree_cache_size)` | constructor | `None` | private | — |
| `create_reconstruction_tree_from_reconstruction_graph( const cache_key_type &key, ReconstructionGraph::non_null_ptr_to_const_type reconstruction_graph)` | method | `cache_value_type` | private | Creates a reconstruction tree given the cache key (reconstruction time and anchor plate id). |
| `create_reconstruction_tree_from_reconstruction_tree_creator( const cache_key_type &key, const ReconstructionTreeCreator &reconstruction_tree_creator)` | method | `cache_value_type` | private | Creates a reconstruction tree given the cache key (reconstruction time and anchor plate id). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTIONTREECREATOR_H` | macro | `None` | — |
| `create_reconstruction_graph( const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &reconstruction_feature_collections, bool extend_total_reconstruction_poles_to_distant_past = false)` | function | `ReconstructionGraph::non_null_ptr_to_const_type` | Create and return a reconstruction graph. |
| `create_cached_reconstruction_tree_creator( const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &reconstruction_feature_collections, bool extend_total_reconstruction_poles_to_distant_past = false, GPlatesModel::integer_plate_id_type default_anchor_plate_id = 0, unsigned int reconstruction_tree_cache_size ...` | function | `ReconstructionTreeCreator` | Creates a ReconstructionTreeCreator that is implemented as a least-recently-used cache of reconstruction trees. |
| `create_cached_reconstruction_tree_adaptor( const ReconstructionTreeCreator &reconstruction_tree_creator, boost::optional<GPlatesModel::integer_plate_id_type> default_anchor_plate_id = boost::none, unsigned int reconstruction_tree_cache_size = 1)` | function | `ReconstructionTreeCreator` | Similar to create\_cached\_reconstruction\_tree\_creator but instead of directly creating reconstruction trees it gets them from an existing ReconstructionTreeCreator. |
| `create_cached_reconstruction_tree_creator_impl( const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &reconstruction_feature_collections, bool extend_total_reconstruction_poles_to_distant_past = false, GPlatesModel::integer_plate_id_type default_anchor_plate_id = 0, unsigned int reconstruction_tree_cache_ ...` | function | `GPlatesUtils::non_null_intrusive_ptr<CachedReconstructionTreeCreatorImpl>` | Similar to create\_cached\_reconstruction\_tree\_creator but returns the implementation object (which can subsequently be wrapped in a ReconstructionTreeCreator). |
| `create_cached_reconstruction_tree_adaptor_impl( const ReconstructionTreeCreator &reconstruction_tree_creator, boost::optional<GPlatesModel::integer_plate_id_type> default_anchor_plate_id = boost::none, unsigned int reconstruction_tree_cache_size = 1)` | function | `GPlatesUtils::non_null_intrusive_ptr<CachedReconstructionTreeCreatorImpl>` | Similar to create\_cached\_reconstruction\_tree\_adaptor but returns the implementation object (which can subsequently be wrapped in a ReconstructionTreeCreator). |
| `create_uncached_reconstruction_tree_creator( const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &reconstruction_feature_collections, bool extend_total_reconstruction_poles_to_distant_past = false, GPlatesModel::integer_plate_id_type default_anchor_plate_id = 0)` | function | `ReconstructionTreeCreator` | Creates a ReconstructionTreeCreator that creates a new reconstruction tree each time a reconstruction tree is requested. |

## Notes

**Snapshot semantics.** The graph is built from the rotation feature collections *at the moment the creator (or `create_reconstruction_graph()`) is called*. Later edits to those features are invisible to every tree the creator subsequently hands out. When rotations change, the creator must be rebuilt — this is why `ReconstructionLayerProxy` recreates its creator rather than poking at an existing one.

**Cache size zero throws.** `create_cached_reconstruction_tree_creator_impl()` and `create_cached_reconstruction_tree_adaptor_impl()` assert `reconstruction_tree_cache_size > 0` and raise `GPlatesGlobal::PreconditionViolationError`. The wrapper functions inherit that.

**The cache key is a `GPlatesMaths::real_t`, not a `double`.** Lookups therefore use `real_t`'s epsilon comparison, so two nearby but unequal times can share a cached tree. That is deliberate, but it means you cannot rely on distinct `double` values producing distinct trees.

**Do not compare trees by pointer across a cache boundary.** A tree can be evicted and a logically identical one rebuilt at any later request; use `ReconstructionTree::created_from_same_graph_with_same_parameters()`. This is exactly the situation that method exists for.

**Default anchor plate is resolved lazily.** Both cached constructors store a `boost::function` rather than a plain plate ID; in adaptor mode with no explicit default, `get_default_anchor_plate_id()` forwards to the adapted creator on every call, so a change of default there is picked up. Note that `get_reconstruction_tree(time)` resolves the default *then* keys the cache on the resolved ID, so switching the default does not invalidate entries built under the old one — they simply stop being hit.

**Ownership cycle risk in adaptor mode.** `CachedReconstructionTreeCreatorImpl` binds a copy of the adapted `ReconstructionTreeCreator` into its own member function, and that copy holds a counted reference to the adapted impl. Chaining an adaptor back onto something that (transitively) holds this impl would leak. The `boost::bind` also captures `this`, so the impl must not be copied or relocated — it is heap-only and reference-counted for that reason.

**No synchronisation.** The cache is mutated by `get_reconstruction_tree()`, which is why `ReconstructionTreeCreatorImpl`'s tree accessors are non-`const` while `ReconstructionTreeCreator`'s are `const`. Sharing one creator across threads is not safe.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/FlowlineUtils](FlowlineUtils.md) | app-logic | 18 |
| [app-logic/ResolvedVertexSourceInfo](ResolvedVertexSourceInfo.md) | app-logic | 18 |
| [app-logic/ReconstructUtils](ReconstructUtils.md) | app-logic | 15 |
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 12 |
| [app-logic/ReconstructedFeatureGeometry](ReconstructedFeatureGeometry.md) | app-logic | 11 |
| [app-logic/ReconstructionLayerProxy](ReconstructionLayerProxy.md) | app-logic | 10 |
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 9 |
| [app-logic/RotationUtils](RotationUtils.md) | app-logic | 7 |
| [app-logic/TopologyGeometryResolver](TopologyGeometryResolver.md) | app-logic | 7 |
| [app-logic/ReconstructContext](ReconstructContext.md) | app-logic | 5 |
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 5 |
| [app-logic/FlowlineGeometryPopulator](FlowlineGeometryPopulator.md) | app-logic | 4 |
| [app-logic/MotionPathGeometryPopulator](MotionPathGeometryPopulator.md) | app-logic | 4 |
| [app-logic/PlateVelocityUtils](PlateVelocityUtils.md) | app-logic | 4 |
| [app-logic/ResolvedTopologicalGeometry](ResolvedTopologicalGeometry.md) | app-logic | 4 |
| [app-logic/ResolvedTriangulationNetwork](ResolvedTriangulationNetwork.md) | app-logic | 4 |
| [app-logic/SmallCircleGeometryPopulator](SmallCircleGeometryPopulator.md) | app-logic | 4 |
| [app-logic/CoRegistrationLayerProxy](CoRegistrationLayerProxy.md) | app-logic | 3 |
| [app-logic/ReconstructMethodInterface](ReconstructMethodInterface.md) | app-logic | 3 |
| [api/PyFunctions](../api/PyFunctions.md) | api | 2 |

*... and 24 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructionTreeCreator.h
python scripts/gpq.py def GPlatesAppLogic::CachedReconstructionTreeCreatorImpl --body
python scripts/gpq.py uses CachedReconstructionTreeCreatorImpl --kind class
python scripts/gpq.py hier CachedReconstructionTreeCreatorImpl
```

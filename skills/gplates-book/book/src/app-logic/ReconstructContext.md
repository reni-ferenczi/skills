# ReconstructContext

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 662 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructContext.h` | C++ | 769 |
| `src/app-logic/ReconstructContext.cc` | C++ | 946 |

## Overview

The workhorse behind `ReconstructLayerProxy`: give it a set of features once, and
it will reconstruct them into `ReconstructedFeatureGeometry` objects at any time,
or over any time range, as often as you like. Its reason to exist is caching of
the parts that do not depend on the reconstruction time. `set_features` asks
`ReconstructMethodRegistry` which `ReconstructMethod::Type` can handle each
feature and remembers that mapping, so the (non-trivial) method detection is not
repeated on every frame; features that no method claims are dropped, which is how
topological features are kept out of this framework.

The second thing it caches is the *geometry property handle*, a plain index that
identifies one reconstructable geometry property of one feature, stable across all
reconstruction times as long as the feature set is unchanged.
`get_present_day_feature_geometries` returns a vector indexed by exactly that
handle, so a client can build something expensive per present-day geometry — an
OpenGL polygon mesh in `GLReconstructedStaticPolygonMeshes`, a co-registration
row in `data-mining` — and then, at any time, use the handle on each
`Reconstruction` to find it again in O(1). That is what distinguishes
`get_reconstructions` and `get_reconstructed_features` from the plain
`get_reconstructed_feature_geometries`.

The third piece is `ContextState`, and the split it enforces is the design idea
worth understanding. A feature's own properties are *intrinsic* state; the
`ReconstructMethodInterface::Context` — reconstruct params, a
`ReconstructionTreeCreator`, and optionally a `TopologyReconstruct` for deformation
— is *extrinsic*. Keeping the extrinsic state in a separately created
`ContextState` lets one `ReconstructContext` serve several simultaneous
reconstruction scenarios (different anchored plates, with and without deformation)
while sharing the single feature-to-method mapping between them. Each context
state owns its own `ReconstructMethodInterface` instances precisely because those
objects accumulate state specific to their context. Every `get_*` method here
takes a context-state reference and returns a fresh `ReconstructHandle`, stamped
into every geometry it produced, so a later search over a feature's weak observers
can tell which reconstruction run a given RFG came from.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::(anonymous)::IdentityReconstructionTreeCreatorImpl`](#gplatesapplogicanonymousidentityreconstructiontreecreatorimpl) | class | [`ReconstructionTreeCreatorImpl`](ReconstructionTreeCreator.md) | — | 0 | The default reconstruction tree creator implementation until the client supplies one. |
| [`GPlatesAppLogic::ReconstructContext`](#gplatesapplogicreconstructcontext) | class | — | — | 0 | Used to reconstruct regular features into ReconstructedFeatureGeometry objects at various reconstruction times. |

## Members

### `GPlatesAppLogic::(anonymous)::IdentityReconstructionTreeCreatorImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `IdentityReconstructionTreeCreatorImpl()` | constructor | `None` | public | — |
| `get_reconstruction_tree( const double &reconstruction_time, GPlatesModel::integer_plate_id_type anchor_plate_id)` | method | `ReconstructionTree::non_null_ptr_to_const_type` | public | — |
| `get_reconstruction_tree_default_anchored_plate_id( const double &reconstruction_time)` | method | `ReconstructionTree::non_null_ptr_to_const_type` | public | — |
| `get_default_anchor_plate_id()` | method | `GPlatesModel::integer_plate_id_type` | public | — |
| `d_empty_reconstruction_graph` | field | `ReconstructionGraph::non_null_ptr_to_const_type` | private | An empty ReconstructionGraph will create empty ReconstructionTree objects which will always return identity finite rotations. |

### `GPlatesAppLogic::ReconstructContext`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `geometry_type` | typedef | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | Typedef for a geometry type. |
| `geometry_property_handle_type` | typedef | `unsigned int` | public | Typedef for a handle to a geometry feature property. |
| `Reconstruction` | class | `None` | public | Used to associate a reconstructed feature geometry with its resolved geometry (ie, \*unreconstructed\*). |
| `ReconstructedFeature` | class | `None` | public | Used to associate a feature with its reconstructed feature geometry(s). |
| `ReconstructionTimeSpan` | class | `None` | public | Similar to Reconstruction but for a span of times rather than a single time. |
| `ReconstructedFeatureTimeSpan` | class | `None` | public | Similar to ReconstructedFeature but for a span of times rather than a single time. |
| `TopologyReconstructedFeatureTimeSpan` | class | `None` | public | Similar to ReconstructedFeatureTimeSpan but specific to feature's reconstructed using topologies and returns a TopologyReconstruct::GeometryTimeSpan instead of a TopologyReconstructedFeatureGeometry. |
| `ContextState` | class | `None` | public | Extrinsic reconstruction state that features are reconstructed with. |
| `context_state_reference_type` | typedef | `boost::shared_ptr<ContextState>` | public | Typedef for a reference to a context state. |
| `context_state_weak_reference_type` | typedef | `boost::weak_ptr<ContextState>` | public | Typedef for a weak reference to a context state. |
| `ReconstructContext( const ReconstructMethodRegistry &reconstruct_method_registry)` | constructor | `None` | public | Constructor defaults to no features. |
| `set_features( const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &feature_collections, boost::optional<std::vector<GPlatesModel::FeatureHandle::weak_ref> &> reconstructable_features = boost::none)` | method | `void` | public | Adds the specified features after removing any features added in a previous call to set\_features and for each feature in each feature collection determines which reconstruct method to use. |
| `set_features( const std::vector<GPlatesModel::FeatureHandle::weak_ref> &features, boost::optional<std::vector<GPlatesModel::FeatureHandle::weak_ref> &> reconstructable_features = boost::none)` | method | `void` | public | Overload accepting a sequence of features instead of feature collections. |
| `create_context_state( const ReconstructMethodInterface::Context &reconstruct_method_context)` | method | `context_state_reference_type` | public | Creates a context state associated with the specified reconstruct context state. |
| `get_present_day_feature_geometries` | field | `std::vector<geometry_type>` | public | The same as get\_resolved\_feature\_geometries with a reconstruction time of zero except the returned sequence contains geometries instead of optional geometries - this is because the value of the geometry property (at time zero) is obtained ... |
| `get_resolved_feature_geometries( const double &reconstruction_time)` | method | `std::vector<boost::optional<geometry_type> >` | public | Returns the resolved geometries for the geometry properties of the features, specified in the most recent call to set\_features, at the specified reconstruction time. |
| `get_reconstructed_feature_geometries( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const context_state_reference_type &context_state_ref, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Reconstructs the features, specified in the most recent call to set\_features, to the specified reconstruction time using the specified reconstruct context state. |
| `get_reconstructions( std::vector<Reconstruction> &reconstructed_feature_geometries, const context_state_reference_type &context_state_ref, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Reconstructs the features, specified in the most recent call to set\_features, to the specified reconstruction time using the specified reconstruct context state. |
| `get_reconstructed_features( std::vector<ReconstructedFeature> &reconstructed_features, const context_state_reference_type &context_state_ref, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Reconstructs the features, specified in the most recent call to set\_features, to the specified reconstruction time using the specified reconstruct context state. |
| `get_reconstruction_time_spans( std::vector<ReconstructionTimeSpan> &reconstruction_time_spans, const context_state_reference_type &context_state_ref, const TimeSpanUtils::TimeRange &time_range)` | method | `ReconstructHandle::type` | public | This is similar to get\_reconstructions but reconstructs over a time range of reconstruction times instead of a single reconstruction time. |
| `get_reconstructed_feature_time_spans( std::vector<ReconstructedFeatureTimeSpan> &reconstructed_feature_time_spans, const context_state_reference_type &context_state_ref, const TimeSpanUtils::TimeRange &time_range)` | method | `ReconstructHandle::type` | public | This is similar to get\_reconstructed\_features but reconstructs over a time range of reconstruction times instead of a single reconstruction time. |
| `get_topology_reconstructed_feature_time_spans( std::vector<TopologyReconstructedFeatureTimeSpan> &topology_reconstructed_feature_time_spans, const context_state_reference_type &context_state_ref)` | method | `void` | public | Returns any topology-reconstructed feature time spans. |
| `get_reconstructed_topological_sections( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_topological_sections, const std::set<GPlatesModel::FeatureId> &topological_sections_referenced, const context_state_reference_type &context_state_ref, const double &reconstruction_time)` | method | `ReconstructHandle::type` | public | Reconstructs the features, specified in the most recent call to set\_features, to the specified reconstruction time using the specified reconstruct context state and limited to features matching the specified feature IDs. |
| `reconstruct_feature_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &reconstructed_feature_velocities, const context_state_reference_type &context_state_ref, const double &reconstruction_time, const double &velocity_delta_time = 1.0, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime ...` | method | `ReconstructHandle::type` | public | Calculate velocities at the geometry reconstruction positions of the features, specified in the most recent call to set\_features, at the specified reconstruction time using the specified reconstruct context state. |
| `ReconstructMethodFeature` | struct | `None` | private | Groups a feature with its geometry properties. |
| `reconstruct_method_feature_seq_type` | typedef | `std::vector<ReconstructMethodFeature>` | private | Typedef for a sequence of reconstruct methods and their associated features. |
| `context_state_weak_ref_seq_type` | typedef | `std::vector<context_state_weak_reference_type>` | private | Typedef for a sequence of context states. |
| `d_reconstruct_method_registry` | field | `ReconstructMethodRegistry` | private | Used to assign reconstruct methods to features. |
| `d_reconstruct_method_feature_seq` | field | `reconstruct_method_feature_seq_type` | private | A sequence of features associated with their reconstruct method. |
| `d_context_states` | field | `context_state_weak_ref_seq_type` | private | The context states that the client has created. |
| `d_cached_present_day_geometries` | field | `boost::optional<std::vector<geometry_type> >` | private | The present day geometries of all reconstructable geometry properties of all features. |
| `get_feature_reconstructions( std::vector<Reconstruction> &reconstructions, const ReconstructMethodFeature::geometry_property_to_handle_seq_type &feature_geometry_property_handles, const std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries)` | method | `void` | private | Converts the reconstructed feature geometries, of the specified feature, to reconstructions. |
| `build_feature_reconstruction_time_spans( std::vector<ReconstructionTimeSpan> &reconstruction_time_spans, const ReconstructMethodFeature::geometry_property_to_handle_seq_type &feature_geometry_property_handles, const std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const Ti ...` | method | `void` | private | Add the reconstructed feature geometries, of the specified feature, to reconstruction time spans. |
| `have_assigned_geometry_property_handles()` | method | `bool` | private | Returns true if the geometry property handles have been assigned and are up-to-date with the current set of features. |
| `assign_geometry_property_handles()` | method | `void` | private | Iterates over the assigned features and assigns geometry property handles. |
| `initialise_context_states()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTCONTEXT_H` | macro | `None` | — |

## Notes

**Call `set_features` again whenever the features change.** It is not just an
optimisation gate: it clears the cached present-day geometries, re-detects the
reconstruct method for every feature, and — via `initialise_context_states` —
re-creates the `ReconstructMethodInterface` instances inside every live context
state, because their accumulated internal state is no longer applicable. Skipping
it leaves stale reconstruct methods and stale geometry property handles.

**Geometry property handles are only stable between calls to `set_features`.**
They are assigned lazily by `assign_geometry_property_handles` as running indices
into `d_cached_present_day_geometries`, in feature order, so adding or removing a
feature renumbers everything. The reference returned by
`get_present_day_feature_geometries` is likewise valid only until the next
`set_features`. `get_reconstructed_feature_geometries`,
`get_reconstructed_topological_sections` and `reconstruct_feature_velocities` do
*not* need the handles and deliberately skip assigning them — the handle-based
methods force the assignment themselves.

**Handle assignment can construct a throwaway context state.** If no live context
state exists, `assign_geometry_property_handles` creates one on the spot using an
`IdentityReconstructionTreeCreatorImpl` — a `ReconstructionTreeCreator` backed by
an empty `ReconstructionGraph`, so every rotation is the identity and the anchored
plate is 0. That is sound only because present-day geometry does not depend on the
rotation model; do not reuse that impl anywhere the rotations matter.

**Context state ownership is inverted from the usual pattern.** The client owns
the `shared_ptr` returned by `create_context_state`; `ReconstructContext` keeps
only `weak_ptr`s, reclaiming expired slots on the next `create_context_state` or
`set_features`. Drop your reference and the context state is destroyed even though
the `ReconstructContext` is still alive. Conversely, the
`ReconstructMethodRegistry` passed to the constructor is held by reference and
must outlive the `ReconstructContext`.

**Every handle-based method asserts** that the context state's reconstruct-method
count equals the feature count. A mismatch means the state was created against a
different feature set and raises `AssertionFailureException`.

**Matching RFGs back to handles is a linear scan.** `get_feature_reconstructions`
and `build_feature_reconstruction_time_spans` compare
`FeatureHandle::iterator`s in a nested loop over the feature's geometry properties;
an RFG whose property iterator matches nothing is silently dropped rather than
reported. This is per-feature, so it is cheap for the common one-geometry feature
and quadratic for a feature with many geometry properties.

**Empty results are meaningful and differ per method.**
`get_reconstructed_features` returns an entry for *every* feature, including ones
inactive at that time (with an empty reconstruction sequence) — co-registration
depends on that, since it correlates by feature across frames.
`get_topology_reconstructed_feature_time_spans`, by contrast, omits features that
are not topology-reconstructed entirely.

**Reconstruct handles are process-global and not thread-safe.**
`ReconstructHandle::get_next_reconstruct_handle` increments a function-local
static, flagged in its own source as needing protection if GPlates ever becomes
multi-threaded. Treat every method on this class as single-threaded.

Feature references throughout are `weak_ref`s and are re-checked with `is_valid()`
before each use, so a feature deleted after `set_features` is skipped rather than
crashing — but it still occupies a slot in the internal sequence, and its geometry
property handles remain allocated.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 106 |
| [app-logic/ReconstructUtils](ReconstructUtils.md) | app-logic | 82 |
| [data-mining/RegionOfInterestFilter](../data-mining/RegionOfInterestFilter.md) | data-mining | 33 |
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 28 |
| [data-mining/DataSelector](../data-mining/DataSelector.md) | data-mining | 24 |
| [data-mining/CoRegFilterMapReduceFactory](../data-mining/CoRegFilterMapReduceFactory.md) | data-mining | 15 |
| [app-logic/ReconstructScalarCoverageLayerProxy](ReconstructScalarCoverageLayerProxy.md) | app-logic | 12 |
| [data-mining/RFGToRelationalPropertyMapper](../data-mining/RFGToRelationalPropertyMapper.md) | data-mining | 12 |
| [app-logic/CoRegistrationLayerProxy](CoRegistrationLayerProxy.md) | app-logic | 11 |
| [data-mining/LookupReducer](../data-mining/LookupReducer.md) | data-mining | 11 |
| [opengl/GLReconstructedStaticPolygonMeshes](../opengl/GLReconstructedStaticPolygonMeshes.md) | opengl | 8 |
| [data-mining/CoRegFilter](../data-mining/CoRegFilter.md) | data-mining | 7 |
| [app-logic/ReconstructMethodByPlateId](ReconstructMethodByPlateId.md) | app-logic | 6 |
| [data-mining/SeedSelfFilter](../data-mining/SeedSelfFilter.md) | data-mining | 6 |
| [data-mining/CoRegMapper](../data-mining/CoRegMapper.md) | data-mining | 5 |
| [data-mining/CoRegReducer](../data-mining/CoRegReducer.md) | data-mining | 5 |
| [api/PyFunctions](../api/PyFunctions.md) | api | 4 |
| [data-mining/CoRegFilterCache](../data-mining/CoRegFilterCache.md) | data-mining | 4 |
| [app-logic/ReconstructMethodHalfStageRotation](ReconstructMethodHalfStageRotation.md) | app-logic | 3 |
| [api/CoReg](../api/CoReg.md) | api | 2 |

*... and 7 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructContext.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructContext --body
python scripts/gpq.py uses ReconstructContext --kind class
python scripts/gpq.py hier ReconstructContext
```

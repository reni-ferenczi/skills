# ReconstructContext

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 662 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructContext.h` | C++ | 769 |
| `src/app-logic/ReconstructContext.cc` | C++ | 946 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructContext tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=app-logic/ReconstructContext tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

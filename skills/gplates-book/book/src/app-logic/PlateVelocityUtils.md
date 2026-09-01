# PlateVelocityUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 968 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/PlateVelocityUtils.h` | C++ | 333 |
| `src/app-logic/PlateVelocityUtils.cc` | C++ | 1226 |

## Overview

`PlateVelocityUtils` computes surface velocities, the core of what a `VelocityFieldCalculatorLayerProxy` and the deprecated `PlateVelocityWorkflow` produce. `solve_velocities_on_surfaces` is the entry point: for each point of each velocity-domain `ReconstructedFeatureGeometry`, it tests the point against a `GeometryCookieCutter` built from reconstructed static polygons and resolved topological boundaries, and against a `TopologicalNetworksVelocities` built from resolved topological networks, resolving overlaps with a fixed precedence — networks first, then topological boundaries, then static polygons — and writing one `MultiPointVectorField` per domain geometry. When a `VelocitySmoothingOptions` is supplied, points near a boundary get their velocity interpolated with the boundary's averaged velocity instead of taking whichever side's raw value they landed on, via `solve_velocity_on_surfaces_with_boundary_smoothing`, `solve_velocity_at_boundary` and `solve_average_velocity_at_boundary`.

Underneath that surface-testing machinery sit the basic building blocks: `calculate_velocity_vector`/`calculate_velocity_colat_lon` turn either two explicit `GPlatesMaths::FiniteRotation`s or a plate id resolved through a `ReconstructionTreeCreator` at two nearby times into a velocity, falling back to zero and retrying with an adjusted delta-time window when a plate id is missing from the reconstruction tree at one of the two times (see the header comments on both overloads for the exact fallback rules); `calculate_stage_rotation` exposes the underlying stage rotation directly. Two private `GPlatesModel::ConstFeatureVisitor`s, `DetectVelocityMeshNodes` and `AddVelocityFieldFeatures`, implement the `gpml:MeshNode` → `gpml:VelocityField` feature conversion used by `detect_velocity_mesh_nodes(_node)` and `create_velocity_field_feature_collection`, the older, feature-based way of describing a set of velocity domain points (one `gml:domainSet` per `meshPoints` property found).

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::(anonymous)::DetectVelocityMeshNodes`](#gplatesapplogicanonymousdetectvelocitymeshnodes) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Determines if any mesh node features that can be used by plate velocity calculations. |
| [`GPlatesAppLogic::(anonymous)::AddVelocityFieldFeatures`](#gplatesapplogicanonymousaddvelocityfieldfeatures) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | For each feature of type "gpml:MeshNode" creates a new feature of type "gpml:VelocityField" and adds to a new feature collection. |
| [`GPlatesAppLogic::PlateVelocityUtils::VelocitySmoothingOptions`](#gplatesapplogicplatevelocityutilsvelocitysmoothingoptions) | class | — | — | 0 | Options to control how velocities are smoothed across plate boundaries. |
| [`GPlatesAppLogic::PlateVelocityUtils::TopologicalNetworksVelocities`](#gplatesapplogicplatevelocityutilstopologicalnetworksvelocities) | class | — | — | 0 | Calculates of velocities at arbitrary points within a topological network. |

## Members

### `GPlatesAppLogic::(anonymous)::DetectVelocityMeshNodes`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DetectVelocityMeshNodes()` | constructor | `None` | public | — |
| `has_velocity_mesh_node_features()` | method | `bool` | public | — |
| `visit_feature_handle( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | public | — |
| `d_found_velocity_mesh_nodes` | field | `bool` | private | — |

### `GPlatesAppLogic::(anonymous)::AddVelocityFieldFeatures`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AddVelocityFieldFeatures( const GPlatesModel::FeatureCollectionHandle::weak_ref &velocity_field_feature_collection)` | constructor | `None` | public | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | public | — |
| `visit_gml_multi_point( const GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | public | — |
| `d_velocity_field_feature_collection` | field | `GPlatesModel::FeatureCollectionHandle::weak_ref` | private | — |
| `d_velocity_field_feature` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | — |
| `create_velocity_field_feature()` | method | `GPlatesModel::FeatureHandle::weak_ref` | private | — |
| `create_and_append_domain_set_property_to_velocity_field_feature( const GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | private | — |

### `GPlatesAppLogic::PlateVelocityUtils::VelocitySmoothingOptions`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VelocitySmoothingOptions( const double &angular_half_extent_radians_, bool exclude_deforming_regions_)` | constructor | `None` | public | — |
| `angular_half_extent_radians` | field | `double` | public | — |
| `exclude_deforming_regions` | field | `bool` | public | — |

### `GPlatesAppLogic::PlateVelocityUtils::TopologicalNetworksVelocities`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TopologicalNetworksVelocities( const std::vector<GPlatesGlobal::PointerTraits<ResolvedTopologicalNetwork>::non_null_ptr_type> &networks)` | constructor | `None` | public | — |
| `calculate_velocity( const GPlatesMaths::PointOnSphere &point, const double &velocity_delta_time = 1.0, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_DELTA_T_TO_T)` | method | `boost::optional< std::pair< // The resolved topological network (if point is inside it's deforming region) // or an interior rigid block of the network... const ReconstructionGeome ...` | public | Returns the velocity at location point if it's inside any network's boundary, otherwise returns false. |
| `network_seq_type` | typedef | `std::vector<GPlatesGlobal::PointerTraits<ResolvedTopologicalNetwork>::non_null_ptr_type>` | private | — |
| `d_networks` | field | `network_seq_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `solve_velocities_on_networks( const GPlatesMaths::PointOnSphere &domain_point, boost::optional<MultiPointVectorField::CodomainElement> &range_element, const PlateVelocityUtils::TopologicalNetworksVelocities &resolved_networks_query, const double &velocity_delta_time, VelocityDeltaTime::Type velocity_delta_time_type)` | function | `bool` | Test the domain point against the resolved topological network. |
| `solve_velocities_on_rigid_plates( const GPlatesMaths::PointOnSphere &domain_point, boost::optional<MultiPointVectorField::CodomainElement> &range_element, const GeometryCookieCutter &rigid_plates_query, const double &velocity_delta_time, VelocityDeltaTime::Type velocity_delta_time_type)` | function | `bool` | Test the domain point against rigid plates (resolved topological boundaries and static polygons). |
| `solve_velocity_on_surfaces( const GPlatesMaths::PointOnSphere &domain_point, boost::optional<MultiPointVectorField::CodomainElement> &range_element, const GeometryCookieCutter &rigid_plates_query, const PlateVelocityUtils::TopologicalNetworksVelocities &resolved_networks_query, const double &velocity_delta_time, Veloci ...` | function | `bool` | Test the domain point against the all surface types. |
| `solve_velocity_at_boundary( const GPlatesMaths::PointOnSphere &point_sample, boost::optional<GPlatesMaths::Vector3D> &velocity_inside_polygon_boundary, boost::optional<GPlatesMaths::Vector3D> &velocity_outside_polygon_boundary, const ReconstructionGeometry *polygon_recon_geom_containing_domain_point, const GeometryCook ...` | function | `void` | Calculate the boundary velocity at the specified point sample (which is very close to the boundary but not on it). |
| `solve_average_velocity_at_boundary( const GPlatesMaths::PointOnSphere &polygon_boundary_point, const GPlatesMaths::PointOnSphere &domain_point, const ReconstructionGeometry *polygon_recon_geom_containing_domain_point, const GeometryCookieCutter &rigid_plates_query, const PlateVelocityUtils::TopologicalNetworksVelocitie ...` | function | `boost::optional<GPlatesMaths::Vector3D>` | Calculate the average velocity, at the specified point on the polygon boundary, by averaging the velocity on each side of the boundary. |
| `solve_velocity_on_surfaces_with_boundary_smoothing( const GPlatesMaths::PointOnSphere &domain_point, boost::optional<MultiPointVectorField::CodomainElement> &range_element, const GeometryCookieCutter &rigid_plates_query, const PlateVelocityUtils::TopologicalNetworksVelocities &resolved_networks_query, const double &vel ...` | function | `bool` | Test the domain point against the all surface types and smooth velocities near boundaries. |
| `GPLATES_APP_LOGIC_PLATEVELOCITYUTILS_H` | macro | `None` | — |
| `detect_velocity_mesh_nodes( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection)` | function | `bool` | Returns true if any features in feature\_collection can be used as a domain for velocity calculations (currently this is feature type "gpml:MeshNode"). |
| `detect_velocity_mesh_node( const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref)` | function | `bool` | Returns true if the specified feature can be used as a domain for velocity calculations (currently this is feature type "gpml:MeshNode"). |
| `create_velocity_field_feature_collection( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection_with_mesh_nodes)` | function | `GPlatesModel::FeatureCollectionHandle::non_null_ptr_type` | Creates a new feature collection containing a feature of type "gpml:VelocityField" for every feature in feature\_collection\_with\_mesh\_nodes that can be used as a domain for velocity calculations (currently this is feature type ... |
| `solve_velocities_on_surfaces( std::vector<MultiPointVectorField::non_null_ptr_type> &multi_point_velocity_fields, const double &reconstruction_time, const std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &velocity_domains, const std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &velocity_surface_ ...` | function | `void` | The precedence is topological networks then topological boundaries then static polygons. |
| `calculate_velocity_colat_lon( const GPlatesMaths::PointOnSphere &point, const GPlatesMaths::FiniteRotation &finite_rotation1, const GPlatesMaths::FiniteRotation &finite_rotation2, const double &delta_time)` | function | `GPlatesMaths::VectorColatitudeLongitude` | Calculates velocity at point by using the rotation between the two specified rotations. delta\_time should be t2-t1. |
| `calculate_velocity_colat_lon( const GPlatesMaths::PointOnSphere &point, const GPlatesModel::integer_plate_id_type &reconstruction_plate_id, const ReconstructionTreeCreator &reconstruction_tree_creator, const double &reconstruction_time, const double &velocity_delta_time, VelocityDeltaTime::Type velocity_delta_time_type ...` | function | `GPlatesMaths::VectorColatitudeLongitude` | Calculates velocity at point by using the rotation between two nearby reconstruction times. |
| `calculate_velocity_vector( const GPlatesMaths::PointOnSphere &point, const GPlatesMaths::FiniteRotation &finite_rotation1, const GPlatesMaths::FiniteRotation &finite_rotation2, const double &delta_time)` | function | `GPlatesMaths::Vector3D` | Calculates velocity at point by using the rotation between the two specified rotations. delta\_time should be t2-t1. |
| `calculate_velocity_vector( const GPlatesMaths::PointOnSphere &point, const GPlatesModel::integer_plate_id_type &reconstruction_plate_id, const ReconstructionTreeCreator &reconstruction_tree_creator, const double &reconstruction_time, const double &velocity_delta_time, VelocityDeltaTime::Type velocity_delta_time_type)` | function | `GPlatesMaths::Vector3D` | Calculates velocity at point by using the rotation between two nearby reconstruction times. |
| `calculate_stage_rotation( const GPlatesModel::integer_plate_id_type &reconstruction_plate_id, const ReconstructionTreeCreator &reconstruction_tree_creator, const double &reconstruction_time, const double &velocity_delta_time, VelocityDeltaTime::Type velocity_delta_time_type)` | function | `GPlatesMaths::FiniteRotation` | Similar to calculate\_velocity\_vector but returns the stage rotation. |

## Notes

- Surface-type precedence is fixed: a point inside both a topological network and a topological boundary (or static polygon) always gets the network's velocity, never a blend, unless boundary smoothing is explicitly requested.
- `calculate_velocity_vector`/`calculate_velocity_colat_lon` (the plate-id overloads) return the zero vector whenever the plate id cannot be found in the reconstruction tree at *either* delta-time endpoint, except for two documented retry cases (a negative younger time, or a plate id present only at the younger time) where the delta-time window is shifted and the lookup retried — see the Doxygen on the header for the exact conditions before assuming a zero result means "no motion".
- `solve_velocities_on_surfaces` uses each domain's *reconstructed* geometry (not present-day) for surface testing, so a velocity domain feature with a non-zero plate id can move between calls; assigning it plate id zero pins it to the spin axis (still subject to a non-zero anchor plate id).
- `create_velocity_field_feature_collection` can return an empty feature collection if the input has no `gpml:MeshNode` features; call `detect_velocity_mesh_nodes` first to avoid that.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 29 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 9 |
| [app-logic/VelocityFieldCalculatorLayerProxy](VelocityFieldCalculatorLayerProxy.md) | app-logic | 8 |
| [app-logic/deprecated/PlateVelocityWorkflow](deprecated/PlateVelocityWorkflow.md) | app-logic | 8 |
| [app-logic/ResolvedTriangulationNetwork](ResolvedTriangulationNetwork.md) | app-logic | 6 |
| [app-logic/ResolvedVertexSourceInfo](ResolvedVertexSourceInfo.md) | app-logic | 4 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 4 |
| [app-logic/ReconstructMethodInterface](ReconstructMethodInterface.md) | app-logic | 3 |
| [app-logic/VelocityFieldCalculatorLayerTask](VelocityFieldCalculatorLayerTask.md) | app-logic | 3 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 3 |
| [app-logic/ReconstructMethodByPlateId](ReconstructMethodByPlateId.md) | app-logic | 1 |
| [qt-widgets/KinematicGraphsDialog](../qt-widgets/KinematicGraphsDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/PlateVelocityUtils.h
python scripts/gpq.py def GPlatesAppLogic::(anonymous)::AddVelocityFieldFeatures --body
python scripts/gpq.py uses AddVelocityFieldFeatures --kind class
python scripts/gpq.py hier AddVelocityFieldFeatures
```

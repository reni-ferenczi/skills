# ReconstructMethodByPlateId

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 44 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructMethodByPlateId.h` | C++ | 199 |
| `src/app-logic/ReconstructMethodByPlateId.cc` | C++ | 775 |

## Overview

`ReconstructMethodByPlateId` is the default `ReconstructMethodInterface` implementation: it reconstructs a feature's present-day geometry by rotating it with the finite rotation for the feature's reconstruction plate ID, resolved through the plate circuit passed in via `Context`. `can_reconstruct_feature` accepts any feature with a non-topological geometry, even one without a plate ID — `reconstruct_feature_geometries` still produces a result in that case, falling back to plate id zero (the spin axis) via the identity-defaulted `ReconstructionInfo`.

The method actually supports two distinct reconstruction paths. When the `Context` carries a `TopologyReconstruct`, geometries are instead advanced incrementally through resolved topological plates/networks — built once per feature by `get_topology_reconstruction_info` into a cached `topology_reconstructed_geometry_time_span_sequence_type` — so that points can migrate across plate boundaries over time and optionally deactivate when they fall outside a network or exceed lifetime-detection thresholds from `ReconstructParams`. When no topology reconstruction is configured, geometries and velocities are computed directly with rigid rotations via `ReconstructUtils::reconstruct_by_plate_id` and `PlateVelocityUtils`. The anonymous-namespace `Transform` wraps the resolved `FiniteRotation` as a `ReconstructMethodFiniteRotation`, and the `CanReconstructFeature` / `GetPresentDayGeometries` visitors implement the present-day-geometry extraction and reconstructability test by walking the feature's `GmlPoint`/`GmlLineString`/`GmlPolygon`/`GmlMultiPoint`/`GpmlConstantValue` properties.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::(anonymous)::Transform`](#gplatesapplogicanonymoustransform) | class | [`ReconstructMethodFiniteRotation`](ReconstructMethodFiniteRotation.md) | — | 0 | The transform used to reconstruct by plate id. |
| [`GPlatesAppLogic::(anonymous)::CanReconstructFeature`](#gplatesapplogicanonymouscanreconstructfeature) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Used to determine if can reconstruct a feature. |
| [`GPlatesAppLogic::(anonymous)::GetPresentDayGeometries`](#gplatesapplogicanonymousgetpresentdaygeometries) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Finds the present day geometries of a feature. |
| [`GPlatesAppLogic::ReconstructMethodByPlateId`](#gplatesapplogicreconstructmethodbyplateid) | class | [`ReconstructMethodInterface`](ReconstructMethodInterface.md) | — | 0 | Reconstructs a feature using its present day geometry and its plate Id. |

## Members

### `GPlatesAppLogic::(anonymous)::Transform`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<Transform>` | public | Convenience typedefs for a shared pointer to a Transform. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const Transform>` | public | — |
| `create( const GPlatesMaths::FiniteRotation &finite_rotation, GPlatesModel::integer_plate_id_type reconstruction_plate_id)` | method | `non_null_ptr_type` | public | Create a transform if have a reconstruction plate id. |
| `create()` | method | `non_null_ptr_type` | public | Create an identity transform if do \*not\* have a reconstruction plate id. |
| `d_reconstruction_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `Transform( const GPlatesMaths::FiniteRotation &finite_rotation, GPlatesModel::integer_plate_id_type reconstruction_plate_id)` | constructor | `None` | private | — |
| `Transform()` | constructor | `None` | private | — |
| `less_than_compare_finite_rotation_parameters( const ReconstructMethodFiniteRotation &rhs)` | method | `bool` | private | — |

### `GPlatesAppLogic::(anonymous)::CanReconstructFeature`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CanReconstructFeature()` | constructor | `None` | public | — |
| `can_reconstruct()` | method | `bool` | public | Returns true any features visited by us can be reconstructed. |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | private | — |
| `finalise_post_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | private | — |
| `visit_gml_line_string( const GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | private | — |
| `visit_gml_multi_point( const GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | private | — |
| `visit_gml_orientable_curve( const GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | private | — |
| `visit_gml_point( const GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gml_polygon( const GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | private | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `d_can_reconstruct` | field | `bool` | private | — |
| `d_has_geometry` | field | `bool` | private | — |

### `GPlatesAppLogic::(anonymous)::GetPresentDayGeometries`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GetPresentDayGeometries( std::vector<ReconstructMethodInterface::Geometry> &present_day_geometries)` | constructor | `None` | public | — |
| `visit_gml_line_string( GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | private | — |
| `visit_gml_multi_point( GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | private | — |
| `visit_gml_orientable_curve( GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | private | — |
| `visit_gml_point( GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gml_polygon( GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | private | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `d_present_day_geometries` | field | `std::vector<ReconstructMethodInterface::Geometry>` | private | — |

### `GPlatesAppLogic::ReconstructMethodByPlateId`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructMethodByPlateId>` | public | Convenience typedefs for a shared pointer to a ReconstructMethodByPlateId. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructMethodByPlateId>` | public | — |
| `can_reconstruct_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature_weak_ref)` | method | `bool` | public | Returns true if can reconstruct the specified feature. |
| `create( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const Context &context)` | method | `ReconstructMethodByPlateId::non_null_ptr_type` | public | Creates a ReconstructMethodByPlateId object associated with the specified feature. |
| `get_present_day_feature_geometries( std::vector<Geometry> &present_day_geometries)` | method | `void` | public | Returns the present day geometries of the feature associated with this reconstruct method. |
| `reconstruct_feature_geometries( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const ReconstructHandle::type &reconstruct_handle, const Context &context, const double &reconstruction_time)` | method | `void` | public | Reconstructs the feature associated with this reconstruct method to the specified reconstruction time and returns one or more reconstructed feature geometries. |
| `reconstruct_feature_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &reconstructed_feature_velocities, const ReconstructHandle::type &reconstruct_handle, const Context &context, const double &reconstruction_time, const double &velocity_delta_time, VelocityDeltaTime::Type velocity_delta_time_type)` | method | `void` | public | Calculates velocities at the positions of the reconstructed feature geometries, of the feature associated with this reconstruct method, at the specified reconstruction time and returns one or more reconstructed feature \*velocities\*. |
| `reconstruct_geometry( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry, const Context &context, const double &reconstruction_time, bool reverse_reconstruct)` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | Reconstructs the specified geometry from present day to the specified reconstruction time - unless reverse\_reconstruct is true in which case the geometry is assumed to be the reconstructed geometry (at the reconstruction time) and the ... |
| `get_topology_reconstructed_geometry_time_spans( topology_reconstructed_geometry_time_span_sequence_type &topology_reconstructed_geometry_time_spans, const Context &context)` | method | `void` | public | Returns any topology-reconstructed geometry time spans. |
| `ReconstructionInfo` | struct | `None` | private | Feature property information used for reconstructing. |
| `d_present_day_geometries` | field | `boost::optional< std::vector<Geometry> >` | private | Cache the present day geometries so we don't need to gather them each time they're reconstructed. |
| `d_reconstruction_info` | field | `boost::optional<ReconstructionInfo>` | private | Cache the reconstruction information so can re-use it for each reconstruction. |
| `d_topology_reconstructed_geometry_time_spans` | field | `boost::optional<topology_reconstructed_geometry_time_span_sequence_type>` | private | The topology reconstructed geometry look up tables, or boost::none if not reconstructing using topologies. |
| `ReconstructMethodByPlateId( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const Context &context)` | constructor | `None` | private | — |
| `get_reconstruction_info` | field | `ReconstructionInfo` | private | — |
| `get_topology_reconstruction_info( const Context &context)` | method | `boost::optional<const topology_reconstructed_geometry_time_span_sequence_type &>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTMETHODBYPLATEID_H` | macro | `None` | — |

## Notes

- `d_present_day_geometries`, `d_reconstruction_info` and `d_topology_reconstructed_geometry_time_spans` are `mutable` caches computed lazily on first use and reused for every subsequent reconstruction of the same feature; they are invalidated only by destroying the object, so a `ReconstructMethodByPlateId` must not outlive changes to the underlying feature's geometry or plate ID properties.
- Once topology reconstruction is set up for a feature (`get_topology_reconstruction_info` succeeds), the object commits to that path for its lifetime; `reconstruct_feature_geometries`/`reconstruct_feature_velocities` always check for a topology time span first and only fall back to rigid-rotation-by-plate-id when none exists.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructMethodRegistry](ReconstructMethodRegistry.md) | app-logic | 9 |
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 9 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 4 |
| [qt-widgets/deprecated/CreateTopologyWidget](../qt-widgets/deprecated/CreateTopologyWidget.md) | qt-widgets | 4 |
| [app-logic/ResolvedTriangulationNetwork](ResolvedTriangulationNetwork.md) | app-logic | 2 |
| [app-logic/ResolvedVertexSourceInfo](ResolvedVertexSourceInfo.md) | app-logic | 2 |
| [qt-widgets/QueryFeaturePropertiesWidget](../qt-widgets/QueryFeaturePropertiesWidget.md) | qt-widgets | 2 |
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 1 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 1 |
| [view-operations/MoveVertexGeometryOperation](../view-operations/MoveVertexGeometryOperation.md) | view-operations | 1 |
| [view-operations/SplitFeatureUndoCommand](../view-operations/SplitFeatureUndoCommand.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructMethodByPlateId.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructMethodByPlateId --body
python scripts/gpq.py uses ReconstructMethodByPlateId --kind class
python scripts/gpq.py hier ReconstructMethodByPlateId
```

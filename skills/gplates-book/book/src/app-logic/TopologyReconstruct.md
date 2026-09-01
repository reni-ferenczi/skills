# TopologyReconstruct

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 223 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TopologyReconstruct.h` | C++ | 1144 |
| `src/app-logic/TopologyReconstruct.cc` | C++ | 3231 |

## Overview

[[[PROSE overview unit=app-logic/TopologyReconstruct tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::(anonymous)::IntersectGeometryPointsAndResolvedBoundarySmallCircleBounds`](#gplatesapplogicanonymousintersectgeometrypointsandresolvedboundarysmallcirclebounds) | class | — | — | 0 | Predicate to test if the geometry \*points\* bounding small circle intersects the resolved boundary bounding small circle. |
| [`GPlatesAppLogic::(anonymous)::IntersectGeometryPointsAndResolvedNetworkSmallCircleBounds`](#gplatesapplogicanonymousintersectgeometrypointsandresolvednetworksmallcirclebounds) | class | — | — | 0 | Predicate to test if the geometry \*points\* bounding small circle intersects the resolved network bounding small circle. |
| [`GPlatesAppLogic::TopologyReconstruct`](#gplatesapplogictopologyreconstruct) | class | [`GPlatesUtils::ReferenceCount<TopologyReconstruct>`](../utils/ReferenceCount.md) | — | 0 | Uses topologies (rigid and deforming plates) to incrementally reconstruct geometries over time. |

## Members

### `GPlatesAppLogic::(anonymous)::IntersectGeometryPointsAndResolvedBoundarySmallCircleBounds`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `IntersectGeometryPointsAndResolvedBoundarySmallCircleBounds( const GPlatesMaths::BoundingSmallCircle *geometry_points_bounding_small_circle)` | constructor | `None` | public | — |
| `operator()( const ResolvedTopologicalBoundary::non_null_ptr_type &rtb)` | operator | `bool` | public | — |
| `d_geometry_points_bounding_small_circle` | field | `GPlatesMaths::BoundingSmallCircle` | private | — |

### `GPlatesAppLogic::(anonymous)::IntersectGeometryPointsAndResolvedNetworkSmallCircleBounds`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `IntersectGeometryPointsAndResolvedNetworkSmallCircleBounds( const GPlatesMaths::BoundingSmallCircle *geometry_points_bounding_small_circle)` | constructor | `None` | public | — |
| `operator()( const ResolvedTopologicalNetwork::non_null_ptr_type &rtn)` | operator | `bool` | public | — |
| `d_geometry_points_bounding_small_circle` | field | `GPlatesMaths::BoundingSmallCircle` | private | — |

### `GPlatesAppLogic::TopologyReconstruct`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<TopologyReconstruct>` | public | A convenience typedef for a shared pointer to a non-const TopologyReconstruct. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const TopologyReconstruct>` | public | A convenience typedef for a shared pointer to a const TopologyReconstruct. |
| `rtb_seq_type` | typedef | `std::vector<ResolvedTopologicalBoundary::non_null_ptr_type>` | public | Typedef for a sequence of resolved topological boundaries. |
| `rtn_seq_type` | typedef | `std::vector<ResolvedTopologicalNetwork::non_null_ptr_type>` | public | Typedef for a sequence of resolved topological networks. |
| `resolved_boundary_time_span_type` | typedef | `TimeSpanUtils::TimeSampleSpan<rtb_seq_type>` | public | A look up table of resolved topological boundaries over a time span. |
| `resolved_network_time_span_type` | typedef | `TimeSpanUtils::TimeSampleSpan<rtn_seq_type>` | public | A look up table of resolved topological networks over a time span. |
| `DeactivatePoint` | class | `None` | public | Interface for deactivating geometry points as a geometry is reconstructed forward and backward from its geometry import time. |
| `DefaultDeactivatePoint` | class | `None` | public | Default implementation for deactivating geometry points. |
| `create( const TimeSpanUtils::TimeRange &time_range, const resolved_boundary_time_span_type::non_null_ptr_to_const_type &resolved_boundary_time_span, const resolved_network_time_span_type::non_null_ptr_to_const_type &resolved_network_time_span, const ReconstructionTreeCreator &reconstruction_tree_creator)` | method | `non_null_ptr_type` | public | Creates a new TopologyReconstruct. |
| `create_geometry_time_span( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry, GPlatesModel::integer_plate_id_type reconstruction_plate_id, const double &geometry_import_time = 0.0, boost::optional<DeactivatePoint::non_null_ptr_to_const_type> deactivate_points = boost::none, boost::optional<doub ...` | method | `GPlatesUtils::non_null_intrusive_ptr<GeometryTimeSpan>` | public | Creates a time span for the specified present day geometry. |
| `GeometryTimeSpan` | class | `None` | public | Builds and keeps track of a geometry over a time span. |
| `d_time_range` | field | `TimeSpanUtils::TimeRange` | private | — |
| `d_resolved_boundary_time_span` | field | `resolved_boundary_time_span_type::non_null_ptr_to_const_type` | private | — |
| `d_resolved_network_time_span` | field | `resolved_network_time_span_type::non_null_ptr_to_const_type` | private | — |
| `d_reconstruction_tree_creator` | field | `ReconstructionTreeCreator` | private | — |
| `TopologyReconstruct( const TimeSpanUtils::TimeRange &time_range, const resolved_boundary_time_span_type::non_null_ptr_to_const_type &resolved_boundary_time_span, const resolved_network_time_span_type::non_null_ptr_to_const_type &resolved_network_time_span, const ReconstructionTreeCreator &reconstruction_tree_creator)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `copysign` | macro | `_copysign` | — |
| `INVERSE_EARTH_EQUATORIAL_RADIUS_KMS` | variable | `double` | Inverse of Earth radius (Kms). |
| `get_stage_rotation( GPlatesModel::integer_plate_id_type reconstruction_plate_id, const ReconstructionTreeCreator &reconstruction_tree_creator, const double &initial_time, const double &final_time)` | function | `GPlatesMaths::FiniteRotation` | Get the rigid rotation from initial\_time to final\_time. |
| `DEFAULT_THRESHOLD_VELOCITY_DELTA` | variable | `double` | — |
| `DEFAULT_THRESHOLD_DISTANCE_TO_BOUNDARY_IN_KMS_PER_MY` | variable | `double` | — |
| `DEFAULT_DEACTIVATE_POINTS_THAT_FALL_OUTSIDE_A_NETWORK` | variable | `bool` | — |
| `GPLATES_APP_LOGIC_TOPOLOGYRECONSTRUCT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/TopologyReconstruct tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 39 |
| [app-logic/ScalarCoverageTimeSpan](ScalarCoverageTimeSpan.md) | app-logic | 29 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 21 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 19 |
| [app-logic/ScalarCoverageEvolution](ScalarCoverageEvolution.md) | app-logic | 13 |
| [app-logic/ReconstructParams](ReconstructParams.md) | app-logic | 10 |
| [app-logic/ReconstructMethodByPlateId](ReconstructMethodByPlateId.md) | app-logic | 8 |
| [app-logic/TopologyReconstructedFeatureGeometry](TopologyReconstructedFeatureGeometry.md) | app-logic | 8 |
| [app-logic/ReconstructMethodInterface](ReconstructMethodInterface.md) | app-logic | 7 |
| [app-logic/DeformationStrainRate](DeformationStrainRate.md) | app-logic | 5 |
| [app-logic/ReconstructContext](ReconstructContext.md) | app-logic | 3 |
| [app-logic/PartitionFeatureUtils](PartitionFeatureUtils.md) | app-logic | 2 |
| [app-logic/ReconstructScalarCoverageLayerProxy](ReconstructScalarCoverageLayerProxy.md) | app-logic | 2 |
| [file-io/GMTFormatDeformationExport](../file-io/GMTFormatDeformationExport.md) | file-io | 1 |
| [file-io/GMTFormatReconstructedScalarCoverageExport](../file-io/GMTFormatReconstructedScalarCoverageExport.md) | file-io | 1 |
| [file-io/GpmlFormatDeformationExport](../file-io/GpmlFormatDeformationExport.md) | file-io | 1 |
| [file-io/GpmlFormatReconstructedScalarCoverageExport](../file-io/GpmlFormatReconstructedScalarCoverageExport.md) | file-io | 1 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/TopologyReconstruct.h
python scripts/gpq.py def GPlatesAppLogic::TopologyReconstruct --body
python scripts/gpq.py uses TopologyReconstruct --kind class
python scripts/gpq.py hier TopologyReconstruct
```

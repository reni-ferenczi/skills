# TopologyReconstruct

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 223 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TopologyReconstruct.h` | C++ | 1144 |
| `src/app-logic/TopologyReconstruct.cc` | C++ | 3231 |

## Overview

This is the deformation engine. Ordinary reconstruction rotates a whole geometry by
one finite rotation; topological reconstruction advances it one time step at a time,
letting every point follow whichever rigid plate or deforming network it happens to
be sitting inside at that moment. `TopologyReconstruct` itself is only the context —
a `TimeRange` plus the already-resolved boundaries and networks for each time slot,
plus a fallback `ReconstructionTreeCreator`. `ReconstructLayerProxy` builds it, filling
the two `TimeSampleSpan`s from `TopologyGeometryResolverLayerProxy` and
`TopologyNetworkResolverLayerProxy`; `ReconstructMethodByPlateId` then calls
`create_geometry_time_span` once per feature geometry, and the resulting
`GeometryTimeSpan` is what `TopologyReconstructedFeatureGeometry` and
`ScalarCoverageTimeSpan` read from. Everything interesting lives in that nested class.

Construction does all the work. The geometry is flattened to points — every geometry
type becomes a multi-point, with polylines and polygons optionally tessellated first,
`InterpolateOriginalPoints` recording which original segment each tessellated point
came from so scalar coverages can be interpolated onto the new points. The import
time is snapped to a time slot, the present-day geometry is rigidly rotated there, and
`reconstruct_time_steps` then marches outward in *both* directions from that slot,
which is why paleo-geometries work: a fracture zone imported at 50 Ma is masked by
mid-ocean ridges going backward and by subduction zones going forward. Each step, each
point is tried against the resolved networks first and the resolved boundaries second
— networks win deliberately, since a network may overlap a boundary — deforming
through `ResolvedTriangulation::Network::calculate_deformed_point` or rotating by the
containing boundary's plate stage rotation. Points that land in neither get one shared
rigid stage rotation from the feature's own `d_reconstruction_plate_id`, and if *no*
point intersects anything the whole sample is rigidly rotated in one go. Two
optimisations matter for large geometries: the active points' bounding small circle
culls topologies that cannot possibly contain them, and a hit moves that
boundary/network to the front of the list, since the next point is usually in the same
one.

Between steps, an optional `DeactivatePoint` decides whether a point has been
subducted going forward or consumed by a ridge going backward.
`DefaultDeactivatePoint` fires only on a *transition* — network to rigid plate, rigid
plate to network, or rigid plate to a different plate ID — and then only if the
velocity difference across that transition exceeds a threshold *and* the point's
previous position was close enough to the previous topology's boundary to have reached
it. Measuring from the previous position rather than the current one is the crux: a
boundary that appears next to a point (a plate splitting) must not swallow it, while a
boundary that disappears (a merge) should. Deactivated points become null entries in
the sample; when the last one goes, the span records a time slot of appearance or
disappearance and `is_valid` reports the geometry as gone from there on — which is
distinct from, and narrower than, the feature's own valid time.

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

**Point index is the identity, and it is invariant across every sample.** Deactivated
points are set to `NULL` in place; the vector is never shortened, and the code asserts
that adjacent samples have equal size. `get_all_geometry_data` and
`get_points_are_active` preserve that indexing (inactive points come back as
`boost::none` / `false`), while `get_geometry`, `get_geometry_data` and
`get_velocities` compact the output down to active points only. Mixing the two views
and pairing them up by index is the easy mistake here. Likewise `NULL` in
`GeometryPoint::strain_rate` or `strain` means *zero* strain rate / identity strain,
not missing data.

**The present-day sample is rewritten during construction.** Unless the geometry
import time is younger than the end of the time range, `initialise_time_windows`
replaces the present-day sample with the end-of-range sample rigidly rotated back to
present day, so the points topologies produced — not the points you passed in — are
what the span reports at 0 Ma. The import time itself is also mutated: it is snapped to
the nearest time slot, so `get_geometry_import_time` can differ from the argument, by
up to half a time increment.

**Two pool-allocator regimes, and the distinction is load-bearing.** Samples stored in
the time span share the span's `PoolAllocator`, so their `GeometryPoint` and strain
objects can be shared by pointer and live as long as the span. Samples manufactured on
demand for an arbitrary time — the `create_rigid_geometry_sample` and
`interpolate_geometry_sample` callbacks handed to the `TimeWindowSpan` — each get a
*fresh* allocator, which is why those paths deep-copy strains instead of sharing them;
without that, repeated queries at arbitrary times would grow the span's pool without
bound. Any new code that stores a computed sample into the span must pass
`d_pool_allocator`, and any code that does not must not.

**Lazy state under `const`, so one `GeometryTimeSpan` is single-threaded.** Strain
rates are computed per sample on first access and total strains in a single forward
pass over the whole span; both are driven by the `mutable` `d_accessing_strain_rates` /
`d_accessing_strains` counters that the `AccessingStrainRates` and `AccessingStrains`
RAII scopes bump, and `get_geometry_sample` is the single funnel that triggers
`initialise_deformation_total_strains`. Reach around it — calling
`GeometrySample::get_geometry_points` directly, or fetching strains without entering
the scope — and you get zeros rather than an error. Concurrent calls on one span race
on all of it.

**Velocities between time slots are not evaluated at the requested time.**
`get_velocities` computes them at the nearest bounding slot *towards the geometry
import time*, deliberately mirroring `interpolate_geometry_sample`, so that the active
point count matches the interpolated domain points; only the returned domain positions
are interpolated. There is an assert on that size match, and it is the reason the
choice cannot be simplified.

**`DefaultDeactivatePoint`'s stage-rotation cache does not work as its comment
claims.** `d_velocity_stage_rotation_time` is never assigned anywhere in the unit, so
`get_or_create_velocity_stage_rotation` clears the map on every call whose
reconstruction time is not 0.0, and the by-plate-ID reuse it is meant to provide never
materialises. Also note that the `create` doc comment refers to a `time_increment`
parameter that the function does not have — the time increment is derived from the
previous and current times passed to `deactivate`.

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

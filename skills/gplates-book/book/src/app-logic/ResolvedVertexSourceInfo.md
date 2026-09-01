# ResolvedVertexSourceInfo

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 70 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ResolvedVertexSourceInfo.h` | C++ | 588 |
| `src/app-logic/ResolvedVertexSourceInfo.cc` | C++ | 257 |

## Overview

Resolving a topology throws away provenance. A resolved topological boundary is
assembled from sub-segments clipped out of other resolved geometries, which were
themselves assembled from `ReconstructedFeatureGeometry` objects, and by the time
the boundary polygon exists nothing in it says which plate moved any particular
vertex. Velocity calculation needs exactly that. `ResolvedVertexSourceInfo` is the
small, shared, reference-counted record that carries it: enough of the originating
RFG — a `ReconstructionTreeCreator` plus either a reconstruction plate ID or the RFG
itself — to recompute a stage rotation at an arbitrary time and delta time, long
after resolution finished. `ResolvedTopologicalBoundary`, `ResolvedTopologicalLine`,
`ResolvedTopologicalNetwork` and the sub-segment classes each hold a
`resolved_vertex_source_info_seq_type` running parallel to their vertex sequence, one
entry per vertex, and build it lazily on first request; sharing one instance across a
whole run of vertices from the same source is the point of the reference counting.

`d_source` is a five-way `boost::variant` and every public operation is a
`boost::apply_visitor` over it. Two cases are leaves derived from an RFG:
`create_source_from_reconstruction_properties` picks `HalfStageRotationProperties`
when the RFG's reconstruct method is `ReconstructMethod::HALF_STAGE_ROTATION` and
`PlateIdProperties` otherwise, defaulting a missing plate ID to zero. One case,
`StageRotation`, wraps an already-computed rotation, used by
`ResolvedTriangulation::Network` for interpolated points such as subdivided edge
mid-points that have no single source feature. The remaining two are composites built
by `ResolvedTopologicalSubSegmentImpl` when it rubber-bands adjacent sections:
`FixedPointVelocityAdapter` pins velocity evaluation to a section end point, and
`InterpolateVertexSourceInfos` blends two of those for a rubber-band vertex lying
between two sections.

The two velocity entry points deliberately disagree on the interpolated case.
`get_stage_rotation` interpolates the two child stage rotations with
`GPlatesMaths::interpolate`, whereas `get_velocity_vector` computes each child's
velocity separately and interpolates the resulting `Vector3D`s. That is not
redundancy: a `FixedPointVelocityAdapter` child substitutes its own fixed point for
the caller's point, and interpolating rotations first would evaluate the blended
rotation at the caller's point, discarding both fixed points. If you touch the
visitors, preserve that asymmetry.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ResolvedVertexSourceInfo`](#gplatesapplogicresolvedvertexsourceinfo) | class | `boost::equality_comparable<ResolvedVertexSourceInfo>`<br>[`GPlatesUtils::ReferenceCount<ResolvedVertexSourceInfo>`](../utils/ReferenceCount.md) | — | 0 | Information, shared by vertices of a resolved geometry, that references the original reconstructed feature geometry. |
| [`GPlatesAppLogic::resolved_vertex_source_info_seq_type`](#gplatesapplogicresolved_vertex_source_info_seq_type) | typedef | — | — | 0 | Typedef for a sequence of ResolvedVertexSourceInfo objects. |

## Members

### `GPlatesAppLogic::ResolvedVertexSourceInfo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ResolvedVertexSourceInfo>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ResolvedVertexSourceInfo>` | public | — |
| `create( const ReconstructedFeatureGeometry::non_null_ptr_to_const_type &reconstruction_properties)` | method | `non_null_ptr_type` | public | Create a source info from a reconstructed geometry/feature. |
| `create( ResolvedVertexSourceInfo::non_null_ptr_to_const_type source_info, const GPlatesMaths::PointOnSphere &fixed_point)` | method | `non_null_ptr_type` | public | Adapt a source info to calculate velocity at a fixed point. |
| `create( ResolvedVertexSourceInfo::non_null_ptr_to_const_type source_info1, ResolvedVertexSourceInfo::non_null_ptr_to_const_type source_info2, const double &interpolate_ratio)` | method | `non_null_ptr_type` | public | Create an interpolation between two source infos. interpolate\_ratio is in range \[0, 1\] where 0 represents source\_info1 and 1 represents source\_info2. |
| `create( const GPlatesMaths::FiniteRotation &stage_rotation, const ReconstructionTreeCreator &reconstruction_tree_creator)` | method | `non_null_ptr_type` | public | Create from a pre-calculated stage rotation. |
| `get_stage_rotation( const double &reconstruction_time, const double &velocity_delta_time, VelocityDeltaTime::Type velocity_delta_time_type)` | method | `GPlatesMaths::FiniteRotation` | public | Get the stage rotation for the specified reconstruction time and velocity delta time. |
| `get_velocity_vector( const GPlatesMaths::PointOnSphere &point, const double &reconstruction_time, const double &velocity_delta_time, VelocityDeltaTime::Type velocity_delta_time_type)` | method | `GPlatesMaths::Vector3D` | public | Calculates the velocity vector at the specified point location. |
| `get_reconstruction_tree_creator()` | method | `ReconstructionTreeCreator` | public | Return the ReconstructionTreeCreator associated with this vertex. |
| `operator==( const ResolvedVertexSourceInfo &rhs)` | operator | `bool` | public | Equality operator - operator != provided by boost::equality\_comparable. |
| `PlateIdProperties` | struct | `None` | private | Geometry was reconstructed by plate ID. |
| `HalfStageRotationProperties` | struct | `None` | private | Geometry was reconstructed by half stage rotation. |
| `FixedPointVelocityAdapter` | struct | `None` | private | Adapter that fixes velocity calculations to a specific point. |
| `InterpolateVertexSourceInfos` | struct | `None` | private | Interpolating between two vertex source infos. |
| `StageRotation` | struct | `None` | private | — |
| `source_type` | typedef | `boost::variant< PlateIdProperties, HalfStageRotationProperties, FixedPointVelocityAdapter, InterpolateVertexSourceInfos, StageRotation>` | private | Vertex source is one of the above types. |
| `CalcStageRotationVisitor` | struct | `None` | private | Variant visitor to calculate stage rotation. |
| `CalcVelocityVectorVisitor` | struct | `None` | private | Variant visitor to calculate velocity vector. |
| `GetReconstructionTreeCreatorVisitor` | struct | `None` | private | Variant visitor to retrieve a ReconstructionTreeCreator. |
| `EqualityVisitor` | struct | `None` | private | Variant visitor to compare equality. |
| `stage_rotation_key_type` | typedef | `boost::tuple< GPlatesMaths::Real/*reconstruction_time*/, GPlatesMaths::Real/*velocity_delta_time*/, VelocityDeltaTime::Type>` | private | Cache the stage rotation for a specific reconstruction time and velocity delta time. |
| `d_source` | field | `source_type` | private | — |
| `d_cached_stage_rotation` | field | `boost::optional< std::pair< stage_rotation_key_type, GPlatesMaths::FiniteRotation> >` | private | Stage rotation key (input parameters) and value (stage rotation). |
| `ResolvedVertexSourceInfo( const ReconstructedFeatureGeometry::non_null_ptr_to_const_type &reconstruction_properties)` | constructor | `None` | private | Create source info using reconstruction by plate ID or by half-stage rotation. |
| `ResolvedVertexSourceInfo( ResolvedVertexSourceInfo::non_null_ptr_to_const_type source_info, const GPlatesMaths::PointOnSphere &fixed_point)` | constructor | `None` | private | Adapt a source info to calculate velocity at a fixed point. |
| `ResolvedVertexSourceInfo( ResolvedVertexSourceInfo::non_null_ptr_to_const_type source_info1, ResolvedVertexSourceInfo::non_null_ptr_to_const_type source_info2, const double &interpolate_ratio)` | constructor | `None` | private | Create an interpolated source info (between two other source infos). |
| `ResolvedVertexSourceInfo( const GPlatesMaths::FiniteRotation &stage_rotation, const ReconstructionTreeCreator &reconstruction_tree_creator)` | constructor | `None` | private | — |
| `create_source_from_reconstruction_properties( const ReconstructedFeatureGeometry::non_null_ptr_to_const_type &reconstruction_properties)` | method | `source_type` | private | Create source info using reconstruction by plate ID or by half-stage rotation. |
| `calc_stage_rotation( const double &reconstruction_time, const double &velocity_delta_time, VelocityDeltaTime::Type velocity_delta_time_type)` | method | `GPlatesMaths::FiniteRotation` | private | Calculate the stage rotation for the specified reconstruction time and velocity delta time. |

### `GPlatesAppLogic::resolved_vertex_source_info_seq_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator==( const ResolvedVertexSourceInfo &rhs)` | operator | `bool` | — |
| `operator()( const PlateIdProperties &source)` | operator | `GPlatesMaths::FiniteRotation` | — |
| `operator()( const HalfStageRotationProperties &source)` | operator | `GPlatesMaths::FiniteRotation` | — |
| `operator()( const FixedPointVelocityAdapter &source)` | operator | `GPlatesMaths::FiniteRotation` | — |
| `operator()( const InterpolateVertexSourceInfos &source)` | operator | `GPlatesMaths::FiniteRotation` | — |
| `operator()( const PlateIdProperties &lhs, const PlateIdProperties &rhs)` | operator | `bool` | — |
| `operator()( const HalfStageRotationProperties &lhs, const HalfStageRotationProperties &rhs)` | operator | `bool` | — |
| `operator()( const FixedPointVelocityAdapter &lhs, const FixedPointVelocityAdapter &rhs)` | operator | `bool` | — |
| `operator()( const InterpolateVertexSourceInfos &lhs, const InterpolateVertexSourceInfos &rhs)` | operator | `bool` | — |
| `operator()( const StageRotation &lhs, const StageRotation &rhs)` | operator | `bool` | — |
| `GPLATES_APP_LOGIC_RESOLVEDVERTEXSOURCEINFO_H` | macro | `None` | — |

## Notes

**The caches are mutable, so the const methods are not thread safe.**
`d_cached_stage_rotation` is a single-slot memo keyed on the tuple
(reconstruction time, velocity delta time, delta time type); a call with a different
key overwrites it. This is tuned for the intended access pattern — every vertex
sharing one source info asks for the same parameters in immediate succession —
and degenerates to no caching at all if callers alternate parameters. Because an
instance is shared across many vertices and reached through
`non_null_ptr_to_const_type`, two threads calling `get_stage_rotation` on the same
object race on that member. `HalfStageRotationProperties::reconstruction_params` is
a second mutable lazy cache with the same caveat; it runs a
`ReconstructionFeatureProperties` visitor over the RFG's feature reference on first
use, so the source feature must still be alive at that point, not merely at
construction.

**Equality is structural, not identity, and is deliberately loose.** The templated
fallback in `EqualityVisitor` makes any two different variant cases unequal.
`PlateIdProperties` compares plate IDs *only* — two source infos from different
rotation models compare equal. `HalfStageRotationProperties` compares the five
half-stage inputs (left and right plate IDs, geometry import time, spreading
asymmetry, reconstruction method) rather than the features. `InterpolateVertexSourceInfos`
also treats the mirrored pair — ratio `1 - r` with the two sources swapped — as
equal. `StageRotation` compares unit quaternions, so it is decided by the rotation
value, not by whatever produced it. Callers use this to collapse runs of vertices
that would give identical velocities; do not use it to test whether two vertices
came from the same feature.

**Chains keep their children alive.** `FixedPointVelocityAdapter` and
`InterpolateVertexSourceInfos` hold `non_null_ptr_to_const_type` to their operands,
so an adapter over an interpolation over two leaves retains the whole chain,
including the RFG referenced by any half-stage leaf. Velocity and equality both
recurse down that chain, so depth costs time as well as memory — the composites are
only ever built one or two levels deep by the current callers.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ResolvedTopologicalSubSegmentImpl](ResolvedTopologicalSubSegmentImpl.md) | app-logic | 24 |
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 18 |
| [app-logic/ResolvedTriangulationDelaunay2](ResolvedTriangulationDelaunay2.md) | app-logic | 13 |
| [app-logic/ResolvedTriangulationNetwork](ResolvedTriangulationNetwork.md) | app-logic | 13 |
| [app-logic/ResolvedTopologicalGeometrySubSegment](ResolvedTopologicalGeometrySubSegment.md) | app-logic | 12 |
| [app-logic/ResolvedTopologicalSharedSubSegment](ResolvedTopologicalSharedSubSegment.md) | app-logic | 12 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 9 |
| [app-logic/VelocityFieldCalculatorLayerProxy](VelocityFieldCalculatorLayerProxy.md) | app-logic | 8 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 7 |
| [app-logic/ResolvedTopologicalBoundary](ResolvedTopologicalBoundary.md) | app-logic | 6 |
| [app-logic/ResolvedTopologicalLine](ResolvedTopologicalLine.md) | app-logic | 6 |
| [app-logic/ResolvedTopologicalNetwork](ResolvedTopologicalNetwork.md) | app-logic | 6 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 5 |
| [app-logic/ReconstructMethodByPlateId](ReconstructMethodByPlateId.md) | app-logic | 5 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 5 |
| [app-logic/ScalarField3DLayerProxy](ScalarField3DLayerProxy.md) | app-logic | 4 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 4 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 4 |
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 3 |
| [app-logic/TopologyInternalUtils](TopologyInternalUtils.md) | app-logic | 3 |

*... and 5 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ResolvedVertexSourceInfo.h
python scripts/gpq.py def GPlatesAppLogic::ResolvedVertexSourceInfo --body
python scripts/gpq.py uses ResolvedVertexSourceInfo --kind class
python scripts/gpq.py hier ResolvedVertexSourceInfo
```

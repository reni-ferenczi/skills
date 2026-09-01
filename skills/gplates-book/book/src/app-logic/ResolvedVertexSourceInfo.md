# ResolvedVertexSourceInfo

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 70 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ResolvedVertexSourceInfo.h` | C++ | 588 |
| `src/app-logic/ResolvedVertexSourceInfo.cc` | C++ | 257 |

## Overview

[[[PROSE overview unit=app-logic/ResolvedVertexSourceInfo tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=app-logic/ResolvedVertexSourceInfo tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

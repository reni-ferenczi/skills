# ResolvedTriangulationNetwork

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 72 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ResolvedTriangulationNetwork.h` | C++ | 1220 |
| `src/app-logic/ResolvedTriangulationNetwork.cc` | C++ | 2406 |

## Overview

[[[PROSE overview unit=app-logic/ResolvedTriangulationNetwork tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::DelaunayPoint2`](#gplatesapplogicdelaunaypoint2) | struct | — | — | 0 | Same as ResolvedTriangulation::Network::DelaunayPoint but stores a 2D point (instead of 3D) so can be spatially sorted by CGAL. |
| [`GPlatesAppLogic::DelaunayPoint2SpatialSortingTraits`](#gplatesapplogicdelaunaypoint2spatialsortingtraits) | struct | — | — | 0 | To assist CGAL::spatial\_sort when sorting DelaunayPoint2 objects. |
| [`GPlatesAppLogic::ResolvedTriangulation::Network`](#gplatesapplogicresolvedtriangulationnetwork) | class | [`GPlatesUtils::ReferenceCount<Network>`](../utils/ReferenceCount.md) | — | 0 | The central access point for resolved topological network triangulations. |

## Members

### `GPlatesAppLogic::DelaunayPoint2`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DelaunayPoint2( const ResolvedTriangulation::Network::DelaunayPoint *delaunay_point_, const GPlatesMaths::LatLonPoint &lat_lon_point_, const ResolvedTriangulation::Delaunay_2::Point &point_2_)` | constructor | `None` | public | — |
| `delaunay_point` | field | `ResolvedTriangulation::Network::DelaunayPoint` | public | The delaunay point information. |
| `lat_lon_point` | field | `GPlatesMaths::LatLonPoint` | public | Lat/lon coordinates. |
| `point_2` | field | `ResolvedTriangulation::Delaunay_2::Point` | public | The 2D projected point (azimuthal equal area projection). |
| `LessX` | struct | `None` | public | — |
| `LessY` | struct | `None` | public | — |

### `GPlatesAppLogic::DelaunayPoint2SpatialSortingTraits`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Point_2` | typedef | `DelaunayPoint2` | public | — |
| `Less_x_2` | typedef | `DelaunayPoint2::LessX` | public | — |
| `Less_y_2` | typedef | `DelaunayPoint2::LessY` | public | — |
| `less_x_2_object()` | method | `Less_x_2` | public | — |
| `less_y_2_object()` | method | `Less_y_2` | public | — |

### `GPlatesAppLogic::ResolvedTriangulation::Network`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<Network>` | public | A convenience typedef for a shared pointer to a non-const Network. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const Network>` | public | A convenience typedef for a shared pointer to a const Network. |
| `RigidBlock` | class | `None` | public | An interior rigid block in the network. |
| `rigid_block_seq_type` | typedef | `std::vector<RigidBlock>` | public | Typedef for a sequence of RigidBlock objects. |
| `PointLocation` | class | `None` | public | Location of a point within network (either inside a Delaunay face or a rigid block). |
| `DelaunayPoint` | struct | `None` | public | Information from a topological section to store in a vertex in the delaunay triangulation when it is created. |
| `Rift` | struct | `None` | public | Feature properties if this network is a rift. |
| `create( const double &reconstruction_time, const GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type &network_boundary_polygon, DelaunayPointIter delaunay_points_begin, DelaunayPointIter delaunay_points_end, RigidBlockIter rigid_blocks_begin, RigidBlockIter rigid_blocks_end, const TopologyNetworkParams &topology_ ...` | method | `non_null_ptr_type` | public | Creates a Network. |
| `get_boundary_polygon()` | method | `GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type` | public | Returns the polygon that bounds the network. |
| `get_boundary_polygon_with_rigid_block_holes()` | method | `GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type` | public | Returns the polygon that bounds the network with the rigid blocks (if any) as interior holes. |
| `is_point_in_network( const GPlatesMaths::PointOnSphere &point)` | method | `bool` | public | Returns true if the specified 3D point is inside the network boundary (PolygonOnSphere). |
| `is_point_in_network( const Point2Type &point_2)` | method | `bool` | public | Convenient overload for 2D projected point. |
| `is_point_in_deforming_region( const GPlatesMaths::PointOnSphere &point)` | method | `bool` | public | Returns true if the specified 3D point is inside the network boundary (PolygonOnSphere) but outside any interior rigid blocks (also PolygonOnSphere's). |
| `is_point_in_deforming_region( const Point2Type &point_2)` | method | `bool` | public | Convenient overload for 2D projected point. |
| `is_point_in_a_rigid_block( const GPlatesMaths::PointOnSphere &point)` | method | `boost::optional<const RigidBlock &>` | public | Returns true if the specified 3D point is inside any interior rigid blocks (PolygonOnSphere's). |
| `is_point_in_a_rigid_block( const Point2Type &point_2)` | method | `boost::optional<const RigidBlock &>` | public | Convenient overload for 2D projected point. |
| `get_point_location( const GPlatesMaths::PointOnSphere &point)` | method | `boost::optional<PointLocation>` | public | Returns the location of the specified 3D point within network (either inside a delaunay face or a rigid block). |
| `get_point_location( const Point2Type &point_2)` | method | `boost::optional<PointLocation>` | public | Convenient overload for 2D projected point. |
| `calc_delaunay_natural_neighbor_coordinates( delaunay_natural_neighbor_coordinates_2_type &natural_neighbor_coordinates, const GPlatesMaths::PointOnSphere &point, Delaunay_2::Face_handle start_face_hint = Delaunay_2::Face_handle())` | method | `bool` | public | Returns the natural neighbor coordinates of point in the \*delaunay\* triangulation (which can then be used with different interpolation methods like linear interpolation). start\_face\_hint is an optional optimisation if you already know the ... |
| `calc_delaunay_natural_neighbor_coordinates( delaunay_natural_neighbor_coordinates_2_type &natural_neighbor_coordinates, const Point2Type &point_2, Delaunay_2::Face_handle start_face_hint = Delaunay_2::Face_handle())` | method | `bool` | public | Convenient overload for 2D projected point. |
| `calc_delaunay_barycentric_coordinates( delaunay_coord_2_type &barycentric_coord_vertex_1, delaunay_coord_2_type &barycentric_coord_vertex_2, delaunay_coord_2_type &barycentric_coord_vertex_3, const GPlatesMaths::PointOnSphere &point, Delaunay_2::Face_handle start_face_hint = Delaunay_2::Face_handle())` | method | `boost::optional<Delaunay_2::Face_handle>` | public | Returns the barycentric coordinates of point in the delaunay triangulation along with the face containing point. start\_face\_hint is an optional optimisation if you already know the delaunay face containing the point (or near the point). |
| `calc_delaunay_barycentric_coordinates( delaunay_coord_2_type &barycentric_coord_vertex_1, delaunay_coord_2_type &barycentric_coord_vertex_2, delaunay_coord_2_type &barycentric_coord_vertex_3, const Point2Type &point_2, Delaunay_2::Face_handle start_face_hint = Delaunay_2::Face_handle())` | method | `boost::optional<Delaunay_2::Face_handle>` | public | Convenient overload for 2D projected point. |
| `get_strain_rate_smoothing()` | method | `TopologyNetworkParams::StrainRateSmoothing` | public | Returns whether deformation strain rates are smoothed and how. |
| `get_strain_rate_clamping()` | method | `TopologyNetworkParams::StrainRateClamping` | public | Returns whether deformation strain rates are clamped (and, if so, by how much). |
| `calculate_deformation( const GPlatesMaths::PointOnSphere &point, boost::optional<PointLocation> point_location = boost::none)` | method | `boost::optional<DeformationInfo>` | public | Calculates the deformation at point in the network interpolated using natural neighbour coordinates (if get\_strain\_rate\_smoothing returns NATURAL\_NEIGHBOUR\_SMOOTHING), or barycentric coordinates (if BARYCENTRIC\_SMOOTHING), or using the ... |
| `calculate_deformation( const Point2Type &point_2, boost::optional<PointLocation> point_location = boost::none)` | method | `boost::optional<DeformationInfo>` | public | Convenient overload for 2D projected point. |
| `calculate_deformation_in_deforming_region( const GPlatesMaths::PointOnSphere &point, Delaunay_2::Face_handle start_face_hint = Delaunay_2::Face_handle())` | method | `DeformationInfo` | public | Same as calculate\_deformation except assumes point is inside the deforming region (ie, does not check if point is outside the network or inside a rigid block). |
| `calculate_deformation_in_deforming_region( const Point2Type &point_2, Delaunay_2::Face_handle start_face_hint = Delaunay_2::Face_handle())` | method | `DeformationInfo` | public | Overload for 2D projected point. |
| `calculate_deformation_in_deforming_region( const Delaunay_2::Point &point_2, Delaunay_2::Face_handle start_face_hint)` | method | `DeformationInfo` | public | Overload for 2D projected point of type 'Delaunay\_2::Point'. |
| `calculate_deformed_point( const GPlatesMaths::PointOnSphere &point, const double &time_increment = 1.0, bool reverse_deform = false, bool use_natural_neighbour_interpolation = true, boost::optional<PointLocation> point_location = boost::none)` | method | `boost::optional< std::pair<GPlatesMaths::PointOnSphere, PointLocation> >` | public | Calculates the position that point deforms to. |
| `calculate_deformed_point( const Point2Type &point_2, const double &time_increment = 1.0, bool reverse_deform = false, bool use_natural_neighbour_interpolation = true, boost::optional<PointLocation> point_location = boost::none)` | method | `boost::optional< std::pair<GPlatesMaths::PointOnSphere, PointLocation> >` | public | Convenient overload for 2D projected point. |
| `calculate_stage_rotation( const GPlatesMaths::PointOnSphere &point, const double &velocity_delta_time = 1.0, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_DELTA_T_TO_T, boost::optional<PointLocation> point_location = boost::none)` | method | `boost::optional< std::pair<GPlatesMaths::FiniteRotation, PointLocation> >` | public | Calculates the stage rotation at point in the network interpolated using barycentric coordinates. |
| `calculate_stage_rotation( const Point2Type &point_2, const double &velocity_delta_time = 1.0, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_DELTA_T_TO_T, boost::optional<PointLocation> point_location = boost::none)` | method | `boost::optional< std::pair<GPlatesMaths::FiniteRotation, PointLocation> >` | public | Convenient overload for 2D projected point. |
| `calculate_velocity( const GPlatesMaths::PointOnSphere &point, const double &velocity_delta_time = 1.0, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_DELTA_T_TO_T, boost::optional<PointLocation> point_location = boost::none)` | method | `boost::optional< std::pair<GPlatesMaths::Vector3D, PointLocation> >` | public | Calculates the velocity at point in the network interpolated using natural neighbour coordinates. |
| `calculate_velocity( const Point2Type &point_2, const double &velocity_delta_time = 1.0, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_DELTA_T_TO_T, boost::optional<PointLocation> point_location = boost::none)` | method | `boost::optional< std::pair<GPlatesMaths::Vector3D, PointLocation> >` | public | Convenient overload for 2D projected point. |
| `get_delaunay_2` | field | `Delaunay_2` | public | Gets, or creates, 2D delaunay triangulation. |
| `BuildInfo` | struct | `None` | private | Information used to build the internal triangulations. |
| `delaunay_point_2_to_vertex_handle_map_type` | typedef | `std::map<delaunay_point_2_type, Delaunay_2::Vertex_handle, delaunay_kernel_2_type::Less_xy_2>` | private | Typedef for a mapping of 2D delaunay triangulation points to delaunay vertex handles. |
| `UncachedDataAccess` | class | `None` | private | Functor class for accessing function values at delaunay vertices. |
| `CachedDataAccess` | class | `None` | private | Functor class for accessing, and caching, function values at delaunay vertices. |
| `velocity_delta_time_params_type` | typedef | `std::pair<GPlatesMaths::Real, VelocityDeltaTime::Type>` | private | Typedef for velocity delta-time parameters. |
| `DelaunayVertexHandleToVelocityMapType` | struct | `None` | private | Typedef for a mapping of 2D delaunay triangulation vertex handles to velocities. |
| `velocity_delta_time_to_velocity_map_type` | typedef | `GPlatesUtils::KeyValueCache<velocity_delta_time_params_type, DelaunayVertexHandleToVelocityMapType>` | private | Typedef for a mapping of velocity delta-time parameter to 2D delaunay triangulation vertices-to-velocities maps. |
| `DelaunayVertexHandleToStageRotationMapType` | struct | `None` | private | Typedef for a mapping of 2D delaunay triangulation vertex handles to stage rotations. |
| `velocity_delta_time_to_stage_rotation_map_type` | typedef | `GPlatesUtils::KeyValueCache<velocity_delta_time_params_type, DelaunayVertexHandleToStageRotationMapType>` | private | Typedef for a mapping of velocity delta-time parameter to 2D delaunay triangulation vertices-to-stage-rotations maps. |
| `DelaunayVertexHandleToDeformedPointMapType` | struct | `None` | private | Typedef for a mapping of 2D delaunay triangulation vertex handles to deformed 2D positions. |
| `deformed_point_params_type` | typedef | `std::pair<bool/*reverse_deform*/, velocity_delta_time_params_type>` | private | Typedef for deformed position parameters. |
| `velocity_delta_time_to_deformed_point_map_type` | typedef | `GPlatesUtils::KeyValueCache<deformed_point_params_type, DelaunayVertexHandleToDeformedPointMapType>` | private | Typedef for a mapping of deformed position parameters to 2D delaunay triangulation vertices-to-deformed-positions maps. |
| `d_reconstruction_time` | field | `double` | private | The reconstruction time this triangulation network was build at. |
| `d_network_boundary_polygon` | field | `GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type` | private | The polygon that bounds the network. |
| `d_network_boundary_polygon_with_rigid_block_holes` | field | `boost::optional<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | private | The polygon that bounds the network with rigid blocks (if any) as interior holes. |
| `d_rigid_blocks` | field | `rigid_block_seq_type` | private | The rigid blocks inside the network. |
| `d_projection` | field | `GPlatesMaths::AzimuthalEqualAreaProjection` | private | Used to project from 3D to 2D (for 2D triangulation). |
| `d_build_info` | field | `BuildInfo` | private | Information used to build the internal triangulation (building delayed in case not needed). |
| `d_delaunay_2` | field | `boost::optional<Delaunay_2>` | private | 2D delaunay triangulation is only built if it's needed. |
| `d_delaunay_point_2_to_vertex_handle_map` | field | `boost::optional<delaunay_point_2_to_vertex_handle_map_type>` | private | Maps delaunay vertex points to vertex handles. |
| `d_velocity_delta_time_to_velocity_map` | field | `velocity_delta_time_to_velocity_map_type` | private | Maps velocity delta-time parameters to velocity maps. |
| `d_velocity_delta_time_to_stage_rotation_map` | field | `velocity_delta_time_to_stage_rotation_map_type` | private | Maps velocity delta-time parameters to stage rotation maps. |
| `d_velocity_delta_time_to_deformed_point_map` | field | `velocity_delta_time_to_deformed_point_map_type` | private | Maps velocity delta-time parameters to deformed position maps. |
| `Network( const double &reconstruction_time, const GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type &network_boundary_polygon, DelaunayPointIter delaunay_points_begin, DelaunayPointIter delaunay_points_end, RigidBlockIter rigid_blocks_begin_, RigidBlockIter rigid_blocks_end_, const TopologyNetworkParams &topolo ...` | constructor | `None` | private | — |
| `create_delaunay_2()` | method | `void` | private | — |
| `refine_rift_delaunay_2( const BuildInfo::RiftParams &rift_params, unsigned int vertex_index)` | method | `void` | private | — |
| `refine_rift_delaunay_edge( std::vector<DelaunayPoint> &delaunay_edge_point_seq, const GPlatesMaths::PointOnSphere &first_subdivided_edge_vertex_point, const GPlatesMaths::PointOnSphere &second_subdivided_edge_vertex_point, const GPlatesMaths::real_t &first_subdivided_edge_vertex_interpolation, const GPlatesMaths::real_ ...` | method | `void` | private | — |
| `get_delaunay_point_2_to_vertex_handle_map` | field | `delaunay_point_2_to_vertex_handle_map_type` | private | — |
| `create_delaunay_point_2_to_vertex_handle_map( delaunay_point_2_to_vertex_handle_map_type &delaunay_point_2_to_vertex_handle_map)` | method | `void` | private | — |
| `calc_delaunay_natural_neighbor_coordinates_in_deforming_region( delaunay_natural_neighbor_coordinates_2_type &natural_neighbor_coordinates, const delaunay_point_2_type &point_2, Delaunay_2::Face_handle start_face_hint = Delaunay_2::Face_handle())` | method | `void` | private | Calculate the natural neighbour coordinates of the specified point. start\_face\_hint is an optional optimisation if you already know the delaunay face containing the point. |
| `calc_delaunay_barycentric_coordinates_in_deforming_region( delaunay_coord_2_type &barycentric_coord_vertex_1, delaunay_coord_2_type &barycentric_coord_vertex_2, delaunay_coord_2_type &barycentric_coord_vertex_3, const delaunay_point_2_type &point_2, Delaunay_2::Face_handle start_face_hint = Delaunay_2::Face_handle())` | method | `Delaunay_2::Face_handle` | private | Calculate the barycentric coordinates of the specified point and return the face containing the point. start\_face\_hint is an optional optimisation if you already know the delaunay face containing the point. |
| `get_delaunay_face_in_deforming_region( const delaunay_point_2_type &point_2, Delaunay_2::Face_handle start_face_hint = Delaunay_2::Face_handle())` | method | `Delaunay_2::Face_handle` | private | Find the delaunay face containing the specified point. start\_face\_hint is an optional optimisation if you already know the delaunay face containing the point. |
| `get_closest_delaunay_convex_hull_edge( const delaunay_point_2_type &point_2)` | method | `std::pair< Delaunay_2::Vertex_handle/*closest vertex*/, boost::optional<Delaunay_2::Vertex_handle>/*end vertex of closest edge*/ >` | private | Find the delaunay convex hull edge that is closest to the specified point (where one of the edge end points is also the closest triangulation vertex to the specified point). |
| `is_point_in_rigid_block( const GPlatesMaths::PointOnSphere &point, const RigidBlock &rigid_block)` | method | `bool` | private | Returns true if point is inside rigid\_block. |
| `calculate_rigid_block_stage_rotation( const RigidBlock &rigid_block, const double &velocity_delta_time, VelocityDeltaTime::Type velocity_delta_time_type)` | method | `GPlatesMaths::FiniteRotation` | private | Returns the stage rotation for the specified rigid block. |
| `calculate_rigid_block_velocity( const GPlatesMaths::PointOnSphere &point, const RigidBlock &rigid_block, const double &velocity_delta_time, VelocityDeltaTime::Type velocity_delta_time_type)` | method | `GPlatesMaths::Vector3D` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `copysign` | macro | `_copysign` | — |
| `VELOCITY_DELTA_TIME` | variable | `double` | — |
| `INV_VELOCITY_DELTA_TIME` | variable | `double` | — |
| `SCALE_PER_MY_TO_PER_SECOND` | variable | `double` | Scale 1/my -\> 1/s. |
| `calc_delaunay_vertex_velocity( const ResolvedTriangulation::Delaunay_2::Vertex_handle &vertex_handle, const double &velocity_delta_time, VelocityDeltaTime::Type velocity_delta_time_type)` | function | `GPlatesMaths::Vector3D` | Calculate the velocity at a delaunay vertex. |
| `calc_delaunay_vertex_deformation( const ResolvedTriangulation::Delaunay_2::Vertex_handle &vertex_handle)` | function | `ResolvedTriangulation::DeformationInfo` | Calculate the deformation at a delaunay vertex. |
| `calc_delaunay_vertex_deformed_point( const ResolvedTriangulation::Delaunay_2::Vertex_handle &vertex_handle, const double &time_increment, bool reverse_deform, VelocityDeltaTime::Type velocity_delta_time_type, const GPlatesMaths::AzimuthalEqualAreaProjection &projection)` | function | `QPointF` | Calculate the deformed position of a delaunay vertex. |
| `GPLATES_APP_LOGIC_RESOLVEDTRIANGULATIONNETWORK_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ResolvedTriangulationNetwork tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 22 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 16 |
| [app-logic/GeometryCookieCutter](GeometryCookieCutter.md) | app-logic | 14 |
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 14 |
| [app-logic/TopologyPointLocation](TopologyPointLocation.md) | app-logic | 11 |
| [app-logic/ResolvedTriangulationDelaunay2](ResolvedTriangulationDelaunay2.md) | app-logic | 9 |
| [app-logic/PlateVelocityUtils](PlateVelocityUtils.md) | app-logic | 8 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 8 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 5 |
| [app-logic/ResolvedTopologicalNetwork](ResolvedTopologicalNetwork.md) | app-logic | 4 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 3 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 2 |
| [presentation/LayerOutputRenderer](../presentation/LayerOutputRenderer.md) | presentation | 2 |
| [app-logic/ReconstructMethodByPlateId](ReconstructMethodByPlateId.md) | app-logic | 1 |
| [app-logic/VgpPartitionFeatureTask](VgpPartitionFeatureTask.md) | app-logic | 1 |
| [maths/PolygonMesh](../maths/PolygonMesh.md) | maths | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ResolvedTriangulationNetwork.h
python scripts/gpq.py def GPlatesAppLogic::ResolvedTriangulation::Network --body
python scripts/gpq.py uses Network --kind class
python scripts/gpq.py hier Network
```

# ResolvedTriangulationDelaunay2

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 29 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ResolvedTriangulationDelaunay2.h` | C++ | 1052 |
| `src/app-logic/ResolvedTriangulationDelaunay2.cc` | C++ | 446 |

## Overview

[[[PROSE overview unit=app-logic/ResolvedTriangulationDelaunay2 tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ResolvedTriangulation::DeformationInfo`](#gplatesapplogicresolvedtriangulationdeformationinfo) | class | — | — | 0 | Deformation information containing the strain rate of a triangle in triangulation or smoothed strain rate at a point over nearby triangles. |
| [`GPlatesAppLogic::ResolvedTriangulation::delaunay_kernel_2_type`](#gplatesapplogicresolvedtriangulationdelaunay_kernel_2_type) | typedef | — | — | 0 | Basic CGAL typedefs for 2D delaunay triangulation. |
| [`GPlatesAppLogic::ResolvedTriangulation::delaunay_coord_2_type`](#gplatesapplogicresolvedtriangulationdelaunay_coord_2_type) | typedef | — | — | 0 | — |
| [`GPlatesAppLogic::ResolvedTriangulation::delaunay_point_2_type`](#gplatesapplogicresolvedtriangulationdelaunay_point_2_type) | typedef | — | — | 0 | — |
| [`GPlatesAppLogic::ResolvedTriangulation::delaunay_vector_2_type`](#gplatesapplogicresolvedtriangulationdelaunay_vector_2_type) | typedef | — | — | 0 | — |
| [`GPlatesAppLogic::ResolvedTriangulation::delaunay_point_coordinate_vector_2_type`](#gplatesapplogicresolvedtriangulationdelaunay_point_coordinate_vector_2_type) | typedef | — | — | 0 | — |
| [`GPlatesAppLogic::ResolvedTriangulation::delaunay_map_point_to_value_2_type`](#gplatesapplogicresolvedtriangulationdelaunay_map_point_to_value_2_type) | typedef | — | — | 0 | Typedefs for interpolations in 2D |
| [`GPlatesAppLogic::ResolvedTriangulation::delaunay_natural_neighbor_coordinates_2_type`](#gplatesapplogicresolvedtriangulationdelaunay_natural_neighbor_coordinates_2_type) | typedef | — | — | 0 | Typedef for result of a natural neighbours query on a 2D triangulation. |
| [`GPlatesAppLogic::ResolvedTriangulation::DelaunayVertex_2`](#gplatesapplogicresolvedtriangulationdelaunayvertex_2) | class | `Vb` | `< typename GT, typename Vb = CGAL::Triangulation_vertex_base_2<GT> >` | 0 | This class holds the extra info for each delaunay triangulation vertex. |
| [`GPlatesAppLogic::ResolvedTriangulation::DelaunayFace_2`](#gplatesapplogicresolvedtriangulationdelaunayface_2) | class | `Fb` | `< typename GT, typename Fb = CGAL::Triangulation_face_base_2<GT> >` | 0 | This class holds the extra info for each delaunay triangulation face. |
| [`GPlatesAppLogic::ResolvedTriangulation::delaunay_triangulation_vertex_2_type`](#gplatesapplogicresolvedtriangulationdelaunay_triangulation_vertex_2_type) | struct | `CGAL::Triangulation_hierarchy_vertex_base_2< DelaunayVertex_2<delaunay_kernel_2_type> >` | — | 0 | Vertex type with extra vertex info for delaunay triangulation. |
| [`GPlatesAppLogic::ResolvedTriangulation::delaunay_triangulation_face_2_type`](#gplatesapplogicresolvedtriangulationdelaunay_triangulation_face_2_type) | typedef | — | — | 0 | Face type with extra face info for delaunay triangulation. |
| [`GPlatesAppLogic::ResolvedTriangulation::delaunay_triangulation_data_structure_2_type`](#gplatesapplogicresolvedtriangulationdelaunay_triangulation_data_structure_2_type) | typedef | — | — | 0 | 2D Triangle data structure, with extra info for each vertex and face |
| [`GPlatesAppLogic::ResolvedTriangulation::Delaunay_2`](#gplatesapplogicresolvedtriangulationdelaunay_2) | class | `CGAL::Triangulation_hierarchy_2< CGAL::Delaunay_triangulation_2< delaunay_kernel_2_type, delaunay_triangulation_data_structure_2_type> >` | — | 0 | 2D Delaunay triangulation. |

## Members

### `GPlatesAppLogic::ResolvedTriangulation::DeformationInfo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DeformationInfo()` | constructor | `None` | public | Zero strain rates (non-deforming). |
| `DeformationInfo( const DeformationStrainRate &strain_rate)` | constructor | `None` | public | — |
| `d_strain_rate` | field | `DeformationStrainRate` | private | — |

### `GPlatesAppLogic::ResolvedTriangulation::delaunay_kernel_2_type`

*None.*

### `GPlatesAppLogic::ResolvedTriangulation::delaunay_coord_2_type`

*None.*

### `GPlatesAppLogic::ResolvedTriangulation::delaunay_point_2_type`

*None.*

### `GPlatesAppLogic::ResolvedTriangulation::delaunay_vector_2_type`

*None.*

### `GPlatesAppLogic::ResolvedTriangulation::delaunay_point_coordinate_vector_2_type`

*None.*

### `GPlatesAppLogic::ResolvedTriangulation::delaunay_map_point_to_value_2_type`

*None.*

### `GPlatesAppLogic::ResolvedTriangulation::delaunay_natural_neighbor_coordinates_2_type`

*None.*

### `GPlatesAppLogic::ResolvedTriangulation::DelaunayVertex_2`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Face_handle` | typedef | `typename Vb::Face_handle` | public | — |
| `Vertex_handle` | typedef | `typename Vb::Vertex_handle` | public | — |
| `Point` | typedef | `typename Vb::Point` | public | — |
| `Rebind_TDS` | struct | `None` | public | — |
| `DelaunayVertex_2()` | constructor | `None` | public | — |
| `DelaunayVertex_2( const Point &p)` | constructor | `None` | public | — |
| `DelaunayVertex_2( const Point &p, Face_handle c)` | constructor | `None` | public | — |
| `DelaunayVertex_2( Face_handle c)` | constructor | `None` | public | — |
| `is_initialised()` | method | `bool` | public | Returns true if initialise has been called. |
| `initialise( const Delaunay_2 &delaunay_2, unsigned int vertex_index, const GPlatesMaths::PointOnSphere &point_on_sphere, const GPlatesMaths::LatLonPoint &lat_lon_point, const ResolvedVertexSourceInfo::non_null_ptr_to_const_type &shared_source_info)` | method | `void` | public | Set all essential vertex information in one go. |
| `get_vertex_index()` | method | `unsigned int` | public | Returns index of this vertex within all vertices in the delaunay triangulation. |
| `calc_stage_rotation( const double &velocity_delta_time = 1.0, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_DELTA_T_TO_T)` | method | `GPlatesMaths::FiniteRotation` | public | Calculates the stage rotation of this vertex. |
| `calc_velocity_vector( const double &velocity_delta_time = 1.0, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_DELTA_T_TO_T)` | method | `GPlatesMaths::Vector3D` | public | Calculates the velocity vector of this vertex. |
| `calc_velocity_colat_lon( const double &velocity_delta_time = 1.0, VelocityDeltaTime::Type velocity_delta_time_type = VelocityDeltaTime::T_PLUS_DELTA_T_TO_T)` | method | `GPlatesMaths::VectorColatitudeLongitude` | public | Calculates the velocity colat/lon of this vertex. |
| `VertexInfo` | struct | `None` | private | All information passed into initialise goes here. |
| `d_vertex_info` | field | `boost::optional<VertexInfo>` | private | — |
| `d_deformation_info` | field | `boost::optional<DeformationInfo>` | private | Derived values - these are mutable since they are calculated on first call. |
| `calculate_deformation_info()` | method | `DeformationInfo` | private | Compute the deformation info for this vertex. |
| `get_handle()` | method | `Vertex_handle` | private | — |

### `GPlatesAppLogic::ResolvedTriangulation::DelaunayFace_2`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Vertex_handle` | typedef | `typename Fb::Vertex_handle` | public | — |
| `Face_handle` | typedef | `typename Fb::Face_handle` | public | — |
| `Rebind_TDS` | struct | `None` | public | — |
| `DelaunayFace_2()` | constructor | `None` | public | — |
| `DelaunayFace_2( Vertex_handle v0, Vertex_handle v1, Vertex_handle v2)` | constructor | `None` | public | — |
| `DelaunayFace_2( Vertex_handle v0, Vertex_handle v1, Vertex_handle v2, Face_handle n0, Face_handle n1, Face_handle n2)` | constructor | `None` | public | — |
| `is_in_deforming_region()` | method | `bool` | public | Returns true if face is inside the deforming region. |
| `CheckFaceVertices` | struct | `None` | private | Information to determine whether this face has been modified when the Delaunay triangulation is modified. |
| `d_check_face_vertices` | field | `CheckFaceVertices` | private | — |
| `d_delaunay_2` | field | `boost::optional<const Delaunay_2 &>` | private | Delaunay triangulation containing this face. |
| `d_is_in_deforming_region` | field | `boost::optional<bool>` | private | Whether this face is inside the deforming region. |
| `d_deformation_info` | field | `boost::optional<DeformationInfo>` | private | Derived values - these are mutable since they are calculated on first call. |
| `check_face_vertices()` | method | `void` | private | Reset any cached information for this face (except reference to Delaunay triangulation) if any vertices of this face have changed (when the Delaunay triangulation is modified). |
| `calculate_is_in_deforming_region()` | method | `bool` | private | — |
| `calculate_deformation_info()` | method | `DeformationInfo` | private | Compute the deformation info for this face. |

### `GPlatesAppLogic::ResolvedTriangulation::delaunay_triangulation_vertex_2_type`

*None.*

### `GPlatesAppLogic::ResolvedTriangulation::delaunay_triangulation_face_2_type`

*None.*

### `GPlatesAppLogic::ResolvedTriangulation::delaunay_triangulation_data_structure_2_type`

*None.*

### `GPlatesAppLogic::ResolvedTriangulation::Delaunay_2`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Delaunay_2( const Network &network, const double &reconstruction_time)` | constructor | `None` | public | — |
| `calc_natural_neighbor_coordinates( delaunay_natural_neighbor_coordinates_2_type &natural_neighbor_coordinates, const delaunay_point_2_type &point, Face_handle start_face_hint = Face_handle())` | method | `bool` | public | Returns the natural neighbor coordinates of point in the triangulation (which can then be used with different interpolation methods like linear interpolation). |
| `calc_barycentric_coordinates( delaunay_coord_2_type &barycentric_coord_vertex_1, delaunay_coord_2_type &barycentric_coord_vertex_2, delaunay_coord_2_type &barycentric_coord_vertex_3, const delaunay_point_2_type &point, Face_handle start_face_hint = Face_handle())` | method | `boost::optional<Face_handle>` | public | Returns the barycentric coordinates of point in the triangulation along with the face containing point. |
| `get_face_containing_point( const delaunay_point_2_type &point, Face_handle start_face_hint = Face_handle())` | method | `boost::optional<Face_handle>` | public | Returns the face containing point. |
| `gradient_2( const delaunay_point_2_type &point, const delaunay_map_point_to_value_2_type &function_values)` | method | `delaunay_vector_2_type` | public | Returns the gradient vector at the specified point. |
| `get_projection` | field | `GPlatesMaths::AzimuthalEqualAreaProjection` | public | Returns the projection used by this triangulation to convert from 3D points to 2D points and vice versa. |
| `get_clamp_total_strain_rate()` | method | `boost::optional<double>` | public | Returns the optional maximum total strain rate (2nd invariant). |
| `is_point_in_deforming_region( const GPlatesMaths::PointOnSphere &point)` | method | `bool` | public | Delegates to the Network that owns this Delaunay triangulation. |
| `d_network` | field | `Network` | private | The Network that owns this Delaunay triangulation. |
| `d_reconstruction_time` | field | `double` | private | — |
| `d_clamp_total_strain_rate` | field | `boost::optional<double>` | private | — |
| `set_finished_modifying_triangulation()` | method | `void` | public | — |
| `is_finished_modifying_triangulation()` | method | `bool` | public | — |
| `d_finished_modifying_triangulation` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `CGAL_DT2_USE_RECURSIVE_PROPAGATE_CONFLICTS` | macro | `None` | — |
| `EARTH_RADIUS_METRES` | variable | `double` | — |
| `INVERSE_EARTH_RADIUS_METRES` | variable | `double` | — |
| `GPLATES_APP_LOGIC_RESOLVEDTRIANGULATIONDELAUNAY2_H` | macro | `None` | — |
| `DISABLE_MSVC_WARNING` | variable | `PUSH_MSVC_WARNINGS` | PUSH\_GCC\_WARNINGS DISABLE\_GCC\_WARNING("-Wshadow") DISABLE\_GCC\_WARNING("-Wold-style-cast") DISABLE\_GCC\_WARNING("-Werror") |
| `calculate_face_deformation_info( const Delaunay_2 &delaunay_2, const double &theta1, const double &theta2, const double &theta3, const double &theta_centroid, const double &phi1, const double &phi2, const double &phi3, const double &phi_centroid, const double &utheta1, const double &utheta2, const double &utheta3, cons ...` | function | `DeformationInfo` | Put part of DelaunayFace\_2\<GT, Fb\>::calculate\_deformation\_info() in the '.cc' file to avoid lengthy recompile times each time it's modified. |

## Notes

[[[PROSE notes unit=app-logic/ResolvedTriangulationDelaunay2 tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ResolvedTriangulationNetwork](ResolvedTriangulationNetwork.md) | app-logic | 417 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 123 |
| [app-logic/TopologyPointLocation](TopologyPointLocation.md) | app-logic | 22 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 21 |
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 20 |
| [app-logic/ResolvedTopologicalNetwork](ResolvedTopologicalNetwork.md) | app-logic | 10 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 10 |
| [app-logic/PlateVelocityUtils](PlateVelocityUtils.md) | app-logic | 6 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 3 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 2 |
| [view-operations/AddPointGeometryOperation](../view-operations/AddPointGeometryOperation.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ResolvedTriangulationDelaunay2.h
python scripts/gpq.py def GPlatesAppLogic::ResolvedTriangulation::DelaunayVertex_2 --body
python scripts/gpq.py uses DelaunayVertex_2 --kind class
python scripts/gpq.py hier DelaunayVertex_2
```

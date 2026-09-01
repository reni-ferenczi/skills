# ResolvedTriangulationDelaunay2

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 29 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ResolvedTriangulationDelaunay2.h` | C++ | 1052 |
| `src/app-logic/ResolvedTriangulationDelaunay2.cc` | C++ | 446 |

## Overview

This is the geometric substrate of a deforming topological network: a CGAL 2D Delaunay triangulation of the network's points, built in the plane of an `AzimuthalEqualAreaProjection` centred on the network, and decorated with enough GPlates data at each vertex and face to compute deformation. `Network` (in `ResolvedTriangulationNetwork`) owns one `Delaunay_2` per resolved network per reconstruction time and is the only thing that constructs it; everything else — `TopologyReconstruct` advecting points through the deforming region, `PlateVelocityUtils`, `ReconstructionGeometryRenderer` colouring by strain rate — reads it.

The decoration is done through CGAL's rebind mechanism rather than `Triangulation_vertex_base_with_info_2`, so `DelaunayVertex_2` and `DelaunayFace_2` are real base classes that a `Vertex_handle` or `Face_handle` dereferences straight into. A vertex carries its index, its 3D `PointOnSphere` and `LatLonPoint` (the un-projected originals, so nothing has to round-trip through the projection), and a shared `ResolvedVertexSourceInfo` that knows how to produce the vertex's stage rotation and velocity — which is what makes a vertex's velocity, and therefore the whole strain-rate calculation, derivable from the triangulation alone. Note the vertices carry *velocities*, not strain: strain rate is a derived quantity computed from the velocity field.

That derivation is the substance of the file. A face's `DeformationInfo` is the constant velocity-gradient tensor across its triangle: the three vertex velocities in colatitude/longitude are differentiated using the analytic derivatives of the barycentric coordinates with respect to (theta, phi), then converted from a flat lat/lon gradient into the spherical velocity gradient tensor `L` (Malvern, appendix II) at the face centroid, and finally optionally clamped so the second invariant does not exceed the network's configured maximum. A vertex's `DeformationInfo` is then the face-area-weighted average of its incident faces, skipping the infinite face and any face outside the deforming region. The heavy half of the face calculation lives in `calculate_face_deformation_info()` in the `.cc` purely so that editing it does not retrigger the template recompile of everything that includes this header.

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

**The triangulation is the convex hull of the network's points, so it is bigger than the network.** Faces exist outside the network boundary and inside non-deforming interior rigid blocks. `DelaunayFace_2::is_in_deforming_region()` is the filter, and it classifies by *face centroid* only — the triangulation is not constrained, so a face may straddle a boundary or interior-block edge and still be classified wholly in or wholly out. The header flags this as a known limitation.

**Vertices must be initialised; faces must not be.** Every accessor on `DelaunayVertex_2` asserts `d_vertex_info` and throws `PreconditionViolationError` otherwise, and `Network` initialises each vertex as it inserts it. Faces deliberately have no initialisation step, because incremental refinement creates faces the inserting code never sees; a face recovers the triangulation from `vertex(0)` on demand. If you add a code path that inserts vertices, it must call `initialise()` on each one. Initialising the same vertex twice is allowed and intended (a coincident insertion) — the last call wins.

**Face caches self-invalidate; vertex caches do not.** `DelaunayFace_2` fingerprints its three vertex indices (`CheckFaceVertices`) and drops its cached deforming-region flag and `DeformationInfo` whenever they change, which is how it survives a vertex insertion that rewrites an existing face in place. `DelaunayVertex_2` has no such mechanism, so `calculate_deformation_info()` asserts `Delaunay_2::is_finished_modifying_triangulation()` — computed before `Network` calls `set_finished_modifying_triangulation()`, a vertex would cache an average over an intermediate triangulation. If you touch vertex strain rates, respect that gate. Note also the fingerprint's default is `{0,0,0}`, which is a real vertex index triple; it relies on no actual face having exactly those three indices.

**Inexact kernel, with a documented failure mode.** The triangulation uses `Exact_predicates_inexact_constructions_kernel`. `calc_natural_neighbor_coordinates()` therefore checks for a zero normalisation factor from CGAL and silently falls back to barycentric coordinates of the containing face, returning those as three "natural neighbour" coordinates with norm 1. Callers get a usable answer, but it is not the Sibson result; do not treat the coordinate count as meaningful.

**CGAL version workaround.** The `.cc` defines `CGAL_DT2_USE_RECURSIVE_PROPAGATE_CONFLICTS` for CGAL below 4.12.2 and for 4.13.0, to dodge an infinite loop in `Delaunay_triangulation_2.h`. It buys that at the cost of unbounded recursion depth in conflict propagation. The define must appear before any direct or indirect include of that CGAL header, including in the app-logic precompiled header — moving includes around in this file can silently disable it.

**Units are not uniform and are converted mid-calculation.** `ResolvedVertexSourceInfo` yields velocities in cm/yr; `calculate_deformation_info()` scales them to m/s (divide by 3.1536e9) and converts degrees to radians before handing off. Strain rates are therefore in 1/s. Two divide-by-zero guards return a zero `DeformationInfo` rather than failing: a degenerate triangle (`b0` near zero) and a face centroid at a pole (`sin(theta)` near zero).

**Point location.** `Delaunay_2` derives from `CGAL::Triangulation_hierarchy_2`, so `locate()` is fast, but the `start_face_hint` parameter on the query methods still matters when walking a sequence of nearby points — that is the intended use. `get_face_containing_point()` accepts `FACE`, `EDGE` and `VERTEX` locate results and rejects everything else as outside the hull.

**Lifetime.** `Delaunay_2` holds a bare `const Network &`, and each vertex holds a bare `const Delaunay_2 &` inside its `VertexInfo`; the network must outlive the triangulation, which must outlive any handle you keep. All the lazy caches are `mutable` and unsynchronised, so a triangulation is not safe to query concurrently even through a `const` reference.

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

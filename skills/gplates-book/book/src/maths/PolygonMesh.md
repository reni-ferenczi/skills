# PolygonMesh

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 47 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/PolygonMesh.h` | C++ | 243 |
| `src/maths/PolygonMesh.cc` | C++ | 1315 |

## Overview

`PolygonMesh` triangulates the true interior fill region of a polygon (or of a polyline/multipoint coerced into one), unlike `PolygonFan` which produces a cheaper fan that can overlap itself or extend outside the interior on a concave polygon. `initialise` projects the polygon onto a tangent plane with a `GnomonicProjection` centred on the boundary centroid — chosen specifically because great circle arcs project to straight lines under a gnomonic projection, so tessellating the 2D triangulation's edges keeps the extra vertices on the original great circle arcs — then hands the projected exterior and interior rings to CGAL's `Constrained_Delaunay_triangulation_2` (`polygon_mesh_constrained_triangulation_type`) with `CGAL::Exact_predicates_tag`, which is what allows self-intersecting polygons to be triangulated at all, since it lets triangulation constraints cross each other.

The anonymous-namespace `PolygonMeshRefinement` then takes over from CGAL: it builds its own half-edge triangle mesh from the faces CGAL classified as inside the polygon (`initialise_face`) and repeatedly splits the longest edge, via a priority queue ordered by `EdgeLengthCompare`, until every edge is shorter than `mesh_refinement_threshold_radians` (floored at `MINIMUM_EDGE_LENGTH_THRESHOLD_RADIANS`, about 10 metres). This refinement is deliberately not delegated to CGAL's own mesh refiners — CGAL's exact-arithmetic kernels needed for that are much more expensive, so the file uses `CGAL::Exact_predicates_inexact_constructions_kernel` for the triangulation itself and refines separately with plain doubles. `PolygonMeshConstrainedDelaunayVertex_2`/`Face_2` extend CGAL's vertex/face base classes with the extra bookkeeping (`point3d`, `mesh_refinement_info`) that ties CGAL's 2D triangulation back to the mesh being built.

The public interface mirrors `PolygonFan`: the `create` overloads (from a `PolygonOnSphere`, `PolylineOnSphere`, `MultiPointOnSphere` or generic `GeometryOnSphere` via `CreatePolygonMeshFromGeometryOnSphere`) each return `boost::optional`, since meshing can fail — too few vertices, or CGAL/projection failure — and the resulting `Triangle`/`Vertex` arrays are consumed the same way as `PolygonFan`'s.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::PolygonMeshRefinementVertexInfo`](#gplatesmathspolygonmeshrefinementvertexinfo) | struct | — | — | 0 | Vertex info used by PolygonMeshRefinement. |
| [`GPlatesMaths::PolygonMeshConstrainedDelaunayVertex_2`](#gplatesmathspolygonmeshconstraineddelaunayvertex_2) | class | `Vb` | `< typename GT, typename Vb = CGAL::Triangulation_vertex_base_2<GT> >` | 0 | This class holds the extra info for each constrained delaunay triangulation vertex. |
| [`GPlatesMaths::PolygonMeshRefinementTriangleInfo`](#gplatesmathspolygonmeshrefinementtriangleinfo) | struct | — | — | 0 | Triangle info used by PolygonMeshRefinement. |
| [`GPlatesMaths::PolygonMeshConstrainedDelaunayFace_2`](#gplatesmathspolygonmeshconstraineddelaunayface_2) | class | `Fb` | `< typename GT, typename Fb = CGAL::Constrained_triangulation_face_base_2<GT> >` | 0 | This class holds the extra info for each constrained delaunay triangulation face. |
| [`GPlatesMaths::polygon_mesh_kernel_type`](#gplatesmathspolygon_mesh_kernel_type) | typedef | — | — | 0 | UPDATE: The following comment no longer applies because we no longer use CGAL for mesh refinement (we only use CGAL to create constrained delaunay triangulation) - we use our own mesh refinement based on edge splitting. |
| [`GPlatesMaths::polygon_mesh_vertex_type`](#gplatesmathspolygon_mesh_vertex_type) | typedef | — | — | 0 | — |
| [`GPlatesMaths::polygon_mesh_face_type`](#gplatesmathspolygon_mesh_face_type) | typedef | — | — | 0 | — |
| [`GPlatesMaths::polygon_mesh_triangulation_data_structure_type`](#gplatesmathspolygon_mesh_triangulation_data_structure_type) | typedef | — | — | 0 | — |
| [`GPlatesMaths::polygon_mesh_constrained_triangulation_type`](#gplatesmathspolygon_mesh_constrained_triangulation_type) | struct | `CGAL::Constrained_Delaunay_triangulation_2< polygon_mesh_kernel_type, polygon_mesh_triangulation_data_structure_type, CGAL::Exact_predicates_tag>` | — | 0 | NOTE: The CGAL::Exact\_predicates\_tag enables meshing of \*self-intersecting\* polygons since it enables triangulation constraints to intersect each other. |
| [`GPlatesMaths::polygon_mesh_polygon_ring_2_traits_type`](#gplatesmathspolygon_mesh_polygon_ring_2_traits_type) | typedef | — | — | 0 | — |
| [`GPlatesMaths::polygon_mesh_polygon_ring_2_point_type`](#gplatesmathspolygon_mesh_polygon_ring_2_point_type) | typedef | — | — | 0 | — |
| [`GPlatesMaths::polygon_mesh_polygon_ring_2_type`](#gplatesmathspolygon_mesh_polygon_ring_2_type) | typedef | — | — | 0 | — |
| [`GPlatesMaths::(anonymous)::CreatePolygonMeshFromGeometryOnSphere`](#gplatesmathsanonymouscreatepolygonmeshfromgeometryonsphere) | class | [`ConstGeometryOnSphereVisitor`](ConstGeometryOnSphereVisitor.md) | — | 0 | Creates a PolygonMesh from a GeometryOnSphere. |
| [`GPlatesMaths::(anonymous)::PolygonMeshRefinement`](#gplatesmathsanonymouspolygonmeshrefinement) | class | — | — | 0 | We do our own mesh refinement based on splitting edges that exceed a threshold length. |
| [`GPlatesMaths::PolygonMesh`](#gplatesmathspolygonmesh) | class | [`GPlatesUtils::ReferenceCount<PolygonMesh>`](../utils/ReferenceCount.md) | — | 0 | A triangular mesh of the interior region of a polygon. |

## Members

### `GPlatesMaths::PolygonMeshRefinementVertexInfo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PolygonMeshRefinementVertexInfo( unsigned int vertex_index_)` | constructor | `None` | public | — |
| `vertex_index` | field | `unsigned int` | public | — |

### `GPlatesMaths::PolygonMeshConstrainedDelaunayVertex_2`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Face_handle` | typedef | `typename Vb::Face_handle` | public | — |
| `Point` | typedef | `typename Vb::Point` | public | — |
| `Rebind_TDS` | struct | `None` | public | — |
| `PolygonMeshConstrainedDelaunayVertex_2()` | constructor | `None` | public | — |
| `PolygonMeshConstrainedDelaunayVertex_2( const Point &p)` | constructor | `None` | public | — |
| `PolygonMeshConstrainedDelaunayVertex_2( const Point &p, Face_handle c)` | constructor | `None` | public | — |
| `PolygonMeshConstrainedDelaunayVertex_2( Face_handle c)` | constructor | `None` | public | — |
| `point3d` | field | `boost::optional<UnitVector3D>` | public | The original 3D point on the globe. |
| `mesh_refinement_info` | field | `boost::optional<PolygonMeshRefinementVertexInfo>` | public | Vertex info used by PolygonMeshRefinement. |

### `GPlatesMaths::PolygonMeshRefinementTriangleInfo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `triangle_index` | field | `boost::optional<unsigned int>` | public | Index/reference to triangle associated with this face. |

### `GPlatesMaths::PolygonMeshConstrainedDelaunayFace_2`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Vertex_handle` | typedef | `typename Fb::Vertex_handle` | public | — |
| `Face_handle` | typedef | `typename Fb::Face_handle` | public | — |
| `Rebind_TDS` | struct | `None` | public | — |
| `PolygonMeshConstrainedDelaunayFace_2()` | constructor | `None` | public | — |
| `PolygonMeshConstrainedDelaunayFace_2( Vertex_handle v0, Vertex_handle v1, Vertex_handle v2)` | constructor | `None` | public | — |
| `PolygonMeshConstrainedDelaunayFace_2( Vertex_handle v0, Vertex_handle v1, Vertex_handle v2, Face_handle n0, Face_handle n1, Face_handle n2)` | constructor | `None` | public | — |
| `mesh_refinement_info` | field | `boost::optional<PolygonMeshRefinementTriangleInfo>` | public | Triangle info used by PolygonMeshRefinement. |

### `GPlatesMaths::polygon_mesh_kernel_type`

*None.*

### `GPlatesMaths::polygon_mesh_vertex_type`

*None.*

### `GPlatesMaths::polygon_mesh_face_type`

*None.*

### `GPlatesMaths::polygon_mesh_triangulation_data_structure_type`

*None.*

### `GPlatesMaths::polygon_mesh_constrained_triangulation_type`

*None.*

### `GPlatesMaths::polygon_mesh_polygon_ring_2_traits_type`

*None.*

### `GPlatesMaths::polygon_mesh_polygon_ring_2_point_type`

*None.*

### `GPlatesMaths::polygon_mesh_polygon_ring_2_type`

*None.*

### `GPlatesMaths::(anonymous)::CreatePolygonMeshFromGeometryOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CreatePolygonMeshFromGeometryOnSphere( const double &mesh_refinement_threshold_radians)` | constructor | `None` | public | — |
| `get_polygon_mesh()` | method | `boost::optional<PolygonMesh::non_null_ptr_to_const_type>` | public | Returns the optionally created PolygonMesh after visiting a GeometryOnSphere. |
| `visit_multi_point_on_sphere( MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | public | — |
| `visit_point_on_sphere( PointGeometryOnSphere::non_null_ptr_to_const_type /*point_on_sphere*/)` | method | `void` | public | — |
| `visit_polygon_on_sphere( PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | public | — |
| `visit_polyline_on_sphere( PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | public | — |
| `d_polygon_mesh` | field | `boost::optional<PolygonMesh::non_null_ptr_to_const_type>` | private | — |
| `d_mesh_refinement_threshold_radians` | field | `double` | private | — |

### `GPlatesMaths::(anonymous)::PolygonMeshRefinement`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Vertex` | struct | `None` | public | — |
| `Triangle` | struct | `None` | public | — |
| `Edge` | struct | `None` | public | — |
| `PolygonMeshRefinement( const PolygonOnSphere::non_null_ptr_to_const_type &polygon, const polygon_mesh_constrained_triangulation_type &cdt, const GnomonicProjection &gnomonic_projection)` | constructor | `None` | public | Construct a triangle mesh suitable for refinement from the constrained delaunay triangulation. |
| `refine_mesh( double edge_length_threshold_radians)` | method | `void` | public | Keep spitting edges in half until all edge lengths are below the specified angular threshold. |
| `get_polygon_mesh( std::vector<PolygonMesh::Triangle> &polygon_mesh_triangles, std::vector<PolygonMesh::Vertex> &polygon_mesh_vertices)` | method | `void` | public | Get the PolygonMesh triangles/vertices from the current mesh refinement. |
| `EdgeLengthCompare` | struct | `None` | private | Compares the lengths of two edges. |
| `MINIMUM_EDGE_LENGTH_THRESHOLD_RADIANS` | field | `double` | private | — |
| `d_vertex_pool` | field | `boost::object_pool<Vertex>` | private | — |
| `d_triangle_pool` | field | `boost::object_pool<Triangle>` | private | — |
| `d_edge_pool` | field | `boost::object_pool<Edge>` | private | — |
| `d_vertices` | field | `std::vector<Vertex *>` | private | — |
| `d_triangles` | field | `std::vector<Triangle *>` | private | — |
| `d_edges` | field | `std::vector<Edge *>` | private | — |
| `initialise_face( polygon_mesh_constrained_triangulation_type::Face_handle face_handle, const GnomonicProjection &gnomonic_projection, const PolygonOnSphere::non_null_ptr_to_const_type &polygon)` | method | `void` | private | Visit a face of the constrained delaunay triangulation and if it's inside the polygon then create a triangle (and associated vertices) for it, otherwise mark it as outside the polygon so we don't visit it again. |
| `split_edge( std::priority_queue<Edge *, std::vector<Edge *>, EdgeLengthCompare> &edges_to_refine, const AngularDistance &edge_length_threshold)` | method | `void` | private | Split the longest edge (which is at the front of the heap). |

### `GPlatesMaths::PolygonMesh`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<PolygonMesh>` | public | A convenience typedef for a shared pointer to a non-const PolygonMesh. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const PolygonMesh>` | public | A convenience typedef for a shared pointer to a const PolygonMesh. |
| `Triangle` | class | `None` | public | A mesh triangle. |
| `Vertex` | class | `None` | public | A mesh vertex. |
| `create( const PolygonOnSphere::non_null_ptr_to_const_type &polygon, const double &mesh_refinement_threshold_radians)` | method | `boost::optional<non_null_ptr_to_const_type>` | public | Creates a PolygonMesh object from a PolygonOnSphere. |
| `create( const PolylineOnSphere::non_null_ptr_to_const_type &polyline, const double &mesh_refinement_threshold_radians)` | method | `boost::optional<non_null_ptr_to_const_type>` | public | Creates a PolygonMesh object from a PolylineOnSphere. |
| `create( const MultiPointOnSphere::non_null_ptr_to_const_type &multi_point, const double &mesh_refinement_threshold_radians)` | method | `boost::optional<non_null_ptr_to_const_type>` | public | Creates a PolygonMesh object from a MultiPointOnSphere. |
| `create( const GeometryOnSphere::non_null_ptr_to_const_type &geometry_on_sphere, const double &mesh_refinement_threshold_radians)` | method | `boost::optional<non_null_ptr_to_const_type>` | public | Creates a PolygonMesh object from a GeometryOnSphere. |
| `d_triangles` | field | `std::vector<Triangle>` | private | The mesh triangles. |
| `d_vertices` | field | `std::vector<Vertex>` | private | The mesh vertices. |
| `PolygonMesh()` | constructor | `None` | private | Default constructor starts off with no triangles or vertices. |
| `initialise( const PolygonOnSphere::non_null_ptr_to_const_type &polygon, const double &mesh_refinement_threshold_radians)` | method | `bool` | private | Creates, and initialises, this polygon mesh using the specified polygon. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DISABLE_GCC_WARNING` | variable | `PUSH_GCC_WARNINGS` | — |
| `project_polygon_ring( polygon_mesh_polygon_ring_2_type &polygon_ring_2, const GnomonicProjection &gnomonic_projection, PolygonOnSphere::ring_vertex_const_iterator ring_vertex_begin, PolygonOnSphere::ring_vertex_const_iterator ring_vertex_end)` | function | `bool` | Project an exterior or interior ring of a polygon onto the specified projection plane. |
| `insert_polygon_ring_into_constrained_delaunay_triangulation( polygon_mesh_constrained_triangulation_type &cdt, std::map<polygon_mesh_constrained_triangulation_type::Vertex_handle, unsigned int/*vertex index*/> & cdt_unique_vertex_handles_map, std::vector<polygon_mesh_constrained_triangulation_type::Vertex_handle> &cdt_ ...` | function | `void` | Insert a polygon's exterior or interior ring into the constrained delaunay triangulation. |
| `create_constrained_delaunay_triangulation( polygon_mesh_constrained_triangulation_type &cdt, const PolygonOnSphere::non_null_ptr_to_const_type &polygon, const polygon_mesh_polygon_ring_2_type &exterior_ring_2, const std::vector<polygon_mesh_polygon_ring_2_type> &interior_rings_2)` | function | `bool` | Create a constrained delaunay triangulation from the specified polygon. |
| `MINIMUM_EDGE_LENGTH_THRESHOLD_RADIANS` | variable | `double` | Set the minimum edge length to 0.01km (10 metres). |
| `GPLATES_MATHS_POLYGONMESH_H` | macro | `None` | — |

## Notes

- `mesh_refinement_threshold_radians` is clamped to at least `MINIMUM_EDGE_LENGTH_THRESHOLD_RADIANS` (~10 metres on Earth's radius) and at most `PI`, so a caller cannot request unbounded refinement or a degenerate zero threshold.
- Meshing fails (returning `boost::none`) if any polygon vertex is too far from the boundary centroid to project under the gnomonic projection, in addition to the documented "too few vertices" failure — a very large or oddly shaped polygon can therefore fail to mesh even with enough vertices.
- Building the mesh is comparatively expensive (CGAL triangulation plus iterative edge splitting), which is why `PolygonFan` exists as a cheaper alternative when only an approximate, stencil-rendered fill is needed.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLReconstructedStaticPolygonMeshes](../opengl/GLReconstructedStaticPolygonMeshes.md) | opengl | 18 |
| [app-logic/ReconstructLayerProxy](../app-logic/ReconstructLayerProxy.md) | app-logic | 7 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 6 |
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/PolygonMesh.h
python scripts/gpq.py def GPlatesMaths::(anonymous)::PolygonMeshRefinement --body
python scripts/gpq.py uses PolygonMeshRefinement --kind class
python scripts/gpq.py hier PolygonMeshRefinement
```

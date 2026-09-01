# GeneratePoints

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 177 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/GeneratePoints.h` | C++ | 91 |
| `src/maths/GeneratePoints.cc` | C++ | 641 |

## Overview

`GeneratePoints` provides the three public entry points GPlates uses to scatter
points evenly across the globe, a lat/lon box, or a `PolygonOnSphere`. All
three delegate to the anonymous-namespace `UniformPointsBuilder`, which drives
a `SphericalSubdivision::RhombicTriacontahedronTraversal` down to
`point_density_level` levels of recursion and emits the quad vertices it
reaches. Starting from a Rhombic Triacontahedron (30 quad faces) rather than
the Hierarchical Triangular Mesh (8 triangular faces) gives a more uniform
point spacing; each recursion level halves the roughly-40-degree spacing of
level zero.

When a bounding polygon or lat/lon extent is supplied, `UniformPointsBuilder`
prunes whole subtrees early: it tests each quad against bounds contracted or
expanded by an angular distance threshold sized to the maximum possible random
offset at the current recursion depth, so a quad found entirely inside (or
outside) the tolerance skips per-child testing lower in the recursion, and
individual vertices are still bounds-checked at the leaf level to catch the
boundary case exactly. `d_visited_vertices` deduplicates vertices shared by
adjacent quads. If `point_random_offset` is non-zero, `RandomOffsetPointGenerator`
nudges each surviving vertex within a circle scaled by that fraction of the
local quad edge length, using two independent `RandomOffsetGenerator`
(Mersenne Twister) instances for radius and angle.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::(anonymous)::UniformPointsBuilder`](#gplatesmathsanonymousuniformpointsbuilder) | class | — | — | 0 | Used to recurse into a Rhombic Triacontahedron to generate points (optionally within a polygon, or lat/lon extent, bounding region). |

## Members

### `GPlatesMaths::(anonymous)::UniformPointsBuilder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RecursionContext` | struct | `None` | public | Keeps track of the recursion depth and whether we need to test child quads against the bounds (don't have to if parent quad is completely inside). |
| `UniformPointsBuilder( std::vector<PointOnSphere> &points, unsigned int recursion_depth_to_generate_points, const double &point_random_offset)` | constructor | `None` | public | — |
| `UniformPointsBuilder( std::vector<PointOnSphere> &points, unsigned int recursion_depth_to_generate_points, const double &point_random_offset, const PolygonOnSphere &polygon_bounds)` | constructor | `None` | public | — |
| `UniformPointsBuilder( std::vector<PointOnSphere> &points, unsigned int recursion_depth_to_generate_points, const double &point_random_offset, const double &top, const double &bottom, const double &left, const double &right)` | constructor | `None` | public | — |
| `visit( const SphericalSubdivision::RhombicTriacontahedronTraversal::Quad &quad, const RecursionContext &recursion_context)` | method | `void` | public | — |
| `LatLonExtent` | class | `None` | private | Lat/lon bounding box. |
| `RandomOffsetGenerator` | class | `None` | private | — |
| `RandomOffsetPointGenerator` | class | `None` | private | — |
| `visited_vertices_type` | typedef | `std::set<PointOnSphere, PointOnSphereMapPredicate>` | private | Typedef for seeing if we've already visited a vertex. |
| `bounds_type` | typedef | `boost::variant<LatLonExtent, PolygonOnSphere::non_null_ptr_to_const_type>` | private | — |
| `get_angular_distance_threshold( unsigned int recursion_depth_to_generate_points)` | method | `AngularExtent` | private | — |
| `create_lat_lon_extend_bounds( double top, double bottom, double left, double right, const AngularExtent &distance_threshold)` | method | `LatLonExtent` | private | — |
| `initialise_random_offset_point_generator( const double &point_random_offset)` | method | `void` | private | — |
| `d_points` | field | `std::vector<PointOnSphere>` | private | — |
| `d_recursion_depth_to_generate_points` | field | `unsigned int` | private | — |
| `d_distance_threshold` | field | `AngularExtent` | private | — |
| `d_random_offset_point_generator` | field | `boost::optional<RandomOffsetPointGenerator>` | private | — |
| `d_bounds` | field | `boost::optional<bounds_type>` | private | — |
| `d_visited_vertices` | field | `visited_vertices_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_GENERATEPOINTS_H` | macro | `None` | — |
| `create_global_uniform_points( std::vector<PointOnSphere> &points, unsigned int point_density_level, const double &point_random_offset)` | function | `void` | Generate a uniform distribution of points across the entire globe. |
| `create_uniform_points_in_lat_lon_extent( std::vector<PointOnSphere> &points, unsigned int point_density_level, const double &point_random_offset, const double &top, // Max lat. const double &bottom, // Min lat. const double &left, // Min lon. const double &right)` | function | `void` | Generate a uniform distribution of points within a latitude/longitude extent. top and bottom must be in range \[-90, 90\]. left and right must be in range \[-360, 360\]. |
| `create_uniform_points_in_polygon( std::vector<PointOnSphere> &points, unsigned int point_density_level, const double &point_random_offset, const PolygonOnSphere &polygon)` | function | `void` | Generate a uniform distribution of points inside the specified polygon. |

## Notes

`point_random_offset` must lie in `[0, 1]`; for `create_uniform_points_in_lat_lon_extent`,
`top`/`bottom` must lie in `[-90, 90]` and `left`/`right` in `[-360, 360]`.
Violating any of these raises `GPlatesGlobal::PreconditionViolationError`
via `GPlatesGlobal::Assert`, not a maths-specific exception. `top`/`bottom`
and `left`/`right` are silently swapped if passed in the wrong order.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 7 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/GeneratePoints.h
python scripts/gpq.py def GPlatesMaths::(anonymous)::UniformPointsBuilder --body
python scripts/gpq.py uses UniformPointsBuilder --kind class
python scripts/gpq.py hier UniformPointsBuilder
```

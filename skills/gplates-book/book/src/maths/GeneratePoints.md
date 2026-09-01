# GeneratePoints

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 177 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/GeneratePoints.h` | C++ | 91 |
| `src/maths/GeneratePoints.cc` | C++ | 641 |

## Overview

[[[PROSE overview unit=maths/GeneratePoints tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/GeneratePoints tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

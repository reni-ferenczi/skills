# ResolvedTriangulationUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 426 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ResolvedTriangulationUtils.h` | C++ | 296 |

## Overview

[[[PROSE overview unit=app-logic/ResolvedTriangulationUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ResolvedTriangulation::VertexIndices`](#gplatesapplogicresolvedtriangulationvertexindices) | class | — | `< class VertexType, class VertexMapPredicateType = std::less<VertexType> >` | 0 | Convenient utility class to assign indices (starting at zero) to triangulation vertices. |

## Members

### `GPlatesAppLogic::ResolvedTriangulation::VertexIndices`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `vertex_type` | typedef | `VertexType` | public | Typedef for the triangulation vertex type. |
| `vertex_seq_type` | typedef | `std::vector<vertex_type>` | public | Typedef for a sequence of vertices. |
| `add_vertex( const vertex_type &vertex)` | method | `unsigned int` | public | Adds vertex and returns the index assigned to vertex. |
| `vertex_index_map_type` | typedef | `std::map<vertex_type, unsigned int, VertexMapPredicateType>` | private | Keeps track of indices assigned to vertices. |
| `d_vertex_index_map` | field | `vertex_index_map_type` | private | — |
| `d_vertices` | field | `vertex_seq_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RESOLVEDTRIANGULATIONUTILS_H` | macro | `None` | — |
| `linear_interpolation_2( const std::pair< std::vector< std::pair<Point2Type, CoordType> >, CoordType> &natural_neighbor_coordinates_2, const Functor &function_value)` | function | `typename Functor::data_type` | — |
| `get_barycentric_coords_2( const Point2Type &p0, const Point2Type &p1, const Point2Type &p2, const Point2Type &p3, CoordType &b0, CoordType &b1, CoordType &b2, CoordType &b3)` | function | `void` | — |
| `convert_point_on_sphere_to_point_3( const GPlatesMaths::PointOnSphere &point)` | function | `Point3Type` | — |
| `convert_point_3_to_point_on_sphere( const Point3Type &point_3)` | function | `GPlatesMaths::PointOnSphere` | — |

## Notes

[[[PROSE notes unit=app-logic/ResolvedTriangulationUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 35 |
| [app-logic/ResolvedTriangulationNetwork](ResolvedTriangulationNetwork.md) | app-logic | 4 |
| [app-logic/ResolvedTriangulationDelaunay2](ResolvedTriangulationDelaunay2.md) | app-logic | 2 |
| [app-logic/PlateVelocityUtils](PlateVelocityUtils.md) | app-logic | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ResolvedTriangulationUtils.h
python scripts/gpq.py def GPlatesAppLogic::ResolvedTriangulation::VertexIndices --body
python scripts/gpq.py uses VertexIndices --kind class
python scripts/gpq.py hier VertexIndices
```

# GeometryCrossing

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1489 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/GeometryCrossing.h` | C++ | 61 |
| `src/maths/GeometryCrossing.cc` | C++ | 202 |

## Overview

Filters a `GeometryIntersect::Graph` to identify only the intersections that represent true geometric crossings. When two geometries intersect through segment-segment contact, that is a crossing; when they touch or overlap at vertices without crossing, it is not. This module distinguishes those cases by analyzing the nature and topology of vertex intersections, removing non-crossing overlaps and touches from the intersection graph.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::GeometryCrossing::vertex_intersection_map_type`](#gplatesmathsgeometrycrossingvertex_intersection_map_type) | typedef | — | — | 0 | Typedef for mapping segment indices of geometry1 to intersections. |

## Members

### `GPlatesMaths::GeometryCrossing::vertex_intersection_map_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `contains_vertex_intersections( const GeometryIntersect::Graph &intersection_graph)` | function | `bool` | Returns true if any intersections touch a vertex of either geometry. |
| `find_vertex_crossing( const GeometryIntersect::Intersection &vertex_intersection, vertex_intersection_map_type &vertex_intersection_map, const GeometryIntersect::intersection_seq_type &intersections)` | function | `boost::optional<unsigned int/*intersection_index*/>` | — |
| `find_vertex_crossings( const GeometryIntersect::Graph &intersection_graph)` | function | `GPlatesMaths::GeometryIntersect::Graph` | — |
| `GPLATES_MATH_GEOMETRYCROSSING_H` | macro | `None` | — |
| `find_crossings( GeometryIntersect::Graph &intersection_graph)` | function | `GeometryIntersect::Graph` | Finds the intersections of two geometries that result in each geometry \*crossing\* the other. |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/GeometryCrossing.h
python scripts/gpq.py def GPlatesMaths::GeometryCrossing::vertex_intersection_map_type --body
python scripts/gpq.py uses vertex_intersection_map_type --kind typedef
```

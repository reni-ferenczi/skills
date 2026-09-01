# GeometryCrossing

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1489 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/GeometryCrossing.h` | C++ | 61 |
| `src/maths/GeometryCrossing.cc` | C++ | 202 |

## Overview

[[[PROSE overview unit=maths/GeometryCrossing tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/GeometryCrossing tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

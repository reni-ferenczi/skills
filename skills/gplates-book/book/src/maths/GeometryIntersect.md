# GeometryIntersect

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 414 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/GeometryIntersect.h` | C++ | 410 |
| `src/maths/GeometryIntersect.cc` | C++ | 1438 |

## Overview

This is the primitive that finds every point where two polylines or polygons meet
on the sphere, and it is the thing the topology machinery is built on:
`GPlatesMaths::PolylineIntersections` and `GPlatesMaths::GeometryCrossing` wrap
it, and `GPlatesAppLogic::TopologyIntersections` uses it to work out where plate
boundary sections cut one another. The interface deliberately does not return
partitioned geometries — it returns a `Graph` of intersection *locations*, each
carrying the segment index and the angle into that segment for both inputs. That
is what lets a caller map a vertex of a partitioned piece back to a vertex of the
original geometry, which matters when a per-vertex quantity (a scalar coverage
value, a velocity) has to travel with the partition. `PolylineIntersections`,
which does return geometries, throws that association away.

The dominant concern in this code is robustness under finite precision, not
speed, and the whole design follows from it. Every segment is treated as a
*thick* great-circle plane whose half-thickness is
`THICKNESS_THRESHOLD_SINE` — about 1e-6 radians, metres on the Earth's surface —
and every vertex has a matching coincidence radius `THICKNESS_THRESHOLD_COSINE`.
Two further decisions fall out. First, of the nine ways two segments can meet
(start/middle/end against start/middle/end, drawn as ASCII art in the header),
only four are recorded, because an intersection at a segment's *end* point is
always recorded instead as the *start* point of the following segment; this
removes duplicates and makes vertex-touching cases uniform. Second, since a
polyline's last segment has no following segment, its final vertex is reported
against a *fictitious one-past-the-last* segment index — the same trick as an
end iterator. Polygons need none of this because their rings wrap around, which
is what the `POLYGON_NEEDS_NO_LAST_SEGMENT_INDEX` sentinel disables.

Cost is controlled by the cached `PolyGreatCircleArcBoundingTree` that each
`PolylineOnSphere` and `PolygonOnSphere` already builds: the two trees are
descended in tandem, pruning whenever the nodes' bounding small circles miss,
and recursing into the larger node first so fewer small-circle tests are needed.
Only when both sides reach leaves is `intersect_segments` run over the segment
pairs. Below that, `add_segments_crossing_intersection` handles the ordinary case
with a normalised cross product of the two segment planes, and then carries three
successive fallbacks for degenerate configurations — segments sharing a great
circle, a segment whose endpoints are nearly antipodal, and both segments being
near half-circles on the same great circle, where it bisects the first segment
and interpolates within whichever half actually crosses.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::GeometryIntersect::SortGeometryIntersection`](#gplatesmathsgeometryintersectsortgeometryintersection) | class | — | — | 0 | Predicate to sort intersections from beginning of the geometry to end. |
| [`GPlatesMaths::GeometryIntersect::Intersection`](#gplatesmathsgeometryintersectintersection) | class | — | — | 0 | Location of an intersection between two geometries. |
| [`GPlatesMaths::GeometryIntersect::intersection_seq_type`](#gplatesmathsgeometryintersectintersection_seq_type) | typedef | — | — | 0 | Typedef for a sequence of Intersection. |
| [`GPlatesMaths::GeometryIntersect::Graph`](#gplatesmathsgeometryintersectgraph) | class | — | — | 0 | Contains the results of intersecting two geometries. |

## Members

### `GPlatesMaths::GeometryIntersect::SortGeometryIntersection`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SortGeometryIntersection( const intersection_seq_type &intersections, const unsigned int Intersection::*segment_index_ptr, const AngularDistance Intersection::*angle_in_segment_ptr)` | constructor | `None` | public | — |
| `operator()( unsigned int lhs, unsigned int rhs)` | operator | `bool` | public | — |
| `d_intersections` | field | `intersection_seq_type` | private | — |
| `Intersection` | field | `unsigned int` | private | — |

### `GPlatesMaths::GeometryIntersect::Intersection`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Type` | enum | `None` | public | Type of intersection, whether two great circle arc segments cross or touch. |
| `get_on_segment_start_threshold_cosine()` | method | `double` | public | Return the cosine (dot product of two points) of maximum angular distance used for "on segment start". |
| `get_on_segment_start_threshold_sine()` | method | `double` | public | Return the sine (dot product of point and GCA plane) of maximum angular distance used for "on segment start". |
| `Intersection( Type type_, const PointOnSphere &position_, unsigned int segment_index1_, unsigned int segment_index2_, const AngularDistance &angle_in_segment1_ = AngularDistance::ZERO, const AngularDistance &angle_in_segment2_ = AngularDistance::ZERO)` | constructor | `None` | public | — |
| `is_on_segment1_start()` | method | `bool` | public | Is this intersection \*on\* the start point of segment1 ? |
| `is_on_segment2_start()` | method | `bool` | public | Is this intersection \*on\* the start point of segment2 ? |
| `type` | field | `Type` | public | — |
| `position` | field | `PointOnSphere` | public | — |
| `segment_index1` | field | `unsigned int` | public | Segment index within the first geometry. |
| `segment_index2` | field | `unsigned int` | public | Segment index within the second geometry. |
| `angle_in_segment1` | field | `AngularDistance` | public | Angle (radians) from segment start point to intersection along segment in first geometry. |
| `angle_in_segment2` | field | `AngularDistance` | public | Angle (radians) from segment start point to intersection along segment in second geometry. |

### `GPlatesMaths::GeometryIntersect::intersection_seq_type`

*None.*

### `GPlatesMaths::GeometryIntersect::Graph`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `empty()` | method | `bool` | public | Returns true if graph is empty. |
| `clear()` | method | `void` | public | Empties the graph. |
| `unordered_intersections` | field | `intersection_seq_type` | public | The \*unordered\* intersections. |
| `geometry1_ordered_intersections` | field | `std::vector<unsigned int>` | public | The intersections \*ordered\* along each original geometry. |
| `geometry2_ordered_intersections` | field | `std::vector<unsigned int>` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `THICKNESS_THRESHOLD_COSINE` | variable | `double` | Thickness threshold used for a dot product between two points. |
| `THICKNESS_THRESHOLD_SINE` | variable | `double` | Thickness threshold used for a dot product between a point and a plane (GCA normal vector). |
| `POLYGON_NEEDS_NO_LAST_SEGMENT_INDEX` | variable | `unsigned int` | We don't need any special handling of the last segment in a polygon ring, so for polygons we just specify the maximum unsigned integer (so that no segment indices will compare equal with it and activate the special handling). |
| `sort_geometry_intersections( Graph &graph)` | function | `void` | For each of the two geometries, sort its intersection list such that intersections are ordered from the geometries start to end. |
| `add_intersection( Graph &graph, Intersection::Type intersection_type, const UnitVector3D &intersection_position, const UnitVector3D &segment1_start_point, const UnitVector3D &segment2_start_point, unsigned int segment1_index, unsigned int segment2_index)` | function | `void` | Add an Intersection to the graph. |
| `add_segments_crossing_intersection( Graph &graph, const UnitVector3D &segment1_start_point, const UnitVector3D &segment1_end_point, const UnitVector3D &segment1_plane, const UnitVector3D &segment2_start_point, const UnitVector3D &segment2_end_point, const UnitVector3D &segment2_plane, bool segment1_start_point_on_posit ...` | function | `void` | Two non-zero-length segments cross each other's \*thick\* plane - find and add the intersection. |
| `point_is_in_segment_lune( const UnitVector3D &point, const UnitVector3D &segment_plane, const UnitVector3D &segment_start_point, const UnitVector3D &segment_end_point)` | function | `bool` | Returns true if the specified point lies within the lune of the specified segment. |
| `intersect_segments( Graph &graph, const GreatCircleArc &segment1, const GreatCircleArc &segment2, unsigned int segment1_index, unsigned int segment2_index, unsigned int last_segment1_index, unsigned int last_segment2_index)` | function | `void` | See if two segments cross or touch each other's \*thick\* plane - if so, find and add the intersection(s). |
| `intersect_bounding_tree_nodes( Graph &graph, const PolyGreatCircleArcBoundingTree<GreatCircleArcConstIterator1Type> &geometry1_bounding_tree, const typename PolyGreatCircleArcBoundingTree<GreatCircleArcConstIterator1Type>::node_type &geometry1_sub_tree_node, const unsigned int last_segment1_index, const PolyGreatCircle ...` | function | `void` | Find any intersections between a bounding tree node (of segments) of one polyline or polygon, and the bounding tree node (of segments) of another polyline or polygon. |
| `intersect_geometries( Graph &graph, const PolyGeometryBoundingTree1Type &poly_geometry1_bounding_tree, const unsigned int last_segment1_index, const PolyGeometryBoundingTree2Type &poly_geometry2_bounding_tree, const unsigned int last_segment2_index)` | function | `bool` | Find any intersections between two polyline/polygon geometries. |
| `GPLATES_MATHS_GEOMETRYINTERSECT_H` | macro | `None` | — |
| `intersect( Graph &intersection_graph, const PolylineOnSphere &polyline1, const PolylineOnSphere &polyline2)` | function | `bool` | Find all points of intersection of polyline1 and polyline2, and store them in the returned Graph object. |
| `intersect( Graph &intersection_graph, const PolygonOnSphere &polygon1, const PolygonOnSphere &polygon2, bool include_polygon1_interior_rings = true, bool include_polygon2_interior_rings = true)` | function | `bool` | Find all points of intersection of polygon1 and polygon2, and store them in the returned Graph object. |
| `intersect( Graph &intersection_graph, const PolylineOnSphere &polyline, const PolygonOnSphere &polygon, bool include_polygon_interior_rings = true)` | function | `bool` | Find all points of intersection of polyline and polygon, and store them in the returned Graph object. |
| `intersect( Graph &intersection_graph, const PolygonOnSphere &polygon, const PolylineOnSphere &polyline, bool include_polygon_interior_rings = true)` | function | `bool` | Find all points of intersection of polygon and polyline, and store them in the returned Graph object. |

## Notes

- **A segment index can be one past the last segment.** For polylines,
  `segment_index1` may equal `polyline1.number_of_segments()`, meaning the
  intersection is at the polyline's final vertex. Indexing a geometry with it —
  `get_segment()`, or the segment iterators — is out of range. Polygon indices
  never do this, and are always valid for `PolygonOnSphere::get_segment()`,
  including when interior rings are included.
- **The two thresholds are coupled to code in other files, and the coupling is
  load-bearing.** `get_on_segment_start_threshold_cosine()` is deliberately equal
  to `GreatCircleArc::get_zero_length_threshold_cosine()`, so that a zero-length
  segment straddling another segment's plane still touches it and no intersection
  is lost. Separately, `BoundingSmallCircleBuilder`'s default angular expansion
  must match the same threshold, or the bounding-tree pruning could discard a
  pair of segments that do touch. Changing one threshold without the others
  silently loses intersections.
- **Test order inside `intersect_segments` is not arbitrary.** The
  distance-to-vertex tests run *before* the signed-distance-to-plane tests, and
  the crossing test is skipped entirely when any endpoint of one segment is
  coincident with any endpoint of the other. The long comment in the source
  explains the failure this prevents: one segment tunnelling through a shared
  vertex of two adjacent segments without any intersection being reported.
  Reordering these for tidiness reintroduces the bug.
- **Coincidence tests must stay exactly complementary.** The code consistently
  uses `dot >= THICKNESS_THRESHOLD_COSINE` for "coincident" and `<` for "not
  coincident", so that the same vertex reached from two adjacent segments always
  classifies identically. Any inconsistency here produces contradictory results
  for the shared vertex.
- **One segment pair can yield more than one intersection.** Overlapping
  collinear segments can produce two from a single pair — the header enumerates
  the cases. Do not assume a single result per pair, nor that the count matches a
  naive crossing count.
- **`Graph` is an out-parameter that is cleared on entry** by
  `intersect_geometries`, so reusing one instance across many calls avoids
  reallocation; when `intersect` returns `false` the graph is left empty. The
  two ordered vectors are index permutations into `unordered_intersections` and
  always have the same length as it — they are not separate intersection lists.
- **The ordering is by segment index then angle within the segment**, using
  `AngularDistance::is_precisely_less_than` (exact, not epsilon-tolerant), so two
  intersections at the same position within one segment have an unspecified
  relative order.
- The `Intersection::position` is not always exactly on both segments: for the
  three touching types it is a *vertex* of one geometry, which may be off the
  other segment by up to the threshold. Only `SEGMENTS_CROSS` computes a genuine
  crossing point.
- `get_bounding_tree()` builds and caches the tree on first call, so the first
  intersection test against a large geometry pays for the tree; there is no
  threading protection around that lazy build.

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/PolylineIntersections](PolylineIntersections.md) | maths | 144 |
| [maths/GeometryCrossing](GeometryCrossing.md) | maths | 49 |
| [app-logic/TopologyIntersections](../app-logic/TopologyIntersections.md) | app-logic | 43 |
| [app-logic/ResolvedSubSegmentRangeInSection](../app-logic/ResolvedSubSegmentRangeInSection.md) | app-logic | 13 |
| [app-logic/TopologyGeometryResolverLayerProxy](../app-logic/TopologyGeometryResolverLayerProxy.md) | app-logic | 6 |
| [maths/SmallCircleBounds](SmallCircleBounds.md) | maths | 4 |
| [app-logic/TopologyNetworkResolver](../app-logic/TopologyNetworkResolver.md) | app-logic | 3 |
| [app-logic/TopologyNetworkResolverLayerProxy](../app-logic/TopologyNetworkResolverLayerProxy.md) | app-logic | 3 |
| [app-logic/TopologyReconstruct](../app-logic/TopologyReconstruct.md) | app-logic | 3 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 2 |
| [app-logic/TopologyGeometryResolver](../app-logic/TopologyGeometryResolver.md) | app-logic | 1 |
| [app-logic/TopologyUtils](../app-logic/TopologyUtils.md) | app-logic | 1 |
| [app-logic/VelocityFieldCalculatorLayerProxy](../app-logic/VelocityFieldCalculatorLayerProxy.md) | app-logic | 1 |
| [file-io/CitcomsResolvedTopologicalBoundaryExport](../file-io/CitcomsResolvedTopologicalBoundaryExport.md) | file-io | 1 |
| [file-io/GMTFormatResolvedTopologicalGeometryExport](../file-io/GMTFormatResolvedTopologicalGeometryExport.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/GeometryIntersect.h
python scripts/gpq.py def GPlatesMaths::GeometryIntersect::Intersection --body
python scripts/gpq.py uses Intersection --kind class
python scripts/gpq.py hier Intersection
```

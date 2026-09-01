# PointInPolygon

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 68 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/PointInPolygon.h` | C++ | 181 |
| `src/maths/PointInPolygon.cc` | C++ | 1752 |

## Overview

This unit implements spherical point-in-polygon testing for `PolygonOnSphere`, including non-simple (self-intersecting) polygons and polygons with interior rings. The test counts how many polygon edges (exterior and interior rings) are crossed by the great circle arc running from the polygon's antipodal centroid to the test point; an odd number of crossings means the point is inside. `use_point_on_polygon_threshold` treats a point extremely close to an edge as inside, which matters for cases such as a point that falls exactly on the dateline against a polygon edge aligned with it.

There are two ways to run the test. The free function `is_point_in_polygon` is O(n) in the number of edges and does no bounds pre-processing, so it is only worthwhile for a handful of test points against a given polygon. `Polygon` wraps a `PolygonOnSphere` and, when profiling justifies it (`build_ologn_hint`), builds a `SphericalLuneTree`: a recursive partition of the sphere into spherical lunes sharing the centroid/antipodal axis, which lets a query descend to the small subset of edges that could possibly be crossed and brings the cost down to O(log n). Both paths always do cheap bounding-small-circle rejection first, which is where most of the practical speed-up over the naive edge count comes from.

Callers rarely construct a `SphericalLuneTree` directly — `Polygon` is the intended entry point, and `PolygonOnSphere` itself caches one internally (passing `keep_shared_reference_to_polygon = false` to avoid a reference cycle) so that most call sites just call `PolygonOnSphere::is_point_in_polygon` or use `Polygon` when testing many points against the same polygon, such as topology resolution and reconstructed-raster meshing.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::PointInPolygon::EdgeSequence`](#gplatesmathspointinpolygonedgesequence) | class | — | — | 0 | Keeps track of an iteration range of polygon edges. |
| [`GPlatesMaths::PointInPolygon::edge_sequence_list_type`](#gplatesmathspointinpolygonedge_sequence_list_type) | typedef | — | — | 0 | Typedef for a list of polygon edge ranges. |
| [`GPlatesMaths::PointInPolygon::SphericalLuneTree`](#gplatesmathspointinpolygonsphericallunetree) | class | — | — | 0 | A recursive spatial partition of the surface of the sphere into spherical lunes. |
| [`GPlatesMaths::PointInPolygon::Polygon`](#gplatesmathspointinpolygonpolygon) | class | — | — | 0 | A data structure, wrapped around a PolygonOnSphere, that optimises point-in-polygon tests and works with non-simple (eg, self-intersecting) polygons. |

## Members

### `GPlatesMaths::PointInPolygon::EdgeSequence`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EdgeSequence( const PolygonOnSphere::ring_const_iterator &begin_, const PolygonOnSphere::ring_const_iterator &end_)` | constructor | `None` | public | — |
| `begin` | field | `PolygonOnSphere::ring_const_iterator` | public | — |
| `end` | field | `PolygonOnSphere::ring_const_iterator` | public | — |

### `GPlatesMaths::PointInPolygon::edge_sequence_list_type`

*None.*

### `GPlatesMaths::PointInPolygon::SphericalLuneTree`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( const PolygonOnSphere::non_null_ptr_to_const_type &polygon, bool build_ologn_hint, bool keep_shared_reference_to_polygon)` | method | `std::unique_ptr<SphericalLuneTree>` | public | Creates a SphericalLuneTree. |
| `is_point_in_polygon( const UnitVector3D &test_point, bool use_point_on_polygon_threshold)` | method | `bool` | public | — |
| `edge_sequence_index_type` | typedef | `unsigned int` | private | Typedef for an index into a sequence of EdgeSequence objects. |
| `node_index_type` | typedef | `unsigned int` | private | Typedef for a node index (can be internal or leaf). |
| `InternalNode` | class | `None` | private | An internal node of spherical lune tree (has two child nodes). |
| `internal_node_seq_type` | typedef | `std::vector<InternalNode>` | private | — |
| `LeafNode` | class | `None` | private | A leaf node of spherical lune tree. |
| `leaf_node_seq_type` | typedef | `std::vector<LeafNode>` | private | — |
| `TreeData` | class | `None` | private | The data for the spherical lune tree - the code is in class SphericalLuneTree - this is so the TreeBuilder can build the tree data and pass it to the SphericalLuneTree. |
| `BoundsDataBuilder` | class | `None` | private | Builds the inner and outer bounding small circles used for quickly testing if a point is inside/outside the polygon. |
| `BoundsData` | class | `None` | private | The inner and outer bounding small circles used for quickly testing if a point is inside/outside the polygon. |
| `TreeBuilder` | class | `None` | private | Use to build the spherical lune tree. |
| `d_polygon_shared_pointer` | field | `boost::optional<PolygonOnSphere::non_null_ptr_to_const_type>` | private | A reference to ensure the polygon stays alive because we are storing iterators into its internal structures. |
| `d_polygon` | field | `PolygonOnSphere` | private | The polygon reference to use when iterating over the polygon's points. |
| `d_polygon_centroid_antipodal` | field | `UnitVector3D` | private | The antipodal of the polygon centroid that is also the start of the crossings arc (the end is the test point of the point-in-polygon test). |
| `d_bounds_data` | field | `BoundsData` | private | Bounds data for the entire polygon - for early rejection/acceptance testing. |
| `d_tree_data` | field | `boost::optional<TreeData>` | private | The data for the spherical lune tree. |
| `SphericalLuneTree( const PolygonOnSphere::non_null_ptr_to_const_type &polygon, bool keep_shared_reference_to_polygon, const UnitVector3D &polygon_centroid_antipodal, const BoundsDataBuilder &bounds_data_builder, const boost::optional<TreeData> &tree_data = boost::none)` | constructor | `None` | private | — |
| `is_point_in_polygon( const InternalNode &node, const UnitVector3D &test_point, bool use_point_on_polygon_threshold)` | method | `bool` | private | — |

### `GPlatesMaths::PointInPolygon::Polygon`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Polygon( const GPlatesGlobal::PointerTraits<const PolygonOnSphere>::non_null_ptr_type &polygon, bool build_ologn_hint = true, bool keep_shared_reference_to_polygon = true)` | constructor | `None` | public | Constructor - polygon can be non-simple (eg, self-intersecting). |
| `is_point_in_polygon( const PointOnSphere &point, bool use_point_on_polygon_threshold = true)` | method | `bool` | public | Tests if point is inside the polygon passed into the constructor. |
| `d_spherical_lune_tree` | field | `boost::shared_ptr<SphericalLuneTree>` | private | Bounds testing and an optional O(log(N)) tree (in the number of polygons edges N). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `MAX_DOT_PRODUCT_CROSSING_ARC_AND_POLYGON_EDGE` | variable | `double` | If dot product of crossing arc and polygon edge greater than this then too closely aligned. |
| `MIN_DOT_PRODUCT_CROSSING_ARC_AND_POLYGON_EDGE` | variable | `double` | If dot product of crossing arc and polygon edge less than this then too closely aligned. |
| `POINT_ON_POLYGON_OUTLINE_COSINE` | variable | `double` | The test point can lie "on" a polygon edge by using an epsilon when testing closeness to the great circle plane of a polygon edge. |
| `POINT_ON_POLYGON_OUTLINE_SINE` | variable | `double` | Base epsilon calculations off a cosine since that usually has the least accuracy for small angles. '1 - 1e-12' in cosine corresponds to a displacement of about 1.4e-6 \[=sin(acos(1 - 1e-12))\]. |
| `get_polygon_centroid( const PolygonOnSphere &polygon)` | function | `UnitVector3D` | Finds the point antipodal to the centroid of the polygon boundary. |
| `get_crossings_arc_plane_normal( const UnitVector3D &crossing_arc_start_point, const UnitVector3D &crossing_arc_end_point)` | function | `UnitVector3D` | Returns the un-normalised normal (rotation axis) of the arc joining the antipodal point of a polygon's centroid and the test point. |
| `does_polygon_edge_intersection_with_crossing_gc_lie_on_crossing_gca( const UnitVector3D &crossings_arc_start_point, const UnitVector3D &crossings_arc_end_point, const UnitVector3D &crossings_arc_rotation_axis, const double &dot_crossings_arc_end_points, const UnitVector3D &intersection_point, bool use_point_on_polygon_ ...` | function | `bool` | Returns true if the intersection of polygon edge with crossing arc \*great circle\* lies on the crossing \*arc\* defined by crossing\_arc\_start\_point, crossing\_arc\_end\_point and dot\_crossing\_arc\_end\_points. |
| `if_plane_divides_gca_get_intersection_of_gca_and_plane( const GreatCircleArc &gca, const UnitVector3D &plane_normal)` | function | `UnitVector3D` | Returns the intersection of the great circle arc gca and the plane (passing through origin) with normal plane\_normal. @pre the endpoints of the great circle arc gca must be on opposite sides of the plane. @pre the great circle arc gca must ... |
| `get_num_polygon_edges_crossed( const PolygonOnSphere::ring_const_iterator &edges_begin, const PolygonOnSphere::ring_const_iterator &edges_end, const UnitVector3D &crossings_arc_start_point, const UnitVector3D &crossings_arc_end_point, const UnitVector3D &crossings_arc_plane_normal, const double &dot_crossings_arc_end_p ...` | function | `unsigned int` | Returns the number of polygon edges crossed by the great circle arc joining crossings\_arc\_start\_point and crossings\_arc\_end\_point. |
| `is_point_in_polygon( const PolygonOnSphere &polygon, const UnitVector3D &crossings_arc_start_point, const UnitVector3D &crossings_arc_end_point, bool use_point_on_polygon_threshold)` | function | `bool` | Returns true if the test point (which is crossings\_arc\_end\_point) is inside polygon (taking into account exterior and interior rings). |
| `is_point_in_polygon( const edge_sequence_list_type::const_iterator &edge_sequences_begin, const edge_sequence_list_type::const_iterator &edge_sequences_end, const UnitVector3D &crossings_arc_start_point, const UnitVector3D &crossings_arc_end_point, bool use_point_on_polygon_threshold)` | function | `bool` | Returns true if the test point (which is crossings\_arc\_end\_point) is inside polygon. |
| `get_dot_product_range_of_polygon_edges_to_point( const edge_sequence_list_type &edge_sequences, const UnitVector3D &point)` | function | `std::pair< double/*min dot product*/, double/*max dot product*/ >` | Returns the coverage of polygon edges as a min/max range of dot products to a point. |
| `SPHERICAL_WEDGE_PLANE_EPSILON` | variable | `double` | '1e-4' represents an angular deviation of 0.34 minutes away from the plane. |
| `GPLATES_MATHS_POINTINPOLYGON_H` | macro | `None` | — |
| `is_point_in_polygon( const PointOnSphere &point, const PolygonOnSphere &polygon, bool use_point_on_polygon_threshold = true)` | function | `bool` | Tests if point is inside polygon which can be a non-simple (eg, self-intersecting) polygon. |

## Notes

- If an interior ring intersects the exterior ring, a test point outside the exterior ring but inside the interior ring can still be classified as inside, because the algorithm only counts total edge crossings rather than reasoning about ring containment. This mirrors how filled polygons are rendered elsewhere, so it is treated as acceptable rather than as a bug.
- `Polygon` and `SphericalLuneTree` keep the polygon alive via `d_polygon_shared_pointer` only when `keep_shared_reference_to_polygon` is true; `PolygonOnSphere` passes `false` when it owns the tree itself, since otherwise the shared pointers would form a reference cycle and leak.
- The "on the outline counts as inside" threshold is an extremely small angular epsilon (`POINT_ON_POLYGON_OUTLINE_COSINE`/`_SINE`), tuned to catch essentially-coincident points such as ones exactly on the dateline — it is not a general-purpose tolerance for nearby points.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 11 |
| [maths/PolygonPartitioner](PolygonPartitioner.md) | maths | 7 |
| [maths/PolygonOnSphere](PolygonOnSphere.md) | maths | 6 |
| [data-mining/deprecated/IsInRegionOfInterestVisitor](../data-mining/deprecated/IsInRegionOfInterestVisitor.md) | data-mining | 5 |
| [view-operations/RenderedPolylineOnSphere](../view-operations/RenderedPolylineOnSphere.md) | view-operations | 5 |
| [view-operations/RenderedGeometryFactory](../view-operations/RenderedGeometryFactory.md) | view-operations | 4 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/PointInPolygon.h
python scripts/gpq.py def GPlatesMaths::PointInPolygon::SphericalLuneTree --body
python scripts/gpq.py uses SphericalLuneTree --kind class
python scripts/gpq.py hier SphericalLuneTree
```

# PolygonOnSphere

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 100 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/PolygonOnSphere.h` | C++ | 2288 |
| `src/maths/PolygonOnSphere.cc` | C++ | 1127 |

## Overview

`PolygonOnSphere` is the closed-region member of the `GeometryOnSphere` family, alongside
`PointGeometryOnSphere`, `MultiPointOnSphere` and `PolylineOnSphere`. It does not store points:
it stores one exterior ring plus zero or more interior rings, each ring a
`std::vector<GreatCircleArc>` whose final arc closes back onto the ring's first vertex. Interior
rings turn the polygon into a "donut" with holes. Because the closing arc is part of the
representation, a ring has exactly as many segments as vertices — the structural difference from
`PolylineOnSphere`, and the reason three separate iteration schemes exist rather than one: straight
per-ring iteration over the arc vector (`ring_const_iterator`); whole-polygon iteration over every
arc of every ring (`ConstIterator`, a `boost::iterator_facade` that hops from the exterior ring into
each interior ring in turn, tagged random-access so `std::advance` can index into it); and
"treat this ring as a polyline" iteration, which reuses `PolylineOnSphere::VertexConstIterator` and
emits the ring's first vertex a second time at the end. Exporters and renderers that need an
explicitly closed vertex list want the third.

Instances are immutable, heap-allocated and intrusively reference-counted through
`GPlatesUtils::ReferenceCount`; `create` is the only way in, and it hands back
`non_null_ptr_to_const_type`, so nothing outside the class ever holds a mutable polygon. `create`
allocates an empty polygon through the private constructor and then calls
`generate_rings_and_swap`, which validates, builds the rings into temporaries and swaps them in —
that is where the "strongly exception-safe" guarantee in the Doxygen comes from. Validation rejects
two things: a ring with fewer than `s_min_num_ring_points` (three) points, and adjacent points that
are antipodal, which `GreatCircleArc::evaluate_construction_parameter_validity` refuses because the
arc between them is not unique. Either failure throws
`InvalidPointsForPolygonConstructionError`, carrying the `ConstructionParameterValidity` value so
the message can name the cause. The `check_distinct_points` flag exists to make the point count
lenient by default: rotating a small polygon can collapse two points to within epsilon, and the
comment on `create` is explicit that a polygon good enough to load should stay good enough after
rotation.

Everything derived from the ring data is computed lazily and cached in
`PolygonOnSphereImpl::CachedCalculations`, an intrusively counted struct hanging off a `mutable`
pointer that stays null until the first derived quantity is asked for. The polygon itself owns no
algorithms — it delegates to `SphericalArea` for signed area, `PolygonOrientation`, `Centroid` for
the outline and interior centroids, `InnerOuterBoundingSmallCircleBuilder` from `SmallCircleBounds`,
`PolyGreatCircleArcBoundingTree` for the per-ring and whole-polygon bounding trees, and
`PointInPolygon` for containment — and its job is to make those results shared and reusable across
every caller that holds the same geometry. `is_point_in_polygon` goes further and escalates the
acceleration structure with use: `ADAPTIVE` builds a medium-speed `PointInPolygon::Polygon` after
four calls and a high-speed (O(log N)) one after two hundred, and the speed setting only ever
ratchets upward, since dropping back would throw away the setup already paid for.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::PolygonOnSphereImpl::CachedCalculations`](#gplatesmathspolygononsphereimplcachedcalculations) | struct | [`GPlatesUtils::ReferenceCount<CachedCalculations>`](../utils/ReferenceCount.md) | — | 0 | Cached results of calculations performed on the polygon geometry. |
| [`GPlatesMaths::PolygonOnSphere`](#gplatesmathspolygononsphere) | class | [`GeometryOnSphere`](GeometryOnSphere.md) | — | 0 | Represents a polygon on the surface of a sphere. |
| [`GPlatesMaths::InvalidPointsForPolygonConstructionError`](#gplatesmathsinvalidpointsforpolygonconstructionerror) | class | [`GPlatesGlobal::PreconditionViolationError`](../global/PreconditionViolationError.md) | — | 0 | The exception thrown when an attempt is made to create a polygon using invalid points. |

## Members

### `GPlatesMaths::PolygonOnSphereImpl::CachedCalculations`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CachedCalculations()` | constructor | `None` | public | — |
| `exterior_ring_arc_length` | field | `boost::optional<real_t>` | public | — |
| `interior_ring_arc_lengths` | field | `boost::optional< std::vector<real_t> >` | public | — |
| `outline_centroid_including_interior_rings` | field | `boost::optional<UnitVector3D>` | public | — |
| `outline_centroid_excluding_interior_rings` | field | `boost::optional<UnitVector3D>` | public | — |
| `interior_centroid` | field | `boost::optional<UnitVector3D>` | public | — |
| `inner_outer_bounding_small_circle` | field | `boost::optional<InnerOuterBoundingSmallCircle>` | public | — |
| `signed_area` | field | `boost::optional<real_t>` | public | — |
| `orientation` | field | `boost::optional<PolygonOrientation::Orientation>` | public | — |
| `point_in_polygon_speed_and_memory` | field | `PolygonOnSphere::PointInPolygonSpeedAndMemory` | public | — |
| `num_point_in_polygon_calls` | field | `unsigned int` | public | — |
| `point_in_polygon_tester` | field | `boost::optional<PointInPolygon::Polygon>` | public | — |
| `polygon_bounding_tree` | field | `boost::optional<PolygonOnSphere::bounding_tree_type>` | public | — |
| `exterior_polygon_bounding_tree` | field | `boost::optional<PolygonOnSphere::ring_bounding_tree_type>` | public | — |
| `interior_polygon_bounding_trees` | field | `boost::optional< std::vector< boost::shared_ptr<PolygonOnSphere::ring_bounding_tree_type> > >` | public | — |

### `GPlatesMaths::PolygonOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<PolygonOnSphere>` | private | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<PolygonOnSphere\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const PolygonOnSphere>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const PolygonOnSphere\>. |
| `ring_type` | typedef | `std::vector<GreatCircleArc>` | public | The type of the sequence of great circle arcs that form a closed ring. |
| `ring_const_iterator` | typedef | `ring_type::const_iterator` | public | The type used to const-iterate over the sequence of arcs in a closed ring. |
| `ring_sequence_type` | typedef | `std::vector<ring_type>` | public | Typedef for a sequence of rings. |
| `ring_sequence_const_iterator` | typedef | `ring_sequence_type::const_iterator` | public | Typedef for a const iterator over ring\_sequence\_type. |
| `RingVertexConstIterator` | class | `None` | public | This class enables const\_iteration over vertices in an exterior or interior ring of PolygonOnSphere. |
| `ring_vertex_const_iterator` | typedef | `RingVertexConstIterator` | public | The type used to const\_iterate over the vertices in a ring. |
| `polyline_vertex_const_iterator` | typedef | `PolylineOnSphere::VertexConstIterator<ring_const_iterator>` | public | The type used to const\_iterate over the vertices in a ring as if it was a polyline. |
| `ConstIterator` | class | `None` | public | This class enables const\_iteration over \*all\* arcs of PolygonOnSphere. |
| `const_iterator` | typedef | `ConstIterator` | public | The type used to const\_iterate over \*all\* arcs. |
| `VertexConstIterator` | class | `None` | public | This class enables const\_iteration over vertices in \*all\* arcs of PolygonOnSphere (exterior and interior). |
| `vertex_const_iterator` | typedef | `VertexConstIterator` | public | The type used to const\_iterate over vertices in \*all\* arcs of PolygonOnSphere (exterior and interior). |
| `ring_bounding_tree_type` | typedef | `PolyGreatCircleArcBoundingTree<ring_const_iterator, true/*RequireRandomAccessIterator*/>` | public | Typedef for the bounding tree of great circle arcs within a ring. |
| `bounding_tree_type` | typedef | `PolyGreatCircleArcBoundingTree<const_iterator, true/*RequireRandomAccessIterator*/>` | public | Typedef for the bounding tree of \*all\* great circle arcs in polygon. |
| `ConstructionParameterValidity` | enum | `None` | public | The possible return values from the construction-parameter validation function evaluate\_construction\_parameter\_validity. |
| `evaluate_construction_parameter_validity( PointForwardIter exterior_begin, PointForwardIter exterior_end, bool check_distinct_points = false)` | method | `ConstructionParameterValidity` | public | Evaluate the validity of the construction-parameters. |
| `evaluate_construction_parameter_validity( const PointCollectionType &exterior_points, bool check_distinct_points = false)` | method | `ConstructionParameterValidity` | public | Evaluate the validity of the construction-parameters. exterior\_points should be a sequential STL container (list, vector, ...) of PointOnSphere. |
| `evaluate_construction_parameter_validity( PointForwardIter exterior_begin, PointForwardIter exterior_end, PointCollectionForwardIter interior_rings_begin, PointCollectionForwardIter interior_rings_end, bool check_distinct_points = false)` | method | `ConstructionParameterValidity` | public | Evaluate the validity of the construction-parameters. |
| `evaluate_construction_parameter_validity( const PointCollectionType &exterior_points, PointCollectionForwardIter interior_rings_begin, PointCollectionForwardIter interior_rings_end, bool check_distinct_points = false)` | method | `ConstructionParameterValidity` | public | Evaluate the validity of the construction-parameters. exterior\_points should be a sequential STL container (list, vector, ...) of PointOnSphere. |
| `create( PointForwardIter exterior_begin, PointForwardIter exterior_end, bool check_distinct_points = false)` | method | `non_null_ptr_to_const_type` | public | Say you have a sequence of PointOnSphere \[A, B, C, D\] for an exterior ring. |
| `create( const PointCollectionType &exterior_points, bool check_distinct_points = false)` | method | `non_null_ptr_to_const_type` | public | Create a new PolygonOnSphere instance on the heap from a sequence of exterior points in exterior\_points. exterior\_points should be a sequential STL container (list, vector, ...) of PointOnSphere. |
| `create( PointForwardIter exterior_begin, PointForwardIter exterior_end, PointCollectionForwardIter interior_rings_begin, PointCollectionForwardIter interior_rings_end, bool check_distinct_points = false)` | method | `non_null_ptr_to_const_type` | public | iterating through the arcs of the interior ring using the member functions interior\_ring\_begin and interior\_ring\_end (with interior ring index 0) will return the 3 interior ring segments. - Iterating through the arcs of all rings using the ... |
| `create( const PointCollectionType &exterior_points, PointCollectionForwardIter interior_rings_begin, PointCollectionForwardIter interior_rings_end, bool check_distinct_points = false)` | method | `non_null_ptr_to_const_type` | public | Create a new PolygonOnSphere instance on the heap from a sequence of exterior points in exterior\_points and a sequence of interior rings (where each ring is a sequence of points). exterior\_points should be a sequential STL container (list, ... |
| `create( const PointCollectionType &exterior_points, const RingCollectionType &interior_rings, bool check_distinct_points = false)` | method | `non_null_ptr_to_const_type` | public | Create a new PolygonOnSphere instance on the heap from a sequence of exterior points in exterior\_points and a sequence of interior rings in interior\_rings. exterior\_points should be a sequential STL container (list, vector, ...) of ... |
| `~PolygonOnSphere()` | destructor | `None` | public | — |
| `test_proximity( const ProximityCriteria &criteria)` | method | `ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `test_vertex_proximity( const ProximityCriteria &criteria)` | method | `ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `accept_visitor( ConstGeometryOnSphereVisitor &visitor)` | method | `void` | public | Accept a ConstGeometryOnSphereVisitor instance. |
| `get_non_null_pointer()` | method | `non_null_ptr_to_const_type` | public | Return this instance as a non-null pointer. |
| `begin()` | method | `const_iterator` | public | Return the 'begin' const\_iterator over \*all\* GreatCircleArc of this polygon. |
| `end()` | method | `const_iterator` | public | Return the 'end' const\_iterator over \*all\* GreatCircleArc of this polygon. |
| `segment_iterator( unsigned int segment_index)` | method | `const_iterator` | public | Return the const\_iterator in this polygon at the specified segment index (which can be in an exterior or interior ring), so can iterate over GreatCircleArc starting at that segment. |
| `number_of_segments()` | method | `unsigned int` | public | Return the number of segments in this polygon. |
| `vertex_begin()` | method | `vertex_const_iterator` | public | Return the 'begin' vertex\_const\_iterator over \*all\* vertices of this polygon. |
| `vertex_end()` | method | `vertex_const_iterator` | public | Return the 'end' vertex\_const\_iterator over \*all\* vertices of this polygon. |
| `vertex_iterator( unsigned int vertex_index)` | method | `vertex_const_iterator` | public | Return the vertex\_const\_iterator in this polygon at the specified vertex index (which can be in an exterior or interior ring). |
| `number_of_vertices()` | method | `unsigned int` | public | Return the number of vertices in this polygon. |
| `exterior_ring_begin()` | method | `ring_const_iterator` | public | Return the 'begin' ring\_const\_iterator over the sequence of GreatCircleArc which defines the exterior of this polygon. |
| `exterior_ring_end()` | method | `ring_const_iterator` | public | Return the 'end' ring\_const\_iterator over the sequence of GreatCircleArc which defines the exterior of this polygon. |
| `exterior_ring_iterator( unsigned int exterior_segment_index)` | method | `ring_const_iterator` | public | Return the ring\_const\_iterator at the specified segment index in the exterior ring. exterior\_segment\_index can be one past the last segment, corresponding to exterior\_ring\_end. |
| `number_of_segments_in_exterior_ring()` | method | `unsigned int` | public | Return the number of segments in the exterior ring in this polygon. |
| `exterior_ring_vertex_begin()` | method | `ring_vertex_const_iterator` | public | Return the 'begin' ring\_vertex\_const\_iterator over the exterior vertices of this polygon. |
| `exterior_ring_vertex_end()` | method | `ring_vertex_const_iterator` | public | Return the 'end' ring\_vertex\_const\_iterator over the exterior vertices of this polygon. |
| `exterior_ring_vertex_iterator( unsigned int exterior_vertex_index)` | method | `ring_vertex_const_iterator` | public | Return the ring\_vertex\_const\_iterator at the specified vertex index in the exterior ring. exterior\_vertex\_index can be one past the last vertex, corresponding to exterior\_ring\_vertex\_end. |
| `number_of_vertices_in_exterior_ring()` | method | `unsigned int` | public | Return the number of vertices in the exterior ring in this polygon. |
| `exterior_polyline_vertex_begin()` | method | `polyline_vertex_const_iterator` | public | Return the 'begin' polyline\_vertex\_const\_iterator over the exterior ring as if it was a polyline. |
| `exterior_polyline_vertex_end()` | method | `polyline_vertex_const_iterator` | public | Return the 'end' polyline\_vertex\_const\_iterator over the exterior ring as if it was a polyline. |
| `exterior_polyline_vertex_iterator( unsigned int exterior_vertex_index)` | method | `polyline_vertex_const_iterator` | public | Return the polyline\_vertex\_const\_iterator at the specified vertex index in the exterior ring behaving as if it was a polyline. exterior\_vertex\_index can be one past the last vertex, corresponding to exterior\_polyline\_vertex\_end. |
| `number_of_vertices_in_exterior_polyline()` | method | `unsigned int` | public | Return the number of vertices in the exterior ring as if it was a polyline. |
| `interior_rings_begin()` | method | `ring_sequence_const_iterator` | public | Return the "begin" const iterator over the interior rings of this polygon. |
| `interior_rings_end()` | method | `ring_sequence_const_iterator` | public | Return the "end" const iterator over the interior rings of this polygon. |
| `number_of_interior_rings()` | method | `unsigned int` | public | Return the number of interior rings in this polygon. |
| `interior_ring_begin( unsigned int interior_ring_index)` | method | `ring_const_iterator` | public | Return the 'begin' ring\_const\_iterator over the sequence of GreatCircleArc which defines the interior ring of this polygon at the specified interior ring index. |
| `interior_ring_end( unsigned int interior_ring_index)` | method | `ring_const_iterator` | public | Return the 'end' ring\_const\_iterator over the sequence of GreatCircleArc which defines the interior ring of this polygon at the specified interior ring index. |
| `interior_ring_iterator( unsigned int interior_ring_index, unsigned int segment_index)` | method | `ring_const_iterator` | public | Return the ring\_const\_iterator at the specified segment index in the specified interior ring. segment\_index can be one past the last segment, corresponding to interior\_ring\_end. |
| `number_of_segments_in_interior_ring( unsigned int interior_ring_index)` | method | `unsigned int` | public | Return the number of segments in the interior ring in this polygon at the specified interior ring index. |
| `interior_ring_vertex_begin( unsigned int interior_ring_index)` | method | `ring_vertex_const_iterator` | public | Return the 'begin' ring\_vertex\_const\_iterator over the vertices of the interior ring of this polygon at the specified interior ring index. |
| `interior_ring_vertex_end( unsigned int interior_ring_index)` | method | `ring_vertex_const_iterator` | public | Return the 'end' ring\_vertex\_const\_iterator over the vertices of the interior ring of this polygon at the specified interior ring index. |
| `interior_ring_vertex_iterator( unsigned int interior_ring_index, unsigned int vertex_index)` | method | `ring_vertex_const_iterator` | public | Return the ring\_vertex\_const\_iterator at the specified vertex index in the specified interior ring. vertex\_index can be one past the last vertex, corresponding to interior\_ring\_vertex\_end. |
| `number_of_vertices_in_interior_ring( unsigned int interior_ring_index)` | method | `unsigned int` | public | Return the number of vertices in the interior ring in this polygon at the specified interior ring index. |
| `interior_polyline_vertex_begin( unsigned int interior_ring_index)` | method | `polyline_vertex_const_iterator` | public | Return the 'begin' polyline\_vertex\_const\_iterator over an interior ring as if it was a polyline. |
| `interior_polyline_vertex_end( unsigned int interior_ring_index)` | method | `polyline_vertex_const_iterator` | public | Return the 'end' polyline\_vertex\_const\_iterator over an interior ring as if it was a polyline. |
| `interior_polyline_vertex_iterator( unsigned int interior_ring_index, unsigned int vertex_index)` | method | `polyline_vertex_const_iterator` | public | Return the polyline\_vertex\_const\_iterator at the specified vertex index in an interior ring behaving as if it was a polyline. vertex\_index can be one past the last vertex, corresponding to interior\_polyline\_vertex\_end. |
| `number_of_vertices_in_interior_polyline( unsigned int interior_ring_index)` | method | `unsigned int` | public | Return the number of vertices in an interior ring as if it was a polyline. |
| `is_close_to( const PointOnSphere &test_point, const AngularExtent &closeness_angular_extent_threshold, real_t &closeness)` | method | `boost::optional<PointOnSphere>` | public | Evaluate whether test\_point is "close" to this polygon. |
| `operator==( const PolygonOnSphere &other)` | operator | `bool` | public | Equality operator compares great circle arc subsegments. |
| `operator!=( const PolygonOnSphere &other)` | operator | `bool` | public | Inequality operator. |
| `get_arc_length()` | method | `real_t` | public | Returns the total arc-length of the exterior ring and interior rings (each ring is a sequences of GreatCirclArc. |
| `get_exterior_ring_arc_length` | field | `real_t` | public | Returns the arc-length of the exterior ring sequence of GreatCirclArc which defines the exterior of this polygon. |
| `get_interior_ring_arc_length` | field | `real_t` | public | Returns the arc-length of an interior ring sequence of GreatCirclArc for the specified interior ring index. |
| `get_area()` | method | `real_t` | public | Returns the area of this polygon. |
| `get_signed_area` | field | `real_t` | public | Returns the signed area of this polygon. |
| `get_orientation()` | method | `PolygonOrientation::Orientation` | public | Returns the orientation of this polygon. |
| `PointInPolygonSpeedAndMemory` | enum | `None` | public | Determines the speed versus memory trade-off of point-in-polygon tests. |
| `is_point_in_polygon( const PointOnSphere &point, PointInPolygonSpeedAndMemory speed_and_memory = ADAPTIVE, bool use_point_on_polygon_threshold = true)` | method | `bool` | public | Tests whether the specified point is inside this polygon. |
| `get_boundary_centroid` | field | `UnitVector3D` | public | Returns the centroid of the \*edges\* of the exterior ring of this polygon (see Centroid::calculate\_outline\_centroid). |
| `get_outline_centroid` | field | `UnitVector3D` | public | Returns the centroid of the \*edges\* of this polygon (see Centroid::calculate\_outline\_centroid). |
| `get_interior_centroid` | field | `UnitVector3D` | public | Returns the centroid of the \*interior\* of this polygon (see Centroid::calculate\_interior\_centroid). |
| `get_bounding_small_circle` | field | `BoundingSmallCircle` | public | Returns the small circle that bounds this polygon - the small circle centre is the same as calculated by get\_boundary\_centroid. |
| `get_inner_outer_bounding_small_circle` | field | `InnerOuterBoundingSmallCircle` | public | Returns the inner and outer small circle bounds of this polygon - the small circle centre is the same as calculated by get\_boundary\_centroid. |
| `get_bounding_tree` | field | `bounding_tree_type` | public | Returns the small circle bounding tree over \*all\* great circle arc segments. |
| `get_exterior_ring_bounding_tree` | field | `ring_bounding_tree_type` | public | Returns the exterior ring small circle bounding tree over the great circle arc segments of the exterior ring of this polygon. |
| `get_interior_ring_bounding_tree` | field | `ring_bounding_tree_type` | public | Returns the interior ring small circle bounding tree at the specified interior ring index. |
| `PolygonOnSphere()` | constructor | `None` | private | Create an empty PolygonOnSphere instance. |
| `evaluate_ring_validity( PointForwardIter begin, PointForwardIter end, bool check_distinct_points)` | method | `ConstructionParameterValidity` | private | Evaluate the validity of the points for use in the creation of a ring. |
| `evaluate_segment_endpoint_validity( const PointOnSphere &p1, const PointOnSphere &p2)` | method | `ConstructionParameterValidity` | private | Evaluate the validity of the points p1 and p2 for use in the creation of a polygon line-segment. |
| `generate_rings_and_swap( PolygonOnSphere &polygon, PointForwardIter exterior_begin, PointForwardIter exterior_end, bool check_distinct_points)` | method | `void` | private | Generate a sequence of polygon segments from the exterior points in the range exterior\_begin / exterior\_end. |
| `generate_rings_and_swap( PolygonOnSphere &polygon, PointForwardIter exterior_begin, PointForwardIter exterior_end, PointCollectionForwardIter interior_rings_begin, PointCollectionForwardIter interior_rings_end, bool check_distinct_points)` | method | `void` | private | Generate a sequence of polygon segments from the exterior points in the range exterior\_begin / exterior\_end and a sequence of interior rings in the range interior\_rings\_begin / interior\_rings\_end (where each ring is a sequence of points). |
| `generate_ring( ring_type &ring, PointForwardIter begin, PointForwardIter end)` | method | `void` | private | Generate a ring from a sequence of points. |
| `s_min_num_ring_points` | field | `unsigned` | private | This is the minimum number of (distinct) ring points to be passed into the 'create' function (for each ring) to enable creation of closed, well-defined polygon rings. |
| `d_exterior_ring` | field | `ring_type` | private | The exterior ring of this polygon. |
| `d_interior_rings` | field | `ring_sequence_type` | private | The interior rings of this polygon (if any). |
| `d_cached_calculations` | field | `boost::intrusive_ptr<PolygonOnSphereImpl::CachedCalculations>` | private | Useful calculations on the polygon data. |

### `GPlatesMaths::InvalidPointsForPolygonConstructionError`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InvalidPointsForPolygonConstructionError( const GPlatesUtils::CallStack::Trace &exception_source, PolygonOnSphere::ConstructionParameterValidity cpv)` | constructor | `None` | public | Instantiate the exception. presumably describes why the points are invalid. |
| `~InvalidPointsForPolygonConstructionError()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_cpv` | field | `PolygonOnSphere::ConstructionParameterValidity` | private | — |
| `d_filename` | field | `char` | private | — |
| `d_line_num` | field | `int` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `build_and_cache_point_in_polygon_tester( const PolygonOnSphere &polygon, CachedCalculations &cached_calculations, bool high_speed)` | function | `void` | Build a point-in-polygon tester of medium or high (if high\_speed is true) speed and cache the result in cached\_calculations. |
| `is_close_to_polygon_ring( const PolygonOnSphere::ring_const_iterator &ring_begin, const PolygonOnSphere::ring_const_iterator &ring_end, const PointOnSphere &test_point, const AngularExtent &closeness_angular_extent_threshold, real_t &closest_closeness_so_far, boost::optional<PointOnSphere> &closest_point)` | function | `void` | — |
| `calculate_ring_arc_length( const PolygonOnSphere::ring_const_iterator &ring_begin, const PolygonOnSphere::ring_const_iterator &ring_end)` | function | `real_t` | — |
| `tessellate_ring( std::vector<PointOnSphere> &tessellated_ring_points, const PolygonOnSphere::ring_const_iterator &ring_begin, const PolygonOnSphere::ring_const_iterator &ring_end, const real_t &max_angular_extent)` | function | `void` | — |
| `s_min_num_ring_points` | variable | `unsigned` | — |
| `GPLATES_MATHS_POLYGONONSPHERE_H` | macro | `None` | — |
| `tessellate( const PolygonOnSphere &polygon, const real_t &max_angular_extent)` | function | `PolygonOnSphere::non_null_ptr_to_const_type` | Subdivides each segment (great circle arc) of a polygon and returns tessellated polygon. |

## Notes

**Index preconditions abort in debug builds.** The bounds checks on every indexed accessor go
through `GPlatesGlobal::Assert<PreconditionViolationError>`, which throws only when `GPLATES_DEBUG`
is undefined; in a debug build it calls `GPlatesGlobal::Abort`. A bad ring or vertex index is a
crash during development and an exception in release, so do not write a debug-build test that
expects to catch it.

**Ring invariants.** Every ring holds at least three arcs, and segment count equals vertex count.
`generate_ring` appends the wrap-around arc only if the last supplied point differs from the first
(or if exactly three points were supplied), so an already-closed input `[A,B,C,D,A]` produces four
segments, not five. Validation with the default `check_distinct_points = false` only counts points,
so a ring like `[A,B,A]` passes and yields a zero-length closing arc; if your code cannot cope with
degenerate segments, pass `true`.

**Const is not thread-safe.** The geometry data is immutable, but `d_cached_calculations` is
`mutable` and *every* derived-value accessor — arc length, area, orientation, centroids, bounding
circles, bounding trees, `is_point_in_polygon` — allocates or writes to it, with no locking. The
reference count in `GPlatesUtils::ReferenceCount` is atomic, so sharing the pointer across threads
is fine, but two threads calling apparently read-only members on the same `const PolygonOnSphere`
concurrently is a data race. `is_point_in_polygon` also increments a call counter on every call, so
it mutates even when it does no setup.

**No back-references from the cache.** The cached `PointInPolygon::Polygon` and every
`PolyGreatCircleArcBoundingTree` are deliberately constructed *without* a shared reference to the
polygon — the comments say so at each site — because the cache is owned by the polygon and a shared
reference would close a cycle and leak. Anything new you add to `CachedCalculations` must follow
the same rule.

**Proximity and containment are different questions.** `is_close_to` (and therefore
`test_proximity`, which merely delegates to it — see the FIXME) measures distance to the polygon
*outline*, exterior and interior rings alike, and says nothing about being inside. Conversely
`is_point_in_polygon` counts edge crossings from the antipodal centroid, so if an interior ring
crosses the exterior ring a point outside the exterior but inside the interior ring tests as
inside; the header notes this matches how filled polygons are rendered. `test_vertex_proximity`
only walks the *exterior* ring, and the index it reports in the `PolygonProximityHitDetail` is an
exterior-ring vertex index.

**Iterator lifetime and default construction.** `ConstIterator` keeps raw pointers to the polygon
and to the current ring vector, so it is invalidated by the polygon's destruction and must not
outlive it. A default-constructed iterator throws `UninitialisedIteratorException` on dereference
or comparison, but `increment`, `decrement` and `advance` silently no-op on it. Note also that
`end()` is defined as the end of the *last* ring with ring id equal to the interior ring count, so
comparisons rely on both the ring id and the within-ring iterator matching.

**Cost.** `number_of_segments()` and `number_of_vertices()` loop over the interior rings on every
call, and the indexed accessors (`get_segment`, `segment_iterator`, `vertex_iterator`, …) call them
for their precondition assert and then `std::advance` ring by ring — cheap for the common
single-ring polygon, but not free in an inner loop over a many-holed polygon. `get_orientation`
reuses a cached signed area if one is already present and otherwise runs
`PolygonOrientation::calculate_polygon_orientation` without producing a signed area, so the two
values are not always computed together.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 101 |
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 83 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 75 |
| [maths/GeometryDistance](GeometryDistance.md) | maths | 69 |
| [maths/SmallCircleBounds](SmallCircleBounds.md) | maths | 57 |
| [maths/DateLineWrapper](DateLineWrapper.md) | maths | 46 |
| [maths/PolygonMesh](PolygonMesh.md) | maths | 42 |
| [maths/GeometryIntersect](GeometryIntersect.md) | maths | 41 |
| [maths/PolylineIntersections](PolylineIntersections.md) | maths | 39 |
| [maths/PointInPolygon](PointInPolygon.md) | maths | 35 |
| [maths/SphericalArea](SphericalArea.md) | maths | 33 |
| [maths/Centroid](Centroid.md) | maths | 31 |
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 29 |
| [opengl/GLIntersectPrimitives](../opengl/GLIntersectPrimitives.md) | opengl | 28 |
| [maths/PolylineOnSphere](PolylineOnSphere.md) | maths | 26 |
| [maths/deprecated/PolylineIntersections_test](deprecated/PolylineIntersections_test.md) | maths | 26 |
| [file-io/GMTFormatGeometryExporter](../file-io/GMTFormatGeometryExporter.md) | file-io | 25 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 25 |
| [maths/PolygonOrientation](PolygonOrientation.md) | maths | 25 |
| [maths/Rotation](Rotation.md) | maths | 25 |

*... and 79 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/PolygonOnSphere.h
python scripts/gpq.py def GPlatesMaths::PolygonOnSphere --body
python scripts/gpq.py uses PolygonOnSphere --kind class
python scripts/gpq.py hier PolygonOnSphere
```

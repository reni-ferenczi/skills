# PolylineOnSphere

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 169 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/PolylineOnSphere.h` | C++ | 1146 |
| `src/maths/PolylineOnSphere.cc` | C++ | 455 |

## Overview

[[[PROSE overview unit=maths/PolylineOnSphere tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::PolylineOnSphereImpl::CachedCalculations`](#gplatesmathspolylineonsphereimplcachedcalculations) | struct | [`GPlatesUtils::ReferenceCount<CachedCalculations>`](../utils/ReferenceCount.md) | — | 0 | Cached results of calculations performed on the polyline geometry. |
| [`GPlatesMaths::PolylineOnSphere`](#gplatesmathspolylineonsphere) | class | [`GeometryOnSphere`](GeometryOnSphere.md) | — | 0 | Represents a polyline on the surface of a sphere. |
| [`GPlatesMaths::InvalidPointsForPolylineConstructionError`](#gplatesmathsinvalidpointsforpolylineconstructionerror) | class | [`GPlatesGlobal::PreconditionViolationError`](../global/PreconditionViolationError.md) | — | 0 | The exception thrown when an attempt is made to create a polyline using invalid points. |

## Members

### `GPlatesMaths::PolylineOnSphereImpl::CachedCalculations`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `arc_length` | field | `boost::optional<real_t>` | public | — |
| `centroid` | field | `boost::optional<UnitVector3D>` | public | — |
| `bounding_small_circle` | field | `boost::optional<BoundingSmallCircle>` | public | — |
| `polyline_bounding_tree` | field | `boost::optional<PolylineOnSphere::bounding_tree_type>` | public | — |

### `GPlatesMaths::PolylineOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<PolylineOnSphere>` | private | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<PolylineOnSphere\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const PolylineOnSphere>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const PolylineOnSphere\>. |
| `seq_type` | typedef | `std::vector<GreatCircleArc>` | public | The type of the sequence of great circle arcs. |
| `const_iterator` | typedef | `seq_type::const_iterator` | public | The type used to const\_iterate over the sequence of arcs. |
| `bounding_tree_type` | typedef | `PolyGreatCircleArcBoundingTree<const_iterator, true/*RequireRandomAccessIterator*/>` | public | Typedef for the bounding tree of great circle arcs in a polyline. |
| `VertexConstIterator` | class | `None` | public | This class enables const\_iteration over the vertices of a sequence of GreatCircleArc. |
| `vertex_const_iterator` | typedef | `VertexConstIterator<const_iterator>` | public | The type used to const\_iterate over the vertices. |
| `ConstructionParameterValidity` | enum | `None` | public | The possible return values from the construction-parameter validation function evaluate\_construction\_parameter\_validity. |
| `evaluate_construction_parameter_validity( PointForwardIter begin, PointForwardIter end, bool check_distinct_points = false)` | method | `ConstructionParameterValidity` | public | Evaluate the validity of the construction-parameters. |
| `evaluate_construction_parameter_validity( const C &coll, bool check_distinct_points = false)` | method | `ConstructionParameterValidity` | public | Evaluate the validity of the construction-parameters. coll should be a sequential STL container (list, vector, ...) of PointOnSphere. |
| `create( PointForwardIter begin, PointForwardIter end, bool check_distinct_points = false)` | method | `non_null_ptr_to_const_type` | public | Create a new PolylineOnSphere instance on the heap from the sequence of points delimited by the forward iterators begin and end and return an intrusive\_ptr which points to the newly-created instance. |
| `create( const C &coll, bool check_distinct_points = false)` | method | `non_null_ptr_to_const_type` | public | Create a new PolylineOnSphere instance on the heap from the sequence of points coll, and return an intrusive\_ptr which points to the newly-created instance. coll should be a sequential STL container (list, vector, ...) of PointOnSphere. |
| `~PolylineOnSphere()` | destructor | `None` | public | — |
| `test_proximity( const ProximityCriteria &criteria)` | method | `ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `test_vertex_proximity( const ProximityCriteria &criteria)` | method | `ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `accept_visitor( ConstGeometryOnSphereVisitor &visitor)` | method | `void` | public | Accept a ConstGeometryOnSphereVisitor instance. |
| `get_non_null_pointer()` | method | `non_null_ptr_to_const_type` | public | Return this instance as a non-null pointer. |
| `begin()` | method | `const_iterator` | public | Return the "begin" const\_iterator to iterate over the sequence of GreatCircleArc which defines this polyline. |
| `end()` | method | `const_iterator` | public | Return the "end" const\_iterator to iterate over the sequence of GreatCircleArc which defines this polyline. |
| `segment_iterator( unsigned int segment_index)` | method | `const_iterator` | public | Return the const\_iterator in this polyline at the specified segment index, so can iterate over GreatCircleArc starting at that segment. segment\_index can be one past the last segment, corresponding to end. |
| `number_of_segments()` | method | `unsigned int` | public | Return the number of segments in this polyline. |
| `vertex_begin()` | method | `vertex_const_iterator` | public | Return the "begin" vertex\_const\_iterator to iterate over the vertices of this polyline. |
| `vertex_end()` | method | `vertex_const_iterator` | public | Return the "end" vertex\_const\_iterator to iterate over the vertices of this polyline. |
| `vertex_iterator( unsigned int vertex_index)` | method | `vertex_const_iterator` | public | Return the vertex\_const\_iterator in this polyline at the specified vertex index. vertex\_index can be one past the last vertex, corresponding to vertex\_end. |
| `number_of_vertices()` | method | `unsigned int` | public | Return the number of vertices in this polyline. |
| `is_close_to( const PointOnSphere &test_point, const AngularExtent &closeness_angular_extent_threshold, real_t &closeness)` | method | `boost::optional<PointOnSphere>` | public | Evaluate whether test\_point is "close" to this polyline. |
| `operator==( const PolylineOnSphere &other)` | operator | `bool` | public | Equality operator compares great circle arc subsegments. |
| `operator!=( const PolylineOnSphere &other)` | operator | `bool` | public | Inequality operator. |
| `get_arc_length` | field | `real_t` | public | Returns the total arc-length of the sequence of GreatCirclArc which defines this polyline. |
| `get_centroid` | field | `UnitVector3D` | public | Returns the centroid of the edges of this polyline (see Centroid::calculate\_outline\_centroid). |
| `get_bounding_small_circle` | field | `BoundingSmallCircle` | public | Returns the small circle that bounds this polyline - the small circle centre is the same as calculated by get\_centroid. |
| `get_bounding_tree` | field | `bounding_tree_type` | public | Returns the small circle bounding tree over of great circle arc segments of this polyline. |
| `PolylineOnSphere()` | constructor | `None` | private | Create an empty PolylineOnSphere instance. |
| `evaluate_segment_endpoint_validity( const PointOnSphere &p1, const PointOnSphere &p2)` | method | `ConstructionParameterValidity` | private | Evaluate the validity of the points p1 and p2 for use in the creation of a polyline line-segment. |
| `generate_segments_and_swap( PolylineOnSphere &poly, PointForwardIter begin, PointForwardIter end, bool check_distinct_points)` | method | `void` | private | Generate a sequence of polyline segments from the sequence of points in the range begin / end, using the points to define the endpoints and vertices of the segments, then swap this new sequence of segments into the polyline poly, ... |
| `s_min_num_collection_points` | field | `unsigned` | private | This is the minimum number of (distinct) collection points to be passed into the 'create' function to enable creation of a closed, well-defined polyline. |
| `d_seq` | field | `seq_type` | private | This is the sequence of polyline segments. |
| `d_cached_calculations` | field | `boost::intrusive_ptr<PolylineOnSphereImpl::CachedCalculations>` | private | Useful calculations on the polyline data. |

### `GPlatesMaths::InvalidPointsForPolylineConstructionError`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InvalidPointsForPolylineConstructionError( const GPlatesUtils::CallStack::Trace &exception_source, PolylineOnSphere::ConstructionParameterValidity cpv)` | constructor | `None` | public | Instantiate the exception. presumably describes why the points are invalid. |
| `~InvalidPointsForPolylineConstructionError()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | FIXME: This would be better as a 'const std::string'. |
| `d_cpv` | field | `PolylineOnSphere::ConstructionParameterValidity` | private | — |
| `d_filename` | field | `char` | private | — |
| `d_line_num` | field | `int` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `s_min_num_collection_points` | variable | `unsigned` | — |
| `GPLATES_MATHS_POLYLINEONSPHERE_H` | macro | `None` | — |
| `tessellate( const PolylineOnSphere &polyline, const real_t &max_angular_extent)` | function | `PolylineOnSphere::non_null_ptr_to_const_type` | Subdivides each segment (great circle arc) of a polyline and returns tessellated polyline. |
| `polylines_are_directed_equivalent( const PolylineOnSphere &poly1, const PolylineOnSphere &poly2)` | function | `bool` | Determine whether the two polylines poly1 and poly2 are equivalent when the directedness of the polyline segments is taken into account. |
| `polylines_are_undirected_equivalent( const PolylineOnSphere &poly1, const PolylineOnSphere &poly2)` | function | `bool` | Determine whether the two polylines poly1 and poly2 are equivalent when the directedness of the polyline segments is ignored. |
| `concatenate_polylines( PolylineForwardIter begin, PolylineForwardIter end)` | function | `PolylineOnSphere::non_null_ptr_to_const_type` | Concatenates multiple polylines into a single polyline by joining the tail of one polyline to the head of the next, etc. |
| `concatenate_polylines( PolylineForwardIter polylines_begin, PolylineForwardIter polylines_end)` | function | `PolylineOnSphere::non_null_ptr_to_const_type` | — |

## Notes

[[[PROSE notes unit=maths/PolylineOnSphere tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 25 |
| [qt-widgets/CreateFeaturePropertiesPage](../qt-widgets/CreateFeaturePropertiesPage.md) | qt-widgets | 21 |
| [file-io/deprecated/GpmlOnePointFiveOutputVisitor](../file-io/deprecated/GpmlOnePointFiveOutputVisitor.md) | file-io | 19 |
| [file-io/OgrWriter](../file-io/OgrWriter.md) | file-io | 10 |
| [app-logic/ResolvedTopologicalGeometrySubSegment](../app-logic/ResolvedTopologicalGeometrySubSegment.md) | app-logic | 9 |
| [app-logic/ResolvedTopologicalSharedSubSegment](../app-logic/ResolvedTopologicalSharedSubSegment.md) | app-logic | 9 |
| [view-operations/RenderedColouredEdgeSurfaceMesh](../view-operations/RenderedColouredEdgeSurfaceMesh.md) | view-operations | 9 |
| [file-io/PlatesRotationFormatWriter](../file-io/PlatesRotationFormatWriter.md) | file-io | 7 |
| [file-io/GMTFormatFlowlineExport](../file-io/GMTFormatFlowlineExport.md) | file-io | 6 |
| [file-io/ReconstructedFlowlineExport](../file-io/ReconstructedFlowlineExport.md) | file-io | 6 |
| [file-io/ReconstructedMotionPathExport](../file-io/ReconstructedMotionPathExport.md) | file-io | 6 |
| [app-logic/ResolvedTopologicalLine](../app-logic/ResolvedTopologicalLine.md) | app-logic | 5 |
| [app-logic/GenerateVelocityDomainCitcoms](../app-logic/GenerateVelocityDomainCitcoms.md) | app-logic | 4 |
| [data-mining/deprecated/IsInRegionOfInterestVisitor](../data-mining/deprecated/IsInRegionOfInterestVisitor.md) | data-mining | 3 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 3 |
| [maths/PolylineEquivalencePredicates](PolylineEquivalencePredicates.md) | maths | 3 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 3 |
| [qt-widgets/EditEnumerationWidget](../qt-widgets/EditEnumerationWidget.md) | qt-widgets | 3 |
| [view-operations/AddPointGeometryOperation](../view-operations/AddPointGeometryOperation.md) | view-operations | 3 |
| [app-logic/ResolvedSubSegmentRangeInSection](../app-logic/ResolvedSubSegmentRangeInSection.md) | app-logic | 2 |

*... and 78 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/PolylineOnSphere.h
python scripts/gpq.py def GPlatesMaths::PolylineOnSphere --body
python scripts/gpq.py uses PolylineOnSphere --kind class
python scripts/gpq.py hier PolylineOnSphere
```

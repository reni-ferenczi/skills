# GeometryDistance

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 715 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/GeometryDistance.h` | C++ | 627 |
| `src/maths/GeometryDistance.cc` | C++ | 2077 |

## Overview

`GeometryDistance` is the single home for "how far apart are these two
geometries" queries between any pair of the four `GeometryOnSphere` derived
types (`PointOnSphere`, `MultiPointOnSphere`, `PolylineOnSphere`,
`PolygonOnSphere`). Rather than a distance method per class, every combination
is exposed as a free `minimum_distance` overload, plus one type-erased
overload that dispatches at runtime through the anonymous-namespace
`MinimumDistanceBetweenGeometryOnSpheres`, a `ConstGeometryOnSphereVisitor`
that resolves both arguments to their concrete types and forwards to the
matching typed overload.

Every overload can optionally report *where* the geometries are closest — the
closest `UnitVector3D` position on each geometry and the index of the
underlying point or segment (`PolylineOnSphere::get_segment()` /
`PolygonOnSphere::get_segment()`) it lies on — and can be given a
`minimum_distance_threshold` so callers uninterested in the exact value beyond
some cutoff can stop early; `AngularDistance::PI` in the result signals the
threshold was exceeded, in which case none of the optional outputs are
written. Polygon overloads additionally take a `..._interior_is_solid` flag
that makes anything overlapping the polygon's interior collapse to zero
distance, using the same odd-crossing point-in-polygon rule used elsewhere,
even when the exterior and interior rings intersect each other.

For the polyline/polygon-against-polyline/polygon overloads, the
implementation builds a `PolyGreatCircleArcBoundingTree` over each geometry's
segments and recurses pairwise over bounding-tree nodes
(`minimum_distance_between_bounding_tree_nodes_of_two_geometries`), pruning
subtrees whose bounds are already farther apart than the best distance found
so far (or the caller's threshold) instead of testing every segment pair
directly.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::(anonymous)::MinimumDistanceBetweenGeometryOnSpheres`](#gplatesmathsanonymousminimumdistancebetweengeometryonspheres) | class | [`ConstGeometryOnSphereVisitor`](ConstGeometryOnSphereVisitor.md) | — | 0 | Find the minimum distance between two derived GeometryOnSphere objects. |

## Members

### `GPlatesMaths::(anonymous)::MinimumDistanceBetweenGeometryOnSpheres`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MinimumDistanceBetweenGeometryOnSpheres( const GeometryOnSphere &second_geometry, bool geometry1_interior_is_solid, bool geometry2_interior_is_solid, AngularDistance &minimum_distance, const boost::optional<const AngularExtent &> &minimum_distance_threshold, const boost::optional< boost::tuple<UnitVector3D &/*geometry1 ...` | constructor | `None` | public | — |
| `visit_point_on_sphere( PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere1)` | method | `void` | public | — |
| `visit_multi_point_on_sphere( MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere1)` | method | `void` | public | — |
| `visit_polygon_on_sphere( PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere1)` | method | `void` | public | — |
| `visit_polyline_on_sphere( PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere1)` | method | `void` | public | — |
| `d_second_geometry` | field | `GeometryOnSphere` | private | — |
| `d_geometry1_interior_is_solid` | field | `bool` | private | — |
| `d_geometry2_interior_is_solid` | field | `bool` | private | — |
| `d_minimum_distance` | field | `AngularDistance` | private | — |
| `d_minimum_distance_threshold` | field | `boost::optional<const AngularExtent &>` | private | — |
| `d_closest_positions` | field | `boost::optional< boost::tuple<UnitVector3D &/*geometry1*/, UnitVector3D &/*geometry2*/> >` | private | — |
| `d_closest_indices` | field | `boost::optional< boost::tuple<unsigned int &/*geometry1*/, unsigned int &/*geometry2*/> >` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `minimum_distance_between_point_and_poly_geometry_bounding_tree_node( const PointOnSphere &point, const PolyGreatCircleArcBoundingTree<GreatCircleArcConstIteratorType> &polygeom_bounding_tree, const typename PolyGreatCircleArcBoundingTree<GreatCircleArcConstIteratorType>::node_type &polygeom_sub_tree_node, AngularDistan ...` | function | `void` | Calculate (and update) the minimum distance between a point and a polyline or polygon. |
| `minimum_distance_between_bounding_tree_nodes_of_two_geometries( const PolyGreatCircleArcBoundingTree<GreatCircleArcConstIterator1Type> &geometry1_bounding_tree, const typename PolyGreatCircleArcBoundingTree<GreatCircleArcConstIterator1Type>::node_type &geometry1_sub_tree_node, const PolyGreatCircleArcBoundingTree<Great ...` | function | `void` | Calculate (and update) the minimum distance between a bounding tree node of one polyline or polygon, and the bounding tree node of another polyline or polygon. |
| `minimum_distance_between_bounding_tree_node_of_geometry1_and_two_child_nodes_of_geometry2( const PolyGreatCircleArcBoundingTree<GreatCircleArcConstIterator1Type> &geometry1_bounding_tree, const typename PolyGreatCircleArcBoundingTree<GreatCircleArcConstIterator1Type>::node_type &geometry1_sub_tree_node, const PolyGreat ...` | function | `void` | Calculate (and update) the minimum distance between a bounding tree node of the first polyline or polygon, and two child bounding tree nodes of the second polyline or polygon. |
| `GPLATES_MATHS_GEOMETRYDISTANCE_H` | macro | `None` | — |
| `minimum_distance( const GeometryOnSphere &geometry1, const GeometryOnSphere &geometry2, bool geometry1_interior_is_solid = false, bool geometry2_interior_is_solid = false, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional< boost::tuple<UnitVector3D &/*geometry1*/, UnitVect ...` | function | `AngularDistance` | interior rings intersect each other. |
| `minimum_distance( const PointOnSphere &point1, const PointOnSphere &point2, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none)` | function | `AngularDistance` | Returns the minimum angular distance between two points. |
| `minimum_distance( const PointOnSphere &point, const MultiPointOnSphere &multipoint, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional<UnitVector3D &> closest_position_in_multipoint = boost::none, boost::optional<unsigned int &> closest_position_index_in_multipoint = boost: ...` | function | `AngularDistance` | Returns the minimum angular distance between a point and a multi-point. |
| `minimum_distance( const PointOnSphere &point, const PolylineOnSphere &polyline, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional<UnitVector3D &> closest_position_on_polyline = boost::none, boost::optional<unsigned int &> closest_segment_index_in_polyline = boost::none)` | function | `AngularDistance` | Returns the minimum angular distance between a point and a polyline. |
| `minimum_distance( const PointOnSphere &point, const PolygonOnSphere &polygon, bool polygon_interior_is_solid = false, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional<UnitVector3D &> closest_position_on_polygon_outline = boost::none, boost::optional<unsigned int &> closes ...` | function | `AngularDistance` | Returns the minimum angular distance between a point and a polygon. |
| `minimum_distance( const MultiPointOnSphere &multipoint, const PointOnSphere &point, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional<UnitVector3D &> closest_position_in_multipoint = boost::none, boost::optional<unsigned int &> closest_position_index_in_multipoint = boost: ...` | function | `AngularDistance` | Returns the minimum angular distance between a point and a multi-point. |
| `minimum_distance( const MultiPointOnSphere &multipoint1, const MultiPointOnSphere &multipoint2, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional< boost::tuple<UnitVector3D &/*multipoint1*/, UnitVector3D &/*multipoint2*/> > closest_positions = boost::none, boost::optional< ...` | function | `AngularDistance` | Returns the minimum angular distance between two multi-points. |
| `minimum_distance( const MultiPointOnSphere &multipoint, const PolylineOnSphere &polyline, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional< boost::tuple<UnitVector3D &/*multipoint*/, UnitVector3D &/*polyline*/> > closest_positions = boost::none, boost::optional< boost::tu ...` | function | `AngularDistance` | Returns the minimum angular distance between a multi-point and a polyline. |
| `minimum_distance( const MultiPointOnSphere &multipoint, const PolygonOnSphere &polygon, bool polygon_interior_is_solid = false, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional< boost::tuple<UnitVector3D &/*multipoint*/, UnitVector3D &/*polygon*/> > closest_positions = bo ...` | function | `AngularDistance` | Returns the minimum angular distance between a multi-point and a polygon. |
| `minimum_distance( const PolylineOnSphere &polyline, const PointOnSphere &point, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional<UnitVector3D &> closest_position_on_polyline = boost::none, boost::optional<unsigned int &> closest_segment_index_in_polyline = boost::none)` | function | `AngularDistance` | Returns the minimum angular distance between a point and a polyline. |
| `minimum_distance( const PolylineOnSphere &polyline, const MultiPointOnSphere &multipoint, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional< boost::tuple<UnitVector3D &/*polyline*/, UnitVector3D &/*multipoint*/> > closest_positions = boost::none, boost::optional< boost::tu ...` | function | `AngularDistance` | Returns the minimum angular distance between a multi-point and a polyline. |
| `minimum_distance( const PolylineOnSphere &polyline1, const PolylineOnSphere &polyline2, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional< boost::tuple<UnitVector3D &/*polyline1*/, UnitVector3D &/*polyline2*/> > closest_positions = boost::none, boost::optional< boost::tupl ...` | function | `AngularDistance` | Returns the minimum angular distance between two polylines. |
| `minimum_distance( const PolylineOnSphere &polyline, const PolygonOnSphere &polygon, bool polygon_interior_is_solid = false, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional< boost::tuple<UnitVector3D &/*polyline*/, UnitVector3D &/*polygon*/> > closest_positions = boost::n ...` | function | `AngularDistance` | If polygon\_interior\_is\_solid is true then anything overlapping the interior of polygon has a distance of zero (AngularDistance::ZERO), otherwise the distance to the polygon outline. |
| `minimum_distance( const PolygonOnSphere &polygon, const PointOnSphere &point, bool polygon_interior_is_solid = false, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional<UnitVector3D &> closest_position_on_polygon = boost::none, boost::optional<unsigned int &> closest_segmen ...` | function | `AngularDistance` | Returns the minimum angular distance between a point and a polygon. |
| `minimum_distance( const PolygonOnSphere &polygon, const MultiPointOnSphere &multipoint, bool polygon_interior_is_solid = false, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional< boost::tuple<UnitVector3D &/*polygon*/, UnitVector3D &/*multipoint*/> > closest_positions = bo ...` | function | `AngularDistance` | Returns the minimum angular distance between a multi-point and a polygon. |
| `minimum_distance( const PolygonOnSphere &polygon, const PolylineOnSphere &polyline, bool polygon_interior_is_solid = false, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional< boost::tuple<UnitVector3D &/*polygon*/, UnitVector3D &/*polyline*/> > closest_positions = boost::n ...` | function | `AngularDistance` | Returns the minimum angular distance between a polyline and a polygon. |
| `minimum_distance( const PolygonOnSphere &polygon1, const PolygonOnSphere &polygon2, bool polygon1_interior_is_solid = false, bool polygon2_interior_is_solid = false, boost::optional<const AngularExtent &> minimum_distance_threshold = boost::none, boost::optional< boost::tuple<UnitVector3D &/*polygon1*/, UnitVector3D &/ ...` | function | `AngularDistance` | If polygon1\_interior\_is\_solid is true and the boundary of polygon2 overlaps the interior of polygon1 then the returned distance will be zero, otherwise... if polygon2\_interior\_is\_solid is true and the boundary of polygon1 overlaps the ... |

## Notes

Closest positions and indices are only written when the returned distance is
below `minimum_distance_threshold` (if one was given) — code that reads those
optional outputs unconditionally after a threshold-exceeded result will read
stale or default-initialised values. Segment indices for polygons can refer
to an interior ring, not just the exterior ring, so callers must resolve them
through `PolygonOnSphere::get_segment()` rather than assuming a flat exterior
index space. When two polylines/polygons intersect, an arbitrary one of the
(possibly many) intersection points is returned as the "closest" point, not
necessarily a unique or stable choice across calls.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 5 |
| [maths/GeometryInterpolation](GeometryInterpolation.md) | maths | 5 |
| [app-logic/TopologyReconstruct](../app-logic/TopologyReconstruct.md) | app-logic | 2 |
| [data-mining/DataMiningUtils](../data-mining/DataMiningUtils.md) | data-mining | 2 |
| [data-mining/RegionOfInterestFilter](../data-mining/RegionOfInterestFilter.md) | data-mining | 2 |
| [maths/DateLineWrapper](DateLineWrapper.md) | maths | 2 |
| [maths/GeneratePoints](GeneratePoints.md) | maths | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/GeometryDistance.h
python scripts/gpq.py def GPlatesMaths::(anonymous)::MinimumDistanceBetweenGeometryOnSpheres --body
python scripts/gpq.py uses MinimumDistanceBetweenGeometryOnSpheres --kind class
python scripts/gpq.py hier MinimumDistanceBetweenGeometryOnSpheres
```

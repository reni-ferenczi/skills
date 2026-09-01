# DateLineWrapper

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 18 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/DateLineWrapper.h` | C++ | 1340 |
| `src/maths/DateLineWrapper.cc` | C++ | 3126 |

## Overview

This is the bridge from spherical geometry to the flat lat/lon world, and it
exists because that conversion is not a per-point operation. A polygon straddling
±180° converts point-by-point into something that draws as a horizontal smear
across a rectangular projection, so the geometry has to be *clipped* at the
dateline and reassembled into separate pieces before any point is emitted. The
two consumers are the 2D map views (`GPlatesGui::MapRenderedGeometryLayerPainter`)
and OGR/shapefile export (`GPlatesFileIO::OgrFeatureCollectionWriter` and
`OgrWriter`) — the header names ArcGIS as the original motivation.

The central idea, taken from Greiner and Hormann's polygon-clipping paper, is to
treat the dateline itself as an infinitesimally thin *polygon*: four corner
vertices at (±90, ±180) held in their own doubly-linked list, so that clipping a
geometry against the dateline is ordinary polygon-polygon clipping. Each
intersection is materialised as two `Vertex` copies — one spliced into the
geometry's vertex list, one sorted into the dateline list — cross-linked by
`intersection_neighbour`, and flagged as entering or exiting. Output then walks
the graph, hopping lists at every intersection and reversing direction as the
entry/exit flags demand, emitting one output polygon per unused exit vertex.
Polylines reuse the same `IntersectionGraph` but never build the dateline list:
they only need to be cut at intersections, not routed around the frame edge.

Three further things shape the interface. A non-zero central meridian is not a
special case in the algorithm — the geometry is rotated into a frame where that
meridian is longitude zero (`CentralMeridian` holds the rotation and its
inverse), wrapped there, and each output point rotated back and longitude-shifted.
Second, `possibly_wraps` is a cheap bounding-small-circle rejection that lets
callers skip the whole path, and it is worth using: it rotates only the small
circle's centre rather than the geometry. Third, the output is not just points.
Every emitted point carries flags saying whether it is original, tessellated, on
the dateline or on an original segment, plus an `InterpolateOriginalSegment`
giving the original segment index and an interpolation ratio along it — which is
what lets a caller carry per-vertex scalars through wrapping and tessellation.
Optional tessellation is folded into `LatLonLineGeometry::add_point` so that it
happens in the same pass.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::DateLineWrapper`](#gplatesmathsdatelinewrapper) | class | [`GPlatesUtils::ReferenceCount<DateLineWrapper>`](../utils/ReferenceCount.md) | — | 0 | Clips polyline/polygon geometries to the dateline (at -180, or +180, degrees longitude) and wraps them to the opposite longitude so that they display correctly over a (-180,180) rectangular (lat/lon) projection. |

## Members

### `GPlatesMaths::DateLineWrapper`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<DateLineWrapper>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const DateLineWrapper>` | public | — |
| `lat_lon_points_seq_type` | typedef | `std::vector<LatLonPoint>` | public | Typedef for a sequence of lat/lon points. |
| `LatLonPolygon` | class | `None` | public | A wrapped lat/lon polygon. |
| `LatLonPolyline` | class | `None` | public | A wrapped lat/lon polyline. |
| `LatLonMultiPoint` | class | `None` | public | A wrapped lat/lon multi-point. |
| `create( const double &central_meridian = 0.0)` | method | `non_null_ptr_type` | public | Creates a DateLineWrapper object. |
| `wrap_polygon( const PolygonOnSphere::non_null_ptr_to_const_type &input_polygon, std::vector<LatLonPolygon> &wrapped_polygons, boost::optional<AngularExtent> tessellate_threshold = boost::none, bool group_interior_with_exterior_rings = true)` | method | `void` | public | Clips the specified \*polygon\* to the dateline. |
| `wrap_polyline( const PolylineOnSphere::non_null_ptr_to_const_type &input_polyline, std::vector<LatLonPolyline> &wrapped_polylines, boost::optional<AngularExtent> tessellate_threshold = boost::none)` | method | `void` | public | Clips the specified \*polyline\* to the dateline. |
| `wrap_multi_point( const MultiPointOnSphere::non_null_ptr_to_const_type &input_multipoint)` | method | `LatLonMultiPoint` | public | Wraps points in the specified \*multi-point\* to the range \[-180 + central\_meridian, central\_meridian + 180\]. |
| `wrap_point( const PointOnSphere &input_point)` | method | `LatLonPoint` | public | Wraps the specified \*point\* to the range \[-180 + central\_meridian, central\_meridian + 180\]. |
| `possibly_wraps( const PolylineOnSphere::non_null_ptr_to_const_type &input_polyline)` | method | `bool` | public | Returns true if the specified polyline can possibly intersect the (central meridian shifted) dateline arc. |
| `possibly_wraps( const PolygonOnSphere::non_null_ptr_to_const_type &input_polygon)` | method | `bool` | public | Returns true if the specified polygon can possibly intersect the (central meridian shifted) dateline arc. |
| `CentralMeridian` | struct | `None` | private | For non-zero central meridians we need to rotate geometries into a dateline reference frame for clipping/wrapping and then reverse the rotation when outputting wrapped geometries. |
| `LatLonLineGeometry` | class | `None` | private | A possibly tessellated sequence of points (for a polyline/polygon). |
| `VertexClassification` | enum | `None` | private | Classification of a vertex based on its position relative to the dateline. |
| `IntersectionType` | enum | `None` | private | The type of intersection when intersecting a line segment of a geometry with the dateline. |
| `Vertex` | struct | `None` | private | A vertex in the graph. |
| `vertex_list_type` | typedef | `GPlatesUtils::SmartNodeLinkedList<Vertex>` | private | Typedef for a double-linked list of vertices. |
| `vertex_node_pool_type` | typedef | `boost::object_pool<vertex_list_type::Node>` | private | Typedef for a pool allocator of vertex list nodes. |
| `IntersectionGraph` | class | `None` | private | A graph of a geometry potentially intersecting the dateline. |
| `d_central_meridian` | field | `boost::optional<CentralMeridian>` | private | Used to transform input geometries to the dateline reference frame (for wrapping) and back again. |
| `DateLineWrapper( double central_meridian)` | constructor | `None` | private | Constructor. |
| `output_input_polyline( std::vector<LatLonPolyline> &wrapped_polylines, const PolylineOnSphere::non_null_ptr_to_const_type &input_polyline, const boost::optional<AngularExtent> &tessellate_threshold)` | method | `void` | private | Output the input polyline (it is entirely off the dateline). |
| `output_input_polygon( std::vector<LatLonPolygon> &wrapped_polygons, const PolygonOnSphere::non_null_ptr_to_const_type &input_polygon, const boost::optional<AngularExtent> &tessellate_threshold)` | method | `void` | private | Output the input polygon (it is entirely off the dateline). |
| `output_polyline_if_entirely_on_dateline( std::vector<LatLonPolyline> &wrapped_polylines, const PolylineOnSphere::non_null_ptr_to_const_type &input_polyline, const IntersectionGraph &graph, const boost::optional<AngularExtent> &tessellate_threshold_degrees)` | method | `void` | private | Output the input polyline if it is entirely \*on\* the dateline. |
| `output_non_intersecting_polygon_rings( std::vector<LatLonPolygon> &wrapped_polygons, const PolygonOnSphere::non_null_ptr_to_const_type &input_polygon, const IntersectionGraph &graph, const boost::optional<AngularExtent> &tessellate_threshold_degrees, bool group_interior_with_exterior_rings)` | method | `void` | private | Output the rings of the input polygon that do not intersect the dateline (if any). |
| `output_input_line_geometry( const VertexIteratorType vertex_begin, const VertexIteratorType vertex_end, LatLonLineGeometry &output_line_geometry, boost::optional<unsigned int> polygon_ring_index, bool on_dateline_arc, const boost::optional<AngularExtent> &tessellate_threshold_degrees)` | method | `void` | private | Output the non-intersecting input vertices of a polyline, or polygon ring. |
| `intersects_dateline( BoundingSmallCircle geometry_bounding_small_circle)` | method | `bool` | private | Returns true if the specified bounding small circle intersects the dateline arc. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `NORTH_POLE` | variable | `UnitVector3D` | Normal to sphere at the north pole. |
| `SOUTH_POLE` | variable | `UnitVector3D` | Normal to sphere at the south pole. |
| `FRONT_HALF_SPACE_NORMAL` | variable | `UnitVector3D` | Normal to the plane of the dateline great circle arc going from south pole to north pole. |
| `DATELINE_HEMISPHERE_NORMAL` | variable | `UnitVector3D` | Normal to plane dividing globe into hemisphere that contains dateline in front of it. |
| `EPSILON_THICK_PLANE_COSINE` | variable | `double` | Base epsilon calculations off a cosine since that usually has the least accuracy for small angles. '1 - 1e-9' in cosine corresponds to a displacement of about 4.5e-5 \[=sin(acos(1 - 1e-9))\]. |
| `EPSILON_THICK_PLANE_SINE` | variable | `double` | At the dateline we use a dot product and compare near zero. cos(90-epsilon) = sin(epsilon) |
| `does_line_segment_on_dateline_plane_cross_north_pole( const GreatCircleArc &line_segment, bool is_line_segment_start_point_on_dateline)` | function | `bool` | Returns true if the specified line segment crosses north pole, otherwise it crosses south pole. @pre line segment must lie on the 'thick' plane containing the dateline \*and\* the line segment must cross one of the poles. |
| `shift_dateline_frame_lat_lon_point_to_central_meridian_range( const LatLonPoint &lat_lon_point, const double &central_meridian)` | function | `LatLonPoint` | Shift a lat/lon in the \*dateline frame\* to have a longitude in the range... \[-180 + central\_meridian, central\_meridian + 180\] |
| `make_lat_lon_point_in_central_meridian_range( const PointOnSphere &point_on_sphere, const double &central_meridian)` | function | `LatLonPoint` | Convert lat/lon with longitude in the range \[-180 + central\_meridian, central\_meridian + 180\]. |
| `make_lat_lon_point_on_back_dateline_of_central_meridian( const PointOnSphere &point_on_sphere, const double &central_meridian)` | function | `LatLonPoint` | Convert a point on the dateline arc to lat/lon with longitude of 'central\_meridian - 180'. |
| `LISTS_SENTINEL` | variable | `GPlatesMaths::DateLineWrapper::Vertex` | Note that the value doesn't matter - it's just used when constructing list sentinel nodes. |
| `GPLATES_MATHS_DATELINEWRAPPER_H` | macro | `None` | — |

## Notes

- **A polygon covering both poles gets an arbitrary answer.** Entry/exit flags
  are seeded by a point-in-polygon test at the north pole, falling back to the
  south pole. If the input polygon intersects *both* poles neither test is usable
  and `generate_entry_exit_flags_for_dateline_polygon` just picks `true`, with a
  comment conceding the inside and outside may come out swapped. That choice also
  produces consecutive north/south pole vertices, which is why
  `add_tessellated_points` carries a special antipodal branch — `GreatCircleArc`
  cannot be built from antipodal endpoints.
- **Output polygon rings are not closed.** The header says so explicitly: the
  first and last points are generally different, and a renderer that treats the
  ring as a line string must append the first point itself.
- **The epsilons here are far coarser than the rest of `maths`.**
  `EPSILON_THICK_PLANE_COSINE` is `1 - 1e-9`, an angular tolerance around
  4.5e-5 radians — hundreds of metres on the Earth — versus
  `GPlatesMaths::EPSILON` at 1e-12. Most comparisons deliberately call `.dval()`
  to bypass `Real`'s own epsilon and use this larger one instead. Anything within
  that band of the dateline plane, or of either pole, is treated as *on* it.
- **Intersection vertices are snapped, not computed.** Their longitude is
  overwritten with exactly ±180 (or, at a pole, the latitude with ±90) and the
  `Vertex` is then constructed with no 3-D point, so its `PointOnSphere` is
  rebuilt from the snapped lat/lon. The snapping is the point — it is what makes
  the two halves meet the frame edge exactly — but it means the emitted position
  is not the exact intersection.
- **A geometry lying entirely along the dateline is a special output path.** The
  dateline "polygon" effectively excludes an epsilon-thin strip, so such a
  geometry is *outside* it and gets consumed by the clip, leaving an empty vertex
  list (`ENTIRELY_ON_DATELINE`). The original geometry is then emitted directly
  with every point forced to longitude `central_meridian - 180`, so it degenerates
  to a vertical line rather than a horizontal smear.
- **`group_interior_with_exterior_rings` is a cost/quality trade, not a
  formatting flag.** With it on, each non-intersecting ring is tested against
  every output exterior ring so far using `minimum_distance` over constructed
  `PolygonOnSphere`s — quadratic in the number of rings, and it builds a polygon
  per ring. Turn it off only for consumers that treat all rings alike, such as
  the stencil-buffer filled-polygon path named in the header.
- **Self-intersecting input is not handled.** A standing FIXME notes that
  polygons are not cleaned to the shapefile convention first, so an interior ring
  that meets both wrapped halves of the exterior ring cannot be assigned
  correctly.
- **Lifetime.** All vertex nodes come from a `boost::object_pool` owned by the
  `IntersectionGraph` and are freed only when the graph dies; `intersection_neighbour`
  is a raw `void *` into that pool (a `void *` to break a cyclic type dependency),
  valid only for the graph's lifetime. `LatLonPolygon` and `LatLonPolyline`, by
  contrast, are copyable handles over `boost::shared_ptr<LatLonLineGeometry>`, so
  they outlive the graph and copies share their points.
- **Threading.** A `DateLineWrapper` instance holds only the central meridian and
  all wrap methods are `const`, building a fresh graph per call, so instances are
  cheap to share. The unsafe part is the *input*: `possibly_wraps` calls
  `get_bounding_small_circle()`, which lazily populates a mutable cache inside the
  geometry, so wrapping the same geometry from two threads is not safe.
- `possibly_wraps` returning true does not mean the geometry wraps; false does
  mean it does not.
- The constructor silently wraps a central meridian outside [-180, 180] back into
  range, so output longitudes stay within `LatLonPoint`'s valid [-360, 360].

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 140 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 112 |
| [file-io/OgrWriter](../file-io/OgrWriter.md) | file-io | 90 |
| [file-io/OgrGeometryExporter](../file-io/OgrGeometryExporter.md) | file-io | 9 |
| [app-logic/ResolvedTriangulationUtils](../app-logic/ResolvedTriangulationUtils.md) | app-logic | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/DateLineWrapper.h
python scripts/gpq.py def GPlatesMaths::DateLineWrapper --body
python scripts/gpq.py uses DateLineWrapper --kind class
python scripts/gpq.py hier DateLineWrapper
```

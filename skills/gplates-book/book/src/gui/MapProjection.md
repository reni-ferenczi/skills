# MapProjection

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 262 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/MapProjection.h` | C++ | 432 |
| `src/gui/MapProjection.cc` | C++ | 828 |

## Overview

`MapProjection` is GPlates' wrapper around the PROJ library, and the single point
of truth for the 2-D map view's coordinate system. It converts between geographic
`LatLonPoint` / `PointOnSphere` and a 2-D map space expressed as `QPointF`, and
everything that draws or hit-tests the map goes through it — the layer painters,
`MapGrid` and `MapBackground`, the OpenGL cube-mesh generators, `GLLight`, and the
canvas tools that need to turn a scene position back into a location. It is
reference-counted (`GPlatesUtils::ReferenceCount`) precisely because it is shared
that widely; the projection settings themselves are chosen in
`SetProjectionDialog` / `ProjectionControlWidget` and carried by
`ViewportProjection`.

Rather than configuring PROJ fully and trusting it, this class deliberately keeps
several responsibilities on the GPlates side. The PROJ object is always created
with `lon_0=0.0`, and the central meridian is applied by hand — subtracted from
longitude and wrapped back into [-180, 180] before projecting, added back after
inverting — because older PROJ versions misbehaved with a non-zero central
meridian. The Rectangular projection bypasses PROJ entirely and is an identity map
from degrees to map units, because PROJ treats `latlong` as a special case whose
units varied across versions. The remaining projections come out of PROJ in
metres, so each row of the file-local `projection_table` carries a `scaling_factor`
that brings them roughly into the same degree-scaled units as Rectangular. On top
of that the code carries three PROJ dialects at once: a `GPLATES_USING_PROJ4`
compile-time branch, and a runtime `d_proj_info.major == 5` test, mostly because
PROJ 4 and 5 want radians while PROJ 6+ accepts degrees for `latlong`.

The most interesting design decision is that the map boundary is not described
analytically anywhere. Latitude is clamped just inside the poles and longitude
wrapped in `forward_transform()`, and that clamping *is* the definition of the map
edge. `inverse_transform()` therefore validates itself: it inverts, then forward
transforms the result and rejects the point unless the round trip lands back where
it started within `CHECK_FORWARD_TRANFORM_MAP_SPACE_DELTA_THRESHOLD`. Without this
the Mercator inverse cheerfully returns plausible longitudes for points far off
the left or right of the map. `is_inside_map_boundary()` is nothing more than
"did `inverse_transform()` succeed", `get_map_boundary_position()` bisects along a
segment using that predicate to find the edge crossing (valid because the boundary
is convex, so the segment crosses once), and `get_map_bounding_radius()` samples
eight extremal lat/lon points and caches the largest distance from the origin —
the origin being wherever (0, central meridian) lands.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::MapProjectionParameters`](#anonymousmapprojectionparameters) | struct | — | — | 0 | — |
| [`GPlatesGui::MapProjection`](#gplatesguimapprojection) | class | [`GPlatesUtils::ReferenceCount<MapProjection>`](../utils/ReferenceCount.md) | — | 0 | Projects latitude/longitude to/from various map projections. |
| [`GPlatesGui::MapProjectionSettings`](#gplatesguimapprojectionsettings) | class | `boost::equality_comparable<MapProjectionSettings>` | — | 0 | Projection settings used to determine if two map projections will generate the same projection results. |

## Members

### `(anonymous)::MapProjectionParameters`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `projection_name` | field | `GPlatesGui::MapProjection::Type` | public | — |
| `label_name` | field | `char` | public | — |
| `proj_name` | field | `char` | public | — |
| `proj_ellipse` | field | `char` | public | — |
| `scaling_factor` | field | `double` | public | — |

### `GPlatesGui::MapProjection`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<MapProjection>` | public | A convenience typedef for a shared pointer to a non-const MapProjection. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const MapProjection>` | public | A convenience typedef for a shared pointer to a const MapProjection. |
| `Type` | enum | `None` | public | Make the first enum Orthographic (even though we don't implement that as a map projection), so that we'll match up better with the combo-box indices, which will use the zeroth entry for the 3D Orthographic (Globe) view. |
| `get_display_name( Type projection_type)` | method | `char` | public | Return a suitable label naming the specified projection type. |
| `create()` | method | `non_null_ptr_type` | public | Creates a MapProjection object with no map projection setting. |
| `create( Type projection_type)` | method | `non_null_ptr_type` | public | Creates a MapProjection object with the specified map projection and zero central meridian. |
| `create( const MapProjectionSettings &projection_settings)` | method | `non_null_ptr_type` | public | Creates a MapProjection object with the specified map projection type and central meridian. |
| `~MapProjection()` | destructor | `None` | public | — |
| `get_projection_settings()` | method | `MapProjectionSettings` | public | Returns the projection settings of this map projection. |
| `set_projection_type( Type projection_type)` | method | `void` | public | Change the projection to that referred to by projection\_type. |
| `projection_type()` | method | `Type` | public | Get the projection type. |
| `set_central_meridian( const double &central_meridian_)` | method | `void` | public | Set the central meridian. |
| `central_meridian()` | method | `double` | public | Get the central meridian. |
| `forward_transform( const GPlatesMaths::PointOnSphere &point_on_sphere)` | method | `QPointF` | public | Transforms the point on sphere to cartesian coordinates (x,y) according to the current state of the projection. |
| `forward_transform( const GPlatesMaths::LatLonPoint &lat_lon_point)` | method | `QPointF` | public | Transforms the lat-lon point to cartesian coordinates (x,y) according to the current state of the projection. |
| `forward_transform( double &longitude, double &latitude)` | method | `void` | public | Transform the longitude and latitude to cartesian coordinates according to the current state of the projection. |
| `inverse_transform( const QPointF &map_point)` | method | `boost::optional<GPlatesMaths::LatLonPoint>` | public | Transform cartesian (x,y) coordinates to a LatLonPoint according to the current state of the projection. |
| `inverse_transform( double &x, double &y)` | method | `bool` | public | Transform cartesian (x,y) coordinates to longitude and latitude according to the current state of the projection. |
| `is_inside_map_boundary( const QPointF &map_point)` | method | `bool` | public | Returns true if specified point is inside the map projection boundary. |
| `get_map_boundary_position( const QPointF &map_point_inside_boundary, const QPointF &map_point_outside_boundary, double bisection_iteration_threshold_ratio = 1e-6/*equivalent to roughly 1 arc second on map*/)` | method | `QPointF` | public | Return the map position near (but just inside to within a small tolerance) the map boundary given two map positions (one inside and one outside map boundary). |
| `get_map_bounding_radius()` | method | `double` | public | Return the radius of the circle/sphere that bounds the map (including a very small numerical tolerance). |
| `CLAMP_LATITUDE_NEAR_POLES_EPSILON` | field | `double` | public | The Proj library has issues with the Mercator projection at the poles (ie, latitudes -90 and 90). |
| `MIN_LATITUDE` | field | `double` | public | — |
| `MAX_LATITUDE` | field | `double` | public | — |
| `d_projection` | field | `projPJ` | private | The proj4 projection. |
| `d_latlon_projection` | field | `projPJ` | private | A proj4 latlon projection. |
| `d_scale` | field | `double` | private | The scale factor for the projection. |
| `d_projection_type` | field | `Type` | private | An integer representing the current projection. |
| `d_central_meridian` | field | `double` | private | The central meridian for the projection. |
| `d_cached_bounding_radius` | field | `boost::optional<double>` | private | Radius of the circle/sphere that bounds the map (including a very small numerical tolerance). |
| `MapProjection()` | constructor | `None` | private | — |
| `MapProjection( Type projection_type)` | constructor | `None` | private | — |
| `MapProjection( const MapProjectionSettings &projection_settings)` | constructor | `None` | private | — |
| `forward_proj_transform( double longitude, double latitude, double &x, double &y)` | method | `void` | private | Ask the Proj library to forward transform from (longitude, latitude) in degrees to map projection space. |
| `inverse_proj_transform( double x, double y, double &longitude, double &latitude)` | method | `bool` | private | Ask the Proj library to inverse transform from map projection space (x, y) back to (longitude, latitude) in degrees. |
| `check_forward_transform( const double &inverted_x, const double &inverted_y, const double &x, const double &y)` | method | `bool` | private | Check that the inverted (x, y), which are (longitude, latitude) coordinates, forward transform to the specified (x, y) within a numerical tolerance. |

### `GPlatesGui::MapProjectionSettings`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MapProjectionSettings( MapProjection::Type projection_type_, const double &central_meridian_)` | constructor | `None` | public | — |
| `get_projection_type()` | method | `MapProjection::Type` | public | — |
| `set_projection_type( MapProjection::Type projection_type_)` | method | `void` | public | — |
| `get_central_meridian()` | method | `double` | public | — |
| `set_central_meridian( const double &central_meridian_)` | method | `void` | public | — |
| `d_projection_type` | field | `MapProjection::Type` | private | The projection type. |
| `d_central_meridian` | field | `double` | private | The central meridian for the projection. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `MIN_SCALE_FACTOR` | variable | `double` | — |
| `CHECK_FORWARD_TRANFORM_MAP_SPACE_DELTA_THRESHOLD` | variable | `double` | The distance threshold in map projected space (after scaling) for comparing original (x, y) with inverted and forward transformed (x, y). |
| `projection_table` | variable | `MapProjectionParameters` | — |
| `get_length( const QPointF &point)` | function | `double` | Return the length of the specified QPointF. |
| `GPLATES_GUI_MAPPROJECTION_H` | macro | `None` | — |

## Notes

**`ORTHOGRAPHIC` is not a projection, and an object set to it silently does
nothing.** The enum starts at `ORTHOGRAPHIC = 0` only so its values line up with
the projection combo box, whose zeroth entry is the 3-D globe.
`set_projection_type(ORTHOGRAPHIC)` returns before creating any PROJ object, so
`forward_transform()` returns its input unchanged and `inverse_transform()`
returns `boost::none` / false. The no-argument `create()` leaves the object in
exactly that state. The enum order must also stay in step with
`projection_table`, which `get_display_name()` indexes directly with no bounds
check.

**Every transform is far more expensive than it looks.** `inverse_transform()`
runs a full `forward_transform()` for its round-trip validation, so it costs at
least two PROJ calls. `is_inside_map_boundary()` is a full inverse transform. And
`get_map_boundary_position()` bisects until the interval falls below
`bisection_iteration_threshold_ratio` (default 1e-6) times the bounding radius,
calling `is_inside_map_boundary()` on every iteration — roughly twenty inverse
transforms per call. None of this is suitable per-vertex in a render loop.

**Error handling is asymmetric.** A failed inverse is reported by return value,
but the forward path *throws*: `ProjectionException` from `set_projection_type()`
when PROJ initialisation fails, and again from `forward_proj_transform()` if PROJ
returns `HUGE_VAL`. Since the constructors call `set_projection_type()`, `create()`
can throw. `get_map_boundary_position()` additionally asserts
(`PreconditionViolationError`) that the caller really did pass one inside and one
outside point.

**Mutating a shared projection changes it for everyone.** The object is
reference-counted and handed around widely, yet `set_projection_type()` and
`set_central_meridian()` are non-const. Most clients therefore hold
`non_null_ptr_to_const_type`. Note also that `set_central_meridian()` is not a
cheap parameter tweak: it re-enters `set_projection_type()`, which destroys and
recreates the PROJ object and invalidates the cached bounding radius.

**`d_cached_bounding_radius` is `mutable` and lazily filled by a `const` method**,
so `get_map_bounding_radius()` is not safe to call concurrently on one instance
even though it looks like a read.

**`MapProjectionSettings` is the comparison key, not a configuration struct.** Two
`MapProjection`s produce identical results iff their settings compare equal, which
is how callers decide whether cached projected geometry can be reused. It compares
the central meridian with `are_almost_exactly_equal`, so it is an exact-value
comparison, not a tolerance. It sits outside `MapProjection` rather than nested
because the injected `friend operator==` caused compile problems on some systems.

**The clamping epsilon has visible consequences.**
`CLAMP_LATITUDE_NEAR_POLES_EPSILON` is 1e-5, applied to every projection for
consistency even though only Mercator needs it. Because Mercator's y goes to
infinity at the pole, this constant sets the *height* of the Mercator map — the
code notes that changing it from 1e-3 to 1e-5 alters the range noticeably. There
is a second, less obvious dependency: the comment in `forward_transform()` warns
that global grid-line-registered raster export in the Rectangular projection
relies on the extents being exactly [-90, 90] and [-180, 180] after subtracting
the central meridian, so changes to the wrapping and clamping code there need to
be checked against raster export.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/MapRenderedGeometryLayerPainter](MapRenderedGeometryLayerPainter.md) | gui | 35 |
| [qt-widgets/SetProjectionDialog](../qt-widgets/SetProjectionDialog.md) | qt-widgets | 24 |
| [qt-widgets/ProjectionControlWidget](../qt-widgets/ProjectionControlWidget.md) | qt-widgets | 21 |
| [gui/MapBackground](MapBackground.md) | gui | 20 |
| [gui/Map](Map.md) | gui | 17 |
| [gui/MapGrid](MapGrid.md) | gui | 17 |
| [opengl/GLMultiResolutionMapCubeMesh](../opengl/GLMultiResolutionMapCubeMesh.md) | opengl | 15 |
| [opengl/GLLight](../opengl/GLLight.md) | opengl | 13 |
| [gui/ExportRasterAnimationStrategy](ExportRasterAnimationStrategy.md) | gui | 12 |
| [gui/LayerPainter](LayerPainter.md) | gui | 10 |
| [gui/ViewportProjection](ViewportProjection.md) | gui | 9 |
| [opengl/GLMapCubeMeshGenerator](../opengl/GLMapCubeMeshGenerator.md) | opengl | 9 |
| [qt-widgets/MapView](../qt-widgets/MapView.md) | qt-widgets | 7 |
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 5 |
| [qt-widgets/GlobeAndMapWidget](../qt-widgets/GlobeAndMapWidget.md) | qt-widgets | 5 |
| [view-operations/MovePoleOperation](../view-operations/MovePoleOperation.md) | view-operations | 5 |
| [gui/Dialogs](Dialogs.md) | gui | 4 |
| [qt-widgets/ReconstructionViewWidget](../qt-widgets/ReconstructionViewWidget.md) | qt-widgets | 4 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](../opengl/GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 3 |
| [qt-widgets/EditAgeWidget](../qt-widgets/EditAgeWidget.md) | qt-widgets | 3 |

*... and 5 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/MapProjection.h
python scripts/gpq.py def GPlatesGui::MapProjection --body
python scripts/gpq.py uses MapProjection --kind class
python scripts/gpq.py hier MapProjection
```

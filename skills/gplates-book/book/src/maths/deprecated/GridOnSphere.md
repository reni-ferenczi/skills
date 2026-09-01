# GridOnSphere

[Book TOC](../../../TOC.md) · [maths](../../../components/maths.md) · cluster Community 871 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/deprecated/GridOnSphere.h` | C++ | 215 |
| `src/maths/deprecated/GridOnSphere.cc` | C++ | 315 |

## Overview

A parametric representation of a rectangular grid on a sphere's surface. Rather than storing grid points directly, `GridOnSphere` stores the grid's geometry using a `SmallCircle` (defining lines of latitude), a `GreatCircle` (defining lines of longitude), an origin point, and angular deltas. This allows efficient storage and manipulation of large grids in raster operations. The class encodes the relationship between the small circle and great circle (they must intersect perpendicularly at the origin) as a class invariant, enforced on construction. It is used by raster I/O operations in `GPlatesFileIO` to describe grid-based data sources.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::GridOnSphere`](#gplatesmathsgridonsphere) | class | — | — | 0 | Represents a grid of points on the surface of a sphere. |

## Members

### `GPlatesMaths::GridOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Create(const PointOnSphere &origin, const PointOnSphere &next_along_lat, const PointOnSphere &next_along_lon)` | method | `GridOnSphere` | public | Call this "factory method" to create a GridOnSphere instance from three grid-points. |
| `GridOnSphere(const SmallCircle &line_of_lat, const GreatCircle &line_of_lon, const PointOnSphere &orig, const real_t &delta_along_lat, const real_t &delta_along_lon)` | constructor | `None` | public | Create a GridOnSphere instance, passing it all of its member data at once. |
| `lineOfLat()` | method | `SmallCircle` | public | — |
| `lineOfLon()` | method | `GreatCircle` | public | — |
| `origin()` | method | `PointOnSphere` | public | — |
| `deltaAlongLat()` | method | `real_t` | public | — |
| `deltaAlongLon()` | method | `real_t` | public | — |
| `resolve(index_t x, index_t y)` | method | `PointOnSphere` | public | Return the point-on-sphere corresponding to the grid indices x and y. |
| `AssertInvariantHolds()` | method | `void` | protected | Assert the class invariant: that the great circle is perpendicular to the small circle, and the origin lies at their intersection. |
| `_line_of_lat` | field | `SmallCircle` | private | — |
| `_line_of_lon` | field | `GreatCircle` | private | — |
| `_origin` | field | `PointOnSphere` | private | — |
| `_delta_along_lat` | field | `real_t` | private | Angular delta along the line of lat |
| `_delta_along_lon` | field | `real_t` | private | Angular delta along the line of lon |
| `EnsureValidOrigin(const PointOnSphere &o)` | method | `void` | private | Ensure the origin of the grid does not lie on either the North or South pole. |
| `calcDeltaAlongLat(const UnitVector3D &orig, const UnitVector3D &next, const UnitVector3D &north)` | method | `real_t` | private | Given the unit-vector of the origin of the grid, the unit-vector of the the next point along the line-of-latitude from the origin, and the unit-vector of the North pole, calculate the angular delta (in radians) from the origin to the next ... |
| `calcDelta(const UnitVector3D &orig, const UnitVector3D &next, const UnitVector3D &axis)` | method | `real_t` | private | Given two unit-vectors orig and next, as well as the unit-vector of an axis, calculate the angular delta (in radians) about the axis from orig to next. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `rotate_point_about_axis( const GPlatesMaths::PointOnSphere &p, const GPlatesMaths::UnitVector3D &rot_axis, const GPlatesMaths::real_t &rot_angle)` | function | `GPlatesMaths::PointOnSphere` | — |
| `_GPLATES_MATHS_GRIDONSPHERE_H_` | macro | `None` | — |

## Notes

The class enforces a strict invariant: the great circle (longitude) must be perpendicular to the small circle (latitude), and the origin must lie at their intersection. Violating this invariant throws `ViolatedClassInvariantException`. Additionally, the origin cannot be placed at either pole (North or South), which would make the latitude lines undefined; the factory method `Create()` performs extensive validation and throws `InvalidGridException` if grid points do not lie on the expected lines. Grid points are computed on demand via `resolve()` by rotation rather than direct lookup, avoiding the singularities and discontinuities of the lat/lon coordinate system.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/deprecated/NetCDFWriter](../../file-io/deprecated/NetCDFWriter.md) | file-io | 2 |
| [file-io/GpmlOutputVisitor](../../file-io/GpmlOutputVisitor.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/deprecated/GridOnSphere.h
python scripts/gpq.py def GPlatesMaths::GridOnSphere --body
python scripts/gpq.py uses GridOnSphere --kind class
python scripts/gpq.py hier GridOnSphere
```

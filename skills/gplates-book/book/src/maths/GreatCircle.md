# GreatCircle

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1536 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/GreatCircle.h` | C++ | 168 |
| `src/maths/GreatCircle.cc` | C++ | 120 |

## Overview

`GreatCircle` represents a whole great circle (not just an arc of one) as its
axis: the `UnitVector3D` normal to the plane through the sphere's centre and
the circle. It is a much lighter-weight type than `GreatCircleArc` — no
endpoints, no arc-specific machinery — used where code only cares about the
circle itself, such as `contains()` (a point lies on the circle iff it is
perpendicular to the axis), building a great-circle grid line
(`gui/SphericalGrid`), or comparing whether two independently-computed circles
coincide (`are_equivalent`, via `collinear` on the two axes rather than
comparing points).

The free `tessellate()` function subdivides a whole great circle into
uniformly-spaced points at most `max_segment_angular_extent` radians apart,
starting from an arbitrary point on the circle (`generate_perpendicular` of
the axis) and rotating around the axis; it appends only the distinct points,
leaving the caller to close the loop explicitly since the last point coincides
with the first.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::GreatCircle`](#gplatesmathsgreatcircle) | class | — | — | 0 | A great circle of a unit sphere. |

## Members

### `GPlatesMaths::GreatCircle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GreatCircle( const UnitVector3D &axis)` | constructor | `None` | public | Create a great circle, given its axis. |
| `GreatCircle( const PointOnSphere &p1, const PointOnSphere &p2)` | constructor | `None` | public | Create a great circle, given two points on it. |
| `contains( const PointOnSphere &pt)` | method | `bool` | public | Evaluate whether the point pt lies on this great circle. |
| `intersection(const GreatCircle &other)` | method | `UnitVector3D` | public | Computes one intersection point of this GreatCircle with another. |
| `calc_normal(const UnitVector3D &u1, const UnitVector3D &u2)` | method | `UnitVector3D` | private | Given two unit vectors, v1 and v2, calculate the normal of the great circle they define. |
| `d_axis` | field | `UnitVector3D` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_GREATCIRCLE_H` | macro | `None` | — |
| `operator-(const GreatCircle &c)` | operator | `GreatCircle` | — |
| `tessellate( std::vector<PointOnSphere> &tessellation_points, const GreatCircle &great_circle, const real_t &max_segment_angular_extent)` | function | `void` | Uniformly subdivides a great circle into smaller great circle arcs and appends the sequence of subdivided points to tessellation\_points. |
| `are_equivalent(const GreatCircle &a, const GreatCircle &b)` | function | `bool` | — |

## Notes

The two-point constructor throws `IndeterminateResultException` if the points
are coincident or antipodal (collinear position vectors give a zero-magnitude
cross product, so no unique great circle exists through them). The
`intersection()` member listed in the table is compiled out (`#if 0` in the
header) and has no implementation — it does not actually exist in the built
class despite appearing declared.

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/deprecated/GridOnSphere](deprecated/GridOnSphere.md) | maths | 9 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 8 |
| [maths/SmallCircle](SmallCircle.md) | maths | 6 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 4 |
| [view-operations/RenderedEllipse](../view-operations/RenderedEllipse.md) | view-operations | 4 |
| [gui/SphericalGrid](../gui/SphericalGrid.md) | gui | 2 |
| [maths/EllipseGenerator](EllipseGenerator.md) | maths | 1 |
| [maths/FiniteRotation](FiniteRotation.md) | maths | 1 |
| [maths/SmallCircleArc](SmallCircleArc.md) | maths | 1 |
| [view-operations/RenderedGeometryFactory](../view-operations/RenderedGeometryFactory.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/GreatCircle.h
python scripts/gpq.py def GPlatesMaths::GreatCircle --body
python scripts/gpq.py uses GreatCircle --kind class
python scripts/gpq.py hier GreatCircle
```

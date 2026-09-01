# GreatCircle

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1536 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/GreatCircle.h` | C++ | 168 |
| `src/maths/GreatCircle.cc` | C++ | 120 |

## Overview

[[[PROSE overview unit=maths/GreatCircle tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/GreatCircle tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

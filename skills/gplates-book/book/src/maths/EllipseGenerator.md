# EllipseGenerator

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 19 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/EllipseGenerator.h` | C++ | 86 |
| `src/maths/EllipseGenerator.cc` | C++ | 120 |

## Overview

[[[PROSE overview unit=maths/EllipseGenerator tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::EllipseGenerator`](#gplatesmathsellipsegenerator) | class | `boost::noncopyable` | — | 0 | This class can be used to obtain unit vector representations of points on an ellipse as a function of the angle from the semi-major axis. |

## Members

### `GPlatesMaths::EllipseGenerator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EllipseGenerator( const PointOnSphere &centre, const Real &semi_major_axis_radians, const Real &semi_minor_axis_radians, const GreatCircle &axis)` | constructor | `None` | public | — |
| `get_point_on_ellipse( double angle_from_semi_major_axis)` | method | `UnitVector3D` | public | — |
| `d_rotation` | field | `Rotation` | private | The rotation required to transform a point on the ellipse, defined in a tangent plane to the north pole, to the desired location and orientation on the sphere. |
| `d_semi_major_axis` | field | `double` | private | Semi major axis of the ellipse as defined in the tangent plane to the north pole. |
| `d_semi_minor_axis` | field | `double` | private | Semi minor axis of the ellipse as defined in the tangent plane to the north pole. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_rotation_angle( const GPlatesMaths::PointOnSphere &u1, const GPlatesMaths::PointOnSphere &u2, const GPlatesMaths::PointOnSphere &pivot)` | function | `GPlatesMaths::Real` | — |
| `GPLATES_MATHS_ELLIPSEGENERATOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/EllipseGenerator tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 31 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/EllipseGenerator.h
python scripts/gpq.py def GPlatesMaths::EllipseGenerator --body
python scripts/gpq.py uses EllipseGenerator --kind class
python scripts/gpq.py hier EllipseGenerator
```

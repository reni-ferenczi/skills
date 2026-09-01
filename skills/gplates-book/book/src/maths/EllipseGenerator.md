# EllipseGenerator

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 19 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/EllipseGenerator.h` | C++ | 86 |
| `src/maths/EllipseGenerator.cc` | C++ | 120 |

## Overview

Generates points on an elliptical small-circle-like curve on the sphere,
given a centre, semi-major/semi-minor axis lengths (in radians of arc), and a
`GreatCircle` fixing the orientation of the semi-major axis. It exists so
callers such as the globe and map painters (`GlobeRenderedGeometryLayerPainter`,
`MapRenderedGeometryLayerPainter`) can render error ellipses by sampling
`get_point_on_ellipse` at a sequence of angles rather than working out the
spherical geometry themselves.

Internally the ellipse is defined and sampled in a tangent plane touching the
north pole, with its semi-major axis along the plane's x-axis, and a single
`Rotation` (`d_rotation`) computed once in the constructor carries every
sampled point from that tangent-plane ellipse to the requested centre and
orientation on the sphere. Deriving that rotation takes several intermediate
rotations, worked out step by step and left partly acknowledged in the source
as more complex than necessary; the free helper `get_rotation_angle` (file
scope in the `.cc`, not part of the public interface despite appearing in the
index) computes the signed angle between two points as seen from a pivot,
used to correct the ellipse's twist about its centre.

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

`get_point_on_ellipse` samples the tangent-plane ellipse and then normalises
the result onto the sphere, so the returned points are evenly spaced in the
tangent-plane parametrisation, not in true arc length or angle as measured on
the sphere — adequate for rendering but not for area or arc-length
calculations. The class is `boost::noncopyable`; each instance is tied to the
one ellipse it was constructed for.

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

# LatLonPoint

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 631 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/LatLonPoint.h` | C++ | 143 |
| `src/maths/LatLonPoint.cc` | C++ | 113 |

## Overview

`LatLonPoint` is the boundary type between the outside world and GPlates' internal
geometry. Files, dialogs, the Python API and map projections all speak degrees of
latitude and longitude; everything inside `maths` speaks `UnitVector3D`. This unit holds
the pair of doubles, validates them on construction, and provides the only two
conversions — `make_point_on_sphere` and `make_lat_lon_point` — that cross that
boundary. Its fan-in is correspondingly wide, and it is the unit you touch when a
coordinate convention or a range check needs changing.

The conversion is a plain spherical-to-Cartesian transform with the z axis through the
poles and the x axis at (0, 0): `make_point_on_sphere` builds a `UnitVector3D` directly
from cosines and sines, so the unit-magnitude invariant is satisfied by construction
rather than by normalisation. The inverse is more careful than it looks. It deliberately
uses `Real`'s `asin` and `atan2` rather than the ones from `<cmath>`, because the stored
components may have drifted slightly outside [-1, 1] through accumulated rounding, and
`Real`'s versions do domain checking and correct almost-valid arguments instead of
returning NaN. It then folds a longitude of exactly -PI up to +PI, which is what makes
the round trip land in the half-open output range (-180, 180] the header describes.

Note that this file is also where `MathsUtils.h` enters the geometry headers:
`LatLonPoint.h` includes it for `is_in_range`, and `PointOnSphere.h` in turn includes
`LatLonPoint.h`, so `EPSILON`, `PI` and the degree/radian conversions are visible almost
everywhere in `maths`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::LatLonPoint`](#gplatesmathslatlonpoint) | class | [`GPlatesUtils::QtStreamable<LatLonPoint>`](../utils/QtStreamable.md) | — | 0 | — |

## Members

### `GPlatesMaths::LatLonPoint`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LatLonPoint( const double &lat, const double &lon)` | constructor | `None` | public | Make a point in the standard spherical coordinate system. |
| `is_valid_latitude( const double &val)` | method | `bool` | public | Return whether a given value is a valid latitude. |
| `is_valid_longitude( const double &val)` | method | `bool` | public | Return whether a given value is a valid longitude. |
| `d_latitude` | field | `double` | private | The latitude of the point, in degrees. |
| `d_longitude` | field | `double` | private | The longitude of the point, in degrees. |
| `operator==( const LatLonPoint &)` | operator | `bool` | private | Declare this operator private (but don't define it) so it can never be invoked. |
| `operator!=( const LatLonPoint &)` | operator | `bool` | private | Declare this operator private (but don't define it) so it can never be invoked. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_LATLONPOINT_H` | macro | `None` | — |
| `operator<<` | variable | `std::ostream` | — |
| `make_point_on_sphere( const LatLonPoint &)` | function | `PointOnSphere` | — |
| `make_lat_lon_point( const PointOnSphere &)` | function | `LatLonPoint` | — |

## Notes

Values are stored in **degrees**, never radians, and the constructor throws
`InvalidLatLonException` rather than clamping. There is no default constructor.

The two range checks are not symmetric. Latitude is restricted to [-90, 90], but
longitude accepts the whole of [-360, 360] on input while the class's stated output
convention is the half-open range (-180, 180]. Nothing in this unit normalises a
longitude: a `LatLonPoint` constructed with 350 keeps 350, and only a round trip through
`make_point_on_sphere` and `make_lat_lon_point` brings it back as -10. Code that
compares stored longitudes, or feeds them to a map projection, has to account for that
itself.

Both checks go through `GPlatesMaths::is_in_range`, which widens each bound by
`EPSILON`, so a latitude marginally past 90 is accepted and then passed to
`std::cos`/`std::sin` unchanged — harmless here, but it means "valid latitude" is
slightly wider than [-90, 90].

`operator==` and `operator!=` are declared private and never defined, so comparing two
`LatLonPoint`s is a compile or link error by design. This is deliberate rather than an
oversight: the representation is not unique (every longitude names the same pole, and
-180 and 180 are the same meridian), so equality only means something after conversion
to `PointOnSphere`.

`make_lat_lon_point` depends on `Real`'s domain-correcting `asin`/`atan2`. If you
replace them with the `<cmath>` versions for speed, points whose components have drifted
a few ulps outside [-1, 1] will start yielding NaN latitudes.

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/DateLineWrapper](DateLineWrapper.md) | maths | 97 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 74 |
| [maths/GeometryInterpolation](GeometryInterpolation.md) | maths | 65 |
| [app-logic/TopologyReconstruct](../app-logic/TopologyReconstruct.md) | app-logic | 57 |
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 50 |
| [maths/GreatCircleArc](GreatCircleArc.md) | maths | 44 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 41 |
| [gui/MapProjection](../gui/MapProjection.md) | gui | 41 |
| [app-logic/ResolvedSubSegmentRangeInSection](../app-logic/ResolvedSubSegmentRangeInSection.md) | app-logic | 39 |
| [app-logic/TopologyIntersections](../app-logic/TopologyIntersections.md) | app-logic | 39 |
| [maths/FiniteRotation](FiniteRotation.md) | maths | 39 |
| [maths/PolygonOnSphere](PolygonOnSphere.md) | maths | 38 |
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 38 |
| [view-operations/GeometryBuilder](../view-operations/GeometryBuilder.md) | view-operations | 38 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 35 |
| [maths/GeneratePoints](GeneratePoints.md) | maths | 32 |
| [qt-widgets/FiniteRotationCalculatorDialog](../qt-widgets/FiniteRotationCalculatorDialog.md) | qt-widgets | 31 |
| [qt-widgets/MovePoleWidget](../qt-widgets/MovePoleWidget.md) | qt-widgets | 31 |
| [canvas-tools/CanvasTool](../canvas-tools/CanvasTool.md) | canvas-tools | 30 |
| [maths/PointOnSphere](PointOnSphere.md) | maths | 29 |

*... and 183 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/LatLonPoint.h
python scripts/gpq.py def GPlatesMaths::LatLonPoint --body
python scripts/gpq.py uses LatLonPoint --kind class
python scripts/gpq.py hier LatLonPoint
```

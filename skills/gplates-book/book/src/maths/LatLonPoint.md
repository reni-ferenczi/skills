# LatLonPoint

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 631 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/LatLonPoint.h` | C++ | 143 |
| `src/maths/LatLonPoint.cc` | C++ | 113 |

## Overview

[[[PROSE overview unit=maths/LatLonPoint tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/LatLonPoint tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

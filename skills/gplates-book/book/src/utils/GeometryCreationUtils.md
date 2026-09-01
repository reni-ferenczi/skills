# GeometryCreationUtils

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1341 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/GeometryCreationUtils.h` | C++ | 519 |

## Overview

[[[PROSE overview unit=utils/GeometryCreationUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::GeometryConstruction::GeometryConstructionValidity`](#gplatesutilsgeometryconstructiongeometryconstructionvalidity) | enum | — | — | 0 | — |

## Members

### `GPlatesUtils::GeometryConstruction::GeometryConstructionValidity`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VALID` | enumerator | `None` | — | — |
| `INVALID_INSUFFICIENT_POINTS` | enumerator | `None` | — | — |
| `INVALID_ANTIPODAL_SEGMENT_ENDPOINTS` | enumerator | `None` | — | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_GEOMETRYCREATIONUTILS_H` | macro | `None` | — |
| `create_geometry_on_sphere( GPlatesMaths::GeometryType::Value geometry_type, const std::vector<GPlatesMaths::PointOnSphere> &points, GeometryConstruction::GeometryConstructionValidity &validity)` | function | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | An overload of create\_geometry\_on\_sphere accepting a vector of points. |
| `create_point_on_sphere( ForwardIterPointOnSphere begin_points_on_sphere, ForwardIterPointOnSphere end_points_on_sphere, GPlatesUtils::GeometryConstruction::GeometryConstructionValidity &validity)` | function | `boost::optional<GPlatesMaths::PointOnSphere>` | Creates a single PointOnSphere (assuming \>= 1 points are provided). |
| `create_point_on_sphere( const std::vector<GPlatesMaths::PointOnSphere> &points, GeometryConstruction::GeometryConstructionValidity &validity)` | function | `boost::optional<GPlatesMaths::PointOnSphere>` | Creates a single PointOnSphere (assuming \>= 1 points are provided). |
| `create_point_geometry_on_sphere( const std::vector<GPlatesMaths::PointOnSphere> &points, GeometryConstruction::GeometryConstructionValidity &validity)` | function | `boost::optional<GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type>` | Same as create\_point\_on\_sphere but returns the GeoemtryOnSphere derivation PointGeometryOnSphere. |
| `create_polyline_on_sphere( const std::vector<GPlatesMaths::PointOnSphere> &points, GeometryConstruction::GeometryConstructionValidity &validity)` | function | `boost::optional<GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type>` | Creates a single PolylineOnSphere (assuming \>= 2 distinct points are provided). validity is a return-parameter. |
| `create_polygon_on_sphere( const std::vector<GPlatesMaths::PointOnSphere> &points, GeometryConstruction::GeometryConstructionValidity &validity)` | function | `boost::optional<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | Creates a single PolygonOnSphere (assuming \>= 3 distinct points are provided). validity is a return-parameter. |
| `create_multipoint_on_sphere( const std::vector<GPlatesMaths::PointOnSphere> &points, GeometryConstruction::GeometryConstructionValidity &validity)` | function | `boost::optional<GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type>` | Creates a single MultiPointOnSphere (assuming \>= 1 point is provided). validity is a return-parameter. |
| `create_geometry_on_sphere( GPlatesMaths::GeometryType::Value geometry_type, ForwardIterPointOnSphere begin_points_on_sphere, ForwardIterPointOnSphere end_points_on_sphere, GPlatesUtils::GeometryConstruction::GeometryConstructionValidity &validity)` | function | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | — |
| `create_point_on_sphere( ForwardIterPointOnSphere begin_points_on_sphere, ForwardIterPointOnSphere end_points_on_sphere, GeometryConstruction::GeometryConstructionValidity &validity)` | function | `boost::optional<GPlatesMaths::PointOnSphere>` | — |
| `create_point_geometry_on_sphere( ForwardIterPointOnSphere begin_points_on_sphere, ForwardIterPointOnSphere end_points_on_sphere, GPlatesUtils::GeometryConstruction::GeometryConstructionValidity &validity)` | function | `boost::optional<GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type>` | — |
| `create_polyline_on_sphere( ForwardIterPointOnSphere begin_points_on_sphere, ForwardIterPointOnSphere end_points_on_sphere, GeometryConstruction::GeometryConstructionValidity &validity)` | function | `boost::optional<GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type>` | — |
| `create_polygon_on_sphere( ForwardIterPointOnSphere begin_points_on_sphere, ForwardIterPointOnSphere end_points_on_sphere, GeometryConstruction::GeometryConstructionValidity &validity)` | function | `boost::optional<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | — |
| `create_multipoint_on_sphere( ForwardIterPointOnSphere begin_points_on_sphere, ForwardIterPointOnSphere end_points_on_sphere, GeometryConstruction::GeometryConstructionValidity &validity)` | function | `boost::optional<GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type>` | — |

## Notes

[[[PROSE notes unit=utils/GeometryCreationUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 16 |
| [view-operations/InternalGeometryBuilder](../view-operations/InternalGeometryBuilder.md) | view-operations | 14 |
| [view-operations/InsertVertexGeometryOperation](../view-operations/InsertVertexGeometryOperation.md) | view-operations | 13 |
| [view-operations/SplitFeatureGeometryOperation](../view-operations/SplitFeatureGeometryOperation.md) | view-operations | 13 |
| [qt-widgets/EditGeometryWidget](../qt-widgets/EditGeometryWidget.md) | qt-widgets | 12 |
| [app-logic/TopologyGeometryResolver](../app-logic/TopologyGeometryResolver.md) | app-logic | 9 |
| [view-operations/GeometryBuilder](../view-operations/GeometryBuilder.md) | view-operations | 9 |
| [app-logic/TopologyNetworkResolver](../app-logic/TopologyNetworkResolver.md) | app-logic | 5 |
| [canvas-tools/MeasureDistance](../canvas-tools/MeasureDistance.md) | canvas-tools | 5 |
| [view-operations/AddPointGeometryOperation](../view-operations/AddPointGeometryOperation.md) | view-operations | 3 |
| [app-logic/ResolvedTopologicalNetwork](../app-logic/ResolvedTopologicalNetwork.md) | app-logic | 1 |
| [app-logic/TopologyReconstruct](../app-logic/TopologyReconstruct.md) | app-logic | 1 |
| [canvas-tools/BuildTopology](../canvas-tools/BuildTopology.md) | canvas-tools | 1 |
| [canvas-tools/EditTopology](../canvas-tools/EditTopology.md) | canvas-tools | 1 |
| [qt-widgets/DigitisationWidget](../qt-widgets/DigitisationWidget.md) | qt-widgets | 1 |
| [qt-widgets/LatLonCoordinatesTable](../qt-widgets/LatLonCoordinatesTable.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/GeometryCreationUtils.h
python scripts/gpq.py def GPlatesUtils::GeometryConstruction::GeometryConstructionValidity --body
python scripts/gpq.py uses GeometryConstructionValidity --kind enum
```

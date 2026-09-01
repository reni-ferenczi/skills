# IsInRegionOfInterestVisitor

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 516 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/IsInRegionOfInterestVisitor.h` | C++ | 537 |
| `src/data-mining/deprecated/IsInRegionOfInterestVisitor.cc` | C++ | 58 |

## Overview

[[[PROSE overview unit=data-mining/deprecated/IsInRegionOfInterestVisitor tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::MultiPointPtr`](#gplatesdataminingmultipointptr) | typedef | — | — | 0 | — |
| [`GPlatesDataMining::PointPtr`](#gplatesdataminingpointptr) | typedef | — | — | 0 | — |
| [`GPlatesDataMining::PolygonPtr`](#gplatesdataminingpolygonptr) | typedef | — | — | 0 | — |
| [`GPlatesDataMining::PolylinePtr`](#gplatesdataminingpolylineptr) | typedef | — | — | 0 | — |
| [`GPlatesDataMining::(anonymous)::IsInReigonOfInterestDispatchVisitor`](#gplatesdatamininganonymousisinreigonofinterestdispatchvisitor) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | — |
| [`GPlatesDataMining::(anonymous)::IsInReigonOfInterestCheckerVisitor`](#gplatesdatamininganonymousisinreigonofinterestcheckervisitor) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../../maths/ConstGeometryOnSphereVisitor.md) | `< class GeometryType >` | 0 | — |

## Members

### `GPlatesDataMining::MultiPointPtr`

*None.*

### `GPlatesDataMining::PointPtr`

*None.*

### `GPlatesDataMining::PolygonPtr`

*None.*

### `GPlatesDataMining::PolylinePtr`

*None.*

### `GPlatesDataMining::(anonymous)::IsInReigonOfInterestDispatchVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `IsInReigonOfInterestDispatchVisitor( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type base_geometry, double range)` | constructor | `None` | public | — |
| `visit_multi_point_on_sphere( MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | public | — |
| `visit_point_on_sphere( PointOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | public | — |
| `visit_polygon_on_sphere( PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | public | — |
| `visit_polyline_on_sphere( PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | public | — |
| `is_in_reigon_of_interest()` | method | `bool` | public | — |
| `distance()` | method | `double` | public | — |
| `dispatch( GeometryType geometry )` | method | `void` | protected | — |
| `d_base_geometry` | field | `boost::optional< GeometryOnSphere::non_null_ptr_to_const_type >` | protected | — |
| `d_ROI_range` | field | `double` | protected | — |
| `d_distance` | field | `double` | protected | — |
| `d_is_in_reigon_of_interest` | field | `bool` | protected | — |
| `IsInReigonOfInterestDispatchVisitor()` | constructor | `None` | private | — |

### `GPlatesDataMining::(anonymous)::IsInReigonOfInterestCheckerVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `IsInReigonOfInterestCheckerVisitor( GeometryType geometry, IsInReigonOfInterestDispatchVisitor* parent)` | constructor | `None` | public | — |
| `visit_multi_point_on_sphere( MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | public | — |
| `visit_point_on_sphere( PointOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | public | — |
| `visit_polygon_on_sphere( PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | public | — |
| `visit_polyline_on_sphere( PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | public | — |
| `d_candidate_geometry` | field | `boost::optional< GeometryType >` | private | — |
| `d_parent_ptr` | field | `IsInReigonOfInterestDispatchVisitor` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_ISINREGIONOFINTERESTVISITOR_H` | macro | `None` | — |
| `RADIUS_OF_EARTH` | variable | `double` | — |
| `is_close_enough( const GeometryOnSphere& g1, const GeometryOnSphere& g2, const double range)` | function | `bool` | TODO: more comments Until function. |
| `is_close_enough_internal( PolylinePtr polyline, PointPtr point, double range)` | function | `bool` | — |
| `is_close_enough_internal( PolygonPtr polygon, PointPtr point, double range)` | function | `bool` | — |
| `is_close_enough_internal( PolygonPtr polygon, PolylinePtr polyline, double range)` | function | `bool` | — |
| `is_close_enough_internal( MultiPointPtr multi_point, PointPtr point, double range)` | function | `bool` | — |
| `is_close_enough_internal( MultiPointPtr multi_point, PolylinePtr polyline, double range)` | function | `bool` | — |
| `is_close_enough_internal( MultiPointPtr multi_point, PolygonPtr polygon, double range)` | function | `bool` | — |
| `is_close_enough_internal( PointPtr point1, PointPtr point2, double range)` | function | `bool` | Point to point |
| `is_close_enough_internal( PointPtr point, PolygonPtr polygon, double range)` | function | `bool` | Point to polygon |
| `is_close_enough_internal( PointPtr point, PolylinePtr polyline, double range)` | function | `bool` | Point to polyline |
| `is_close_enough_internal( PointPtr point, MultiPointPtr multi_point, double range)` | function | `bool` | Point to multi points |
| `is_close_enough_internal( PolylinePtr polyline1, PolylinePtr polyline2, double range)` | function | `bool` | — |
| `is_close_enough_internal( PolylinePtr polyline, PolygonPtr polygon, double range)` | function | `bool` | — |
| `is_close_enough_internal( PolylinePtr polyline, MultiPointPtr multi_point, double range)` | function | `bool` | — |
| `is_close_enough_internal( PolygonPtr polygon1, PolygonPtr polygon2, double range)` | function | `bool` | — |
| `is_close_enough_internal( PolygonPtr polygon, MultiPointPtr multi_point, double range)` | function | `bool` | — |
| `is_close_enough_internal( MultiPointPtr multi_point1, MultiPointPtr multi_point2, double range)` | function | `bool` | — |

## Notes

[[[PROSE notes unit=data-mining/deprecated/IsInRegionOfInterestVisitor tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/PolygonOnSphere](../../maths/PolygonOnSphere.md) | maths | 9 |
| [app-logic/GeometryUtils](../../app-logic/GeometryUtils.md) | app-logic | 3 |
| [data-mining/deprecated/RegionOfInterestAssociationOperator](RegionOfInterestAssociationOperator.md) | data-mining | 3 |
| [file-io/PlatesRotationFileProxy](../../file-io/PlatesRotationFileProxy.md) | file-io | 3 |
| [maths/PolyGreatCircleArcBoundingTree](../../maths/PolyGreatCircleArcBoundingTree.md) | maths | 3 |
| [maths/PolylineOnSphere](../../maths/PolylineOnSphere.md) | maths | 3 |
| [utils/Profile](../../utils/Profile.md) | utils | 3 |
| [api/PyFeature](../../api/PyFeature.md) | api | 2 |
| [data-mining/DataMiningUtils](../DataMiningUtils.md) | data-mining | 2 |
| [data-mining/LookupReducer](../LookupReducer.md) | data-mining | 2 |
| [file-io/GpmlOutputVisitor](../../file-io/GpmlOutputVisitor.md) | file-io | 2 |
| [gui/TopologySectionsContainer](../../gui/TopologySectionsContainer.md) | gui | 2 |
| [maths/PointOnSphere](../../maths/PointOnSphere.md) | maths | 2 |
| [data-mining/RFGToRelationalPropertyMapper](../RFGToRelationalPropertyMapper.md) | data-mining | 1 |
| [feature-visitors/ViewFeatureGeometriesWidgetPopulator](../../feature-visitors/ViewFeatureGeometriesWidgetPopulator.md) | feature-visitors | 1 |
| [gui/TreeWidgetBuilder](../../gui/TreeWidgetBuilder.md) | gui | 1 |
| [maths/GeometryInterpolation](../../maths/GeometryInterpolation.md) | maths | 1 |
| [maths/MultiPointOnSphere](../../maths/MultiPointOnSphere.md) | maths | 1 |
| [property-values/GpmlStringList](../../property-values/GpmlStringList.md) | property-values | 1 |
| [unit-test/FilterTest](../../unit-test/FilterTest.md) | unit-test | 1 |

*... and 1 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/deprecated/IsInRegionOfInterestVisitor.h
python scripts/gpq.py def GPlatesDataMining::(anonymous)::IsInReigonOfInterestDispatchVisitor --body
python scripts/gpq.py uses IsInReigonOfInterestDispatchVisitor --kind class
python scripts/gpq.py hier IsInReigonOfInterestDispatchVisitor
```

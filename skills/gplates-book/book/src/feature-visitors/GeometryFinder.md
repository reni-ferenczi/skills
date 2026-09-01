# GeometryFinder

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 298 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/GeometryFinder.h` | C++ | 254 |
| `src/feature-visitors/GeometryFinder.cc` | C++ | 137 |

## Overview

`GeometryFinder` walks a feature's properties and collects every `GmlPoint`, `GmlLineString`, `GmlMultiPoint` and `GmlPolygon` it encounters, both into one combined `geometry_container_type` and into per-type containers so callers can ask for "all the polylines" without filtering the combined list themselves. `GmlOrientableCurve` and `GpmlConstantValue` wrappers are transparently unwrapped by re-visiting the geometry or value they carry.

Passing a `GPlatesModel::PropertyName` to the constructor (or `add_property_name_to_allow()`) restricts the search to top-level properties with that name, via `initialise_pre_property_values()`; with no names supplied, every property is visited. `GeometryTypeFinder` and the free functions below build on this same visiting pattern for classification and lookup rather than collection.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFeatureVisitors::GeometryFinder`](#gplatesfeaturevisitorsgeometryfinder) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | This const feature visitor finds all geometry contained within the feature. |

## Members

### `GPlatesFeatureVisitors::GeometryFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `geometry_elem_type` | typedef | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | All geoms |
| `geometry_container_type` | typedef | `std::vector<geometry_elem_type>` | public | — |
| `geometry_container_const_iterator` | typedef | `geometry_container_type::const_iterator` | public | — |
| `point_geometry_elem_type` | typedef | `GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type` | public | Point Geoms |
| `point_geometry_container_type` | typedef | `std::vector<point_geometry_elem_type>` | public | — |
| `point_geometry_container_const_iterator` | typedef | `point_geometry_container_type::const_iterator` | public | — |
| `polyline_geometry_elem_type` | typedef | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | public | Polyline Geoms |
| `polyline_geometry_container_type` | typedef | `std::vector<polyline_geometry_elem_type>` | public | — |
| `polyline_geometry_container_const_iterator` | typedef | `polyline_geometry_container_type::const_iterator` | public | — |
| `polygon_geometry_elem_type` | typedef | `GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type` | public | Polygon Geoms |
| `polygon_geometry_container_type` | typedef | `std::vector<polygon_geometry_elem_type>` | public | — |
| `polygon_geometry_container_const_iterator` | typedef | `polygon_geometry_container_type::const_iterator` | public | — |
| `multi_point_geometry_elem_type` | typedef | `GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type` | public | MultiPoint Geoms |
| `multi_point_geometry_container_type` | typedef | `std::vector<multi_point_geometry_elem_type>` | public | — |
| `multi_point_geometry_container_const_iterator` | typedef | `multi_point_geometry_container_type::const_iterator` | public | — |
| `GeometryFinder()` | constructor | `None` | public | FIXME: Supply the current reconstruction time to allow for time-dependent properties. |
| `GeometryFinder( const GPlatesModel::PropertyName &property_name_to_allow)` | constructor | `None` | public | — |
| `~GeometryFinder()` | destructor | `None` | public | — |
| `add_property_name_to_allow( const GPlatesModel::PropertyName &property_name_to_allow)` | method | `void` | public | — |
| `found_geometries_begin()` | method | `geometry_container_const_iterator` | public | All Geometry types in one vector |
| `found_geometries_end()` | method | `geometry_container_const_iterator` | public | — |
| `found_point_geometries_begin()` | method | `point_geometry_container_const_iterator` | public | Point Geometries |
| `found_point_geometries_end()` | method | `point_geometry_container_const_iterator` | public | — |
| `found_polyline_geometries_begin()` | method | `polyline_geometry_container_const_iterator` | public | Polyline Geometries |
| `found_polyline_geometries_end()` | method | `polyline_geometry_container_const_iterator` | public | — |
| `found_polygon_geometries_begin()` | method | `polygon_geometry_container_const_iterator` | public | Polygon Geometries |
| `found_polygon_geometries_end()` | method | `polygon_geometry_container_const_iterator` | public | — |
| `found_multi_point_geometries_begin()` | method | `multi_point_geometry_container_const_iterator` | public | MultiPoint Geometries |
| `found_multi_point_geometries_end()` | method | `multi_point_geometry_container_const_iterator` | public | — |
| `has_found_geometries()` | method | `bool` | public | Return true if any geometries have been found. |
| `first_geometry_found()` | method | `geometry_elem_type` | public | Access the first element in the container of found geometries. |
| `clear_found_geometries()` | method | `void` | public | — |
| `initialise_pre_property_values( const GPlatesModel::TopLevelPropertyInline &top_level_property_inline)` | method | `bool` | protected | — |
| `visit_gml_line_string( const GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | protected | — |
| `visit_gml_multi_point( const GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | protected | — |
| `visit_gml_orientable_curve( const GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | protected | — |
| `visit_gml_point( const GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | protected | — |
| `visit_gml_polygon( const GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | protected | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | protected | — |
| `d_property_names_to_allow` | field | `std::vector<GPlatesModel::PropertyName>` | private | — |
| `d_found_geometries` | field | `geometry_container_type` | private | One container holding all types of geoms |
| `d_found_point_geometries` | field | `point_geometry_container_type` | private | Separte containers for each basic type |
| `d_found_polyline_geometries` | field | `polyline_geometry_container_type` | private | — |
| `d_found_polygon_geometries` | field | `polygon_geometry_container_type` | private | — |
| `d_found_multi_point_geometries` | field | `multi_point_geometry_container_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `contains_elem( const C &container, const E &elem)` | function | `bool` | — |
| `GPLATES_FEATUREVISITORS_GEOMETRYFINDER_H` | macro | `None` | — |

## Notes

`first_geometry_found()` throws `GPlatesGlobal::RetrievalFromEmptyContainerException` if nothing was found — call `has_found_geometries()` first. A `GmlPolygon`'s interior/exterior ring distinction is lost: the whole polygon becomes one `PolygonOnSphere`.

## Used by

| Unit | Component | References |
|---|---|---|
| [feature-visitors/GeometryTypeFinder](GeometryTypeFinder.md) | feature-visitors | 26 |
| [gui/FeatureTableModel](../gui/FeatureTableModel.md) | gui | 10 |
| [qt-widgets/KinematicGraphsDialog](../qt-widgets/KinematicGraphsDialog.md) | qt-widgets | 8 |
| [view-operations/SplitFeatureUndoCommand](../view-operations/SplitFeatureUndoCommand.md) | view-operations | 8 |
| [unit-test/GenerateVelocityDomainCitcomsTest](../unit-test/GenerateVelocityDomainCitcomsTest.md) | unit-test | 5 |
| [app-logic/deprecated/PaleomagWorkflow](../app-logic/deprecated/PaleomagWorkflow.md) | app-logic | 4 |
| [data-mining/deprecated/RegionOfInterestAssociationOperator](../data-mining/deprecated/RegionOfInterestAssociationOperator.md) | data-mining | 3 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 2 |
| [data-mining/deprecated/IsInRegionOfInterestVisitor](../data-mining/deprecated/IsInRegionOfInterestVisitor.md) | data-mining | 1 |
| [gui/FeatureFocus](../gui/FeatureFocus.md) | gui | 1 |
| [qt-widgets/GenerateVelocityDomainCitcomsDialog](../qt-widgets/GenerateVelocityDomainCitcomsDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/GeometryFinder.h
python scripts/gpq.py def GPlatesFeatureVisitors::GeometryFinder --body
python scripts/gpq.py uses GeometryFinder --kind class
python scripts/gpq.py hier GeometryFinder
```

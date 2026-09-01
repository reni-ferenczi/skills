# GeometryTypeFinder

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 581 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/GeometryTypeFinder.h` | C++ | 246 |
| `src/feature-visitors/GeometryTypeFinder.cc` | C++ | 219 |

## Overview

[[[PROSE overview unit=feature-visitors/GeometryTypeFinder tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFeatureVisitors::GeometryTypeFinder`](#gplatesfeaturevisitorsgeometrytypefinder) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md)<br>[`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | This feature visitor can be used to determine which geometry types exist in a feature. |

## Members

### `GPlatesFeatureVisitors::GeometryTypeFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GeometryTypeFinder()` | constructor | `None` | public | — |
| `~GeometryTypeFinder()` | destructor | `None` | public | — |
| `visit_gml_line_string( const GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | protected | — |
| `visit_gml_multi_point( const GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | protected | — |
| `visit_gml_orientable_curve( const GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | protected | — |
| `visit_gml_point( const GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | protected | — |
| `visit_gml_polygon( const GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | protected | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | protected | — |
| `visit_multipoint_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | protected | — |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | protected | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | protected | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | protected | — |
| `found_point_geometries()` | method | `bool` | public | — |
| `found_multi_point_geometries()` | method | `bool` | public | — |
| `found_polyline_geometries()` | method | `bool` | public | — |
| `found_polygon_geometries()` | method | `bool` | public | — |
| `num_point_geometries_found()` | method | `int` | public | — |
| `num_multi_point_geometries_found()` | method | `int` | public | — |
| `num_polyline_geometries_found()` | method | `int` | public | — |
| `num_polygon_geometries_found()` | method | `int` | public | — |
| `has_found_geometries()` | method | `bool` | public | — |
| `has_found_multiple_geometry_types()` | method | `bool` | public | Returns true if different types of geometry were found. |
| `has_found_multiple_geometries_of_the_same_type()` | method | `bool` | public | Returns true if found more than one geometry of the same type. |
| `clear()` | method | `void` | public | — |
| `d_num_point_geometries_found` | field | `int` | private | — |
| `d_num_multi_point_geometries_found` | field | `int` | private | — |
| `d_num_polyline_geometries_found` | field | `int` | private | — |
| `d_num_polygon_geometries_found` | field | `int` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FEATUREVISITORS_GEOMETRYTYPEFINDER_H` | macro | `None` | — |
| `find_first_geometry_property( GPlatesModel::FeatureHandle::weak_ref feature_ref)` | function | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | Find the first geometry property from a feature. |
| `find_first_geometry_property( GPlatesModel::FeatureHandle& feature_ref)` | function | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | — |
| `is_not_geometry_property( const GPlatesModel::TopLevelProperty::non_null_ptr_to_const_type &top_level_prop_ptr)` | function | `bool` | Determine if the given property contains a geometry. |
| `is_geometry_property( const GPlatesModel::TopLevelProperty::non_null_ptr_to_const_type &top_level_prop_ptr)` | function | `bool` | Determine if the given property contains a geometry. |
| `find_first_geometry( GPlatesModel::FeatureHandle::iterator iter)` | function | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | Find the first geometry from a property. |

## Notes

[[[PROSE notes unit=feature-visitors/GeometryTypeFinder tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 25 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 19 |
| [file-io/OgrFormatReconstructedFeatureGeometryExport](../file-io/OgrFormatReconstructedFeatureGeometryExport.md) | file-io | 8 |
| [view-operations/SplitFeatureUndoCommand](../view-operations/SplitFeatureUndoCommand.md) | view-operations | 6 |
| [file-io/OgrFormatResolvedTopologicalGeometryExport](../file-io/OgrFormatResolvedTopologicalGeometryExport.md) | file-io | 5 |
| [view-operations/CloneOperation](../view-operations/CloneOperation.md) | view-operations | 5 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 2 |
| [view-operations/SplitFeatureGeometryOperation](../view-operations/SplitFeatureGeometryOperation.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/GeometryTypeFinder.h
python scripts/gpq.py def GPlatesFeatureVisitors::GeometryTypeFinder --body
python scripts/gpq.py uses GeometryTypeFinder --kind class
python scripts/gpq.py hier GeometryTypeFinder
```

# GeometrySetter

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 1310 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/GeometrySetter.h` | C++ | 133 |
| `src/feature-visitors/GeometrySetter.cc` | C++ | 148 |

## Overview

[[[PROSE overview unit=feature-visitors/GeometrySetter tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFeatureVisitors::GeometrySetter`](#gplatesfeaturevisitorsgeometrysetter) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | This feature visitor takes a GPlatesMaths::GeometryOnSphere, and assigns it to a GPlatesModel::PropertyValue. |

## Members

### `GPlatesFeatureVisitors::GeometrySetter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `geometry_ptr_type` | typedef | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | — |
| `GeometrySetter( geometry_ptr_type geometry_to_set)` | constructor | `None` | public | — |
| `~GeometrySetter()` | destructor | `None` | public | — |
| `set_geometry( GPlatesModel::PropertyValue *geometry_property_value)` | method | `void` | public | Sets the geometry contained in geometry\_property to the geometry specified in the constructor. |
| `set_geometry( GPlatesModel::TopLevelProperty *geometry_top_level_property)` | method | `void` | public | Sets the geometry contained in geometry\_property\_container to the geometry specified in the constructor. |
| `visit_gml_line_string( GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | private | — |
| `visit_gml_multi_point( GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | private | — |
| `visit_gml_orientable_curve( GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | private | — |
| `visit_gml_point( GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gml_polygon( GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | private | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `d_geometry_to_set` | field | `geometry_ptr_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FEATUREVISITORS_GEOMETRYSETTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=feature-visitors/GeometrySetter tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 219 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 74 |
| [view-operations/SplitFeatureUndoCommand](../view-operations/SplitFeatureUndoCommand.md) | view-operations | 33 |
| [view-operations/FocusedFeatureGeometryManipulator](../view-operations/FocusedFeatureGeometryManipulator.md) | view-operations | 18 |
| [api/PyFunctions](../api/PyFunctions.md) | api | 16 |
| [qt-widgets/EditGeometryWidget](../qt-widgets/EditGeometryWidget.md) | qt-widgets | 8 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/GeometrySetter.h
python scripts/gpq.py def GPlatesFeatureVisitors::GeometrySetter --body
python scripts/gpq.py uses GeometrySetter --kind class
python scripts/gpq.py hier GeometrySetter
```

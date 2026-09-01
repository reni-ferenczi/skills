# GeometrySetter

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 1310 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/GeometrySetter.h` | C++ | 133 |
| `src/feature-visitors/GeometrySetter.cc` | C++ | 148 |

## Overview

`GeometrySetter` is `GeometryFinder`'s inverse: it holds one `GeometryOnSphere` and, when visited onto an existing `PropertyValue` or `TopLevelProperty`, writes that geometry into whichever concrete geometry property-value it lands on (`GmlPoint`, `GmlLineString`, `GmlMultiPoint`, `GmlPolygon`), dynamic-casting the stored geometry to the type each `visit_*` override expects. It is used wherever edited or newly-drawn geometry needs to be pushed back into the model without call sites needing property-type-specific code — `CreateFeatureDialog`, `PartitionFeatureUtils`, `SplitFeatureUndoCommand` and the geometry-editing operations in `view-operations` all go through it.

It inherits `FeatureVisitor` privately and exposes only the two `set_geometry()` overloads; per the header comment, setting geometry directly on a `FeatureHandle` is deliberately not supported because it would be ambiguous which of the feature's geometry properties should change — the caller must pick the property first.

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

If the stored `GeometryOnSphere`'s runtime type doesn't match the visited property value's expected geometry type, the `dynamic_cast` fails and the `visit_*` override does nothing — no exception, no error, the property value is left unchanged.

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

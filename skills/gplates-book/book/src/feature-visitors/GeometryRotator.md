# GeometryRotator

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 1424 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/GeometryRotator.h` | C++ | 87 |
| `src/feature-visitors/GeometryRotator.cc` | C++ | 94 |

## Overview

This visitor applies a `FiniteRotation` to all geometry properties in a feature, modifying them in place. It traverses the feature hierarchy, visiting each geometry type (point, multi-point, line string, orientable curve, polygon) and replacing it with its rotated equivalent. This is used when features need to be transformed to a different reference frame during reconstruction or other operations.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFeatureVisitors::GeometryRotator`](#gplatesfeaturevisitorsgeometryrotator) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Visits all geometry properties in a feature, rotates them and replaces the original geometry with the rotated versions. |

## Members

### `GPlatesFeatureVisitors::GeometryRotator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GeometryRotator( const GPlatesMaths::FiniteRotation &finite_rotation)` | constructor | `None` | public | — |
| `visit_gml_line_string( GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | protected | — |
| `visit_gml_multi_point( GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | protected | — |
| `visit_gml_orientable_curve( GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | protected | — |
| `visit_gml_point( GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | protected | — |
| `visit_gml_polygon( GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | protected | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | protected | — |
| `d_finite_rotation` | field | `GPlatesMaths::FiniteRotation` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FEATURE_VISITORS_GEOMETRYROTATOR_H` | macro | `None` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/GeometryRotator.h
python scripts/gpq.py def GPlatesFeatureVisitors::GeometryRotator --body
python scripts/gpq.py uses GeometryRotator --kind class
python scripts/gpq.py hier GeometryRotator
```

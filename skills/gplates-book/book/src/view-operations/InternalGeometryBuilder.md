# InternalGeometryBuilder

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1118 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/InternalGeometryBuilder.h` | C++ | 183 |
| `src/view-operations/InternalGeometryBuilder.cc` | C++ | 125 |

## Overview

[[[PROSE overview unit=view-operations/InternalGeometryBuilder tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::InternalGeometryBuilder`](#gplatesviewoperationsinternalgeometrybuilder) | class | — | — | 0 | This is a helper class used only by GeometryBuilder to help with building geometry(s). |

## Members

### `GPlatesViewOperations::InternalGeometryBuilder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `geometry_opt_ptr_type` | typedef | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | public | This typedef is used wherever geometry (of some unknown type) is expected. |
| `point_seq_type` | typedef | `std::vector<GPlatesMaths::PointOnSphere>` | public | Sequence of points on sphere. |
| `point_seq_const_iterator_type` | typedef | `point_seq_type::const_iterator` | public | Iterator over sequence of const points on sphere. |
| `InternalGeometryBuilder( GeometryBuilder *geometry_builder, GPlatesMaths::GeometryType::Value desired_geom_type)` | constructor | `None` | public | Construct empty geometry. |
| `set_desired_geometry_type( GPlatesMaths::GeometryType::Value geom_type)` | method | `void` | public | Sets the type of geometry we'd like to build. |
| `get_actual_geometry_type()` | method | `GPlatesMaths::GeometryType::Value` | public | Returns actual geometry. |
| `get_geometry_on_sphere()` | method | `geometry_opt_ptr_type` | public | Returns a GeometryOnSphere representing the current geometry state. |
| `update()` | method | `void` | public | Updates internal state to reflect current point sequence and actual geometry type. |
| `d_desired_geometry_type` | field | `GPlatesMaths::GeometryType::Value` | private | The type of geometry we are trying to build. |
| `d_point_seq` | field | `point_seq_type` | private | — |
| `d_geometry_opt_ptr` | field | `geometry_opt_ptr_type` | private | What kind of geometry did we successfully build last? |
| `d_actual_geometry_type` | field | `GPlatesMaths::GeometryType::Value` | private | The actual type of geometry as it currently stands. |
| `d_update` | field | `bool` | private | Does d\_geometry\_opt\_ptr or d\_actual\_geometry\_type need updating? |
| `create_geometry_on_sphere( GPlatesMaths::GeometryType::Value)` | method | `void` | private | Attempts to create a GeometryOnSphere of the specified type. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_INTERNALGEOMETRYBUILDER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=view-operations/InternalGeometryBuilder tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/GeometryBuilder](GeometryBuilder.md) | view-operations | 30 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/InternalGeometryBuilder.h
python scripts/gpq.py def GPlatesViewOperations::InternalGeometryBuilder --body
python scripts/gpq.py uses InternalGeometryBuilder --kind class
python scripts/gpq.py hier InternalGeometryBuilder
```

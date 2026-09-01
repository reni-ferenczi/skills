# DigitiseGeometry

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 500 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/DigitiseGeometry.h` | C++ | 136 |
| `src/canvas-tools/DigitiseGeometry.cc` | C++ | 104 |

## Overview

[[[PROSE overview unit=canvas-tools/DigitiseGeometry tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::DigitiseGeometry`](#gplatescanvastoolsdigitisegeometry) | class | [`CanvasTool`](CanvasTool.md) | — | 0 | This is the canvas tool used to define new geometry. |

## Members

### `GPlatesCanvasTools::DigitiseGeometry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( const status_bar_callback_type &status_bar_callback, GPlatesMaths::GeometryType::Value geom_type, GPlatesViewOperations::GeometryBuilder &geometry_builder, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, GPlat ...` | method | `non_null_ptr_type` | public | — |
| `~DigitiseGeometry()` | destructor | `None` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `DigitiseGeometry( const status_bar_callback_type &status_bar_callback, GPlatesMaths::GeometryType::Value geom_type, GPlatesViewOperations::GeometryBuilder &geometry_builder, GPlatesCanvasTools::GeometryOperationState &geometry_operation_state, GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collect ...` | constructor | `None` | private | Create a DigitiseGeometry instance. |
| `d_default_geom_type` | field | `GPlatesMaths::GeometryType::Value` | private | This is the type of geometry this particular DigitiseGeometry tool should default to. |
| `d_geometry_builder` | field | `GPlatesViewOperations::GeometryBuilder` | private | — |
| `d_add_point_geometry_operation` | field | `boost::scoped_ptr<GPlatesViewOperations::AddPointGeometryOperation>` | private | Digitise operation for adding a point to digitised geometry. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_DIGITISEGEOMETRY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=canvas-tools/DigitiseGeometry tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/DigitisationCanvasToolWorkflow](../gui/DigitisationCanvasToolWorkflow.md) | gui | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/DigitiseGeometry.h
python scripts/gpq.py def GPlatesCanvasTools::DigitiseGeometry --body
python scripts/gpq.py uses DigitiseGeometry --kind class
python scripts/gpq.py hier DigitiseGeometry
```

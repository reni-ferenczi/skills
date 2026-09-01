# RenderedPolygonOnSphere

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1063 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedPolygonOnSphere.h` | C++ | 149 |

## Overview

[[[PROSE overview unit=view-operations/RenderedPolygonOnSphere tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedPolygonOnSphere`](#gplatesviewoperationsrenderedpolygononsphere) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | — |

## Members

### `GPlatesViewOperations::RenderedPolygonOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedPolygonOnSphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere, const GPlatesGui::ColourProxy &colour, float line_width_hint, bool filled, const GPlatesGui::Colour &fill_modulate_colour)` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `test_vertex_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `get_polygon_on_sphere()` | method | `GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type` | public | — |
| `get_line_width_hint()` | method | `float` | public | — |
| `get_is_filled()` | method | `bool` | public | — |
| `d_polygon_on_sphere` | field | `GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type` | private | — |
| `d_colour` | field | `GPlatesGui::ColourProxy` | private | — |
| `d_line_width_hint` | field | `float` | private | — |
| `d_is_filled` | field | `bool` | private | — |
| `d_fill_modulate_colour` | field | `GPlatesGui::Colour` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDPOLYGONONSPHERE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=view-operations/RenderedPolygonOnSphere tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 1 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 1 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedPolygonOnSphere.h
python scripts/gpq.py def GPlatesViewOperations::RenderedPolygonOnSphere --body
python scripts/gpq.py uses RenderedPolygonOnSphere --kind class
python scripts/gpq.py hier RenderedPolygonOnSphere
```

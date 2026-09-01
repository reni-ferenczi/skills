# RenderedPolylineOnSphere

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1064 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedPolylineOnSphere.h` | C++ | 159 |

## Overview

A rendered geometry wrapper for a polyline on a sphere, holding a `PolylineOnSphere`, display properties, and optional fill state. `test_proximity()` first defers to the polyline itself; if that misses and the geometry is filled with at least three vertices, it builds a temporary `PolygonOnSphere` from the polyline's vertices and runs a point-in-polygon test, so a hit anywhere in the filled interior is reported at closeness 1.0. `test_vertex_proximity()` always delegates straight to the polyline.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedPolylineOnSphere`](#gplatesviewoperationsrenderedpolylineonsphere) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | — |

## Members

### `GPlatesViewOperations::RenderedPolylineOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedPolylineOnSphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere, const GPlatesGui::ColourProxy &colour, float line_width_hint, bool filled, const GPlatesGui::Colour &fill_modulate_colour)` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `test_vertex_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `get_polyline_on_sphere()` | method | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | public | — |
| `get_line_width_hint()` | method | `float` | public | — |
| `get_is_filled()` | method | `bool` | public | — |
| `d_polyline_on_sphere` | field | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | private | — |
| `d_colour` | field | `GPlatesGui::ColourProxy` | private | — |
| `d_line_width_hint` | field | `float` | private | — |
| `d_is_filled` | field | `bool` | private | — |
| `d_fill_modulate_colour` | field | `GPlatesGui::Colour` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDPOLYLINEONSPHERE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 2 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 1 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 1 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedPolylineOnSphere.h
python scripts/gpq.py def GPlatesViewOperations::RenderedPolylineOnSphere --body
python scripts/gpq.py uses RenderedPolylineOnSphere --kind class
python scripts/gpq.py hier RenderedPolylineOnSphere
```

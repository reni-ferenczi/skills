# RenderedColouredPolylineOnSphere

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1226 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedColouredPolylineOnSphere.h` | C++ | 116 |

## Overview

A rendered representation of a `PolylineOnSphere` geometry where each point carries its own colour. The class holds the underlying polyline geometry, a vector of `ColourProxy` values (one per point), and a width hint for rendering. It implements the visitor pattern and provides proximity testing on both the geometry and its individual vertices.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedColouredPolylineOnSphere`](#gplatesviewoperationsrenderedcolouredpolylineonsphere) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | — |

## Members

### `GPlatesViewOperations::RenderedColouredPolylineOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedColouredPolylineOnSphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere, const std::vector<GPlatesGui::ColourProxy> &point_colours, float line_width_hint)` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `test_vertex_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `get_polyline_on_sphere()` | method | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | public | — |
| `get_line_width_hint()` | method | `float` | public | — |
| `d_polyline_on_sphere` | field | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | private | — |
| `d_point_colours` | field | `std::vector<GPlatesGui::ColourProxy>` | private | — |
| `d_line_width_hint` | field | `float` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDCOLOUREDPOLYLINEONSPHERE_H` | macro | `None` | — |

## Notes

The number of colours must match the number of polyline points. Proximity testing applies only to the line geometry itself, not to any filled region (since polylines are rendered as stroked paths).

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 2 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 2 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedColouredPolylineOnSphere.h
python scripts/gpq.py def GPlatesViewOperations::RenderedColouredPolylineOnSphere --body
python scripts/gpq.py uses RenderedColouredPolylineOnSphere --kind class
python scripts/gpq.py hier RenderedColouredPolylineOnSphere
```

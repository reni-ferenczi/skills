# RenderedColouredPolygonOnSphere

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1225 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedColouredPolygonOnSphere.h` | C++ | 117 |

## Overview

A rendered representation of a `PolygonOnSphere` geometry where each exterior-ring point carries its own colour. The class holds the underlying polygon geometry, a vector of `ColourProxy` values (one per exterior-ring point), and a width hint for rendering the outline. It implements the visitor pattern and provides proximity testing on both the geometry outline and its individual vertices. Polygon-coloured geometries are drawn as outlines only, not as filled regions.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedColouredPolygonOnSphere`](#gplatesviewoperationsrenderedcolouredpolygononsphere) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | — |

## Members

### `GPlatesViewOperations::RenderedColouredPolygonOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedColouredPolygonOnSphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere, const std::vector<GPlatesGui::ColourProxy> &point_colours, float line_width_hint)` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `test_vertex_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `get_polygon_on_sphere()` | method | `GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type` | public | — |
| `get_line_width_hint()` | method | `float` | public | — |
| `d_polygon_on_sphere` | field | `GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type` | private | — |
| `d_point_colours` | field | `std::vector<GPlatesGui::ColourProxy>` | private | — |
| `d_line_width_hint` | field | `float` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDCOLOUREDPOLYGONONSPHERE_H` | macro | `None` | — |

## Notes

Only the exterior ring points are coloured; interior ring (hole) points are ignored. Proximity testing applies only to the outline, never to the polygon's interior, because these geometries are drawn as stroked paths rather than filled regions.

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
python scripts/gpq.py file src/view-operations/RenderedColouredPolygonOnSphere.h
python scripts/gpq.py def GPlatesViewOperations::RenderedColouredPolygonOnSphere --body
python scripts/gpq.py uses RenderedColouredPolygonOnSphere --kind class
python scripts/gpq.py hier RenderedColouredPolygonOnSphere
```

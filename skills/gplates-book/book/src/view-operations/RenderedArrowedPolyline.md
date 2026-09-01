# RenderedArrowedPolyline

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1173 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedArrowedPolyline.h` | C++ | 111 |

## Overview

A `RenderedGeometryImpl` that represents a polyline with arrows for rendering on the globe or map view. It wraps a `PolylineOnSphere` with a colour and rendering parameters (arrowhead size and line width) and participates in the visitor pattern so that renderers in the `gui` module can draw it appropriately.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedArrowedPolyline`](#gplatesviewoperationsrenderedarrowedpolyline) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | — |

## Members

### `GPlatesViewOperations::RenderedArrowedPolyline`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedArrowedPolyline( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type points, const GPlatesGui::ColourProxy &colour, float arrowhead_size_in_pixels, float arrowline_width_hint)` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `test_vertex_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `get_polyline_on_sphere()` | method | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | public | — |
| `get_arrowhead_size_in_pixels()` | method | `float` | public | The size of the arrowhead (in device-independent pixels). |
| `get_arrowline_width_hint()` | method | `float` | public | The arrow line width (in device-independent pixels). |
| `d_points` | field | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | private | — |
| `d_colour` | field | `GPlatesGui::ColourProxy` | private | — |
| `d_arrowhead_size_in_pixels` | field | `float` | private | — |
| `d_arrowline_width_hint` | field | `float` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDARROWEDPOLYLINE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 4 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 4 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedArrowedPolyline.h
python scripts/gpq.py def GPlatesViewOperations::RenderedArrowedPolyline --body
python scripts/gpq.py uses RenderedArrowedPolyline --kind class
python scripts/gpq.py hier RenderedArrowedPolyline
```

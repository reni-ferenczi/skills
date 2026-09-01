# RenderedPointOnSphere

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1342 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedPointOnSphere.h` | C++ | 99 |

## Overview

A rendered geometry wrapper for a point on a sphere, holding a `PointOnSphere`, a `ColourProxy` for display properties, and a point size hint for rendering. The class participates in the visitor pattern for geometry traversal and delegates proximity testing to the underlying point, allowing click detection and vertex selection in interactive tools.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedPointOnSphere`](#gplatesviewoperationsrenderedpointonsphere) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | — |

## Members

### `GPlatesViewOperations::RenderedPointOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedPointOnSphere( const GPlatesMaths::PointOnSphere &point_on_sphere, const GPlatesGui::ColourProxy &colour, float point_size_hint)` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `test_vertex_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `get_point_size_hint()` | method | `float` | public | — |
| `d_point_on_sphere` | field | `GPlatesMaths::PointOnSphere` | private | — |
| `d_colour` | field | `GPlatesGui::ColourProxy` | private | — |
| `d_point_size_hint` | field | `float` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDPOINTONSPHERE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 1 |
| [canvas-tools/SelectHellingerGeometries](../canvas-tools/SelectHellingerGeometries.md) | canvas-tools | 1 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 1 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 1 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 1 |
| [view-operations/RenderedGeometryLayer](RenderedGeometryLayer.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedPointOnSphere.h
python scripts/gpq.py def GPlatesViewOperations::RenderedPointOnSphere --body
python scripts/gpq.py uses RenderedPointOnSphere --kind class
python scripts/gpq.py hier RenderedPointOnSphere
```

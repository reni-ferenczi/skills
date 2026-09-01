# RenderedMultiPointOnSphere

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1284 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedMultiPointOnSphere.h` | C++ | 99 |

## Overview

A concrete `RenderedGeometryImpl` that wraps a `MultiPointOnSphere` for rendering. Stores the underlying geometry, its display color, and a size hint for point rendering. Implements the visitor pattern via `accept_visitor()` to allow traversal by rendering engines, and delegates proximity testing to the contained `MultiPointOnSphere` to support point selection operations.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedMultiPointOnSphere`](#gplatesviewoperationsrenderedmultipointonsphere) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | — |

## Members

### `GPlatesViewOperations::RenderedMultiPointOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedMultiPointOnSphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere, const GPlatesGui::ColourProxy &colour, float point_size_hint)` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `test_vertex_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `get_multi_point_on_sphere()` | method | `GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type` | public | — |
| `get_point_size_hint()` | method | `float` | public | — |
| `d_multi_point_on_sphere` | field | `GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type` | private | — |
| `d_colour` | field | `GPlatesGui::ColourProxy` | private | — |
| `d_point_size_hint` | field | `float` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDMULTIPOINTONSPHERE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 3 |
| [canvas-tools/SelectHellingerGeometries](../canvas-tools/SelectHellingerGeometries.md) | canvas-tools | 3 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 1 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 1 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedMultiPointOnSphere.h
python scripts/gpq.py def GPlatesViewOperations::RenderedMultiPointOnSphere --body
python scripts/gpq.py uses RenderedMultiPointOnSphere --kind class
python scripts/gpq.py hier RenderedMultiPointOnSphere
```

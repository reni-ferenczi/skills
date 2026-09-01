# RenderedTriangleSymbol

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1176 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedTriangleSymbol.h` | C++ | 122 |

## Overview

A rendered geometry wrapper for an equilateral triangle symbol positioned at a `PointOnSphere`. The triangle is north-south aligned, with one altitude running along the meridian. Like `RenderedSquareSymbol`, it supports optional fill and a configurable size, storing the centre position, visual properties (colour, fill flag, size), and a line-width hint for rendering. Proximity testing delegates to the centre point, allowing the triangle to be selectable via its centre location.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedTriangleSymbol`](#gplatesviewoperationsrenderedtrianglesymbol) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | First attempt at rendered equilateral triangle. |

## Members

### `GPlatesViewOperations::RenderedTriangleSymbol`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedTriangleSymbol( const GPlatesMaths::PointOnSphere &centre, const GPlatesGui::ColourProxy &colour, unsigned int size, bool filled, float line_width_hint)` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `get_line_width_hint()` | method | `float` | public | — |
| `get_is_filled()` | method | `bool` | public | — |
| `get_size()` | method | `unsigned int` | public | — |
| `d_centre` | field | `GPlatesMaths::PointOnSphere` | private | — |
| `d_colour` | field | `GPlatesGui::ColourProxy` | private | — |
| `d_size` | field | `unsigned int` | private | — |
| `d_is_filled` | field | `bool` | private | — |
| `d_line_width_hint` | field | `float` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDTRIANGLESYMBOL_H` | macro | `None` | — |

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

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedTriangleSymbol.h
python scripts/gpq.py def GPlatesViewOperations::RenderedTriangleSymbol --body
python scripts/gpq.py uses RenderedTriangleSymbol --kind class
python scripts/gpq.py hier RenderedTriangleSymbol
```

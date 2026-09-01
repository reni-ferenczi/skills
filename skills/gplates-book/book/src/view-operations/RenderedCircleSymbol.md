# RenderedCircleSymbol

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 436 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedCircleSymbol.h` | C++ | 119 |

## Overview

`RenderedCircleSymbol` is a header-only `RenderedGeometryImpl` for a filled or outlined circle symbol centred on a point on the sphere, drawn by `GlobeRenderedGeometryLayerPainter`/`MapRenderedGeometryLayerPainter` and used by canvas tools such as `AdjustFittedPoleEstimate` and `SelectHellingerGeometries` to mark a point of interest with a circle instead of the usual point marker. Its own doc comment calls it a "first attempt", flagging it as a minimal implementation rather than a fully worked-out symbol type.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedCircleSymbol`](#gplatesviewoperationsrenderedcirclesymbol) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | First attempt at rendered circle. |

## Members

### `GPlatesViewOperations::RenderedCircleSymbol`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedCircleSymbol( const GPlatesMaths::PointOnSphere &centre, const GPlatesGui::ColourProxy &colour, unsigned int size, bool filled, float line_width_hint)` | constructor | `None` | public | — |
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
| `GPLATES_VIEWOPERATIONS_RENDEREDCIRCLESYMBOL_H` | macro | `None` | — |

## Notes

`test_proximity` delegates entirely to the centre `PointOnSphere`'s own proximity test, so `d_size` and `d_line_width_hint` are purely display hints for the painters (pixel-space circle radius and outline width) and have no effect on hit-testing — a large rendered circle is no easier to click than a bare point at its centre.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 26 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 25 |
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 17 |
| [canvas-tools/SelectHellingerGeometries](../canvas-tools/SelectHellingerGeometries.md) | canvas-tools | 14 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedCircleSymbol.h
python scripts/gpq.py def GPlatesViewOperations::RenderedCircleSymbol --body
python scripts/gpq.py uses RenderedCircleSymbol --kind class
python scripts/gpq.py hier RenderedCircleSymbol
```

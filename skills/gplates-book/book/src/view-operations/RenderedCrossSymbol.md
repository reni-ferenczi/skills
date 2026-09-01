# RenderedCrossSymbol

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1282 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedCrossSymbol.h` | C++ | 111 |

## Overview

A rendered visual symbol of a cross at a location on the sphere. The cross is north-south aligned, with one arm pointing north and the other pointing south, centred at the specified `PointOnSphere`. The class stores the centre point, a colour, a size in pixels, and a line width hint for rendering.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedCrossSymbol`](#gplatesviewoperationsrenderedcrosssymbol) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | Rendered cross geometry. |

## Members

### `GPlatesViewOperations::RenderedCrossSymbol`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedCrossSymbol( const GPlatesMaths::PointOnSphere &centre, const GPlatesGui::ColourProxy &colour, unsigned int size, float line_width_hint)` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `get_line_width_hint()` | method | `float` | public | — |
| `get_size()` | method | `unsigned int` | public | — |
| `d_centre` | field | `GPlatesMaths::PointOnSphere` | private | — |
| `d_colour` | field | `GPlatesGui::ColourProxy` | private | — |
| `d_size` | field | `unsigned int` | private | — |
| `d_line_width_hint` | field | `float` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDCROSSSYMBOL_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 2 |
| [canvas-tools/SelectHellingerGeometries](../canvas-tools/SelectHellingerGeometries.md) | canvas-tools | 2 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 2 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 2 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedCrossSymbol.h
python scripts/gpq.py def GPlatesViewOperations::RenderedCrossSymbol --body
python scripts/gpq.py uses RenderedCrossSymbol --kind class
python scripts/gpq.py hier RenderedCrossSymbol
```

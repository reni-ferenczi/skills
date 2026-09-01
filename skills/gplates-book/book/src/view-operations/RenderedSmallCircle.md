# RenderedSmallCircle

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 436 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedSmallCircle.h` | C++ | 133 |

## Overview

A rendered geometry wrapper for a small circle on a sphere, defined by an axis (pole) and a colatitude (radius). Holds the circle, its display colour, and line width hint. Proximity testing computes the angular distance from the test point to the circle's axis and uses that to find the closest point on the circle, returning a closeness measure based on the angular separation. This enables interactive selection of plate motion circles and other geographic constraints.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedSmallCircle`](#gplatesviewoperationsrenderedsmallcircle) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | — |

## Members

### `GPlatesViewOperations::RenderedSmallCircle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedSmallCircle( const GPlatesMaths::SmallCircle &small_circle, const GPlatesGui::ColourProxy &colour, float line_width_hint)` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `get_line_width_hint()` | method | `float` | public | — |
| `d_small_circle` | field | `GPlatesMaths::SmallCircle` | private | — |
| `d_colour` | field | `GPlatesGui::ColourProxy` | private | — |
| `d_line_width_hint` | field | `float` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDSMALLCIRCLE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 1 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 1 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 1 |
| [view-operations/RenderedGeometryLayer](RenderedGeometryLayer.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedSmallCircle.h
python scripts/gpq.py def GPlatesViewOperations::RenderedSmallCircle --body
python scripts/gpq.py uses RenderedSmallCircle --kind class
python scripts/gpq.py hier RenderedSmallCircle
```

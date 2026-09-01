# RenderedSmallCircleArc

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 645 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedSmallCircleArc.h` | C++ | 97 |

## Overview

[[[PROSE overview unit=view-operations/RenderedSmallCircleArc tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedSmallCircleArc`](#gplatesviewoperationsrenderedsmallcirclearc) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | — |

## Members

### `GPlatesViewOperations::RenderedSmallCircleArc`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedSmallCircleArc( const GPlatesMaths::SmallCircleArc &small_circle_arc, const GPlatesGui::ColourProxy &colour, float line_width_hint)` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `get_line_width_hint()` | method | `float` | public | — |
| `d_small_circle_arc` | field | `GPlatesMaths::SmallCircleArc` | private | The small circle arc. |
| `d_colour` | field | `GPlatesGui::ColourProxy` | private | — |
| `d_line_width_hint` | field | `float` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDSMALLCIRCLEARC_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=view-operations/RenderedSmallCircleArc tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 1 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 1 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedSmallCircleArc.h
python scripts/gpq.py def GPlatesViewOperations::RenderedSmallCircleArc --body
python scripts/gpq.py uses RenderedSmallCircleArc --kind class
python scripts/gpq.py hier RenderedSmallCircleArc
```

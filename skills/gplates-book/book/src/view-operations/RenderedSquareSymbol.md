# RenderedSquareSymbol

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1175 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedSquareSymbol.h` | C++ | 120 |

## Overview

[[[PROSE overview unit=view-operations/RenderedSquareSymbol tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedSquareSymbol`](#gplatesviewoperationsrenderedsquaresymbol) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | First attempt at rendered square. |

## Members

### `GPlatesViewOperations::RenderedSquareSymbol`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedSquareSymbol( const GPlatesMaths::PointOnSphere &centre, const GPlatesGui::ColourProxy &colour, unsigned int size, bool filled, float line_width_hint)` | constructor | `None` | public | — |
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
| `GPLATES_VIEWOPERATIONS_RENDEREDSQUARESYMBOL_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=view-operations/RenderedSquareSymbol tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
python scripts/gpq.py file src/view-operations/RenderedSquareSymbol.h
python scripts/gpq.py def GPlatesViewOperations::RenderedSquareSymbol --body
python scripts/gpq.py uses RenderedSquareSymbol --kind class
python scripts/gpq.py hier RenderedSquareSymbol
```

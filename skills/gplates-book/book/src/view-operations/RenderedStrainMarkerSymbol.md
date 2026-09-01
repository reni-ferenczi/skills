# RenderedStrainMarkerSymbol

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1119 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedStrainMarkerSymbol.h` | C++ | 116 |

## Overview

[[[PROSE overview unit=view-operations/RenderedStrainMarkerSymbol tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedStrainMarkerSymbol`](#gplatesviewoperationsrenderedstrainmarkersymbol) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | Rendered strain marker geometry. |

## Members

### `GPlatesViewOperations::RenderedStrainMarkerSymbol`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedStrainMarkerSymbol( const GPlatesMaths::PointOnSphere &centre, unsigned int size, double scale_x, double scale_y, double angle)` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `get_size()` | method | `unsigned int` | public | — |
| `get_scale_x()` | method | `double` | public | — |
| `get_scale_y()` | method | `double` | public | — |
| `get_angle()` | method | `double` | public | — |
| `d_centre` | field | `GPlatesMaths::PointOnSphere` | private | — |
| `d_size` | field | `unsigned int` | private | — |
| `d_scale_x` | field | `double` | private | — |
| `d_scale_y` | field | `double` | private | — |
| `d_angle` | field | `double` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDSTRAINMARKERSYMBOL_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=view-operations/RenderedStrainMarkerSymbol tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 4 |
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 3 |
| [maths/AngularExtent](../maths/AngularExtent.md) | maths | 2 |
| [maths/DateLineWrapper](../maths/DateLineWrapper.md) | maths | 2 |
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 1 |
| [canvas-tools/SelectHellingerGeometries](../canvas-tools/SelectHellingerGeometries.md) | canvas-tools | 1 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedStrainMarkerSymbol.h
python scripts/gpq.py def GPlatesViewOperations::RenderedStrainMarkerSymbol --body
python scripts/gpq.py uses RenderedStrainMarkerSymbol --kind class
python scripts/gpq.py hier RenderedStrainMarkerSymbol
```

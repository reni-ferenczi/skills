# RenderedStrainMarkerSymbol

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1119 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedStrainMarkerSymbol.h` | C++ | 116 |

## Overview

A rendered geometry wrapper for a strain marker symbol, used to visualize strain-rate or geodetic strain ellipses at a location on the globe. The class stores a centre `PointOnSphere`, plus shape parameters: a base size, separate scale factors in x and y directions to represent ellipticity, and a rotation angle to orient the ellipse. These parameters allow efficient representation of strain ellipses without storing the full ellipse geometry. Proximity testing delegates to the centre point.

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

*None.*

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

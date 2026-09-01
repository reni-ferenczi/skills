# RenderedRadialArrow

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 882 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedRadialArrow.h` | C++ | 236 |

## Overview

`RenderedRadialArrow` is a `RenderedGeometryImpl` for an arrow that stands normal to the globe's surface at a point, used to depict things like poles and light direction that have no natural on-globe extent. Because such an arrow points out of the screen in the 2D map views, it is only actually drawn as an arrow in the 3D globe view; in map view only its base symbol is shown.

The arrow's length, arrowhead size and body width are stored as *projected* sizes — proportions of the fully-zoomed-out globe radius — so that the arrow keeps a constant apparent size on screen as the view zooms, rather than being defined in world-space units. The base symbol is one of a small set of circularly symmetric shapes (`SymbolType`) chosen to match the circular cross-section of the arrow's cylindrical body in globe view; in map view the symbol is drawn at its own, separately specified, scene-space size.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedRadialArrow`](#gplatesviewoperationsrenderedradialarrow) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | An arrow that is radial, or normal, to the globe's surface. |

## Members

### `GPlatesViewOperations::RenderedRadialArrow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SymbolType` | enum | `None` | public | The types of (circularly symmetric) symbols used in map view and at base of arrow in globe view. |
| `RenderedRadialArrow( const GPlatesMaths::PointOnSphere &position, float arrow_projected_length, float arrowhead_projected_size, float arrowline_projected_width, const GPlatesGui::ColourProxy &arrow_colour, SymbolType symbol_type, float symbol_size, const GPlatesGui::ColourProxy &symbol_colour)` | constructor | `None` | public | In globe view the symbol size matches the size of the arrow (cylindrical) body. |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | No hit detection performed because the arrow's geometry is \*off\* the globe and also is scaled by the viewport zoom and hence its geometry is not known until it is rendered. |
| `get_arrow_projected_length()` | method | `float` | public | Returns the length of the arrow projected onto the viewport window. |
| `get_arrowhead_projected_size()` | method | `float` | public | Returns the size of the arrowhead projected onto the viewport window. |
| `get_projected_arrowline_width()` | method | `float` | public | Returns the width of the arrow body projected onto the viewport window. |
| `get_symbol_type()` | method | `SymbolType` | public | Returns the type of the symbol. |
| `get_symbol_size()` | method | `float` | public | Returns the size of the symbol. |
| `d_position` | field | `GPlatesMaths::PointOnSphere` | private | — |
| `d_arrow_projected_length` | field | `float` | private | — |
| `d_arrowhead_projected_size` | field | `float` | private | — |
| `d_arrowline_projected_width` | field | `float` | private | — |
| `d_arrow_colour` | field | `GPlatesGui::ColourProxy` | private | — |
| `d_symbol_type` | field | `SymbolType` | private | — |
| `d_symbol_size` | field | `float` | private | — |
| `d_symbol_colour` | field | `GPlatesGui::ColourProxy` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDRADIALARROW_H` | macro | `None` | — |

## Notes

`test_proximity` always returns null: the arrow's on-screen geometry depends on viewport zoom and is not known until render time, so proximity/hit-testing against it is not supported (marked as a `FIXME` in the header).

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 11 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 9 |
| [view-operations/ChangeLightDirectionOperation](ChangeLightDirectionOperation.md) | view-operations | 5 |
| [view-operations/MovePoleOperation](MovePoleOperation.md) | view-operations | 5 |
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 4 |
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 4 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 3 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 1 |
| [view-operations/RenderedGeometryLayer](RenderedGeometryLayer.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedRadialArrow.h
python scripts/gpq.py def GPlatesViewOperations::RenderedRadialArrow --body
python scripts/gpq.py uses RenderedRadialArrow --kind class
python scripts/gpq.py hier RenderedRadialArrow
```

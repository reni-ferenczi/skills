# RenderedSubductionTeethPolyline

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 834 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedSubductionTeethPolyline.h` | C++ | 139 |

## Overview

`RenderedSubductionTeethPolyline` is a `RenderedGeometryImpl` that wraps a `GPlatesMaths::PolylineOnSphere` together with the styling needed to draw it as a subduction zone: a triangular-tooth decoration along one side of the line, conventionally used to mark which plate is subducting. `SubductionPolarity` records which side of the polyline (`LEFT` or `RIGHT`) the teeth point towards, and the remaining fields are painter hints — line width, tooth width and the tooth spacing/height expressed as ratios of tooth width — rather than geometry, leaving the actual tessellation of the teeth to the painter.

Proximity and vertex-proximity testing simply delegate to the underlying `PolylineOnSphere`, so this class behaves like an ordinary polyline for hit-testing purposes even though it renders with extra decoration.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedSubductionTeethPolyline`](#gplatesviewoperationsrenderedsubductionteethpolyline) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | A polyline with subduction teeth. |

## Members

### `GPlatesViewOperations::RenderedSubductionTeethPolyline`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SubductionPolarity` | enum | `None` | public | — |
| `RenderedSubductionTeethPolyline( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere, SubductionPolarity subduction_polarity, const GPlatesGui::ColourProxy &colour, float line_width_hint, float teeth_width_in_pixels, float teeth_spacing_to_width_ratio, float teeth_height_to_width_ratio)` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor &visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `test_vertex_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `get_polyline_on_sphere()` | method | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | public | — |
| `get_subduction_polarity()` | method | `SubductionPolarity` | public | — |
| `get_line_width_hint()` | method | `float` | public | The line width (in device-independent pixels). |
| `get_teeth_width_in_pixels()` | method | `float` | public | The width of a tooth (in device-independent pixels). |
| `get_teeth_spacing_to_width_ratio()` | method | `float` | public | — |
| `get_teeth_height_to_width_ratio()` | method | `float` | public | — |
| `d_polyline_on_sphere` | field | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | private | — |
| `d_subduction_polarity` | field | `SubductionPolarity` | private | — |
| `d_colour` | field | `GPlatesGui::ColourProxy` | private | — |
| `d_line_width_hint` | field | `float` | private | — |
| `d_teeth_width_in_pixels` | field | `float` | private | — |
| `d_teeth_spacing_to_width_ratio` | field | `float` | private | — |
| `d_teeth_height_to_width_ratio` | field | `float` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDERED_SUBDUCTION_TEETH_POLYLINE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 7 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 7 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedSubductionTeethPolyline.h
python scripts/gpq.py def GPlatesViewOperations::RenderedSubductionTeethPolyline --body
python scripts/gpq.py uses RenderedSubductionTeethPolyline --kind class
python scripts/gpq.py hier RenderedSubductionTeethPolyline
```

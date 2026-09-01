# RenderedEllipse

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1174 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedEllipse.h` | C++ | 132 |

## Overview

A rendered representation of an ellipse on the sphere, defined by a centre point, semi-major and semi-minor axes (in radians), and a `GreatCircle` that orients the ellipse. The class stores colour and rendering width hint. It implements the visitor pattern and provides proximity testing (not yet implemented).

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedEllipse`](#gplatesviewoperationsrenderedellipse) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | — |

## Members

### `GPlatesViewOperations::RenderedEllipse`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedEllipse( const GPlatesMaths::PointOnSphere &centre, const GPlatesMaths::Real &semi_major_axis_radians, const GPlatesMaths::Real &semi_minor_axis_radians, const GPlatesMaths::GreatCircle &axis, const GPlatesGui::ColourProxy &colour, float line_width_hint)` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `get_line_width_hint()` | method | `float` | public | — |
| `d_centre` | field | `GPlatesMaths::PointOnSphere` | private | The centre of the ellipse. |
| `d_semi_major_axis_radians` | field | `GPlatesMaths::Real` | private | The semi-major axis of the ellipse, in radians. |
| `d_semi_minor_axis_radians` | field | `GPlatesMaths::Real` | private | The semi-minor axis of the ellipse, in radians |
| `d_axis` | field | `GPlatesMaths::GreatCircle` | private | The orientation of the ellipse. |
| `d_colour` | field | `GPlatesGui::ColourProxy` | private | — |
| `d_line_width_hint` | field | `float` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDELLIPSE_H` | macro | `None` | — |

## Notes

Proximity testing is not yet implemented (returns NULL). The semi-major axis is oriented along the `GreatCircle` axis.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 3 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 2 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedEllipse.h
python scripts/gpq.py def GPlatesViewOperations::RenderedEllipse --body
python scripts/gpq.py uses RenderedEllipse --kind class
python scripts/gpq.py hier RenderedEllipse
```

# RenderedTangentialArrow

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 957 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedTangentialArrow.h` | C++ | 192 |

## Overview

[[[PROSE overview unit=view-operations/RenderedTangentialArrow tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedTangentialArrow`](#gplatesviewoperationsrenderedtangentialarrow) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | An arrow that is tangential to the globe's surface. |

## Members

### `GPlatesViewOperations::RenderedTangentialArrow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedTangentialArrow( const GPlatesMaths::PointOnSphere &start, const GPlatesMaths::Vector3D &arrow_direction, float arrowhead_projected_size, float max_ratio_arrowhead_to_arrowline_length, const GPlatesGui::ColourProxy &colour, float globe_view_ratio_arrowline_width_to_arrowhead_size, float map_view_arrowline_width ...` | constructor | `None` | public | Note that even though the arrow direction is not constrained to be tangential to the globe's surface (because it can be an arbitrary vector), in the 2D map views only the tangential component is rendered. |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | No hit detection performed because a rendered arrow is not meant to be picked or selected by the user. |
| `get_arrowhead_projected_size()` | method | `float` | public | Returns the size of the arrowhead projected onto the viewport window. |
| `get_max_ratio_arrowhead_to_arrowline_length()` | method | `float` | public | Returns the maximum ratio of arrowhead size to arrowline length. |
| `get_globe_view_ratio_arrowline_width_to_arrowhead_size()` | method | `float` | public | The ratio of arrow line width to arrow head size. |
| `get_map_view_arrowline_width_hint()` | method | `float` | public | The 2D map views render arrow body as an anti-aliased line primitive. |
| `d_start_position` | field | `GPlatesMaths::PointOnSphere` | private | — |
| `d_arrow_direction` | field | `GPlatesMaths::Vector3D` | private | — |
| `d_arrowhead_projected_size` | field | `float` | private | — |
| `d_max_ratio_arrowhead_to_arrowline_length` | field | `float` | private | — |
| `d_colour` | field | `GPlatesGui::ColourProxy` | private | — |
| `d_globe_view_ratio_arrowline_width_to_arrowhead_size` | field | `float` | private | — |
| `d_map_view_arrowline_width_hint` | field | `float` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDTANGENTIALARROW_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=view-operations/RenderedTangentialArrow tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 3 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 3 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 1 |
| [view-operations/RenderedGeometryLayer](RenderedGeometryLayer.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedTangentialArrow.h
python scripts/gpq.py def GPlatesViewOperations::RenderedTangentialArrow --body
python scripts/gpq.py uses RenderedTangentialArrow --kind class
python scripts/gpq.py hier RenderedTangentialArrow
```

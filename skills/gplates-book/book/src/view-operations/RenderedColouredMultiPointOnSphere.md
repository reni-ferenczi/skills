# RenderedColouredMultiPointOnSphere

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1224 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedColouredMultiPointOnSphere.h` | C++ | 114 |

## Overview

[[[PROSE overview unit=view-operations/RenderedColouredMultiPointOnSphere tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedColouredMultiPointOnSphere`](#gplatesviewoperationsrenderedcolouredmultipointonsphere) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | — |

## Members

### `GPlatesViewOperations::RenderedColouredMultiPointOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedColouredMultiPointOnSphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere, const std::vector<GPlatesGui::ColourProxy> &point_colours, float point_size_hint)` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `test_vertex_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `get_multi_point_on_sphere()` | method | `GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type` | public | — |
| `get_point_size_hint()` | method | `float` | public | — |
| `d_multi_point_on_sphere` | field | `GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type` | private | — |
| `d_point_colours` | field | `std::vector<GPlatesGui::ColourProxy>` | private | — |
| `d_point_size_hint` | field | `float` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDCOLOUREDMULTIPOINTONSPHERE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=view-operations/RenderedColouredMultiPointOnSphere tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 5 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 5 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedColouredMultiPointOnSphere.h
python scripts/gpq.py def GPlatesViewOperations::RenderedColouredMultiPointOnSphere --body
python scripts/gpq.py uses RenderedColouredMultiPointOnSphere --kind class
python scripts/gpq.py hier RenderedColouredMultiPointOnSphere
```

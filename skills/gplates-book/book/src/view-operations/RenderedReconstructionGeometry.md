# RenderedReconstructionGeometry

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1457 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedReconstructionGeometry.h` | C++ | 88 |

## Overview

[[[PROSE overview unit=view-operations/RenderedReconstructionGeometry tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedReconstructionGeometry`](#gplatesviewoperationsrenderedreconstructiongeometry) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | — |

## Members

### `GPlatesViewOperations::RenderedReconstructionGeometry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedReconstructionGeometry( GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type reconstruction_geom, RenderedGeometry rendered_geom)` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `test_vertex_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `d_reconstruction_geom` | field | `GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type` | private | — |
| `d_rendered_geom` | field | `RenderedGeometry` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDRECONSTRUCTIONGEOMETRY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=view-operations/RenderedReconstructionGeometry tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/MoveVertexGeometryOperation](MoveVertexGeometryOperation.md) | view-operations | 1 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 1 |
| [view-operations/RenderedGeometryUtils](RenderedGeometryUtils.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedReconstructionGeometry.h
python scripts/gpq.py def GPlatesViewOperations::RenderedReconstructionGeometry --body
python scripts/gpq.py uses RenderedReconstructionGeometry --kind class
python scripts/gpq.py hier RenderedReconstructionGeometry
```

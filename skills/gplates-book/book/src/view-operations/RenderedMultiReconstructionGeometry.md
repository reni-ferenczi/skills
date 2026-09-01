# RenderedMultiReconstructionGeometry

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1403 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedMultiReconstructionGeometry.h` | C++ | 84 |

## Overview

A wrapper that combines a vector of `ReconstructionGeometry` objects with a single `RenderedGeometry`. This class implements the visitor pattern, allowing geometry traversal operations to visit both the reconstruction geometries and the rendered representation. Proximity testing (for click detection and vertex selection) delegates to the wrapped rendered geometry, while visitor acceptance traverses both the geometry list and the internal rendered form.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedMultiReconstructionGeometry`](#gplatesviewoperationsrenderedmultireconstructiongeometry) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | — |

## Members

### `GPlatesViewOperations::RenderedMultiReconstructionGeometry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedMultiReconstructionGeometry( const std::vector<GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type> &reconstruction_geoms, RenderedGeometry rendered_geom)` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `test_vertex_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `d_reconstruction_geoms` | field | `std::vector<GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type>` | private | — |
| `d_rendered_geom` | field | `RenderedGeometry` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDMULTIRECONSTRUCTIONGEOMETRY_H` | macro | `None` | — |

## Notes

*None.*

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
python scripts/gpq.py file src/view-operations/RenderedMultiReconstructionGeometry.h
python scripts/gpq.py def GPlatesViewOperations::RenderedMultiReconstructionGeometry --body
python scripts/gpq.py uses RenderedMultiReconstructionGeometry --kind class
python scripts/gpq.py hier RenderedMultiReconstructionGeometry
```

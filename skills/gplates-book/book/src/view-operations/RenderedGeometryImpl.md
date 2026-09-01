# RenderedGeometryImpl

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 436 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedGeometryImpl.h` | C++ | 88 |

## Overview

The abstract base every concrete rendered-geometry type (`RenderedPointOnSphere`, `RenderedPolylineOnSphere`, the coloured meshes, the symbol and arrow types, and 20-odd others) implements. `RenderedGeometry` is the pimpl handle that holds one of these behind a `non_null_ptr_type`; this class is the interface that makes that indirection possible, and reference counting via `GPlatesUtils::ReferenceCount` is what lets the handle be copied cheaply.

`test_vertex_proximity()` has a default implementation returning no hit, since — per the header comment — vertex proximity is only meaningful for implementations that wrap a `GeometryOnSphere` with actual vertices; subclasses that do (points, polylines, polygons, meshes) override it, and the rest simply inherit the no-op.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedGeometryImpl`](#gplatesviewoperationsrenderedgeometryimpl) | class | [`GPlatesUtils::ReferenceCount<RenderedGeometryImpl>`](../utils/ReferenceCount.md) | — | 26 | The interface for the implementation of RenderedGeometry. |

## Members

### `GPlatesViewOperations::RenderedGeometryImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<RenderedGeometryImpl>` | public | A convenience typedef for a shared pointer to a non-const RenderedGeometryImpl. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const RenderedGeometryImpl>` | public | A convenience typedef for a shared pointer to a const RenderedGeometryImpl. |
| `~RenderedGeometryImpl()` | destructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor&)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `test_vertex_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | Default implementation returns no hit since this method probably only makes sense for rendered geometries that wrap GeometryOnSphere types where interest in vertex proximity occurs. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYIMPL_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/RenderedArrowedPolyline](RenderedArrowedPolyline.md) | view-operations | 3 |
| [view-operations/RenderedCircleSymbol](RenderedCircleSymbol.md) | view-operations | 3 |
| [view-operations/RenderedColouredEdgeSurfaceMesh](RenderedColouredEdgeSurfaceMesh.md) | view-operations | 3 |
| [view-operations/RenderedColouredMultiPointOnSphere](RenderedColouredMultiPointOnSphere.md) | view-operations | 3 |
| [view-operations/RenderedColouredPolygonOnSphere](RenderedColouredPolygonOnSphere.md) | view-operations | 3 |
| [view-operations/RenderedColouredPolylineOnSphere](RenderedColouredPolylineOnSphere.md) | view-operations | 3 |
| [view-operations/RenderedColouredTriangleSurfaceMesh](RenderedColouredTriangleSurfaceMesh.md) | view-operations | 3 |
| [view-operations/RenderedCrossSymbol](RenderedCrossSymbol.md) | view-operations | 3 |
| [view-operations/RenderedEllipse](RenderedEllipse.md) | view-operations | 3 |
| [view-operations/RenderedGeometry](RenderedGeometry.md) | view-operations | 3 |
| [view-operations/RenderedMultiPointOnSphere](RenderedMultiPointOnSphere.md) | view-operations | 3 |
| [view-operations/RenderedPointOnSphere](RenderedPointOnSphere.md) | view-operations | 3 |
| [view-operations/RenderedPolygonOnSphere](RenderedPolygonOnSphere.md) | view-operations | 3 |
| [view-operations/RenderedPolylineOnSphere](RenderedPolylineOnSphere.md) | view-operations | 3 |
| [view-operations/RenderedRadialArrow](RenderedRadialArrow.md) | view-operations | 3 |
| [view-operations/RenderedResolvedRaster](RenderedResolvedRaster.md) | view-operations | 3 |
| [view-operations/RenderedResolvedScalarField3D](RenderedResolvedScalarField3D.md) | view-operations | 3 |
| [view-operations/RenderedSmallCircle](RenderedSmallCircle.md) | view-operations | 3 |
| [view-operations/RenderedSmallCircleArc](RenderedSmallCircleArc.md) | view-operations | 3 |
| [view-operations/RenderedSquareSymbol](RenderedSquareSymbol.md) | view-operations | 3 |

*... and 9 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedGeometryImpl.h
python scripts/gpq.py def GPlatesViewOperations::RenderedGeometryImpl --body
python scripts/gpq.py uses RenderedGeometryImpl --kind class
python scripts/gpq.py hier RenderedGeometryImpl
```

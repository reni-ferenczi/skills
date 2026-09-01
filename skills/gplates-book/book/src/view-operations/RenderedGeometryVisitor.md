# RenderedGeometryVisitor

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 133 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedGeometryVisitor.h` | C++ | 247 |

## Overview

The visitor interface that stands between `RenderedGeometry`'s pimpl handle and the many concrete `RenderedGeometryImpl` subclasses: `RenderedGeometry::accept_visitor()` dispatches to one `visit_rendered_*` method per concrete type, and every method takes its argument by const reference — the header notes this is deliberate, since `RenderedGeometry` objects are meant to be treated as immutable once built. Painters (`GlobeRenderedGeometryLayerPainter`, `MapRenderedGeometryLayerPainter`) and canvas tools that need to react differently per geometry kind subclass this rather than adding a type switch.

Every `visit_*` method has an empty default body, so a subclass only needs to override the handful of geometry kinds it actually cares about; unhandled kinds are silently skipped rather than causing a compile error or an assertion. `visit_rendered_reconstruction_geometry()` and `visit_rendered_multi_reconstruction_geometry()` are called out as composite objects, unlike the other, purely geometric kinds — they wrap the underlying `ReconstructionGeometry` (and, for the multi- variant, its per-instance associations) rather than describing a shape directly.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::ConstRenderedGeometryVisitor`](#gplatesviewoperationsconstrenderedgeometryvisitor) | class | — | — | 16 | Interface for visiting a derived RenderedGeometryImpl object. |

## Members

### `GPlatesViewOperations::ConstRenderedGeometryVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~ConstRenderedGeometryVisitor()` | destructor | `None` | public | — |
| `visit_rendered_arrowed_polyline( const GPlatesViewOperations::RenderedArrowedPolyline &)` | method | `void` | public | — |
| `visit_rendered_circle_symbol( const RenderedCircleSymbol &)` | method | `void` | public | — |
| `visit_rendered_coloured_edge_surface_mesh( const RenderedColouredEdgeSurfaceMesh &)` | method | `void` | public | — |
| `visit_rendered_coloured_triangle_surface_mesh( const RenderedColouredTriangleSurfaceMesh &)` | method | `void` | public | — |
| `visit_rendered_cross_symbol( const GPlatesViewOperations::RenderedCrossSymbol &)` | method | `void` | public | — |
| `visit_rendered_ellipse( const GPlatesViewOperations::RenderedEllipse &)` | method | `void` | public | — |
| `visit_rendered_point_on_sphere( const GPlatesViewOperations::RenderedPointOnSphere &)` | method | `void` | public | — |
| `visit_rendered_multi_point_on_sphere( const RenderedMultiPointOnSphere &)` | method | `void` | public | — |
| `visit_rendered_coloured_multi_point_on_sphere( const RenderedColouredMultiPointOnSphere &)` | method | `void` | public | — |
| `visit_rendered_polyline_on_sphere( const RenderedPolylineOnSphere &)` | method | `void` | public | — |
| `visit_rendered_coloured_polyline_on_sphere( const RenderedColouredPolylineOnSphere &)` | method | `void` | public | — |
| `visit_rendered_polygon_on_sphere( const RenderedPolygonOnSphere &)` | method | `void` | public | — |
| `visit_rendered_coloured_polygon_on_sphere( const RenderedColouredPolygonOnSphere &)` | method | `void` | public | — |
| `visit_rendered_radial_arrow( const RenderedRadialArrow &)` | method | `void` | public | — |
| `visit_rendered_reconstruction_geometry( const RenderedReconstructionGeometry &)` | method | `void` | public | This rendered geometry is a composite object as opposed to the others. |
| `visit_rendered_multi_reconstruction_geometry( const RenderedMultiReconstructionGeometry &)` | method | `void` | public | This rendered geometry is a composite object as opposed to the others. |
| `visit_rendered_resolved_raster( const RenderedResolvedRaster &)` | method | `void` | public | — |
| `visit_rendered_resolved_scalar_field_3d( const RenderedResolvedScalarField3D &)` | method | `void` | public | — |
| `visit_rendered_small_circle( const RenderedSmallCircle &)` | method | `void` | public | — |
| `visit_rendered_small_circle_arc( const RenderedSmallCircleArc &)` | method | `void` | public | — |
| `visit_rendered_square_symbol( const RenderedSquareSymbol &)` | method | `void` | public | — |
| `visit_rendered_strain_marker_symbol( const GPlatesViewOperations::RenderedStrainMarkerSymbol &)` | method | `void` | public | — |
| `visit_rendered_string( const RenderedString &)` | method | `void` | public | — |
| `visit_rendered_subduction_teeth_polyline( const RenderedSubductionTeethPolyline &)` | method | `void` | public | — |
| `visit_rendered_tangential_arrow( const RenderedTangentialArrow &)` | method | `void` | public | Note that this is not the same as a polyline with a symbol decoration. |
| `visit_rendered_triangle_symbol( const RenderedTriangleSymbol &)` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYVISITOR_H` | macro | `None` | — |

## Notes

Adding a new `RenderedGeometryImpl` subclass means adding a matching `visit_*` method here and to every existing subclass that needs to handle it specifically — the empty-default-body design means a forgotten override fails silently (the new geometry kind is just never visited) rather than failing to compile.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 45 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 22 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 17 |
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 10 |
| [canvas-tools/SelectHellingerGeometries](../canvas-tools/SelectHellingerGeometries.md) | canvas-tools | 5 |
| [view-operations/RenderedGeometryLayer](RenderedGeometryLayer.md) | view-operations | 4 |
| [view-operations/MoveVertexGeometryOperation](MoveVertexGeometryOperation.md) | view-operations | 3 |
| [view-operations/RenderedGeometryUtils](RenderedGeometryUtils.md) | view-operations | 3 |
| [view-operations/RenderedArrowedPolyline](RenderedArrowedPolyline.md) | view-operations | 2 |
| [view-operations/RenderedCircleSymbol](RenderedCircleSymbol.md) | view-operations | 2 |
| [view-operations/RenderedColouredEdgeSurfaceMesh](RenderedColouredEdgeSurfaceMesh.md) | view-operations | 2 |
| [view-operations/RenderedColouredMultiPointOnSphere](RenderedColouredMultiPointOnSphere.md) | view-operations | 2 |
| [view-operations/RenderedColouredPolygonOnSphere](RenderedColouredPolygonOnSphere.md) | view-operations | 2 |
| [view-operations/RenderedColouredPolylineOnSphere](RenderedColouredPolylineOnSphere.md) | view-operations | 2 |
| [view-operations/RenderedColouredTriangleSurfaceMesh](RenderedColouredTriangleSurfaceMesh.md) | view-operations | 2 |
| [view-operations/RenderedCrossSymbol](RenderedCrossSymbol.md) | view-operations | 2 |
| [view-operations/RenderedEllipse](RenderedEllipse.md) | view-operations | 2 |
| [view-operations/RenderedMultiPointOnSphere](RenderedMultiPointOnSphere.md) | view-operations | 2 |
| [view-operations/RenderedMultiReconstructionGeometry](RenderedMultiReconstructionGeometry.md) | view-operations | 2 |
| [view-operations/RenderedPointOnSphere](RenderedPointOnSphere.md) | view-operations | 2 |

*... and 19 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedGeometryVisitor.h
python scripts/gpq.py def GPlatesViewOperations::ConstRenderedGeometryVisitor --body
python scripts/gpq.py uses ConstRenderedGeometryVisitor --kind class
python scripts/gpq.py hier ConstRenderedGeometryVisitor
```

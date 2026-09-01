# RenderedResolvedScalarField3D

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 93 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedResolvedScalarField3D.h` | C++ | 107 |

## Overview

A rendered geometry wrapper for a 3D scalar field, holding a `ResolvedScalarField3D` and associated `ScalarField3DRenderParameters`. Scalar fields are volumetric data resolved at a specific reconstruction time, with rendering parameters controlling visualization (isosurface threshold, opacity, colour, etc.). This class integrates 3D data into the rendered geometry model for display on the globe.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedResolvedScalarField3D`](#gplatesviewoperationsrenderedresolvedscalarfield3d) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | — |

## Members

### `GPlatesViewOperations::RenderedResolvedScalarField3D`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedResolvedScalarField3D( const GPlatesAppLogic::ResolvedScalarField3D::non_null_ptr_to_const_type &resolved_scalar_field, const ScalarField3DRenderParameters &render_parameters)` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `get_resolved_scalar_field_3d()` | method | `GPlatesAppLogic::ResolvedScalarField3D::non_null_ptr_to_const_type` | public | — |
| `d_resolved_scalar_field` | field | `GPlatesAppLogic::ResolvedScalarField3D::non_null_ptr_to_const_type` | private | The resolved scalar field. |
| `d_render_parameters` | field | `ScalarField3DRenderParameters` | private | Parameters that determine how to render the scalar field. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEW_OPERATIONS_RENDEREDRESOLVEDSCALARFIELD3D_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 2 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedResolvedScalarField3D.h
python scripts/gpq.py def GPlatesViewOperations::RenderedResolvedScalarField3D --body
python scripts/gpq.py uses RenderedResolvedScalarField3D --kind class
python scripts/gpq.py hier RenderedResolvedScalarField3D
```

# RenderedGeometryLayerVisitor

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 59 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedGeometryLayerVisitor.h` | C++ | 99 |

## Overview

Defines the visitor interface for traversing a `RenderedGeometryLayer` and its child `RenderedGeometry` objects. Two versions are provided: `ConstRenderedGeometryLayerVisitor` for const-only traversal, and `RenderedGeometryLayerVisitor` for mutable access to the layer itself while visiting its geometries as const. The core method, `visit_rendered_geometry_layer()`, returns a bool that controls whether the visitor will continue to its child geometries — the default implementation visits only active layers.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::ConstRenderedGeometryLayerVisitor`](#gplatesviewoperationsconstrenderedgeometrylayervisitor) | class | [`ConstRenderedGeometryVisitor`](RenderedGeometryVisitor.md) | — | 6 | Interface for visiting a RenderedGeometryLayer object and its RenderedGeometry objects. |
| [`GPlatesViewOperations::RenderedGeometryLayerVisitor`](#gplatesviewoperationsrenderedgeometrylayervisitor) | class | [`ConstRenderedGeometryVisitor`](RenderedGeometryVisitor.md) | — | 2 | Interface for visiting a RenderedGeometryLayer object and its RenderedGeometry objects. |

## Members

### `GPlatesViewOperations::ConstRenderedGeometryLayerVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit_rendered_geometry_layer( const RenderedGeometryLayer &rendered_geometry_layer)` | method | `bool` | public | Visit a rendered geometry layer. |

### `GPlatesViewOperations::RenderedGeometryLayerVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit_rendered_geometry_layer( RenderedGeometryLayer &rendered_geometry_layer)` | method | `bool` | public | Visit a rendered geometry layer. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYLAYERVISITOR_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/DeleteVertexGeometryOperation](DeleteVertexGeometryOperation.md) | view-operations | 1 |
| [view-operations/InsertVertexGeometryOperation](InsertVertexGeometryOperation.md) | view-operations | 1 |
| [view-operations/MoveVertexGeometryOperation](MoveVertexGeometryOperation.md) | view-operations | 1 |
| [view-operations/RenderedGeometryCollectionVisitor](RenderedGeometryCollectionVisitor.md) | view-operations | 1 |
| [view-operations/RenderedGeometryLayer](RenderedGeometryLayer.md) | view-operations | 1 |
| [view-operations/SplitFeatureGeometryOperation](SplitFeatureGeometryOperation.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedGeometryLayerVisitor.h
python scripts/gpq.py def GPlatesViewOperations::ConstRenderedGeometryLayerVisitor --body
python scripts/gpq.py uses ConstRenderedGeometryLayerVisitor --kind class
python scripts/gpq.py hier ConstRenderedGeometryLayerVisitor
```

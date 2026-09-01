# RenderedGeometryCollectionVisitor

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1402 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedGeometryCollectionVisitor.h` | C++ | 150 |

## Overview

Visitor pattern interfaces for traversing a `RenderedGeometryCollection` and its nested layers and geometries. Both const and non-const versions are provided. The visitors control which main layers are visited (filtering to active layers by default) and allow customization of child-layer traversal order through subclass specialization. Subclasses also inherit from `RenderedGeometryLayerVisitor` to visit individual layer and geometry contents.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::ConstRenderedGeometryCollectionVisitor`](#gplatesviewoperationsconstrenderedgeometrycollectionvisitor) | class | [`ConstRenderedGeometryLayerVisitor`](RenderedGeometryLayerVisitor.md) | `<class ForwardReadableRange = RenderedGeometryCollection::child_layer_index_seq_type>` | 5 | Interface for visiting a RenderedGeometryCollection object and its RenderedGeometryLayer objects and its RenderedGeometry objects in turn. |
| [`GPlatesViewOperations::RenderedGeometryCollectionVisitor`](#gplatesviewoperationsrenderedgeometrycollectionvisitor) | class | [`RenderedGeometryLayerVisitor`](RenderedGeometryLayerVisitor.md) | `<class ForwardReadableRange = RenderedGeometryCollection::child_layer_index_seq_type>` | 1 | Interface for visiting a RenderedGeometryCollection object and its RenderedGeometryLayer objects and its RenderedGeometry objects in turn. |

## Members

### `GPlatesViewOperations::ConstRenderedGeometryCollectionVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit_main_rendered_layer( const RenderedGeometryCollection &rendered_geometry_collection, RenderedGeometryCollection::MainLayerType main_rendered_layer_type)` | method | `bool` | public | Visit a main rendered layer. |
| `get_custom_child_layers_order( RenderedGeometryCollection::MainLayerType parent_layer)` | method | `boost::optional<ForwardReadableRange>` | public | Returns a sequence of child layer indices used for custom order of visitation of child layers for the given main layer. |

### `GPlatesViewOperations::RenderedGeometryCollectionVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit_main_rendered_layer( RenderedGeometryCollection &rendered_geometry_collection, RenderedGeometryCollection::MainLayerType main_rendered_layer_type)` | method | `bool` | public | Visit a main rendered layer. |
| `get_custom_child_layers_order( RenderedGeometryCollection::MainLayerType parent_layer)` | method | `boost::optional<ForwardReadableRange>` | public | Returns a sequence of child layer indices used for custom order of visitation of child layers for the given main layer. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYCOLLECTIONVISITOR_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryCollectionPainter](../gui/GlobeRenderedGeometryCollectionPainter.md) | gui | 1 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 1 |
| [gui/MapRenderedGeometryCollectionPainter](../gui/MapRenderedGeometryCollectionPainter.md) | gui | 1 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 1 |
| [view-operations/RenderedGeometryCollection](RenderedGeometryCollection.md) | view-operations | 1 |
| [view-operations/RenderedGeometryUtils](RenderedGeometryUtils.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedGeometryCollectionVisitor.h
python scripts/gpq.py def GPlatesViewOperations::ConstRenderedGeometryCollectionVisitor --body
python scripts/gpq.py uses ConstRenderedGeometryCollectionVisitor --kind class
python scripts/gpq.py hier ConstRenderedGeometryCollectionVisitor
```

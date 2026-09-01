# GeometryOperation

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 239 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/GeometryOperation.h` | C++ | 133 |
| `src/view-operations/GeometryOperation.cc` | C++ | 76 |

## Overview

`GeometryOperation` is the abstract base every canvas-tool geometry-editing operation implements (five subclasses, including `InsertVertexGeometryOperation` and `MoveVertexGeometryOperation`), fixing the `activate()`/`deactivate()` lifecycle a canvas tool drives as it is selected and deselected. Beyond that lifecycle it standardises how an operation reports which point of a `GeometryBuilder` geometry the mouse is currently over: subclasses call the protected `emit_highlight_point_signal`/`emit_unhighlight_signal` helpers rather than emitting `highlight_point_in_geometry`/`unhighlight_point_in_geometry` directly, so every subclass gets the same de-duplication for free — a repeated highlight of the same point is a no-op, and highlighting a new point automatically unhighlights the previous one first.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::GeometryOperation`](#gplatesviewoperationsgeometryoperation) | class | `QObject` | — | 5 | Interface for activating/deactivating a geometry operation. |

## Members

### `GPlatesViewOperations::GeometryOperation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~GeometryOperation()` | destructor | `None` | public | — |
| `activate()` | method | `void` | public | Activate this operation. |
| `deactivate()` | method | `void` | public | Deactivate this operation. |
| `highlight_point_in_geometry( GPlatesViewOperations::GeometryBuilder *geometry_builder, GPlatesViewOperations::GeometryBuilder::GeometryIndex geometry_index, GPlatesViewOperations::GeometryBuilder::PointIndex point_index, const GPlatesGui::Colour &highlight_colour)` | method | `void` | public | The point at index point\_index was in the geometry at index geometry\_index in the geometry builder geometry\_builder was highlighted by this geometry operation. |
| `unhighlight_point_in_geometry( GPlatesViewOperations::GeometryBuilder *geometry_builder, GPlatesViewOperations::GeometryBuilder::GeometryIndex geometry_index, GPlatesViewOperations::GeometryBuilder::PointIndex point_index)` | method | `void` | public | The point at index point\_index was in the geometry at index geometry\_index in the geometry builder geometry\_builder was unhighlighted by this geometry operation. |
| `GeometryOperation()` | constructor | `None` | protected | Constructor. |
| `emit_highlight_point_signal( GPlatesViewOperations::GeometryBuilder *geometry_builder, GPlatesViewOperations::GeometryBuilder::GeometryIndex geometry_index, GPlatesViewOperations::GeometryBuilder::PointIndex point_index, const GPlatesGui::Colour &highlight_colour)` | method | `void` | protected | If point is not currently highlighted then emit a highlight signal to listeners. |
| `emit_unhighlight_signal( GPlatesViewOperations::GeometryBuilder *geometry_builder)` | method | `void` | protected | If point is currently highlighted then emit a unhighlight signal to listeners. |
| `d_point_is_highlighted` | field | `bool` | private | Is a point currently highlighted in this GeometryOperation. |
| `d_highlight_geometry_index` | field | `GPlatesViewOperations::GeometryBuilder::GeometryIndex` | private | Parameters used in last highlight point signal. |
| `d_highlight_point_index` | field | `GPlatesViewOperations::GeometryBuilder::PointIndex` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_GEOMETRYOPERATION_H` | macro | `None` | — |

## Notes

Subclasses declaring the `highlight_point_in_geometry`/`unhighlight_point_in_geometry` slots must use fully namespace-qualified argument types, per the header's own note — Qt's signal/slot matching is a literal string comparison, so an unqualified type in a slot signature silently fails to connect at runtime.

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/DeleteVertexGeometryOperation](DeleteVertexGeometryOperation.md) | view-operations | 6 |
| [view-operations/MoveVertexGeometryOperation](MoveVertexGeometryOperation.md) | view-operations | 5 |
| [canvas-tools/InsertVertex](../canvas-tools/InsertVertex.md) | canvas-tools | 2 |
| [canvas-tools/MoveVertex](../canvas-tools/MoveVertex.md) | canvas-tools | 2 |
| [canvas-tools/SplitFeature](../canvas-tools/SplitFeature.md) | canvas-tools | 2 |
| [view-operations/AddPointGeometryOperation](AddPointGeometryOperation.md) | view-operations | 2 |
| [view-operations/GeometryOperationUndo](GeometryOperationUndo.md) | view-operations | 2 |
| [view-operations/InsertVertexGeometryOperation](InsertVertexGeometryOperation.md) | view-operations | 2 |
| [view-operations/SplitFeatureGeometryOperation](SplitFeatureGeometryOperation.md) | view-operations | 2 |
| [qt-widgets/LatLonCoordinatesTable](../qt-widgets/LatLonCoordinatesTable.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/GeometryOperation.h
python scripts/gpq.py def GPlatesViewOperations::GeometryOperation --body
python scripts/gpq.py uses GeometryOperation --kind class
python scripts/gpq.py hier GeometryOperation
```

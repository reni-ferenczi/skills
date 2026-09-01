# RenderedGeometry

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1554 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedGeometry.h` | C++ | 103 |
| `src/view-operations/RenderedGeometry.cc` | C++ | 74 |

## Overview

The value type passed around the rendering path: a thin, copyable pimpl wrapper around a reference-counted `RenderedGeometryImpl` (via `boost::intrusive_ptr`). `RenderedGeometryFactory` builds them, `RenderedGeometryLayer` and `RenderedGeometryCollection` store and hand them out, and painters and canvas tools consume them — hence the very wide fan-in across `view-operations`, `presentation`, `gui` and `canvas-tools`.

A default-constructed `RenderedGeometry` has no implementation at all: `accept_visitor()` and both proximity tests silently do nothing (or return a null hit) rather than dereferencing a null pointer, so callers do not need to special-case "empty" instances before using them.

The implementation is reachable only through `accept_visitor()`, and every `ConstRenderedGeometryVisitor` method takes its argument by const reference. That makes a constructed `RenderedGeometry` effectively immutable from the outside — the class exists specifically to hide which concrete `RenderedGeometryImpl` subclass (point, polyline, coloured mesh, symbol, …) it holds behind one non-polymorphic type.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedGeometry`](#gplatesviewoperationsrenderedgeometry) | class | — | — | 0 | This class describes a geometry which has been rendered for display. |

## Members

### `GPlatesViewOperations::RenderedGeometry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `impl_ptr_type` | typedef | `boost::intrusive_ptr<RenderedGeometryImpl>` | public | Typedef for pointer to a RenderedGeometry implementation. |
| `RenderedGeometry()` | constructor | `None` | public | Creates a RenderedGeometry object that has no implementation. |
| `RenderedGeometry( impl_ptr_type)` | constructor | `None` | public | Creates a RenderedGeometry with specified implementation. |
| `accept_visitor( ConstRenderedGeometryVisitor&)` | method | `void` | public | Visit the rendered geometry implementation type. |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `test_vertex_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `d_impl` | field | `impl_ptr_type` | private | Pimpl idiom: pointer to implementation interface. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_RENDEREDGEOMETRY_H` | macro | `None` | — |

## Notes

Ownership of the underlying `RenderedGeometryImpl` is shared via intrusive reference counting, so copying a `RenderedGeometry` is cheap and safe; the implementation is freed once the last copy goes away. The "effective immutability" only holds from outside the class — a caller that stashes its own pointer to the implementation (obtained, say, inside a visitor override) can still mutate it, which the header calls out as a subversion of the intended design rather than a supported use.

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 151 |
| [view-operations/RenderedGeometryLayer](RenderedGeometryLayer.md) | view-operations | 50 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 45 |
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 14 |
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 12 |
| [view-operations/MoveVertexGeometryOperation](MoveVertexGeometryOperation.md) | view-operations | 12 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 11 |
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 7 |
| [app-logic/deprecated/PaleomagUtils](../app-logic/deprecated/PaleomagUtils.md) | app-logic | 6 |
| [view-operations/RenderedMultiReconstructionGeometry](RenderedMultiReconstructionGeometry.md) | view-operations | 6 |
| [view-operations/RenderedReconstructionGeometry](RenderedReconstructionGeometry.md) | view-operations | 6 |
| [view-operations/SplitFeatureGeometryOperation](SplitFeatureGeometryOperation.md) | view-operations | 6 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 5 |
| [view-operations/AddPointGeometryOperation](AddPointGeometryOperation.md) | view-operations | 5 |
| [view-operations/DeleteVertexGeometryOperation](DeleteVertexGeometryOperation.md) | view-operations | 4 |
| [view-operations/InsertVertexGeometryOperation](InsertVertexGeometryOperation.md) | view-operations | 4 |
| [canvas-tools/MeasureDistance](../canvas-tools/MeasureDistance.md) | canvas-tools | 3 |
| [canvas-tools/SelectHellingerGeometries](../canvas-tools/SelectHellingerGeometries.md) | canvas-tools | 3 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 3 |
| [view-operations/RenderedGeometryUtils](RenderedGeometryUtils.md) | view-operations | 3 |

*... and 9 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedGeometry.h
python scripts/gpq.py def GPlatesViewOperations::RenderedGeometry --body
python scripts/gpq.py uses RenderedGeometry --kind class
python scripts/gpq.py hier RenderedGeometry
```

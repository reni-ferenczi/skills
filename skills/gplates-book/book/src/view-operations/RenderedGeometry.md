# RenderedGeometry

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1554 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedGeometry.h` | C++ | 103 |
| `src/view-operations/RenderedGeometry.cc` | C++ | 74 |

## Overview

[[[PROSE overview unit=view-operations/RenderedGeometry tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=view-operations/RenderedGeometry tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

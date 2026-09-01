# RenderedColouredEdgeSurfaceMesh

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 832 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedColouredEdgeSurfaceMesh.h` | C++ | 230 |

## Overview

[[[PROSE overview unit=view-operations/RenderedColouredEdgeSurfaceMesh tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedColouredEdgeSurfaceMesh`](#gplatesviewoperationsrenderedcolourededgesurfacemesh) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | A non-filled edge mesh on the surface of the globe where each edge or each vertex has its own colour. |

## Members

### `GPlatesViewOperations::RenderedColouredEdgeSurfaceMesh`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Edge` | struct | `None` | public | A mesh edge. |
| `edge_seq_type` | typedef | `std::vector<Edge>` | public | — |
| `vertex_seq_type` | typedef | `std::vector<GPlatesMaths::PointOnSphere>` | public | — |
| `colour_seq_type` | typedef | `std::vector<GPlatesGui::ColourProxy>` | public | TODO: Change this to Colour once the deferred (until painting) colouring has been removed. |
| `RenderedColouredEdgeSurfaceMesh( EdgeForwardIter edges_begin, EdgeForwardIter edges_end, PointOnSphereForwardIter vertices_begin, PointOnSphereForwardIter vertices_end, ColourForwardIter colours_begin, ColourForwardIter colours_end, bool use_vertex_colours, float line_width_hint)` | constructor | `None` | public | Construct from a sequence of edges and a sequence of vertices (PointOnSphere). |
| `get_use_vertex_colours()` | method | `bool` | public | Whether the colours are per-vertex (true) or per-edge (false). |
| `get_line_width_hint()` | method | `float` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `test_vertex_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `d_mesh_edges` | field | `edge_seq_type` | private | — |
| `d_mesh_vertices` | field | `vertex_seq_type` | private | — |
| `d_mesh_colours` | field | `colour_seq_type` | private | These colours are either per-vertex or per-edge depending on d\_use\_vertex\_colours. |
| `d_use_vertex_colours` | field | `bool` | private | — |
| `d_line_width_hint` | field | `float` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDCOLOUREDEDGESURFACEMESH_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=view-operations/RenderedColouredEdgeSurfaceMesh tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 29 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 27 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 20 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 19 |
| [qt-widgets/deprecated/CreateTopologyWidget](../qt-widgets/deprecated/CreateTopologyWidget.md) | qt-widgets | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedColouredEdgeSurfaceMesh.h
python scripts/gpq.py def GPlatesViewOperations::RenderedColouredEdgeSurfaceMesh --body
python scripts/gpq.py uses RenderedColouredEdgeSurfaceMesh --kind class
python scripts/gpq.py hier RenderedColouredEdgeSurfaceMesh
```

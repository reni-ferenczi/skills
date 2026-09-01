# RenderedColouredEdgeSurfaceMesh

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 832 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedColouredEdgeSurfaceMesh.h` | C++ | 230 |

## Overview

A wireframe mesh — an explicit list of edges over a shared vertex array — rendered on the globe with colour attached per vertex or per edge rather than as one solid fill. Each `Edge` is a pair of indices into the mesh's own `vertex_seq_type`, so the mesh owns copies of its vertices, edges and colours once constructed from the iterator ranges passed in; nothing is shared back with whatever built them.

Colours are stored as `GPlatesGui::ColourProxy` rather than a resolved `Colour`, deferring the actual colour lookup to paint time, when a colour scheme is available. `get_use_vertex_colours()` says whether `d_mesh_colours` should be indexed per vertex or per edge when painting.

Like the other `RenderedGeometryImpl` subclasses in this unit, it participates in the visitor and proximity-testing protocols (`accept_visitor`, `test_proximity`, `test_vertex_proximity`) rather than exposing any drawing logic itself; painting and hit-testing both happen outside the class.

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

`test_proximity()` returns the first edge whose polyline registers a proximity hit, not the closest edge in the mesh — the source notes this as a known shortcut, so proximity results near overlapping edges can pick an arbitrary one of them rather than the nearest.

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

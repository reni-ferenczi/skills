# RenderedColouredTriangleSurfaceMesh

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 833 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedColouredTriangleSurfaceMesh.h` | C++ | 272 |

## Overview

[[[PROSE overview unit=view-operations/RenderedColouredTriangleSurfaceMesh tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedColouredTriangleSurfaceMesh`](#gplatesviewoperationsrenderedcolouredtrianglesurfacemesh) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | A filled triangle mesh on the surface of the globe where each triangle or each vertex is filled with its own colour. |

## Members

### `GPlatesViewOperations::RenderedColouredTriangleSurfaceMesh`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Triangle` | struct | `None` | public | A mesh triangle. |
| `triangle_seq_type` | typedef | `std::vector<Triangle>` | public | — |
| `vertex_seq_type` | typedef | `std::vector<GPlatesMaths::PointOnSphere>` | public | — |
| `colour_seq_type` | typedef | `std::vector<GPlatesGui::ColourProxy>` | public | TODO: Change this to Colour once the deferred (until painting) colouring has been removed. |
| `RenderedColouredTriangleSurfaceMesh( TriangleForwardIter triangles_begin, TriangleForwardIter triangles_end, PointOnSphereForwardIter vertices_begin, PointOnSphereForwardIter vertices_end, ColourForwardIter colours_begin, ColourForwardIter colours_end, bool use_vertex_colours, const GPlatesGui::Colour &fill_modulate_co ...` | constructor | `None` | public | Construct from a sequence of triangles and a sequence of vertices (PointOnSphere). |
| `get_use_vertex_colours()` | method | `bool` | public | Whether the colours are per-vertex (true) or per-triangle (false). |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `test_vertex_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `d_mesh_triangles` | field | `triangle_seq_type` | private | — |
| `d_mesh_vertices` | field | `vertex_seq_type` | private | — |
| `d_mesh_colours` | field | `colour_seq_type` | private | These colours are either per-vertex or per-triangle depending on d\_use\_vertex\_colours. |
| `d_use_vertex_colours` | field | `bool` | private | — |
| `d_fill_modulate_colour` | field | `GPlatesGui::Colour` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDCOLOUREDTRIANGLESURFACEMESH_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=view-operations/RenderedColouredTriangleSurfaceMesh tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 15 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 11 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 6 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 6 |
| [opengl/GLReconstructedStaticPolygonMeshes](../opengl/GLReconstructedStaticPolygonMeshes.md) | opengl | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedColouredTriangleSurfaceMesh.h
python scripts/gpq.py def GPlatesViewOperations::RenderedColouredTriangleSurfaceMesh --body
python scripts/gpq.py uses RenderedColouredTriangleSurfaceMesh --kind class
python scripts/gpq.py hier RenderedColouredTriangleSurfaceMesh
```

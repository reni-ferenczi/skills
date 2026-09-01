# GLFilledPolygonsMapView

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 327 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLFilledPolygonsMapView.h` | C++ | 334 |
| `src/opengl/GLFilledPolygonsMapView.cc` | C++ | 441 |

## Overview

`GLFilledPolygonsMapView` is the 2D-map counterpart to `GLFilledPolygonsGlobeView`: it fills polygons and polylines using the same stencil-based technique — draw boundary triangles fanned from a centroid and let the stencil test resolve the interior — instead of tessellating a polygon mesh, because tessellation is too slow to redo every frame for dynamic topological polygons. Because the map projection is already flat, there is no cube-quad-tree spatial partition or per-tile level-of-detail here: geometry is given directly as `QPointF` line geometries in projected map space and rendered in a single pass.

Callers accumulate drawables into a `FilledDrawables` instance via `add_filled_polygon` (single ring, or multiple rings for a polygon with holes) or the `begin_filled_triangle_mesh`/`add_filled_triangle_to_mesh`/`end_filled_triangle_mesh` sequence for individually supplied triangles, then hand the whole batch to `render`, which writes it into a shared vertex array and issues one draw call per accumulated drawable.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLFilledPolygonsMapView`](#gplatesopenglglfilledpolygonsmapview) | class | [`GPlatesUtils::ReferenceCount<GLFilledPolygonsMapView>`](../utils/ReferenceCount.md) | — | 0 | Renders (reconstructed) filled polygons (static or dynamic) using stenciling to generate the polygon interior fill mask instead of generating a polygon mesh (triangulation). |

## Members

### `GPlatesOpenGL::GLFilledPolygonsMapView`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `drawable_vertex_element_type` | typedef | `GLuint` | private | Typedef for a vertex element (vertex index) of a drawable. |
| `drawable_vertex_type` | typedef | `GLColourVertex` | private | Typedef for a coloured vertex of a drawable. |
| `FilledDrawable` | struct | `None` | private | Contains information to render a filled drawable. |
| `filled_drawable_type` | typedef | `FilledDrawable` | private | Typedef for a filled drawable. |
| `filled_drawable_seq_type` | typedef | `std::vector<filled_drawable_type>` | private | Typedef for a sequence of filled drawables. |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLFilledPolygonsMapView>` | public | A convenience typedef for a shared pointer to a non-const GLFilledPolygonsMapView. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLFilledPolygonsMapView>` | public | A convenience typedef for a shared pointer to a const GLFilledPolygonsMapView. |
| `FilledDrawables` | class | `None` | public | Used to accumulate filled drawables for rendering. |
| `filled_drawables_type` | typedef | `FilledDrawables` | public | Typedef for a group of filled drawables. |
| `create( GLRenderer &renderer)` | method | `non_null_ptr_type` | public | Creates a GLFilledPolygonsMapView object. |
| `render( GLRenderer &renderer, const filled_drawables_type &filled_drawables)` | method | `void` | public | Renders the specified filled drawables. |
| `d_drawables_vertex_buffer` | field | `GLVertexBuffer::shared_ptr_type` | private | The vertex buffer containing the vertices of all drawables of the current render call. |
| `d_drawables_vertex_element_buffer` | field | `GLVertexElementBuffer::shared_ptr_type` | private | The vertex buffer containing the vertex elements (indices) of all drawables of the current render call. |
| `d_drawables_vertex_array` | field | `GLVertexArray::shared_ptr_type` | private | The vertex array containing all drawables of the current render call. |
| `GLFilledPolygonsMapView( GLRenderer &renderer)` | constructor | `None` | private | Constructor. |
| `create_drawables_vertex_array( GLRenderer &renderer)` | method | `void` | private | — |
| `write_filled_drawables_to_vertex_array( GLRenderer &renderer, const filled_drawables_type &filled_drawables)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLFILLEDPOLYGONSMAPVIEW_H` | macro | `None` | — |

## Notes

- `render` requires a stencil buffer; if the context's `QGLFormat` has none it logs one warning and returns without drawing, so filled polygons silently disappear on such hardware (rare in practice).
- `begin_filled_drawable`/`end_filled_drawable` must bracket each drawable exactly once, and `FilledDrawables::clear()` should be reused across render calls rather than replaced, to avoid repeated vector reallocation.
- Colours are expected pre-multiplied by alpha; `render` sets up blending accordingly.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 23 |
| [opengl/GLVisualLayers](GLVisualLayers.md) | opengl | 7 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLFilledPolygonsMapView.h
python scripts/gpq.py def GPlatesOpenGL::GLFilledPolygonsMapView --body
python scripts/gpq.py uses GLFilledPolygonsMapView --kind class
python scripts/gpq.py hier GLFilledPolygonsMapView
```

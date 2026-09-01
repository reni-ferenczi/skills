# LayerPainter

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 97 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/LayerPainter.h` | C++ | 663 |
| `src/gui/LayerPainter.cc` | C++ | 1580 |

## Overview

[[[PROSE overview unit=gui/LayerPainter tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::LayerPainter`](#gplatesguilayerpainter) | class | `boost::noncopyable` | — | 0 | Interface for streaming and queuing and rendering primitives/drawables for a single layer. |

## Members

### `GPlatesGui::LayerPainter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `vertex_element_type` | typedef | `GLuint` | public | Typedef for a vertex element (index). |
| `vertex_element_seq_type` | typedef | `std::vector<vertex_element_type>` | public | Typedef for a sequence of vertex elements. |
| `coloured_vertex_type` | typedef | `GPlatesOpenGL::GLColourVertex` | public | Typedef for a coloured vertex. |
| `coloured_vertex_seq_type` | typedef | `std::vector<coloured_vertex_type>` | public | Typedef for a sequence of coloured vertices. |
| `stream_primitives_type` | typedef | `GPlatesOpenGL::GLDynamicStreamPrimitives<coloured_vertex_type, vertex_element_type>` | public | Typedef for a primitives stream containing coloured vertices. |
| `AxiallySymmetricMeshVertex` | struct | `None` | public | A vertex of an axially symmetric (about model-space z-axis) triangle mesh. |
| `axially_symmetric_mesh_vertex_seq_type` | typedef | `std::vector<AxiallySymmetricMeshVertex>` | public | Typedef for a sequence of axially symmetric mesh vertices. |
| `axially_symmetric_mesh_stream_primitives_type` | typedef | `GPlatesOpenGL::GLDynamicStreamPrimitives<AxiallySymmetricMeshVertex, vertex_element_type>` | public | Typedef for a primitives stream containing vertices of an axially symmetric mesh. |
| `cache_handle_type` | typedef | `boost::shared_ptr<void>` | public | Typedef for an opaque object that caches a particular painting. |
| `PointLinePolygonDrawables` | class | `None` | public | Drawables for points, lines and polygons (triangles and quads). |
| `TextDrawable2D` | struct | `None` | public | Information to render a text string located at a 2D viewport position. |
| `TextDrawable3D` | struct | `None` | public | Information to render a text string located at a 3D world position. |
| `RasterDrawable` | struct | `None` | public | Information to render a raster. |
| `ScalarField3DDrawable` | struct | `None` | public | Information to render a scalar field. |
| `LayerPainter( const GPlatesOpenGL::GLVisualLayers::non_null_ptr_type &gl_visual_layers, int device_pixel_ratio, boost::optional<MapProjection::non_null_ptr_to_const_type> map_projection = boost::none)` | constructor | `None` | public | Constructor. device\_pixel\_ratio is a multiplier for point sizes and line widths. |
| `initialise( GPlatesOpenGL::GLRenderer &renderer)` | method | `void` | public | Initialise objects requiring GLRenderer. |
| `begin_painting( GPlatesOpenGL::GLRenderer &renderer)` | method | `void` | public | Must be called before streaming or queuing any primitives. |
| `end_painting( GPlatesOpenGL::GLRenderer &renderer, float scale, boost::optional<GPlatesOpenGL::GLTexture::shared_ptr_to_const_type> surface_occlusion_texture = boost::none)` | method | `cache_handle_type` | public | Renders any streamed or queued primitives. of the surface geometries/rasters on the \*front\* of the globe. |
| `drawables_off_the_sphere` | field | `PointLinePolygonDrawables` | public | — |
| `opaque_drawables_on_the_sphere` | field | `PointLinePolygonDrawables` | public | — |
| `translucent_drawables_on_the_sphere` | field | `PointLinePolygonDrawables` | public | — |
| `rasters` | field | `std::vector<RasterDrawable>` | public | — |
| `scalar_fields` | field | `std::vector<ScalarField3DDrawable>` | public | — |
| `text_drawables_3D` | field | `std::vector<TextDrawable3D>` | public | — |
| `text_drawables_2D` | field | `std::vector<TextDrawable2D>` | public | — |
| `paint_scalar_fields( GPlatesOpenGL::GLRenderer &renderer, boost::optional<GPlatesOpenGL::GLTexture::shared_ptr_to_const_type> surface_occlusion_texture)` | method | `cache_handle_type` | private | — |
| `paint_rasters( GPlatesOpenGL::GLRenderer &renderer)` | method | `cache_handle_type` | private | — |
| `paint_text_drawables_2D( GPlatesOpenGL::GLRenderer &renderer, float scale)` | method | `void` | private | — |
| `paint_text_drawables_3D( GPlatesOpenGL::GLRenderer &renderer, float scale)` | method | `void` | private | — |
| `d_renderer` | field | `boost::optional<GPlatesOpenGL::GLRenderer &>` | private | References the renderer (is only valid between begin\_painting and end\_painting). |
| `d_gl_visual_layers` | field | `GPlatesOpenGL::GLVisualLayers::non_null_ptr_type` | private | For obtaining the OpenGL light and rendering rasters and scalar fields. |
| `d_vertex_element_buffer` | field | `GPlatesOpenGL::GLVertexElementBuffer::shared_ptr_type` | private | Used to stream vertex elements (indices) to. |
| `d_vertex_buffer` | field | `GPlatesOpenGL::GLVertexBuffer::shared_ptr_type` | private | Used to stream vertices to. |
| `d_vertex_array` | field | `GPlatesOpenGL::GLVertexArray::shared_ptr_type` | private | Used when vertices of type coloured\_vertex\_type (streamed to d\_vertex\_buffer). |
| `d_unlit_axially_symmetric_mesh_vertex_array` | field | `GPlatesOpenGL::GLVertexArray::shared_ptr_type` | private | Used when vertices of type AxiallySymmetricMeshVertex are rendered \*without\* lighting. |
| `d_lit_axially_symmetric_mesh_vertex_array` | field | `GPlatesOpenGL::GLVertexArray::shared_ptr_type` | private | Used when vertices of type AxiallySymmetricMeshVertex are rendered \*with\* lighting. |
| `d_map_projection` | field | `boost::optional<MapProjection::non_null_ptr_to_const_type>` | private | Used for rendering to a 2D map view (is none for 3D globe view). |
| `d_render_point_line_polygon_lighting_in_globe_view_program_object` | field | `boost::optional<GPlatesOpenGL::GLProgramObject::shared_ptr_type>` | private | Shader program to render points/lines/polygons with lighting in a 3D \*globe\* view. |
| `d_render_point_line_polygon_lighting_in_map_view_program_object` | field | `boost::optional<GPlatesOpenGL::GLProgramObject::shared_ptr_type>` | private | Shader program to render points/lines/polygons with lighting in a 2D \*map\* view. |
| `d_render_axially_symmetric_mesh_lighting_program_object` | field | `boost::optional<GPlatesOpenGL::GLProgramObject::shared_ptr_type>` | private | Shader program for lighting axially symmetric meshes. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `RENDER_POINT_LINE_POLYGON_LIGHTING_VERTEX_SHADER` | variable | `QString` | Vertex shader source code to render points, lines and polygons with lighting. |
| `RENDER_POINT_LINE_POLYGON_LIGHTING_FRAGMENT_SHADER` | variable | `QString` | Fragment shader source code to render points, lines and polygons with lighting. |
| `RENDER_AXIALLY_SYMMETRIC_MESH_LIGHTING_VERTEX_SHADER` | variable | `QString` | Vertex shader source code for lighting axially symmetric meshes. |
| `RENDER_AXIALLY_SYMMETRIC_MESH_LIGHTING_FRAGMENT_SHADER` | variable | `QString` | Fragment shader source code for lighting axially symmetric meshes. |
| `GPLATES_GUI_LAYERPAINTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/LayerPainter tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/MapRenderedGeometryLayerPainter](MapRenderedGeometryLayerPainter.md) | gui | 193 |
| [gui/GlobeRenderedGeometryLayerPainter](GlobeRenderedGeometryLayerPainter.md) | gui | 86 |
| [gui/Map](Map.md) | gui | 22 |
| [gui/MapRenderedGeometryCollectionPainter](MapRenderedGeometryCollectionPainter.md) | gui | 17 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 8 |
| [gui/GlobeRenderedGeometryCollectionPainter](GlobeRenderedGeometryCollectionPainter.md) | gui | 2 |
| [qt-widgets/MapView](../qt-widgets/MapView.md) | qt-widgets | 2 |

## Related

**Shader programs compiled by this unit**

| Shader unit | Component |
|---|---|
| [shaders/layer_painter](../qt-resources/opengl/layer_painter.md) | shaders |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/LayerPainter.h
python scripts/gpq.py def GPlatesGui::LayerPainter --body
python scripts/gpq.py uses LayerPainter --kind class
python scripts/gpq.py hier LayerPainter
```

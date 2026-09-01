# LayerPainter

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 97 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/LayerPainter.h` | C++ | 663 |
| `src/gui/LayerPainter.cc` | C++ | 1580 |

## Overview

`LayerPainter` is the batching layer between GPlates' rendered-geometry model and
OpenGL. One rendered geometry layer is painted at a time by a
`GlobeRenderedGeometryLayerPainter` or `MapRenderedGeometryLayerPainter`; those
visitors do not issue draw calls themselves, they push vertices into the streams
this class hands out and append `RasterDrawable` / `ScalarField3DDrawable` /
`TextDrawable2D` / `TextDrawable3D` records to its public vectors. Nothing is
drawn until `end_painting()`, which then emits everything in one carefully ordered
pass. The point of the indirection is state sorting: geometry arrives in whatever
order the layer visitor walks it, and drawing it in that order would mean
thrashing OpenGL state per primitive.

The sorting is two-dimensional. Along one axis the client chooses a bucket by
depth semantics — `opaque_drawables_on_the_sphere`,
`translucent_drawables_on_the_sphere`, `drawables_off_the_sphere` — and
`end_painting()` gives each bucket a different depth and blend configuration.
Geometry *on* the sphere gets depth test on but depth writes off, so tessellated
polylines and filled-polygon meshes cannot depth-fight each other where the mesh
dips below the true sphere; geometry *off* the sphere (velocity and direction
arrows) gets depth writes on so later layers cannot paint over it, and must
therefore be opaque, since writing depth from anti-aliased edges leaves blending
artefacts. Along the other axis, inside each bucket `PointLinePolygonDrawables`
keys points by point size and lines by line width into `std::map`s, so all points
of one size become a single `GL_POINTS` draw call. Triangles need no such split
and go into one stream, with a second stream for `AxiallySymmetricMeshVertex`
meshes, whose extra per-vertex axis frame and radial/axial normal weights exist so
the fragment shader can light a cone (an arrowhead) correctly at its apex, where
per-vertex normals cannot. Within a bucket the fixed draw order is filled polygons
first, then triangles, lines and points, then axially symmetric meshes; across
buckets it is scalar fields, rasters, on-sphere, off-sphere, 2-D text, 3-D text.

The same class serves both views: passing a `MapProjection` to the constructor
switches it into 2-D map mode, which disables the depth buffer and depth writes,
selects the map-view variants of the filled-polygon renderer and the lighting
shader (compiled from the same GLSL with `#define MAP_VIEW`), and makes
`paint_scalar_fields()` a no-op, since 3-D scalar fields have no map rendering.
Lighting and rasters are delegated to `GPlatesOpenGL::GLVisualLayers`;
`set_generic_point_line_polygon_lighting_state()` and
`set_axially_symmetric_mesh_lighting_state()` return false and fall back to the
fixed-function pipeline whenever the runtime lacks the shaders, lighting is
switched off in `SceneLightingParameters`, or the renderer is not targeting the
real framebuffer. That last case is the SVG/vector-export path: when
`GLRenderer::rendering_to_context_framebuffer()` is false, every draw is rerouted
through `FeedbackOpenGLToQPainter` — vector primitives via OpenGL feedback, and
rasters, scalar fields and filled polygons rendered into a tiled `QImage` and
blitted to the `QPainter`.

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

**Three-phase lifetime, and `initialise()` is separate for a reason.** The
constructor only records parameters; the GL buffers, vertex arrays and shader
programs are created in `initialise()`, which needs a live `GLRenderer` and is
called once when the OpenGL context is ready. `begin_painting()` asserts those
objects exist. The instance is then long-lived — `GlobeRenderedGeometryCollectionPainter`
holds one `LayerPainter` by value and drives a `begin_painting`/`end_painting`
cycle around *every* rendered geometry layer, every frame, reusing the same
buffers throughout.

**Everything is cleared by `end_painting()`, including the queues you filled
directly.** `rasters`, `scalar_fields`, `text_drawables_2D`, `text_drawables_3D`
and the filled-polygon lists are all `clear()`ed after being drawn, and the
per-size point and line maps are erased so the next layer can use different
widths. The vectors are public with no invariant guarding them, so pushing to
them outside a begin/end pair means the entries sit there until the next
`end_painting()` draws them as part of some other layer.

**`get_renderer()` and every stream accessor are only valid inside a begin/end
pair.** `d_renderer` is a `boost::optional<GLRenderer &>` set in
`begin_painting()` and reset to `boost::none` at the end, so calling
`get_renderer()` outside dereferences an empty optional. `Drawables::get_stream()`
and `has_primitives()` assert on the stream object, which likewise exists only
between the paired calls. Note the asymmetry that makes this work: `begin_painting()`
starts streams for triangles only, and the point and line streams are created
lazily by `get_points_stream()` / `get_lines_stream()` the first time a given size
is asked for — but `end_painting()` must still be called on the axially symmetric
drawable even when it has no primitives, which the code does explicitly with a
dummy vertex array.

**References returned by the stream accessors do not survive further calls.** The
per-size drawables live in `std::map`s and the stream is created on first request
for a size, so holding a `stream_primitives_type &` across a request for a
different point size or line width is asking for trouble. Fetch, stream, discard.

**The lighting state functions are silently permissive.** They return false and
*leave the existing GL state alone* rather than reporting an error, in three
distinct situations — no shader support, lighting disabled, or feedback rendering.
So a geometry that looks unlit is not necessarily a bug in the shader; check
`SceneLightingParameters` and whether the render is going to a `QPainter` first.

**The `cache_handle_type` return value is load-bearing.** `end_painting()` returns
an opaque `boost::shared_ptr<void>` holding the internal caches for the rasters and
scalar fields it drew. The caller must keep it alive until the next frame or the
OpenGL structures behind every raster and scalar field are rebuilt from scratch
each frame.

**Axially symmetric meshes have hard geometric preconditions.** The mesh must be
symmetric about its model-space z-axis or the lighting fragment shader produces
wrong results, and front faces must be counter-clockwise because back faces are
culled (the lighting is one-sided). The vertex struct's field order is also fixed:
`world_space_position` and `colour` must stay first, since the unlit path binds
them as non-generic `GL_VERTEX_ARRAY`/`GL_COLOR_ARRAY` pointers at hard-coded
offsets while the lit path binds all seven attributes generically and re-links the
program. Reordering members breaks the unlit path quietly.

**Feedback rendering forces the fixed-function pipeline.** OpenGL feedback here
captures only fixed-function output, so vector export never gets shader lighting —
there is a TODO in the code about implementing OpenGL 2/3 feedback extensions.
This is why exported SVG can look different from the screen.

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

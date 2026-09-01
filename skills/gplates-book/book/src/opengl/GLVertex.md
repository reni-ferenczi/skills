# GLVertex

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 331 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLVertex.h` | C++ | 491 |
| `src/opengl/GLVertex.cc` | C++ | 276 |

## Overview

This unit is the backend's catalogue of interleaved vertex layouts, together with
the mechanism that teaches `GLVertexArray` how to read each of them. The pattern
is one struct plus one full specialisation of the function template
`bind_vertex_buffer_to_vertex_array<VertexType>`: the struct declares the layout
in C++, and the specialisation in `GLVertex.cc` declares the same layout to
OpenGL by calling `GLVertexArray::set_vertex_pointer`, `set_color_pointer` and
`set_tex_coord_pointer` with `sizeof(VertexType)` as the stride and hand-computed
byte offsets for each field. The primary template is declared but intentionally
never defined, so using a vertex type that has no specialisation is a link error
rather than a silently wrong binding.

That indirection is what makes the rest of the backend's vertex plumbing
generic. `GLVertexArray::set_vertex_array_data` and
`compile_vertex_array_draw_state` are templated on `VertexType`: a caller hands
over a `std::vector<VertexType>` and a vector of indices, and the buffers, the
attribute bindings and the compiled `GLCompiledDrawState` all follow from the one
type argument. Consequently almost nothing in the backend writes attribute
bindings by hand — it typedefs one of these structs instead, as
`GPlatesGui::LayerPainter`, `GPlatesGui::Stars`, `GLFilledPolygonsGlobeView`,
`GLFilledPolygonsMapView` and `GLMultiResolutionRaster` all do.

The bindings use the fixed-function client-state arrays (`GL_VERTEX_ARRAY`,
`GL_COLOR_ARRAY`, and per-texture-unit coordinate arrays), not generic vertex
attribute slots, which is why the shader-based paths see this data as
`gl_Vertex`, `gl_Color` and `gl_TexCoord[n]`. `GLTextureTangentSpaceVertex` is
the clearest consequence of that choice: having no generic attributes available,
it ships a per-vertex tangent frame as three 3-component texture coordinate sets
on units 1, 2 and 3, which `render_raster_fragment_shader.glsl` reads back as
`gl_TexCoord[1..3]` to rotate a normal-map sample out of tangent space.
`GLMultiResolutionRaster` uses it for both its normal-map and its scalar-field
depth-layer meshes.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLVertex`](#gplatesopenglglvertex) | struct | — | — | 0 | A vertex with 3D position. |
| [`GPlatesOpenGL::GLColourVertex`](#gplatesopenglglcolourvertex) | struct | — | — | 0 | A vertex with 3D position and a colour. |
| [`GPlatesOpenGL::GLTextureVertex`](#gplatesopenglgltexturevertex) | struct | — | — | 0 | A vertex with 3D position and 2D texture coordinates. |
| [`GPlatesOpenGL::GLTexture3DVertex`](#gplatesopenglgltexture3dvertex) | struct | — | — | 0 | A vertex with 3D position and \*3D\* texture coordinates. |
| [`GPlatesOpenGL::GLColourTextureVertex`](#gplatesopenglglcolourtexturevertex) | struct | — | — | 0 | A vertex with 3D position, a colour and 2D texture coordinates. |
| [`GPlatesOpenGL::GLTextureTangentSpaceVertex`](#gplatesopenglgltexturetangentspacevertex) | struct | — | — | 0 | A vertex with 3D position, 2D texture coordinates and a tangent-space frame consisting of three 3D texture coordinates representing the three frame axes. |

## Members

### `GPlatesOpenGL::GLVertex`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLVertex()` | constructor | `None` | public | NOTE: Default constructor does \*not\* initialise ! |
| `GLVertex( GLfloat x_, GLfloat y_, GLfloat z_)` | constructor | `None` | public | — |
| `GLVertex( const GPlatesMaths::UnitVector3D &vertex_)` | constructor | `None` | public | — |
| `GLVertex( const GPlatesMaths::Vector3D &vertex_)` | constructor | `None` | public | — |
| `x` | field | `GLfloat` | public | — |
| `y` | field | `GLfloat` | public | — |
| `z` | field | `GLfloat` | public | — |

### `GPlatesOpenGL::GLColourVertex`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLColourVertex()` | constructor | `None` | public | NOTE: Default constructor does \*not\* initialise ! |
| `GLColourVertex( GLfloat x_, GLfloat y_, GLfloat z_, GPlatesGui::rgba8_t colour_)` | constructor | `None` | public | — |
| `GLColourVertex( const GPlatesMaths::UnitVector3D &vertex_, GPlatesGui::rgba8_t colour_)` | constructor | `None` | public | — |
| `GLColourVertex( const GPlatesMaths::Vector3D &vertex_, GPlatesGui::rgba8_t colour_)` | constructor | `None` | public | — |
| `x` | field | `GLfloat` | public | — |
| `y` | field | `GLfloat` | public | — |
| `z` | field | `GLfloat` | public | — |
| `colour` | field | `GPlatesGui::rgba8_t` | public | — |

### `GPlatesOpenGL::GLTextureVertex`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLTextureVertex()` | constructor | `None` | public | NOTE: Default constructor does \*not\* initialise ! |
| `GLTextureVertex( GLfloat x_, GLfloat y_, GLfloat z_, GLfloat u_, GLfloat v_)` | constructor | `None` | public | — |
| `GLTextureVertex( const GPlatesMaths::UnitVector3D &vertex_, GLfloat u_, GLfloat v_)` | constructor | `None` | public | — |
| `GLTextureVertex( const GPlatesMaths::Vector3D &vertex_, GLfloat u_, GLfloat v_)` | constructor | `None` | public | — |
| `x` | field | `GLfloat` | public | — |
| `y` | field | `GLfloat` | public | — |
| `z` | field | `GLfloat` | public | — |
| `u` | field | `GLfloat` | public | — |
| `v` | field | `GLfloat` | public | — |

### `GPlatesOpenGL::GLTexture3DVertex`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLTexture3DVertex()` | constructor | `None` | public | NOTE: Default constructor does \*not\* initialise ! |
| `GLTexture3DVertex( GLfloat x_, GLfloat y_, GLfloat z_, GLfloat s_, GLfloat t_, GLfloat r_)` | constructor | `None` | public | — |
| `GLTexture3DVertex( const GPlatesMaths::UnitVector3D &vertex_, GLfloat s_, GLfloat t_, GLfloat r_)` | constructor | `None` | public | — |
| `GLTexture3DVertex( const GPlatesMaths::Vector3D &vertex_, GLfloat s_, GLfloat t_, GLfloat r_)` | constructor | `None` | public | — |
| `x` | field | `GLfloat` | public | — |
| `y` | field | `GLfloat` | public | — |
| `z` | field | `GLfloat` | public | — |
| `s` | field | `GLfloat` | public | — |
| `t` | field | `GLfloat` | public | — |
| `r` | field | `GLfloat` | public | — |

### `GPlatesOpenGL::GLColourTextureVertex`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLColourTextureVertex()` | constructor | `None` | public | NOTE: Default constructor does \*not\* initialise ! |
| `GLColourTextureVertex( GLfloat x_, GLfloat y_, GLfloat z_, GLfloat u_, GLfloat v_, GPlatesGui::rgba8_t colour_)` | constructor | `None` | public | — |
| `GLColourTextureVertex( const GPlatesMaths::UnitVector3D &vertex_, GLfloat u_, GLfloat v_, GPlatesGui::rgba8_t colour_)` | constructor | `None` | public | — |
| `GLColourTextureVertex( const GPlatesMaths::Vector3D &vertex_, GLfloat u_, GLfloat v_, GPlatesGui::rgba8_t colour_)` | constructor | `None` | public | — |
| `x` | field | `GLfloat` | public | — |
| `y` | field | `GLfloat` | public | — |
| `z` | field | `GLfloat` | public | — |
| `u` | field | `GLfloat` | public | — |
| `v` | field | `GLfloat` | public | — |
| `colour` | field | `GPlatesGui::rgba8_t` | public | — |

### `GPlatesOpenGL::GLTextureTangentSpaceVertex`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLTextureTangentSpaceVertex()` | constructor | `None` | public | NOTE: Default constructor does \*not\* initialise ! |
| `GLTextureTangentSpaceVertex( GLfloat x_, GLfloat y_, GLfloat z_, GLfloat u_, GLfloat v_, GLfloat tangent_x_, GLfloat tangent_y_, GLfloat tangent_z_, GLfloat binormal_x_, GLfloat binormal_y_, GLfloat binormal_z_, GLfloat normal_x_, GLfloat normal_y_, GLfloat normal_z_)` | constructor | `None` | public | — |
| `GLTextureTangentSpaceVertex( const GPlatesMaths::UnitVector3D &vertex_, GLfloat u_, GLfloat v_, const GPlatesMaths::UnitVector3D &tangent_, const GPlatesMaths::UnitVector3D &binormal_, const GPlatesMaths::UnitVector3D &normal_)` | constructor | `None` | public | — |
| `GLTextureTangentSpaceVertex( const GPlatesMaths::UnitVector3D &vertex_, GLfloat u_, GLfloat v_, const GPlatesMaths::Vector3D &tangent_, const GPlatesMaths::Vector3D &binormal_, const GPlatesMaths::Vector3D &normal_)` | constructor | `None` | public | — |
| `x` | field | `GLfloat` | public | — |
| `y` | field | `GLfloat` | public | — |
| `z` | field | `GLfloat` | public | — |
| `u` | field | `GLfloat` | public | — |
| `v` | field | `GLfloat` | public | — |
| `tangent_x` | field | `GLfloat` | public | — |
| `tangent_y` | field | `GLfloat` | public | — |
| `tangent_z` | field | `GLfloat` | public | — |
| `binormal_x` | field | `GLfloat` | public | — |
| `binormal_y` | field | `GLfloat` | public | — |
| `binormal_z` | field | `GLfloat` | public | — |
| `normal_x` | field | `GLfloat` | public | — |
| `normal_y` | field | `GLfloat` | public | — |
| `normal_z` | field | `GLfloat` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `bind_vertex_buffer_to_vertex_array( GLRenderer &renderer, GLVertexArray &vertex_array, const GLVertexBuffer::shared_ptr_to_const_type &vertex_buffer, GLint offset)` | function | `void` | — |
| `GPLATES_OPENGL_VERTEX_H` | macro | `None` | — |
| `bind_vertex_buffer_to_vertex_array( GLRenderer &renderer, GLVertexArray &vertex_array, const GLVertexBuffer::shared_ptr_to_const_type &vertex_buffer, GLint offset = 0)` | function | `void` | Specifies the source of vertex attribute data (vertices) as a vertex buffer and binds the attribute data contained within to the vertex array (the internal GLVertexArray). |

## Notes

- The layout is duplicated in two places that nothing checks against each other:
  the field order in the header, and the literal `offset + N * sizeof(GLfloat)`
  arithmetic in the specialisation in `GLVertex.cc`. Adding, removing or
  reordering a field means updating every offset after it by hand. Get it wrong
  and you get garbled geometry at runtime, not a compile error.
- Those offsets assume the compiler inserts no padding, and in particular that
  `GPlatesGui::rgba8_t` is exactly four bytes — the colour is bound as four
  `GL_UNSIGNED_BYTE` components immediately after the floats. `rgba8_t` carries a
  comment warning against multiple inheritance for exactly this reason; keep it
  a four-byte union.
- None of these structs initialise anything in their default constructor, by
  design, because they are bulk-filled into `std::vector` and uploaded. A
  default-constructed vertex that is never assigned uploads garbage. `rgba8_t`'s
  default constructor behaves the same way.
- The `UnitVector3D` and `Vector3D` constructors call `.dval()` and store the
  result in `GLfloat`, so the `maths` module's double-precision positions are
  truncated to single precision here. This is the boundary at which that
  happens; do not expect exact geometry to survive a round trip through a vertex
  buffer.
- `bind_vertex_buffer_to_vertex_array` records into the vertex array through
  `GLRenderer`, so it needs an active renderer, and the `offset` argument must
  satisfy the alignment requirements of the vertex type. Multiple buffers can be
  bound to one vertex array when attributes are split across streams, in which
  case each `VertexType` describes only that stream's subset. The vertex buffer's
  contents may be filled before or after the binding call.
- To add a vertex type you need both halves: a `template <>` declaration next to
  the struct in the header and the matching definition in the `.cc`. Only
  declaring the struct compiles fine and fails at link time.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 58 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 36 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 20 |
| [opengl/GLFilledPolygonsMapView](GLFilledPolygonsMapView.md) | opengl | 14 |
| [opengl/GLUtils](GLUtils.md) | opengl | 13 |
| [gui/SphericalGrid](../gui/SphericalGrid.md) | gui | 10 |
| [opengl/GLMultiResolutionMapCubeMesh](GLMultiResolutionMapCubeMesh.md) | opengl | 10 |
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 10 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 9 |
| [gui/OpaqueSphere](../gui/OpaqueSphere.md) | gui | 8 |
| [opengl/GLMultiResolutionCubeMesh](GLMultiResolutionCubeMesh.md) | opengl | 8 |
| [opengl/GLReconstructedStaticPolygonMeshes](GLReconstructedStaticPolygonMeshes.md) | opengl | 8 |
| [opengl/GLVertexArray](GLVertexArray.md) | opengl | 7 |
| [gui/MapBackground](../gui/MapBackground.md) | gui | 6 |
| [gui/Stars](../gui/Stars.md) | gui | 6 |
| [gui/MapGrid](../gui/MapGrid.md) | gui | 5 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 4 |
| [opengl/GLStreamPrimitives](GLStreamPrimitives.md) | opengl | 4 |
| [opengl/GLSaveRestoreFrameBuffer](GLSaveRestoreFrameBuffer.md) | opengl | 3 |
| [opengl/GLScalarField3DGenerator](GLScalarField3DGenerator.md) | opengl | 3 |

*... and 11 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLVertex.h
python scripts/gpq.py def GPlatesOpenGL::GLTextureTangentSpaceVertex --body
python scripts/gpq.py uses GLTextureTangentSpaceVertex --kind struct
python scripts/gpq.py hier GLTextureTangentSpaceVertex
```

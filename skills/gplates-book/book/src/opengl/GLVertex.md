# GLVertex

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 331 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLVertex.h` | C++ | 491 |
| `src/opengl/GLVertex.cc` | C++ | 276 |

## Overview

[[[PROSE overview unit=opengl/GLVertex tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=opengl/GLVertex tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

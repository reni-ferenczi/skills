# GLTexture

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 491 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLTexture.h` | C++ | 586 |
| `src/opengl/GLTexture.cc` | C++ | 449 |

## Overview

[[[PROSE overview unit=opengl/GLTexture tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLTexture`](#gplatesopenglgltexture) | class | [`GLObject`](GLObject.md)<br>`boost::enable_shared_from_this<GLTexture>` | — | 0 | A texture object. |

## Members

### `GPlatesOpenGL::GLTexture`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLTexture>` | public | A convenience typedef for a shared pointer to a GLTexture. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLTexture>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<GLTexture>` | public | A convenience typedef for a weak pointer to a GLTexture. |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const GLTexture>` | public | — |
| `resource_handle_type` | typedef | `GLuint` | public | Typedef for a resource handle. |
| `Allocator` | class | `None` | public | Policy class to allocate and deallocate OpenGL texture objects. |
| `resource_type` | typedef | `GLObjectResource<resource_handle_type, Allocator>` | public | Typedef for a resource. |
| `resource_manager_type` | typedef | `GLObjectResourceManager<resource_handle_type, Allocator>` | public | Typedef for a resource manager. |
| `create( GLRenderer &renderer)` | method | `shared_ptr_type` | public | Creates a shared pointer to a GLTexture object. |
| `create_as_unique_ptr( GLRenderer &renderer)` | method | `std::unique_ptr<GLTexture>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `gl_tex_parameteri( GLRenderer &renderer, GLenum target, GLenum pname, GLint param)` | method | `void` | public | Performs same function as the glTexParameteri OpenGL function. |
| `gl_tex_parameterf( GLRenderer &renderer, GLenum target, GLenum pname, GLfloat param)` | method | `void` | public | Performs same function as the glTexParameterf OpenGL function. |
| `gl_tex_image_1D( GLRenderer &renderer, GLenum target, GLint level, GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum type, const GLvoid *pixels)` | method | `void` | public | Performs same function as the glTexImage1D OpenGL function. |
| `gl_tex_image_1D( GLRenderer &renderer, GLenum target, GLint level, GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum type, const GLPixelBuffer::shared_ptr_to_const_type &pixels, GLint offset = 0)` | method | `void` | public | Performs same function as the glTexImage1D OpenGL function. |
| `gl_tex_image_2D( GLRenderer &renderer, GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const GLvoid *pixels)` | method | `void` | public | Performs same function as the glTexImage2D OpenGL function. |
| `gl_tex_image_2D( GLRenderer &renderer, GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const GLPixelBuffer::shared_ptr_to_const_type &pixels, GLint offset = 0)` | method | `void` | public | Performs same function as the glTexImage2D OpenGL function. |
| `gl_tex_image_3D( GLRenderer &renderer, GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, const GLvoid *pixels)` | method | `void` | public | Performs same function as the glTexImage3D OpenGL function. |
| `gl_tex_image_3D( GLRenderer &renderer, GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, const GLPixelBuffer::shared_ptr_to_const_type &pixels, GLint offset = 0)` | method | `void` | public | Performs same function as the glTexImage3D OpenGL function. |
| `gl_copy_tex_image_1D( GLRenderer &renderer, GLenum target, GLint level, GLint internalformat, GLint x, GLint y, GLsizei width, GLint border)` | method | `void` | public | Performs same function as the glCopyTexImage1D OpenGL function. |
| `gl_copy_tex_image_2D( GLRenderer &renderer, GLenum target, GLint level, GLint internalformat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border)` | method | `void` | public | Performs same function as the glCopyTexImage2D OpenGL function. |
| `gl_tex_sub_image_1D( GLRenderer &renderer, GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const GLvoid *pixels)` | method | `void` | public | Performs same function as the glTexSubImage1D OpenGL function. |
| `gl_tex_sub_image_1D( GLRenderer &renderer, GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const GLPixelBuffer::shared_ptr_to_const_type &pixels, GLint offset = 0)` | method | `void` | public | Performs same function as the glTexSubImage1D OpenGL function. |
| `gl_tex_sub_image_2D( GLRenderer &renderer, GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const GLvoid *pixels)` | method | `void` | public | Performs same function as the glTexSubImage2D OpenGL function. |
| `gl_tex_sub_image_2D( GLRenderer &renderer, GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const GLPixelBuffer::shared_ptr_to_const_type &pixels, GLint offset = 0)` | method | `void` | public | Performs same function as the glTexSubImage2D OpenGL function. |
| `gl_tex_sub_image_3D( GLRenderer &renderer, GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid *pixels)` | method | `void` | public | Performs same function as the glTexSubImage3D OpenGL function. |
| `gl_tex_sub_image_3D( GLRenderer &renderer, GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLPixelBuffer::shared_ptr_to_const_type &pixels, GLint offset = 0)` | method | `void` | public | Performs same function as the glTexSubImage3D OpenGL function. |
| `get_width()` | method | `boost::optional<GLuint>` | public | Returns the width of the texture (level 0). |
| `get_height()` | method | `boost::optional<GLuint>` | public | Returns the height of the texture (level 0). |
| `get_depth()` | method | `boost::optional<GLuint>` | public | Returns the depth of the texture (level 0). |
| `get_internal_format()` | method | `boost::optional<GLint>` | public | Returns the internal format of the texture. |
| `is_floating_point()` | method | `bool` | public | Returns true if 'this' texture is a floating-point texture. |
| `is_format_floating_point( GLint internalformat)` | method | `bool` | public | Returns true if the specified internal texture format is a floating-point format. |
| `get_texture_resource_handle()` | method | `resource_handle_type` | public | Returns the texture resource handle. |
| `d_resource` | field | `resource_type::non_null_ptr_to_const_type` | private | — |
| `d_width` | field | `boost::optional<GLuint>` | private | — |
| `d_height` | field | `boost::optional<GLuint>` | private | — |
| `d_depth` | field | `boost::optional<GLuint>` | private | — |
| `d_internal_format` | field | `boost::optional<GLint>` | private | — |
| `GLTexture( GLRenderer &renderer)` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLTEXTURE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLTexture tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 35 |
| [opengl/GLMultiResolutionCubeRaster](GLMultiResolutionCubeRaster.md) | opengl | 16 |
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 15 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](GLMultiResolutionCubeReconstructedRaster.md) | opengl | 13 |
| [opengl/GLTextureUtils](GLTextureUtils.md) | opengl | 13 |
| [opengl/GLRenderer](GLRenderer.md) | opengl | 10 |
| [opengl/GLFrameBufferObject](GLFrameBufferObject.md) | opengl | 9 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 9 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 8 |
| [opengl/GLSaveRestoreFrameBuffer](GLSaveRestoreFrameBuffer.md) | opengl | 8 |
| [opengl/GLAgeGridMaskSource](GLAgeGridMaskSource.md) | opengl | 7 |
| [opengl/GLLight](GLLight.md) | opengl | 7 |
| [opengl/GLRenderTargetImpl](GLRenderTargetImpl.md) | opengl | 7 |
| [opengl/GLVisualRasterSource](GLVisualRasterSource.md) | opengl | 7 |
| [opengl/GLNormalMapSource](GLNormalMapSource.md) | opengl | 6 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 5 |
| [opengl/GLDataRasterSource](GLDataRasterSource.md) | opengl | 4 |
| [gui/GlobeRenderedGeometryCollectionPainter](../gui/GlobeRenderedGeometryCollectionPainter.md) | gui | 3 |
| [opengl/GLMultiResolutionRasterMapView](GLMultiResolutionRasterMapView.md) | opengl | 3 |
| [opengl/GLStateSets](GLStateSets.md) | opengl | 3 |

*... and 17 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLTexture.h
python scripts/gpq.py def GPlatesOpenGL::GLTexture --body
python scripts/gpq.py uses GLTexture --kind class
python scripts/gpq.py hier GLTexture
```

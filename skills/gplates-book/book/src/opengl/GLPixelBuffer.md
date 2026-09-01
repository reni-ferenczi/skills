# GLPixelBuffer

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1179 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLPixelBuffer.h` | C++ | 356 |
| `src/opengl/GLPixelBuffer.cc` | C++ | 56 |

## Overview

[[[PROSE overview unit=opengl/GLPixelBuffer tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLPixelBuffer`](#gplatesopenglglpixelbuffer) | class | `boost::enable_shared_from_this<GLPixelBuffer>` | — | 2 | An abstraction of the OpenGL buffer objects extension as used for pixel buffers containing framebuffer data - either from or to OpenGL (eg, streaming to a texture or reading back pixels from the framebuffer). |

## Members

### `GPlatesOpenGL::GLPixelBuffer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLPixelBuffer>` | public | A convenience typedef for a shared pointer to a non-const GLPixelBuffer. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLPixelBuffer>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<GLPixelBuffer>` | public | A convenience typedef for a weak pointer to a GLPixelBuffer. |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const GLPixelBuffer>` | public | — |
| `create( GLRenderer &renderer, const GLBuffer::shared_ptr_type &buffer)` | method | `shared_ptr_type` | public | Creates a GLPixelBuffer object attached to the specified buffer. |
| `create_as_unique_ptr( GLRenderer &renderer, const GLBuffer::shared_ptr_type &buffer)` | method | `std::unique_ptr<GLPixelBuffer>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `~GLPixelBuffer()` | destructor | `None` | public | — |
| `get_buffer()` | method | `GLBuffer::shared_ptr_type` | public | Returns the 'non-const' buffer used to store the pixel data. |
| `gl_bind_unpack( GLRenderer &renderer)` | method | `void` | public | Binds this pixel buffer as a pixel \*unpack\* buffer so that data can be unpacked (read) from the buffer. |
| `gl_bind_pack( GLRenderer &renderer)` | method | `void` | public | Binds this pixel buffer as a pixel \*pack\* buffer so that data can be packed (written) into the buffer. |
| `gl_draw_pixels( GLRenderer &renderer, GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs the equivalent of the OpenGL command 'glDrawPixels' with the exception that, to mirror 'glReadPixels', the x and y pixel offsets are also specified (internally 'glWindowPos2i(x, y)' is called since 'glDrawPixels' does not accept x ... |
| `gl_read_pixels( GLRenderer &renderer, GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs the equivalent of the OpenGL command 'glReadPixels'. |
| `gl_tex_image_1D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum type, GLint offset)` | method | `void` | private | Performs same function as the glTexImage1D OpenGL function. |
| `gl_tex_image_2D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, GLint offset)` | method | `void` | private | Performs same function as the glTexImage2D OpenGL function. |
| `gl_tex_image_3D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, GLint offset)` | method | `void` | private | Performs same function as the glTexImage3D OpenGL function. |
| `gl_tex_sub_image_1D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, GLint offset)` | method | `void` | private | Performs same function as the glTexSubImage1D OpenGL function. |
| `gl_tex_sub_image_2D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, GLint offset)` | method | `void` | private | Performs same function as the glTexSubImage2D OpenGL function. |
| `gl_tex_sub_image_3D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, GLint offset)` | method | `void` | private | Performs same function as the glTexSubImage3D OpenGL function. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLPIXELBUFFER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLPixelBuffer tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 57 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 57 |
| [opengl/GLAgeGridMaskSource](GLAgeGridMaskSource.md) | opengl | 48 |
| [opengl/GLTextureUtils](GLTextureUtils.md) | opengl | 45 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 24 |
| [opengl/GLVisualRasterSource](GLVisualRasterSource.md) | opengl | 21 |
| [opengl/GLContext](GLContext.md) | opengl | 19 |
| [opengl/GLFrameBufferObject](GLFrameBufferObject.md) | opengl | 19 |
| [opengl/GLMultiResolutionCubeRaster](GLMultiResolutionCubeRaster.md) | opengl | 17 |
| [opengl/GLSaveRestoreFrameBuffer](GLSaveRestoreFrameBuffer.md) | opengl | 17 |
| [opengl/GLNormalMapSource](GLNormalMapSource.md) | opengl | 15 |
| [opengl/GLPixelBufferObject](GLPixelBufferObject.md) | opengl | 14 |
| [opengl/GLScalarField3DGenerator](GLScalarField3DGenerator.md) | opengl | 13 |
| [opengl/GLTexture](GLTexture.md) | opengl | 13 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 11 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](GLMultiResolutionCubeReconstructedRaster.md) | opengl | 11 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 11 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 10 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 10 |
| [opengl/GLLight](GLLight.md) | opengl | 8 |

*... and 21 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLPixelBuffer.h
python scripts/gpq.py def GPlatesOpenGL::GLPixelBuffer --body
python scripts/gpq.py uses GLPixelBuffer --kind class
python scripts/gpq.py hier GLPixelBuffer
```

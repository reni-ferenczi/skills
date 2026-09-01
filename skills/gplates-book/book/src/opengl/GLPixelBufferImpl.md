# GLPixelBufferImpl

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 317 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLPixelBufferImpl.h` | C++ | 461 |
| `src/opengl/GLPixelBufferImpl.cc` | C++ | 300 |

## Overview

`GLPixelBufferImpl` is the fallback `GLPixelBuffer` implementation used when the pixel buffer object extension (`GL_ARB_pixel_buffer_object`) is not supported by the runtime system; the constructor asserts that it is indeed absent. Rather than truly transferring pixel data through a bound buffer object, it simulates the pixel buffer contract with plain OpenGL 1.1 client-side memory arrays: `gl_bind_unpack`/`gl_bind_pack` explicitly unbind any pixel pack/unpack buffer object, and each `gl_tex_image_*`/`gl_tex_sub_image_*`/`gl_draw_pixels`/`gl_read_pixels` call forces client-array mode before delegating straight to the matching `GLRenderer` method (or raw `glTexImage*`/`glTexSubImage*` calls), so the pointer/offset arguments are treated as ordinary CPU pointers into client memory rather than buffer-relative offsets.

It exists purely to give `GLPixelBuffer`'s callers — texture streaming and framebuffer readback code — a uniform interface regardless of whether hardware pixel buffer objects are available, so that call sites do not need their own fallback branch when the extension is missing.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLPixelBufferImpl`](#gplatesopenglglpixelbufferimpl) | class | [`GLPixelBuffer`](GLPixelBuffer.md) | — | 0 | An implementation of the OpenGL buffer objects extension as used for pixel buffers containing framebuffer data - either from or to OpenGL (eg, streaming to a texture or reading back pixels from the framebuffer). |

## Members

### `GPlatesOpenGL::GLPixelBufferImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLPixelBufferImpl>` | public | A convenience typedef for a shared pointer to a GLPixelBufferImpl. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLPixelBufferImpl>` | public | — |
| `create( GLRenderer &renderer, const GLBufferImpl::shared_ptr_type &buffer)` | method | `shared_ptr_type` | public | Creates a GLPixelBufferImpl object attached to the specified buffer. |
| `create_as_unique_ptr( GLRenderer &renderer, const GLBufferImpl::shared_ptr_type &buffer)` | method | `std::unique_ptr<GLPixelBufferImpl>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `get_buffer()` | method | `GLBuffer::shared_ptr_to_const_type` | public | Returns the buffer used to store the pixel data. |
| `gl_bind_unpack( GLRenderer &renderer)` | method | `void` | public | Binds this pixel buffer as a pixel \*unpack\* buffer so that data can be unpacked (read) from the buffer. |
| `gl_bind_pack( GLRenderer &renderer)` | method | `void` | public | Binds this pixel buffer as a pixel \*pack\* buffer so that data can be packed (written) into the buffer. |
| `gl_draw_pixels( GLRenderer &renderer, GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs the equivalent of the OpenGL command 'glDrawPixels' with the exception that, to mirror 'glReadPixels', the x and y pixel offsets are also specified (internally 'glWindowPos2i(x, y)' is called since 'glDrawPixels' does not accept x ... |
| `gl_read_pixels( GLRenderer &renderer, GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs the equivalent of the OpenGL command 'glReadPixels'. |
| `gl_tex_image_1D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs same function as the glTexImage1D OpenGL function. |
| `gl_tex_image_1D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum type, const GLvoid *pixels)` | method | `void` | public | Performs same function as the glTexImage1D OpenGL function using pixel data from pixels. |
| `gl_tex_image_2D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs same function as the glTexImage2D OpenGL function. |
| `gl_tex_image_2D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const GLvoid *pixels)` | method | `void` | public | Performs same function as the glTexImage2D OpenGL function using pixel data from pixels. |
| `gl_tex_image_3D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs same function as the glTexImage3D OpenGL function. |
| `gl_tex_image_3D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, const GLvoid *pixels)` | method | `void` | public | Performs same function as the glTexImage3D OpenGL function using pixel data from pixels. |
| `gl_tex_sub_image_1D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs same function as the glTexSubImage1D OpenGL function. |
| `gl_tex_sub_image_1D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const GLvoid *pixels)` | method | `void` | public | Performs same function as the glTexSubImage1D OpenGL function. |
| `gl_tex_sub_image_2D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs same function as the glTexSubImage2D OpenGL function. |
| `gl_tex_sub_image_2D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const GLvoid *pixels)` | method | `void` | public | Performs same function as the glTexSubImage2D OpenGL function. |
| `gl_tex_sub_image_3D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs same function as the glTexSubImage3D OpenGL function. |
| `gl_tex_sub_image_3D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid *pixels)` | method | `void` | public | Performs same function as the glTexSubImage3D OpenGL function. |
| `d_buffer` | field | `GLBufferImpl::shared_ptr_type` | private | The buffer being targeted by this pixel buffer. |
| `GLPixelBufferImpl( GLRenderer &renderer, const GLBufferImpl::shared_ptr_type &buffer)` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLPIXELBUFFERIMPL_H` | macro | `None` | — |

## Notes

- Constructing this class when `GL_ARB_pixel_buffer_object` (and `GL_ARB_vertex_buffer_object`) *is* actually supported trips an assertion failure — it is meant only as the no-extension fallback, selected by whatever factory chooses between it and the real buffer-object-backed implementation.
- `create_as_unique_ptr` exists specifically to guarantee single ownership before the object is optionally handed off to a `shared_ptr` via `create`.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLTexture](GLTexture.md) | opengl | 7 |
| [opengl/GLPixelBuffer](GLPixelBuffer.md) | opengl | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLPixelBufferImpl.h
python scripts/gpq.py def GPlatesOpenGL::GLPixelBufferImpl --body
python scripts/gpq.py uses GLPixelBufferImpl --kind class
python scripts/gpq.py hier GLPixelBufferImpl
```

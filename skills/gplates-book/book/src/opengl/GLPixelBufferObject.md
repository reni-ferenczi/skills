# GLPixelBufferObject

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 421 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLPixelBufferObject.h` | C++ | 325 |
| `src/opengl/GLPixelBufferObject.cc` | C++ | 310 |

## Overview

`GLPixelBufferObject` is the real, `GL_ARB_pixel_buffer_object`-backed implementation of the `GLPixelBuffer` interface, as opposed to `GLPixelBufferImpl`, which simulates the same interface with client-side memory arrays when that extension is unavailable. It wraps a `GLBufferObject` and binds it to the `GL_PIXEL_UNPACK_BUFFER` or `GL_PIXEL_PACK_BUFFER` target (`gl_bind_unpack`/`gl_bind_pack`) so that texture uploads (`gl_tex_image_*`, `gl_tex_sub_image_*`), `glDrawPixels`-equivalent uploads and `glReadPixels`-equivalent downloads transfer through server-side (GPU-resident) buffer memory rather than through client pointers, letting pixel transfer and rendering overlap asynchronously.

It multiply inherits `GLObject` (for the pooled-resource typedefs shared by all GL object wrappers) alongside `GLPixelBuffer`; like other objects meant to live in a `GPlatesUtils::ObjectCache`, it exposes `boost::shared_ptr`/`weak_ptr` rather than the intrusive pointer used elsewhere in `opengl`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLPixelBufferObject`](#gplatesopenglglpixelbufferobject) | class | [`GLPixelBuffer`](GLPixelBuffer.md)<br>[`GLObject`](GLObject.md) | — | 0 | An OpenGL buffer object used for pixel buffers containing framebuffer data - either from or to OpenGL (eg, streaming to a texture or reading back pixels from the framebuffer). |

## Members

### `GPlatesOpenGL::GLPixelBufferObject`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLPixelBufferObject>` | public | A convenience typedef for a shared pointer to a GLPixelBufferObject. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLPixelBufferObject>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<GLPixelBufferObject>` | public | A convenience typedef for a weak pointer to a GLPixelBufferObject. |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const GLPixelBufferObject>` | public | — |
| `get_unpack_target_type()` | method | `GLenum` | public | Returns the target GL\_PIXEL\_UNPACK\_BUFFER. |
| `get_pack_target_type()` | method | `GLenum` | public | Returns the target GL\_PIXEL\_PACK\_BUFFER. |
| `create( GLRenderer &renderer, const GLBufferObject::shared_ptr_type &buffer)` | method | `shared_ptr_type` | public | Creates a shared pointer to a GLPixelBufferObject object. |
| `create_as_unique_ptr( GLRenderer &renderer, const GLBufferObject::shared_ptr_type &buffer)` | method | `std::unique_ptr<GLPixelBufferObject>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `get_buffer()` | method | `GLBuffer::shared_ptr_to_const_type` | public | Returns the buffer used to store the pixel data. |
| `gl_bind_unpack( GLRenderer &renderer)` | method | `void` | public | Binds this pixel buffer as a pixel \*unpack\* buffer so that data can be unpacked (read) from the buffer. |
| `gl_bind_pack( GLRenderer &renderer)` | method | `void` | public | Binds this pixel buffer as a pixel \*pack\* buffer so that data can be packed (written) into the buffer. |
| `gl_draw_pixels( GLRenderer &renderer, GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs the equivalent of the OpenGL command 'glDrawPixels' with the exception that, to mirror 'glReadPixels', the x and y pixel offsets are also specified (internally 'glWindowPos2i(x, y)' is called since 'glDrawPixels' does not accept x ... |
| `gl_read_pixels( GLRenderer &renderer, GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs the equivalent of the OpenGL command 'glReadPixels'. |
| `gl_tex_image_1D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs same function as the glTexImage1D OpenGL function. |
| `gl_tex_image_2D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs same function as the glTexImage2D OpenGL function. |
| `gl_tex_image_3D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs same function as the glTexImage3D OpenGL function. |
| `gl_tex_sub_image_1D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs same function as the glTexSubImage1D OpenGL function. |
| `gl_tex_sub_image_2D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs same function as the glTexSubImage2D OpenGL function. |
| `gl_tex_sub_image_3D( GLRenderer &renderer, const boost::shared_ptr<const GLTexture> &texture, GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs same function as the glTexSubImage3D OpenGL function. |
| `get_buffer_object()` | method | `GLBufferObject::shared_ptr_to_const_type` | public | Returns the buffer object. |
| `d_buffer` | field | `GLBufferObject::shared_ptr_type` | private | — |
| `GLPixelBufferObject( GLRenderer &renderer, const GLBufferObject::shared_ptr_type &buffer)` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLPIXELBUFFEROBJECT_H` | macro | `None` | — |

## Notes

- Requires the `GL_ARB_pixel_buffer_object` extension; code choosing between this class and `GLPixelBufferImpl` must check for that support first, since this class does not fall back on its own.
- The same underlying buffer can legally be bound to both the pack and unpack targets simultaneously, per the `gl_bind_unpack`/`gl_bind_pack` documentation.
- `create_as_unique_ptr` exists to guarantee single ownership before optional conversion to a `shared_ptr` via `create`.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRenderer](GLRenderer.md) | opengl | 15 |
| [opengl/GLVertexBufferObject](GLVertexBufferObject.md) | opengl | 7 |
| [opengl/GLPixelBuffer](GLPixelBuffer.md) | opengl | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLPixelBufferObject.h
python scripts/gpq.py def GPlatesOpenGL::GLPixelBufferObject --body
python scripts/gpq.py uses GLPixelBufferObject --kind class
python scripts/gpq.py hier GLPixelBufferObject
```

# GLPixelBuffer

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1179 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLPixelBuffer.h` | C++ | 356 |
| `src/opengl/GLPixelBuffer.cc` | C++ | 56 |

## Overview

The pixel-transfer end of the buffer abstraction: an interface for moving image
data between a `GLBuffer` and the framebuffer or a texture. It is pure
interface — `create_as_unique_ptr` is a factory that `dynamic_pointer_cast`s the
`GLBuffer` it is handed and returns a `GLPixelBufferObject` if that buffer is a
real `GLBufferObject`, or a `GLPixelBufferImpl` if it is the client-memory
`GLBufferImpl`. The choice was already made upstream by `GLBuffer::create`,
which consults `GLCapabilities::buffer::gl_ARB_pixel_buffer_object` and falls
back to client memory when the extension is missing; `GLPixelBuffer` just
follows it. This mirroring is what lets the rest of `src/opengl` — the raster
sources, `GLScalarField3D`, `GLRasterCoRegistration`, `GLSaveRestoreFrameBuffer`
— be written once against one interface and still run on hardware with no pixel
buffer objects.

The point of going through a pixel buffer rather than a client array is
asynchrony, and the header spells out the contract. On the
`GLPixelBufferObject` path, `gl_draw_pixels` and `gl_read_pixels` start a DMA
transfer and return without blocking; the stall is deferred until something
actually touches the buffer's memory through `get_buffer()`. So the intended
pattern is to issue the transfer, do unrelated work, and only then read or
write — or double-buffer with two alternating pixel buffers, which is exactly
what the heavy clients do. On the `GLPixelBufferImpl` path there is no
asynchrony at all, only source compatibility.

The public surface is deliberately small — bind as pack or unpack, draw pixels,
read pixels. The `glTexImage*` and `glTexSubImage*` equivalents are private with
`GLTexture` as the sole friend, so uploading a texture from a pixel buffer is
always phrased as an operation on the texture. One further thing the header
points out: nothing stops the same `GLBuffer` being wrapped by both a
`GLPixelBuffer` and a `GLVertexBuffer`, or bound to both the pack and unpack
targets at once, which is how a shader can render to the framebuffer, have the
result read back into a buffer, and then have that buffer drawn as vertex data
without a CPU round trip.

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

- **The two public transfer calls do not bind for you.** `gl_read_pixels`
  requires a prior `gl_bind_pack`, `gl_draw_pixels` a prior `gl_bind_unpack`;
  the private `gl_tex_*` family, by contrast, binds both the buffer and the
  texture internally. Getting this wrong on the `GLPixelBufferObject` path
  silently transfers against whatever buffer happened to be bound.
- **Buffer size is never checked here.** The caller must have allocated enough
  through `GLBuffer::gl_buffer_data` for the whole rectangle being read or
  written; every `offset` parameter is a *byte* offset into the buffer, not a
  pixel index.
- **`gl_draw_pixels` moves the raster position.** `glDrawPixels` takes no x/y, so
  the implementation issues `glWindowPos2i(x, y)` first to make the signature
  match `gl_read_pixels`. That is a real state change to the current raster
  position, not just a convenience.
- **Must be owned by a `shared_ptr`.** `GLPixelBufferObject::gl_bind_unpack` and
  `gl_bind_pack` call `shared_from_this()` to hand themselves to the renderer,
  so a stack or `unique_ptr`-owned instance throws on bind.
  `create_as_unique_ptr` exists to feed `GPlatesUtils::ObjectCache`, which is
  also why the class uses `boost::shared_ptr` rather than the
  `non_null_intrusive_ptr` used elsewhere in GPlates.
- **Recycled buffers keep their size.** `GLContext::SharedState::acquire_pixel_buffer`
  pools pixel buffers keyed on size and usage and warns if a recycled buffer's
  size was changed underneath it — resizing a pooled buffer defeats the pooling.
- Asynchronous behaviour is a property of the *derived* type. Code that reasons
  about latency has to know whether it got a `GLPixelBufferObject` or a
  `GLPixelBufferImpl`; against the `GLPixelBuffer` interface alone the transfer
  may or may not have completed on return.

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

# GLSaveRestoreFrameBuffer

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 647 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLSaveRestoreFrameBuffer.h` | C++ | 171 |
| `src/opengl/GLSaveRestoreFrameBuffer.cc` | C++ | 452 |

## Overview

Lets the main OpenGL framebuffer be temporarily used as a render target
without permanently losing its contents, by copying its colour (and
optionally depth/stencil) contents out to textures and pixel buffers on
`save`, then writing them back on `restore`. It exists specifically for
systems without `GL_EXT_framebuffer_object`: when that extension is available,
`GLRenderTarget`/`GLFrameBufferObject` render directly to a texture and this
class is largely redundant — `GLRendererImpl::RenderTargetBlock::MainFrameBuffer`
uses it as the fallback path for render-to-texture on such hardware.

Because the framebuffer can exceed the maximum texture dimensions supported by
the GPU, `save`/`restore` tile the copy internally using a `GLTileRender`
(`d_save_restore_texture_tile_render`), spreading the saved region across
however many colour textures are needed; depth and stencil, however, are
captured into a single `GLPixelBuffer` each regardless of framebuffer size.
The save/restore textures and buffers are not acquired at construction — only
between `save` and `restore`, via `acquire_save_restore_colour_texture` — and
are released again once `restore` completes.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLSaveRestoreFrameBuffer`](#gplatesopenglglsaverestoreframebuffer) | class | — | — | 0 | Copies the currently bound colour framebuffer (and optionally depth and stencil buffers) to a temporary texture and subsequently restores framebuffer from that texture. |

## Members

### `GPlatesOpenGL::GLSaveRestoreFrameBuffer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLSaveRestoreFrameBuffer( const GLCapabilities &capabilities, unsigned int save_restore_width, unsigned int save_restore_height, GLint save_restore_colour_texture_internalformat = GL_RGBA8, bool save_restore_depth_buffer = false, bool save_restore_stencil_buffer = false)` | constructor | `None` | public | Specify the save/restore dimensions. |
| `save( GLRenderer &renderer)` | method | `void` | public | Saves the currently bound (colour) framebuffer to a temporary internal texture of power-of-two dimensions large enough to contain the specified save/restore dimensions. |
| `restore( GLRenderer &renderer)` | method | `void` | public | Restores the (colour) framebuffer to its contents prior to the GLSaveRestoreFrameBuffer constructor. |
| `SaveRestore` | struct | `None` | private | The save/restore colour textures and depth/stencil pixel buffers. |
| `d_save_restore_frame_buffer_width` | field | `unsigned int` | private | — |
| `d_save_restore_frame_buffer_height` | field | `unsigned int` | private | — |
| `d_save_restore_texture_width` | field | `unsigned int` | private | — |
| `d_save_restore_texture_height` | field | `unsigned int` | private | — |
| `d_save_restore_colour_texture_internal_format` | field | `GLint` | private | — |
| `d_save_restore_texture_tile_render` | field | `GLTileRender` | private | We use a tile render in case the save/restore dimensions are larger than the maximum texture dimensions - in which case multiple save/restore textures are needed -. this should never happen though (but it might for really old hardware with ... |
| `d_save_restore_depth_pixel_buffer_size` | field | `boost::optional<unsigned int>` | private | Size, in bytes, of save/restore pixel buffer for depth values. |
| `d_save_restore_stencil_pixel_buffer_size` | field | `boost::optional<unsigned int>` | private | Size, in bytes, of save/restore pixel buffer for stencil values. |
| `d_save_restore` | field | `boost::optional<SaveRestore>` | private | One (or more) save/restore colour textures (and optional depth/stencil pixel buffers) that span the framebuffer. |
| `between_save_and_restore()` | method | `bool` | private | Returns true if between save and restore. |
| `acquire_save_restore_colour_texture( GLRenderer &renderer)` | method | `GLTexture::shared_ptr_type` | private | Acquire one save/restore colour texture. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_power_of_two_save_restore_dimension( const GLCapabilities &capabilities, unsigned int save_restore_dimension)` | function | `unsigned int` | Returns the next power-of-two dimension greater-than-or-equal to save\_restore\_dimension. |
| `GPLATES_OPENGL_GLSAVERESTOREFRAMEBUFFER_H` | macro | `None` | — |

## Notes

Callers must not draw outside the constructor's `save_restore_width`/`height`
region between `save` and `restore` — the header recommends enabling the
scissor test with a matching scissor rectangle to enforce this, since
anything drawn outside that region will not be restored. `restore` itself
temporarily resets OpenGL to the default state, so it ignores any scissoring
in effect and always restores the entire saved region.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLOffScreenContext](GLOffScreenContext.md) | opengl | 4 |
| [opengl/GLRendererImpl](GLRendererImpl.md) | opengl | 2 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLSaveRestoreFrameBuffer.h
python scripts/gpq.py def GPlatesOpenGL::GLSaveRestoreFrameBuffer --body
python scripts/gpq.py uses GLSaveRestoreFrameBuffer --kind class
python scripts/gpq.py hier GLSaveRestoreFrameBuffer
```

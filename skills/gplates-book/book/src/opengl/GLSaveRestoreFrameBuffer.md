# GLSaveRestoreFrameBuffer

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 647 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLSaveRestoreFrameBuffer.h` | C++ | 171 |
| `src/opengl/GLSaveRestoreFrameBuffer.cc` | C++ | 452 |

## Overview

[[[PROSE overview unit=opengl/GLSaveRestoreFrameBuffer tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=opengl/GLSaveRestoreFrameBuffer tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

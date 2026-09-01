# GLFrameBufferObject

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 310 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLFrameBufferObject.h` | C++ | 616 |
| `src/opengl/GLFrameBufferObject.cc` | C++ | 914 |

## Overview

[[[PROSE overview unit=opengl/GLFrameBufferObject tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLFrameBufferObject`](#gplatesopenglglframebufferobject) | class | [`GLObject`](GLObject.md)<br>`boost::enable_shared_from_this<GLFrameBufferObject>` | — | 0 | A wrapper around a framebuffer object. |

## Members

### `GPlatesOpenGL::GLFrameBufferObject`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLFrameBufferObject>` | public | A convenience typedef for a shared pointer to a GLFrameBufferObject. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLFrameBufferObject>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<GLFrameBufferObject>` | public | A convenience typedef for a weak pointer to a GLFrameBufferObject. |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const GLFrameBufferObject>` | public | — |
| `Allocator` | class | `None` | public | Policy class to allocate and deallocate OpenGL framebuffer objects. |
| `resource_handle_type` | typedef | `GLuint` | public | Typedef for a resource handle. |
| `resource_type` | typedef | `GLObjectResource<resource_handle_type, Allocator>` | public | Typedef for a resource. |
| `resource_manager_type` | typedef | `GLObjectResourceManager<resource_handle_type, Allocator>` | public | Typedef for a resource manager. |
| `AttachmentType` | enum | `None` | public | Types of attachments. |
| `Classification` | class | `None` | public | Classifies a frame buffer object to, for example, assist with frame buffer switching efficiency. |
| `DEFAULT_DRAW_READ_BUFFER` | field | `GLenum` | public | The default buffer (GL\_COLOR\_ATTACHMENT0\_EXT) for the glDrawBuffer(s)/glReadBuffer state contained in a framebuffer object. |
| `gl_generate_mipmap( GLRenderer &renderer, GLenum texture_target, const GLTexture::shared_ptr_to_const_type &texture)` | method | `void` | public | Performs same function as the glGenerateMipmap OpenGL function. |
| `create( GLRenderer &renderer)` | method | `shared_ptr_type` | public | Creates a shared pointer to a GLFrameBufferObject object. |
| `create_as_unique_ptr( GLRenderer &renderer)` | method | `std::unique_ptr<GLFrameBufferObject>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `gl_attach_texture_1D( GLRenderer &renderer, GLenum texture_target, const GLTexture::shared_ptr_to_const_type &texture, GLint level, GLenum attachment)` | method | `void` | public | Performs same function as the glFramebufferTexture1D OpenGL function. |
| `gl_attach_texture_2D( GLRenderer &renderer, GLenum texture_target, const GLTexture::shared_ptr_to_const_type &texture, GLint level, GLenum attachment)` | method | `void` | public | Performs same function as the glFramebufferTexture2D OpenGL function. |
| `gl_attach_texture_3D( GLRenderer &renderer, GLenum texture_target, const GLTexture::shared_ptr_to_const_type &texture, GLint level, GLint zoffset, GLenum attachment)` | method | `void` | public | Performs same function as the glFramebufferTexture3D OpenGL function. |
| `gl_attach_texture_array_layer( GLRenderer &renderer, const GLTexture::shared_ptr_to_const_type &texture, GLint level, GLint layer, GLenum attachment)` | method | `void` | public | Performs same function as the glFramebufferTextureLayer OpenGL function - can be used for 1D and 2D array textures (and regular 3D textures - where it does same as gl\_attach\_texture\_3D). |
| `gl_attach_texture_array( GLRenderer &renderer, const GLTexture::shared_ptr_to_const_type &texture, GLint level, GLenum attachment)` | method | `void` | public | Performs same function as the glFramebufferTexture OpenGL function - can be used for 1D and 2D array textures. |
| `gl_attach_render_buffer( GLRenderer &renderer, const GLRenderBufferObject::shared_ptr_to_const_type &render_buffer, GLenum attachment)` | method | `void` | public | Performs same function as the glFramebufferRenderbuffer OpenGL function. |
| `gl_detach( GLRenderer &renderer, GLenum attachment)` | method | `void` | public | Detaches specified attachment point. |
| `gl_detach_all( GLRenderer &renderer)` | method | `void` | public | Detaches any currently attached attachment points. |
| `gl_draw_buffers( GLRenderer &renderer, const std::vector<GLenum> &bufs = std::vector<GLenum>(1, DEFAULT_DRAW_READ_BUFFER))` | method | `void` | public | Performs same function as the glDrawBuffer/glDrawBuffers OpenGL function. |
| `gl_read_buffer( GLRenderer &renderer, GLenum mode = DEFAULT_DRAW_READ_BUFFER)` | method | `void` | public | Performs same function as the glReadBuffer OpenGL function. |
| `gl_check_frame_buffer_status( GLRenderer &renderer)` | method | `bool` | public | Effectively does the same as 'glCheckFramebufferStatusEXT' and returns true if the status is 'GL\_FRAMEBUFFER\_COMPLETE\_EXT' or false is the status is 'GL\_FRAMEBUFFER\_UNSUPPORTED\_EXT'. |
| `get_frame_buffer_dimensions()` | method | `boost::optional< std::pair<GLuint/*width*/, GLuint/*height*/> >` | public | Returns the framebuffer dimensions, or boost::none if no attachments have been specified or if an attachment has not had its storage specified. |
| `get_frame_buffer_resource_handle()` | method | `resource_handle_type` | public | Returns the framebuffer handle. |
| `AttachmentPoint` | struct | `None` | private | Information for a framebuffer object attachment point. |
| `attachment_point_seq_type` | typedef | `std::vector<boost::optional<AttachmentPoint> >` | private | Typedef for a sequence of attachments. |
| `d_resource` | field | `resource_type::non_null_ptr_to_const_type` | private | — |
| `d_attachment_points` | field | `attachment_point_seq_type` | private | All attachment points. |
| `GLFrameBufferObject( GLRenderer &renderer)` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `MAX_NUM_ATTACHMENTS` | variable | `unsigned int` | The maximum number of attachments (supported by GL\_EXT\_framebuffer\_object). |
| `get_attachment_index( GLenum attachment)` | function | `unsigned int` | Converts attachment GLenum into an index starting at GL\_COLOR\_ATTACHMENT0\_EXT. |
| `assert_valid_attachment( GLRenderer &renderer, GLenum attachment, const GPlatesUtils::CallStack::Trace &assert_location)` | function | `void` | — |
| `DEFAULT_DRAW_READ_BUFFER` | variable | `GLenum` | — |
| `GPLATES_OPENGL_GLFRAMEBUFFEROBJECT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLFrameBufferObject tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRenderTargetImpl](GLRenderTargetImpl.md) | opengl | 40 |
| [opengl/GLContext](GLContext.md) | opengl | 36 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 28 |
| [opengl/GLRenderer](GLRenderer.md) | opengl | 27 |
| [opengl/GLLight](GLLight.md) | opengl | 17 |
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 10 |
| [opengl/GLState](GLState.md) | opengl | 7 |
| [opengl/GLStateSets](GLStateSets.md) | opengl | 5 |
| [opengl/GLRendererImpl](GLRendererImpl.md) | opengl | 2 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLFrameBufferObject.h
python scripts/gpq.py def GPlatesOpenGL::GLFrameBufferObject --body
python scripts/gpq.py uses GLFrameBufferObject --kind class
python scripts/gpq.py hier GLFrameBufferObject
```

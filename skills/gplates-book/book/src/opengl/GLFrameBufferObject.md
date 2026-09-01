# GLFrameBufferObject

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 310 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLFrameBufferObject.h` | C++ | 616 |
| `src/opengl/GLFrameBufferObject.cc` | C++ | 914 |

## Overview

This is the off-screen render-target primitive that everything else in
`src/opengl` renders to texture through: `GLRenderTargetImpl`,
`GLScreenRenderTarget`, `GLScalarField3D`, `GLLight` and
`GLRasterCoRegistration` all end up holding one. It wraps a single native
framebuffer name from `GL_EXT_framebuffer_object` — deliberately the EXT
extension rather than the more capable `GL_ARB_framebuffer_object`, because EXT
had far wider driver support at the time. The cost of that choice is the
restriction repeated throughout the header: every attachment point must have the
same 2D dimensions, which is why `get_frame_buffer_dimensions` needs no
attachment argument and why `Classification` carries one width/height pair for
the whole object.

The distinguishing design decision is that none of the `gl_*` methods assume the
framebuffer is bound. Each one opens a `GLRenderer::BindFrameBufferAndApply`
scope guard (`gl_generate_mipmap` uses the `UnbindFrameBufferAndApply` sibling),
which binds through the renderer, forces the renderer's deferred state to be
flushed to real OpenGL before the raw `gl*EXT` call is issued, and restores the
caller's previous binding on the way out. That is what makes it safe to attach a
texture or change draw buffers from anywhere inside a render pass. Alongside the
native handle the object keeps a shadow copy of every attachment in
`d_attachment_points`, holding a `shared_ptr` to the attached `GLTexture` or
`GLRenderBufferObject` so it cannot be destroyed while attached; `gl_detach`
replays that record to issue the matching detach call, and
`get_frame_buffer_dimensions` answers from the attached object rather than
querying GL.

`Classification` is the second half of the design. It is a plain value — a
`boost::tuple` of dimensions plus a per-attachment-point (type, internal format,
target) triple — describing the *shape* of a framebuffer without holding one.
`GLContext::NonSharedState` uses it two ways: as the key of a pool of recyclable
framebuffer objects, so render targets with the same texture format and
dimensions share one FBO (the Nvidia guidance quoted in the header), and as the
key of `check_framebuffer_object_completeness`, which memoises the result of the
expensive `glCheckFramebufferStatus` call per shape. The pool lives in
`NonSharedState` rather than `SharedState` because native framebuffer objects
cannot be shared between OpenGL contexts — `GLRenderTargetImpl` works around
that by creating one `GLFrameBufferObject` per context and sharing only the
texture.

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

- **Must be owned by a `shared_ptr`.** Every mutator calls `shared_from_this()`
  to bind itself through the renderer. `create_as_unique_ptr` exists only to
  hand a uniquely-owned object to `GPlatesUtils::ObjectCache`, which
  immediately wraps it in a `shared_ptr`; calling `gl_attach_*` on a
  `unique_ptr` you still hold yourself throws `boost::bad_weak_ptr`. The whole
  class hierarchy uses `boost::shared_ptr` instead of
  `non_null_intrusive_ptr` for the same reason — `ObjectCache` compatibility.
- **Recycled objects are not clean.** The cache installs a custom deleter, so
  releasing the last `shared_ptr` returned by
  `GLContext::NonSharedState::acquire_frame_buffer_object` returns the object to
  the pool instead of deleting the GL name — attachments and draw/read buffer
  state survive. That is why `acquire_frame_buffer_object` calls
  `gl_detach_all`, `gl_draw_buffers` and `gl_read_buffer` before handing an
  object back out. If you create your own framebuffer objects instead of going
  through the pool, you own that reset.
- **Draw/read buffer state lives inside the framebuffer object**, not in the
  renderer's state vector. `gl_draw_buffers` and `gl_read_buffer` therefore bind
  and issue immediately rather than being recorded as `GLState` sets, and the
  window-system framebuffer's equivalents are not managed here at all.
- **Attachment preconditions are dimensionality checks.** `gl_attach_texture_1D`
  asserts width and *no* height/depth, `_2D` asserts width and height and no
  depth, `_3D` asserts all three. A texture that has not had storage specified
  yet (`GLTexture::gl_tex_image_*`) or the wrong overload both trip the same
  `PreconditionViolationError`. The attachment enum itself is validated against
  the runtime `gl_max_color_attachments`, so an attachment index legal on one
  card can throw on another.
- **`d_attachment_points` is always 18 slots** (16 colour plus depth plus
  stencil, the EXT maximum) regardless of what the driver actually supports;
  slots above the runtime limit simply stay empty. `get_attachment_index` maps
  depth to 16 and stencil to 17.
- **`gl_check_frame_buffer_status` is a profiling hazard.** Measured at
  40–100 µs per call against a couple of µs for a draw call, and it showed up
  high on the CPU profile for age-grid-smoothed reconstructed rasters and filled
  polygons. Prefer `GLContext::NonSharedState::check_framebuffer_object_completeness`,
  which caches per `Classification`. It returns `false` both for
  `GL_FRAMEBUFFER_UNSUPPORTED_EXT` and for any unexpected status (logged via
  `qWarning`) — the abort was deliberately removed after a user hit an
  unexpected status on a virtualised GPU.
- **Detaching a texture array uses `glFramebufferRenderbufferEXT` with a zero
  render buffer**, not `glFramebufferTextureEXT` with a zero texture, because
  the latter produced an invalid-value error on an NVIDIA driver. Both are legal
  per spec. Detaching a point that is not attached is not an error: it logs a
  warning and returns.
- **One context only.** The resource manager is in `GLContext::NonSharedState`,
  so the native name belongs to the context that created it and stays invalid in
  any other context, even one sharing textures with it.
- `Classification`'s setters take a `GLRenderer &` purely to validate the
  attachment enum against capabilities; `set_dimensions` ignores it entirely.

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

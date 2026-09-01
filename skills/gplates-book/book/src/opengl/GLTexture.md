# GLTexture

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 491 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLTexture.h` | C++ | 586 |
| `src/opengl/GLTexture.cc` | C++ | 449 |

## Overview

`GLTexture` wraps one OpenGL texture name and adds the two things raw `glGenTextures` does not give you: lifetime tied to the context's resource manager, and a record of what the texture actually is. The `gl_tex_image_*` and `gl_copy_tex_image_*` methods cache the width, height and depth of level 0, and the internal format from whatever level they were called on, as they go, so the rest of the backend can ask a texture its dimensions without a `glGetTexLevelParameteriv` round trip — `GLRenderer::begin_render_target_2D` depends on exactly this to size its render target, and `GLFrameBufferObject` and `GLSaveRestoreFrameBuffer` on the same information. The header notes why the name has no `Object` suffix, unlike `GLBufferObject` or `GLFrameBufferObject`: texture objects are core in OpenGL 1.1, the lowest version GPlates supports, so there is no software-emulation fallback to distinguish from.

Every method takes a `GLRenderer &`, because a texture cannot be modified without being bound and binding is global state the renderer owns. Each one opens a `GLRenderer::BindTextureAndApply` scope on texture unit zero, which both forces the renderer to push the binding to the driver *before* the direct `glTexParameter*`/`glCopyTexImage2D` call and reverts the binding afterwards, so a client's own bindings survive. The image-upload paths go one step further and route through `GLPixelBuffer`: the client-memory overloads call the corresponding `GLPixelBufferImpl` static, which guarantees no native pixel buffer object is left bound while sourcing from client memory, and the `GLPixelBuffer` overloads hand the work to the buffer itself. That inversion — the pixel buffer uploads to the texture rather than the texture reading from the buffer — is why the buffer overloads take an `offset` and why `GLTexture` needs `boost::enable_shared_from_this` to pass itself along.

The underlying name lives in a `GLObjectResource<GLuint, Allocator>` obtained from the context's shared state, so the texture is shared with any context that shares state with the one it was created on, and destruction only *queues* the `glDeleteTextures` — the resource manager issues it later, when a context is current.

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

**The cached dimensions are a promise the caller must keep.** They are recorded only from level-0 calls, and only from the methods that specify a whole image — `gl_tex_sub_image_*` deliberately does not touch them. Nothing here re-reads the driver, so if you change a texture's size or format behind this class's back, everything downstream believes the stale values. `GLContext::SharedState::acquire_texture` treats that as a hard error: on recycling a cached texture it asserts that width, height, depth and internal format still match the key it was cached under, and throws `OpenGLException` if a previous client changed them.

**Dimensions are `boost::optional` for a reason.** They stay `boost::none` until an image-specification call has been made, so `get_width()` returning nothing means "uninitialised texture", which is precisely the precondition `GLRenderer::begin_render_target_2D` asserts on. `get_height()` also carries the layer count for a `GL_TEXTURE_1D_ARRAY` and `get_depth()` for a `GL_TEXTURE_2D_ARRAY`, so a non-`none` height does not by itself mean the texture is two-dimensional. The Doxygen on `get_internal_format` is inverted and says the opposite of what the code does — the value is present *after* an image specification call, not before.

**Must live in a `shared_ptr` before any method is called.** Every method that binds calls `shared_from_this()`. `create_as_unique_ptr` exists only so ownership can be handed straight to a `GPlatesUtils::ObjectCache` (which is also why `boost::shared_ptr` is used here rather than `non_null_intrusive_ptr`); calling a method on the `unique_ptr` before the cache has taken it throws `boost::bad_weak_ptr`.

**Deallocation is deferred and context-aware.** `~GLObjectResource` only queues the handle with the resource manager rather than calling `glDeleteTextures`, so a texture can be dropped on any thread or with no context current. If the manager itself is already gone the handle is silently abandoned — correct, because that means the context died and took its objects with it.

**Binding side effects.** The methods bind on unit zero and restore the previous binding, but they do *not* restore the renderer's applied state: `BindTextureAndApply` reverts the bind and leaves the apply, per its own contract. They also set the active texture unit as a side effect. For a cube map, `gl_copy_tex_image_2D` binds `GL_TEXTURE_CUBE_MAP_ARB` while passing the per-face target to OpenGL — a distinction the other methods do not make, so passing a cube face target to `gl_tex_parameter*` binds the wrong thing.

**`is_format_floating_point` is a range test.** It works by comparing the internal format against `GL_RGBA32F_ARB`..`GL_LUMINANCE_ALPHA16F_ARB` and `GL_R16F`..`GL_RG32F` (plus two packed-float constants under `#ifdef GL_EXT_packed_float`), relying on those enum values being contiguous. It deliberately excludes floating-point *depth* formats, so a float depth texture reports `false` — which matters because `GLRenderer::supports_floating_point_render_target_2D` and its callers use this to decide whether a render target is viable.

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

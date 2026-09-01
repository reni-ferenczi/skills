# GLContext

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 478 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLContext.h` | C++ | 903 |
| `src/opengl/GLContext.cc` | C++ | 968 |

## Overview

`GLContext` is GPlates' mirror of a real OpenGL context and the central registry
for every long-lived low-level GL object built on it. It never touches Qt
directly: the `Impl` interface delegates "make current", the format and the
framebuffer dimensions to whatever the context really is, and
`GLContextImpl::QGLWidgetImpl` and `QGLPixelBufferImpl` are the two
implementations in the tree. `GlobeCanvas` and `MapView` each construct one
around their widget, `GLOffScreenContext` wraps one for rendering without a
window, and `create_renderer` is where each frame's `GLRenderer` comes from.

The design turns on splitting that registry in two along the line OpenGL itself
draws. `SharedState` holds what a driver lets contexts share — texture, buffer,
shader and program object resource managers, and the `GPlatesUtils::ObjectCache`
pools behind `acquire_texture`, `acquire_pixel_buffer`, `acquire_vertex_array`,
`acquire_render_buffer_object` and `acquire_render_target` — while
`NonSharedState` holds what they cannot: framebuffer objects, screen render
targets, and the resource manager for native vertex array objects. The two-arg
`create` overload hands the new context the existing one's `SharedState`, which
is how `GlobeCanvas` mirrors Qt's own `isSharing()` result into this layer; two
`GLContext`s are sharing exactly when their `get_shared_state()` pointers
compare equal. `GLVertexArrayObject` is the instructive exception, and the
comments explain it: the *wrapper* is cacheable in `SharedState` because it
creates a native VAO per context it meets, but its resource manager sits in
`NonSharedState` so each native name is released while the context that created
it is active.

Everything about resource lifetime here is deferred rather than immediate.
Objects handed out by the `acquire_*` methods come back as `shared_ptr`s with a
custom deleter that returns them to their cache instead of destroying them, and
each cache is keyed by the exact creation parameters so a recycled object always
matches what the next caller asked for. Destruction of the underlying GL names is
deferred too: resources are queued by `GLObjectResource` and only actually
deleted when `begin_render` and `end_render` — called by `GLRenderer` around a
frame — drain all four resource managers, which is the one place the correct
context is known to be current. `GLContext` is also where GLEW is initialised,
where `disable_opengl_extensions` then clears the GLEW flags GPlates does not
want, and only afterwards where `GLCapabilities` is populated — so what the rest
of the program can see has already been filtered by the time anyone asks.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLContext`](#gplatesopenglglcontext) | class | [`GPlatesUtils::ReferenceCount<GLContext>`](../utils/ReferenceCount.md) | — | 0 | Mirrors an OpenGL context and provides a central place to manage low-level OpenGL objects. |

## Members

### `GPlatesOpenGL::GLContext`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLContext>` | public | A convenience typedef for a shared pointer to a non-const GLContext. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLContext>` | public | A convenience typedef for a shared pointer to a const GLContext. |
| `Impl` | class | `None` | public | Used to delegate to the real OpenGL context. |
| `SharedState` | class | `None` | public | OpenGL state that can be shared between contexts (such as texture objects, vertex buffer objects, etc). |
| `NonSharedState` | class | `None` | public | OpenGL state that \*cannot\* be shared between contexts (such as vertex array objects, framebuffer objects). |
| `get_qgl_format_to_create_context_with()` | method | `QGLFormat` | public | Returns the QGLFormat to use when creating a Qt OpenGL context (eg, QGLWidget). |
| `create( const boost::shared_ptr<Impl> &context_impl)` | method | `non_null_ptr_type` | public | Creates a GLContext object. |
| `create( const boost::shared_ptr<Impl> &context_impl, GLContext &shared_context)` | method | `non_null_ptr_type` | public | Creates a GLContext object that shares state with another context. |
| `initialise()` | method | `void` | public | Initialises this GLContext. |
| `make_current()` | method | `void` | public | Sets this context as the active OpenGL context. |
| `get_width()` | method | `unsigned int` | public | The width (in device pixels) of the frame buffer currently attached to the OpenGL context. |
| `get_height()` | method | `unsigned int` | public | The height (in device pixels) of the frame buffer currently attached to the OpenGL context. |
| `create_renderer()` | method | `GPlatesGlobal::PointerTraits<GLRenderer>::non_null_ptr_type` | public | Creates a renderer. |
| `get_shared_state()` | method | `boost::shared_ptr<const SharedState>` | public | Returns the OpenGL state that can be shared with other OpenGL contexts. |
| `get_non_shared_state()` | method | `boost::shared_ptr<const NonSharedState>` | public | Returns the OpenGL state that \*cannot\* be shared with other OpenGL contexts. |
| `get_capabilities` | field | `GLCapabilities` | public | Function to return OpenGL implementation-dependent capabilities and parameters. |
| `begin_render()` | method | `void` | public | Call this before rendering a scene. |
| `end_render()` | method | `void` | public | Call this after rendering a scene. |
| `d_context_impl` | field | `boost::shared_ptr<Impl>` | private | For delegating to the real OpenGL context. |
| `d_qgl_format` | field | `QGLFormat` | private | The format of the OpenGL context. |
| `d_shared_state` | field | `boost::shared_ptr<SharedState>` | private | OpenGL state that can be shared with another context. |
| `d_non_shared_state` | field | `boost::shared_ptr<NonSharedState>` | private | OpenGL state that \*cannot\* be shared with another context. |
| `s_initialised_GLEW` | field | `bool` | private | Is true if the GLEW library has been initialised (if initialise has been called). |
| `s_capabilities` | field | `GLCapabilities` | private | OpenGL implementation-dependent capabilities and parameters. |
| `GLContext( const boost::shared_ptr<Impl> &context_impl)` | constructor | `None` | private | Constructor. |
| `GLContext( const boost::shared_ptr<Impl> &context_impl, const boost::shared_ptr<SharedState> &shared_state)` | constructor | `None` | private | Constructor. |
| `deallocate_queued_object_resources()` | method | `void` | private | Deallocates OpenGL objects that has been released but not yet destroyed/deallocated. |
| `disable_opengl_extensions()` | method | `void` | private | Disable specific OpenGL extensions. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `s_initialised_GLEW` | variable | `bool` | — |
| `s_capabilities` | variable | `GPlatesOpenGL::GLCapabilities` | — |
| `GPLATES_OPENGL_GLCONTEXT_H` | macro | `None` | — |

## Notes

`initialise` must be called with a context current, and despite being an
instance method it does its important work only once per *application*: the GLEW
flag and the `GLCapabilities` it fills are both static. The comment gives the
reason — per-context GLEW state needs a `GLEW_MX` build that is not packaged
everywhere — and the consequence is that capabilities are process-wide, so
contexts with genuinely different capabilities are not something this design
supports. If `glewInit` fails, initialisation continues anyway on the assumption
that every extension flag reads false and the code falls back to OpenGL 1.1.

The format returned by `get_qgl_format_to_create_context_with` is load-bearing
and its choices are all deliberate: a stencil buffer (needed to fill polygons),
an alpha channel (needed when render targets fall back to the main framebuffer),
multisampling explicitly *off* because lines look better without it, the
compatibility profile with deprecated functions enabled, and the version pinned
to 1.1 — GPlates works through extensions rather than a core version, 1.1 is all
the Microsoft software renderer offers, and asking for 3.x can make
`GL_EXT_framebuffer_object` stop being advertised. `initialise` warns when the
alpha or stencil request was not honoured. Note also that `d_qgl_format` is
captured once at construction, while `get_width`/`get_height` delegate live to
the `Impl` and are in device pixels, not the device-independent pixels Qt uses
for widget sizes.

Nothing about sharing is verified here. `GLContext` shares a `SharedState`
because the caller asked it to; it is the caller's job (as `GlobeCanvas` does
via `isSharing()`) to ensure the underlying Qt contexts really do share, and
nothing detects a mismatch.

Objects borrowed from the `acquire_*` caches must be returned unchanged. The
methods hand back non-const pointers, so their dimensions or format *can* be
altered, and the guard against it is only an assertion in the next borrower —
which surfaces as an `OpenGLException` from a completely unrelated part of the
frame. `acquire_vertex_array` and `acquire_frame_buffer_object` reset the state
they can (`clear()`, `gl_detach_all()` plus default draw/read buffers) precisely
because the previous borrower's settings are unknowable.

None of this is synchronised — the caches, the maps and the static
initialisation flags carry no locking — so every use has to stay on the thread
that makes the context current. Finally, `check_framebuffer_object_completeness`
memoises `glCheckFramebufferStatus` per framebuffer classification because a
single check was once profiled at 142 ms; if you change what a classification
means, that cache has to change with it.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRenderer](GLRenderer.md) | opengl | 76 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 63 |
| [opengl/GLOffScreenContext](GLOffScreenContext.md) | opengl | 29 |
| [opengl/GLProgramObject](GLProgramObject.md) | opengl | 28 |
| [opengl/GLFrameBufferObject](GLFrameBufferObject.md) | opengl | 22 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 21 |
| [opengl/GLLight](GLLight.md) | opengl | 15 |
| [opengl/GLNormalMapSource](GLNormalMapSource.md) | opengl | 15 |
| [opengl/GLBufferObject](GLBufferObject.md) | opengl | 11 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 11 |
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 10 |
| [opengl/GLSaveRestoreFrameBuffer](GLSaveRestoreFrameBuffer.md) | opengl | 10 |
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 10 |
| [opengl/GLDataRasterSource](GLDataRasterSource.md) | opengl | 9 |
| [gui/Globe](../gui/Globe.md) | gui | 8 |
| [opengl/GLRenderTargetImpl](GLRenderTargetImpl.md) | opengl | 8 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 7 |
| [opengl/GLVisualLayers](GLVisualLayers.md) | opengl | 7 |
| [opengl/GLAgeGridMaskSource](GLAgeGridMaskSource.md) | opengl | 6 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 6 |

*... and 47 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLContext.h
python scripts/gpq.py def GPlatesOpenGL::GLContext --body
python scripts/gpq.py uses GLContext --kind class
python scripts/gpq.py hier GLContext
```

# GLContext

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 478 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLContext.h` | C++ | 903 |
| `src/opengl/GLContext.cc` | C++ | 968 |

## Overview

[[[PROSE overview unit=opengl/GLContext tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=opengl/GLContext tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

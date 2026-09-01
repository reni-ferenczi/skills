# GLCompiledDrawState

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 3 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLCompiledDrawState.h` | C++ | 105 |
| `src/opengl/GLCompiledDrawState.cc` | C++ | 44 |

## Overview

`GLCompiledDrawState` is an opaque, reference-counted bundle of an OpenGL state change and an optional sequence of draw calls, produced by `GLRenderer` when it compiles a block of rendering commands. It plays the same role as an OpenGL display list, but is implemented so it can be replayed across different OpenGL contexts — a constraint that matters because `GLVertexArrayObject` cannot normally share native vertex array objects across contexts.

The class exposes almost nothing to general client code: `get_state` is documented as being for the render framework's own use, and construction is private, reachable only by `GLRenderer` and `GLRendererImpl::StateBlock`. Callers elsewhere in the codebase (for example `GLAgeGridMaskSource`) simply hold a compiled draw state's `non_null_ptr_type` and hand it back to `GLRenderer` to replay, without inspecting its contents.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLCompiledDrawState`](#gplatesopenglglcompileddrawstate) | class | [`GPlatesUtils::ReferenceCount<GLCompiledDrawState>`](../utils/ReferenceCount.md) | — | 0 | A compiled draw state contains a set of state changes and optionally a sequence of draw calls. |

## Members

### `GPlatesOpenGL::GLCompiledDrawState`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLCompiledDrawState>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLCompiledDrawState>` | public | — |
| `~GLCompiledDrawState()` | destructor | `None` | public | — |
| `get_state()` | method | `boost::shared_ptr<const GLState>` | public | Returns the 'const' state compiled into this draw state. |
| `d_state_change` | field | `boost::shared_ptr<GLState>` | private | The net state change across the scope of the compiled draw state. |
| `d_render_queue` | field | `GPlatesGlobal::PointerTraits<GLRendererImpl::RenderQueue>::non_null_ptr_type` | private | Optional sequence of draw calls - depends whether any were compiled into draw state. |
| `GLCompiledDrawState( const boost::shared_ptr<GLState> &state_change, const GPlatesGlobal::PointerTraits<GLRendererImpl::RenderQueue>::non_null_ptr_type &render_queue)` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLCOMPILEDDRAWSTATE_H` | macro | `None` | — |

## Notes

- The state returned by `get_state` is not immutable in the usual sense of "const": it reflects the compiled state at the time of the call and can change later if more state is compiled into the same `GLCompiledDrawState`.
- Construction is private; only `GLRenderer` and `GLRendererImpl::StateBlock` can create instances, so this type should be treated as an opaque handle rather than something to build directly.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRenderer](GLRenderer.md) | opengl | 139 |
| [opengl/GLRendererImpl](GLRendererImpl.md) | opengl | 20 |
| [gui/SphericalGrid](../gui/SphericalGrid.md) | gui | 9 |
| [opengl/GLContext](GLContext.md) | opengl | 9 |
| [gui/OpaqueSphere](../gui/OpaqueSphere.md) | gui | 8 |
| [opengl/GLUtils](GLUtils.md) | opengl | 7 |
| [opengl/GLVertexArrayObject](GLVertexArrayObject.md) | opengl | 7 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 6 |
| [opengl/GLReconstructedStaticPolygonMeshes](GLReconstructedStaticPolygonMeshes.md) | opengl | 6 |
| [app-logic/ReconstructLayerProxy](../app-logic/ReconstructLayerProxy.md) | app-logic | 5 |
| [gui/Stars](../gui/Stars.md) | gui | 5 |
| [opengl/GLAgeGridMaskSource](GLAgeGridMaskSource.md) | opengl | 5 |
| [opengl/GLVertexArray](GLVertexArray.md) | opengl | 5 |
| [gui/MapBackground](../gui/MapBackground.md) | gui | 4 |
| [gui/MapGrid](../gui/MapGrid.md) | gui | 4 |
| [opengl/GLSaveRestoreFrameBuffer](GLSaveRestoreFrameBuffer.md) | opengl | 3 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 3 |
| [opengl/GLVertexArrayImpl](GLVertexArrayImpl.md) | opengl | 3 |
| [gui/FeedbackOpenGLToQPainter](../gui/FeedbackOpenGLToQPainter.md) | gui | 2 |
| [gui/Globe](../gui/Globe.md) | gui | 2 |

*... and 7 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLCompiledDrawState.h
python scripts/gpq.py def GPlatesOpenGL::GLCompiledDrawState --body
python scripts/gpq.py uses GLCompiledDrawState --kind class
python scripts/gpq.py hier GLCompiledDrawState
```

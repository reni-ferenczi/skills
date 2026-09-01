# GLCompiledDrawState

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 3 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLCompiledDrawState.h` | C++ | 105 |
| `src/opengl/GLCompiledDrawState.cc` | C++ | 44 |

## Overview

[[[PROSE overview unit=opengl/GLCompiledDrawState tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=opengl/GLCompiledDrawState tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

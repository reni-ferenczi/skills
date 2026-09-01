# OpenGLException

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 17 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/OpenGLException.h` | C++ | 76 |

## Overview

`OpenGLException` is the module's catch-all exception type: a thin
`GPlatesGlobal::Exception` specialisation that carries a free-text message
(`_msg`) describing the failing condition, with no structured error code or
category. It is the exception the rest of `opengl` throws for OpenGL-specific
failures — missing extensions, unexpected driver state, resource-creation
failures — that do not warrant a more specific exception type of their own.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::OpenGLException`](#gplatesopenglopenglexception) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | A general openGL-error exception. |

## Members

### `GPlatesOpenGL::OpenGLException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `OpenGLException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | in which the problem occurs. |
| `~OpenGLException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_OPENGL_OPENGLEXCEPTION_H_` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRenderTargetImpl](GLRenderTargetImpl.md) | opengl | 6 |
| [opengl/GLContext](GLContext.md) | opengl | 4 |
| [opengl/GLRenderer](GLRenderer.md) | opengl | 3 |
| [opengl/GLSaveRestoreFrameBuffer](GLSaveRestoreFrameBuffer.md) | opengl | 3 |
| [gui/FeedbackOpenGLToQPainter](../gui/FeedbackOpenGLToQPainter.md) | gui | 2 |
| [gui/VelocityLegendOverlay](../gui/VelocityLegendOverlay.md) | gui | 2 |
| [opengl/GLProgramObject](GLProgramObject.md) | opengl | 2 |
| [opengl/GLShaderObject](GLShaderObject.md) | opengl | 2 |
| [opengl/GLText](GLText.md) | opengl | 2 |
| [file-io/RasterReader](../file-io/RasterReader.md) | file-io | 1 |
| [file-io/RasterWriter](../file-io/RasterWriter.md) | file-io | 1 |
| [opengl/GLBufferObject](GLBufferObject.md) | opengl | 1 |
| [opengl/GLStateSets](GLStateSets.md) | opengl | 1 |
| [opengl/GLUtils](GLUtils.md) | opengl | 1 |
| [opengl/GLVertexArrayObject](GLVertexArrayObject.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/OpenGLException.h
python scripts/gpq.py def GPlatesOpenGL::OpenGLException --body
python scripts/gpq.py uses OpenGLException --kind class
python scripts/gpq.py hier OpenGLException
```

# OpenGLException

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 17 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/OpenGLException.h` | C++ | 76 |

## Overview

[[[PROSE overview unit=opengl/OpenGLException tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=opengl/OpenGLException tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

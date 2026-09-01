# OpenGLBadAllocException

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1540 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/OpenGLBadAllocException.h` | C++ | 78 |

## Overview

[[[PROSE overview unit=opengl/OpenGLBadAllocException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::OpenGLBadAllocException`](#gplatesopenglopenglbadallocexception) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | The Exception thrown by the OpenGL wrappers when OpenGL is unable to allocate memory for an object. |

## Members

### `GPlatesOpenGL::OpenGLBadAllocException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `OpenGLBadAllocException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | in which the problem occurs. |
| `~OpenGLBadAllocException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_OPENGL_OPENGLBADALLOCEXCEPTION_H_` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/OpenGLBadAllocException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/RasterReader](../file-io/RasterReader.md) | file-io | 1 |
| [file-io/RasterWriter](../file-io/RasterWriter.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/OpenGLBadAllocException.h
python scripts/gpq.py def GPlatesOpenGL::OpenGLBadAllocException --body
python scripts/gpq.py uses OpenGLBadAllocException --kind class
python scripts/gpq.py hier OpenGLBadAllocException
```

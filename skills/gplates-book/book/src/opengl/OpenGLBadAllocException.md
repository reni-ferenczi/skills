# OpenGLBadAllocException

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1540 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/OpenGLBadAllocException.h` | C++ | 78 |

## Overview

`OpenGLBadAllocException` is thrown by the OpenGL rendering backend when GPU memory allocation fails. It carries a description of the failed allocation context and is caught by code that needs to handle graphics memory exhaustion — particularly raster I/O and rendering operations that may attempt large allocations.

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

*None.*

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

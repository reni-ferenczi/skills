# OpenGL

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 3 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/OpenGL.h` | C++ | 95 |

## Overview

`OpenGL.h` is the module's platform-portability shim: it pulls in the correct
platform GL headers (`<OpenGL/gl.h>`/`<OpenGL/glu.h>` on macOS,
`<windows.h>` then `<GL/gl.h>`/`<GL/glu.h>` on Windows — carefully guarding
`NOMINMAX` so `windows.h` does not clobber `std::numeric_limits::max()` — and
plain `<GL/gl.h>`/`<GL/glu.h>` elsewhere) behind one `extern "C"` block, and
defines `__CONVENTION__` to the platform calling convention. Deliberately
*not* included here is GLEW: the comment explains that GLEW must precede any
other OpenGL header, but since other modules transitively include this header
alongside Qt headers (which themselves drag in `<GL/gl.h>`), getting a
consistent include order project-wide would be impractical — so GLEW is
included only from `opengl` module `.cc` files, keeping it out of the public
interface entirely.

The two macros, `GPLATES_OPENGL_BOOL` and `GPLATES_OPENGL_BUFFER_OFFSET`, are
small conveniences used throughout the module: the former normalises a
`GLboolean` (typically an `unsigned char`) to a real boolean test, the latter
turns a byte offset into the `void *` that buffer-object drawing calls
expect.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_OPENGL_H` | macro | `None` | — |
| `__CONVENTION__` | macro | `None` | Assume compilation on Mac OS X. \*/ |
| `GPLATES_OPENGL_BOOL` | macro_function | `((b) != 0)` | — |
| `GPLATES_OPENGL_BUFFER_OFFSET` | macro_function | `(reinterpret_cast<GLubyte *>(0) + (bytes))` | — |

## Notes

Never include `<GL/glew.h>` before this header in a shared/`.h` context;
GLEW must only be included in `opengl` module `.cc` files, and always before
any other OpenGL header in that file.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLCapabilities](GLCapabilities.md) | opengl | 19 |
| [opengl/GLPixelBufferObject](GLPixelBufferObject.md) | opengl | 7 |
| [opengl/GLRenderer](GLRenderer.md) | opengl | 5 |
| [opengl/GLStateSets](GLStateSets.md) | opengl | 3 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 2 |
| [opengl/GLBufferObject](GLBufferObject.md) | opengl | 2 |
| [opengl/GLContext](GLContext.md) | opengl | 2 |
| [opengl/GLCubeSubdivision](GLCubeSubdivision.md) | opengl | 2 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 2 |
| [opengl/GLFilledPolygonsMapView](GLFilledPolygonsMapView.md) | opengl | 2 |
| [opengl/GLFrameBufferObject](GLFrameBufferObject.md) | opengl | 2 |
| [opengl/GLPixelBufferImpl](GLPixelBufferImpl.md) | opengl | 2 |
| [opengl/GLProgramObject](GLProgramObject.md) | opengl | 2 |
| [opengl/GLProjectionUtils](GLProjectionUtils.md) | opengl | 2 |
| [opengl/GLRenderTargetImpl](GLRenderTargetImpl.md) | opengl | 2 |
| [opengl/GLSaveRestoreFrameBuffer](GLSaveRestoreFrameBuffer.md) | opengl | 2 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 2 |
| [opengl/GLShaderObject](GLShaderObject.md) | opengl | 2 |
| [opengl/GLState](GLState.md) | opengl | 2 |
| [opengl/GLStateSetKeys](GLStateSetKeys.md) | opengl | 2 |

*... and 63 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/OpenGL.h
```

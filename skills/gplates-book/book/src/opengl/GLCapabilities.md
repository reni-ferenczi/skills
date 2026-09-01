# GLCapabilities

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 508 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLCapabilities.h` | C++ | 429 |
| `src/opengl/GLCapabilities.cc` | C++ | 644 |

## Overview

`GLCapabilities` is the single snapshot of what the OpenGL implementation
underneath GPlates can actually do — which extensions are present, and the
implementation-dependent limits that go with them — grouped into nested structs
by subsystem. It exists so that no other part of the backend has to touch a
`GLEW_*` macro or issue a `glGetIntegerv` of its own. Almost every branch in
`src/opengl` that chooses between a modern path and a fallback reads a field
here: `GLBuffer::create` picking `GLBufferObject` over `GLBufferImpl`,
`GLStateSets` deciding how much fixed-function state exists to shadow,
`GLScalarField3D` deciding whether it can run at all.

Construction and initialisation are private, with `GLContext` as the only
friend, and the instance itself is a static member of `GLContext` populated by
`GLContext::initialise` immediately after `glewInit()` succeeds. Clients reach it
through `GLContext::get_capabilities` or the `GLRenderer::get_capabilities`
that forwards to it, which is the point of the arrangement: the header comment
records that this used to be globally accessible and was deliberately tied to a
`GLContext` so that no one can read capabilities before GLEW has run. The
`initialise_*` methods each issue real GL queries, so a context must be current
when they run.

Two details of the design are worth knowing before editing it. First, the
per-struct constructors do not zero the limits — they set them to what plain
OpenGL guarantees without the extension (one texture unit, one draw buffer, one
viewport, one texture-array layer, 1.0 anisotropy, a 64-texel texture), so
callers may read a limit without first testing its flag. Second, a few fields
are inferred rather than queried, because no query exists:
`gl_supports_floating_point_filtering_and_blending` is deduced from OpenGL 3.0
or `GL_EXT_texture_array`, `gl_is_texture3D_supported` tests core OpenGL 1.2
rather than the EXT extensions because MacOS does not expose them, and
`gl_ARB_gpu_shader_fp64` is detected by probing for non-null `glUniform*d`
entry points — and then written *back* into GLEW's own
`__GLEW_ARB_gpu_shader_fp64` flag so the rest of the program agrees. The two
static `GLenum` constants exist purely as header hygiene: `<GL/glew.h>` has to
precede every OpenGL and Qt header, so it is confined to `.cc` files, and these
smuggle `GL_COLOR_ATTACHMENT0` and `GL_TEXTURE0` out to headers that need them.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLCapabilities`](#gplatesopenglglcapabilities) | class | `boost::noncopyable` | — | 0 | Various OpenGL implementation-dependent capabilities and parameters. |

## Members

### `GPlatesOpenGL::GLCapabilities`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Viewport` | struct | `None` | public | Parameters related to viewports. |
| `Framebuffer` | struct | `None` | public | Parameters related to the framebuffers. |
| `Shader` | struct | `None` | public | — |
| `Texture` | struct | `None` | public | Parameters related to textures. |
| `Vertex` | struct | `None` | public | Parameters related to geometry data. |
| `Buffer` | struct | `None` | public | Parameters related to buffer objects. |
| `gl_version_1_2` | field | `bool` | public | Is OpenGL version 1.2 supported ? |
| `gl_version_1_4` | field | `bool` | public | Is OpenGL version 1.4 supported ? |
| `viewport` | field | `Viewport` | public | OpenGL extension queries. |
| `framebuffer` | field | `Framebuffer` | public | — |
| `shader` | field | `Shader` | public | — |
| `texture` | field | `Texture` | public | — |
| `vertex` | field | `Vertex` | public | — |
| `buffer` | field | `Buffer` | public | — |
| `GLCapabilities()` | constructor | `None` | private | — |
| `initialise()` | method | `void` | private | — |
| `initialise_viewport()` | method | `void` | private | — |
| `initialise_framebuffer()` | method | `void` | private | — |
| `initialise_shader()` | method | `void` | private | — |
| `initialise_texture()` | method | `void` | private | — |
| `initialise_vertex()` | method | `void` | private | — |
| `initialise_buffer()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `gl_COLOR_ATTACHMENT0` | variable | `GLenum` | Set the GL\_COLOR\_ATTACHMENT0\_EXT constant. |
| `gl_TEXTURE0` | variable | `GLenum` | Set the GL\_TEXTURE0 constant. |
| `GPLATES_OPENGL_GLCAPABILITIES_H` | macro | `None` | — |

## Notes

There is exactly one instance in the process. `GLContext` holds it as a *static*
member alongside a static "GLEW initialised" flag, and `GLContext::initialise`
populates it only the first time it is called for the whole application — the
comment there explains why: GLEW would have to be built with `GLEW_MX` to
support per-context state, and that build is not available everywhere. So
capabilities are process-wide even when several contexts exist, and the code
assumes those contexts are equivalent. `get_capabilities` asserts the GLEW flag,
so reading capabilities before `GLContext::initialise` raises a
`PreconditionViolationError` rather than returning stale zeroes.

The `noncopyable` base is a deliberate barrier, not an accident: the comment on
it says clients must not copy and cache capabilities but retrieve them from a
`GLContext`. The fields themselves are public and non-const, so nothing stops a
client writing to them — only the private constructor and the `GLContext`
friendship keep that from being routine.

Extensions can legitimately read as unsupported for reasons other than the
hardware. `GLContext::disable_opengl_extensions` runs immediately *before*
`initialise` and clears GLEW flags: `GL_ARB_vertex_array_object` is switched off
permanently because vertex array objects measured slower than re-specifying the
attribute arrays, and a commented-out block beside it is the intended way to
force any other fallback path for testing. Separately, several blocks are
wrapped in `#ifdef` guards against an old build-time `glew.h`, so a capability
can be false simply because the header GPlates was compiled against did not
declare that extension.

When adding a field, add its default to the corresponding struct's constructor
as well. That default is what every driver lacking the extension will report,
and the convention throughout is a value the caller can use unconditionally —
not zero.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLStateSets](GLStateSets.md) | opengl | 252 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 87 |
| [opengl/GLState](GLState.md) | opengl | 79 |
| [opengl/GLRenderer](GLRenderer.md) | opengl | 70 |
| [opengl/GLContext](GLContext.md) | opengl | 66 |
| [opengl/GLProgramObject](GLProgramObject.md) | opengl | 64 |
| [opengl/GLStateSetKeys](GLStateSetKeys.md) | opengl | 55 |
| [opengl/GLFrameBufferObject](GLFrameBufferObject.md) | opengl | 49 |
| [opengl/GLBufferObject](GLBufferObject.md) | opengl | 41 |
| [opengl/GLDataRasterSource](GLDataRasterSource.md) | opengl | 35 |
| [opengl/GLNormalMapSource](GLNormalMapSource.md) | opengl | 34 |
| [opengl/GLRenderTargetImpl](GLRenderTargetImpl.md) | opengl | 33 |
| [opengl/GLMultiResolutionCubeRaster](GLMultiResolutionCubeRaster.md) | opengl | 26 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 21 |
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 21 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 19 |
| [opengl/GLTextureUtils](GLTextureUtils.md) | opengl | 18 |
| [app-logic/ResolvedTriangulationDelaunay2](../app-logic/ResolvedTriangulationDelaunay2.md) | app-logic | 17 |
| [opengl/GLVisualRasterSource](GLVisualRasterSource.md) | opengl | 17 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](GLMultiResolutionCubeReconstructedRaster.md) | opengl | 16 |

*... and 48 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLCapabilities.h
python scripts/gpq.py def GPlatesOpenGL::GLCapabilities --body
python scripts/gpq.py uses GLCapabilities --kind class
python scripts/gpq.py hier GLCapabilities
```

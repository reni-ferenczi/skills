# GLShaderSource

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 875 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLShaderSource.h` | C++ | 206 |
| `src/opengl/GLShaderSource.cc` | C++ | 227 |

## Overview

`GLShaderSource` assembles the concatenated source string that `GLShaderObject::gl_shader_source()` compiles, from one or more code segments added via `add_code_segment()`/`add_code_segment_from_file()`, while remembering which segment came from which file (or an inline string) so a compile error's line number can later be traced back to it. It also owns the `#version` directive: rather than requiring callers to put `"#version 120"` at the top of whichever segment happens to be concatenated first — awkward when the segment defining `main()` (which typically needs the directive) is added last because it depends on the others — `GLShaderSource` generates its own leading segment from a `ShaderVersion` enum value and prepends it. `get_code_segments()` also hoists any `#extension` directive found in a later segment up into that same initial segment (commenting it out in place), since `#extension` is likewise required to precede ordinary source code.

`create_shader_source_from_file()` is a convenience for the common single-file case; `GLSL_1_2` is `DEFAULT_SHADER_VERSION` since it maps to OpenGL 2.1, which nearly all hardware supporting the OpenGL 2.0 baseline (`GLSL_1_1`) also supports.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLShaderSource`](#gplatesopenglglshadersource) | class | — | — | 0 | A convenience class to handle shader source code segments and whether the individual code segments come from a string or a file (useful for logging failed compiles/links). |

## Members

### `GPlatesOpenGL::GLShaderSource`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ShaderVersion` | enum | `None` | public | GLSL shader versions. |
| `DEFAULT_SHADER_VERSION` | field | `ShaderVersion` | public | The default shader version to compile. |
| `GLSL_1_2` | field | `ShaderVersion` | public | The default shader version to compile. |
| `CodeSegment` | struct | `None` | public | Represents information of a shader code segment. |
| `create_shader_source_from_file( const QString& shader_source_file_name, ShaderVersion shader_version = DEFAULT_SHADER_VERSION)` | method | `GLShaderSource` | public | Creates a GLShaderSource object when only a single shader source, from a file, is required. |
| `GLShaderSource( ShaderVersion shader_version = DEFAULT_SHADER_VERSION)` | constructor | `None` | public | Default constructor contains no shader source. |
| `GLShaderSource( const char *shader_source, ShaderVersion shader_version = DEFAULT_SHADER_VERSION)` | constructor | `None` | public | Implicit converting constructor when only a single shader source is required. |
| `GLShaderSource( const QByteArray &shader_source, ShaderVersion shader_version = DEFAULT_SHADER_VERSION)` | constructor | `None` | public | Implicit converting constructor when only a single shader source is required. |
| `add_code_segment( const char *shader_source)` | method | `void` | public | Adds a shader source code segment. |
| `add_code_segment( const QByteArray &shader_source)` | method | `void` | public | Adds a shader source code segment. |
| `add_code_segment_from_file( const QString& shader_source_file_name)` | method | `void` | public | Adds a shader source code segment from a file. |
| `get_code_segments()` | method | `std::vector<CodeSegment>` | public | Returns all shader source code segments. |
| `get_shader_version()` | method | `ShaderVersion` | public | Returns the shader version. |
| `SHADER_VERSION_STRINGS` | field | `char` | private | Shader source version strings. |
| `d_shader_version` | field | `ShaderVersion` | private | — |
| `d_initial_code_segment` | field | `CodeSegment` | private | Code segment containing #version and any #extension found in code segments added by client. |
| `d_added_code_segments` | field | `std::vector<CodeSegment>` | private | Code segments added by client. |
| `add_processed_code_segment( QByteArray source_code, boost::optional<QString> source_file_name = boost::none)` | method | `void` | private | Do any processing of the code segment and then add it to our internal sequence. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `SHADER_VERSION_STRINGS` | variable | `char` | — |
| `GPLATES_OPENGL_GLSHADERSOURCE_H` | macro | `None` | — |

## Notes

- Callers must not put a `#version` (or `#extension`) directive of their own in an added code segment — `GLShaderSource` synthesises and manages that segment itself, and moves any `#extension` it finds up front automatically.
- The `const char *` constructor and `add_code_segment(const char *)` copy the source internally, so the caller's buffer need not outlive the call.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 40 |
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 31 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 29 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 25 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 25 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 19 |
| [opengl/GLShaderProgramUtils](GLShaderProgramUtils.md) | opengl | 19 |
| [opengl/GLMultiResolutionRasterMapView](GLMultiResolutionRasterMapView.md) | opengl | 14 |
| [opengl/GLShaderObject](GLShaderObject.md) | opengl | 12 |
| [opengl/GLLight](GLLight.md) | opengl | 9 |
| [opengl/GLNormalMapSource](GLNormalMapSource.md) | opengl | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLShaderSource.h
python scripts/gpq.py def GPlatesOpenGL::GLShaderSource --body
python scripts/gpq.py uses GLShaderSource --kind class
python scripts/gpq.py hier GLShaderSource
```

# GLShaderSource

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 875 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLShaderSource.h` | C++ | 206 |
| `src/opengl/GLShaderSource.cc` | C++ | 227 |

## Overview

[[[PROSE overview unit=opengl/GLShaderSource tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=opengl/GLShaderSource tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

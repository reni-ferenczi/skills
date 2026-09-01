# GLShaderProgramUtils

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 422 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLShaderProgramUtils.h` | C++ | 203 |
| `src/opengl/GLShaderProgramUtils.cc` | C++ | 310 |

## Overview

`GLShaderProgramUtils` is a free-function namespace that spares every other rendering unit from repeating the compile-shader/link-program boilerplate around `GLShaderObject` and `GLProgramObject`. The `compile_*_shader` functions wrap a single stage (vertex, fragment or geometry) in `boost::optional`, returning `boost::none` uniformly whether the stage is unsupported on the runtime system or its source failed to compile; the `link_*_program` functions link already-compiled shaders into a program, and the `compile_and_link_*_program` functions combine both steps for the common one-shot case. This is the layer nearly every `GL*` rendering class in this module goes through to build its shader programs, rather than calling `GLShaderObject`/`GLProgramObject` directly.

Linking a geometry shader additionally needs a `GeometryShaderProgramParameters` — the maximum vertices the shader emits (`GL_GEOMETRY_VERTICES_OUT`) plus its input/output primitive types — because some platforms (Mac OS X) require these set on the program *before* linking, not just declared in the GLSL source.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLShaderProgramUtils::GeometryShaderProgramParameters`](#gplatesopenglglshaderprogramutilsgeometryshaderprogramparameters) | struct | — | — | 0 | Shader program parameters required to be set before a geometry shader can be linked. |

## Members

### `GPlatesOpenGL::GLShaderProgramUtils::GeometryShaderProgramParameters`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GeometryShaderProgramParameters( GLint gl_max_vertices_out_, GLint gl_geometry_input_type_ = GL_TRIANGLES, GLint gl_geometry_output_type_ = GL_TRIANGLE_STRIP)` | constructor | `None` | public | — |
| `gl_max_vertices_out` | field | `GLint` | public | — |
| `gl_geometry_input_type` | field | `GLint` | public | — |
| `gl_geometry_output_type` | field | `GLint` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLSHADERPROGRAMUTILS_H` | macro | `None` | — |
| `UTILS_SHADER_SOURCE_FILE_NAME` | variable | `QString` | The filename of the shader source file (Qt resource) containing shader utilities. |
| `compile_fragment_shader( GLRenderer &renderer, const GLShaderSource &fragment_shader_source)` | function | `boost::optional<GLShaderObject::shared_ptr_type>` | Compiles the specified fragment shader source into a shader object. |
| `compile_vertex_shader( GLRenderer &renderer, const GLShaderSource &vertex_shader_source)` | function | `boost::optional<GLShaderObject::shared_ptr_type>` | Compiles the specified vertex shader source into a shader object. |
| `compile_geometry_shader( GLRenderer &renderer, const GLShaderSource &geometry_shader_source)` | function | `boost::optional<GLShaderObject::shared_ptr_type>` | Compiles the specified geometry shader source into a shader object. |
| `link_fragment_program( GLRenderer &renderer, const GLShaderObject::shared_ptr_to_const_type &fragment_shader)` | function | `boost::optional<GLProgramObject::shared_ptr_type>` | Links the specified fragment shader into a program object. |
| `link_vertex_fragment_program( GLRenderer &renderer, const GLShaderObject::shared_ptr_to_const_type &vertex_shader, const GLShaderObject::shared_ptr_to_const_type &fragment_shader)` | function | `boost::optional<GLProgramObject::shared_ptr_type>` | Links the specified vertex/fragment shader into a program object. |
| `link_vertex_geometry_fragment_program( GLRenderer &renderer, const GLShaderObject::shared_ptr_to_const_type &vertex_shader, const GLShaderObject::shared_ptr_to_const_type &geometry_shader, const GLShaderObject::shared_ptr_to_const_type &fragment_shader, const GeometryShaderProgramParameters &geometry_shader_program_par ...` | function | `boost::optional<GLProgramObject::shared_ptr_type>` | Links the specified vertex/geometry/fragment shader into a program object. geometry\_shader\_program\_parameters are program parameters for the geometry shader that must be set to appropriate values on some platforms (MacOS) \*before\* linking. |
| `compile_and_link_fragment_program( GLRenderer &renderer, const GLShaderSource &fragment_shader_source)` | function | `boost::optional<GLProgramObject::shared_ptr_type>` | Compiles the specified fragment shader source and links into a program object. |
| `compile_and_link_vertex_fragment_program( GLRenderer &renderer, const GLShaderSource &vertex_shader_source, const GLShaderSource &fragment_shader_source)` | function | `boost::optional<GLProgramObject::shared_ptr_type>` | Compiles the specified vertex/fragment shader source and links into a program object. |
| `compile_and_link_vertex_geometry_fragment_program( GLRenderer &renderer, const GLShaderSource &vertex_shader_source, const GLShaderSource &geometry_shader_source, const GLShaderSource &fragment_shader_source, const GeometryShaderProgramParameters &geometry_shader_program_parameters)` | function | `boost::optional<GLProgramObject::shared_ptr_type>` | Compiles the specified vertex/geometry/fragment shader source and links into a program object. geometry\_shader\_program\_parameters are program parameters for the geometry shader that must be set to appropriate values on some platforms ... |

## Notes

- `boost::none` from any function here is ambiguous by design between "unsupported hardware" and "compile/link failure" — callers that need to distinguish the two must call the relevant `GLShaderObject`/`GLShaderSource::is_supported()` check themselves first.
- `geometry_shader_program_parameters` must match the geometry shader's declared input array size in its GLSL source; a mismatch is a linking constraint, not something these functions validate.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 42 |
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 31 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 21 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 19 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 19 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 15 |
| [opengl/GLMultiResolutionRasterMapView](GLMultiResolutionRasterMapView.md) | opengl | 9 |
| [opengl/GLLight](GLLight.md) | opengl | 5 |
| [opengl/GLNormalMapSource](GLNormalMapSource.md) | opengl | 3 |
| [opengl/GLScalarFieldDepthLayersSource](GLScalarFieldDepthLayersSource.md) | opengl | 1 |

## Related

**Shader programs compiled by this unit**

| Shader unit | Component |
|---|---|
| [shaders/opengl](../qt-resources/opengl.md) | shaders |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLShaderProgramUtils.h
python scripts/gpq.py def GPlatesOpenGL::GLShaderProgramUtils::GeometryShaderProgramParameters --body
python scripts/gpq.py uses GeometryShaderProgramParameters --kind struct
python scripts/gpq.py hier GeometryShaderProgramParameters
```

# GLShaderObject

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 325 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLShaderObject.h` | C++ | 268 |
| `src/opengl/GLShaderObject.cc` | C++ | 300 |

## Overview

`GLShaderObject` wraps a single OpenGL shader object — vertex, fragment or geometry (`GL_VERTEX_SHADER_ARB`, `GL_FRAGMENT_SHADER_ARB` or `GL_GEOMETRY_SHADER_EXT`) — mirroring `glShaderSource`/`glCompileShader` through `gl_shader_source()` and `gl_compile_shader()`. Source is supplied as a `GLShaderSource`, an ordered set of code segments that may come from files or inline strings; `GLShaderObject` keeps its own record of those segments (`SourceCodeSegment`, `FileCodeSegment`) purely so that a compile failure's line numbers, reported by OpenGL against the single concatenated source string, can be mapped back to the originating file and line for the warning it logs.

Multiple compiled `GLShaderObject`s are linked together into a `GLProgramObject`; `GLShaderProgramUtils` is the main caller that builds shader sources and creates these objects on a unit's behalf. Like other `opengl` resource wrapper classes, it stores its OpenGL name behind a `GLObjectResource`/`GLObjectResourceManager` pair so the underlying shader is deleted through the resource manager rather than directly.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLShaderObject`](#gplatesopenglglshaderobject) | class | [`GLObject`](GLObject.md)<br>`boost::enable_shared_from_this<GLShaderObject>` | — | 0 | A shader object. |

## Members

### `GPlatesOpenGL::GLShaderObject`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLShaderObject>` | public | A convenience typedef for a shared pointer to a GLShaderObject. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLShaderObject>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<GLShaderObject>` | public | A convenience typedef for a weak pointer to a GLShaderObject. |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const GLShaderObject>` | public | — |
| `resource_handle_type` | typedef | `GLuint` | public | Typedef for a resource handle. |
| `Allocator` | class | `None` | public | Policy class to allocate and deallocate OpenGL shader objects. |
| `allocator_type` | typedef | `Allocator` | public | Typedef for a resource allocator. |
| `resource_type` | typedef | `GLObjectResource<resource_handle_type, Allocator>` | public | Typedef for a resource. |
| `resource_manager_type` | typedef | `GLObjectResourceManager<resource_handle_type, Allocator>` | public | Typedef for a resource manager. |
| `SourceCodeSegment` | struct | `None` | public | Represents information of one (of potentially many) shader code segments. |
| `FileCodeSegment` | struct | `None` | public | Locates a \*file\* code segment within the concatenated source code. |
| `is_supported( GLRenderer &renderer, GLenum shader_type)` | method | `bool` | public | Returns true if shader\_type is supported on the runtime system. |
| `create( GLRenderer &renderer, GLenum shader_type)` | method | `shared_ptr_type` | public | Creates a shared pointer to a GLShaderObject object. shader\_type can be GL\_VERTEX\_SHADER\_ARB, GL\_FRAGMENT\_SHADER\_ARB or GL\_GEOMETRY\_SHADER\_EXT. |
| `create_as_unique_ptr( GLRenderer &renderer, GLenum shader_type)` | method | `std::unique_ptr<GLShaderObject>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `gl_shader_source( GLRenderer &renderer, const GLShaderSource &shader_source)` | method | `void` | public | Performs same function as the glShaderSource OpenGL function. |
| `gl_compile_shader( GLRenderer &renderer)` | method | `bool` | public | Performs same function as the glCompileShader OpenGL function (and also retrieves the GL\_COMPILE\_STATUS result). |
| `get_file_code_segments()` | method | `std::vector<FileCodeSegment>` | public | Similar to get\_source\_code\_segments except only returns code segment that came from files and returns the line number range of the code segment within the concatenated shader source code. |
| `get_shader_resource_handle()` | method | `resource_handle_type` | public | Returns the shader resource handle. |
| `d_resource` | field | `resource_type::non_null_ptr_to_const_type` | private | — |
| `d_source_code_segments` | field | `boost::optional< std::vector<SourceCodeSegment> >` | private | Source code segments set by gl\_shader\_source. |
| `GLShaderObject( GLRenderer &renderer, GLenum shader_type)` | constructor | `None` | private | Constructor. |
| `output_info_log()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLSHADEROBJECT_H` | macro | `None` | — |

## Notes

- `create()`/`create_as_unique_ptr()` require `is_supported()` to have already returned `true` for the requested `shader_type`; passing an unsupported type is a precondition violation, not a graceful failure.
- `gl_compile_shader()` logs the compiler diagnostic as a warning only when compilation fails; nothing is logged on success.
- Held via `boost::shared_ptr` rather than `non_null_intrusive_ptr` specifically so instances can be managed by a `GPlatesUtils::ObjectCache`.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLShaderProgramUtils](GLShaderProgramUtils.md) | opengl | 40 |
| [opengl/GLProgramObject](GLProgramObject.md) | opengl | 14 |
| [opengl/GLContext](GLContext.md) | opengl | 12 |
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 8 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 7 |
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 6 |
| [qt-widgets/TotalReconstructionPolesDialog](../qt-widgets/TotalReconstructionPolesDialog.md) | qt-widgets | 4 |
| [file-io/OgrWriter](../file-io/OgrWriter.md) | file-io | 3 |
| [presentation/DeprecatedSessionRestore](../presentation/DeprecatedSessionRestore.md) | presentation | 3 |
| [data-mining/DataMiningUtils](../data-mining/DataMiningUtils.md) | data-mining | 2 |
| [file-io/FeatureCollectionFileFormatRegistry](../file-io/FeatureCollectionFileFormatRegistry.md) | file-io | 2 |
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 2 |
| [app-logic/GPlatesQtMsgHandler](../app-logic/GPlatesQtMsgHandler.md) | app-logic | 1 |
| [file-io/TemporaryFileRegistry](../file-io/TemporaryFileRegistry.md) | file-io | 1 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 1 |
| [presentation/Session](../presentation/Session.md) | presentation | 1 |
| [utils/CommandLineParser](../utils/CommandLineParser.md) | utils | 1 |
| [utils/Profile](../utils/Profile.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLShaderObject.h
python scripts/gpq.py def GPlatesOpenGL::GLShaderObject --body
python scripts/gpq.py uses GLShaderObject --kind class
python scripts/gpq.py hier GLShaderObject
```

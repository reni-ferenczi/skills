# GLProgramObject

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 246 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLProgramObject.h` | C++ | 955 |
| `src/opengl/GLProgramObject.cc` | C++ | 1616 |

## Overview

[[[PROSE overview unit=opengl/GLProgramObject tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLProgramObject`](#gplatesopenglglprogramobject) | class | [`GLObject`](GLObject.md)<br>`boost::enable_shared_from_this<GLProgramObject>` | — | 0 | A shader program object. |

## Members

### `GPlatesOpenGL::GLProgramObject`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLProgramObject>` | public | A convenience typedef for a shared pointer to a GLProgramObject. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLProgramObject>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<GLProgramObject>` | public | A convenience typedef for a weak pointer to a GLProgramObject. |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const GLProgramObject>` | public | — |
| `resource_handle_type` | typedef | `GLuint` | public | Typedef for a resource handle. |
| `Allocator` | class | `None` | public | Policy class to allocate and deallocate OpenGL shader objects. |
| `allocator_type` | typedef | `Allocator` | public | Typedef for a resource allocator. |
| `resource_type` | typedef | `GLObjectResource<resource_handle_type, Allocator>` | public | Typedef for a resource. |
| `resource_manager_type` | typedef | `GLObjectResourceManager<resource_handle_type, Allocator>` | public | Typedef for a resource manager. |
| `is_supported( GLRenderer &renderer)` | method | `bool` | public | Returns true if shader program objects are supported on the runtime system. |
| `create( GLRenderer &renderer)` | method | `shared_ptr_type` | public | Creates a shared pointer to a GLProgramObject object. |
| `create_as_unique_ptr( GLRenderer &renderer)` | method | `std::unique_ptr<GLProgramObject>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `gl_attach_shader( GLRenderer &renderer, const GLShaderObject::shared_ptr_to_const_type &shader)` | method | `void` | public | Performs same function as the glAttachShader OpenGL function. |
| `gl_detach_shader( GLRenderer &renderer, const GLShaderObject::shared_ptr_to_const_type &shader)` | method | `void` | public | Performs same function as the glDetachShader OpenGL function. |
| `gl_bind_attrib_location( const char *attribute_name, GLuint attribute_index)` | method | `void` | public | NOTE: You'll also need to explictly bind each \*generic\* attribute index in the vertex array (see GLVertexArray) in order for this program to access the vertex attribute data in the vertex array (buffers). |
| `gl_program_parameteri( GLRenderer &renderer, GLenum pname, GLint value)` | method | `void` | public | Performs same function as the glProgramParameteri OpenGL function. |
| `gl_link_program( GLRenderer &renderer)` | method | `bool` | public | Performs same function as the glLinkProgram OpenGL function (and also retrieves the GL\_LINK\_STATUS result). |
| `gl_validate_program( GLRenderer &renderer)` | method | `bool` | public | Performs same function as the glValidateProgram OpenGL function (and also retrieves the GL\_VALIDATE\_STATUS result). |
| `is_active_uniform( const char *uniform_name)` | method | `bool` | public | Returns true if the specified uniform name corresponds to an active uniform variable in the most recent linking of this program (see gl\_link\_program). |
| `gl_uniform1f( GLRenderer &renderer, const char *name, GLfloat v0)` | method | `bool` | public | Performs same function as the glUniform1f OpenGL function - returns false if not active. |
| `gl_uniform1f( GLRenderer &renderer, const char *name, const GLfloat *value, unsigned int count)` | method | `bool` | public | Performs same function as the glUniform1fv OpenGL function - returns false if not active. |
| `gl_uniform1i( GLRenderer &renderer, const char *name, GLint v0)` | method | `bool` | public | Performs same function as the glUniform1i OpenGL function - returns false if not active. |
| `gl_uniform1i( GLRenderer &renderer, const char *name, const GLint *value, unsigned int count)` | method | `bool` | public | Performs same function as the glUniform1iv OpenGL function - returns false if not active. |
| `gl_uniform1d( GLRenderer &renderer, const char *name, GLdouble v0)` | method | `bool` | public | Performs same function as the glUniform1d OpenGL function - returns false if not active. |
| `gl_uniform1d( GLRenderer &renderer, const char *name, const GLdouble *value, unsigned int count)` | method | `bool` | public | Performs same function as the glUniform1dv OpenGL function - returns false if not active. |
| `gl_uniform1ui( GLRenderer &renderer, const char *name, GLuint v0)` | method | `bool` | public | Performs same function as the glUniform1ui OpenGL function - returns false if not active. |
| `gl_uniform1ui( GLRenderer &renderer, const char *name, const GLuint *value, unsigned int count)` | method | `bool` | public | Performs same function as the glUniform1uiv OpenGL function - returns false if not active. |
| `gl_uniform2f( GLRenderer &renderer, const char *name, GLfloat v0, GLfloat v1)` | method | `bool` | public | Performs same function as the glUniform2f OpenGL function - returns false if not active. |
| `gl_uniform2f( GLRenderer &renderer, const char *name, const GLfloat *value, unsigned int count)` | method | `bool` | public | Performs same function as the glUniform2fv OpenGL function - returns false if not active. |
| `gl_uniform2i( GLRenderer &renderer, const char *name, GLint v0, GLint v1)` | method | `bool` | public | Performs same function as the glUniform2i OpenGL function - returns false if not active. |
| `gl_uniform2i( GLRenderer &renderer, const char *name, const GLint *value, unsigned int count)` | method | `bool` | public | Performs same function as the glUniform2iv OpenGL function - returns false if not active. |
| `gl_uniform2d( GLRenderer &renderer, const char *name, GLdouble v0, GLdouble v1)` | method | `bool` | public | Performs same function as the glUniform2d OpenGL function - returns false if not active. |
| `gl_uniform2d( GLRenderer &renderer, const char *name, const GLdouble *value, unsigned int count)` | method | `bool` | public | Performs same function as the glUniform2dv OpenGL function - returns false if not active. |
| `gl_uniform2ui( GLRenderer &renderer, const char *name, GLuint v0, GLuint v1)` | method | `bool` | public | Performs same function as the glUniform2ui OpenGL function - returns false if not active. |
| `gl_uniform2ui( GLRenderer &renderer, const char *name, const GLuint *value, unsigned int count)` | method | `bool` | public | Performs same function as the glUniform2uiv OpenGL function - returns false if not active. |
| `gl_uniform3f( GLRenderer &renderer, const char *name, GLfloat v0, GLfloat v1, GLfloat v2)` | method | `bool` | public | Performs same function as the glUniform3f OpenGL function - returns false if not active. |
| `gl_uniform3f( GLRenderer &renderer, const char *name, const GLfloat *value, unsigned int count)` | method | `bool` | public | Performs same function as the glUniform3fv OpenGL function - returns false if not active. |
| `gl_uniform3i( GLRenderer &renderer, const char *name, GLint v0, GLint v1, GLint v2)` | method | `bool` | public | Performs same function as the glUniform3i OpenGL function - returns false if not active. |
| `gl_uniform3i( GLRenderer &renderer, const char *name, const GLint *value, unsigned int count)` | method | `bool` | public | Performs same function as the glUniform3iv OpenGL function - returns false if not active. |
| `gl_uniform3d( GLRenderer &renderer, const char *name, GLdouble v0, GLdouble v1, GLdouble v2)` | method | `bool` | public | Performs same function as the glUniform3d OpenGL function - returns false if not active. |
| `gl_uniform3d( GLRenderer &renderer, const char *name, const GLdouble *value, unsigned int count)` | method | `bool` | public | Performs same function as the glUniform3dv OpenGL function - returns false if not active. |
| `gl_uniform3ui( GLRenderer &renderer, const char *name, GLuint v0, GLuint v1, GLuint v2)` | method | `bool` | public | Performs same function as the glUniform3ui OpenGL function - returns false if not active. |
| `gl_uniform3ui( GLRenderer &renderer, const char *name, const GLuint *value, unsigned int count)` | method | `bool` | public | Performs same function as the glUniform3uiv OpenGL function - returns false if not active. |
| `gl_uniform3f( GLRenderer &renderer, const char *name, const GPlatesMaths::UnitVector3D &value)` | method | `bool` | public | Writes UnitVector3D as single-precision (x,y,z). |
| `gl_uniform3d( GLRenderer &renderer, const char *name, const GPlatesMaths::UnitVector3D &value)` | method | `bool` | public | Writes UnitVector3D as double-precision (x,y,z). |
| `gl_uniform3f( GLRenderer &renderer, const char *name, const GPlatesMaths::Vector3D &value)` | method | `bool` | public | Writes Vector3D as (x,y,z). |
| `gl_uniform3d( GLRenderer &renderer, const char *name, const GPlatesMaths::Vector3D &value)` | method | `bool` | public | Writes Vector3D as double-precision (x,y,z). |
| `gl_uniform4f( GLRenderer &renderer, const char *name, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)` | method | `bool` | public | Performs same function as the glUniform4f OpenGL function - returns false if not active. |
| `gl_uniform4f( GLRenderer &renderer, const char *name, const GLfloat *value, unsigned int count)` | method | `bool` | public | Performs same function as the glUniform4fv OpenGL function - returns false if not active. |
| `gl_uniform4i( GLRenderer &renderer, const char *name, GLint v0, GLint v1, GLint v2, GLint v3)` | method | `bool` | public | Performs same function as the glUniform4i OpenGL function - returns false if not active. |
| `gl_uniform4i( GLRenderer &renderer, const char *name, const GLint *value, unsigned int count)` | method | `bool` | public | Performs same function as the glUniform4iv OpenGL function - returns false if not active. |
| `gl_uniform4d( GLRenderer &renderer, const char *name, GLdouble v0, GLdouble v1, GLdouble v2, GLdouble v3)` | method | `bool` | public | Performs same function as the glUniform4d OpenGL function - returns false if not active. |
| `gl_uniform4d( GLRenderer &renderer, const char *name, const GLdouble *value, unsigned int count)` | method | `bool` | public | Performs same function as the glUniform4dv OpenGL function - returns false if not active. |
| `gl_uniform4ui( GLRenderer &renderer, const char *name, GLuint v0, GLuint v1, GLuint v2, GLuint v3)` | method | `bool` | public | Performs same function as the glUniform4ui OpenGL function - returns false if not active. |
| `gl_uniform4ui( GLRenderer &renderer, const char *name, const GLuint *value, unsigned int count)` | method | `bool` | public | Performs same function as the glUniform4uiv OpenGL function - returns false if not active. |
| `gl_uniform4f( GLRenderer &renderer, const char *name, const GPlatesMaths::UnitVector3D &value_xyz, GLfloat value_w = 1)` | method | `bool` | public | Writes UnitVector3D as single-precision (x,y,z,w). |
| `gl_uniform4d( GLRenderer &renderer, const char *name, const GPlatesMaths::UnitVector3D &value_xyz, GLdouble value_w = 1)` | method | `bool` | public | Writes UnitVector3D as double-precision (x,y,z,w). |
| `gl_uniform4f( GLRenderer &renderer, const char *name, const GPlatesMaths::Vector3D &value_xyz, GLfloat value_w = 1)` | method | `bool` | public | Writes Vector3D as single-precision (x,y,z,w). |
| `gl_uniform4d( GLRenderer &renderer, const char *name, const GPlatesMaths::Vector3D &value_xyz, GLdouble value_w = 1)` | method | `bool` | public | Writes Vector3D as double-precision (x,y,z,w). |
| `gl_uniform4f( GLRenderer &renderer, const char *name, const GPlatesMaths::UnitQuaternion3D &unit_quat)` | method | `bool` | public | Writes UnitQuaternion as single-precision (x,y,z,w). |
| `gl_uniform4d( GLRenderer &renderer, const char *name, const GPlatesMaths::UnitQuaternion3D &unit_quat)` | method | `bool` | public | Writes UnitQuaternion as double-precision (x,y,z,w). |
| `gl_uniform4f( GLRenderer &renderer, const char *name, const GPlatesGui::Colour &colour)` | method | `bool` | public | Writes value as single-precision (r,g,b,a). |
| `gl_uniform_matrix2x2f( GLRenderer &renderer, const char *name, const GLfloat *value, unsigned int count, GLboolean transpose)` | method | `bool` | public | Performs same function as the glUniformMatrix2fv OpenGL function - returns false if not active. |
| `gl_uniform_matrix2x2d( GLRenderer &renderer, const char *name, const GLdouble *value, unsigned int count, GLboolean transpose)` | method | `bool` | public | Performs same function as the glUniformMatrix2dv OpenGL function - returns false if not active. |
| `gl_uniform_matrix3x3f( GLRenderer &renderer, const char *name, const GLfloat *value, unsigned int count, GLboolean transpose)` | method | `bool` | public | Performs same function as the glUniformMatrix3fv OpenGL function - returns false if not active. |
| `gl_uniform_matrix3x3d( GLRenderer &renderer, const char *name, const GLdouble *value, unsigned int count, GLboolean transpose)` | method | `bool` | public | Performs same function as the glUniformMatrix3dv OpenGL function - returns false if not active. |
| `gl_uniform_matrix4x4f( GLRenderer &renderer, const char *name, const GLfloat *value, unsigned int count, GLboolean transpose)` | method | `bool` | public | Performs same function as the glUniformMatrix4fv OpenGL function - returns false if not active. |
| `gl_uniform_matrix4x4d( GLRenderer &renderer, const char *name, const GLdouble *value, unsigned int count, GLboolean transpose)` | method | `bool` | public | Performs same function as the glUniformMatrix4dv OpenGL function - returns false if not active. |
| `gl_uniform_matrix4x4f( GLRenderer &renderer, const char *name, const GLMatrix &matrix)` | method | `bool` | public | Performs same function as the glUniformMatrix4fv OpenGL function with a single matrix - returns false if not active. |
| `gl_uniform_matrix4x4d( GLRenderer &renderer, const char *name, const GLMatrix &matrix)` | method | `bool` | public | Performs same function as the glUniformMatrix4dv OpenGL function with a single matrix - returns false if not active. |
| `gl_uniform_matrix4x4f( GLRenderer &renderer, const char *name, const std::vector<GLMatrix> &matrices)` | method | `bool` | public | Performs same function as the glUniformMatrix4fv OpenGL function with one or more matrices - returns false if not active. |
| `gl_uniform_matrix4x4d( GLRenderer &renderer, const char *name, const std::vector<GLMatrix> &matrices)` | method | `bool` | public | Performs same function as the glUniformMatrix4dv OpenGL function with one or more matrices - returns false if not active. |
| `get_program_resource_handle()` | method | `resource_handle_type` | public | Returns the program resource handle. |
| `shader_object_seq_type` | typedef | `std::set<GLShaderObject::shared_ptr_to_const_type>` | private | Typedef for a sequence of shader objects. |
| `uniform_name_type` | typedef | `std::string` | private | Typedef for a name of a uniform variable. |
| `uniform_location_type` | typedef | `GLint` | private | Typedef for the index, or location, of a uniform variable. |
| `uniform_location_map_type` | typedef | `std::map<uniform_name_type, uniform_location_type>` | private | Typedef for a map of uniform variable names to indices (or locations). |
| `d_resource` | field | `resource_type::non_null_ptr_to_const_type` | private | — |
| `d_shader_objects` | field | `shader_object_seq_type` | private | — |
| `d_uniform_locations` | field | `uniform_location_map_type` | private | — |
| `GLProgramObject( GLRenderer &renderer)` | constructor | `None` | private | Constructor. |
| `get_uniform_location( const char *uniform_name)` | method | `uniform_location_type` | private | Get the uniform location index of the specified uniform variable name. |
| `output_info_log()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLPROGRAMOBJECT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLProgramObject tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 117 |
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 72 |
| [opengl/GLShaderProgramUtils](GLShaderProgramUtils.md) | opengl | 41 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 29 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 21 |
| [opengl/GLContext](GLContext.md) | opengl | 10 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 10 |
| [opengl/GLMultiResolutionRasterMapView](GLMultiResolutionRasterMapView.md) | opengl | 8 |
| [opengl/GLRenderer](GLRenderer.md) | opengl | 6 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 5 |
| [opengl/GLStateSets](GLStateSets.md) | opengl | 5 |
| [opengl/GLNormalMapSource](GLNormalMapSource.md) | opengl | 4 |
| [opengl/GLLight](GLLight.md) | opengl | 3 |
| [opengl/GLOffScreenContext](GLOffScreenContext.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLProgramObject.h
python scripts/gpq.py def GPlatesOpenGL::GLProgramObject --body
python scripts/gpq.py uses GLProgramObject --kind class
python scripts/gpq.py hier GLProgramObject
```

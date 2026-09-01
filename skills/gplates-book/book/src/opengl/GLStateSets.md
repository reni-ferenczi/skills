# GLStateSets

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 11 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLStateSets.h` | C++ | 2194 |
| `src/opengl/GLStateSets.cc` | C++ | 3783 |

## Overview

This is where the rendering backend finally calls OpenGL. Every concrete `GLStateSet` here owns one slice of the OpenGL *global* state — one slot in a `GLState` — and knows how to emit the minimal GL calls for a transition into or out of that slice. The three virtuals it implements come from `GLStateSet` and correspond to the three transitions `GLState::apply_state` can encounter: `apply_state` from another instance of the same type, `apply_from_default_state` when the slot was previously empty, and `apply_to_default_state` when the slot is being vacated. Because an empty slot means "OpenGL default", each state set has to know the OpenGL default for its own state — `GLDepthMaskStateSet` knows the default is `GL_TRUE`, `GLTexGenStateSet` carries `DEFAULT_GEN_MODE` and the default S/T/R/Q planes as static members — and each one returns early without touching OpenGL when the transition would be a no-op. Note the scope boundary drawn in `GLStateSet`: state held *inside* an OpenGL object (texture parameters, buffer contents) is set on those objects directly; only the global state, including the bindings themselves, lives here.

The second job of this file is hiding capability variation from callers. Several state sets branch on `GLCapabilities` at apply time and silently do the right cheaper thing: `GLViewportStateSet` and `GLScissorStateSet` call `glViewportArrayv` when `GL_ARB_viewport_array` is present and plain `glViewport` when it is not (or when all viewports are the same, which the constructor records as a flag so the common single-viewport case stores one rectangle and compares one rectangle); the vertex array object state sets are compiled out entirely if the build's `glew.h` predates `GL_ARB_vertex_array_object`; `set_active_texture` skips `glActiveTextureARB` when `GL_ARB_multitexture` is missing rather than asserting, since unit zero is always valid. `GLTexGenStateSet` and `GLTexEnvStateSet` accept `GLint`/`GLfloat`/`GLdouble` and vectors of each through a `boost::variant`, with a `BOOST_MPL_ASSERT` in the constructor and `TexGenVisitor`/`TexEnvVisitor` dispatching to the right `glTexGen*`/`glTexEnv*` overload; `EqualityVisitor` does the corresponding comparison for change detection.

Two state sets have effects beyond their own slot, and they are the reason `GLState` runs a two-pass apply and a separate vertex-array-object pass. `GLBindTextureStateSet` must make its texture unit current first, so it calls the file-local `set_active_texture`, which mutates the caller's `last_applied_state` to record the change — the active texture unit is another state set's slot. `GLBindVertexArrayObjectStateSet` is more drastic: binding a VAO pulls a whole block of buffer bindings and client enable/disable state into effect at once, so after `glBindVertexArray` it calls `last_applied_state.copy_vertex_array_state()` from the object's shadowed resource state, so the individual vertex-array state sets do not then try to re-apply what the driver already has. `Implementation::GLVertexAttributeBuffer` factors out the change detection shared by all the array-pointer state sets, tracking both the pointer or offset and whether the underlying buffer has been reallocated since it was last handed to OpenGL.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::(anonymous)::TexGenVisitor`](#gplatesopenglanonymoustexgenvisitor) | class | `boost::static_visitor<>` | — | 0 | Applies texture coordinate generation state based on param variant type. |
| [`GPlatesOpenGL::(anonymous)::TexEnvVisitor`](#gplatesopenglanonymoustexenvvisitor) | class | `boost::static_visitor<>` | — | 0 | Applies texture environment state based on param variant type. |
| [`GPlatesOpenGL::(anonymous)::EqualityVisitor`](#gplatesopenglanonymousequalityvisitor) | class | `boost::static_visitor<bool>` | — | 0 | Compares state that consists of GLint, GLfloat, GLdouble or a std::vector of any of those types. |
| [`GPlatesOpenGL::Implementation::GLVertexAttributeBuffer`](#gplatesopenglimplementationglvertexattributebuffer) | class | — | — | 0 | Utility class for tracking state changes of vertex attribute pointers (both generic and non-generic). |
| [`GPlatesOpenGL::GLActiveTextureStateSet`](#gplatesopenglglactivetexturestateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the active texture unit. |
| [`GPlatesOpenGL::GLAlphaFuncStateSet`](#gplatesopenglglalphafuncstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the alpha test function. |
| [`GPlatesOpenGL::GLBindBufferObjectStateSet`](#gplatesopenglglbindbufferobjectstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to bind a framebuffer object. |
| [`GPlatesOpenGL::GLBindFrameBufferObjectStateSet`](#gplatesopenglglbindframebufferobjectstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to bind a framebuffer object. |
| [`GPlatesOpenGL::GLBindProgramObjectStateSet`](#gplatesopenglglbindprogramobjectstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to bind a shader program object. |
| [`GPlatesOpenGL::GLBindTextureStateSet`](#gplatesopenglglbindtexturestateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to bind a texture to a texture unit. |
| [`GPlatesOpenGL::GLBindVertexArrayObjectStateSet`](#gplatesopenglglbindvertexarrayobjectstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to bind a vertex array object. |
| [`GPlatesOpenGL::GLBlendEquationStateSet`](#gplatesopenglglblendequationstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the alpha blend equation. |
| [`GPlatesOpenGL::GLBlendFuncStateSet`](#gplatesopenglglblendfuncstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the alpha blend function. |
| [`GPlatesOpenGL::GLClearColorStateSet`](#gplatesopenglglclearcolorstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the clear color. |
| [`GPlatesOpenGL::GLClearDepthStateSet`](#gplatesopenglglcleardepthstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the clear depth. |
| [`GPlatesOpenGL::GLClearStencilStateSet`](#gplatesopenglglclearstencilstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the clear stencil. |
| [`GPlatesOpenGL::GLClientActiveTextureStateSet`](#gplatesopenglglclientactivetexturestateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the client active texture unit. |
| [`GPlatesOpenGL::GLColorMaskStateSet`](#gplatesopenglglcolormaskstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the color mask. |
| [`GPlatesOpenGL::GLColorPointerStateSet`](#gplatesopenglglcolorpointerstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the vertex color array source. |
| [`GPlatesOpenGL::GLCullFaceStateSet`](#gplatesopenglglcullfacestateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used glCullFace. |
| [`GPlatesOpenGL::GLDepthFuncStateSet`](#gplatesopenglgldepthfuncstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the depth test function. |
| [`GPlatesOpenGL::GLDepthMaskStateSet`](#gplatesopenglgldepthmaskstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the depth mask. |
| [`GPlatesOpenGL::GLDepthRangeStateSet`](#gplatesopenglgldepthrangestateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the depth range. |
| [`GPlatesOpenGL::GLEnableClientStateStateSet`](#gplatesopenglglenableclientstatestateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to enable/disable client state vertex arrays. |
| [`GPlatesOpenGL::GLEnableClientTextureStateStateSet`](#gplatesopenglglenableclienttexturestatestateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to enable/disable client state texture coordinate vertex arrays. |
| [`GPlatesOpenGL::GLEnableStateSet`](#gplatesopenglglenablestateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to enable/disable capabilities (except texturing - use GLEnableTextureStateSet for that). |
| [`GPlatesOpenGL::GLEnableTextureStateSet`](#gplatesopenglglenabletexturestateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to enable/disable texturing. |
| [`GPlatesOpenGL::GLEnableVertexAttribArrayStateSet`](#gplatesopenglglenablevertexattribarraystateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to enable/disable \*generic\* vertex attribute arrays. |
| [`GPlatesOpenGL::GLFrontFaceStateSet`](#gplatesopenglglfrontfacestateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used for glFrontFace. |
| [`GPlatesOpenGL::GLHintStateSet`](#gplatesopenglglhintstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used for glHint. |
| [`GPlatesOpenGL::GLLineWidthStateSet`](#gplatesopenglgllinewidthstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the line width. |
| [`GPlatesOpenGL::GLLoadMatrixStateSet`](#gplatesopenglglloadmatrixstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to load a modelview or projection matrix. |
| [`GPlatesOpenGL::GLLoadTextureMatrixStateSet`](#gplatesopenglglloadtexturematrixstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to load a texture matrix. |
| [`GPlatesOpenGL::GLMatrixModeStateSet`](#gplatesopenglglmatrixmodestateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to specify matrix mode. |
| [`GPlatesOpenGL::GLNormalPointerStateSet`](#gplatesopenglglnormalpointerstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the vertex normal array source. |
| [`GPlatesOpenGL::GLPointSizeStateSet`](#gplatesopenglglpointsizestateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the point size. |
| [`GPlatesOpenGL::GLPolygonModeStateSet`](#gplatesopenglglpolygonmodestateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the polygon mode. |
| [`GPlatesOpenGL::GLPolygonOffsetStateSet`](#gplatesopenglglpolygonoffsetstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used for glPolygonOffset. |
| [`GPlatesOpenGL::GLScissorStateSet`](#gplatesopenglglscissorstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the scissor rectangle(s). |
| [`GPlatesOpenGL::GLStencilFuncStateSet`](#gplatesopenglglstencilfuncstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the stencil function. |
| [`GPlatesOpenGL::GLStencilMaskStateSet`](#gplatesopenglglstencilmaskstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the stencil mask. |
| [`GPlatesOpenGL::GLStencilOpStateSet`](#gplatesopenglglstencilopstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the stencil operation. |
| [`GPlatesOpenGL::GLTexCoordPointerStateSet`](#gplatesopenglgltexcoordpointerstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the vertex texture coordinate array source. |
| [`GPlatesOpenGL::GLTexGenStateSet`](#gplatesopenglgltexgenstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used set texture coordinate generation state. |
| [`GPlatesOpenGL::GLTexEnvStateSet`](#gplatesopenglgltexenvstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used set texture environment state. |
| [`GPlatesOpenGL::GLVertexAttribPointerStateSet`](#gplatesopenglglvertexattribpointerstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the \*generic\* vertex attribute array source. |
| [`GPlatesOpenGL::GLVertexPointerStateSet`](#gplatesopenglglvertexpointerstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the vertex position array source. |
| [`GPlatesOpenGL::GLViewportStateSet`](#gplatesopenglglviewportstateset) | struct | [`GLStateSet`](GLStateSet.md) | — | 0 | Used to set the viewport. |

## Members

### `GPlatesOpenGL::(anonymous)::TexGenVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TexGenVisitor( GLenum coord, GLenum pname)` | constructor | `None` | public | — |
| `operator()( const GLint &param)` | operator | `void` | public | — |
| `operator()( const GLfloat &param)` | operator | `void` | public | — |
| `operator()( const GLdouble &param)` | operator | `void` | public | — |
| `operator()( const std::vector<GLint> &param)` | operator | `void` | public | — |
| `operator()( const std::vector<GLfloat> &param)` | operator | `void` | public | — |
| `operator()( const std::vector<GLdouble> &param)` | operator | `void` | public | — |
| `d_coord` | field | `GLenum` | private | — |
| `d_pname` | field | `GLenum` | private | — |

### `GPlatesOpenGL::(anonymous)::TexEnvVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TexEnvVisitor( GLenum target, GLenum pname)` | constructor | `None` | public | — |
| `operator()( const GLint &param)` | operator | `void` | public | — |
| `operator()( const GLfloat &param)` | operator | `void` | public | — |
| `operator()( const std::vector<GLint> &param)` | operator | `void` | public | — |
| `operator()( const std::vector<GLfloat> &param)` | operator | `void` | public | — |
| `d_target` | field | `GLenum` | private | — |
| `d_pname` | field | `GLenum` | private | — |

### `GPlatesOpenGL::(anonymous)::EqualityVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const ParamDataType1 &param1, const ParamDataType2 &param2)` | operator | `bool` | public | This is needed since can't really compare say a GLint with a std::vector\<GLint\>. |
| `operator()( GLint param1, GLint param2)` | operator | `bool` | public | For GLint. |
| `operator()( GLfloat param1, GLfloat param2)` | operator | `bool` | public | For GLfloat. |
| `operator()( GLdouble param1, GLdouble param2)` | operator | `bool` | public | For GLdouble. |
| `operator()( const std::vector<ParamDataType1> &param1, const std::vector<ParamDataType2> &param2)` | operator | `bool` | public | The template types can be GLint, GLfloat or GLdouble. |

### `GPlatesOpenGL::Implementation::GLVertexAttributeBuffer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLVertexAttributeBuffer( GLint offset, const GLBufferObject::shared_ptr_to_const_type &buffer_object)` | constructor | `None` | public | Binds to a vertex buffer object. |
| `GLVertexAttributeBuffer( GLint offset, const GLBufferImpl::shared_ptr_to_const_type &buffer_impl)` | constructor | `None` | public | No binding to a vertex buffer object (using client memory array). |
| `has_changed_state( const GLVertexAttributeBuffer &last_applied_buffer)` | method | `bool` | public | Returns true if a buffer pointer state change is necessary. |
| `has_changed_from_default_state()` | method | `bool` | public | Returns true if a buffer pointer state change from the default state is necessary. |
| `has_changed_to_default_state()` | method | `bool` | public | Returns true if a buffer pointer state change to the default state is necessary. |
| `bind_buffer( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | Binds the current buffer. |
| `unbind_buffer( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | Unbinds the current buffer. |
| `get_buffer_pointer_to_apply()` | method | `GLvoid` | public | Returns the buffer pointer (to an attribute array with offset added) that needs to be applied. |
| `applied_buffer_pointer_to_opengl()` | method | `void` | public | Call this when you've just specified a vertex array pointer. |
| `buffer_type` | typedef | `boost::variant<GLBufferObject::shared_ptr_to_const_type, GLBufferImpl::shared_ptr_to_const_type>` | private | Typedef for a variant of GLBufferObject or GLBufferImpl. |
| `d_offset` | field | `GLint` | private | The offset into the buffer. |
| `d_buffer_variant` | field | `buffer_type` | private | The derived GLBuffer type (used to access methods existing only in derived classes). |
| `d_buffer` | field | `GLBuffer::shared_ptr_to_const_type` | private | The base GLBuffer pointer. |
| `d_pointer_to_apply` | field | `GLvoid` | private | Keeps track of the last applied buffer (array) pointer. |
| `d_buffer_allocation_observer` | field | `GLBuffer::buffer_allocation_observer_type` | private | Keeps track of internal buffer (re)allocations (ie, calls to 'GLBuffer::gl\_buffer\_data'). |

### `GPlatesOpenGL::GLActiveTextureStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLActiveTextureStateSet( const GLCapabilities &capabilities, GLenum active_texture)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_active_texture` | field | `GLenum` | public | — |

### `GPlatesOpenGL::GLAlphaFuncStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLAlphaFuncStateSet( GLenum func, GLclampf ref)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_alpha_func` | field | `GLenum` | public | — |
| `d_ref` | field | `GPlatesMaths::real_t` | public | — |

### `GPlatesOpenGL::GLBindBufferObjectStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLBindBufferObjectStateSet( const GLBufferObject::shared_ptr_to_const_type &buffer_object, GLenum target)` | constructor | `None` | public | Binds a buffer object. |
| `GLBindBufferObjectStateSet( GLenum target)` | constructor | `None` | public | Specifies no bound buffer object (at the specified target). |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_buffer_object` | field | `boost::optional<GLBufferObject::shared_ptr_to_const_type>` | public | — |
| `d_buffer_object_resource` | field | `boost::optional<GLBufferObject::resource_handle_type>` | public | — |
| `d_target` | field | `GLenum` | public | — |

### `GPlatesOpenGL::GLBindFrameBufferObjectStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLBindFrameBufferObjectStateSet( boost::optional<GLFrameBufferObject::shared_ptr_to_const_type> frame_buffer_object)` | constructor | `None` | public | Binds a framebuffer object, or unbinds (if frame\_buffer\_object is boost::none). |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_frame_buffer_object` | field | `boost::optional<GLFrameBufferObject::shared_ptr_to_const_type>` | public | — |

### `GPlatesOpenGL::GLBindProgramObjectStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLBindProgramObjectStateSet( boost::optional<GLProgramObject::shared_ptr_to_const_type> program_object)` | constructor | `None` | public | Binds a shader program object, or unbinds (if program\_object is boost::none). |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_program_object` | field | `boost::optional<GLProgramObject::shared_ptr_to_const_type>` | public | — |

### `GPlatesOpenGL::GLBindTextureStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLBindTextureStateSet( const GLCapabilities &capabilities, const GLTexture::shared_ptr_to_const_type &texture_object, GLenum texture_unit, GLenum texture_target)` | constructor | `None` | public | Binds a texture object. |
| `GLBindTextureStateSet( const GLCapabilities &capabilities, GLenum texture_unit, GLenum texture_target)` | constructor | `None` | public | Unbinds any texture object currently bound to the specified target and texture unit. |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_texture_object` | field | `boost::optional<GLTexture::shared_ptr_to_const_type>` | public | — |
| `d_texture_unit` | field | `GLenum` | public | — |
| `d_texture_target` | field | `GLenum` | public | — |

### `GPlatesOpenGL::GLBindVertexArrayObjectStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLBindVertexArrayObjectStateSet( GLVertexArrayObject::resource_handle_type resource_handle, const boost::shared_ptr<GLState> &current_resource_state, const boost::shared_ptr<GLState> &current_default_state, const GLVertexArrayObject::shared_ptr_to_const_type &vertex_array_object)` | constructor | `None` | public | Binds a vertex array object. current\_resource\_state represents the vertex array state of the vertex array object. current\_default\_state represents the vertex array state of the default vertex array object (resource handle zero). |
| `GLBindVertexArrayObjectStateSet( const boost::shared_ptr<GLState> &current_default_state)` | constructor | `None` | public | Unbinds any vertex array object (switches to using the default vertex array object with resource handle zero). current\_default\_state represents the vertex array state of the default vertex array object (resource handle zero). |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_resource_handle` | field | `boost::optional<GLVertexArrayObject::resource_handle_type>` | public | — |
| `d_current_resource_state` | field | `boost::shared_ptr<GLState>` | public | Represents the current vertex array object state as seen by the underlying OpenGL. |
| `d_current_default_state` | field | `boost::shared_ptr<GLState>` | public | Represents the current vertex array state for the default vertex array object with resource handle zero (as seen by the underlying OpenGL). |
| `d_vertex_array_object` | field | `boost::optional<GLVertexArrayObject::shared_ptr_to_const_type>` | public | NOTE: This is \*only\* here for clients to retrieve - so they can know what GLVertexArrayObject the resource handle came from - we don't actually use it in the implementation of this class. |

### `GPlatesOpenGL::GLBlendEquationStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLBlendEquationStateSet( const GLCapabilities &capabilities, GLenum mode)` | constructor | `None` | public | — |
| `GLBlendEquationStateSet( const GLCapabilities &capabilities, GLenum modeRGB, GLenum modeAlpha)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_mode_RGB` | field | `GLenum` | public | — |
| `d_mode_A` | field | `GLenum` | public | — |
| `d_separate_equations` | field | `bool` | public | If the RGB and A components have separate equations. |

### `GPlatesOpenGL::GLBlendFuncStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLBlendFuncStateSet( GLenum sfactor, GLenum dfactor)` | constructor | `None` | public | — |
| `GLBlendFuncStateSet( const GLCapabilities &capabilities, GLenum sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_src_factor_RGB` | field | `GLenum` | public | — |
| `d_dst_factor_RGB` | field | `GLenum` | public | — |
| `d_src_factor_A` | field | `GLenum` | public | — |
| `d_dst_factor_A` | field | `GLenum` | public | — |
| `d_separate_factors` | field | `bool` | public | If the RGB and A components have separate factors. |

### `GPlatesOpenGL::GLClearColorStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLClearColorStateSet( GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_red` | field | `GPlatesMaths::real_t` | public | — |
| `d_green` | field | `GPlatesMaths::real_t` | public | — |
| `d_blue` | field | `GPlatesMaths::real_t` | public | — |
| `d_alpha` | field | `GPlatesMaths::real_t` | public | — |

### `GPlatesOpenGL::GLClearDepthStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLClearDepthStateSet( GLclampd depth)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_depth` | field | `GPlatesMaths::real_t` | public | — |

### `GPlatesOpenGL::GLClearStencilStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLClearStencilStateSet( GLint stencil)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_stencil` | field | `GLint` | public | — |

### `GPlatesOpenGL::GLClientActiveTextureStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLClientActiveTextureStateSet( const GLCapabilities &capabilities, GLenum client_active_texture)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_client_active_texture` | field | `GLenum` | public | — |

### `GPlatesOpenGL::GLColorMaskStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLColorMaskStateSet( GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_red` | field | `GLboolean` | public | — |
| `d_green` | field | `GLboolean` | public | — |
| `d_blue` | field | `GLboolean` | public | — |
| `d_alpha` | field | `GLboolean` | public | — |

### `GPlatesOpenGL::GLColorPointerStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLColorPointerStateSet( GLint size, GLenum type, GLsizei stride, GLint offset, const GLBufferObject::shared_ptr_to_const_type &buffer_object)` | constructor | `None` | public | Binds to a vertex buffer object. |
| `GLColorPointerStateSet( GLint size, GLenum type, GLsizei stride, GLint offset, const GLBufferImpl::shared_ptr_to_const_type &buffer_impl)` | constructor | `None` | public | No binding to a vertex buffer object (using client memory array). |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_buffer` | field | `Implementation::GLVertexAttributeBuffer` | private | — |
| `d_size` | field | `GLint` | private | — |
| `d_type` | field | `GLenum` | private | — |
| `d_stride` | field | `GLsizei` | private | — |

### `GPlatesOpenGL::GLCullFaceStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLCullFaceStateSet( GLenum mode)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_mode` | field | `GLenum` | public | — |

### `GPlatesOpenGL::GLDepthFuncStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLDepthFuncStateSet( GLenum func)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_depth_func` | field | `GLenum` | public | — |

### `GPlatesOpenGL::GLDepthMaskStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLDepthMaskStateSet( GLboolean flag)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_flag` | field | `GLboolean` | public | — |

### `GPlatesOpenGL::GLDepthRangeStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `depth_range_seq_type` | typedef | `std::vector<GLDepthRange>` | public | Typedef for a sequence of depth ranges. |
| `GLDepthRangeStateSet( const GLCapabilities &capabilities, const GLDepthRange &depth_range)` | constructor | `None` | public | Constructor to set all depth ranges to the same parameters. |
| `GLDepthRangeStateSet( const GLCapabilities &capabilities, const depth_range_seq_type &all_depth_ranges)` | constructor | `None` | public | Constructor to set depth ranges individually. |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_depth_ranges` | field | `depth_range_seq_type` | private | Contains 'GLCapabilities::Viewport::gl\_max\_viewports' depth ranges. |
| `d_all_depth_ranges_are_the_same` | field | `bool` | private | Is true if all depth ranges in d\_depth\_ranges are the same. |
| `DEFAULT_DEPTH_RANGE` | field | `GLDepthRange` | private | — |
| `apply_state( const GLCapabilities &capabilities)` | method | `void` | private | — |

### `GPlatesOpenGL::GLEnableClientStateStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLEnableClientStateStateSet( GLenum array, bool enable)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_array` | field | `GLenum` | public | — |
| `d_enable` | field | `bool` | public | — |

### `GPlatesOpenGL::GLEnableClientTextureStateStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLEnableClientTextureStateStateSet( GLenum texture_unit, bool enable)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_texture_unit` | field | `GLenum` | public | — |
| `d_enable` | field | `bool` | public | — |

### `GPlatesOpenGL::GLEnableStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLEnableStateSet( GLenum cap, bool enable)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `get_default( GLenum cap)` | method | `bool` | public | Utilitiy function to return the default for the specified capability. |
| `d_cap` | field | `GLenum` | public | — |
| `d_enable` | field | `bool` | public | — |

### `GPlatesOpenGL::GLEnableTextureStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLEnableTextureStateSet( GLenum texture_unit, GLenum texture_target, bool enable)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_texture_unit` | field | `GLenum` | public | — |
| `d_texture_target` | field | `GLenum` | public | — |
| `d_enable` | field | `bool` | public | — |

### `GPlatesOpenGL::GLEnableVertexAttribArrayStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLEnableVertexAttribArrayStateSet( GLuint attribute_index, bool enable)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_attribute_index` | field | `GLuint` | public | — |
| `d_enable` | field | `bool` | public | — |

### `GPlatesOpenGL::GLFrontFaceStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLFrontFaceStateSet( GLenum mode)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_mode` | field | `GLenum` | public | — |

### `GPlatesOpenGL::GLHintStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLHintStateSet( GLenum target, GLenum mode)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_target` | field | `GLenum` | public | — |
| `d_mode` | field | `GLenum` | public | — |

### `GPlatesOpenGL::GLLineWidthStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLLineWidthStateSet( GLfloat width)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_width` | field | `GPlatesMaths::real_t` | public | — |

### `GPlatesOpenGL::GLLoadMatrixStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLLoadMatrixStateSet( GLenum mode, const GLMatrix &matrix)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_mode` | field | `GLenum` | public | — |
| `d_matrix` | field | `GLMatrix` | public | — |

### `GPlatesOpenGL::GLLoadTextureMatrixStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLLoadTextureMatrixStateSet( GLenum texture_unit, const GLMatrix &matrix)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_texture_unit` | field | `GLenum` | public | — |
| `d_matrix` | field | `GLMatrix` | public | — |

### `GPlatesOpenGL::GLMatrixModeStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLMatrixModeStateSet( GLenum mode)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_mode` | field | `GLenum` | public | — |

### `GPlatesOpenGL::GLNormalPointerStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLNormalPointerStateSet( GLenum type, GLsizei stride, GLint offset, const GLBufferObject::shared_ptr_to_const_type &buffer_object)` | constructor | `None` | public | Binds to a vertex buffer object. |
| `GLNormalPointerStateSet( GLenum type, GLsizei stride, GLint offset, const GLBufferImpl::shared_ptr_to_const_type &buffer_impl)` | constructor | `None` | public | No binding to a vertex buffer object (using client memory array). |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_buffer` | field | `Implementation::GLVertexAttributeBuffer` | private | — |
| `d_type` | field | `GLenum` | private | — |
| `d_stride` | field | `GLsizei` | private | — |

### `GPlatesOpenGL::GLPointSizeStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLPointSizeStateSet( GLfloat size)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_size` | field | `GPlatesMaths::real_t` | public | — |

### `GPlatesOpenGL::GLPolygonModeStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLPolygonModeStateSet( GLenum face, GLenum mode)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_face` | field | `GLenum` | public | — |
| `d_mode` | field | `GLenum` | public | — |

### `GPlatesOpenGL::GLPolygonOffsetStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLPolygonOffsetStateSet( GLfloat factor, GLfloat units)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_factor` | field | `GPlatesMaths::real_t` | public | — |
| `d_units` | field | `GPlatesMaths::real_t` | public | — |

### `GPlatesOpenGL::GLScissorStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `scissor_rectangle_seq_type` | typedef | `std::vector<GLViewport>` | public | Typedef for a sequence of scissor rectangles. |
| `GLScissorStateSet( const GLCapabilities &capabilities, const GLViewport &all_scissor_rectangles, const GLViewport &default_viewport)` | constructor | `None` | public | Constructor to set all scissor rectangles to the same parameters. |
| `GLScissorStateSet( const GLCapabilities &capabilities, const scissor_rectangle_seq_type &all_scissor_rectangles, const GLViewport &default_viewport)` | constructor | `None` | public | Constructor to set scissor rectangles individually. |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `get_scissor` | field | `GLViewport` | public | Returns scissor rectangle at index viewport\_index (default index is zero). |
| `d_scissor_rectangles` | field | `scissor_rectangle_seq_type` | private | Contains 'GLCapabilities::Viewport::gl\_max\_viewports' scissor rectangles. |
| `d_all_scissor_rectangles_are_the_same` | field | `bool` | private | Is true if all scissor rectangles in d\_scissor\_rectangles are the same. |
| `d_default_viewport` | field | `GLViewport` | private | Default viewport of window currently attached to the OpenGL context. |
| `apply_state( const GLCapabilities &capabilities)` | method | `void` | private | — |

### `GPlatesOpenGL::GLStencilFuncStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLStencilFuncStateSet( GLenum func, GLint ref, GLuint mask)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_func` | field | `GLenum` | public | — |
| `d_ref` | field | `GLint` | public | — |
| `d_mask` | field | `GLuint` | public | — |

### `GPlatesOpenGL::GLStencilMaskStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLStencilMaskStateSet( GLuint stencil)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_stencil` | field | `GLuint` | public | — |

### `GPlatesOpenGL::GLStencilOpStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLStencilOpStateSet( GLenum fail, GLenum zfail, GLenum zpass)` | constructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_fail` | field | `GLenum` | public | — |
| `d_zfail` | field | `GLenum` | public | — |
| `d_zpass` | field | `GLenum` | public | — |

### `GPlatesOpenGL::GLTexCoordPointerStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLTexCoordPointerStateSet( GLint size, GLenum type, GLsizei stride, GLint offset, const GLBufferObject::shared_ptr_to_const_type &buffer_object, GLenum texture_unit)` | constructor | `None` | public | Binds to a vertex buffer object. |
| `GLTexCoordPointerStateSet( GLint size, GLenum type, GLsizei stride, GLint offset, const GLBufferImpl::shared_ptr_to_const_type &buffer_impl, GLenum texture_unit)` | constructor | `None` | public | No binding to a vertex buffer object (using client memory array). |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_buffer` | field | `Implementation::GLVertexAttributeBuffer` | private | — |
| `d_size` | field | `GLint` | private | — |
| `d_type` | field | `GLenum` | private | — |
| `d_stride` | field | `GLsizei` | private | — |
| `d_texture_unit` | field | `GLenum` | private | — |

### `GPlatesOpenGL::GLTexGenStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLTexGenStateSet( GLenum texture_unit, GLenum coord, GLenum pname, ParamType param)` | constructor | `None` | public | 'ParamType' should be one of GLint, GLfloat, GLdouble, std::vector\<GLint\>, std::vector\<GLfloat\> or std::vector\<GLdouble\>. |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `param_data_types` | typedef | `boost::mpl::vector< GLint, GLfloat, GLdouble, std::vector<GLint>, std::vector<GLfloat>, std::vector<GLdouble> >` | private | The valid variant types. |
| `param_type` | typedef | `boost::make_variant_over<param_data_types>::type` | private | The boost::variant itself. |
| `DEFAULT_GEN_MODE` | field | `param_type` | private | — |
| `DEFAULT_S_PLANE` | field | `param_type` | private | — |
| `DEFAULT_T_PLANE` | field | `param_type` | private | — |
| `DEFAULT_R_AND_Q_PLANE` | field | `param_type` | private | — |
| `d_texture_unit` | field | `GLenum` | private | — |
| `d_coord` | field | `GLenum` | private | — |
| `d_pname` | field | `GLenum` | private | — |
| `d_param` | field | `param_type` | private | — |
| `initialise_plane( const GLdouble &x, const GLdouble &y, const GLdouble &z, const GLdouble &w)` | method | `param_type` | private | — |
| `get_default_param()` | method | `param_type` | private | Returns the default param\_type for 'this' state. |

### `GPlatesOpenGL::GLTexEnvStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLTexEnvStateSet( GLenum texture_unit, GLenum target, GLenum pname, ParamType param)` | constructor | `None` | public | 'ParamType' should be one of GLint, GLfloat, std::vector\<GLint\> or std::vector\<GLfloat\>. |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `param_data_types` | typedef | `boost::mpl::vector<GLint, GLfloat, std::vector<GLint>, std::vector<GLfloat> >` | private | The valid variant types. |
| `param_type` | typedef | `boost::make_variant_over<param_data_types>::type` | private | The boost::variant itself. |
| `d_texture_unit` | field | `GLenum` | private | — |
| `d_target` | field | `GLenum` | private | — |
| `d_pname` | field | `GLenum` | private | — |
| `d_param` | field | `param_type` | private | — |
| `get_default_param()` | method | `param_type` | private | Returns the default param\_type for 'this' state. |

### `GPlatesOpenGL::GLVertexAttribPointerStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VertexAttribAPIType` | enum | `None` | public | The vertex attribute API to use... |
| `GLVertexAttribPointerStateSet( const GLCapabilities &capabilities, GLuint attribute_index, VertexAttribAPIType vertex_attrib_api, GLint size, GLenum type, // Only used for 'VERTEX_ATTRIB_POINTER', not 'VERTEX_ATTRIB_I_POINTER' or 'VERTEX_ATTRIB_L_POINTER'... boost::optional<GLboolean> normalized, GLsizei stride, GLint ...` | constructor | `None` | public | Binds to a vertex buffer object. |
| `GLVertexAttribPointerStateSet( const GLCapabilities &capabilities, GLuint attribute_index, VertexAttribAPIType vertex_attrib_api, GLint size, GLenum type, // Only used for 'VERTEX_ATTRIB_POINTER', not 'VERTEX_ATTRIB_I_POINTER' or 'VERTEX_ATTRIB_L_POINTER'... boost::optional<GLboolean> normalized, GLsizei stride, GLint ...` | constructor | `None` | public | No binding to a vertex buffer object (using client memory array). |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_buffer` | field | `Implementation::GLVertexAttributeBuffer` | private | — |
| `d_attribute_index` | field | `GLuint` | private | — |
| `d_vertex_attrib_api` | field | `VertexAttribAPIType` | private | — |
| `d_size` | field | `GLint` | private | — |
| `d_type` | field | `GLenum` | private | — |
| `d_normalized` | field | `boost::optional<GLboolean>` | private | Is optional since only used for 'glVertexAttribPointer' but not 'glVertexAttribIPointer' or 'glVertexAttribLPointer'... |
| `d_stride` | field | `GLsizei` | private | — |

### `GPlatesOpenGL::GLVertexPointerStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLVertexPointerStateSet( GLint size, GLenum type, GLsizei stride, GLint offset, const GLBufferObject::shared_ptr_to_const_type &buffer_object)` | constructor | `None` | public | Binds to a vertex buffer object. |
| `GLVertexPointerStateSet( GLint size, GLenum type, GLsizei stride, GLint offset, const GLBufferImpl::shared_ptr_to_const_type &buffer_impl)` | constructor | `None` | public | No binding to a vertex buffer object (using client memory array). |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `d_buffer` | field | `Implementation::GLVertexAttributeBuffer` | private | — |
| `d_size` | field | `GLint` | private | — |
| `d_type` | field | `GLenum` | private | — |
| `d_stride` | field | `GLsizei` | private | — |

### `GPlatesOpenGL::GLViewportStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `viewport_seq_type` | typedef | `std::vector<GLViewport>` | public | Typedef for a sequence of viewports. |
| `GLViewportStateSet( const GLCapabilities &capabilities, const GLViewport &all_viewports, const GLViewport &default_viewport)` | constructor | `None` | public | Constructor to set all viewport to the same parameters. |
| `GLViewportStateSet( const GLCapabilities &capabilities, const viewport_seq_type &all_viewports, const GLViewport &default_viewport)` | constructor | `None` | public | Constructor to set viewports individually. |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | — |
| `get_viewport` | field | `GLViewport` | public | Returns viewport at index viewport\_index (default index is zero). |
| `d_viewports` | field | `viewport_seq_type` | private | Contains 'GLCapabilities::Viewport::gl\_max\_viewports' viewports. |
| `d_all_viewports_are_the_same` | field | `bool` | private | Is true if all viewports in viewports are the same. |
| `d_default_viewport` | field | `GLViewport` | private | Default viewport of window currently attached to the OpenGL context. |
| `apply_state( const GLCapabilities &capabilities)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `set_matrix_mode( GLenum mode, GLState &last_applied_state)` | function | `void` | Ensures the matrix mode is set to matrix mode and changes it if necessary. |
| `set_active_texture( const GLCapabilities &capabilities, GLenum texture_unit, GLState &last_applied_state)` | function | `void` | Ensures the active texture unit is set to texture\_unit and changes it if necessary. |
| `set_client_active_texture( const GLCapabilities &capabilities, GLenum texture_unit, GLState &last_applied_state)` | function | `void` | Ensures the client active texture unit is set to texture\_unit and changes it if necessary. |
| `bind_buffer_object( const GLCapabilities &capabilities, GLBufferObject::resource_handle_type buffer_object_resource, const GLBufferObject::shared_ptr_to_const_type &buffer_object, GLenum target, GLState &last_applied_state)` | function | `void` | Ensures the currently bound buffer object (for its target type) is buffer\_object\_resource. |
| `unbind_buffer_object( const GLCapabilities &capabilities, GLenum target, GLState &last_applied_state)` | function | `void` | Ensures there is no currently bound buffer object for the specified target type. |
| `create_4_vector( const Type &x, const Type &y, const Type &z, const Type &w)` | function | `std::vector<Type>` | Converts an array of 4 numbers into a std::vector. |
| `DEFAULT_DEPTH_RANGE` | variable | `GPlatesOpenGL::GLDepthRange` | — |
| `DEFAULT_GEN_MODE` | variable | `GPlatesOpenGL::GLTexGenStateSet::param_type` | — |
| `DEFAULT_S_PLANE` | variable | `GPlatesOpenGL::GLTexGenStateSet::param_type` | — |
| `DEFAULT_T_PLANE` | variable | `GPlatesOpenGL::GLTexGenStateSet::param_type` | — |
| `DEFAULT_R_AND_Q_PLANE` | variable | `GPlatesOpenGL::GLTexGenStateSet::param_type` | — |
| `GPLATES_OPENGL_GLSTATESETS_H` | macro | `None` | — |

## Notes

**The contract for a new state set.** Instances must be immutable and are shared between `GLState` objects, so `apply_*` are `const` and must stay repeatable — the same object can be applied many times and must produce the same OpenGL state each time. `apply_state` receives a `const GLStateSet &` that the caller guarantees is the same derived type; every implementation here `dynamic_cast`s it and lets the cast throw if that guarantee is ever broken. Adding a state set also means adding a key in `GLStateSetKeys`, a pool in `GLStateSetStore`, and, if it can touch state outside its own slot, an entry in `GLState::SharedData::initialise_dependent_state_set_slots` — a dependent state set that is not registered there can be silently overridden by a later slot in the same pass.

**Mutable exceptions to immutability.** All the vertex array pointer slots (`GLVertexPointerStateSet`, `GLColorPointerStateSet`, `GLNormalPointerStateSet`, the per-unit `GLTexCoordPointerStateSet`s and the generic `GLVertexAttribPointerStateSet`s) are registered as *mutable* in `GLState::SharedData::initialise_mutable_state_set_slots`, which disables the pointer-equality shortcut for them. The reason is in `GLVertexAttributeBuffer::has_changed_state`: the same state set object can need re-application because the client memory pointer moved, or because `glBufferData` reallocated the buffer. The `UPDATE` comment records that this was found to be needed for native buffer objects too, not just emulated ones — ATI hardware required vertex array pointers to be rebound after `glBufferData` where nVidia did not — so the mutable marking is applied unconditionally, and the `GLState` header comment claiming it applies only without `GL_ARB_vertex_buffer_object` is stale.

**Change detection is a choice, not an obligation.** `GLStateSet` explicitly permits a state set to skip comparison and just apply, on the grounds that a redundant GL call is cheaper than an expensive comparison. `GLViewportStateSet` and `GLScissorStateSet` take that option: they compare only when both sides hold a single rectangle for all viewports, and re-apply unconditionally otherwise.

**Constructor-time validation.** Texture unit and viewport-count arguments are checked against `GLCapabilities` in the constructors, not at apply time — `GLBindTextureStateSet` against `gl_max_texture_image_units`, the array-form `GLViewportStateSet` requiring *exactly* `gl_max_viewports` rectangles. The failure therefore surfaces where the state was set, in the caller's frame, not later inside `apply_state`.

**Compile-time gating is separate from runtime capability.** Several apply paths sit inside `#ifdef GL_ARB_vertex_array_object` / `#ifdef GL_ARB_viewport_array` guards against an old `glew.h`, *in addition* to the runtime `GLCapabilities` test. The two guards behave differently: the vertex-array-object paths have an `#else` that throws `OpenGLException`, whereas the multi-viewport paths simply fall through and do nothing. Both conditions have to hold before the extension path is taken.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLState](GLState.md) | opengl | 52 |
| [opengl/GLStateSetStore](GLStateSetStore.md) | opengl | 45 |
| [opengl/GLTexture](GLTexture.md) | opengl | 10 |
| [app-logic/ApplicationState](../app-logic/ApplicationState.md) | app-logic | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLStateSets.h
python scripts/gpq.py def GPlatesOpenGL::Implementation::GLVertexAttributeBuffer --body
python scripts/gpq.py uses GLVertexAttributeBuffer --kind class
python scripts/gpq.py hier GLVertexAttributeBuffer
```

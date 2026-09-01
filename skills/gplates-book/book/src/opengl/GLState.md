# GLState

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 51 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLState.h` | C++ | 1857 |
| `src/opengl/GLState.cc` | C++ | 1061 |

## Overview

`GLState` is the data structure behind `GLRenderer`'s deferred state model: a snapshot of the whole OpenGL state expressed as a sparse array of immutable `GLStateSet` objects, one per slot, indexed by a `GLStateSetKeys::key_type`. An empty slot *means* the OpenGL default for that piece of state, so a freshly allocated `GLState` is the default state and nothing has to be written out to represent it. Every `set_*` method builds a new state set in the matching `GPlatesUtils::ObjectPool` inside `GLStateSetStore` and drops the pointer into its slot; because the state sets are immutable and shared, `clone()` is a pointer copy of the occupied slots rather than a deep copy, which is what makes `GLRenderer`'s per-state-block cloning affordable.

The interesting method is `apply_state`. It takes the caller's model of what OpenGL currently looks like (`last_applied_state`, owned by `GLRenderer`) and walks the slots in key order, letting each `GLStateSet` emit only the transition it needs: `apply_state` between two set states, `apply_from_default_state` when the slot was empty, `apply_to_default_state` when it is now empty. Two shortcuts do the filtering work. Identical `GLStateSet` pointers in both states mean no possible difference, so the slot is skipped without a virtual call; and the slot-occupancy bitmask (`d_state_set_slots`, packed 32 slots to a `boost::uint32_t`) lets thirty-two untouched slots be dismissed with one integer test — which matters because the slot count grew from roughly 250 to roughly 750 when the state sets were extended to 32 shader-era texture units, most of which are never used. Slots are visited in key order deliberately: the ordering keeps related state adjacent, so binding and enabling on the same texture unit does not thrash the active texture unit.

Three complications sit on top. `SharedData`, allocated once per `GLStateStore` and shared by every `GLState`, precomputes the slot masks that the special-cased passes need: which slots are *dependent* state sets (ones another state set can modify while it applies — the active texture unit is the example, which is why `apply_state` runs two passes, non-dependent first), which slots are vertex-array state that a native vertex array object records, which subsets `glClear` and `glReadPixels` actually consult, and which rare slots are mutable rather than immutable. Second, vertex array objects are bound first and then re-shadowed afterwards by `end_bind_vertex_array_object`, so `GLState` keeps a mirror of what the bound VAO has actually recorded. Third, `merge_state_change` exists for `GLCompiledDrawState`: it copies only the *set* slots, treating the argument as a delta on top of the current state, where `copy_vertex_array_state` copies set and unset slots alike within the vertex-array mask.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLState`](#gplatesopenglglstate) | class | `boost::noncopyable` | — | 0 | Contains a snapshot of the global state of OpenGL. |

## Members

### `GPlatesOpenGL::GLState`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `state_set_slot_flag32_type` | typedef | `boost::uint32_t` | private | Typedef for a group of 32 boolean flags indicating if 32 state set slots have been initialised. |
| `state_set_slot_flags_type` | typedef | `std::vector<state_set_slot_flag32_type>` | private | Typedef for a set of flags indicating which state set slots have been initialised. |
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLState>` | public | A convenience typedef for a shared pointer to a GLState. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLState>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<GLState>` | public | A convenience typedef for a weak pointer to a GLState. |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const GLState>` | public | — |
| `SharedData` | class | `None` | public | Constant data that is shared across GLState instances. |
| `create( const GLStateSetStore::non_null_ptr_type &state_set_store, const GLStateSetKeys::non_null_ptr_to_const_type &state_set_keys, const SharedData::shared_ptr_to_const_type &shared_data, const boost::weak_ptr<GLStateStore> &state_store = boost::weak_ptr<GLStateStore>())` | method | `shared_ptr_type` | public | Creates a GLState object - call 'GLStateStore::allocate\_state()' instead. |
| `create_as_unique_ptr( const GLStateSetStore::non_null_ptr_type &state_set_store, const GLStateSetKeys::non_null_ptr_to_const_type &state_set_keys, const SharedData::shared_ptr_to_const_type &shared_data, const boost::weak_ptr<GLStateStore> &state_store = boost::weak_ptr<GLStateStore>())` | method | `std::unique_ptr<GLState>` | public | Same as create but returns a std::unique\_ptr - to guarantee only one owner. |
| `clone()` | method | `shared_ptr_type` | public | Creates a copy of this object that shares the same immutable state sets. |
| `clear()` | method | `void` | public | Clears references to GLStateSet objects such that 'this' object behaves the same as a newly allocated GLState object. |
| `apply_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | Applies the current state (internal to 'this' object). last\_applied\_state is the last applied state (ie, it represents the current state as seen by the OpenGL library). |
| `apply_state_used_by_gl_clear( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | The same as apply\_state except only those GLStateSet's needed by 'glClear' are applied. |
| `apply_state_used_by_gl_read_pixels( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | The same as apply\_state except only those GLStateSet's needed by 'glReadPixels' are applied. |
| `merge_state_change( const GLState &state_change)` | method | `void` | public | Merges the specified state change into 'this' state. |
| `copy_vertex_array_state( const GLState &state)` | method | `void` | public | Copies the state-sets of state that represent vertex array state into 'this'. |
| `set_color_mask( GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha)` | method | `void` | public | Sets the OpenGL colour mask. |
| `set_depth_mask( GLboolean flag)` | method | `void` | public | Sets the OpenGL depth mask. |
| `get_depth_mask()` | method | `GLboolean` | public | Returns the current depth mask. |
| `set_stencil_mask( GLuint stencil)` | method | `void` | public | Sets the OpenGL stencil mask. |
| `get_stencil_mask()` | method | `GLuint` | public | Returns the current stencil mask. |
| `set_clear_color( GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha)` | method | `void` | public | Sets the OpenGL clear colour. |
| `set_clear_depth( GLclampd depth)` | method | `void` | public | Sets the OpenGL clear depth value. |
| `set_clear_stencil( GLint stencil)` | method | `void` | public | Sets the OpenGL clear stencil value. |
| `set_bind_frame_buffer( const GLFrameBufferObject::shared_ptr_to_const_type &frame_buffer_object)` | method | `void` | public | Sets the framebuffer object to bind to the active OpenGL context. |
| `set_bind_frame_buffer_and_apply( const GLCapabilities &capabilities, const GLFrameBufferObject::shared_ptr_to_const_type &frame_buffer_object, GLState &last_applied_state)` | method | `void` | public | Same as set\_bind\_frame\_buffer but also applies directly to OpenGL. |
| `set_unbind_frame_buffer()` | method | `void` | public | Unbinds any framebuffer object currently bound. |
| `set_unbind_frame_buffer_and_apply( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | Same as set\_unbind\_frame\_buffer but also applies directly to OpenGL. |
| `get_bind_frame_buffer()` | method | `boost::optional<GLFrameBufferObject::shared_ptr_to_const_type>` | public | Returns the framebuffer object to bind to the active OpenGL context - boost::none implies default main framebuffer. |
| `set_bind_program_object( const GLProgramObject::shared_ptr_to_const_type &program_object)` | method | `void` | public | Sets the shader program object to bind to the active OpenGL context. |
| `set_bind_program_object_and_apply( const GLCapabilities &capabilities, const GLProgramObject::shared_ptr_to_const_type &program_object, GLState &last_applied_state)` | method | `void` | public | Same as set\_bind\_program\_object but also applies directly to OpenGL. |
| `set_unbind_program_object()` | method | `void` | public | Unbinds any shader program object currently bound. |
| `set_unbind_program_object_and_apply( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | Same as set\_unbind\_program\_object but also applies directly to OpenGL. |
| `get_bind_program_object()` | method | `boost::optional<GLProgramObject::shared_ptr_to_const_type>` | public | Returns the shader program object bound (or to bind if not yet applied) to the active OpenGL context. boost::none implies fixed-function pipeline. |
| `set_bind_texture( const GLCapabilities &capabilities, const GLTexture::shared_ptr_to_const_type &texture_object, GLenum texture_unit, GLenum texture_target)` | method | `void` | public | Sets the texture bound on the specified target and texture unit. |
| `set_bind_texture_and_apply( const GLCapabilities &capabilities, const GLTexture::shared_ptr_to_const_type &texture_object, GLenum texture_unit, GLenum texture_target, GLState &last_applied_state)` | method | `void` | public | Same as set\_bind\_texture but also applies directly to OpenGL. |
| `set_unbind_texture( const GLCapabilities &capabilities, GLenum texture_unit, GLenum texture_target)` | method | `void` | public | Unbinds any texture object currently bound to the specified target and texture unit. |
| `set_unbind_texture_and_apply( const GLCapabilities &capabilities, GLenum texture_unit, GLenum texture_target, GLState &last_applied_state)` | method | `void` | public | Same as set\_unbind\_texture but also applies directly to OpenGL. |
| `get_bind_texture( GLenum texture_unit, GLenum texture_target)` | method | `boost::optional<GLTexture::shared_ptr_to_const_type>` | public | Returns the texture bound on the specified target and texture unit - boost::none implies the default no binding. |
| `set_bind_vertex_array_object( GLVertexArrayObject::resource_handle_type resource_handle, const shared_ptr_type &current_resource_state, const shared_ptr_to_const_type &target_resource_state, // NOTE: This is *only* here for @a get_bind_vertex_array_object and to keep it alive until rendered. // The resource handle is w ...` | method | `void` | public | Binds the vertex array object to the active OpenGL context. |
| `set_bind_vertex_array_object_and_apply( const GLCapabilities &capabilities, GLVertexArrayObject::resource_handle_type resource_handle, const shared_ptr_type &current_resource_state, const shared_ptr_to_const_type &target_resource_state, // NOTE: This is *only* here for @a get_bind_vertex_array_object and to keep it ali ...` | method | `void` | public | Same as set\_bind\_vertex\_array\_object but also applies directly to OpenGL. |
| `set_unbind_vertex_array_object()` | method | `void` | public | Unbinds any vertex array object currently bound. |
| `get_bind_vertex_array_object()` | method | `boost::optional<GLVertexArrayObject::shared_ptr_to_const_type>` | public | Returns the currently bound vertex array object - boost::none implies the default no binding. |
| `set_bind_buffer_object( const GLBufferObject::shared_ptr_to_const_type &buffer_object, GLenum target)` | method | `void` | public | Binds the buffer object (at the specified target) to the active OpenGL context. |
| `set_bind_buffer_object_and_apply( const GLCapabilities &capabilities, const GLBufferObject::shared_ptr_to_const_type &buffer_object, GLenum target, GLState &last_applied_state)` | method | `void` | public | Same as set\_bind\_buffer\_object but also applies directly to OpenGL. |
| `set_unbind_buffer_object( GLenum target)` | method | `void` | public | Unbinds any buffer object currently bound at the specified target. |
| `set_unbind_buffer_object_and_apply( const GLCapabilities &capabilities, GLenum target, GLState &last_applied_state)` | method | `void` | public | Same as set\_unbind\_buffer\_object but also applies directly to OpenGL. |
| `get_bind_buffer_object( GLenum target)` | method | `boost::optional<GLBufferObject::shared_ptr_to_const_type>` | public | Returns the bound buffer object, or boost::none if no object bound. |
| `get_bind_buffer_object_resource( GLenum target)` | method | `boost::optional<GLBufferObject::resource_handle_type>` | public | Returns the bound buffer object resource, or boost::none if no object bound. |
| `set_scissor( const GLCapabilities &capabilities, const GLViewport &scissor, const GLViewport &default_viewport)` | method | `void` | public | Sets all scissor rectangles to the same parameters. default\_viewport is the viewport of the window attached to the OpenGL context. |
| `set_scissor_array( const GLCapabilities &capabilities, const std::vector<GLViewport> &all_scissor_rectangles, const GLViewport &default_viewport)` | method | `void` | public | Sets all scissor rectangles to the parameters specified in all\_scissor\_rectangles. default\_viewport is the viewport of the window attached to the OpenGL context. |
| `get_scissor( const GLCapabilities &capabilities, unsigned int viewport_index)` | method | `boost::optional<const GLViewport &>` | public | Returns the scissor rectangle for the specified viewport index. |
| `set_viewport( const GLCapabilities &capabilities, const GLViewport &viewport, const GLViewport &default_viewport)` | method | `void` | public | Sets all viewports to the same parameters. default\_viewport is the viewport of the window attached to the OpenGL context. |
| `set_viewport_array( const GLCapabilities &capabilities, const std::vector<GLViewport> &all_viewports, const GLViewport &default_viewport)` | method | `void` | public | Sets all viewports to the parameters specified in all\_viewports. default\_viewport is the viewport of the window attached to the OpenGL context. |
| `get_viewport( const GLCapabilities &capabilities, unsigned int viewport_index)` | method | `boost::optional<const GLViewport &>` | public | Returns the viewport for the specified viewport index. |
| `set_depth_range( const GLCapabilities &capabilities, const GLDepthRange &depth_range)` | method | `void` | public | Sets all depth ranges to the same parameters. |
| `set_depth_range_array( const GLCapabilities &capabilities, const std::vector<GLDepthRange> &all_depth_ranges)` | method | `void` | public | Sets all depth ranges to the parameters specified in all\_depth\_ranges. |
| `set_stencil_func( GLenum func, GLint ref, GLuint mask)` | method | `void` | public | Sets the stencil function. |
| `set_stencil_op( GLenum fail, GLenum zfail, GLenum zpass)` | method | `void` | public | Sets the stencil operation. |
| `set_enable( GLenum cap, bool enable)` | method | `void` | public | Enable/disable a capability - \*except\* texturing (use set\_enable\_texture for that). |
| `get_enable( GLenum cap)` | method | `bool` | public | Returns true if the specified capability is currently enabled. |
| `set_enable_texture( GLenum texture_unit, GLenum texture_target, bool enable)` | method | `void` | public | Enable/disable texturing for the specified target and texture unit. |
| `set_point_size( GLfloat size)` | method | `void` | public | Specify point size. |
| `set_line_width( GLfloat width)` | method | `void` | public | Specify line width. |
| `set_polygon_mode( GLenum face, GLenum mode)` | method | `void` | public | Specify polygon mode. |
| `set_front_face( GLenum mode)` | method | `void` | public | — |
| `set_cull_face( GLenum mode)` | method | `void` | public | — |
| `set_polygon_offset( GLfloat factor, GLfloat units)` | method | `void` | public | — |
| `set_hint( GLenum target, GLenum mode)` | method | `void` | public | Specify a hint. |
| `set_alpha_func( GLenum func, GLclampf ref)` | method | `void` | public | Sets the alpha test function. |
| `set_blend_equation( const GLCapabilities &capabilities, GLenum mode)` | method | `void` | public | Sets the alpha-blend equation (glBlendEquation). |
| `set_blend_equation_separate( const GLCapabilities &capabilities, GLenum modeRGB, GLenum modeAlpha)` | method | `void` | public | Sets the alpha-blend equation (glBlendEquationSeparate). |
| `set_blend_func( GLenum sfactor, GLenum dfactor)` | method | `void` | public | Sets the alpha-blend function (glBlendFunc). |
| `set_blend_func_separate( const GLCapabilities &capabilities, GLenum sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha)` | method | `void` | public | Sets the alpha-blend function (glBlendFuncSeparate). |
| `set_depth_func( GLenum func)` | method | `void` | public | Set the depth function. |
| `set_active_texture( const GLCapabilities &capabilities, GLenum active_texture)` | method | `void` | public | Sets the active texture unit. |
| `get_active_texture()` | method | `GLenum` | public | Returns the active texture unit. |
| `set_client_active_texture( const GLCapabilities &capabilities, GLenum client_active_texture)` | method | `void` | public | Sets the client active texture unit. |
| `get_client_active_texture()` | method | `GLenum` | public | Returns the client active texture unit. |
| `set_tex_env( GLenum texture_unit, GLenum target, GLenum pname, const ParamType &param)` | method | `void` | public | Sets the specified texture environment state to the specified parameter on the specified texture unit. |
| `set_tex_gen( GLenum texture_unit, GLenum coord, GLenum pname, const ParamType &param)` | method | `void` | public | Sets the specified texture coordinate generation state to the specified parameter on the specified texture unit. |
| `set_enable_client_state( GLenum array, bool enable)` | method | `void` | public | Enables the specified (array) vertex array (in the fixed-function pipeline). |
| `set_enable_client_texture_state( GLenum texture_unit, bool enable)` | method | `void` | public | Enables the vertex attribute array GL\_TEXTURE\_COORD\_ARRAY on the specified texture unit. |
| `set_vertex_pointer( GLint size, GLenum type, GLsizei stride, GLint offset, const GLBufferObject::shared_ptr_to_const_type &buffer_object)` | method | `void` | public | Specify the source of vertex position data (from a buffer object). |
| `set_vertex_pointer( GLint size, GLenum type, GLsizei stride, GLint offset, const GLBufferImpl::shared_ptr_to_const_type &buffer_impl)` | method | `void` | public | Specify the source of vertex position data (from client memory). |
| `set_color_pointer( GLint size, GLenum type, GLsizei stride, GLint offset, const GLBufferObject::shared_ptr_to_const_type &buffer_object)` | method | `void` | public | Specify the source of vertex color data (from a buffer object). |
| `set_color_pointer( GLint size, GLenum type, GLsizei stride, GLint offset, const GLBufferImpl::shared_ptr_to_const_type &buffer_impl)` | method | `void` | public | Specify the source of vertex color data (from client memory). |
| `set_normal_pointer( GLenum type, GLsizei stride, GLint offset, const GLBufferObject::shared_ptr_to_const_type &buffer_object)` | method | `void` | public | Specify the source of vertex normal data (from a buffer object). |
| `set_normal_pointer( GLenum type, GLsizei stride, GLint offset, const GLBufferImpl::shared_ptr_to_const_type &buffer_impl)` | method | `void` | public | Specify the source of vertex normal data (from client memory). |
| `set_tex_coord_pointer( GLint size, GLenum type, GLsizei stride, GLint offset, const GLBufferObject::shared_ptr_to_const_type &buffer_object, GLenum texture_unit)` | method | `void` | public | Specify the source of vertex texture coordinate data (from a buffer object). |
| `set_tex_coord_pointer( GLint size, GLenum type, GLsizei stride, GLint offset, const GLBufferImpl::shared_ptr_to_const_type &buffer_impl, GLenum texture_unit)` | method | `void` | public | Specify the source of vertex texture coordinate data (from client memory). |
| `set_enable_vertex_attrib_array( GLuint attribute_index, bool enable)` | method | `void` | public | Enables the specified \*generic\* vertex attribute array (for use in a shader program). |
| `set_vertex_attrib_pointer( const GLCapabilities &capabilities, GLuint attribute_index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, GLint offset, const GLBufferObject::shared_ptr_to_const_type &buffer_object)` | method | `void` | public | Specify the source of \*generic\* vertex attribute array (for use in a shader program "from a buffer object"). |
| `set_vertex_attrib_pointer( const GLCapabilities &capabilities, GLuint attribute_index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, GLint offset, const GLBufferImpl::shared_ptr_to_const_type &buffer_impl)` | method | `void` | public | Specify the source of \*generic\* vertex attribute array (for use in a shader program "from client memory"). |
| `set_vertex_attrib_i_pointer( const GLCapabilities &capabilities, GLuint attribute_index, GLint size, GLenum type, GLsizei stride, GLint offset, const GLBufferObject::shared_ptr_to_const_type &buffer_object)` | method | `void` | public | Same as set\_vertex\_attrib\_pointer except used to specify attributes mapping to \*integer\* shader variables. |
| `set_vertex_attrib_i_pointer( const GLCapabilities &capabilities, GLuint attribute_index, GLint size, GLenum type, GLsizei stride, GLint offset, const GLBufferImpl::shared_ptr_to_const_type &buffer_impl)` | method | `void` | public | Same as set\_vertex\_attrib\_pointer except used to specify attributes mapping to \*integer\* shader variables. |
| `set_vertex_attrib_l_pointer( const GLCapabilities &capabilities, GLuint attribute_index, GLint size, GLenum type, GLsizei stride, GLint offset, const GLBufferObject::shared_ptr_to_const_type &buffer_object)` | method | `void` | public | Same as set\_vertex\_attrib\_pointer except used to specify attributes mapping to \*double\* shader variables. |
| `set_vertex_attrib_l_pointer( const GLCapabilities &capabilities, GLuint attribute_index, GLint size, GLenum type, GLsizei stride, GLint offset, const GLBufferImpl::shared_ptr_to_const_type &buffer_impl)` | method | `void` | public | Same as set\_vertex\_attrib\_pointer except used to specify attributes mapping to \*double\* shader variables. |
| `set_matrix_mode( GLenum mode)` | method | `void` | public | Specifies which matrix stack is the target for matrix operations. |
| `get_matrix_mode()` | method | `GLenum` | public | Returns the matrix stack targeted for matrix operations. |
| `set_load_matrix( GLenum mode, const GLMatrix &matrix)` | method | `void` | public | Loads the specified matrix into the specified matrix mode. |
| `get_load_matrix( GLenum mode)` | method | `boost::optional<const GLMatrix &>` | public | Returns the matrix for the specified matrix mode. |
| `set_load_texture_matrix( GLenum texture_unit, const GLMatrix &matrix)` | method | `void` | public | Loads the specified texture matrix into the specified texture unit. |
| `get_load_texture_matrix( GLenum texture_unit)` | method | `boost::optional<const GLMatrix &>` | public | Returns the texture matrix for the specified texture unit. |
| `state_set_key_type` | typedef | `GLStateSetKeys::key_type` | private | Typedef for a state set key. |
| `immutable_state_set_ptr_type` | typedef | `boost::shared_ptr<const GLStateSet>` | private | Typedef for a shared pointer to an immutable GLStateSet. |
| `state_set_seq_type` | typedef | `std::vector<immutable_state_set_ptr_type>` | private | Typedef for a sequence of immutable GLStateSet pointers. |
| `d_state_set_store` | field | `GLStateSetStore::non_null_ptr_type` | private | — |
| `d_state_set_keys` | field | `GLStateSetKeys::non_null_ptr_to_const_type` | private | — |
| `d_state_store` | field | `boost::weak_ptr<GLStateStore>` | private | Used to efficiently allocate new GLState objects when cloning. |
| `d_state_sets` | field | `state_set_seq_type` | private | Contains the actual state sets indexed by state\_set\_key\_type. |
| `d_state_set_slots` | field | `state_set_slot_flags_type` | private | A flag for each state set (indexed by state set key). |
| `d_shared_data` | field | `SharedData::shared_ptr_to_const_type` | private | Constant data that is shared by all GLState instances (allocated by our state store). |
| `GLState( const GLStateSetStore::non_null_ptr_type &state_set_store, const GLStateSetKeys::non_null_ptr_to_const_type &state_set_keys, const SharedData::shared_ptr_to_const_type &shared_data, const boost::weak_ptr<GLStateStore> &state_store)` | constructor | `None` | private | Default constructor. |
| `set_state_set( GPlatesUtils::ObjectPool<GLStateSetType> &state_set_pool, state_set_key_type state_set_key, const InPlaceFactoryType &state_set_constructor_args)` | method | `void` | private | Sets a derived GLStateSet type at the specified state set key slot. |
| `get_state_set_query( state_set_key_type state_set_key, QueryMemberDataType GLStateSetType::*query_member)` | method | `boost::optional<QueryReturnType>` | private | Returns a derived GLStateSet type at the specified state set key slot. |
| `get_state_set_query( state_set_key_type state_set_key, const QueryFunctionType &query_function)` | method | `boost::optional<QueryReturnType>` | private | Returns a derived GLStateSet type at the specified state set key slot. |
| `apply_state( const GLCapabilities &capabilities, GLState &last_applied_state, const state_set_slot_flags_type &state_set_slots_mask)` | method | `void` | private | Applies 'this' state (from last\_applied\_state) for the specified state-set slots. |
| `apply_state( const GLCapabilities &capabilities, GLState &last_applied_state, state_set_key_type state_set_slot_to_apply)` | method | `void` | private | Applies 'this' state (from last\_applied\_state) for the specified \*single\* state-set slot. |
| `begin_bind_vertex_array_object( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | private | Bind (or unbind) a vertex array object if necessary. |
| `end_bind_vertex_array_object( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | private | Update the shadowed state of the currently bound vertex array object to mirror any vertex array state set after begin\_bind\_vertex\_array\_object. |
| `get_num_state_set_slot_flag32s( const GLStateSetKeys &state_set_keys)` | method | `unsigned int` | private | Returns the number of groups of 32 state-set slots required. |
| `is_state_set_slot_set( state_set_slot_flags_type &state_set_slots, state_set_key_type state_set_slot)` | method | `bool` | private | Returns true if the specified state set slot flag is set. |
| `set_state_set_slot_flag( state_set_slot_flags_type &state_set_slots, state_set_key_type state_set_slot)` | method | `void` | private | Sets the specified state set slot flag. |
| `clear_state_set_slot_flag( state_set_slot_flags_type &state_set_slots, state_set_key_type state_set_slot)` | method | `void` | private | Clears the specified state set slot flag. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLSTATE_H` | macro | `None` | — |

## Notes

**Empty slot means default.** This is the invariant everything else rests on. A slot must never hold a state set that encodes the default value where an empty slot would do, or the filtering will emit redundant calls; conversely, clearing a slot is how you say "return this to the OpenGL default", and `apply_state` will call `apply_to_default_state` on the *previous* state set to get there.

**`apply_state` is `const` but mutates its argument.** On return, `last_applied_state` has been rewritten to equal `*this`. It is the caller's model of the driver, so if you call `apply_state` and the GL calls do not actually happen, the model silently desynchronises for the rest of the frame.

**Allocation.** Do not call `create` directly — `GLStateStore::allocate_state()` recycles instances through a `GPlatesUtils::ObjectCache`, which is why `shared_ptr` is used here rather than `non_null_intrusive_ptr`. The store is held as a `boost::weak_ptr`, and `clone()` degrades to a plain heap allocation if the store has already gone; correctness is unaffected, performance is not. Note that recycled instances come back via `clear()`, so `clear()` must leave the object indistinguishable from a fresh one.

**Immutability has exceptions.** `SharedData::mutable_state_set_slots` marks the few state sets that can change internally — currently only the emulated buffer objects used when `GL_ARB_vertex_buffer_object` is missing. For those slots the pointer-equality shortcut is deliberately bypassed, so a state set that changes behind its pointer must be registered there or its change will be filtered away.

**Two-pass application is load-bearing.** Adding a state set whose `apply_state` touches state outside its own slot means adding it to the dependent-slot mask in `SharedData::initialise_dependent_state_set_slots`; otherwise the single pass that includes it can be overridden by a later slot. The code assumes dependent state sets do not themselves modify others — a third pass would be needed if that stopped holding.

**Do not hold on to state sets.** The header is explicit: a `GLStateSet` cannot outlive the `GLStateSetStore` object pool it came from, which is why the accessors return copied values or `boost::optional` references rather than shared pointers.

**Performance is the reason for the shape of this code.** `clone`, `clear`, `merge_state_change`, `copy_vertex_array_state` and both `apply_state` overloads are all hand-unrolled bit-scan loops carrying `PROFILE_FUNC` markers, written that way because state application shows high on the CPU profile on paths such as raster reconstruction with age-grid smoothing. Rewriting any of them for clarity is a measurable regression, not a neutral cleanup.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLStateSets](GLStateSets.md) | opengl | 152 |
| [opengl/GLRenderer](GLRenderer.md) | opengl | 115 |
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 36 |
| [opengl/GLVertex](GLVertex.md) | opengl | 30 |
| [opengl/GLStateStore](GLStateStore.md) | opengl | 22 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 18 |
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 10 |
| [opengl/GLRendererImpl](GLRendererImpl.md) | opengl | 4 |
| [gui/FeedbackOpenGLToQPainter](../gui/FeedbackOpenGLToQPainter.md) | gui | 2 |
| [opengl/GLVertexArrayObject](GLVertexArrayObject.md) | opengl | 2 |
| [opengl/GLCompiledDrawState](GLCompiledDrawState.md) | opengl | 1 |
| [opengl/GLContext](GLContext.md) | opengl | 1 |
| [opengl/GLProgramObject](GLProgramObject.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLState.h
python scripts/gpq.py def GPlatesOpenGL::GLState --body
python scripts/gpq.py uses GLState --kind class
python scripts/gpq.py hier GLState
```

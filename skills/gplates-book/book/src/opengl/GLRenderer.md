# GLRenderer

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 24 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLRenderer.h` | C++ | 2787 |
| `src/opengl/GLRenderer.cc` | C++ | 3175 |

## Overview

[[[PROSE overview unit=opengl/GLRenderer tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLRenderer::ClearDrawable`](#gplatesopenglglrenderercleardrawable) | struct | [`Drawable`](GLFilledPolygonsGlobeView.md) | — | 0 | Wrap up the draw call in case it gets added to a render queue. |
| [`GPlatesOpenGL::GLRenderer::DrawElementsDrawable`](#gplatesopenglglrendererdrawelementsdrawable) | struct | [`Drawable`](GLFilledPolygonsGlobeView.md) | — | 0 | Wrap up the draw call in case it gets added to a render queue. |
| [`GPlatesOpenGL::GLRenderer::DrawRangeElementsDrawable`](#gplatesopenglglrendererdrawrangeelementsdrawable) | struct | [`Drawable`](GLFilledPolygonsGlobeView.md) | — | 0 | Wrap up the draw call in case it gets added to a render queue. |
| [`GPlatesOpenGL::GLRenderer::ReadPixelsDrawable`](#gplatesopenglglrendererreadpixelsdrawable) | struct | [`Drawable`](GLFilledPolygonsGlobeView.md) | — | 0 | Wrap up the read pixels call in case it gets added to a render queue. |
| [`GPlatesOpenGL::GLRenderer::DrawPixelsDrawable`](#gplatesopenglglrendererdrawpixelsdrawable) | struct | [`Drawable`](GLFilledPolygonsGlobeView.md) | — | 0 | Wrap up the draw pixels call in case it gets added to a render queue. |
| [`GPlatesOpenGL::GLRenderer::CopyTexSubImage1DDrawable`](#gplatesopenglglrenderercopytexsubimage1ddrawable) | struct | [`Drawable`](GLFilledPolygonsGlobeView.md) | — | 0 | Wrap up the draw call in case it gets added to a render queue. |
| [`GPlatesOpenGL::GLRenderer::CopyTexSubImage2DDrawable`](#gplatesopenglglrenderercopytexsubimage2ddrawable) | struct | [`Drawable`](GLFilledPolygonsGlobeView.md) | — | 0 | Wrap up the draw call in case it gets added to a render queue. |
| [`GPlatesOpenGL::GLRenderer::CopyTexSubImage3DDrawable`](#gplatesopenglglrenderercopytexsubimage3ddrawable) | struct | [`Drawable`](GLFilledPolygonsGlobeView.md) | — | 0 | Wrap up the draw call in case it gets added to a render queue. |
| [`GPlatesOpenGL::GLRenderer`](#gplatesopenglglrenderer) | class | [`GPlatesUtils::ReferenceCount<GLRenderer>`](../utils/ReferenceCount.md) | — | 0 | Handles OpenGL rendering to render targets (and the main framebuffer). |

## Members

### `GPlatesOpenGL::GLRenderer::ClearDrawable`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ClearDrawable( GLbitfield clear_mask_)` | constructor | `None` | public | — |
| `draw( const GLCapabilities &capabilities, const GLState &state_to_apply, GLState &last_applied_state)` | method | `void` | public | — |
| `clear_mask` | field | `GLbitfield` | public | — |

### `GPlatesOpenGL::GLRenderer::DrawElementsDrawable`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DrawElementsDrawable( GLenum mode_, GLsizei count_, GLenum type_, GLint indices_offset_)` | constructor | `None` | public | — |
| `draw( const GLCapabilities &capabilities, const GLState &state_to_apply, GLState &last_applied_state)` | method | `void` | public | — |
| `mode` | field | `GLenum` | public | — |
| `count` | field | `GLsizei` | public | — |
| `type` | field | `GLenum` | public | — |
| `indices_offset` | field | `GLint` | public | — |

### `GPlatesOpenGL::GLRenderer::DrawRangeElementsDrawable`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DrawRangeElementsDrawable( GLenum mode_, GLuint start_, GLuint end_, GLsizei count_, GLenum type_, GLint indices_offset_)` | constructor | `None` | public | — |
| `draw( const GLCapabilities &capabilities, const GLState &state_to_apply, GLState &last_applied_state)` | method | `void` | public | — |
| `mode` | field | `GLenum` | public | — |
| `start` | field | `GLuint` | public | — |
| `end` | field | `GLuint` | public | — |
| `count` | field | `GLsizei` | public | — |
| `type` | field | `GLenum` | public | — |
| `indices_offset` | field | `GLint` | public | — |

### `GPlatesOpenGL::GLRenderer::ReadPixelsDrawable`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ReadPixelsDrawable( GLint x_, GLint y_, GLsizei width_, GLsizei height_, GLenum format_, GLenum type_, GLint offset_)` | constructor | `None` | public | — |
| `draw( const GLCapabilities &capabilities, const GLState &state_to_apply, GLState &last_applied_state)` | method | `void` | public | — |
| `x` | field | `GLint` | public | — |
| `y` | field | `GLint` | public | — |
| `width` | field | `GLsizei` | public | — |
| `height` | field | `GLsizei` | public | — |
| `format` | field | `GLenum` | public | — |
| `type` | field | `GLenum` | public | — |
| `offset` | field | `GLint` | public | — |

### `GPlatesOpenGL::GLRenderer::DrawPixelsDrawable`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DrawPixelsDrawable( GLint x_, GLint y_, GLsizei width_, GLsizei height_, GLenum format_, GLenum type_, GLint offset_)` | constructor | `None` | public | — |
| `draw( const GLCapabilities &capabilities, const GLState &state_to_apply, GLState &last_applied_state)` | method | `void` | public | — |
| `x` | field | `GLint` | public | — |
| `y` | field | `GLint` | public | — |
| `width` | field | `GLsizei` | public | — |
| `height` | field | `GLsizei` | public | — |
| `format` | field | `GLenum` | public | — |
| `type` | field | `GLenum` | public | — |
| `offset` | field | `GLint` | public | — |

### `GPlatesOpenGL::GLRenderer::CopyTexSubImage1DDrawable`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CopyTexSubImage1DDrawable( GLenum texture_target_, GLint level_, GLint xoffset_, GLint x_, GLint y_, GLsizei width_)` | constructor | `None` | public | — |
| `draw( const GLCapabilities &capabilities, const GLState &state_to_apply, GLState &last_applied_state)` | method | `void` | public | — |
| `texture_target` | field | `GLenum` | public | — |
| `level` | field | `GLint` | public | — |
| `xoffset` | field | `GLint` | public | — |
| `x` | field | `GLint` | public | — |
| `y` | field | `GLint` | public | — |
| `width` | field | `GLsizei` | public | — |

### `GPlatesOpenGL::GLRenderer::CopyTexSubImage2DDrawable`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CopyTexSubImage2DDrawable( GLenum texture_target_, GLint level_, GLint xoffset_, GLint yoffset_, GLint x_, GLint y_, GLsizei width_, GLsizei height_)` | constructor | `None` | public | — |
| `draw( const GLCapabilities &capabilities, const GLState &state_to_apply, GLState &last_applied_state)` | method | `void` | public | — |
| `texture_target` | field | `GLenum` | public | — |
| `level` | field | `GLint` | public | — |
| `xoffset` | field | `GLint` | public | — |
| `yoffset` | field | `GLint` | public | — |
| `x` | field | `GLint` | public | — |
| `y` | field | `GLint` | public | — |
| `width` | field | `GLsizei` | public | — |
| `height` | field | `GLsizei` | public | — |

### `GPlatesOpenGL::GLRenderer::CopyTexSubImage3DDrawable`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CopyTexSubImage3DDrawable( GLenum texture_target_, GLint level_, GLint xoffset_, GLint yoffset_, GLint zoffset_, GLint x_, GLint y_, GLsizei width_, GLsizei height_)` | constructor | `None` | public | — |
| `draw( const GLCapabilities &capabilities, const GLState &state_to_apply, GLState &last_applied_state)` | method | `void` | public | — |
| `texture_target` | field | `GLenum` | public | — |
| `level` | field | `GLint` | public | — |
| `xoffset` | field | `GLint` | public | — |
| `yoffset` | field | `GLint` | public | — |
| `zoffset` | field | `GLint` | public | — |
| `x` | field | `GLint` | public | — |
| `y` | field | `GLint` | public | — |
| `width` | field | `GLsizei` | public | — |
| `height` | field | `GLsizei` | public | — |

### `GPlatesOpenGL::GLRenderer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLRenderer>` | public | A convenience typedef for a shared pointer to a non-const GLRenderer. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLRenderer>` | public | A convenience typedef for a shared pointer to a const GLRenderer. |
| `GLRendererAPIError` | class | `None` | public | Reports an error using the begin/end block interface of GLRenderer. |
| `create( const GLContext::non_null_ptr_type &context, const boost::shared_ptr<GLStateStore> &state_store)` | method | `non_null_ptr_type` | public | Creates a GLRenderer object NOTE: Call GLContext::create\_renderer instead of calling this directly. |
| `begin_render()` | method | `void` | public | Call this method before using 'this' renderer. |
| `begin_render( QPainter &qpainter, // Does the QPainter render to the framebuffer or some other paint device ? ... bool paint_device_is_framebuffer = true)` | method | `void` | public | An alternative version of begin\_render that accepts a QPainter. |
| `end_render()` | method | `void` | public | Call this method after using 'this' renderer and before it is destroyed. |
| `RenderScope` | class | `None` | public | RAII class to call begin\_render and end\_render over a scope. |
| `rendering_to_context_framebuffer()` | method | `bool` | public | Returns true if we are rendering to the framebuffer of the OpenGL context. |
| `get_current_frame_buffer_dimensions()` | method | `std::pair<unsigned int/*width*/, unsigned int/*height*/>` | public | Returns the dimensions of the main framebuffer, or the currently bound framebuffer object (GLFrameBufferObject - see gl\_get\_bind\_frame\_buffer) if any are currently bound. |
| `get_qpainter_device_dimensions()` | method | `boost::optional< std::pair<unsigned int/*width*/, unsigned int/*height*/> >` | public | Returns the dimensions of the paint device of the QPainter attached in begin\_render, or boost::none if none attached. |
| `begin_qpainter_block()` | method | `boost::optional<QPainter &>` | public | Begins rendering to a QPainter (and suspends rendering using GLRenderer). |
| `end_qpainter_block()` | method | `void` | public | Ends the current QPainter block. |
| `QPainterBlockScope` | class | `None` | public | RAII class to call begin\_qpainter\_block and end\_qpainter\_block over a scope. |
| `supports_floating_point_render_target_2D()` | method | `bool` | public | Returns true if begin\_render\_target\_2D / end\_render\_target\_2D support rendering to floating-point textures. |
| `get_max_dimensions_untiled_render_target_2D( unsigned int &max_untiled_render_target_width, unsigned int &max_untiled_render_target_height)` | method | `void` | public | Returns the maximum (untiled) render target dimensions when using begin\_render\_target\_2D / end\_render\_target\_2D (values returned as power-of-two dimensions). |
| `begin_render_target_2D( const GLTexture::shared_ptr_to_const_type &texture, boost::optional<GLViewport> render_texture_viewport = boost::none, const double &max_point_size_and_line_width = 0, GLint level = 0, bool reset_to_default_state = true, bool depth_buffer = false, bool stencil_buffer = false)` | method | `void` | public | smaller than the render-texture). |
| `begin_tile_render_target_2D( bool save_restore_state = true, GLViewport *tile_render_target_viewport = NULL, GLViewport *tile_render_target_scissor_rect = NULL)` | method | `GLTransform::non_null_ptr_to_const_type` | public | Begins a tile (sub-region) of the current 2D render target. |
| `end_tile_render_target_2D()` | method | `bool` | public | Ends the current tile (sub-region) of the current 2D render target. |
| `end_render_target_2D()` | method | `void` | public | Ends the current 2D render target. |
| `RenderTarget2DScope` | class | `None` | public | RAII class to call begin\_render\_target\_2D and end\_render\_target\_2D over a scope. |
| `begin_state_block( bool reset_to_default_state = false)` | method | `void` | public | Begins a new state block. |
| `end_state_block()` | method | `void` | public | Ends the current state block. |
| `StateBlockScope` | class | `None` | public | RAII class to call begin\_state\_block and end\_state\_block over a scope. |
| `begin_render_queue_block()` | method | `void` | public | begin\_render\_queue\_block begin\_render\_target\_2D A draw to render target (immediately) end\_render\_target\_2D draw X using render texture A (queued) begin\_render\_target\_2D B draw to render target (immediately) end\_render\_target\_2D draw Y ... |
| `end_render_queue_block()` | method | `void` | public | Ends the current render queue block. |
| `RenderQueueBlockScope` | class | `None` | public | RAII class to call begin\_render\_queue\_block and end\_render\_queue\_block over a scope. |
| `begin_compile_draw_state( boost::optional<GLCompiledDrawState::non_null_ptr_type> compiled_draw_state = boost::none)` | method | `void` | public | Begins compiling a draw state. |
| `end_compile_draw_state()` | method | `GLCompiledDrawState::non_null_ptr_type` | public | Ends compilation of a draw state and returns the compiled draw state (which is either a new compile draw state or the compile draw state passed into begin\_compile\_draw\_state). |
| `CompileDrawStateScope` | class | `None` | public | RAII class to call begin\_compile\_draw\_state and end\_compile\_draw\_state over a scope. |
| `create_empty_compiled_draw_state()` | method | `GLCompiledDrawState::non_null_ptr_type` | public | Creates an empty compiled draw state that contains no state changes or draw commands. |
| `apply_compiled_draw_state( const GLCompiledDrawState &compiled_draw_state)` | method | `void` | public | Applies the specified compiled draw state. |
| `gl_clear( GLbitfield clear_mask)` | method | `void` | public | Clears the current framebuffer. clear\_mask is the same as the argument to the OpenGL function 'glClear()'. |
| `gl_copy_tex_sub_image_1D( GLenum texture_unit, GLenum texture_target, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)` | method | `void` | public | Performs same function as the glCopyTexSubImage1D OpenGL function. |
| `gl_copy_tex_sub_image_2D( GLenum texture_unit, GLenum texture_target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height)` | method | `void` | public | Performs same function as the glCopyTexSubImage2D OpenGL function. |
| `gl_copy_tex_sub_image_3D( GLenum texture_unit, GLenum texture_target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y, GLsizei width, GLsizei height)` | method | `void` | public | Performs same function as the glCopyTexSubImage3D OpenGL function. |
| `gl_bind_frame_buffer( const GLFrameBufferObject::shared_ptr_to_const_type &frame_buffer_object)` | method | `void` | public | Binds the specified framebuffer object - requires the GL\_EXT\_framebuffer\_object extension. |
| `gl_unbind_frame_buffer()` | method | `void` | public | Unbinds any currently bound framebuffer object - the \*main\* framebuffer is now targeted. |
| `gl_bind_program_object( const GLProgramObject::shared_ptr_to_const_type &program_object)` | method | `void` | public | Binds the specified shader program object - requires the GL\_ARB\_shader\_objects extension. |
| `gl_unbind_program_object()` | method | `void` | public | Unbinds any currently bound shader program object - the fixed-function pipeline is now used exclusively. |
| `gl_bind_texture( const GLTexture::shared_ptr_to_const_type &texture_object, GLenum texture_unit, GLenum texture_target)` | method | `void` | public | Binds a texture to the specified texture unit. |
| `gl_unbind_texture( GLenum texture_unit, GLenum texture_target)` | method | `void` | public | Unbinds any currently bound texture object on the specified texture unit and texture target. |
| `gl_color_mask( GLboolean red = GL_TRUE, GLboolean green = GL_TRUE, GLboolean blue = GL_TRUE, GLboolean alpha = GL_TRUE)` | method | `void` | public | Sets the OpenGL colour mask. |
| `gl_depth_mask( GLboolean flag = GL_TRUE)` | method | `void` | public | Sets the OpenGL depth mask. |
| `gl_stencil_mask( GLuint stencil = ~0/*all ones*/)` | method | `void` | public | Sets the OpenGL stencil mask. |
| `gl_clear_color( GLclampf red = GLclampf(0.0), GLclampf green = GLclampf(0.0), GLclampf blue = GLclampf(0.0), GLclampf alpha = GLclampf(0.0))` | method | `void` | public | Sets the OpenGL clear colour. |
| `gl_clear_depth( GLclampd depth = GLclampd(1.0))` | method | `void` | public | Sets the OpenGL clear depth value. |
| `gl_clear_stencil( GLint stencil = 0)` | method | `void` | public | Sets the OpenGL clear stencil value. |
| `gl_scissor( GLint x, GLint y, GLsizei width, GLsizei height)` | method | `void` | public | Sets the current scissor rectangle (GL\_SCISSOR\_TEST also needs to be enabled). |
| `gl_scissor_array( const std::vector<GLViewport> &all_scissor_rectangles)` | method | `void` | public | Sets all scissor rectangles to the parameters specified in all\_scissor\_rectangles. |
| `gl_viewport( GLint x, GLint y, GLsizei width, GLsizei height)` | method | `void` | public | Sets the current viewport. |
| `gl_viewport_array( const std::vector<GLViewport> &all_viewports)` | method | `void` | public | Sets all viewports to the parameters specified in all\_viewports. |
| `gl_depth_range( GLclampd zNear = 0.0, GLclampd zFar = 1.0)` | method | `void` | public | Sets the depth range for the current viewport. |
| `gl_depth_range_array( const std::vector<GLDepthRange> &all_depth_ranges)` | method | `void` | public | Sets depth ranges of all viewports to the parameters specified in all\_depth\_ranges. |
| `gl_stencil_func( GLenum func = GL_ALWAYS, GLint ref = GLint(0), GLuint mask = ~0/*all ones*/)` | method | `void` | public | Sets the stencil function (GL\_STENCIL\_TEST also needs to be enabled). |
| `gl_stencil_op( GLenum fail = GL_KEEP, GLenum zfail = GL_KEEP, GLenum zpass = GL_KEEP)` | method | `void` | public | Sets the stencil operation (GL\_STENCIL\_TEST also needs to be enabled). |
| `gl_enable( GLenum cap, bool enable = true)` | method | `void` | public | Enable/disable the specified capability. |
| `gl_enable_texture( GLenum texture_unit, GLenum texture_target, bool enable = true)` | method | `void` | public | Enable/disable texturing for the specified target and texture unit. |
| `gl_point_size( GLfloat size = GLfloat(1))` | method | `void` | public | Sets the point size. |
| `gl_line_width( GLfloat width = GLfloat(1))` | method | `void` | public | Sets the line width. |
| `gl_polygon_mode( GLenum face = GL_FRONT_AND_BACK, GLenum mode = GL_FILL)` | method | `void` | public | — |
| `gl_front_face( GLenum mode = GL_CCW)` | method | `void` | public | — |
| `gl_cull_face( GLenum mode = GL_BACK)` | method | `void` | public | — |
| `gl_polygon_offset( GLfloat factor = GLfloat(0), GLfloat units = GLfloat(0))` | method | `void` | public | — |
| `gl_hint( GLenum target, GLenum mode)` | method | `void` | public | Specify a hint. |
| `gl_alpha_func( GLenum func = GL_ALWAYS, GLclampf ref = GLclampf(0))` | method | `void` | public | Sets the alpha test function. |
| `gl_depth_func( GLenum func = GL_LESS)` | method | `void` | public | Sets the depth function. |
| `gl_blend_equation( GLenum mode = DEFAULT_BLEND_EQUATION)` | method | `void` | public | Sets the alpha-blend equation (NOTE: you'll also want to enable blending). |
| `gl_blend_equation_separate( GLenum modeRGB = DEFAULT_BLEND_EQUATION, GLenum modeAlpha = DEFAULT_BLEND_EQUATION)` | method | `void` | public | Sets the alpha-blend equation separately for RGB and Alpha (NOTE: you'll also want to enable blending). |
| `gl_blend_func( GLenum sfactor = GL_ONE, GLenum dfactor = GL_ZERO)` | method | `void` | public | Sets the alpha-blend function (NOTE: you'll also want to enable blending). |
| `gl_blend_func_separate( GLenum sfactorRGB = GL_ONE, GLenum dfactorRGB = GL_ZERO, GLenum sfactorAlpha = GL_ONE, GLenum dfactorAlpha = GL_ZERO)` | method | `void` | public | Sets the alpha-blend function separately for RGB and Alpha (NOTE: you'll also want to enable blending). |
| `gl_tex_env( GLenum texture_unit, GLenum target, GLenum pname, const ParamType &param)` | method | `void` | public | Sets the specified texture environment state to the specified parameter on the specified texture unit. |
| `gl_tex_gen( GLenum texture_unit, GLenum coord, GLenum pname, const ParamType &param)` | method | `void` | public | Sets the specified texture coordinate generation state to the specified parameter on the specified texture unit. |
| `gl_load_matrix( GLenum mode, const GLMatrix &matrix)` | method | `void` | public | Loads the specified matrix into the specified matrix mode. |
| `gl_load_texture_matrix( GLenum texture_unit, const GLMatrix &texture_matrix)` | method | `void` | public | Loads the specified matrix into the texture matrix (GL\_TEXTURE) for the specified texture unit. |
| `gl_mult_matrix( GLenum mode, const GLMatrix &matrix)` | method | `void` | public | Post-multiplies the current matrix (for mode) by matrix. |
| `gl_mult_texture_matrix( GLenum texture_unit, const GLMatrix &texture_matrix)` | method | `void` | public | Post-multiplies the current texture matrix (GL\_TEXTURE) on the specified texture unit by texture\_matrix. |
| `gl_get_enable( GLenum cap)` | method | `bool` | public | Returns whether the specified capability is enabled or disabled (see gl\_enable). |
| `gl_get_viewport` | field | `GLViewport` | public | Returns the current viewport at index viewport\_index (default index is zero). |
| `gl_get_scissor` | field | `GLViewport` | public | Returns the current scissor rectangle at index viewport\_index (default index is zero). |
| `gl_get_matrix` | field | `GLMatrix` | public | Returns the current matrix for the specified matrix mode, or identity if not set. |
| `gl_get_texture_matrix` | field | `GLMatrix` | public | Returns the current texture matrix for the specified texture unit, or identity if not set. |
| `gl_get_bind_frame_buffer()` | method | `boost::optional<GLFrameBufferObject::shared_ptr_to_const_type>` | public | Returns the current framebuffer object, or boost::none if main framebuffer is currently bound. |
| `QPainterInfo` | struct | `None` | private | Information about the QPainter, if any, that is active at the beginning of rendering. |
| `DEFAULT_BLEND_EQUATION` | field | `GLenum` | private | The default blend equation for 'glBlendEquation()'. |
| `d_qpainter_info` | field | `boost::optional<QPainterInfo>` | private | Is valid if a QPainter is active during rendering (when begin\_render is called). |
| `d_context` | field | `GLContext::non_null_ptr_type` | private | Used to begin/end rendering and manage framebuffer objects. |
| `d_main_frame_buffer_dimensions` | field | `std::pair<unsigned int/*width*/, unsigned int/*height*/>` | private | The dimensions of the main frame buffer. |
| `d_default_viewport` | field | `boost::optional<GLViewport>` | private | The viewport of the window currently attached to the OpenGL context. |
| `d_state_store` | field | `boost::shared_ptr<GLStateStore>` | private | Used to efficiently allocate GLState objects. |
| `d_default_state` | field | `GLState::shared_ptr_type` | private | Represents the default OpenGL state. |
| `d_last_applied_state` | field | `GLState::shared_ptr_type` | private | Represents the actual OpenGL state (as it was last applied to OpenGL). |
| `d_current_frame_buffer_draw_count` | field | `GLRendererImpl::frame_buffer_draw_count_type` | private | The current draw count for draw calls that modify any framebuffers. |
| `d_render_target_block_stack` | field | `GLRendererImpl::render_target_block_stack_type` | private | Stack of currently render target blocks. |
| `GLRenderer( const GLContext::non_null_ptr_type &context, const boost::shared_ptr<GLStateStore> &state_store)` | constructor | `None` | private | Constructor. |
| `get_current_state()` | method | `GLState::shared_ptr_to_const_type` | private | Returns the 'const' state of the current state block of the current render target block. |
| `clone_current_state()` | method | `GLState::shared_ptr_type` | private | Clones the state of the current state block (top of stack). |
| `update_compiled_draw_state_for_current_context( GLState &compiled_state_change)` | method | `void` | private | When compiled draw state is applied it may need to be updated to work with the current OpenGL context if it is a different context than when the draw state was compiled. |
| `draw( const GLRendererImpl::RenderOperation &render_operation)` | method | `void` | private | Renders a render operation containing a drawable and a state. |
| `suspend_qpainter()` | method | `void` | private | — |
| `resume_qpainter()` | method | `void` | private | NOTE: OpenGL must be in the default state before this is called. |
| `begin_rgba8_main_framebuffer_2D( GLRendererImpl::RenderTextureTarget &render_texture_target, const double &max_point_size_and_line_width)` | method | `void` | private | — |
| `begin_tile_rgba8_main_framebuffer_2D( GLRendererImpl::RenderTextureTarget &render_texture_target, GLViewport *tile_render_target_viewport, GLViewport *tile_render_target_scissor_rect)` | method | `GLTransform::non_null_ptr_to_const_type` | private | — |
| `end_tile_rgba8_main_framebuffer_2D( GLRendererImpl::RenderTextureTarget &render_texture_target)` | method | `bool` | private | — |
| `end_rgba8_main_framebuffer_2D( GLRendererImpl::RenderTextureTarget &render_texture_target)` | method | `void` | private | — |
| `begin_framebuffer_object_2D( GLRendererImpl::RenderTextureTarget &render_texture_target)` | method | `bool` | private | — |
| `begin_tile_framebuffer_object_2D( GLRendererImpl::RenderTextureTarget &render_texture_target, GLViewport *tile_render_target_viewport, GLViewport *tile_render_target_scissor_rect)` | method | `GLTransform::non_null_ptr_to_const_type` | private | — |
| `end_tile_framebuffer_object_2D( GLRendererImpl::RenderTextureTarget &render_texture_target)` | method | `bool` | private | — |
| `end_framebuffer_object_2D( GLRendererImpl::RenderTextureTarget &render_texture_target)` | method | `void` | private | — |
| `begin_render_internal()` | method | `void` | private | — |
| `begin_render_target_block_internal( bool reset_to_default_state, const boost::optional<GLRendererImpl::RenderTextureTarget> &render_texture_target = boost::none)` | method | `void` | private | — |
| `end_render_target_block_internal()` | method | `void` | private | — |
| `begin_state_block_internal( const GLRendererImpl::StateBlock &state_block)` | method | `void` | private | — |
| `begin_render_queue_block_internal( const GLRendererImpl::RenderQueue::non_null_ptr_type &render_queue)` | method | `void` | private | — |
| `end_render_queue_block_internal()` | method | `GLRendererImpl::RenderQueue::non_null_ptr_type` | private | — |
| `gl_draw_elements( GLenum mode, GLsizei count, GLenum type, GLint indices_offset)` | method | `void` | private | Performs same function as the glDrawElements OpenGL function. |
| `gl_draw_elements( GLenum mode, GLsizei count, GLenum type, GLint indices_offset, const GLBufferImpl::shared_ptr_to_const_type &vertex_element_buffer_impl)` | method | `void` | private | Performs same function as the glDrawElements OpenGL function. |
| `apply_current_state_to_opengl()` | method | `void` | public | Applies the current renderer state immediately to OpenGL instead of waiting until the next un-queued draw command (or any command that writes to, or reads from, the current framebuffer). |
| `gl_draw_range_elements( GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, GLint indices_offset)` | method | `void` | public | Performs same function as the glDrawRangeElements OpenGL function. |
| `gl_draw_range_elements( GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, GLint indices_offset, const GLBufferImpl::shared_ptr_to_const_type &vertex_element_buffer_impl)` | method | `void` | public | Performs same function as the glDrawRangeElements OpenGL function. |
| `gl_read_pixels( GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs the equivalent of the OpenGL command 'glReadPixels'. |
| `gl_read_pixels( GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLint offset, const GLBufferImpl::shared_ptr_type &pixel_buffer_impl)` | method | `void` | public | Performs the equivalent of the OpenGL command 'glReadPixels'. |
| `gl_draw_pixels( GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLint offset)` | method | `void` | public | Performs the equivalent of the OpenGL command 'glDrawPixels' with the exception that, to mirror 'glReadPixels', the x and y pixel offsets are also specified (internally 'glWindowPos2i(x, y)' is called since 'glDrawPixels' does not accept x ... |
| `gl_draw_pixels( GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLint offset, const GLBufferImpl::shared_ptr_type &pixel_buffer_impl)` | method | `void` | public | Performs the equivalent of the OpenGL command 'glDrawPixels' with the exception that, to mirror 'glReadPixels', the x and y pixel offsets are also specified (internally 'glWindowPos2i(x, y)' is called since 'glDrawPixels' does not accept x ... |
| `gl_active_texture( GLenum active_texture)` | method | `void` | public | Sets the currently active texture unit. |
| `gl_client_active_texture( GLenum client_active_texture)` | method | `void` | public | Sets the currently active texture unit targeted by vertex texture coordinate arrays. |
| `gl_matrix_mode( GLenum mode)` | method | `void` | public | Specifies which matrix stack is the target for matrix operations. |
| `gl_bind_frame_buffer_and_apply( const GLFrameBufferObject::shared_ptr_to_const_type &frame_buffer_object)` | method | `void` | public | Binds the specified framebuffer object and applies directly to OpenGL - requires the GL\_EXT\_framebuffer\_object extension. |
| `BindFrameBufferAndApply` | class | `None` | public | RAII class to bind, and apply, to OpenGL over a scope (reverts bind, but not apply, at scope exit). |
| `gl_unbind_frame_buffer_and_apply()` | method | `void` | public | Unbinds any currently bound framebuffer object and applies directly to OpenGL - requires the GL\_EXT\_framebuffer\_object extension. |
| `UnbindFrameBufferAndApply` | class | `None` | public | RAII class to unbind, and apply, to OpenGL over a scope (reverts bind, but not apply, at scope exit). |
| `gl_bind_program_object_and_apply( const GLProgramObject::shared_ptr_to_const_type &program_object)` | method | `void` | public | Binds the specified shader program object and applies directly to OpenGL - requires the GL\_ARB\_shader\_objects extension. |
| `BindProgramObjectAndApply` | class | `None` | public | RAII class to bind, and apply, to OpenGL over a scope (reverts bind, but not apply, at scope exit). |
| `gl_unbind_program_object_and_apply()` | method | `void` | public | Same as gl\_unbind\_program\_object but also applies binding directly to OpenGL. |
| `UnbindProgramObjectAndApply` | class | `None` | public | RAII class to unbind, and apply, to OpenGL over a scope (reverts unbind, but not apply, at scope exit). |
| `gl_bind_texture_and_apply( const GLTexture::shared_ptr_to_const_type &texture_object, GLenum texture_unit, GLenum texture_target)` | method | `void` | public | Binds a texture to the specified texture unit and applies directly to OpenGL. |
| `BindTextureAndApply` | class | `None` | public | RAII class to bind, and apply, to OpenGL over a scope (reverts bind, but not apply, at scope exit). |
| `gl_unbind_texture_and_apply( GLenum texture_unit, GLenum texture_target)` | method | `void` | public | Same as gl\_unbind\_texture but also applies binding directly to OpenGL. |
| `UnbindTextureAndApply` | class | `None` | public | RAII class to unbind, and apply, to OpenGL over a scope (reverts unbind, but not apply, at scope exit). |
| `gl_bind_vertex_array_object( const GLVertexArrayObject::shared_ptr_to_const_type &vertex_array_object)` | method | `void` | public | Binds a vertex array object - requires the GL\_ARB\_vertex\_array\_object extension. |
| `gl_bind_vertex_array_object_and_apply( const GLVertexArrayObject::shared_ptr_to_const_type &vertex_array_object)` | method | `void` | public | Same as gl\_bind\_vertex\_array\_object but also applies binding directly to OpenGL. |
| `BindVertexArrayObjectAndApply` | class | `None` | public | RAII class to bind, and apply, to OpenGL over a scope (reverts bind, but not apply, at scope exit). |
| `gl_unbind_vertex_array_object()` | method | `void` | public | Unbinds any currently bound vertex array object. |
| `gl_bind_vertex_element_buffer_object( const GLVertexElementBufferObject::shared_ptr_to_const_type &vertex_element_buffer_object)` | method | `void` | public | Binds a vertex element buffer object - requires the GL\_ARB\_vertex\_buffer\_object extension. |
| `gl_unbind_vertex_element_buffer_object()` | method | `void` | public | Unbinds any currently bound vertex element buffer object. |
| `gl_bind_vertex_buffer_object( const GLVertexBufferObject::shared_ptr_to_const_type &vertex_buffer_object)` | method | `void` | public | Binds a vertex buffer object - requires the GL\_ARB\_vertex\_buffer\_object extension. |
| `gl_unbind_vertex_buffer_object()` | method | `void` | public | Unbinds any currently bound vertex buffer object. |
| `gl_bind_pixel_unpack_buffer_object( const GLPixelBufferObject::shared_ptr_to_const_type &pixel_buffer_object)` | method | `void` | public | Binds a pixel buffer object on the \*unpack\* target - requires the GL\_ARB\_pixel\_buffer\_object extension. |
| `gl_unbind_pixel_unpack_buffer_object()` | method | `void` | public | Unbinds any currently bound pixel buffer object on the \*unpack\* target. |
| `gl_bind_pixel_pack_buffer_object( const GLPixelBufferObject::shared_ptr_to_const_type &pixel_buffer_object)` | method | `void` | public | Binds a pixel buffer object on the \*pack\* target - requires the GL\_ARB\_pixel\_buffer\_object extension. |
| `gl_unbind_pixel_pack_buffer_object()` | method | `void` | public | Unbinds any currently bound pixel buffer object on the \*pack\* target. |
| `gl_bind_buffer_object( const GLBufferObject::shared_ptr_to_const_type &buffer_object, GLenum target)` | method | `void` | public | Binds a buffer object to the specified target - requires the GL\_ARB\_vertex\_buffer\_object extension. |
| `gl_bind_buffer_object_and_apply( const GLBufferObject::shared_ptr_to_const_type &buffer_object, GLenum target)` | method | `void` | public | Same as gl\_bind\_buffer\_object but also applies binding directly to OpenGL. |
| `BindBufferObjectAndApply` | class | `None` | public | RAII class to bind, and apply, to OpenGL over a scope (reverts bind, but not apply, at scope exit). |
| `gl_unbind_buffer_object( GLenum target)` | method | `void` | public | Unbinds any buffer object currently bound to the specified target. |
| `gl_unbind_buffer_object_and_apply( GLenum target)` | method | `void` | public | Same as gl\_unbind\_buffer\_object but also applies binding directly to OpenGL. |
| `UnbindBufferObjectAndApply` | class | `None` | public | RAII class to unbind, and apply, to OpenGL over a scope (reverts unbind, but not apply, at scope exit). |
| `gl_enable_client_state( GLenum array, bool enable = true)` | method | `void` | public | Enables the specified (array) vertex array (in the fixed-function pipeline). array should be one of GL\_VERTEX\_ARRAY, GL\_COLOR\_ARRAY, or GL\_NORMAL\_ARRAY. |
| `gl_enable_client_texture_state( GLenum texture_unit, bool enable = true)` | method | `void` | public | Enables the vertex attribute array GL\_TEXTURE\_COORD\_ARRAY (in the fixed-function pipeline) on the specified texture unit. |
| `gl_vertex_pointer( GLint size, GLenum type, GLsizei stride, GLint offset, GLBufferObject::shared_ptr_to_const_type vertex_buffer_object)` | method | `void` | public | Specify the source of vertex position data (from a buffer object). |
| `gl_vertex_pointer( GLint size, GLenum type, GLsizei stride, GLint offset, GLBufferImpl::shared_ptr_to_const_type vertex_buffer_impl)` | method | `void` | public | Specify the source of vertex position data (from client memory). |
| `gl_color_pointer( GLint size, GLenum type, GLsizei stride, GLint offset, GLBufferObject::shared_ptr_to_const_type vertex_buffer_object)` | method | `void` | public | Specify the source of vertex color data (from a buffer object). |
| `gl_color_pointer( GLint size, GLenum type, GLsizei stride, GLint offset, GLBufferImpl::shared_ptr_to_const_type vertex_buffer_impl)` | method | `void` | public | Specify the source of vertex color data (from client memory). |
| `gl_normal_pointer( GLenum type, GLsizei stride, GLint offset, GLBufferObject::shared_ptr_to_const_type vertex_buffer_object)` | method | `void` | public | Specify the source of vertex normal data (from a buffer object). |
| `gl_normal_pointer( GLenum type, GLsizei stride, GLint offset, GLBufferImpl::shared_ptr_to_const_type vertex_buffer_impl)` | method | `void` | public | Specify the source of vertex normal data (from client memory). |
| `gl_tex_coord_pointer( GLint size, GLenum type, GLsizei stride, GLint offset, GLBufferObject::shared_ptr_to_const_type vertex_buffer_object, GLenum texture_unit)` | method | `void` | public | Specify the source of vertex texture coordinate data (from a buffer object). |
| `gl_tex_coord_pointer( GLint size, GLenum type, GLsizei stride, GLint offset, GLBufferImpl::shared_ptr_to_const_type vertex_buffer_impl, GLenum texture_unit)` | method | `void` | public | Specify the source of vertex texture coordinate data (from client memory). |
| `gl_enable_vertex_attrib_array( GLuint attribute_index, bool enable = true)` | method | `void` | public | Enables the specified \*generic\* vertex attribute array (for use in a shader program). |
| `gl_vertex_attrib_pointer( GLuint attribute_index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, GLint offset, GLBufferObject::shared_ptr_to_const_type vertex_buffer_object)` | method | `void` | public | Specify the source of \*generic\* vertex attribute array (for use in a shader program "from a buffer object"). |
| `gl_vertex_attrib_pointer( GLuint attribute_index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, GLint offset, GLBufferImpl::shared_ptr_to_const_type vertex_buffer_impl)` | method | `void` | public | Specify the source of \*generic\* vertex attribute array (for use in a shader program "from client memory"). |
| `gl_vertex_attrib_i_pointer( GLuint attribute_index, GLint size, GLenum type, GLsizei stride, GLint offset, GLBufferObject::shared_ptr_to_const_type vertex_buffer_object)` | method | `void` | public | Same as gl\_vertex\_attrib\_pointer except used to specify attributes mapping to \*integer\* shader variables. |
| `gl_vertex_attrib_i_pointer( GLuint attribute_index, GLint size, GLenum type, GLsizei stride, GLint offset, GLBufferImpl::shared_ptr_to_const_type vertex_buffer_impl)` | method | `void` | public | Same as gl\_vertex\_attrib\_pointer except used to specify attributes mapping to \*integer\* shader variables. |
| `gl_vertex_attrib_l_pointer( GLuint attribute_index, GLint size, GLenum type, GLsizei stride, GLint offset, GLBufferObject::shared_ptr_to_const_type vertex_buffer_object)` | method | `void` | public | Same as gl\_vertex\_attrib\_pointer except used to specify attributes mapping to \*double\* shader variables. |
| `gl_vertex_attrib_l_pointer( GLuint attribute_index, GLint size, GLenum type, GLsizei stride, GLint offset, GLBufferImpl::shared_ptr_to_const_type vertex_buffer_impl)` | method | `void` | public | Same as gl\_vertex\_attrib\_pointer except used to specify attributes mapping to \*double\* shader variables. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DEFAULT_BLEND_EQUATION` | variable | `GLenum` | — |
| `GPLATES_OPENGL_GLRENDERER_H` | macro | `None` | — |
| `create_unbound_vertex_array_compiled_draw_state( GLRenderer &renderer)` | function | `GLCompiledDrawState::non_null_ptr_type` | Creates a compiled draw state that specifies no bound vertex element buffer, no bound vertex attribute arrays (vertex buffers) and no enabled client vertex attribute state. |

## Notes

[[[PROSE notes unit=opengl/GLRenderer tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLScalarField3D](GLScalarField3D.md) | opengl | 78 |
| [opengl/GLAgeGridMaskSource](GLAgeGridMaskSource.md) | opengl | 61 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 60 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 59 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 43 |
| [opengl/GLProgramObject](GLProgramObject.md) | opengl | 43 |
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 43 |
| [gui/Globe](../gui/Globe.md) | gui | 41 |
| [opengl/GLVertexArrayImpl](GLVertexArrayImpl.md) | opengl | 25 |
| [gui/SphericalGrid](../gui/SphericalGrid.md) | gui | 22 |
| [opengl/GLSaveRestoreFrameBuffer](GLSaveRestoreFrameBuffer.md) | opengl | 21 |
| [opengl/GLUtils](GLUtils.md) | opengl | 21 |
| [opengl/GLVisualRasterSource](GLVisualRasterSource.md) | opengl | 19 |
| [opengl/GLScalarField3DGenerator](GLScalarField3DGenerator.md) | opengl | 18 |
| [gui/OpaqueSphere](../gui/OpaqueSphere.md) | gui | 17 |
| [gui/Stars](../gui/Stars.md) | gui | 17 |
| [opengl/GLFilledPolygonsMapView](GLFilledPolygonsMapView.md) | opengl | 17 |
| [opengl/GLMultiResolutionRasterMapView](GLMultiResolutionRasterMapView.md) | opengl | 17 |
| [gui/MapGrid](../gui/MapGrid.md) | gui | 15 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 15 |

*... and 53 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLRenderer.h
python scripts/gpq.py def GPlatesOpenGL::GLRenderer --body
python scripts/gpq.py uses GLRenderer --kind class
python scripts/gpq.py hier GLRenderer
```

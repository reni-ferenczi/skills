# GLScalarField3D

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 42 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLScalarField3D.h` | C++ | 1075 |
| `src/opengl/GLScalarField3D.cc` | C++ | 4410 |

## Overview

`GLScalarField3D` ray-traces a sub-surface scalar field (e.g. seismic tomography data) loaded from a cube-map file of concentric depth layers, and draws it either as an iso-surface or as vertical cross-sections through arbitrary geometry. The field data, per-tile metadata and a depth-radius-to-layer lookup are all uploaded as texture arrays; rendering itself happens in shader programs compiled from `src/qt-resources/opengl/scalar_field_3d`, driven by a `GPlatesViewOperations::ScalarField3DRenderParameters` bundle that selects render mode, colour mode, depth restriction and quality/performance trade-offs, and lit via a shared `GLLight`.

Both render entry points accept an optional `SurfaceFillMask`, built from surface polygon/polyline geometry, which extrudes the surface region towards the globe centre to restrict where the ray-tracer draws (and can additionally render the mask's vertical walls). Producing that mask, and the associated volume-fill boundary and wall passes, involves several private `ConstGeometryOnSphereVisitor` subclasses that stream cross-section, fill-mask and boundary vertices through `GLStaticStreamPrimitives`, plus intermediate off-screen passes rendered into `GLScreenRenderTarget`s. A separate always-drawn white inner sphere, built by recursively subdividing a hierarchical triangular mesh (`SphereMeshBuilder`), represents the solid Earth beneath the field.

Instances are only ever produced through the static `create()` factory (the constructor is private), after checking `is_supported()`/`supports_surface_fill_mask()` for the required OpenGL 3.0 features. `change_scalar_field()` lets a time-dependent field swap its underlying data in place as long as the new file has the same dimensions as the current one.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLScalarField3D`](#gplatesopenglglscalarfield3d) | class | [`GPlatesUtils::ReferenceCount<GLScalarField3D>`](../utils/ReferenceCount.md) | — | 0 | A 3D sub-surface scalar field represented as a cube map of concentric depth layers. |

## Members

### `GPlatesOpenGL::GLScalarField3D`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLScalarField3D>` | public | A convenience typedef for a shared pointer to a non-const GLScalarField3D. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLScalarField3D>` | public | A convenience typedef for a shared pointer to a const GLScalarField3D. |
| `cache_handle_type` | typedef | `boost::shared_ptr<void>` | public | Typedef for an opaque object that caches a particular render of this scalar field. |
| `cross_sections_seq_type` | typedef | `std::vector<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | public | Typedef for a sequence of cross section geometries (points, multipoints, polylines, polygons). |
| `surface_polygons_mask_seq_type` | typedef | `std::vector<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | public | Typedef for a sequence of surface polygons mask geometries (polylines, polygons). |
| `SurfaceFillMask` | struct | `None` | public | Defines surface geometries used as fill masks to limit rendering of isosurface (or cross sections) to certain volume regions defined by extruding the surface mask towards the globe centre. |
| `is_supported( GLRenderer &renderer)` | method | `bool` | public | Returns true if rendering (ray-tracing) of 3D scalar fields are supported on the runtime system. |
| `supports_surface_fill_mask( GLRenderer &renderer)` | method | `bool` | public | Returns true if surface polygons masking of 3D scalar fields is supported on the runtime system. |
| `create( GLRenderer &renderer, const QString &scalar_field_filename, const GLLight::non_null_ptr_type &light)` | method | `non_null_ptr_type` | public | Creates a GLScalarField3D object. scalar\_field\_filename is the cube map file containing the source of scalar field data. light determines the light direction and other parameters to use when rendering the scalar field. |
| `set_colour_palette( GLRenderer &renderer, const GPlatesGui::ColourPalette<double>::non_null_ptr_to_const_type &colour_palette, const std::pair<double, double> &colour_palette_value_range)` | method | `void` | public | Set the colour palette. |
| `change_scalar_field( GLRenderer &renderer, const QString &scalar_field_filename)` | method | `bool` | public | Change to a new scalar field of the same dimensions as the current internal scalar field. |
| `get_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns a subject token that clients can observe to see if they need to update themselves (such as any cached data we render for them) by getting us to re-render. |
| `render_iso_surface( GLRenderer &renderer, cache_handle_type &cache_handle, GPlatesViewOperations::ScalarField3DRenderParameters::IsosurfaceDeviationWindowMode deviation_window_mode, GPlatesViewOperations::ScalarField3DRenderParameters::IsosurfaceColourMode colour_mode, const GPlatesViewOperations::ScalarField3DRenderPa ...` | method | `void` | public | Renders the scalar field as an iso-surface visible in the view frustum (determined by the current model-view/projection transforms of renderer). render\_mode must an isosurface mode (ie, not 'RENDER\_MODE\_CROSS\_SECTIONS'). surface\_fill\_mask ... |
| `render_cross_sections( GLRenderer &renderer, cache_handle_type &cache_handle, const cross_sections_seq_type &cross_sections, GPlatesViewOperations::ScalarField3DRenderParameters::CrossSectionColourMode colour_mode, const GPlatesViewOperations::ScalarField3DRenderParameters::DepthRestriction &depth_restriction, const st ...` | method | `void` | public | Renders the scalar field as cross-section(s) visible in the view frustum (determined by the current model-view/projection transforms of renderer). |
| `SHADER_VERSION` | field | `GLShaderSource::ShaderVersion` | private | The version of GLSL shading language to use in our shaders. |
| `DEFAULT_SHADER_VERSION` | field | `GLShaderSource::ShaderVersion` | private | The version of GLSL shading language to use in our shaders. |
| `DEPTH_RADIUS_TO_LAYER_RESOLUTION` | field | `unsigned int` | private | The resolution of the 1D texture for converting depth radii to layer indices. |
| `COLOUR_PALETTE_RESOLUTION` | field | `unsigned int` | private | The resolution of the 1D texture for converting scalar values (or gradient magnitudes) to colour. |
| `SURFACE_FILL_MASK_RESOLUTION` | field | `unsigned int` | private | The (square) texture dimension of the textures in the surface fill mask texture array. |
| `MAX_TEXTURE_IMAGE_UNITS_USED` | field | `unsigned int` | private | The most texture image units used for any shader program. |
| `SURFACE_FILL_MASK_GEOMETRY_SHADER_MAX_OUTPUT_VERTICES` | field | `unsigned int` | private | The maximum number of vertices output by the surface fill mask geometry shader. |
| `SPHERICAL_CAP_NUM_SUBDIVISIONS` | field | `unsigned int` | private | We will tessellate a great circle arc, when rendering spherical caps, if either line segment endpoint is far enough away from the polygon centroid. |
| `VOLUME_FILL_SPHERICAL_CAP_GEOMETRY_SHADER_MAX_OUTPUT_VERTICES` | field | `unsigned int` | private | The maximum number of vertices output by the volume fill spherical cap geometry shaders. |
| `VOLUME_FILL_WALL_GEOMETRY_SHADER_MAX_OUTPUT_VERTICES` | field | `unsigned int` | private | The maximum number of vertices output by the volume fill wall geometry shaders. |
| `NUM_BYTES_IN_STREAMING_VERTEX_BUFFER` | field | `unsigned int` | private | The number of bytes in the vertex buffer used to stream. |
| `MINIMUM_BYTES_TO_STREAM_IN_VERTEX_BUFFER` | field | `unsigned int` | private | The minimum number of bytes to stream in the vertex buffer. |
| `NUM_BYTES_IN_STREAMING_VERTEX_ELEMENT_BUFFER` | field | `unsigned int` | private | The number of bytes in the vertex element (indices) buffer used to stream. |
| `MINIMUM_BYTES_TO_STREAM_IN_VERTEX_ELEMENT_BUFFER` | field | `unsigned int` | private | The minimum number of bytes to stream in the vertex element buffer. |
| `streaming_vertex_element_type` | typedef | `GLuint` | private | Typedef for vertex elements (indices) used for streaming vertex array. |
| `CrossSectionVertex` | struct | `None` | private | A vertex of a cross-section geometry. |
| `cross_section_stream_primitives_type` | typedef | `GLStaticStreamPrimitives<CrossSectionVertex, streaming_vertex_element_type>` | private | Typedef for a static stream of cross-section vertices. |
| `CrossSection1DGeometryOnSphereVisitor` | class | `None` | private | Renders points/multipoints as vertically extruded cross-section 1D (line) geometries. |
| `CrossSection2DGeometryOnSphereVisitor` | class | `None` | private | Renders polylines/polygons as vertically extruded cross-section 2D (mesh) geometries. |
| `SurfaceFillMaskVertex` | struct | `None` | private | A vertex of a surface fill mask geometry. |
| `surface_fill_mask_stream_primitives_type` | typedef | `GLStaticStreamPrimitives<SurfaceFillMaskVertex, streaming_vertex_element_type>` | private | Typedef for a static stream of surface fill mask geometry vertices. |
| `SurfaceFillMaskGeometryOnSphereVisitor` | class | `None` | private | Renders filled polygons (and optionally polylines) to the surface fill mask. |
| `VolumeFillBoundaryVertex` | struct | `None` | private | A vertex of a volume fill boundary geometry. |
| `volume_fill_boundary_stream_primitives_type` | typedef | `GLStaticStreamPrimitives<VolumeFillBoundaryVertex, streaming_vertex_element_type>` | private | Typedef for a static stream of volume fill boundary geometry vertices. |
| `VolumeFillBoundaryGeometryOnSphereVisitor` | class | `None` | private | Class for rendering boundary surface of volume fill region from the same surface polygons (and optionally polylines) used to generate the surface fill mask. |
| `SphereMeshBuilder` | class | `None` | private | Used to recurse into a hierarchical triangular mesh to generate white inner sphere. |
| `d_subject_token` | field | `GPlatesUtils::SubjectToken` | private | Used to inform clients that we have been updated. |
| `d_light` | field | `GLLight::non_null_ptr_type` | private | The light (direction) used during lighting. |
| `d_light_observer_token` | field | `GPlatesUtils::ObserverToken` | private | Keep track of changes to d\_light. |
| `d_tile_meta_data_resolution` | field | `unsigned int` | private | The tile metadata resolution of the current scalar field. |
| `d_tile_resolution` | field | `unsigned int` | private | The tile resolution of the current scalar field. |
| `d_num_active_tiles` | field | `unsigned int` | private | The number of active tiles of the current scalar field. |
| `d_num_depth_layers` | field | `unsigned int` | private | The number of depth layers of the current scalar field. |
| `d_min_depth_layer_radius` | field | `float` | private | Minimum depth layer radius (closest to Earth's core). |
| `d_max_depth_layer_radius` | field | `float` | private | Maximum depth layer radius (closest to Earth's surface). |
| `d_depth_layer_radii` | field | `std::vector<float>` | private | The radius of each depth layer - ordered from smaller to larger radii. |
| `d_scalar_min` | field | `double` | private | The minimum scalar value across the entire scalar field. |
| `d_scalar_max` | field | `double` | private | The maximum scalar value across the entire scalar field. |
| `d_scalar_mean` | field | `double` | private | The mean scalar value across the entire scalar field. |
| `d_scalar_standard_deviation` | field | `double` | private | The scalar standard deviation across the entire scalar field. |
| `d_gradient_magnitude_min` | field | `double` | private | The minimum gradient magnitude across the entire scalar field. |
| `d_gradient_magnitude_max` | field | `double` | private | The maximum gradient magnitude across the entire scalar field. |
| `d_gradient_magnitude_mean` | field | `double` | private | The mean gradient magnitude across the entire scalar field. |
| `d_gradient_magnitude_standard_deviation` | field | `double` | private | The gradient magnitude standard deviation across the entire scalar field. |
| `d_tile_meta_data_texture_array` | field | `GLTexture::shared_ptr_type` | private | Texture array where each texel contains metadata for a tile (tile ID, max/min scalar value). |
| `d_field_data_texture_array` | field | `GLTexture::shared_ptr_type` | private | Texture array containing the field data (scalar value and gradient). |
| `d_mask_data_texture_array` | field | `GLTexture::shared_ptr_type` | private | Texture array containing the mask data. |
| `d_depth_radius_to_layer_texture` | field | `GLTexture::shared_ptr_type` | private | 1D texture to map layer depth radii to layer indices (into texture array). |
| `d_colour_palette_texture` | field | `GLTexture::shared_ptr_type` | private | 1D texture to map scalar values (or gradient magnitudes) to colour. |
| `d_colour_palette_value_range` | field | `std::pair<double, double>` | private | The current range of the colour palette. |
| `d_render_iso_surface_program_object` | field | `boost::optional<GLProgramObject::shared_ptr_type>` | private | Shader program for rendering an iso-surface. |
| `d_render_cross_section_program_object` | field | `boost::optional<GLProgramObject::shared_ptr_type>` | private | Shader program for rendering a cross-section of an iso-surface. |
| `d_render_surface_fill_mask_program_object` | field | `boost::optional<GLProgramObject::shared_ptr_type>` | private | Shader program for rendering surface fill mask as optional preliminary step to rendering isosurface. |
| `d_render_volume_fill_spherical_cap_depth_range_program_object` | field | `boost::optional<GLProgramObject::shared_ptr_type>` | private | Shader program for rendering volume fill spherical cap (depth range). |
| `d_render_volume_fill_wall_depth_range_program_object` | field | `boost::optional<GLProgramObject::shared_ptr_type>` | private | Shader program for rendering volume fill walls (depth range). |
| `d_render_volume_fill_wall_surface_normals_program_object` | field | `boost::optional<GLProgramObject::shared_ptr_type>` | private | Shader program for rendering volume fill wall surface normals. |
| `d_surface_fill_mask_resolution` | field | `unsigned int` | private | The (square) texture dimension of the textures in the surface fill mask texture array. |
| `d_streaming_vertex_element_buffer` | field | `GLVertexElementBuffer::shared_ptr_type` | private | Used to stream indices (vertex elements) for cross-section geometry and surface fill masks. |
| `d_streaming_vertex_buffer` | field | `GLVertexBuffer::shared_ptr_type` | private | Used to stream vertices for cross-section geometry and surface fill masks. |
| `d_cross_section_vertex_array` | field | `GLVertexArray::shared_ptr_type` | private | Used to contain cross-section geometries. |
| `d_surface_fill_mask_vertex_array` | field | `GLVertexArray::shared_ptr_type` | private | Used to contain surface geometries (when rendering surface fill mask). |
| `d_volume_fill_boundary_vertex_array` | field | `GLVertexArray::shared_ptr_type` | private | Used to contain surface geometries (when rendering volume fill boundary). |
| `d_white_inner_sphere_vertex_array` | field | `GLVertexArray::shared_ptr_type` | private | Vertex array for white inner sphere. |
| `d_white_inner_sphere_compiled_draw_state` | field | `boost::optional<GLCompiledDrawState::non_null_ptr_to_const_type>` | private | Compiled draw state for white inner sphere. |
| `d_render_white_inner_sphere_program_object` | field | `boost::optional<GLProgramObject::shared_ptr_type>` | private | Shader program for rendering white inner sphere (with lighting). |
| `d_render_depth_range_inner_sphere_program_object` | field | `boost::optional<GLProgramObject::shared_ptr_type>` | private | Shader program for rendering inner sphere as screen-space depth. |
| `acquire_surface_fill_mask_texture( GLRenderer &renderer, unsigned int surface_fill_mask_resolution)` | method | `GLTexture::shared_ptr_to_const_type` | private | — |
| `GLScalarField3D( GLRenderer &renderer, const QString &scalar_field_filename, const GLLight::non_null_ptr_type &light)` | constructor | `None` | private | Constructor. |
| `initialise_inner_sphere( GLRenderer &renderer)` | method | `void` | private | — |
| `allocate_streaming_vertex_buffers( GLRenderer &renderer)` | method | `void` | private | — |
| `initialise_cross_section_rendering( GLRenderer &renderer)` | method | `void` | private | — |
| `initialise_iso_surface_rendering( GLRenderer &renderer)` | method | `void` | private | — |
| `initialise_surface_fill_mask_rendering( GLRenderer &renderer)` | method | `void` | private | — |
| `initialise_volume_fill_boundary_rendering( GLRenderer &renderer)` | method | `void` | private | — |
| `initialise_shader_utils( GLRenderer &renderer, const GLProgramObject::shared_ptr_type &program_object)` | method | `void` | private | — |
| `create_shader_program( GLRenderer &renderer, const QString &vertex_shader_source_file_name, const QString &fragment_shader_source_file_name, // Optional geometry shader source file name and program parameters... boost::optional< std::pair<QString, GLShaderProgramUtils::GeometryShaderProgramParameters> > geometry_shader ...` | method | `boost::optional<GLProgramObject::shared_ptr_type>` | private | — |
| `create_tile_meta_data_texture_array( GLRenderer &renderer)` | method | `void` | private | — |
| `create_field_data_texture_array( GLRenderer &renderer)` | method | `void` | private | — |
| `create_mask_data_texture_array( GLRenderer &renderer)` | method | `void` | private | — |
| `create_depth_radius_to_layer_texture( GLRenderer &renderer)` | method | `void` | private | — |
| `create_colour_palette_texture( GLRenderer &renderer)` | method | `void` | private | — |
| `load_scalar_field( GLRenderer &renderer, const GPlatesFileIO::ScalarField3DFileFormat::Reader &scalar_field_reader)` | method | `void` | private | — |
| `load_depth_radius_to_layer_texture( GLRenderer &renderer)` | method | `void` | private | — |
| `load_colour_palette_texture( GLRenderer &renderer, const GPlatesGui::ColourPalette<double>::non_null_ptr_to_const_type &colour_palette, const std::pair<double, double> &colour_palette_value_range)` | method | `void` | private | — |
| `set_iso_surface_and_cross_sections_shader_common_variables( GLRenderer &renderer, const GLProgramObject::shared_ptr_type &program_object, unsigned int &current_texture_unit, const GPlatesViewOperations::ScalarField3DRenderParameters::DepthRestriction &depth_restriction, const std::vector<float> &test_variables, boost:: ...` | method | `void` | private | — |
| `set_shader_test_variables( GLRenderer &renderer, const GLProgramObject::shared_ptr_type &program_object, const std::vector<float> &test_variables)` | method | `void` | private | — |
| `render_surface_fill_mask( GLRenderer &renderer, const surface_polygons_mask_seq_type &surface_polygons_mask, bool include_polylines, GLTexture::shared_ptr_to_const_type &surface_fill_mask_texture)` | method | `bool` | private | Returns true if rendered successfully - should always return true but just in case. |
| `render_volume_fill_wall_depth_range( GLRenderer &renderer, const surface_polygons_mask_seq_type &surface_polygons_mask, bool include_polylines, const GLTexture::shared_ptr_to_const_type &surface_fill_mask_texture, const GPlatesViewOperations::ScalarField3DRenderParameters::DepthRestriction &depth_restriction, boost::op ...` | method | `bool` | private | Returns true if rendered successfully - should always return true but just in case. |
| `render_volume_fill_wall_surface_normal_and_depth( GLRenderer &renderer, const surface_polygons_mask_seq_type &surface_polygons_mask, bool include_polylines, bool only_show_boundary_walls, const GLTexture::shared_ptr_to_const_type &surface_fill_mask_texture, const GPlatesViewOperations::ScalarField3DRenderParameters::De ...` | method | `bool` | private | Returns true if rendered successfully - should always return true but just in case. |
| `render_cross_sections_1d( GLRenderer &renderer, const GLVertexElementBuffer::shared_ptr_type &streaming_vertex_element_buffer, const GLVertexBuffer::shared_ptr_type &streaming_vertex_buffer, const GLVertexArray::shared_ptr_type &cross_section_vertex_array, const cross_sections_seq_type &cross_sections)` | method | `void` | private | — |
| `render_cross_sections_2d( GLRenderer &renderer, const GLVertexElementBuffer::shared_ptr_type &streaming_vertex_element_buffer, const GLVertexBuffer::shared_ptr_type &streaming_vertex_buffer, const GLVertexArray::shared_ptr_type &cross_section_vertex_array, const cross_sections_seq_type &cross_sections)` | method | `void` | private | — |
| `render_white_inner_sphere( GLRenderer &renderer, const GPlatesViewOperations::ScalarField3DRenderParameters::DepthRestriction &depth_restriction)` | method | `void` | private | — |
| `render_inner_sphere_depth_range( GLRenderer &renderer, const GPlatesViewOperations::ScalarField3DRenderParameters::DepthRestriction &depth_restriction)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GREAT_CIRCLE_ARC_ANGULAR_THRESHOLD` | variable | `double` | We will tessellate a great circle arc, when rendering 2D cross-section geometries, if the two endpoints are far enough apart. |
| `COSINE_GREAT_CIRCLE_ARC_ANGULAR_THRESHOLD` | variable | `double` | — |
| `SCALAR_FIELD_UTILS_SOURCE_FILE_NAME` | variable | `QString` | Shader source code utilities used for scalar field ray-tracing. |
| `ISO_SURFACE_VERTEX_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Vertex shader source code to render isosurface. |
| `ISO_SURFACE_FRAGMENT_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Fragment shader source code to render isosurface. |
| `CROSS_SECTION_VERTEX_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Vertex shader source code to render vertical cross-section of scalar field. |
| `CROSS_SECTION_FRAGMENT_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Fragment shader source code to render vertical cross-section of scalar field. |
| `SURFACE_FILL_MASK_VERTEX_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Vertex shader source code to render surface fill mask. |
| `SURFACE_FILL_MASK_GEOMETRY_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Geometry shader source code to render surface fill mask. |
| `SURFACE_FILL_MASK_FRAGMENT_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Fragment shader source code to render surface fill mask. |
| `VOLUME_FILL_VERTEX_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Vertex shader source code to render volume fill boundary. |
| `VOLUME_FILL_SPHERICAL_CAP_GEOMETRY_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Geometry shader source code to render volume fill spherical caps. |
| `VOLUME_FILL_WALL_GEOMETRY_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Geometry shader source code to render volume fill walls. |
| `VOLUME_FILL_SPHERICAL_CAP_FRAGMENT_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Fragment shader source code to render volume fill spherical caps. |
| `VOLUME_FILL_WALL_FRAGMENT_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Fragment shader source code to render volume fill wal depth range. |
| `SPHERE_VERTEX_SHADER` | variable | `QString` | Vertex shader source code to render coloured (white) sphere with lighting. |
| `SPHERE_FRAGMENT_SHADER` | variable | `QString` | Fragment shader source code to render coloured (white) sphere with lighting. |
| `debug_fixed_point_texture_array( GLRenderer &renderer, const GLTexture::shared_ptr_to_const_type &texture, const QString &image_file_basename)` | function | `void` | Useful when debugging a fixed-point texture array by saving each layer to an image file. |
| `GPLATES_OPENGL_GLSCALARFIELD3D_H` | macro | `None` | — |

## Notes

- `change_scalar_field()` returns `false`, without modifying state, when the new file's dimensions don't match the current internal field; the caller must then construct a fresh `GLScalarField3D` instead.
- `render_iso_surface()` requires an isosurface render mode, not `RENDER_MODE_CROSS_SECTIONS`.
- `SHADER_VERSION` is pinned to `GLShaderSource::DEFAULT_SHADER_VERSION` (GLSL 1.2) rather than the 1.3 that the OpenGL 3.0 features technically call for, because of uncertainty over Mac OS X Snow Leopard's OpenGL 3.0 support; the code instead relies on the `GL_EXT_texture_array` shader `#extension` where it can.
- Callers observe `get_subject_token()` to know when they must re-render cached output; `d_light_observer_token` similarly tracks changes to the shared `GLLight` so lighting-dependent shader state stays in sync.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLVisualLayers](GLVisualLayers.md) | opengl | 20 |
| [presentation/ScalarField3DVisualLayerParams](../presentation/ScalarField3DVisualLayerParams.md) | presentation | 3 |
| [gui/GlobeRenderedGeometryCollectionPainter](../gui/GlobeRenderedGeometryCollectionPainter.md) | gui | 2 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 2 |

## Related

**Shader programs compiled by this unit**

| Shader unit | Component |
|---|---|
| [shaders/scalar_field_3d](../qt-resources/opengl/scalar_field_3d.md) | shaders |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLScalarField3D.h
python scripts/gpq.py def GPlatesOpenGL::GLScalarField3D --body
python scripts/gpq.py uses GLScalarField3D --kind class
python scripts/gpq.py hier GLScalarField3D
```

# GLMultiResolutionRaster

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 65 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLMultiResolutionRaster.h` | C++ | 1258 |
| `src/opengl/GLMultiResolutionRaster.cc` | C++ | 2589 |

## Overview

This is the class that puts a georeferenced raster onto the globe. It takes a
`GLMultiResolutionRasterSource` (the pixel data, of any dimensions), a
`GPlatesPropertyValues::Georeferencing` and a
`GPlatesPropertyValues::CoordinateTransformation`, and builds a pyramid of
square texture tiles where each tile also carries its own triangle mesh whose
vertices lie on the unit sphere. Everything downstream builds on it:
`GLMultiResolutionCubeRaster` re-renders it into cube-face tiles,
`GLScalarField3DGenerator` drives it to extract depth layers,
`RasterLayerProxy` and `GLVisualLayers` are where it gets created for a raster
layer.

Two problems are solved here, and the split runs through the whole class. The
first is *which resolution*: `get_level_of_detail` asks
`GLProjectionUtils::get_min_pixel_size_on_unit_sphere` how big a viewport pixel
is on the globe and takes the log2 ratio against
`d_max_highest_resolution_texel_size_on_unit_sphere`, which was measured once at
construction by sampling the level-0 tiles. It returns the *unclamped* value on
purpose, so a caller rendering into a texture can see it needs a bigger render
target rather than settle for a blurrier raster. The second is *which tiles*:
each level of detail owns its own oriented-bounding-box tree, built bottom-up
over that level's tile grid, and `get_visible_tiles` walks it against a
`GLFrustum` using `GLIntersect::intersect_OBB_frustum`, narrowing the active
plane mask as it descends. Only tiles that survive that walk ever get a texture
uploaded or a vertex buffer filled — the `LevelOfDetailTile` objects created up
front hold nothing but the description needed to build them on demand, and both
the textures and the vertices live behind `GPlatesUtils::ObjectCache` so they
recycle as the view pans.

A single `dynamic_cast` on `d_raster_source` selects between four rendering
modes, and the branch is repeated wherever vertex size or shader setup matters.
An ordinary fixed-point raster uses the fixed-function pipeline with a
`GL_REPLACE` texture environment and a plain `GLTextureVertex`. A floating-point
raster switches to a fragment shader purely to escape the fixed-function
pipeline's clamping of values to [0,1], which would corrupt data-analysis
rasters. A `GLNormalMapSource` or `GLScalarFieldDepthLayersSource` needs a
per-vertex tangent-space frame — computed here from the neighbouring vertex
positions, reaching outside the tile when the raster continues past its edge —
and a `SURFACE_NORMALS` or `SCALAR_GRADIENT` variant of
`multi_resolution_raster/render_raster_fragment_shader.glsl` to convert
tangent-space normals into world space. `clear_frame_buffer` exists for the same
family of cases: a *regional* normal map only covers part of a render target, so
the area outside it has to be filled with sphere normals rather than zeros,
which `RenderSphereNormals` does by drawing a cube and normalising in the shader.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLMultiResolutionRaster`](#gplatesopenglglmultiresolutionraster) | class | [`GLMultiResolutionRasterInterface`](GLMultiResolutionRasterInterface.md) | — | 0 | An arbitrary dimension raster image represented as a multi-resolution pyramid of tiled OpenGL textures and associated vertex meshes. |

## Members

### `GPlatesOpenGL::GLMultiResolutionRaster`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLMultiResolutionRaster>` | public | A convenience typedef for a shared pointer to a non-const GLMultiResolutionRaster. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLMultiResolutionRaster>` | public | A convenience typedef for a shared pointer to a const GLMultiResolutionRaster. |
| `tile_handle_type` | typedef | `std::size_t` | public | Typedef for a handle to a tile. |
| `cache_handle_type` | typedef | `GLMultiResolutionRasterInterface::cache_handle_type` | public | Typedef for an opaque object that caches a particular render of this raster. |
| `FixedPointTextureFilterType` | enum | `None` | public | The texture filter types to use for fixed-point textures. |
| `RasterScanlineOrderType` | enum | `None` | public | The order of scanlines or rows of data in the raster as visualised in the image. |
| `DEFAULT_FIXED_POINT_TEXTURE_FILTER` | field | `FixedPointTextureFilterType` | public | The default fixed-point texture filtering mode for the textures returned by get\_tile\_texture is bilinear (with anisotropic) filtering. |
| `FIXED_POINT_TEXTURE_FILTER_ANISOTROPIC` | field | `FixedPointTextureFilterType` | public | The default fixed-point texture filtering mode for the textures returned by get\_tile\_texture is bilinear (with anisotropic) filtering. |
| `CacheTileTexturesType` | enum | `None` | public | Determines the granularity of caching to be used for GLMultiResolutionRaster tile textures... |
| `DEFAULT_CACHE_TILE_TEXTURES` | field | `CacheTileTexturesType` | public | The default granularity of tile texture caching. |
| `CACHE_TILE_TEXTURES_INDIVIDUAL_TILES` | field | `CacheTileTexturesType` | public | The default granularity of tile texture caching. |
| `supports_normal_map_source( GLRenderer &renderer)` | method | `bool` | public | Returns true if a normal map (GLNormalMapSource) can be used as raster source on the runtime system. |
| `supports_scalar_field_depth_layers_source( GLRenderer &renderer)` | method | `bool` | public | Returns true if scalar field depth layers (GLScalarFieldDepthLayersSource) can be used as raster source on the runtime system. |
| `create( GLRenderer &renderer, const GPlatesPropertyValues::Georeferencing::non_null_ptr_to_const_type &georeferencing, const GPlatesPropertyValues::CoordinateTransformation::non_null_ptr_to_const_type &coordinate_transformation, const GLMultiResolutionRasterSource::non_null_ptr_type &raster_source, FixedPointTextureFil ...` | method | `non_null_ptr_type` | public | Creates a GLMultiResolutionRaster object. georeferencing locates the raster pixels/lines in the raster's spatial reference system. coordinate\_transformation transforms georeferenced raster coordinates to the standard geographic coordinate ... |
| `get_num_levels_of_detail()` | method | `unsigned int` | public | Returns the number of levels of detail. |
| `get_level_of_detail( const GLMatrix &model_view_transform, const GLMatrix &projection_transform, const GLViewport &viewport, float level_of_detail_bias = 0.0f)` | method | `float` | public | Returns the unclamped exact floating-point level-of-detail that theoretically represents the exact level-of-detail that would be required to fulfill the resolution needs of a render target (as defined by the specified viewport and ... |
| `clamp_level_of_detail( float level_of_detail)` | method | `float` | public | Takes an unclamped level-of-detail (see get\_level\_of\_detail) and clamps it to lie within the the range \[0, get\_num\_levels\_of\_detail - 1\]. |
| `render( GLRenderer &renderer, float level_of_detail, cache_handle_type &cache_handle)` | method | `bool` | public | Renders all tiles visible in the view frustum (determined by the current model-view/projection transforms of renderer) and returns true if any tiles were rendered. |
| `get_visible_tiles( std::vector<tile_handle_type> &visible_tiles, const GLMatrix &model_view_transform, const GLMatrix &projection_transform, float level_of_detail)` | method | `void` | public | Returns a list of tiles that are visible inside the view frustum planes defined by the specified model-view and projection transforms. |
| `get_visible_tiles( std::vector<tile_handle_type> &visible_tiles, const GLMatrix &model_view_transform, const GLMatrix &projection_transform, const GLViewport &viewport, float level_of_detail_bias = 0.0f)` | method | `void` | public | Returns a list of tiles that are visible inside the view frustum planes defined by the specified model-view and projection transforms. |
| `render( GLRenderer &renderer, const std::vector<tile_handle_type> &tiles, cache_handle_type &cache_handle)` | method | `bool` | public | Renders the specified tiles to the current render target of renderer (returns true if the specified tiles are not empty). |
| `get_tile_texel_dimension()` | method | `unsigned int` | public | Returns the tile texel dimension of this raster which is also the tile texel dimension of the raster source. |
| `get_target_texture_internal_format()` | method | `GLint` | public | Returns the texture internal format that can be used if rendering to a texture, when calling render, as opposed to the main framebuffer. |
| `clear_frame_buffer( GLRenderer &renderer)` | method | `void` | public | Clears the currently bound framebuffer as appropriate for the raster type. |
| `TileVertices` | struct | `None` | private | Maintains a tile's vertices in the form of a vertex buffer and vertex array wrapper. |
| `tile_vertices_cache_type` | typedef | `GPlatesUtils::ObjectCache<TileVertices>` | private | Typedef for a cache of tile vertices. |
| `TileTexture` | struct | `None` | private | Maintains a tile's texture and source tile cache handle. |
| `tile_texture_cache_type` | typedef | `GPlatesUtils::ObjectCache<TileTexture>` | private | Typedef for a cache of tile textures. |
| `Tile` | class | `None` | private | A tile represents an arbitrary patch of the raster that is covered by a single OpenGL texture. |
| `ClientCacheTile` | struct | `None` | private | Used to cache information, specific to a tile, to return to the client for caching. |
| `LevelOfDetailTile` | class | `None` | private | Retains information to build a single tile of the raster. |
| `LevelOfDetail` | class | `None` | private | A level-of-detail represents a full set of tiles covering the entire raster, but at a particular resolution. |
| `level_of_detail_tile_seq_type` | typedef | `std::vector<LevelOfDetailTile::non_null_ptr_type>` | private | Typedef for a sequence of level-of-detail tiles. |
| `level_of_detail_seq_type` | typedef | `std::vector<LevelOfDetail::non_null_ptr_type>` | private | Typedef for a sequence of level-of-details. |
| `TangentSpaceFrame` | struct | `None` | private | The tangent space coordinate frame (not necessarily orthogonal) at a position on the sphere. |
| `vertex_type` | typedef | `GLTextureVertex` | private | Typedef for vertices. |
| `normal_map_vertex_type` | typedef | `GLTextureTangentSpaceVertex` | private | Typedef for normal-map vertices. |
| `scalar_field_depth_layer_vertex_type` | typedef | `GLTextureTangentSpaceVertex` | private | Typedef for scalar-gradient-map vertices. |
| `vertex_element_type` | typedef | `GLushort` | private | Typedef for vertex indices. |
| `vertex_element_buffer_map_type` | typedef | `std::map< std::pair<unsigned int,unsigned int>, GLVertexElementBuffer::shared_ptr_to_const_type>` | private | Typedef for mapping a tile's vertex dimensions to vertex indices (and draw call). |
| `texels_per_vertex_fixed_point_type` | typedef | `boost::uint32_t` | private | A 16:16 fixed point type to get fractional values without floating-point precision issues. |
| `RenderSphereNormals` | class | `None` | private | Used to render sphere normals. |
| `d_georeferencing` | field | `GPlatesPropertyValues::Georeferencing::non_null_ptr_to_const_type` | private | Georeferencing information to position the raster pixels/lines in the raster's spatial reference system. |
| `d_coordinate_transformation` | field | `GPlatesPropertyValues::CoordinateTransformation::non_null_ptr_to_const_type` | private | Transforms georeferenced raster coordinates to the standard geographic coordinate system WGS84 (this transforms from the raster's possibly \*projection\* spatial reference). |
| `d_raster_source` | field | `GLMultiResolutionRasterSource::non_null_ptr_type` | private | The source of multi-resolution raster data. |
| `d_raster_width` | field | `unsigned int` | private | Original raster width. |
| `d_raster_height` | field | `unsigned int` | private | Original raster height. |
| `d_raster_scanline_order` | field | `RasterScanlineOrderType` | private | The scanline order of the raster (whether first row of data is at top or bottom of image). |
| `d_fixed_point_texture_filter` | field | `FixedPointTextureFilterType` | private | The texture filtering mode (for fixed-point textures) for textures rendered during render. |
| `d_tile_texel_dimension` | field | `unsigned int` | private | The number of texels along a tiles edge (horizontal or vertical since it's square). |
| `d_inverse_tile_texel_dimension` | field | `float` | private | 1.0 / 'd\_tile\_texel\_dimension'. |
| `d_num_texels_per_vertex` | field | `texels_per_vertex_fixed_point_type` | private | The (fractional) number of texels between two adjacent vertices along a horizontal or vertical edge of the tile. |
| `d_tiles` | field | `level_of_detail_tile_seq_type` | private | All tiles of all resolution are grouped into one array for easy lookup for clients. |
| `d_level_of_detail_pyramid` | field | `level_of_detail_seq_type` | private | — |
| `d_max_highest_resolution_texel_size_on_unit_sphere` | field | `float` | private | The maximum size of any texel in the original raster (the highest resolution level-of-detail) when projected onto the unit sphere. |
| `d_tile_texture_cache` | field | `tile_texture_cache_type::shared_ptr_type` | private | This raster has its own cache of textures which gets reused/recycled as the view pans across the raster. |
| `d_cache_tile_textures` | field | `CacheTileTexturesType` | private | Determines granularity of caching of \*our\* tile textures. |
| `d_tile_vertices_cache` | field | `tile_vertices_cache_type::shared_ptr_type` | private | A cache of tile vertices to limit memory usage. |
| `d_vertex_element_buffers` | field | `vertex_element_buffer_map_type` | private | Shared vertex indices used by the tiles of this raster. |
| `d_render_raster_program_object` | field | `boost::optional<GLProgramObject::shared_ptr_type>` | private | Shader program to render either a \*floating-point\* raster or a normal-map raster. |
| `d_render_sphere_normals` | field | `boost::optional<RenderSphereNormals>` | private | Used to render sphere normals. |
| `MAX_NUM_TEXELS_PER_VERTEX` | field | `unsigned int` | private | The maximum number of texels between two adjacent vertices along a horizontal or vertical edge of the tile. |
| `MAX_ANGLE_IN_DEGREES_BETWEEN_VERTICES` | field | `unsigned int` | private | We also need to make sure there are enough vertices to follow the curvature of the globe, otherwise the mesh segments will dip too far below the surface of the sphere. |
| `GLMultiResolutionRaster( GLRenderer &renderer, const GPlatesPropertyValues::Georeferencing::non_null_ptr_to_const_type &georeferencing, const GPlatesPropertyValues::CoordinateTransformation::non_null_ptr_to_const_type &coordinate_transformation, const GLMultiResolutionRasterSource::non_null_ptr_type &raster_source, Fix ...` | constructor | `None` | private | Constructor. |
| `create_shader_program_if_necessary( GLRenderer &renderer)` | method | `void` | private | — |
| `initialise_level_of_detail_pyramid()` | method | `void` | private | Creates the level-of-detail pyramid structures. |
| `calculate_num_texels_per_vertex()` | method | `texels_per_vertex_fixed_point_type` | private | Calculates the (fractional) number of texels per vertex required for the entire raster. |
| `create_level_of_detail( const unsigned int lod_level)` | method | `LevelOfDetail::non_null_ptr_type` | private | Creates a level-of-detail structure for level lod\_level. |
| `create_obb_tree( LevelOfDetail &level_of_detail, const unsigned int x_geo_start, const unsigned int x_geo_end, const unsigned int y_geo_start, const unsigned int y_geo_end)` | method | `std::size_t` | private | Creates an oriented bounding box tree covering a level-of-detail. |
| `create_obb_tree_leaf_node( LevelOfDetail &level_of_detail, const unsigned int x_geo_start, const unsigned int x_geo_end, const unsigned int y_geo_start, const unsigned int y_geo_end)` | method | `std::size_t` | private | Creates a leaf node of an OBB tree covering a specific level-of-detail. |
| `create_level_of_detail_tile( LevelOfDetail &level_of_detail, const unsigned int x_geo_start, const unsigned int x_geo_end, const unsigned int y_geo_start, const unsigned int y_geo_end)` | method | `tile_handle_type` | private | Creates a raster tile structure containing enough information to subsequently generate texture and vertex data for rendering the tile. |
| `bound_level_of_detail_tile( const LevelOfDetailTile &lod_tile)` | method | `GLIntersect::OrientedBoundingBox` | private | Creates an oriented bounding box for lod\_tile. |
| `create_oriented_bounding_box_builder( const double &x_geo_coord, const double &y_geo_coord)` | method | `GLIntersect::OrientedBoundingBoxBuilder` | private | Creates an oriented bounding box (OBB) builder whose z-axis coincides with the position of the specified pixel coordinates (of the raster) on the unit sphere. |
| `calc_max_texel_size_on_unit_sphere( const unsigned int lod_level, const LevelOfDetailTile &lod_tile)` | method | `float` | private | Calculates the maximum size of any texel of lod\_tile projected onto the unit sphere. |
| `get_vertex_element_buffer( GLRenderer &renderer, const unsigned int num_vertices_along_tile_x_edge, const unsigned int num_vertices_along_tile_y_edge)` | method | `GLVertexElementBuffer::shared_ptr_to_const_type` | private | Gets, or creates if one doesn't exist, a uniform mesh of triangles covering a tile with num\_vertices\_along\_tile\_x\_edge by num\_vertices\_along\_tile\_y\_edge vertices. |
| `get_visible_tiles( const GLFrustum &frustum_planes, boost::uint32_t frustum_plane_mask, const LevelOfDetail &lod, const LevelOfDetail::OBBTreeNode &obb_tree_node, std::vector<tile_handle_type> &visible_tiles)` | method | `void` | private | Recursively traverses OBB tree to find visible tiles. |
| `get_tile( tile_handle_type tile_handle, GLRenderer &renderer)` | method | `Tile` | private | Returns the tile corresponding to tile\_handle. |
| `get_tile_texture( GLRenderer &renderer, const LevelOfDetailTile &lod_tile)` | method | `tile_texture_cache_type::object_shared_ptr_type` | private | Returns the tile texture for the tile lod\_tile. |
| `get_tile_vertices( GLRenderer &renderer, const LevelOfDetailTile &lod_tile)` | method | `tile_vertices_cache_type::object_shared_ptr_type` | private | Returns the tile vertices for the tile lod\_tile. |
| `load_raster_data_into_tile_texture( const LevelOfDetailTile &lod_tile, TileTexture &tile_texture, GLRenderer &renderer)` | method | `void` | private | Loads raster data into lod\_tile. |
| `create_texture( GLRenderer &renderer, const GLTexture::shared_ptr_type &texture)` | method | `void` | private | Creates a texture in OpenGL but doesn't load any image data into it. |
| `load_vertices_into_tile_vertex_buffer( GLRenderer &renderer, const LevelOfDetailTile &lod_tile, TileVertices &tile_vertices)` | method | `void` | private | Loads vertex data into lod\_tile. |
| `get_adjacent_vertex_positions( GPlatesMaths::UnitVector3D &vertex_position01, bool &has_vertex_position01, GPlatesMaths::UnitVector3D &vertex_position21, bool &has_vertex_position21, GPlatesMaths::UnitVector3D &vertex_position10, bool &has_vertex_position10, GPlatesMaths::UnitVector3D &vertex_position12, bool &has_vert ...` | method | `void` | private | — |
| `calculate_tangent_space_frame( const GPlatesMaths::UnitVector3D &vertex_position, const GPlatesMaths::UnitVector3D &vertex_position01, const GPlatesMaths::UnitVector3D &vertex_position21, const GPlatesMaths::UnitVector3D &vertex_position10, const GPlatesMaths::UnitVector3D &vertex_position12)` | method | `TangentSpaceFrame` | private | — |
| `convert_pixel_coord_to_geographic_coord( const double &x_pixel_coord, const double &y_pixel_coord, boost::optional<double &> y_pixel_coord_clamped = boost::none)` | method | `GPlatesMaths::PointOnSphere` | private | Converts from raster pixel coordinates to a position on the globe. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `INVERSE_LOG2` | variable | `float` | The inverse of log(2.0). |
| `RENDER_RASTER_FRAGMENT_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Fragment shader source code to render a source raster as either a floating-point raster or a normal-map raster. |
| `RENDER_SPHERE_NORMALS_FRAGMENT_SHADER_SOURCE_FILE_NAME` | variable | `QString` | Fragment shader source code to render sphere normals as part of clearing a render target before rendering a normal-map raster. |
| `GPLATES_OPENGL_GLMULTIRESOLUTIONRASTER_H` | macro | `None` | — |

## Notes

- **Crack avoidance is the invariant most likely to be broken by an edit.**
  Adjacent tiles must produce *bitwise identical* vertex positions along their
  shared edge or the raster shows intermittent gaps. Three things enforce it:
  tile boundaries are integer geo (pixel) coordinates of the original raster;
  `load_vertices_into_tile_vertex_buffer` special-cases the last row and column
  to use `x_geo_end`/`y_geo_end` exactly instead of accumulating
  `i * x_pixels_per_quad`; and `d_num_texels_per_vertex` is a 16:16 fixed-point
  value rather than a float, so two adjacent tiles cannot disagree about how
  many vertices go along a common edge. Any change to the vertex generation path
  has to preserve all three.
- **The caller owns the frame-to-frame cache.** `render` returns a
  `cache_handle_type` that must be kept alive until *after* the next `render`
  call — assign over it, do not clear it first. Dropping it early makes every
  tile texture and vertex buffer eligible for recycling each frame. Note that
  `ClientCacheTile` always retains the `GLMultiResolutionRasterSource` cache
  handle but retains *our* tile texture only when `d_cache_tile_textures` is not
  `CACHE_TILE_TEXTURES_NONE`.
- **`CACHE_TILE_TEXTURES_ENTIRE_LEVEL_OF_DETAIL_PYRAMID` disables recycling
  outright.** The constructor calls `set_min_num_objects(d_tiles.size())` on
  both caches, so memory grows to hold every tile that is ever touched, across
  every level. The header is explicit that this is for repeated data analysis
  over a whole floating-point raster (raster co-registration), never for visual
  display.
- **Vertices are written by placement `new` into mapped, write-only buffer
  memory.** `load_vertices_into_tile_vertex_buffer` maps the vertex buffer with
  `GLBuffer::ACCESS_WRITE_ONLY` and constructs each vertex directly in place;
  that memory may be video memory and must never be read back. It is filled with
  `USAGE_STATIC_DRAW` deliberately, to get the driver to place it in fast
  memory, even though a recycled tile rewrites it.
- **The OBB tree is stored bottom-up in a flat vector,** so the root node is the
  *last* element of `obb_tree_nodes`, not the first — always enter through
  `obb_tree_root_node_index`. `OBBTreeNode` overlays the two child indices and
  the tile handle in a union, discriminated by `is_leaf_node`.
- **Tile textures are never mipmapped and are filtered `GL_NEAREST` in both
  directions.** The auto-mipmap path is `#if 0`'d out because it misbehaved when
  the source was itself a render-target texture (age grid mask), and the class
  relies on its own LOD pyramid instead. Anisotropic filtering is the only
  filtering applied, and only to non-floating-point textures when the extension
  is present and `FIXED_POINT_TEXTURE_FILTER_ANISOTROPIC` was requested. The
  Doxygen on `DEFAULT_FIXED_POINT_TEXTURE_FILTER` still says "bilinear"; the
  enum comment nearby corrects this to nearest, which is what the code does.
- **Staleness tracking runs through the source, not through this class.**
  `get_subject_token` simply forwards the raster source's token — valid only
  because there is exactly one input source, as the comment notes. Each
  `LevelOfDetailTile` holds a mutable `ObserverToken`, and a tile texture that
  survived in the cache is reloaded when the source token has moved on.
- **`supports_normal_map_source` and `supports_scalar_field_depth_layers_source`
  memoise into function-local statics** — the first `GLRenderer` to ask fixes
  the answer for the whole process, including the test compile-and-link of the
  fragment shader. `create_shader_program_if_necessary` asserts that the real
  compile succeeds, so a client that skips the `supports_*` call and runs on
  hardware that cannot compile the shader gets an assertion, not a graceful
  fallback.
- **Latitude clamping is conditional.** `convert_pixel_coord_to_geographic_coord`
  clamps latitudes outside ±90 (rasters whose extent is, say, [-90.05, 90.05]),
  but only compensates the `v` texture coordinate when the coordinate
  transformation is the identity and the georeferencing has no rotation or skew
  terms. Longitude is wrapped into [-360, 360] rather than clamped, so a raster
  spanning [-0.05, 360.05] keeps its seamless wrap.
- Per-tile vertex counts are capped at 256 in each direction so the total stays
  inside the `GLushort` index range, and the index buffers themselves are shared
  across every tile with the same vertex dimensions via
  `d_vertex_element_buffers`.
- `render` wraps its work in a `GLRenderer::StateBlockScope`, so it leaves the
  renderer state as it found it.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLMultiResolutionCubeRaster](GLMultiResolutionCubeRaster.md) | opengl | 24 |
| [opengl/GLScalarField3DGenerator](GLScalarField3DGenerator.md) | opengl | 24 |
| [opengl/GLVisualLayers](GLVisualLayers.md) | opengl | 16 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 16 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 14 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 13 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](GLMultiResolutionCubeReconstructedRaster.md) | opengl | 8 |
| [presentation/LayerOutputRenderer](../presentation/LayerOutputRenderer.md) | presentation | 7 |
| [maths/deprecated/GridOnSphere](../maths/deprecated/GridOnSphere.md) | maths | 6 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 6 |
| [maths/GreatCircle](../maths/GreatCircle.md) | maths | 5 |
| [maths/EllipseGenerator](../maths/EllipseGenerator.md) | maths | 4 |
| [maths/SmallCircle](../maths/SmallCircle.md) | maths | 1 |

## Related

**Shader programs compiled by this unit**

| Shader unit | Component |
|---|---|
| [shaders/multi_resolution_raster](../qt-resources/opengl/multi_resolution_raster.md) | shaders |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLMultiResolutionRaster.h
python scripts/gpq.py def GPlatesOpenGL::GLMultiResolutionRaster --body
python scripts/gpq.py uses GLMultiResolutionRaster --kind class
python scripts/gpq.py hier GLMultiResolutionRaster
```

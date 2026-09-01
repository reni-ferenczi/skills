# opengl

[Book TOC](../TOC.md)

88 unit page(s), 158 source file(s) documented here, 1 further file(s) listed below.

## Overview

[[[PROSE component unit=component:opengl tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

### GLBuffer

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLBuffer](../src/opengl/GLBuffer.md) | 1 | 841 | 2451 | abstract OpenGL buffer-object layer plus the factory that falls back to client memory |
| [GLBufferImpl](../src/opengl/GLBufferImpl.md) | 1 | 401 | 438 | client-memory fallback used when the driver has no buffer-object extension |
| [GLBufferObject](../src/opengl/GLBufferObject.md) | 1 | 1078 | 218 | native buffer-object implementation, including the orphan-and-append streaming logic |

### GLCube

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLCubeMeshGenerator](../src/opengl/GLCubeMeshGenerator.md) | 2 | 433 | 9 | Generates seam-free spherical mesh vertices gridded to cube subdivision tiles |
| [GLCubeSubdivision](../src/opengl/GLCubeSubdivision.md) | 2 | 709 | 42 | Computes view/projection transforms and spherical bounds for cube quad-tree tiles |
| [GLCubeSubdivisionCache](../src/opengl/GLCubeSubdivisionCache.md) | 2 | 652 | 92 | Memoises GLCubeSubdivision queries per cube quad-tree node, opt-in per query kind |

### GLMulti

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLMultiResolutionCubeMesh](../src/opengl/GLMultiResolutionCubeMesh.md) | 2 | 744 | 40 | Pre-generated cube quad-tree mesh with clip-texture fallback past its max depth |
| [GLMultiResolutionCubeRaster](../src/opengl/GLMultiResolutionCubeRaster.md) | 2 | 1546 | 142 | Re-samples a georeferenced GLMultiResolutionRaster into the cube-map quad tree scheme |
| [GLMultiResolutionCubeRasterInterface](../src/opengl/GLMultiResolutionCubeRasterInterface.md) | 2 | 253 | 44 | Common cube-map raster interface shared by plain and reconstructed cube rasters |
| [GLMultiResolutionCubeReconstructedRaster](../src/opengl/GLMultiResolutionCubeReconstructedRaster.md) | 2 | 986 | 24 | Adapts a reconstructed raster to the GLMultiResolutionCubeRasterInterface, with unbounded traversal depth |
| [GLMultiResolutionMapCubeMesh](../src/opengl/GLMultiResolutionMapCubeMesh.md) | 2 | 1387 | 22 | Map-projected counterpart of GLMultiResolutionCubeMesh, tracking projection distortion per tile |
| [GLMultiResolutionRaster](../src/opengl/GLMultiResolutionRaster.md) | 1 | 3847 | 137 | georeferenced raster as a level-of-detail pyramid of texture tiles meshed onto the globe |
| [GLMultiResolutionRasterInterface](../src/opengl/GLMultiResolutionRasterInterface.md) | 2 | 287 | 31 | Common level-of-detail-driven render interface for plain and reconstructed rasters |
| [GLMultiResolutionRasterMapView](../src/opengl/GLMultiResolutionRasterMapView.md) | 2 | 1048 | 26 | Draws a cube raster onto a 2D map projection via a matched mesh cube quad tree |
| [GLMultiResolutionRasterSource](../src/opengl/GLMultiResolutionRasterSource.md) | 2 | 244 | 57 | Pluggable tile-data source interface consumed by GLMultiResolutionRaster |
| [GLMultiResolutionStaticPolygonReconstructedRaster](../src/opengl/GLMultiResolutionStaticPolygonReconstructedRaster.md) | 2 | 4129 | 49 | Renders a raster reconstructed onto present-day static polygon meshes, tile by tile |

### GLObject

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLObject](../src/opengl/GLObject.md) | 2 | 68 | 96 | Common non-copyable base for every wrapped OpenGL resource type |
| [GLObjectResource](../src/opengl/GLObjectResource.md) | 2 | 118 | 49 | RAII wrapper that queues an OpenGL resource handle for deferred deallocation |
| [GLObjectResourceManager](../src/opengl/GLObjectResourceManager.md) | 2 | 123 | 15 | Allocates OpenGL resource handles and batches their deallocation into a queue |

### GLPixel

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLPixelBuffer](../src/opengl/GLPixelBuffer.md) | 1 | 412 | 504 | interface for moving pixels between a GLBuffer and the framebuffer or a texture |
| [GLPixelBufferImpl](../src/opengl/GLPixelBufferImpl.md) | 2 | 761 | 7 | Client-memory fallback pixel buffer used when pixel buffer objects are unsupported |
| [GLPixelBufferObject](../src/opengl/GLPixelBufferObject.md) | 2 | 635 | 22 | Pixel buffer implementation backed by a real GL\_ARB\_pixel\_buffer\_object buffer |

### GLRender

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLRenderBufferObject](../src/opengl/GLRenderBufferObject.md) | 2 | 301 | 46 | RAII wrapper around an OpenGL renderbuffer object for use as a depth/stencil target |
| [GLRenderTarget](../src/opengl/GLRenderTarget.md) | 2 | 369 | 49 | Fixed-size off-screen texture render target, shareable across OpenGL contexts |
| [GLRenderTargetImpl](../src/opengl/GLRenderTargetImpl.md) | 2 | 673 | 17 | Per-context framebuffer-object implementation shared by GLRenderTarget and GLScreenRenderTarget |

### GLScalar

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLScalarField3D](../src/opengl/GLScalarField3D.md) | 2 | 5485 | 23 | Ray-traces a cube-mapped 3D sub-surface scalar field as an iso-surface or cross-sections |
| [GLScalarField3DGenerator](../src/opengl/GLScalarField3DGenerator.md) | 2 | 1248 | 8 | Builds a cube-map scalar-field file from a stack of georeferenced depth-layer rasters |
| [GLScalarFieldDepthLayersSource](../src/opengl/GLScalarFieldDepthLayersSource.md) | 2 | 1467 | 17 | Raster source that computes per-depth-layer scalar/gradient tiles for scalar-field generation |

### GLShader

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLShaderObject](../src/opengl/GLShaderObject.md) | 2 | 568 | 104 | Wraps a single compiled OpenGL shader stage (vertex, fragment or geometry) |
| [GLShaderProgramUtils](../src/opengl/GLShaderProgramUtils.md) | 2 | 513 | 154 | Helper functions to compile shader stages and link them into GLProgramObjects |
| [GLShaderSource](../src/opengl/GLShaderSource.md) | 2 | 433 | 215 | Assembles multi-segment GLSL source, managing the #version/#extension directives and file provenance |

### GLState

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLState](../src/opengl/GLState.md) | 1 | 2918 | 387 | sparse array of immutable GLStateSets standing for the whole OpenGL state; empty slot means the GL default |
| [GLStateSet](../src/opengl/GLStateSet.md) | 2 | 134 | 272 | Abstract base for one piece of tracked OpenGL global state, diffed against the last-applied state |
| [GLStateSetKeys](../src/opengl/GLStateSetKeys.md) | 2 | 891 | 253 | Maps every tracked piece of OpenGL state to a dense integer key for GLState's array lookups |
| [GLStateSetStore](../src/opengl/GLStateSetStore.md) | 2 | 118 | 83 | One ObjectPool per concrete GLStateSet subclass, for pooled allocation of per-frame state objects |
| [GLStateSets](../src/opengl/GLStateSets.md) | 1 | 5977 | 110 | the leaves of the state system: one class per slice of OpenGL global state, each emitting its own transitions |
| [GLStateStore](../src/opengl/GLStateStore.md) | 3 | 198 | 6 | Manages allocation and reuse of GLState objects through object pooling |

### GLVertex

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLVertex](../src/opengl/GLVertex.md) | 1 | 767 | 239 | the backend's interleaved vertex layouts and the specialisations that bind each one to a vertex array |
| [GLVertexArray](../src/opengl/GLVertexArray.md) | 2 | 601 | 60 | Abstract vertex/attribute binding and indexed-draw interface, hiding VAO extension support |
| [GLVertexArrayImpl](../src/opengl/GLVertexArrayImpl.md) | 2 | 611 | 4 | Fallback vertex array that replays recorded state via a compiled draw state when VAOs are unsupported |
| [GLVertexArrayObject](../src/opengl/GLVertexArrayObject.md) | 2 | 782 | 29 | Vertex array backed by a real native vertex array object, one per OpenGL context |
| [GLVertexBuffer](../src/opengl/GLVertexBuffer.md) | 2 | 281 | 77 | Extension-agnostic interface interpreting a GLBuffer as vertex attribute data |
| [GLVertexBufferImpl](../src/opengl/GLVertexBufferImpl.md) | 3 | 383 | 1 | Fallback vertex buffer implementation for systems without hardware buffer object support |
| [GLVertexBufferObject](../src/opengl/GLVertexBufferObject.md) | 2 | 378 | 14 | Vertex buffer implementation backed by a real GL\_ARRAY\_BUFFER\_ARB object |
| [GLVertexElementBuffer](../src/opengl/GLVertexElementBuffer.md) | 2 | 238 | 77 | Abstract interface for a GLBuffer interpreted as index data, plus per-type index traits |
| [GLVertexElementBufferImpl](../src/opengl/GLVertexElementBufferImpl.md) | 3 | 208 | 1 | Fallback element buffer implementation for systems without hardware buffer object support |
| [GLVertexElementBufferObject](../src/opengl/GLVertexElementBufferObject.md) | 3 | 245 | 4 | Hardware-accelerated element buffer using GPU-resident storage |

### Open

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [OpenGL](../src/opengl/OpenGL.md) | 2 | 95 | 29 | Platform-specific OpenGL header shim plus small portability macros |
| [OpenGLBadAllocException](../src/opengl/OpenGLBadAllocException.md) | 3 | 78 | 0 | Exception thrown when OpenGL fails to allocate GPU memory |
| [OpenGLException](../src/opengl/OpenGLException.md) | 2 | 76 | 17 | General-purpose exception type for OpenGL-specific failures |

### Other

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLAgeGridMaskSource](../src/opengl/GLAgeGridMaskSource.md) | 2 | 1289 | 73 | Derives a per-reconstruction-time age-grid mask texture via a three-pass GPU render |
| [GLCapabilities](../src/opengl/GLCapabilities.md) | 1 | 1073 | 1279 | the per-process snapshot of OpenGL extensions and limits that every fallback decision reads |
| [GLCompiledDrawState](../src/opengl/GLCompiledDrawState.md) | 2 | 149 | 242 | Opaque, context-portable bundle of a compiled OpenGL state change and draw calls |
| [GLContext](../src/opengl/GLContext.md) | 1 | 1871 | 449 | mirror of a real GL context owning the shared and non-shared object caches and resource managers |
| [GLContextImpl](../src/opengl/GLContextImpl.md) | 2 | 149 | 23 | Qt QGLWidget/QGLPixelBuffer adapters implementing the GLContext::Impl interface |
| [GLDataRasterSource](../src/opengl/GLDataRasterSource.md) | 2 | 918 | 14 | Multi-resolution raster source exposing raw floating-point raster values for analysis |
| [GLDepthRange](../src/opengl/GLDepthRange.md) | 2 | 95 | 16 | Value type for glDepthRange near/far parameters with epsilon-based equality |
| [GLFilledPolygonsGlobeView](../src/opengl/GLFilledPolygonsGlobeView.md) | 2 | 2052 | 64 | Renders reconstructed filled polygons on the globe via stencil fill and cube-quad-tree tile textures |
| [GLFilledPolygonsMapView](../src/opengl/GLFilledPolygonsMapView.md) | 2 | 775 | 30 | Renders reconstructed filled polygons on the flat 2D map via stencil fill, no tiling needed |
| [GLFrameBufferObject](../src/opengl/GLFrameBufferObject.md) | 1 | 1530 | 164 | off-screen render-target primitive wrapping a GL\_EXT\_framebuffer\_object name, with shadowed attachments |
| [GLFrustum](../src/opengl/GLFrustum.md) | 2 | 379 | 100 | Extracts the six view-frustum clip planes from a model-view-projection matrix pair |
| [GLImageUtils](../src/opengl/GLImageUtils.md) | 2 | 236 | 11 | Free functions bridging OpenGL frame buffers and text rendering to QImage |
| [GLIntersect](../src/opengl/GLIntersect.md) | 2 | 343 | 44 | Ray/sphere and sphere/OBB-vs-frustum intersection tests used for culling and LOD selection |
| [GLIntersectPrimitives](../src/opengl/GLIntersectPrimitives.md) | 2 | 1143 | 94 | Geometric primitives (plane, ray, sphere, OBB, OBB builder) used by the intersection routines |
| [GLLight](../src/opengl/GLLight.md) | 2 | 856 | 52 | Directional light shared by globe and map views, encoding map-space light direction via a cube map |
| [GLMapCubeMeshGenerator](../src/opengl/GLMapCubeMeshGenerator.md) | 2 | 369 | 87 | Projects the sphere's cube subdivision mesh onto a 2D map, quadrant by quadrant around the dateline |
| [GLMatrix](../src/opengl/GLMatrix.md) | 1 | 780 | 469 | the 4x4 column-major matrix value used at every OpenGL boundary in GPlates |
| [GLNormalMapSource](../src/opengl/GLNormalMapSource.md) | 2 | 1691 | 22 | Converts a floating-point height/scalar raster into tangent-space normal map tiles |
| [GLOffScreenContext](../src/opengl/GLOffScreenContext.md) | 2 | 742 | 24 | Off-screen rendering context, preferring a pbuffer or FBO over a QGLWidget's main framebuffer |
| [GLProgramObject](../src/opengl/GLProgramObject.md) | 1 | 2571 | 318 | linked GLSL program with name-addressed, location-cached uniform setters |
| [GLProjectionUtils](../src/opengl/GLProjectionUtils.md) | 2 | 423 | 14 | GLU-style window/model-space projection helpers built on GLViewport and GLMatrix |
| [GLRasterCoRegistration](../src/opengl/GLRasterCoRegistration.md) | 2 | 7819 | 15 | GPU render-and-reduce pipeline co-registering seed geometries against a floating-point raster |
| [GLReconstructedStaticPolygonMeshes](../src/opengl/GLReconstructedStaticPolygonMeshes.md) | 2 | 2020 | 45 | Groups reconstructed static polygons by finite rotation and readies them as GPU drawables |
| [GLRenderer](../src/opengl/GLRenderer.md) | 1 | 5962 | 830 | the one funnel for all OpenGL drawing: defers state to the next draw so redundant changes collapse |
| [GLRendererImpl](../src/opengl/GLRendererImpl.md) | 2 | 397 | 194 | Private state-block and render-target-stack machinery backing GLRenderer |
| [GLSaveRestoreFrameBuffer](../src/opengl/GLSaveRestoreFrameBuffer.md) | 2 | 623 | 5 | Saves and restores the main framebuffer's contents around using it as a render target |
| [GLScreenRenderTarget](../src/opengl/GLScreenRenderTarget.md) | 2 | 331 | 22 | Viewport-size off-screen render target (texture plus optional depth/stencil) usable across GL contexts |
| [GLStreamPrimitiveWriters](../src/opengl/GLStreamPrimitiveWriters.md) | 2 | 193 | 48 | Fixed-buffer and std::vector-backed writers sharing a common write/count/remaining interface |
| [GLStreamPrimitives](../src/opengl/GLStreamPrimitives.md) | 1 | 2308 | 580 | a glBegin/glEnd-shaped front end that streams indexed geometry straight into mapped vertex buffers |
| [GLText](../src/opengl/GLText.md) | 2 | 310 | 12 | Renders text over the OpenGL scene by suspending GLRenderer and drawing with QPainter |
| [GLTexture](../src/opengl/GLTexture.md) | 1 | 1035 | 171 | one texture name plus its cached level-0 dimensions and internal format, with context-managed lifetime |
| [GLTextureUtils](../src/opengl/GLTextureUtils.md) | 2 | 991 | 69 | Free functions to allocate and upload data into GLTexture objects, plus clip-texture helpers |
| [GLTileRender](../src/opengl/GLTileRender.md) | 2 | 487 | 64 | Iterates the tiles needed to composite a destination image larger than one render target |
| [GLTransform](../src/opengl/GLTransform.md) | 2 | 171 | 105 | Reference-counted, shareable wrapper around a GLMatrix (model-view, projection, or rotation) |
| [GLUtils](../src/opengl/GLUtils.md) | 1 | 1155 | 248 | shared renderer helpers for full-screen quads and projective texturing, plus quad-tree tile transforms |
| [GLViewport](../src/opengl/GLViewport.md) | 1 | 148 | 453 | the integer rectangle type used for both viewport and scissor throughout the rendering backend |
| [GLVisualLayers](../src/opengl/GLVisualLayers.md) | 1 | 2869 | 69 | per-layer cache of OpenGL objects that outlive a frame, keyed by the app-logic layer proxy |
| [GLVisualRasterSource](../src/opengl/GLVisualRasterSource.md) | 2 | 1150 | 3 | Multi-resolution raster source producing premultiplied-alpha RGBA8 tiles for display |


## Other files

| File | Kind | Lines |
|---|---|---|
| `src/opengl/CMakeLists.txt` | build | 173 |

## Depends on

| Component | References |
|---|---|
| [maths](maths.md) | 3183 |
| [global](global.md) | 2351 |
| [utils](utils.md) | 1679 |
| [gui](gui.md) | 969 |
| [app-logic](app-logic.md) | 616 |
| [file-io](file-io.md) | 430 |
| [property-values](property-values.md) | 348 |
| [view-operations](view-operations.md) | 243 |
| [model](model.md) | 195 |
| [unit-test](unit-test.md) | 15 |
| [system-fixes](system-fixes.md) | 10 |
| [data-mining](data-mining.md) | 6 |
| [presentation](presentation.md) | 6 |
| [qt-widgets](qt-widgets.md) | 4 |
| [canvas-tools](canvas-tools.md) | 3 |

## Used by

| Component | References |
|---|---|
| [gui](gui.md) | 1575 |
| [qt-widgets](qt-widgets.md) | 494 |
| [app-logic](app-logic.md) | 177 |
| [presentation](presentation.md) | 49 |
| [file-io](file-io.md) | 27 |
| [data-mining](data-mining.md) | 20 |
| [maths](maths.md) | 18 |
| [api](api.md) | 6 |
| [utils](utils.md) | 2 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/opengl
python scripts/gpq.py sym . --mode sub --path src/opengl --defs-only
```

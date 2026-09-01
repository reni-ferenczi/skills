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
| [GLBuffer](../src/opengl/GLBuffer.md) | 1 | 841 | 2451 | (pending) |
| [GLBufferImpl](../src/opengl/GLBufferImpl.md) | 1 | 401 | 438 | (pending) |
| [GLBufferObject](../src/opengl/GLBufferObject.md) | 1 | 1078 | 218 | (pending) |

### GLCube

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLCubeMeshGenerator](../src/opengl/GLCubeMeshGenerator.md) | 2 | 433 | 9 | (pending) |
| [GLCubeSubdivision](../src/opengl/GLCubeSubdivision.md) | 2 | 709 | 42 | (pending) |
| [GLCubeSubdivisionCache](../src/opengl/GLCubeSubdivisionCache.md) | 2 | 652 | 92 | (pending) |

### GLMulti

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLMultiResolutionCubeMesh](../src/opengl/GLMultiResolutionCubeMesh.md) | 2 | 744 | 40 | (pending) |
| [GLMultiResolutionCubeRaster](../src/opengl/GLMultiResolutionCubeRaster.md) | 2 | 1546 | 142 | (pending) |
| [GLMultiResolutionCubeRasterInterface](../src/opengl/GLMultiResolutionCubeRasterInterface.md) | 2 | 253 | 44 | (pending) |
| [GLMultiResolutionCubeReconstructedRaster](../src/opengl/GLMultiResolutionCubeReconstructedRaster.md) | 2 | 986 | 24 | (pending) |
| [GLMultiResolutionMapCubeMesh](../src/opengl/GLMultiResolutionMapCubeMesh.md) | 2 | 1387 | 22 | (pending) |
| [GLMultiResolutionRaster](../src/opengl/GLMultiResolutionRaster.md) | 1 | 3847 | 137 | (pending) |
| [GLMultiResolutionRasterInterface](../src/opengl/GLMultiResolutionRasterInterface.md) | 2 | 287 | 31 | (pending) |
| [GLMultiResolutionRasterMapView](../src/opengl/GLMultiResolutionRasterMapView.md) | 2 | 1048 | 26 | (pending) |
| [GLMultiResolutionRasterSource](../src/opengl/GLMultiResolutionRasterSource.md) | 2 | 244 | 57 | (pending) |
| [GLMultiResolutionStaticPolygonReconstructedRaster](../src/opengl/GLMultiResolutionStaticPolygonReconstructedRaster.md) | 2 | 4129 | 49 | (pending) |

### GLObject

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLObject](../src/opengl/GLObject.md) | 2 | 68 | 96 | (pending) |
| [GLObjectResource](../src/opengl/GLObjectResource.md) | 2 | 118 | 49 | (pending) |
| [GLObjectResourceManager](../src/opengl/GLObjectResourceManager.md) | 2 | 123 | 15 | (pending) |

### GLPixel

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLPixelBuffer](../src/opengl/GLPixelBuffer.md) | 1 | 412 | 504 | (pending) |
| [GLPixelBufferImpl](../src/opengl/GLPixelBufferImpl.md) | 2 | 761 | 7 | (pending) |
| [GLPixelBufferObject](../src/opengl/GLPixelBufferObject.md) | 2 | 635 | 22 | (pending) |

### GLRender

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLRenderBufferObject](../src/opengl/GLRenderBufferObject.md) | 2 | 301 | 46 | (pending) |
| [GLRenderTarget](../src/opengl/GLRenderTarget.md) | 2 | 369 | 49 | (pending) |
| [GLRenderTargetImpl](../src/opengl/GLRenderTargetImpl.md) | 2 | 673 | 17 | (pending) |

### GLScalar

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLScalarField3D](../src/opengl/GLScalarField3D.md) | 2 | 5485 | 23 | (pending) |
| [GLScalarField3DGenerator](../src/opengl/GLScalarField3DGenerator.md) | 2 | 1248 | 8 | (pending) |
| [GLScalarFieldDepthLayersSource](../src/opengl/GLScalarFieldDepthLayersSource.md) | 2 | 1467 | 17 | (pending) |

### GLShader

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLShaderObject](../src/opengl/GLShaderObject.md) | 2 | 568 | 104 | (pending) |
| [GLShaderProgramUtils](../src/opengl/GLShaderProgramUtils.md) | 2 | 513 | 154 | (pending) |
| [GLShaderSource](../src/opengl/GLShaderSource.md) | 2 | 433 | 215 | (pending) |

### GLState

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLState](../src/opengl/GLState.md) | 1 | 2918 | 387 | (pending) |
| [GLStateSet](../src/opengl/GLStateSet.md) | 2 | 134 | 272 | (pending) |
| [GLStateSetKeys](../src/opengl/GLStateSetKeys.md) | 2 | 891 | 253 | (pending) |
| [GLStateSetStore](../src/opengl/GLStateSetStore.md) | 2 | 118 | 83 | (pending) |
| [GLStateSets](../src/opengl/GLStateSets.md) | 1 | 5977 | 110 | (pending) |
| [GLStateStore](../src/opengl/GLStateStore.md) | 3 | 198 | 6 | Manages allocation and reuse of GLState objects through object pooling |

### GLVertex

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLVertex](../src/opengl/GLVertex.md) | 1 | 767 | 239 | (pending) |
| [GLVertexArray](../src/opengl/GLVertexArray.md) | 2 | 601 | 60 | (pending) |
| [GLVertexArrayImpl](../src/opengl/GLVertexArrayImpl.md) | 2 | 611 | 4 | (pending) |
| [GLVertexArrayObject](../src/opengl/GLVertexArrayObject.md) | 2 | 782 | 29 | (pending) |
| [GLVertexBuffer](../src/opengl/GLVertexBuffer.md) | 2 | 281 | 77 | (pending) |
| [GLVertexBufferImpl](../src/opengl/GLVertexBufferImpl.md) | 3 | 383 | 1 | Fallback vertex buffer implementation for systems without hardware buffer object support |
| [GLVertexBufferObject](../src/opengl/GLVertexBufferObject.md) | 2 | 378 | 14 | (pending) |
| [GLVertexElementBuffer](../src/opengl/GLVertexElementBuffer.md) | 2 | 238 | 77 | (pending) |
| [GLVertexElementBufferImpl](../src/opengl/GLVertexElementBufferImpl.md) | 3 | 208 | 1 | Fallback element buffer implementation for systems without hardware buffer object support |
| [GLVertexElementBufferObject](../src/opengl/GLVertexElementBufferObject.md) | 3 | 245 | 4 | Hardware-accelerated element buffer using GPU-resident storage |

### Open

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [OpenGL](../src/opengl/OpenGL.md) | 2 | 95 | 29 | (pending) |
| [OpenGLBadAllocException](../src/opengl/OpenGLBadAllocException.md) | 3 | 78 | 0 | Exception thrown when OpenGL fails to allocate GPU memory |
| [OpenGLException](../src/opengl/OpenGLException.md) | 2 | 76 | 17 | (pending) |

### Other

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GLAgeGridMaskSource](../src/opengl/GLAgeGridMaskSource.md) | 2 | 1289 | 73 | (pending) |
| [GLCapabilities](../src/opengl/GLCapabilities.md) | 1 | 1073 | 1279 | (pending) |
| [GLCompiledDrawState](../src/opengl/GLCompiledDrawState.md) | 2 | 149 | 242 | (pending) |
| [GLContext](../src/opengl/GLContext.md) | 1 | 1871 | 449 | (pending) |
| [GLContextImpl](../src/opengl/GLContextImpl.md) | 2 | 149 | 23 | (pending) |
| [GLDataRasterSource](../src/opengl/GLDataRasterSource.md) | 2 | 918 | 14 | (pending) |
| [GLDepthRange](../src/opengl/GLDepthRange.md) | 2 | 95 | 16 | (pending) |
| [GLFilledPolygonsGlobeView](../src/opengl/GLFilledPolygonsGlobeView.md) | 2 | 2052 | 64 | (pending) |
| [GLFilledPolygonsMapView](../src/opengl/GLFilledPolygonsMapView.md) | 2 | 775 | 30 | (pending) |
| [GLFrameBufferObject](../src/opengl/GLFrameBufferObject.md) | 1 | 1530 | 164 | (pending) |
| [GLFrustum](../src/opengl/GLFrustum.md) | 2 | 379 | 100 | (pending) |
| [GLImageUtils](../src/opengl/GLImageUtils.md) | 2 | 236 | 11 | (pending) |
| [GLIntersect](../src/opengl/GLIntersect.md) | 2 | 343 | 44 | (pending) |
| [GLIntersectPrimitives](../src/opengl/GLIntersectPrimitives.md) | 2 | 1143 | 94 | (pending) |
| [GLLight](../src/opengl/GLLight.md) | 2 | 856 | 52 | (pending) |
| [GLMapCubeMeshGenerator](../src/opengl/GLMapCubeMeshGenerator.md) | 2 | 369 | 87 | (pending) |
| [GLMatrix](../src/opengl/GLMatrix.md) | 1 | 780 | 469 | (pending) |
| [GLNormalMapSource](../src/opengl/GLNormalMapSource.md) | 2 | 1691 | 22 | (pending) |
| [GLOffScreenContext](../src/opengl/GLOffScreenContext.md) | 2 | 742 | 24 | (pending) |
| [GLProgramObject](../src/opengl/GLProgramObject.md) | 1 | 2571 | 318 | (pending) |
| [GLProjectionUtils](../src/opengl/GLProjectionUtils.md) | 2 | 423 | 14 | (pending) |
| [GLRasterCoRegistration](../src/opengl/GLRasterCoRegistration.md) | 2 | 7819 | 15 | (pending) |
| [GLReconstructedStaticPolygonMeshes](../src/opengl/GLReconstructedStaticPolygonMeshes.md) | 2 | 2020 | 45 | (pending) |
| [GLRenderer](../src/opengl/GLRenderer.md) | 1 | 5962 | 830 | (pending) |
| [GLRendererImpl](../src/opengl/GLRendererImpl.md) | 2 | 397 | 194 | (pending) |
| [GLSaveRestoreFrameBuffer](../src/opengl/GLSaveRestoreFrameBuffer.md) | 2 | 623 | 5 | (pending) |
| [GLScreenRenderTarget](../src/opengl/GLScreenRenderTarget.md) | 2 | 331 | 22 | (pending) |
| [GLStreamPrimitiveWriters](../src/opengl/GLStreamPrimitiveWriters.md) | 2 | 193 | 48 | (pending) |
| [GLStreamPrimitives](../src/opengl/GLStreamPrimitives.md) | 1 | 2308 | 580 | (pending) |
| [GLText](../src/opengl/GLText.md) | 2 | 310 | 12 | (pending) |
| [GLTexture](../src/opengl/GLTexture.md) | 1 | 1035 | 171 | (pending) |
| [GLTextureUtils](../src/opengl/GLTextureUtils.md) | 2 | 991 | 69 | (pending) |
| [GLTileRender](../src/opengl/GLTileRender.md) | 2 | 487 | 64 | (pending) |
| [GLTransform](../src/opengl/GLTransform.md) | 2 | 171 | 105 | (pending) |
| [GLUtils](../src/opengl/GLUtils.md) | 1 | 1155 | 248 | (pending) |
| [GLViewport](../src/opengl/GLViewport.md) | 1 | 148 | 453 | (pending) |
| [GLVisualLayers](../src/opengl/GLVisualLayers.md) | 1 | 2869 | 69 | (pending) |
| [GLVisualRasterSource](../src/opengl/GLVisualRasterSource.md) | 2 | 1150 | 3 | (pending) |


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

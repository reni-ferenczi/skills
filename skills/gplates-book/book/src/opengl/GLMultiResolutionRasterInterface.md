# GLMultiResolutionRasterInterface

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1561 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLMultiResolutionRasterInterface.h` | C++ | 224 |
| `src/opengl/GLMultiResolutionRasterInterface.cc` | C++ | 63 |

## Overview

`GLMultiResolutionRasterInterface` is the common interface for anything that behaves as a level-of-detail raster that can be rendered into the current view — implemented by `GLMultiResolutionRaster` for a plain raster and by `GLMultiResolutionStaticPolygonReconstructedRaster` for a reconstructed one. It centres on two things: computing which level of detail a given viewport/transform combination needs (`get_level_of_detail()`, implemented per subclass), and rendering the tiles for that level (`render()`).

The non-virtual convenience overload of `render()` (implemented in the `.cc`) chains the two steps together: it reads the renderer's current model-view, projection and viewport state, asks the subclass for the exact unclamped level of detail via `get_level_of_detail()`, clamps it with `clamp_level_of_detail()`, and renders at that integer level. `clamp_level_of_detail()` differs between raster kinds — a plain raster clamps to `[0, get_num_levels_of_detail() - 1]`, but a reconstructed raster allows levels down to negative infinity, because reconstruction can be driven by an age-grid mask at higher resolution than the source raster itself. `get_viewport_dimension_scale()` inverts the level-of-detail calculation to answer a different question — what viewport size would make a *given* level of detail exactly fill it — which is the model used for processing at a user-chosen, fixed level of detail (as opposed to visual display, which adapts level of detail to a fixed viewport size).

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLMultiResolutionRasterInterface`](#gplatesopenglglmultiresolutionrasterinterface) | class | [`GPlatesUtils::ReferenceCount<GLMultiResolutionRasterInterface>`](../utils/ReferenceCount.md) | — | 2 | Interface for a (possibly reconstructed) multi-resolution raster. |

## Members

### `GPlatesOpenGL::GLMultiResolutionRasterInterface`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLMultiResolutionRasterInterface>` | public | A convenience typedef for a shared pointer to a non-const GLMultiResolutionRasterInterface. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLMultiResolutionRasterInterface>` | public | A convenience typedef for a shared pointer to a const GLMultiResolutionRasterInterface. |
| `cache_handle_type` | typedef | `boost::shared_ptr<void>` | public | Typedef for an opaque object that caches a particular render of this raster. |
| `~GLMultiResolutionRasterInterface()` | destructor | `None` | public | — |
| `get_subject_token` | field | `GPlatesUtils::SubjectToken` | public | Returns a subject token that clients can observe to see if they need to update themselves (such as any cached data we render for them) by getting us to re-render. |
| `get_num_levels_of_detail()` | method | `unsigned int` | public | Returns the number of levels of detail. |
| `get_level_of_detail( const GLMatrix &model_view_transform, const GLMatrix &projection_transform, const GLViewport &viewport, float level_of_detail_bias = 0.0f)` | method | `float` | public | Returns the unclamped exact floating-point level-of-detail that theoretically represents the exact level-of-detail that would be required to fulfill the resolution needs of a render target (as defined by the specified viewport and ... |
| `get_viewport_dimension_scale( const GLMatrix &model_view_transform, const GLMatrix &projection_transform, const GLViewport &viewport, float level_of_detail)` | method | `float` | public | Given the specified viewport (and model-view/projection matrices) and the desired level-of-detail this method determines the scale factor that needs to be applied to viewport width and height such that it is sized correctly to contain the ... |
| `clamp_level_of_detail( float level_of_detail)` | method | `float` | public | Takes an unclamped level-of-detail (see get\_level\_of\_detail) and clamps it to lie within a valid range of levels: 1) Regular raster: the range \[0, get\_num\_levels\_of\_detail - 1\], 2) Reconstructed raster: the range \[-Infinity, ... |
| `render( GLRenderer &renderer, cache_handle_type &cache_handle, float level_of_detail_bias = 0.0f)` | method | `bool` | public | Renders all tiles visible in the view frustum (determined by the current viewport and model-view/projection transforms of renderer) and returns true if any tiles were rendered. cache\_handle\_type should be kept alive until the next call to ... |
| `render( GLRenderer &renderer, float level_of_detail, cache_handle_type &cache_handle)` | method | `bool` | public | Renders all tiles visible in the view frustum (determined by the current model-view/projection transforms of renderer) and returns true if any tiles were rendered. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLMULTIRESOLUTIONRASTERINTERFACE_H` | macro | `None` | — |

## Notes

The `render(renderer, level_of_detail, cache_handle)` overload throws if `level_of_detail` is outside the valid range — callers must pass it through `clamp_level_of_detail()` first, which the convenience `render()` overload does automatically. `level_of_detail_bias` is a log2 value, not a linear factor: a bias of 1.0 halves the resolution used (e.g. 256x256 instead of 512x512) and 2.0 quarters it. The `cache_handle_type` returned by `render()` is meant to be kept alive until the *next* call to `render()`, not discarded immediately, since it lets the implementation reuse the previous frame's cached tiles.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 12 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 9 |
| [opengl/GLMultiResolutionRaster](GLMultiResolutionRaster.md) | opengl | 7 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 4 |
| [data-mining/DataSelector](../data-mining/DataSelector.md) | data-mining | 1 |
| [opengl/GLScalarField3DGenerator](GLScalarField3DGenerator.md) | opengl | 1 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLMultiResolutionRasterInterface.h
python scripts/gpq.py def GPlatesOpenGL::GLMultiResolutionRasterInterface --body
python scripts/gpq.py uses GLMultiResolutionRasterInterface --kind class
python scripts/gpq.py hier GLMultiResolutionRasterInterface
```

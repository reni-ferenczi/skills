# multi_resolution_raster_map_view

[Book TOC](../../../TOC.md) · [shaders](../../../components/shaders.md) · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-resources/opengl/multi_resolution_raster_map_view/render_tile_to_scene_fragment_shader.glsl` | GLSL | 67 |
| `src/qt-resources/opengl/multi_resolution_raster_map_view/render_tile_to_scene_vertex_shader.glsl` | GLSL | 38 |

## Overview

`GLMultiResolutionRasterMapView` uses this pair to draw a raster's cube-map tiles onto the flat 2D map projections, as the map-view counterpart to `multi_resolution_raster`'s globe-side tile compositing. It is deliberately narrower in scope: it supports the same `ENABLE_CLIPPING` and `SOURCE_RASTER_IS_FLOATING_POINT` compile-time variants (clip-texture masking, and bilinear filtering of packed data/coverage floating-point rasters) but has no lighting or normal-map handling, because the map view's lighting is either constant across the scene or computed elsewhere.

The vertex shader calls `ftransform()` instead of multiplying by `gl_ModelViewProjectionMatrix` directly, matching the fixed-function pipeline's vertex transform bit-for-bit so this shader can be swapped in without shifting geometry relative to anything still rendered through the fixed-function path.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

*None.*

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

**Compiled by**

| Unit | Component |
|---|---|
| [opengl/GLMultiResolutionRasterMapView](../../opengl/GLMultiResolutionRasterMapView.md) | opengl |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-resources/opengl/multi_resolution_raster_map_view/render_tile_to_scene_fragment_shader.glsl
python scripts/gpq.py grep uniform --category shader --path src/qt-resources/opengl/multi_resolution_raster_map_view
```

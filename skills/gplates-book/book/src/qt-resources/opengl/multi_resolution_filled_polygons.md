# multi_resolution_filled_polygons

[Book TOC](../../../TOC.md) · [shaders](../../../components/shaders.md) · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-resources/opengl/multi_resolution_filled_polygons/render_tile_to_scene_fragment_shader.glsl` | GLSL | 84 |
| `src/qt-resources/opengl/multi_resolution_filled_polygons/render_tile_to_scene_vertex_shader.glsl` | GLSL | 48 |

## Overview

`GLFilledPolygonsGlobeView` renders filled polygons by first rasterising them into cube-map tile textures and then drawing those tiles onto the globe; this pair is the second stage, projecting a tile texture back onto the scene geometry with `texture2DProj` to undo the cube-map's non-uniform texture-coordinate scaling. An optional clip texture (`ENABLE_CLIPPING`) masks out fragments outside the current tile's region, and an optional `SURFACE_LIGHTING` branch applies the shared Lambert diffuse term using the interpolated world-space position as the sphere normal.

The fragment shader corrects a specific artefact of tile bilinear filtering: because texels outside a filled polygon are black with zero alpha, bilinear sampling near a polygon edge blends real colour with black, producing an RGB value that is scaled down twice (once for anti-aliasing coverage, once from the black neighbour) once alpha blending is applied on top. The shader undoes the second scaling by dividing the sampled RGB back out by its own alpha, then discards fully-transparent fragments outright as a cheap early-out.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

*None.*

## Notes

The RGB-divide-by-alpha edge fix relies on the tile texture being a regular fixed-point colour texture; the shader's own comment notes it would not work for the floating-point "data" textures used elsewhere, which pack a value and coverage into separate channels instead of using alpha blending.

## Used by

*Nothing in the tree references this unit.*

## Related

**Compiled by**

| Unit | Component |
|---|---|
| [opengl/GLFilledPolygonsGlobeView](../../opengl/GLFilledPolygonsGlobeView.md) | opengl |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-resources/opengl/multi_resolution_filled_polygons/render_tile_to_scene_fragment_shader.glsl
python scripts/gpq.py grep uniform --category shader --path src/qt-resources/opengl/multi_resolution_filled_polygons
```

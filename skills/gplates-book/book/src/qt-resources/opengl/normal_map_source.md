# normal_map_source

[Book TOC](../../../TOC.md) · [shaders](../../../components/shaders.md) · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-resources/opengl/normal_map_source/generate_normal_map_fragment_shader.glsl` | GLSL | 110 |
| `src/qt-resources/opengl/normal_map_source/generate_normal_map_vertex_shader.glsl` | GLSL | 43 |

## Overview

`GLNormalMapSource` uses this pair to derive a normal-map texture from a height-field raster, so rasters supplied as elevation data can be lit the same way as rasters supplied with ready-made normal maps. The fragment shader estimates the surface gradient at each texel from its eight neighbours (a Sobel-like central-difference scheme) rather than just the immediate left/right and up/down pairs, averaging whichever of the three horizontal (or vertical) neighbour pairs actually have height coverage, so a texel with partial data still gets a usable gradient instead of one skewed by missing samples. A texel with no coverage at all is discarded outright, leaving the render target's pre-existing default normal in place.

The vertex shader's only job is to remap normal-map texture coordinates into height-field texture coordinates, because the height-field texture is padded with extra border texels beyond what the normal map covers (needed by the fragment shader's neighbour sampling) and because a normal-map tile near the edge of the source raster may only be partially filled.

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
| [opengl/GLNormalMapSource](../../opengl/GLNormalMapSource.md) | opengl |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-resources/opengl/normal_map_source/generate_normal_map_fragment_shader.glsl
python scripts/gpq.py grep uniform --category shader --path src/qt-resources/opengl/normal_map_source
```

# light

[Book TOC](../../../TOC.md) · [shaders](../../../components/shaders.md) · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-resources/opengl/light/render_map_view_light_direction_fragment_shader.glsl` | GLSL | 37 |
| `src/qt-resources/opengl/light/render_map_view_light_direction_vertex_shader.glsl` | GLSL | 42 |

## Overview

`GLLight` uses this pair to precompute a directional light's direction as a function of position on the map, storing the result in a cube texture that other shaders (for example the normal-mapped raster fragment shader) sample by world-space sphere normal instead of recomputing the light direction themselves. This exists because a 2D map view can rotate independently of the light, so the light direction relative to the map is not constant the way it is for the ambient/diffuse shortcut used elsewhere in map-view lighting.

The vertex shader takes the light direction in view-space and rotates it into world-space using the inverse of `gl_ModelViewMatrix`. Rather than compute that inverse itself, it repurposes the fixed-function `GL_MODELVIEW` matrix slot to hold the view transform, letting OpenGL's driver supply `gl_ModelViewMatrixInverse` for free. The fragment shader just outputs that direction unchanged per texel of the cube map, remapped from `[-1,1]` to `[0,1]` for storage in an unsigned 8-bit render target.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

*None.*

## Notes

The vertex shader's trick of loading the view transform into `GL_MODELVIEW` to get a free matrix inverse means callers must not rely on `gl_ModelViewMatrix` here for anything else — it does not hold an actual model-view transform for this draw.

## Used by

*Nothing in the tree references this unit.*

## Related

**Compiled by**

| Unit | Component |
|---|---|
| [opengl/GLLight](../../opengl/GLLight.md) | opengl |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-resources/opengl/light/render_map_view_light_direction_fragment_shader.glsl
python scripts/gpq.py grep uniform --category shader --path src/qt-resources/opengl/light
```

# multi_resolution_raster

[Book TOC](../../../TOC.md) · [shaders](../../../components/shaders.md) · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-resources/opengl/multi_resolution_raster/render_raster_fragment_shader.glsl` | GLSL | 97 |
| `src/qt-resources/opengl/multi_resolution_raster/render_sphere_normals_fragment_shader.glsl` | GLSL | 44 |

## Overview

`GLMultiResolutionRaster` uses these two fragment shaders (paired with a shared vertex shader not part of this unit) to populate cube-map tiles from a source raster before the tiles are draped onto the globe. `render_raster_fragment_shader.glsl` is compiled in one of three mutually exclusive modes selected by preprocessor defines: `SOURCE_RASTER_IS_FLOATING_POINT` bilinearly filters a data raster whose value and coverage are packed into the red/green channels (needed because older hardware has no native bilinear filtering for floating-point textures); `SURFACE_NORMALS` converts a tangent-space normal sampled from a normal-map raster into world-space, using per-fragment tangent/binormal/normal vectors interpolated from the vertex shader; `SCALAR_GRADIENT` combines a scalar and a partially pre-computed gradient from the source texture with the same tangent frame to produce a full world-space gradient.

`render_sphere_normals_fragment_shader.glsl` is a separate, much simpler program used to clear a render target with the globe's own unperturbed sphere normal before a normal-map raster is drawn into it — so that any texels a *regional* normal-map raster does not cover still hold a sensible default normal rather than whatever was left in the buffer.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

*None.*

## Notes

The three `render_raster_fragment_shader.glsl` modes are mutually exclusive at compile time; the caller must define exactly one of `SOURCE_RASTER_IS_FLOATING_POINT`, `SURFACE_NORMALS`, or `SCALAR_GRADIENT` (or none, for a plain colour raster) rather than combining them.

## Used by

*Nothing in the tree references this unit.*

## Related

**Compiled by**

| Unit | Component |
|---|---|
| [opengl/GLMultiResolutionRaster](../../opengl/GLMultiResolutionRaster.md) | opengl |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-resources/opengl/multi_resolution_raster/render_raster_fragment_shader.glsl
python scripts/gpq.py grep uniform --category shader --path src/qt-resources/opengl/multi_resolution_raster
```

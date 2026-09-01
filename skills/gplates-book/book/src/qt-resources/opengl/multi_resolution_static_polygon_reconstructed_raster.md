# multi_resolution_static_polygon_reconstructed_raster

[Book TOC](../../../TOC.md) · [shaders](../../../components/shaders.md) · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-resources/opengl/multi_resolution_static_polygon_reconstructed_raster/render_tile_to_scene_fragment_shader.glsl` | GLSL | 243 |
| `src/qt-resources/opengl/multi_resolution_static_polygon_reconstructed_raster/render_tile_to_scene_vertex_shader.glsl` | GLSL | 97 |

## Overview

`GLMultiResolutionStaticPolygonReconstructedRaster` uses this pair to draw a raster that has been reconstructed (each static polygon carrying its own plate rotation) onto the globe or map, one tile at a time. It is the most heavily parameterised shader in `qt-resources/opengl`: a single source file is compiled into many variants by combining preprocessor defines (`USING_AGE_GRID`, `GENERATE_AGE_MASK`, `ACTIVE_POLYGONS`, `SOURCE_RASTER_IS_FLOATING_POINT`, `SURFACE_LIGHTING`, `MAP_VIEW`, `USING_NORMAL_MAP`, `NO_DIRECTIONAL_LIGHT_FOR_NORMAL_MAPS`), each combination chosen by the C++ class at run time to match the raster and view being drawn.

Two independent features layer on top of the base tile-compositing (clip-texture masking, then optional floating-point bilinear filtering, matching `multi_resolution_raster_map_view`). An age grid, when present, tests a per-fragment reconstruction age against the raster's oceanic-crust age either by sampling a pre-generated mask texture or by bilinearly interpolating four raw age/coverage samples and comparing each against `reconstruction_time` before blending (`GENERATE_AGE_MASK`); fragments that fail the age test, or whose age coverage is zero, are discarded so stale data is never drawn. Surface lighting, when present, needs a per-fragment normal: without a normal map it uses the polygon's rotated sphere normal directly; with a normal map it samples a tangent-space normal and rotates it either into world-space (map view, via `plate_rotation_quaternion` and a light-direction cube texture built by `light`) or works in model-space (globe view, more efficient, by reverse-rotating the light direction once per vertex instead of the normal per fragment).

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

*None.*

## Notes

The premultiplied-alpha convention differs by texture format: fixed-point RGBA tiles carry pre-multiplied alpha (so the age factor must also be pre-multiplied in), while floating-point data/coverage tiles keep coverage as a separate green channel and are never alpha-blended, because floating-point render targets don't support blending. Whether the lambert dot product runs in world-space or model-space depends on `MAP_VIEW` and `USING_NORMAL_MAP` together, not on either alone — reading only one of the two defines gives the wrong lighting path.

## Used by

*Nothing in the tree references this unit.*

## Related

**Compiled by**

| Unit | Component |
|---|---|
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](../../opengl/GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-resources/opengl/multi_resolution_static_polygon_reconstructed_raster/render_tile_to_scene_fragment_shader.glsl
python scripts/gpq.py grep uniform --category shader --path src/qt-resources/opengl/multi_resolution_static_polygon_reconstructed_raster
```

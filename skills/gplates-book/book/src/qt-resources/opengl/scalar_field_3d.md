# scalar_field_3d

[Book TOC](../../../TOC.md) · [shaders](../../../components/shaders.md) · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-resources/opengl/scalar_field_3d/cross_section_fragment_shader.glsl` | GLSL | 283 |
| `src/qt-resources/opengl/scalar_field_3d/cross_section_vertex_shader.glsl` | GLSL | 131 |
| `src/qt-resources/opengl/scalar_field_3d/iso_surface_fragment_shader.glsl` | GLSL | 2005 |
| `src/qt-resources/opengl/scalar_field_3d/iso_surface_vertex_shader.glsl` | GLSL | 38 |
| `src/qt-resources/opengl/scalar_field_3d/sphere_fragment_shader.glsl` | GLSL | 70 |
| `src/qt-resources/opengl/scalar_field_3d/sphere_vertex_shader.glsl` | GLSL | 55 |
| `src/qt-resources/opengl/scalar_field_3d/surface_fill_mask_fragment_shader.glsl` | GLSL | 33 |
| `src/qt-resources/opengl/scalar_field_3d/surface_fill_mask_geometry_shader.glsl` | GLSL | 57 |
| `src/qt-resources/opengl/scalar_field_3d/surface_fill_mask_vertex_shader.glsl` | GLSL | 39 |
| `src/qt-resources/opengl/scalar_field_3d/utils.glsl` | GLSL | 795 |
| `src/qt-resources/opengl/scalar_field_3d/volume_fill_spherical_cap_fragment_shader.glsl` | GLSL | 74 |
| `src/qt-resources/opengl/scalar_field_3d/volume_fill_spherical_cap_geometry_shader.glsl` | GLSL | 174 |
| `src/qt-resources/opengl/scalar_field_3d/volume_fill_vertex_shader.glsl` | GLSL | 48 |
| `src/qt-resources/opengl/scalar_field_3d/volume_fill_wall_fragment_shader.glsl` | GLSL | 109 |
| `src/qt-resources/opengl/scalar_field_3d/volume_fill_wall_geometry_shader.glsl` | GLSL | 109 |

## Overview

This is the shader library `GLScalarField3D` links into several distinct GPU programs to render a volumetric scalar field stored as depth layers of cube-mapped tiles. `utils.glsl` is not a standalone shader but a shared include: it holds the `Ray`/`Interval`/`Sphere` intersection primitives, the cube-face projection and tile-lookup functions (`project_world_position_onto_cube_face`, `get_tile_meta_data_from_position`, `sample_field_data_texture_array`) that every other shader in this directory uses to turn a world-space position into a sample of the field's cube-map tile texture arrays, and the surface-fill-mask sampling helpers used to clip rendering to a set of static polygons (e.g. a continent).

`iso_surface_fragment_shader.glsl` is the core of the technique: a full-screen ray-casting shader that, per pixel, walks a ray through the cube-mapped volume sampling `field_data_sampler` at `sampling_rate` intervals, classifies each sample against one or two isovalues (each with an optional deviation band) via `get_crossing_level`, and uses `isosurface_bisection_correction` to refine the crossing point once a sign change is detected. It supports several coloured "window" regions (surface entry windows, wall entry windows, deviation-window volume rendering) that are all composited along the same ray, and it can shortcut ray length using an externally rendered volume-fill-wall depth range or opaque wall hits so that regions outside a surface fill mask are skipped. The remaining pairs implement the auxiliary passes that feed or bound that ray-cast: `sphere_*` renders the globe's opaque core (or its screen-space depth) to occlude rays that shouldn't reach the fill; `surface_fill_mask_*` uses a geometry shader to rasterise a set of surface polygons into a 6-layer cube-map texture array in a single draw call, producing the mask sampled by both the wall and isosurface shaders; `volume_fill_wall_*` and `volume_fill_spherical_cap_*` extrude that same surface fill mask vertically between the field's depth radii — walls as geometry-shader-emitted quads along mask boundary edges, caps as tessellated spherical patches — to bound the volume that gets filled/rendered when a surface mask is in use; and `cross_section_*` renders a vertically extruded polyline/polygon as a flat, lit slice through the field, an alternative to ray-casting for inspecting the field along an explicit surface.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

*None.*

## Notes

`utils.glsl` is concatenated as a source string ahead of the shader it supports rather than compiled on its own — it declares no `main` and only makes sense linked into one of the other programs. Several files (`utils.glsl`, `surface_fill_mask_geometry_shader.glsl`, `volume_fill_wall_geometry_shader.glsl`, `volume_fill_spherical_cap_geometry_shader.glsl`, `iso_surface_fragment_shader.glsl`, `cross_section_fragment_shader.glsl`) require GPlates to hoist their `#extension` directives to the very start of the first source string passed to `glShaderSource`, since GLSL forbids extension pragmas after ordinary source code — a comment in each file warns against removing that line with a multi-line `/* */` comment, since the loader's extraction of it is line-based. As with the co-registration shaders, `#ifdef`-gated blocks (`DEPTH_RANGE`, `WHITE_WITH_LIGHTING`, `SURFACE_NORMALS_AND_DEPTH`, `POINT_REGION_OF_INTEREST`-style variants) mean each `.glsl` file backs multiple distinct linked programs selected by `GLScalarField3D` at compile time, not a single shader.

## Used by

*Nothing in the tree references this unit.*

## Related

**Compiled by**

| Unit | Component |
|---|---|
| [opengl/GLScalarField3D](../../opengl/GLScalarField3D.md) | opengl |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-resources/opengl/scalar_field_3d/cross_section_fragment_shader.glsl
python scripts/gpq.py grep uniform --category shader --path src/qt-resources/opengl/scalar_field_3d
```

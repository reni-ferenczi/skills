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

[[[PROSE overview unit=shaders/scalar_field_3d tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

*None.*

## Notes

[[[PROSE notes unit=shaders/scalar_field_3d tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

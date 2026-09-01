# raster_co_registration

[Book TOC](../../../TOC.md) · [shaders](../../../components/shaders.md) · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-resources/opengl/raster_co_registration/mask_region_of_interest_fragment_shader.glsl` | GLSL | 92 |
| `src/qt-resources/opengl/raster_co_registration/mask_region_of_interest_vertex_shader.glsl` | GLSL | 116 |
| `src/qt-resources/opengl/raster_co_registration/reduction_of_region_of_interest_fragment_shader.glsl` | GLSL | 109 |
| `src/qt-resources/opengl/raster_co_registration/reduction_of_region_of_interest_vertex_shader.glsl` | GLSL | 42 |
| `src/qt-resources/opengl/raster_co_registration/render_region_of_interest_geometries_fragment_shader.glsl` | GLSL | 138 |
| `src/qt-resources/opengl/raster_co_registration/render_region_of_interest_geometries_vertex_shader.glsl` | GLSL | 164 |

## Overview

[[[PROSE overview unit=shaders/raster_co_registration tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

*None.*

## Notes

[[[PROSE notes unit=shaders/raster_co_registration tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

**Compiled by**

| Unit | Component |
|---|---|
| [opengl/GLRasterCoRegistration](../../opengl/GLRasterCoRegistration.md) | opengl |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-resources/opengl/raster_co_registration/mask_region_of_interest_fragment_shader.glsl
python scripts/gpq.py grep uniform --category shader --path src/qt-resources/opengl/raster_co_registration
```

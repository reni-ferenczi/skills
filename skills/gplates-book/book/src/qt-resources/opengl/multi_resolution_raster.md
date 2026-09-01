# multi_resolution_raster

[Book TOC](../../../TOC.md) · [shaders](../../../components/shaders.md) · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-resources/opengl/multi_resolution_raster/render_raster_fragment_shader.glsl` | GLSL | 97 |
| `src/qt-resources/opengl/multi_resolution_raster/render_sphere_normals_fragment_shader.glsl` | GLSL | 44 |

## Overview

[[[PROSE overview unit=shaders/multi_resolution_raster tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

*None.*

## Notes

[[[PROSE notes unit=shaders/multi_resolution_raster tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

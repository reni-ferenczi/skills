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

This shader set implements the multi-pass GPU pipeline `GLRasterCoRegistration` uses to compute per-seed-geometry statistics (mean, standard deviation, minimum, maximum) of a raster over each seed's region of interest. The three shader pairs correspond to the three passes of that pipeline: `render_region_of_interest_geometries_*` rasterises a seed geometry (point, line or fill) into a mask, writing full coverage into every pixel that falls inside the region of interest defined around it — a point's or line's ROI is a small-circle or great-circle-arc band tested with `discard`, using a small-angle (`tan`/`sin`) or large-angle (`acos`) formulation chosen per `#define` to keep the trigonometry numerically stable across the whole angle range. `mask_region_of_interest_*` then extracts the target raster's data and coverage inside that mask, undoing the bilinear-filtering bias described in the fragment shader's comments so MIN/MAX and MEAN agree on single-pixel regions, and folds coverage into either `(C*D, C*D*D, C)` moments (for mean/standard deviation, selected by `FILTER_MOMENTS`) or `(D, C)` extrema (for min/max, `FILTER_MIN_MAX`). `reduction_of_region_of_interest_*` repeatedly downsamples that intermediate texture 2x2-to-1x1 (`REDUCTION_SUM`, `REDUCTION_MIN`, `REDUCTION_MAX`) until each seed's whole region of interest has been folded into a single texel, which `GLRasterCoRegistration` then reads back on the CPU.

All three vertex shaders carry the same two-stage clip-space remapping — raster-frustum-to-seed-frustum, then seed-frustum-to-render-target-frustum — expressed as `(translate_x, translate_y, scale)` triples rather than full matrices, since a post-projection scale/translate is all a cube-map-tile quadrant split needs. `ENABLE_SEED_FRUSTUM_CLIPPING` adds an extra fragment-side clip against the seed frustum's side planes for cases where the GPU's own NDC clipping is not tight enough.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

*None.*

## Notes

Each shader is compiled with a different combination of `#define`s (`FILTER_MOMENTS`/`FILTER_MIN_MAX`, `REDUCTION_SUM`/`REDUCTION_MIN`/`REDUCTION_MAX`, `POINT_REGION_OF_INTEREST`/`LINE_REGION_OF_INTEREST`/`FILL_REGION_OF_INTEREST`, `SMALL_ROI_ANGLE`/`LARGE_ROI_ANGLE`, `ENABLE_SEED_FRUSTUM_CLIPPING`) selected by `GLRasterCoRegistration` at link time, so a given `.glsl` file describes several distinct compiled programs rather than one. The min/max reduction and mask shaders discard fragments with zero coverage rather than writing zero data, relying on the framebuffer having been cleared to zero beforehand so uncovered pixels stay correctly at zero coverage.

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

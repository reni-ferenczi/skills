# Base2Utils

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1550 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/Base2Utils.h` | C++ | 118 |
| `src/utils/Base2Utils.cc` | C++ | 116 |

## Overview

`GPlatesUtils::Base2` is a small collection of bit-twiddling helpers for
power-of-two arithmetic on 32-bit unsigned integers, adapted from Sean Eron
Anderson's public bit-hacks reference. `next_power_of_two()` uses the classic
fill-the-bits-then-increment trick; `previous_power_of_two()` and the
`log2_*` variants are built on top of it, using a five-entry bitmask/bitshift
table to binary-search the position of the highest set bit rather than
looping bit by bit.

Its main consumers are the `opengl` texture and raster-tiling code (mipmap
level counts, cube-map and multi-resolution raster tile sizes) and raster
readers in `file-io`, all of which need to round dimensions up or down to
power-of-two texture sizes.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `LOG2_BITMASK` | variable | `unsigned int` | — |
| `LOG2_BITSHIFT` | variable | `unsigned int` | — |
| `GPLATES_UTILS_BASE2UTILS_H` | macro | `None` | — |
| `is_power_of_two( unsigned int value)` | function | `bool` | Determines if the specified integer is a power-of-two. |
| `previous_power_of_two( boost::uint32_t value)` | function | `unsigned int` | Determines the previous lower power-of-two of the specified integer. |
| `next_power_of_two( boost::uint32_t value)` | function | `unsigned int` | Determines the next higher power-of-two of the specified integer. |
| `log2_previous_power_of_two( boost::uint32_t value)` | function | `unsigned int` | Determines the previous lower power-of-two of the specified integer and returns the log base 2 of that result. |
| `log2_next_power_of_two( boost::uint32_t value)` | function | `unsigned int` | Determines the next higher power-of-two of the specified integer and returns the log base 2 of that result. |
| `log2_power_of_two( boost::uint32_t value)` | function | `unsigned int` | Determines the log base 2 of value (where value \*must\* be a power-of-two). |

## Notes

- None of these functions work for a `value` of `0`; callers must exclude zero
  before calling.
- `log2_power_of_two()` asserts (`PreconditionViolationError`) that `value` is
  already a power of two — passing a non-power-of-two aborts rather than
  returning a nonsense result.
- `previous_power_of_two()` and `next_power_of_two()` return `value` unchanged
  when it is already a power of two.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/GenerateVelocityDomainTerra](../app-logic/GenerateVelocityDomainTerra.md) | app-logic | 16 |
| [opengl/GLFilledPolygonsGlobeView](../opengl/GLFilledPolygonsGlobeView.md) | opengl | 13 |
| [qt-widgets/GenerateVelocityDomainTerraDialog](../qt-widgets/GenerateVelocityDomainTerraDialog.md) | qt-widgets | 13 |
| [opengl/GLSaveRestoreFrameBuffer](../opengl/GLSaveRestoreFrameBuffer.md) | opengl | 11 |
| [file-io/GdalRasterReader](../file-io/GdalRasterReader.md) | file-io | 9 |
| [file-io/RgbaRasterReader](../file-io/RgbaRasterReader.md) | file-io | 9 |
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 9 |
| [opengl/GLRenderer](../opengl/GLRenderer.md) | opengl | 9 |
| [opengl/GLRenderTarget](../opengl/GLRenderTarget.md) | opengl | 7 |
| [file-io/MipmappedRasterFormatWriter](../file-io/MipmappedRasterFormatWriter.md) | file-io | 5 |
| [opengl/GLImageUtils](../opengl/GLImageUtils.md) | opengl | 5 |
| [opengl/GLMultiResolutionCubeRaster](../opengl/GLMultiResolutionCubeRaster.md) | opengl | 5 |
| [opengl/GLCubeMeshGenerator](../opengl/GLCubeMeshGenerator.md) | opengl | 4 |
| [opengl/GLAgeGridMaskSource](../opengl/GLAgeGridMaskSource.md) | opengl | 3 |
| [opengl/GLDataRasterSource](../opengl/GLDataRasterSource.md) | opengl | 3 |
| [opengl/GLMultiResolutionMapCubeMesh](../opengl/GLMultiResolutionMapCubeMesh.md) | opengl | 3 |
| [opengl/GLNormalMapSource](../opengl/GLNormalMapSource.md) | opengl | 3 |
| [opengl/GLScalarFieldDepthLayersSource](../opengl/GLScalarFieldDepthLayersSource.md) | opengl | 3 |
| [opengl/GLVisualRasterSource](../opengl/GLVisualRasterSource.md) | opengl | 3 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](../opengl/GLMultiResolutionCubeReconstructedRaster.md) | opengl | 1 |

*... and 2 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/Base2Utils.h
```

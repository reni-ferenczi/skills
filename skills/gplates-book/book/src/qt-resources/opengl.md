# opengl

[Book TOC](../../TOC.md) · [shaders](../../components/shaders.md) · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-resources/opengl/utils.glsl` | GLSL | 314 |

## Overview

`utils.glsl` is a shared function library, not a standalone shader: `GLShaderProgramUtils::UTILS_SHADER_SOURCE_FILE_NAME` names it, and callers such as `GLMultiResolutionRaster`, `GLMultiResolutionStaticPolygonReconstructedRaster`, `GLMultiResolutionRasterMapView`, `GLFilledPolygonsGlobeView`, `GLScalarField3D` and `GLRasterCoRegistration` append it as an extra code segment onto their own vertex/fragment sources before compiling, giving every one of those shaders access to the same helper functions without duplicating them.

It provides: bilinear interpolation of a 2D texture done manually in the shader (`bilinearly_interpolate`, and a variant that also unpacks a red-channel value against a green-channel coverage weight), needed because earlier hardware has no native bilinear filtering for floating-point textures; `rotate_vector_by_quaternion`, used to apply a per-vertex plate rotation without shipping a full 3x3 matrix as vertex attribute data (trading a cheaper attribute for a more expensive per-vertex rotation, which several of the raster shaders rely on); the Lambert diffuse term and an ambient/diffuse blend shared by every lit shader in this component; and RGB/HSV colour-space conversions.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

*None.*

## Notes

`lambert_diffuse_lighting` and `mix_ambient_with_diffuse_lighting` deliberately use `float` rather than `int` parameters to `max`/`mix`/`clamp`-style calls, because some driver GLSL compilers cannot resolve the integer overload and crash; callers of these functions elsewhere in the component follow the same convention. `lambert_diffuse_lighting` also takes an unnormalised light direction and normal and normalises the dot product algebraically (dividing by `inversesqrt` of both squared lengths) to avoid two separate `normalize` calls — callers must not pre-normalise and expect a cheaper call, the function already assumes unnormalised input.

## Used by

*Nothing in the tree references this unit.*

## Related

**Compiled by**

| Unit | Component |
|---|---|
| [opengl/GLShaderProgramUtils](../opengl/GLShaderProgramUtils.md) | opengl |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-resources/opengl/utils.glsl
python scripts/gpq.py grep uniform --category shader --path src/qt-resources/opengl
```

# cstdint

[Book TOC](../../../TOC.md) · [system-fixes](../../../components/system-fixes.md) · cluster Community 3 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/system-fixes/boost/cstdint.hpp` | C++ | 44 |

## Overview

A compatibility wrapper around Boost's `cstdint` header that fixes compile errors with Visual Studio 2010. The Visual Studio 2010 compiler has conflicting definitions of the `UINT8_C` macro between Boost's cstdint and the standard library, which this header resolves by undefining and reincluding the macro before and after the Boost header.

This wrapper is included by precompiled headers in rendering and file I/O modules to ensure consistent fixed-width integer type availability across the application.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SYSTEMFIXES_BOOST_CSTDINT_HPP` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLAgeGridMaskSource](../../opengl/GLAgeGridMaskSource.md) | opengl | 2 |
| [opengl/GLMultiResolutionRaster](../../opengl/GLMultiResolutionRaster.md) | opengl | 2 |
| [entry-points/gplates-lib_pch](../../entry-points/gplates-lib_pch.md) | entry-points | 1 |
| [entry-points/pygplates_pch](../../entry-points/pygplates_pch.md) | entry-points | 1 |
| [file-io/GdalRasterReader](../../file-io/GdalRasterReader.md) | file-io | 1 |
| [file-io/GdalRasterWriter](../../file-io/GdalRasterWriter.md) | file-io | 1 |
| [file-io/RasterFileCacheFormat](../../file-io/RasterFileCacheFormat.md) | file-io | 1 |
| [file-io/RgbaRasterWriter](../../file-io/RgbaRasterWriter.md) | file-io | 1 |
| [file-io/ScalarField3DFileFormat](../../file-io/ScalarField3DFileFormat.md) | file-io | 1 |
| [gui/Colour](../../gui/Colour.md) | gui | 1 |
| [gui/ColourPaletteVisitor](../../gui/ColourPaletteVisitor.md) | gui | 1 |
| [gui/ExportAnimationType](../../gui/ExportAnimationType.md) | gui | 1 |
| [gui/RasterColourPalette](../../gui/RasterColourPalette.md) | gui | 1 |
| [maths/GreatCircleArc](../../maths/GreatCircleArc.md) | maths | 1 |
| [model/PropertyValue](../../model/PropertyValue.md) | model | 1 |
| [opengl/GLFrustum](../../opengl/GLFrustum.md) | opengl | 1 |
| [opengl/GLImageUtils](../../opengl/GLImageUtils.md) | opengl | 1 |
| [opengl/GLIntersect](../../opengl/GLIntersect.md) | opengl | 1 |
| [opengl/GLRasterCoRegistration](../../opengl/GLRasterCoRegistration.md) | opengl | 1 |
| [opengl/GLState](../../opengl/GLState.md) | opengl | 1 |

*... and 12 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/system-fixes/boost/cstdint.hpp
```

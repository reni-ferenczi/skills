# shaders

[Book TOC](../TOC.md)

GLSL shader programs compiled into the Qt resource bundle.

10 unit page(s), 38 source file(s) documented here, 0 further file(s) listed below.

## Overview

`src/qt-resources/opengl` is the GLSL half of GPlates' rendering backend: source text compiled into `QGLShaderProgram` objects at run time by the `opengl` component's `GL*` classes, rather than C++ compiled once at build time. Its ten directories divide the rendering work by consumer, one directory per `GL*` class or closely related pair of classes, and within a directory the same source file is typically recompiled many times under different preprocessor defines to select a variant rather than being duplicated into separate files. Nothing here decides what geometry or raster data exists — that is settled upstream in `app-logic` and `opengl`'s own multi-resolution machinery — this component only supplies the per-vertex and per-fragment arithmetic that turns tiles, meshes and volumes into pixels.

`opengl` (the `utils.glsl` unit) is the one directory every other shader leans on: it is appended as an extra source segment onto vertex and fragment shaders throughout the component, supplying the manual bilinear filtering needed on hardware without native floating-point texture filtering, quaternion rotation for applying plate rotations without a matrix attribute, the shared Lambert/ambient lighting term, and colour-space conversions. `layer_painter` and `light` cover the two lighting fundamentals — directional lighting for ordinary batched geometry and axially-symmetric meshes, and precomputing a light direction per map position into a cube texture other shaders sample instead of recomputing it. The raster-tiling family — `multi_resolution_raster`, `multi_resolution_raster_map_view` and `multi_resolution_static_polygon_reconstructed_raster` — compiles cube-map tiles from source data and composites them onto the globe or map, with the last of the three the most heavily parameterised unit in the component because it must additionally handle plate-rotated geometry, age-grid masking and normal-map lighting in every combination the C++ caller can select. `normal_map_source` derives normal maps from height fields for that same lighting path, `multi_resolution_filled_polygons` composites rasterised dynamic-polygon tiles, `raster_co_registration` runs a three-pass reduction pipeline computing per-seed raster statistics, and `scalar_field_3d` is the largest and most self-contained unit, a shared library plus several ray-casting and mask-generation programs for volumetric fields.

This component has no measured cross-references to any other, because shader source is loaded by resource path and string concatenation rather than `#include`, so the dependency graph the rest of the book is built from cannot see it. In practice every unit here exists to be compiled by one or more classes in `opengl`: `GLShaderProgramUtils` locates and assembles the sources, and classes such as `GLMultiResolutionRaster`, `GLMultiResolutionStaticPolygonReconstructedRaster`, `GLFilledPolygonsGlobeView`, `GLRasterCoRegistration`, `GLScalarField3D`, `GLLight` and `LayerPainter` each own one directory's worth of programs, choosing preprocessor defines at draw time to match the raster, view and lighting mode in play. What flows across that edge is entirely one-directional and textual: uniform and attribute names, and the `#define` symbols that select a compiled variant, are the only contract between the two components, agreed by convention rather than by any shared header.

## Units

### `src/qt-resources/opengl`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [opengl](../src/qt-resources/opengl.md) | 2 | 314 | 0 | Shared GLSL helper library (bilinear filtering, quaternion rotation, lighting, HSV) linked into other shaders by GLShaderProgramUtils |

### `src/qt-resources/opengl/layer_painter`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [layer_painter](../src/qt-resources/opengl/layer_painter.md) | 2 | 243 | 0 | Directional lighting shaders for LayerPainter's point/line/polygon and axially-symmetric-mesh geometry |

### `src/qt-resources/opengl/light`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [light](../src/qt-resources/opengl/light.md) | 2 | 79 | 0 | Renders a light direction into a cube texture for GLLight's map-view lighting |

### `src/qt-resources/opengl/multi_resolution_filled_polygons`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [multi_resolution_filled_polygons](../src/qt-resources/opengl/multi_resolution_filled_polygons.md) | 2 | 132 | 0 | Composites filled-polygon tile textures onto the scene for GLFilledPolygonsGlobeView |

### `src/qt-resources/opengl/multi_resolution_raster`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [multi_resolution_raster](../src/qt-resources/opengl/multi_resolution_raster.md) | 2 | 141 | 0 | Builds GLMultiResolutionRaster's cube-map tiles: data filtering, normal-map, or gradient conversion |

### `src/qt-resources/opengl/multi_resolution_raster_map_view`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [multi_resolution_raster_map_view](../src/qt-resources/opengl/multi_resolution_raster_map_view.md) | 2 | 105 | 0 | Draws GLMultiResolutionRasterMapView's raster tiles onto the flat map projection |

### `src/qt-resources/opengl/multi_resolution_static_polygon_reconstructed_raster`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [multi_resolution_static_polygon_reconstructed_raster](../src/qt-resources/opengl/multi_resolution_static_polygon_reconstructed_raster.md) | 2 | 340 | 0 | Composites reconstructed raster tiles for GLMultiResolutionStaticPolygonReconstructedRaster with age-grid masking and normal-map lighting |

### `src/qt-resources/opengl/normal_map_source`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [normal_map_source](../src/qt-resources/opengl/normal_map_source.md) | 2 | 153 | 0 | Derives a normal map from a height field for GLNormalMapSource |

### `src/qt-resources/opengl/raster_co_registration`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [raster_co_registration](../src/qt-resources/opengl/raster_co_registration.md) | 2 | 661 | 0 | GPU pipeline for masking, extracting and reducing raster values over seed regions of interest for co-registration |

### `src/qt-resources/opengl/scalar_field_3d`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [scalar_field_3d](../src/qt-resources/opengl/scalar_field_3d.md) | 2 | 4020 | 0 | Shader library for ray-cast isosurface, cross-section and volume-fill rendering of a cube-mapped 3D scalar field |


## Other files

*None.*

## Depends on

*None.*

## Used by

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/qt-resources/opengl/layer_painter
python scripts/gpq.py sym . --mode sub --path src/qt-resources/opengl/layer_painter --defs-only
```

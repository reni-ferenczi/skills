# shaders

[Book TOC](../TOC.md)

GLSL shader programs compiled into the Qt resource bundle.

10 unit page(s), 38 source file(s) documented here, 0 further file(s) listed below.

## Overview

[[[PROSE component unit=component:shaders tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

### `src/qt-resources/opengl`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [opengl](../src/qt-resources/opengl.md) | 2 | 314 | 0 | (pending) |

### `src/qt-resources/opengl/layer_painter`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [layer_painter](../src/qt-resources/opengl/layer_painter.md) | 2 | 243 | 0 | (pending) |

### `src/qt-resources/opengl/light`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [light](../src/qt-resources/opengl/light.md) | 2 | 79 | 0 | (pending) |

### `src/qt-resources/opengl/multi_resolution_filled_polygons`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [multi_resolution_filled_polygons](../src/qt-resources/opengl/multi_resolution_filled_polygons.md) | 2 | 132 | 0 | (pending) |

### `src/qt-resources/opengl/multi_resolution_raster`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [multi_resolution_raster](../src/qt-resources/opengl/multi_resolution_raster.md) | 2 | 141 | 0 | (pending) |

### `src/qt-resources/opengl/multi_resolution_raster_map_view`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [multi_resolution_raster_map_view](../src/qt-resources/opengl/multi_resolution_raster_map_view.md) | 2 | 105 | 0 | (pending) |

### `src/qt-resources/opengl/multi_resolution_static_polygon_reconstructed_raster`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [multi_resolution_static_polygon_reconstructed_raster](../src/qt-resources/opengl/multi_resolution_static_polygon_reconstructed_raster.md) | 2 | 340 | 0 | (pending) |

### `src/qt-resources/opengl/normal_map_source`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [normal_map_source](../src/qt-resources/opengl/normal_map_source.md) | 2 | 153 | 0 | (pending) |

### `src/qt-resources/opengl/raster_co_registration`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [raster_co_registration](../src/qt-resources/opengl/raster_co_registration.md) | 2 | 661 | 0 | (pending) |

### `src/qt-resources/opengl/scalar_field_3d`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [scalar_field_3d](../src/qt-resources/opengl/scalar_field_3d.md) | 2 | 4020 | 0 | (pending) |


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

# GLTileRender

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 678 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLTileRender.h` | C++ | 242 |
| `src/opengl/GLTileRender.cc` | C++ | 245 |

## Overview

`GLTileRender` drives the tiled-rendering pattern used whenever a destination
image (an export raster, a high-resolution screenshot) is larger than a
single render target can hold. Rather than rendering the scene once, the
caller iterates tiles with `first_tile`/`next_tile`/`finished`, and for each
one re-renders the *entire* scene using a narrowed `get_tile_projection_transform`
that restricts the view frustum to just that tile's portion of the
destination, then copies the render target's `get_tile_source_viewport`
region to the destination's `get_tile_destination_viewport` region.

The constructor divides `destination_viewport` into a grid of tiles no larger
than `render_target_width` x `render_target_height`, with `d_num_tile_columns`
and `d_num_tile_rows` computed to cover the destination completely (the last
row/column may be smaller). The optional `border` widens the render target
and view frustum by that many pixels on each side of every tile without
widening the tile's final source/destination region, which is why a caller
must additionally set the scissor rectangle (`get_tile_render_target_scissor_rectangle`)
to clip the border away — the viewport and projection transform do not do
that clipping themselves. The border exists because "fat" points and wide
lines are only rasterized within the frustum they're clipped against, so
without a border, geometry that straddles a tile boundary or has a nonzero
point size/line width can pop in and out of tiles.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLTileRender`](#gplatesopenglgltilerender) | class | — | — | 0 | Used when compositing a destination (image) from a sequence of smaller rendered tiles. |

## Members

### `GPlatesOpenGL::GLTileRender`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLTileRender( unsigned int render_target_width, unsigned int render_target_height, const GLViewport &destination_viewport, unsigned int border = 0)` | constructor | `None` | public | render\_target\_width and render\_target\_height are the dimensions of the render target used to render each tile. destination\_viewport is the destination of the final tile-composited image. border is the number of pixels around the actual ... |
| `get_max_tile_render_target_width()` | method | `unsigned int` | public | Returns the maximum render target tile width across all tiles. |
| `get_max_tile_render_target_height()` | method | `unsigned int` | public | Returns the maximum render target tile height across all tiles. |
| `first_tile()` | method | `void` | public | Starts at the first tile. |
| `next_tile()` | method | `void` | public | Moves to the next tile. |
| `finished()` | method | `bool` | public | Returns true if finished iterating over the tiles. |
| `get_tile_projection_transform()` | method | `GLTransform::non_null_ptr_to_const_type` | public | The projection transform adjustment for the current tile. |
| `get_tile_render_target_viewport( GLViewport &tile_render_target_viewport)` | method | `void` | public | The viewport that should be specified to 'GLRenderer::gl\_viewport()' before rendering to the current tile (this viewport includes the tile's border pixels). |
| `get_tile_render_target_scissor_rectangle( GLViewport &tile_render_target_scissor_rect)` | method | `void` | public | The scissor rectangle that should be specified to 'GLRenderer::gl\_scissor()' before rendering to the current tile (this rectangle excludes the tile's border pixels). |
| `get_tile_source_viewport( GLViewport &tile_source_viewport)` | method | `void` | public | The viewport containing the actual rendered tile data (excludes the border pixels). |
| `get_tile_destination_viewport( GLViewport &tile_destination_viewport)` | method | `void` | public | The viewport in the larger destination viewport where the current tile's source data should be copied or transferred to. |
| `Tile` | struct | `None` | private | Holds information for the current tile. |
| `d_destination_viewport` | field | `GLViewport` | private | — |
| `d_border` | field | `unsigned int` | private | — |
| `d_max_tile_width` | field | `unsigned int` | private | — |
| `d_max_tile_height` | field | `unsigned int` | private | — |
| `d_num_tile_columns` | field | `unsigned int` | private | — |
| `d_num_tile_rows` | field | `unsigned int` | private | — |
| `d_current_tile_index` | field | `unsigned int` | private | Index to the current tile. |
| `d_current_tile` | field | `boost::optional<Tile>` | private | The current tile's parameters, or boost::none if no current tile. |
| `initialise_current_tile()` | method | `void` | private | Create d\_current\_tile associated with the current tile index d\_current\_tile\_index. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLTILERENDER_H` | macro | `None` | — |

## Notes

- The constructor's only precondition is that both render target dimensions are
  non-zero; it throws `PreconditionViolationError` otherwise. Ignore the header
  comment above the constructor (`GLTileRender.h`), which is stale: it claims a
  `PreconditionViolationError` when a render target dimension is `<= 2 * border`
  and that the tile dimensions are `render_target_width - 2 * border` and
  `render_target_height - 2 * border`. Neither is true of the 2.5.0 code —
  `d_max_tile_width`/`d_max_tile_height` are just the smaller of the render
  target and destination viewport dimensions, with no border subtracted, so the
  border is added *on top* of the tile size and it is the caller's job to make
  the render target big enough for `tile size + 2 * border`.
- After construction, `d_current_tile` is unset; callers must call
  `first_tile()` before using any of the per-tile accessors, and must check
  `finished()` after `next_tile()` before reading a (no longer valid) tile.
- The render-target viewport can have negative offsets and extend outside the
  render target's bounds — it is only the NDC-to-window-coordinate mapping,
  not a clip; the projection transform and scissor rectangle do the actual
  clipping, and skipping the scissor call when a border is in use will let
  fat points/wide lines bleed into neighbouring tiles.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 15 |
| [gui/FeedbackOpenGLToQPainter](../gui/FeedbackOpenGLToQPainter.md) | gui | 12 |
| [opengl/GLSaveRestoreFrameBuffer](GLSaveRestoreFrameBuffer.md) | opengl | 12 |
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 11 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 10 |
| [opengl/GLRendererImpl](GLRendererImpl.md) | opengl | 5 |
| [opengl/GLVisualRasterSource](GLVisualRasterSource.md) | opengl | 3 |
| [opengl/GLRenderer](GLRenderer.md) | opengl | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLTileRender.h
python scripts/gpq.py def GPlatesOpenGL::GLTileRender --body
python scripts/gpq.py uses GLTileRender --kind class
python scripts/gpq.py hier GLTileRender
```

# ExportSvgAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 433 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportSvgAnimationStrategy.h` | C++ | 136 |
| `src/gui/ExportSvgAnimationStrategy.cc` | C++ | 134 |

## Overview

`ExportSvgAnimationStrategy` writes a vector snapshot of the currently reconstructed geometry to an SVG file at each animation frame, using Qt's `QSvgGenerator`. Its `Configuration` only needs `ExportOptionsUtils::ExportImageResolutionOptions`, since an SVG has no raster pixels to configure beyond size and aspect ratio.

`do_export_iteration` temporarily disables every `GPlatesViewOperations::RenderedGeometryCollection` main layer except `RECONSTRUCTION_LAYER`, so the SVG captures only reconstructed geometry and not other overlays (mesh, digitisation guides, etc.), then calls `GPlatesQtWidgets::SceneView::render_opengl_feedback_to_paint_device` to feed the OpenGL scene through Qt's paint-engine feedback path into the SVG generator, before restoring the previous layer visibility.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ExportSvgAnimationStrategy`](#gplatesguiexportsvganimationstrategy) | class | [`GPlatesGui::ExportAnimationStrategy`](ExportAnimationStrategy.md) | — | 0 | Concrete implementation of the ExportAnimationStrategy class for writing SVG snapshots of the globe. |

## Members

### `GPlatesGui::ExportSvgAnimationStrategy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportSvgAnimationStrategy>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportSvgAnimationStrategy\>. |
| `Configuration` | class | `None` | public | Configuration options.. |
| `const_configuration_ptr` | typedef | `boost::shared_ptr<const Configuration>` | public | Typedef for a shared pointer to const Configuration. |
| `create( ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | method | `non_null_ptr_type` | public | — |
| `~ExportSvgAnimationStrategy()` | destructor | `None` | public | — |
| `do_export_iteration( std::size_t frame_index)` | method | `bool` | public | Does one frame of export. |
| `ExportSvgAnimationStrategy( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &cfg)` | constructor | `None` | protected | Protected constructor to prevent instantiation on the stack. |
| `d_configuration` | field | `const_configuration_ptr` | private | Export configuration parameters. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_EXPORTSVGANIMATIONSTRATEGY_H` | macro | `None` | — |

## Notes

If `image_resolution_options.image_size` is unset, the SVG is sized to the active scene view's current viewport rather than any fixed default. The rendered-layer active state is saved and restored around the export so the change is invisible to the rest of the UI, but an exception thrown mid-export would leave non-reconstruction layers hidden.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportSvgOptionsWidget](../qt-widgets/ExportSvgOptionsWidget.md) | qt-widgets | 17 |
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 5 |
| [gui/ExportAnimationContext](ExportAnimationContext.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportSvgAnimationStrategy.h
python scripts/gpq.py def GPlatesGui::ExportSvgAnimationStrategy --body
python scripts/gpq.py uses ExportSvgAnimationStrategy --kind class
python scripts/gpq.py hier ExportSvgAnimationStrategy
```

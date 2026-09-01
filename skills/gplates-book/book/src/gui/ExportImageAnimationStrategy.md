# ExportImageAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 251 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportImageAnimationStrategy.h` | C++ | 167 |
| `src/gui/ExportImageAnimationStrategy.cc` | C++ | 151 |

## Overview

`ExportImageAnimationStrategy` is the `ExportAnimationStrategy` (Gamma et al. Strategy role, driven by `ExportAnimationContext`) that saves a screenshot of the active globe or map view to an image file at each animation frame, in one of the Qt image formats listed in `Configuration::ImageType` (BMP, JPG, PNG, TIFF, and others). It also inherits `QObject`, needed only so it can use `QObject::tr()` for status messages, not for signals or slots.

Each `do_export_iteration()` call renders the active `SceneView` to a `QImage` — at the configured resolution if `image_resolution_options.image_size` is set, otherwise at the current viewport size — after temporarily disabling every `RenderedGeometryCollection` main layer except `RECONSTRUCTION_LAYER` so the exported frame shows only the reconstructed geometry, and clearing to transparent black so PNG exports get a transparent background. Layer visibility is restored via `restore_main_layer_active_state()` before returning, even though the restore is skipped if `image_writer.write()` throws.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ExportImageAnimationStrategy`](#gplatesguiexportimageanimationstrategy) | class | `QObject`<br>[`GPlatesGui::ExportAnimationStrategy`](ExportAnimationStrategy.md) | — | 0 | Concrete implementation of the ExportAnimationStrategy class for saving the image (of the globe or map view) to a coloured image file at each timestep. |

## Members

### `GPlatesGui::ExportImageAnimationStrategy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportImageAnimationStrategy>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportImageAnimationStrategy\>. |
| `Configuration` | class | `None` | public | Configuration options. |
| `const_configuration_ptr` | typedef | `boost::shared_ptr<const Configuration>` | public | Typedef for a shared pointer to const Configuration. |
| `create( ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | method | `non_null_ptr_type` | public | — |
| `~ExportImageAnimationStrategy()` | destructor | `None` | public | — |
| `do_export_iteration( std::size_t frame_index)` | method | `bool` | public | Does one frame of export. |
| `ExportImageAnimationStrategy( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | constructor | `None` | protected | Protected constructor to prevent instantiation on the stack. |
| `d_configuration` | field | `const_configuration_ptr` | private | Export configuration parameters. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_EXPORTIMAGEANIMATIONSTRATEGY_H` | macro | `None` | — |

## Notes

A rendered image can come back at a larger pixel size than requested when the display has a device pixel ratio above 1.0; it still occupies the requested widget dimensions. An empty (`isNull()`) result is treated as a memory allocation failure and reported as an export failure rather than raising an exception.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 18 |
| [qt-widgets/ExportImageOptionsWidget](../qt-widgets/ExportImageOptionsWidget.md) | qt-widgets | 17 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportImageAnimationStrategy.h
python scripts/gpq.py def GPlatesGui::ExportImageAnimationStrategy --body
python scripts/gpq.py uses ExportImageAnimationStrategy --kind class
python scripts/gpq.py hier ExportImageAnimationStrategy
```

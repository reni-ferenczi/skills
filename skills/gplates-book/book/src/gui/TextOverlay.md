# TextOverlay

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1697 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/TextOverlay.h` | C++ | 72 |
| `src/gui/TextOverlay.cc` | C++ | 132 |

## Overview

Renders text overlays on the globe and map views. Takes `TextOverlaySettings` specifying the text string, font, colour, position, and optional shadow. Before rendering, substitutes the string `%f` with the current reconstruction time formatted to the specified number of decimal places. Positions the text according to a four-point anchor system (top-left, top-right, bottom-left, bottom-right) with optional offsets, and renders it via `GLText` with optional drop shadow.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::TextOverlay`](#gplatesguitextoverlay) | class | — | — | 0 | TextOverlay is responsible for painting the text overlay onto the globe or map, in a manner specified by TextOverlaySettings. |

## Members

### `GPlatesGui::TextOverlay`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TextOverlay( const GPlatesAppLogic::ApplicationState &application_state)` | constructor | `None` | public | — |
| `paint( GPlatesOpenGL::GLRenderer &renderer, const TextOverlaySettings &settings, int paint_device_width, int paint_device_height, float scale)` | method | `void` | public | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_TEXTOVERLAY_H` | macro | `None` | — |

## Notes

Early return if the overlay is disabled in settings. The OpenGL y-axis is inverted relative to Qt, so y-coordinates are adjusted accordingly. Text width calculation uses Qt 5.11+ `horizontalAdvance()` on newer versions and the deprecated `width()` on older versions.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 3 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/TextOverlay.h
python scripts/gpq.py def GPlatesGui::TextOverlay --body
python scripts/gpq.py uses TextOverlay --kind class
python scripts/gpq.py hier TextOverlay
```

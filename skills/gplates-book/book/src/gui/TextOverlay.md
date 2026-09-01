# TextOverlay

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1697 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/TextOverlay.h` | C++ | 72 |
| `src/gui/TextOverlay.cc` | C++ | 132 |

## Overview

[[[PROSE overview unit=gui/TextOverlay tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=gui/TextOverlay tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

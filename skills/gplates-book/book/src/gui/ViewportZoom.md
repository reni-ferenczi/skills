# ViewportZoom

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 617 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ViewportZoom.h` | C++ | 137 |
| `src/gui/ViewportZoom.cc` | C++ | 153 |

## Overview

`ViewportZoom` is the single source of truth for how far the globe/map view
is zoomed, shared by both the OpenGL viewport (`GlobeCanvas`, `MapCanvas`) and
the zoom-related UI (`ZoomSliderWidget`, `ZoomControlWidget`) and canvas tools
(`ZoomGlobe`, `ZoomMap`). It exposes the zoom two ways: `zoom_percent()`/
`zoom_factor()` is the intuitive linear percentage (100% to 100,000%,
`s_min_zoom_percent`/`s_max_zoom_percent`) that the viewport actually scales
by, while `zoom_level()` is a logarithmic scale (0 to 60,
`s_min_zoom_level`/`s_max_zoom_level`) designed so that UI controls like a
slider or repeated key presses change the zoom at a constant perceived rate
rather than a constant percentage. `set_zoom_level()` converts back to a
percent via `pow(10, ...)` and `zoom_level()` via `log10`, so the two
representations always agree.

All setters funnel through `set_zoom_percent()`, which clamps to the valid
range and emits `zoom_changed()` (plus `send_zoom_to_stdout()`) only when the
value actually changes, so any number of independent widgets can drive or
observe the zoom through the same `QObject` without redundant updates or
feedback loops.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ViewportZoom`](#gplatesguiviewportzoom) | class | `QObject` | — | 0 | This class encapsulates the behaviour of the zooming-in and zooming-out of the Viewport. |

## Members

### `GPlatesGui::ViewportZoom`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `s_min_zoom_level` | field | `int` | public | — |
| `s_max_zoom_level` | field | `int` | public | — |
| `s_min_zoom_percent` | field | `double` | public | — |
| `s_max_zoom_percent` | field | `double` | public | — |
| `ViewportZoom()` | constructor | `None` | public | — |
| `zoom_percent()` | method | `double` | public | — |
| `zoom_factor()` | method | `double` | public | — |
| `zoom_level()` | method | `double` | public | The zoom level is related to the zoom percent in the following manner: zoom percent = pow(10.0, (level - min\_zoom\_level) / (max\_zoom\_level - min\_zoom\_level) \* (max\_zoom\_power - min\_zoom\_power) + min\_zoom\_power) where min\_zoom\_power and ... |
| `zoom_in( double num_levels = 1.0)` | method | `void` | public | — |
| `zoom_out( double num_levels = 1.0)` | method | `void` | public | — |
| `reset_zoom()` | method | `void` | public | — |
| `set_zoom_percent( double new_zoom_percent)` | method | `void` | public | — |
| `set_zoom_level( double new_zoom_level)` | method | `void` | public | — |
| `zoom_changed()` | method | `void` | public | This signal should only be emitted if the zoom is actually different to what it was. |
| `send_zoom_to_stdout( double zoom)` | method | `void` | public | — |
| `min_zoom_power()` | method | `double` | private | — |
| `max_zoom_power()` | method | `double` | private | — |
| `d_zoom_percent` | field | `double` | private | This is the intuitive "zoom percent". |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `s_min_zoom_level` | variable | `int` | — |
| `s_max_zoom_level` | variable | `int` | — |
| `s_min_zoom_percent` | variable | `double` | — |
| `s_max_zoom_percent` | variable | `double` | NOTE: When increasing the maximum zoom percent, be sure to change the maximum zoom level such that the original max zoom level and original max percent still match up. |
| `GPLATES_GUI_VIEWPORTZOOM_H` | macro | `None` | — |

## Notes

- `s_max_zoom_level` is tied to `s_max_zoom_percent` by the
  `zoom_level()`/`set_zoom_level()` formula; the header comment on
  `s_max_zoom_percent` warns that raising the maximum zoom percent requires
  recomputing and updating the matching maximum zoom level, or existing
  zoom-level-based controls (sliders, keyboard shortcuts) will change the
  zoom rate they used to.
- `set_zoom_percent()` compares the new value against the current one via
  `GPlatesMaths::Real` (an epsilon-aware comparison) before emitting
  `zoom_changed()`, so setting a value indistinguishable from the current
  zoom is a no-op that does not trigger listeners.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 14 |
| [gui/deprecated/GLCanvas](deprecated/GLCanvas.md) | gui | 13 |
| [qt-widgets/ZoomSliderWidget](../qt-widgets/ZoomSliderWidget.md) | qt-widgets | 8 |
| [qt-widgets/ZoomControlWidget](../qt-widgets/ZoomControlWidget.md) | qt-widgets | 7 |
| [qt-widgets/GlobeAndMapWidget](../qt-widgets/GlobeAndMapWidget.md) | qt-widgets | 5 |
| [gui/Map](Map.md) | gui | 4 |
| [gui/SimpleGlobeOrientation](SimpleGlobeOrientation.md) | gui | 4 |
| [qt-widgets/ReconstructionViewWidget](../qt-widgets/ReconstructionViewWidget.md) | qt-widgets | 4 |
| [view-operations/MovePoleOperation](../view-operations/MovePoleOperation.md) | view-operations | 4 |
| [canvas-tools/ZoomGlobe](../canvas-tools/ZoomGlobe.md) | canvas-tools | 3 |
| [canvas-tools/ZoomMap](../canvas-tools/ZoomMap.md) | canvas-tools | 3 |
| [gui/ExternalSyncController](ExternalSyncController.md) | gui | 3 |
| [view-operations/ChangeLightDirectionOperation](../view-operations/ChangeLightDirectionOperation.md) | view-operations | 3 |
| [gui/MapTransform](MapTransform.md) | gui | 2 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 2 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ViewportZoom.h
python scripts/gpq.py def GPlatesGui::ViewportZoom --body
python scripts/gpq.py uses ViewportZoom --kind class
python scripts/gpq.py hier ViewportZoom
```

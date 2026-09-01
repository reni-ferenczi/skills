# deprecated

[Book TOC](../TOC.md)

12 unit page(s), 20 source file(s) documented here, 17 further file(s) listed below.

## Overview

[[[PROSE component unit=component:deprecated tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

### `src/deprecated/controls`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AnimationTimer](../src/deprecated/controls/AnimationTimer.md) | 3 | 360 | 15 | (pending) |
| [Dialogs](../src/deprecated/controls/Dialogs.md) | 3 | 109 | 0 | (pending) |
| [File](../src/deprecated/controls/File.md) | 3 | 768 | 11 | (pending) |
| [GuiCalls](../src/deprecated/controls/GuiCalls.md) | 3 | 174 | 27 | (pending) |
| [Lifetime](../src/deprecated/controls/Lifetime.md) | 3 | 168 | 36 | (pending) |
| [Reconstruct](../src/deprecated/controls/Reconstruct.md) | 3 | 506 | 10 | (pending) |
| [View](../src/deprecated/controls/View.md) | 3 | 82 | 0 | (pending) |

### `src/deprecated/patterns`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [PublisherTemplate](../src/deprecated/patterns/PublisherTemplate.md) | 3 | 685 | 27 | (pending) |
| [PublisherTemplate_test](../src/deprecated/patterns/PublisherTemplate_test.md) | 3 | 360 | 0 | (pending) |

### `src/deprecated/presenter`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ExposedPresenterObject](../src/deprecated/presenter/ExposedPresenterObject.md) | 3 | 139 | 1 | (pending) |
| [Presenter](../src/deprecated/presenter/Presenter.md) | 3 | 43 | 0 | (pending) |
| [ReconstructionContext](../src/deprecated/presenter/ReconstructionContext.md) | 3 | 103 | 0 | (pending) |


## Other files

| File | Kind | Lines |
|---|---|---|
| `src/deprecated/pixmaps/drag_globe_35.xpm` | resource | 193 |
| `src/deprecated/pixmaps/drag_plate_35.xpm` | resource | 254 |
| `src/deprecated/pixmaps/help_24.xpm` | resource | 271 |
| `src/deprecated/pixmaps/measure_angle_35.xpm` | resource | 311 |
| `src/deprecated/pixmaps/mode_observation_24.xpm` | resource | 243 |
| `src/deprecated/pixmaps/mode_plate_manip_24.xpm` | resource | 217 |
| `src/deprecated/pixmaps/new_pin_35.xpm` | resource | 271 |
| `src/deprecated/pixmaps/query_data_35.xpm` | resource | 197 |
| `src/deprecated/pixmaps/select_pin_35.xpm` | resource | 246 |
| `src/deprecated/pixmaps/select_plate_35.xpm` | resource | 239 |
| `src/deprecated/pixmaps/spin_globe_35.xpm` | resource | 200 |
| `src/deprecated/pixmaps/spin_plate_35.xpm` | resource | 252 |
| `src/deprecated/pixmaps/stock_stop_24.xpm` | resource | 285 |
| `src/deprecated/pixmaps/stock_zoom_in_24.xpm` | resource | 159 |
| `src/deprecated/pixmaps/stock_zoom_out_24.xpm` | resource | 158 |
| `src/deprecated/pixmaps/viewxpm` | other | 0 |
| `src/deprecated/pixmaps/zoom_initial_24.xpm` | resource | 162 |

## Depends on

| Component | References |
|---|---|
| [global](global.md) | 33 |
| [maths](maths.md) | 22 |
| [gui](gui.md) | 18 |
| [file-io](file-io.md) | 15 |
| [unit-test](unit-test.md) | 7 |
| [model](model.md) | 1 |
| [qt-widgets](qt-widgets.md) | 1 |

## Used by

| Component | References |
|---|---|
| [gui](gui.md) | 64 |
| [maths](maths.md) | 2 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/deprecated/controls
python scripts/gpq.py sym . --mode sub --path src/deprecated/controls --defs-only
```

# RenderSettings

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 304 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/RenderSettings.h` | C++ | 163 |

## Overview

[[[PROSE overview unit=gui/RenderSettings tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::RenderSettings`](#gplatesguirendersettings) | class | `QObject` | — | 0 | — |

## Members

### `GPlatesGui::RenderSettings`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderSettings()` | constructor | `None` | public | — |
| `RenderSettings( bool show_static_points_, bool show_static_multipoints_, bool show_static_lines_, bool show_static_polygons_, bool show_topological_sections_, bool show_topological_lines_, bool show_topological_polygons_, bool show_topological_networks_, bool show_velocity_arrows_, bool show_rasters_, bool show_3d_scal ...` | constructor | `None` | public | — |
| `show_static_points()` | method | `bool` | public | — |
| `show_static_multipoints()` | method | `bool` | public | — |
| `show_static_lines()` | method | `bool` | public | — |
| `show_static_polygons()` | method | `bool` | public | — |
| `show_topological_sections()` | method | `bool` | public | — |
| `show_topological_lines()` | method | `bool` | public | — |
| `show_topological_polygons()` | method | `bool` | public | — |
| `show_topological_networks()` | method | `bool` | public | — |
| `show_velocity_arrows()` | method | `bool` | public | — |
| `show_rasters()` | method | `bool` | public | — |
| `show_3d_scalar_fields()` | method | `bool` | public | — |
| `show_scalar_coverages()` | method | `bool` | public | — |
| `show_strings()` | method | `bool` | public | — |
| `set_show_static_points(bool b)` | method | `void` | public | — |
| `set_show_static_multipoints(bool b)` | method | `void` | public | — |
| `set_show_static_lines(bool b)` | method | `void` | public | — |
| `set_show_static_polygons(bool b)` | method | `void` | public | — |
| `set_show_topological_sections(bool b)` | method | `void` | public | — |
| `set_show_topological_lines(bool b)` | method | `void` | public | — |
| `set_show_topological_polygons(bool b)` | method | `void` | public | — |
| `set_show_topological_networks(bool b)` | method | `void` | public | — |
| `set_show_velocity_arrows(bool b)` | method | `void` | public | — |
| `set_show_rasters(bool b)` | method | `void` | public | — |
| `set_show_3d_scalar_fields(bool b)` | method | `void` | public | — |
| `set_show_scalar_coverages(bool b)` | method | `void` | public | — |
| `set_show_strings(bool b)` | method | `void` | public | — |
| `set_show_all( bool b)` | method | `void` | public | — |
| `settings_changed()` | method | `void` | public | — |
| `d_show_static_points` | field | `bool` | private | — |
| `d_show_static_multipoints` | field | `bool` | private | — |
| `d_show_static_lines` | field | `bool` | private | — |
| `d_show_static_polygons` | field | `bool` | private | — |
| `d_show_topological_sections` | field | `bool` | private | — |
| `d_show_topological_lines` | field | `bool` | private | — |
| `d_show_topological_polygons` | field | `bool` | private | — |
| `d_show_topological_networks` | field | `bool` | private | — |
| `d_show_velocity_arrows` | field | `bool` | private | — |
| `d_show_rasters` | field | `bool` | private | — |
| `d_show_3d_scalar_fields` | field | `bool` | private | — |
| `d_show_scalar_coverages` | field | `bool` | private | — |
| `d_show_strings` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_RENDERSETTINGS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/RenderSettings tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 40 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 35 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 29 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 5 |
| [presentation/VisualLayers](../presentation/VisualLayers.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/RenderSettings.h
python scripts/gpq.py def GPlatesGui::RenderSettings --body
python scripts/gpq.py uses RenderSettings --kind class
python scripts/gpq.py hier RenderSettings
```

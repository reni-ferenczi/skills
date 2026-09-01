# ViewportProjection

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1326 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ViewportProjection.h` | C++ | 117 |

## Overview

[[[PROSE overview unit=gui/ViewportProjection tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ViewportProjection`](#gplatesguiviewportprojection) | class | `QObject` | — | 0 | A central place to set view projection and listens for changes. |

## Members

### `GPlatesGui::ViewportProjection`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ViewportProjection( GPlatesGui::MapProjection::Type projection_type)` | constructor | `None` | public | — |
| `set_projection_type( GPlatesGui::MapProjection::Type projection_type)` | method | `void` | public | Set projection type and notify any listeners. |
| `set_central_meridian( const double &central_meridian)` | method | `void` | public | Set central meridian and notify any listeners. |
| `get_projection_type()` | method | `GPlatesGui::MapProjection::Type` | public | — |
| `projection_type_about_to_change( const GPlatesGui::ViewportProjection &viewport_projection)` | method | `void` | public | — |
| `projection_type_changed( const GPlatesGui::ViewportProjection &viewport_projection)` | method | `void` | public | — |
| `central_meridian_changed( const GPlatesGui::ViewportProjection &viewport_projection)` | method | `void` | public | — |
| `central_meridian_about_to_change( const GPlatesGui::ViewportProjection &viewport_projection)` | method | `void` | public | — |
| `d_projection_type` | field | `GPlatesGui::MapProjection::Type` | private | — |
| `d_central_meridian` | field | `double` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_VIEWPORTPROJECTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/ViewportProjection tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 4 |
| [qt-widgets/GlobeAndMapWidget](../qt-widgets/GlobeAndMapWidget.md) | qt-widgets | 4 |
| [qt-widgets/ReconstructionViewWidget](../qt-widgets/ReconstructionViewWidget.md) | qt-widgets | 4 |
| [qt-widgets/ProjectionControlWidget](../qt-widgets/ProjectionControlWidget.md) | qt-widgets | 3 |
| [gui/Dialogs](Dialogs.md) | gui | 2 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ViewportProjection.h
python scripts/gpq.py def GPlatesGui::ViewportProjection --body
python scripts/gpq.py uses ViewportProjection --kind class
python scripts/gpq.py hier ViewportProjection
```

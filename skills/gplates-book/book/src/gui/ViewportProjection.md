# ViewportProjection

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1326 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ViewportProjection.h` | C++ | 117 |

## Overview

A central hub for map projection state: holds the current `MapProjection::Type` and the central meridian, and notifies listeners whenever either changes. When `set_projection_type()` or `set_central_meridian()` is called, it emits a before-change signal, updates the state, then emits an after-change signal, allowing both pre-validation and post-update reactions across the presentation and UI layers.

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

*None.*

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

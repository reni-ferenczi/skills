# GlobeVisibilityTester

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1638 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/GlobeVisibilityTester.h` | C++ | 73 |
| `src/gui/GlobeVisibilityTester.cc` | C++ | 40 |

## Overview

[[[PROSE overview unit=gui/GlobeVisibilityTester tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::GlobeVisibilityTester`](#gplatesguiglobevisibilitytester) | class | — | — | 0 | — |

## Members

### `GPlatesGui::GlobeVisibilityTester`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GlobeVisibilityTester( const GPlatesQtWidgets::GlobeCanvas &globe_canvas)` | constructor | `None` | public | Constructs an instance of GlobeVisibilityTester given the instance of globe\_canvas used in the main window. |
| `is_point_visible( const GPlatesMaths::PointOnSphere &point_on_sphere)` | method | `bool` | public | Returns true iff the point\_on\_sphere is on the near side of the sphere based on the globe's current camera position. |
| `d_globe_canvas_ptr` | field | `GPlatesQtWidgets::GlobeCanvas` | private | A pointer to the GlobeCanvas, through which we can get the camera position |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_GLOBEVISIBILITYTESTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/GlobeVisibilityTester tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](GlobeRenderedGeometryLayerPainter.md) | gui | 300 |
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 154 |
| [qt-widgets/ReconstructionViewWidget](../qt-widgets/ReconstructionViewWidget.md) | qt-widgets | 10 |
| [gui/Globe](Globe.md) | gui | 8 |
| [gui/GlobeRenderedGeometryCollectionPainter](GlobeRenderedGeometryCollectionPainter.md) | gui | 4 |
| [gui/deprecated/GLCanvas](deprecated/GLCanvas.md) | gui | 4 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 2 |
| [qt-widgets/LightingWidget](../qt-widgets/LightingWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/GlobeVisibilityTester.h
python scripts/gpq.py def GPlatesGui::GlobeVisibilityTester --body
python scripts/gpq.py uses GlobeVisibilityTester --kind class
python scripts/gpq.py hier GlobeVisibilityTester
```

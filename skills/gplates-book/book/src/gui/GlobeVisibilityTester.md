# GlobeVisibilityTester

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1638 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/GlobeVisibilityTester.h` | C++ | 73 |
| `src/gui/GlobeVisibilityTester.cc` | C++ | 40 |

## Overview

`GlobeVisibilityTester` answers a single question — is a given point on the
near or far side of the globe as currently oriented — by comparing it against
the camera position read from a `GlobeCanvas` (`camera_llp()`, converted to a
`PointOnSphere`) using `calculate_closeness()`; a non-negative closeness means
the point is on the visible hemisphere. It holds only a non-owning pointer to
the `GlobeCanvas`, so it is cheap to construct and pass around. It is used
heavily by `GlobeRenderedGeometryLayerPainter` and related painters to decide
which geometries to draw solid versus faded/gray on the globe's far side.

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

Holds a raw, non-owning pointer to its `GlobeCanvas`; the tester must not
outlive the canvas it was constructed from.

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

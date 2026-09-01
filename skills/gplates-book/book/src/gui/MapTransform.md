# MapTransform

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 615 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/MapTransform.h` | C++ | 177 |
| `src/gui/MapTransform.cc` | C++ | 128 |

## Overview

[[[PROSE overview unit=gui/MapTransform tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::MapTransform`](#gplatesguimaptransform) | class | `QObject` | — | 0 | This class encapsulates the current state of the map view in terms of the centre of the viewport and the angle of rotation. |

## Members

### `GPlatesGui::MapTransform`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `point_type` | typedef | `QPointF` | public | Typedef for a point in 2D space. |
| `MapTransform( ViewportZoom &viewport_zoom)` | constructor | `None` | public | Constructs a MapTransform that wraps around the given viewport\_zoom. |
| `set_centre_of_viewport( const point_type &centre_of_viewport)` | method | `void` | public | Sets the centre of the map viewport in scene coordinates. |
| `translate( double dx, double dy)` | method | `void` | public | Translates the centre of viewport by dx and dy, which are expressed in scene coordinates. |
| `get_rotation()` | method | `double` | public | Returns the angle of rotation of the map viewport in degrees. |
| `set_rotation( double rotation)` | method | `void` | public | Sets the angle of rotation of the map viewport in degrees. |
| `rotate( double angle)` | method | `void` | public | Rotates the viewport by angle in degrees. |
| `get_zoom_factor()` | method | `double` | public | Returns the current zoom factor. |
| `MIN_CENTRE_OF_VIEWPORT_X` | field | `double` | public | The smallest value in the x dimension permitted for the centre of viewport, in scene coordinates. |
| `MAX_CENTRE_OF_VIEWPORT_X` | field | `double` | public | The largest value in the x dimension permitted for the centre of viewport, in scene coordinates. |
| `MIN_CENTRE_OF_VIEWPORT_Y` | field | `double` | public | The smallest value in the y dimension permitted for the centre of viewport, in scene coordinates. |
| `MAX_CENTRE_OF_VIEWPORT_Y` | field | `double` | public | The largest value in the y dimension permitted for the centre of viewport, in scene coordinates. |
| `transform_changed( const GPlatesGui::MapTransform &map_transform)` | method | `void` | public | Emitted when the centre of viewport, the rotation or the zoom factor is changed. |
| `handle_zoom_changed()` | method | `void` | private | — |
| `d_viewport_zoom` | field | `ViewportZoom` | private | — |
| `d_centre_of_viewport` | field | `point_type` | private | — |
| `d_rotation` | field | `double` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `MIN_CENTRE_OF_VIEWPORT_X` | variable | `double` | — |
| `MAX_CENTRE_OF_VIEWPORT_X` | variable | `double` | — |
| `MIN_CENTRE_OF_VIEWPORT_Y` | variable | `double` | — |
| `MAX_CENTRE_OF_VIEWPORT_Y` | variable | `double` | — |
| `GPLATES_GUI_MAPTRANSFORM_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/MapTransform tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/MapView](../qt-widgets/MapView.md) | qt-widgets | 28 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 14 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 13 |
| [qt-widgets/GlobeAndMapWidget](../qt-widgets/GlobeAndMapWidget.md) | qt-widgets | 5 |
| [qt-widgets/ReconstructionViewWidget](../qt-widgets/ReconstructionViewWidget.md) | qt-widgets | 4 |
| [gui/MapCanvasTool](MapCanvasTool.md) | gui | 3 |
| [canvas-tools/PanMap](../canvas-tools/PanMap.md) | canvas-tools | 2 |
| [canvas-tools/ZoomMap](../canvas-tools/ZoomMap.md) | canvas-tools | 2 |
| [canvas-tools/CanvasToolAdapterForMap](../canvas-tools/CanvasToolAdapterForMap.md) | canvas-tools | 1 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&viewport_zoom` | `zoom_changed()` | `this` | `handle_zoom_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/MapTransform.h
python scripts/gpq.py def GPlatesGui::MapTransform --body
python scripts/gpq.py uses MapTransform --kind class
python scripts/gpq.py hier MapTransform
```

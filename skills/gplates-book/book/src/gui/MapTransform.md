# MapTransform

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 615 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/MapTransform.h` | C++ | 177 |
| `src/gui/MapTransform.cc` | C++ | 128 |

## Overview

`MapTransform` is the map view's equivalent of a camera: it holds the centre of
the viewport (in projected scene coordinates), the rotation angle, and forwards
the current zoom factor from a `ViewportZoom` it wraps. `GPlatesQtWidgets::MapView`
and `MapCanvasTool` subclasses read and drive it to pan, rotate and zoom the
map, and it emits `transform_changed()` whenever any of the three change so
the view can re-render — including when `ViewportZoom` itself changes,
relayed through the private `handle_zoom_changed()` slot.

It does not own a `QTransform` or perform any projection maths itself; it is
purely the small piece of mutable state that describes the current view, which
callers translate into an actual transform when painting.

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

- `set_centre_of_viewport()` (and therefore `translate()`) rejects the move
  entirely if either coordinate falls outside
  `MIN`/`MAX_CENTRE_OF_VIEWPORT_X`/`Y` — it does **not** clamp. The source notes
  this is deliberate: clamping one axis while a rotated map is dragged would
  make the map appear to slide diagonally along an edge instead of stopping.
- `set_rotation()` wraps the stored angle back into `(-360, 360)` but does not
  further normalise it to `[0, 360)` or `[-180, 180)`.
- `d_viewport_zoom` is stored as a reference, so the referenced `ViewportZoom`
  must outlive the `MapTransform`.

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

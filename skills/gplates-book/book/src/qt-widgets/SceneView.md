# SceneView

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1014 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/SceneView.h` | C++ | 190 |

## Overview

Abstract base class for viewport implementations (globe 3D and map 2D). Defines the interface for camera control, rendering, and viewport management shared by `GlobeCanvas` and `MapView`. Provides methods to set camera viewpoint and orientation, render the scene to image formats or vector graphics, and handle interactive camera motions. The class is non-copyable and cannot be instantiated directly.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::SceneView`](#gplatesqtwidgetssceneview) | class | [`GPlatesViewOperations::QueryProximityThreshold`](../view-operations/QueryProximityThreshold.md) | — | 2 | Base class of GlobeCanvas and MapView. |

## Members

### `GPlatesQtWidgets::SceneView`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SceneView()` | constructor | `None` | public | — |
| `~SceneView()` | destructor | `None` | public | — |
| `set_camera_viewpoint( const GPlatesMaths::LatLonPoint &llp)` | method | `void` | public | — |
| `set_orientation( const GPlatesMaths::Rotation &rotation /*bool should_emit_external_signal = true */)` | method | `void` | public | FIXME should this be pure virtual? |
| `orientation()` | method | `boost::optional<GPlatesMaths::Rotation>` | public | — |
| `handle_zoom_change()` | method | `void` | public | — |
| `camera_llp()` | method | `boost::optional<GPlatesMaths::LatLonPoint>` | public | — |
| `get_viewport_size()` | method | `QSize` | public | Returns the dimensions of the viewport in device \*independent\* pixels (ie, widget size). |
| `render_to_qimage( const QSize &image_size_in_device_independent_pixels, const GPlatesGui::Colour &image_clear_colour)` | method | `QImage` | public | Renders the scene to a QImage of the dimensions specified by image\_size. |
| `render_opengl_feedback_to_paint_device( QPaintDevice &feedback_paint_device)` | method | `void` | public | Paint the scene, as best as possible, by re-directing OpenGL rendering to the specified paint device. |
| `update_canvas()` | method | `void` | public | — |
| `move_camera_up()` | method | `void` | public | — |
| `move_camera_down()` | method | `void` | public | — |
| `move_camera_left()` | method | `void` | public | — |
| `move_camera_right()` | method | `void` | public | — |
| `rotate_camera_clockwise()` | method | `void` | public | — |
| `rotate_camera_anticlockwise()` | method | `void` | public | — |
| `reset_camera_orientation()` | method | `void` | public | — |
| `SceneView( const SceneView &other)` | constructor | `None` | private | Make copy and assignment private to prevent copying/assignment |
| `operator=` | field | `SceneView` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_SCENEVIEW_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [api/PyViewportWindow](../api/PyViewportWindow.md) | api | 3 |
| [gui/ExportSvgAnimationStrategy](../gui/ExportSvgAnimationStrategy.md) | gui | 3 |
| [gui/ExternalSyncController](../gui/ExternalSyncController.md) | gui | 3 |
| [gui/Dialogs](../gui/Dialogs.md) | gui | 2 |
| [qt-widgets/GlobeCanvas](GlobeCanvas.md) | qt-widgets | 2 |
| [qt-widgets/MapView](MapView.md) | qt-widgets | 2 |
| [gui/ExportImageAnimationStrategy](../gui/ExportImageAnimationStrategy.md) | gui | 1 |
| [gui/FeatureFocus](../gui/FeatureFocus.md) | gui | 1 |
| [qt-widgets/DrawStyleDialog](DrawStyleDialog.md) | qt-widgets | 1 |
| [qt-widgets/ExportImageResolutionOptionsWidget](ExportImageResolutionOptionsWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/SceneView.h
python scripts/gpq.py def GPlatesQtWidgets::SceneView --body
python scripts/gpq.py uses SceneView --kind class
python scripts/gpq.py hier SceneView
```

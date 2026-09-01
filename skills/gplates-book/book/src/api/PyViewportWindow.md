# PyViewportWindow

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 301 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PyViewportWindow.cc` | C++ | 250 |

## Overview

This class wraps the GUI's viewport and camera controls, exposing them to Python scripts. It holds references to the main window, active scene view, and viewport zoom controller, which are retrieved from the `Application` singleton at construction. Methods dispatch camera operations (pan, rotate, reset) to the scene view and zoom operations to the zoom controller. `set_focus` allows setting the feature focus and optionally auto-panning the camera to the focused feature, and accepts either a `Feature` object directly or a feature ID string to look up in the loaded feature collections.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::ViewportWindow`](#gplatesapiviewportwindow) | class | — | — | 0 | — |

## Members

### `GPlatesApi::ViewportWindow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ViewportWindow()` | constructor | `None` | public | — |
| `status_message(const char* msg)` | method | `void` | public | — |
| `set_camera(double lat, double lon)` | method | `void` | public | — |
| `move_camera_up()` | method | `void` | public | — |
| `move_camera_down()` | method | `void` | public | — |
| `move_camera_left()` | method | `void` | public | — |
| `move_camera_right()` | method | `void` | public | — |
| `rotate_camera_clockwise()` | method | `void` | public | — |
| `rotate_camera_anticlockwise()` | method | `void` | public | — |
| `reset_camera_orientation()` | method | `void` | public | — |
| `zoom_in(double num_levels)` | method | `void` | public | — |
| `zoom_out(double num_levels)` | method | `void` | public | — |
| `reset_zoom()` | method | `void` | public | — |
| `set_zoom_percent(double new_zoom_percent)` | method | `void` | public | — |
| `set_focus( Feature feature)` | method | `void` | public | — |
| `set_focus_by_id( boost::python::object id)` | method | `void` | public | — |
| `d_viewport` | field | `GPlatesQtWidgets::ViewportWindow` | private | — |
| `d_scene_view` | field | `GPlatesQtWidgets::SceneView` | private | — |
| `d_zoom` | field | `GPlatesGui::ViewportZoom` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `export_main_window()` | function | `void` | — |

## Notes

All methods dispatch to the GUI thread via `DISPATCH_GUI_FUN` to ensure thread safety. The constructor captures references to singleton objects from `Application::instance()`, not owned instances.

## Used by

*Nothing in the tree references this unit.*

## Related

**Python bindings**

| Python name | Kind | Owner | C++ |
|---|---|---|---|
| `MainWindow` | class | — | `ViewportWindow` |
| `set_status_message` | method | `MainWindow` | `&ViewportWindow::status_message` |
| `set_camera` | method | `MainWindow` | `&ViewportWindow::set_camera` |
| `move_camera_up` | method | `MainWindow` | `&ViewportWindow::move_camera_up` |
| `move_camera_down` | method | `MainWindow` | `&ViewportWindow::move_camera_down` |
| `move_camera_left` | method | `MainWindow` | `&ViewportWindow::move_camera_left` |
| `move_camera_right` | method | `MainWindow` | `&ViewportWindow::move_camera_right` |
| `rotate_camera_clockwise` | method | `MainWindow` | `&ViewportWindow::rotate_camera_clockwise` |
| `rotate_camera_anticlockwise` | method | `MainWindow` | `&ViewportWindow::rotate_camera_anticlockwise` |
| `reset_camera_orientation` | method | `MainWindow` | `&ViewportWindow::reset_camera_orientation` |
| `zoom_in` | method | `MainWindow` | `&ViewportWindow::zoom_in` |
| `zoom_out` | method | `MainWindow` | `&ViewportWindow::zoom_out` |
| `reset_zoom` | method | `MainWindow` | `&ViewportWindow::reset_zoom` |
| `set_zoom_percent` | method | `MainWindow` | `&ViewportWindow::set_zoom_percent` |
| `set_focus` | method | `MainWindow` | `&ViewportWindow::set_focus_by_id` |

*... and 1 more bindings.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/PyViewportWindow.cc
python scripts/gpq.py def GPlatesApi::ViewportWindow --body
python scripts/gpq.py uses ViewportWindow --kind class
python scripts/gpq.py hier ViewportWindow
```

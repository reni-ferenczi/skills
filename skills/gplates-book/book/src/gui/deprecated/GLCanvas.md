# GLCanvas

[Book TOC](../../../TOC.md) · [gui](../../../components/gui.md) · cluster Community 273 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/deprecated/GLCanvas.h` | C++ | 160 |
| `src/gui/deprecated/GLCanvas.cc` | C++ | 799 |

## Overview

[[[PROSE overview unit=gui/deprecated/GLCanvas tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::GLCanvas`](#gplatesguiglcanvas) | class | `wxGLCanvas` | — | 0 | — |

## Members

### `GPlatesGui::GLCanvas`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLCanvas(MainWindow *parent, const wxSize &size = wxDefaultSize, const wxPoint &position = wxDefaultPosition)` | constructor | `None` | public | — |
| `OnPaint(wxPaintEvent&)` | method | `void` | public | Paint the picture. |
| `OnSize(wxSizeEvent&)` | method | `void` | public | Set the dimensions of our picture. |
| `OnMouseEvent(wxMouseEvent&)` | method | `void` | public | Handle all mouse events. |
| `OnEraseBackground(wxEraseEvent&)` | method | `void` | public | According to the wxWindows docs, declaring this function to be empty eliminates flicker on some platforms (mainly win32). |
| `OnSpinGlobe(wxCommandEvent&)` | method | `void` | public | Change the mode of interaction to 'spin globe' mode. |
| `ZoomIn()` | method | `void` | public | Zoom in. |
| `ZoomOut()` | method | `void` | public | Zoom out. |
| `ZoomReset()` | method | `void` | public | Reset zoom to initial value of 1. |
| `GetSphereCoordFromScreen(int screenx, int screeny)` | method | `GPlatesMaths::PointOnSphere` | public | Return the PointOnSphere corresponding to the given screen coordinate, or else return a NULL pointer. @pre 0 \<= screenx \< SCREEN\_WIDTH, 0 \<= screeny \< SCREEN\_HEIGHT. @warning The client is responsible for the deletion of the memory pointed ... |
| `GetGlobe()` | method | `Globe` | public | — |
| `_parent` | field | `MainWindow` | private | — |
| `_popup_menu` | field | `wxMenu` | private | — |
| `_globe` | field | `Globe` | private | — |
| `_mouse_x` | field | `int` | private | — |
| `_mouse_y` | field | `int` | private | — |
| `_width` | field | `int` | private | — |
| `_height` | field | `int` | private | — |
| `_smaller_dim` | field | `GLdouble` | private | — |
| `_larger_dim` | field | `GLdouble` | private | — |
| `_wheel_rotation` | field | `int` | private | — |
| `_is_initialised` | field | `bool` | private | — |
| `m_viewport_zoom` | field | `ViewportZoom` | private | — |
| `InitGL()` | method | `void` | private | — |
| `SetView()` | method | `void` | private | — |
| `HandleZoomChange()` | method | `void` | private | — |
| `GetDimensions()` | method | `void` | private | — |
| `ClearCanvas(const Colour &c = Colour::BLACK)` | method | `void` | private | — |
| `getUniverseCoordY(int screen_x)` | method | `GPlatesMaths::real_t` | private | — |
| `getUniverseCoordZ(int screen_y)` | method | `GPlatesMaths::real_t` | private | — |
| `CreatePopupMenu()` | method | `wxMenu` | private | Create a new wxMenu (for the popup menu) and return it. |
| `mouse_event_type` | enum | `None` | private | — |
| `HandleRightMouseClick(long mouse_x, long mouse_y)` | method | `void` | private | — |
| `HandleLeftMouseEvent(enum mouse_event_type type)` | method | `void` | private | — |
| `HandleWheelRotation(int delta)` | method | `void` | private | — |
| `HandleMouseMotion()` | method | `void` | private | — |
| `DECLARE_EVENT_TABLE()` | method | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `FRAMING_RATIO` | variable | `GLfloat` | At the initial zoom, the smaller dimension of the GLCanvas will be FRAMING\_RATIO times the diameter of the Globe. |
| `eyex` | variable | `GLfloat` | — |
| `eyey` | variable | `GLfloat` | — |
| `eyez` | variable | `GLfloat` | — |
| `calcGlobePosDiscrim(const GPlatesMaths::real_t &y, const GPlatesMaths::real_t &z)` | function | `GPlatesMaths::real_t` | — |
| `isOnGlobe(const GPlatesMaths::real_t &discrim)` | function | `bool` | — |
| `onGlobe(const GPlatesMaths::real_t &y, const GPlatesMaths::real_t &z, const GPlatesMaths::real_t &discrim)` | function | `GPlatesMaths::PointOnSphere` | — |
| `atIntersectionWithGlobe(const GPlatesMaths::real_t &y, const GPlatesMaths::real_t &z, const GPlatesMaths::real_t &discrim)` | function | `GPlatesMaths::PointOnSphere` | — |
| `virtualGlobePosition(const GPlatesMaths::real_t &y, const GPlatesMaths::real_t &z)` | function | `GPlatesMaths::PointOnSphere` | — |
| `SetShouldBePainted( std::vector< GPlatesGeo::DrawableData * > &items, bool should_be_painted)` | function | `void` | — |
| `RepaintTheCanvas( GPlatesGui::GLCanvas *the_canvas)` | function | `void` | — |
| `HandleSelectedItems( GPlatesGui::GLCanvas *the_canvas, std::priority_queue< GPlatesState::Layout::CloseDatum > &sorted_results)` | function | `void` | It is assumed that the number of elements in sorted\_results is greater than zero. |
| `_GPLATES_GUI_GLCANVAS_H_` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/deprecated/GLCanvas tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLMatrix](../../opengl/GLMatrix.md) | opengl | 6 |
| [gui/deprecated/MainWindow](MainWindow.md) | gui | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/deprecated/GLCanvas.h
python scripts/gpq.py def GPlatesGui::GLCanvas --body
python scripts/gpq.py uses GLCanvas --kind class
python scripts/gpq.py hier GLCanvas
```

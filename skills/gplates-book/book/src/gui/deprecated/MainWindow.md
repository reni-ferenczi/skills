# MainWindow

[Book TOC](../../../TOC.md) · [gui](../../../components/gui.md) · cluster Community 287 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/deprecated/MainWindow.h` | C++ | 186 |
| `src/gui/deprecated/MainWindow.cc` | C++ | 781 |

## Overview

`MainWindow` is the top-level wxFrame that houses the entire deprecated GUI application. It creates and manages a menu bar with File, Reconstruct, and Help menus, a toolbar with zoom controls and an animation stop button, a status bar displaying current time, globe position, and zoom level, and a `GLCanvas` for rendering the globe visualization. The window handles file operations (opening, importing, exporting, and saving data and rotation files), reconstruction commands (jumping to a specific time, returning to present, and running animations), and zoom controls. It maintains two operational modes: normal mode for interactive use, and animation mode which disables menus and enables the Escape key to interrupt animations. The window also caches the last-used directories and animation parameters for convenience.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`Menus::MenuInstance`](#menusmenuinstance) | struct | — | — | 0 | — |
| [`Menus::(anonymous enum)`](#menusanonymous-enum) | enum | — | — | 0 | IDs for the menu instances. |
| [`StatusbarFields::(anonymous enum)`](#statusbarfieldsanonymous-enum) | enum | — | — | 0 | IDs for the statusbar fields. |
| [`(anonymous)::AnimEvtHandler`](#anonymousanimevthandler) | class | `wxEvtHandler` | — | 0 | Extra event-handling functionality used during animations. |
| [`GPlatesGui::MainWindow`](#gplatesguimainwindow) | class | `wxFrame` | — | 0 | — |

## Members

### `Menus::MenuInstance`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `title` | field | `char` | public | — |
| `fn` | field | `create_fn` | public | — |

### `Menus::(anonymous enum)`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MENU_FILE` | enumerator | `None` | — | — |
| `MENU_RECONSTRUCT` | enumerator | `None` | — | — |
| `MENU_HELP` | enumerator | `None` | — | — |

### `StatusbarFields::(anonymous enum)`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `INFO` | enumerator | `None` | — | — |
| `POSITION` | enumerator | `None` | — | — |
| `TIME` | enumerator | `None` | — | — |
| `ZOOM` | enumerator | `None` | — | — |

### `(anonymous)::AnimEvtHandler`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AnimEvtHandler(GPlatesGui::MainWindow *w)` | constructor | `None` | public | — |
| `OnEscape(wxCommandEvent&)` | method | `void` | public | — |
| `_main_window` | field | `GPlatesGui::MainWindow` | private | — |
| `DECLARE_EVENT_TABLE()` | method | `None` | private | — |

### `GPlatesGui::MainWindow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MainWindow(wxFrame* parent, const wxString& title = "", const wxSize& size = wxDefaultSize, const wxPoint& pos = wxDefaultPosition)` | constructor | `None` | public | — |
| `OnOpenData(wxCommandEvent&)` | method | `void` | public | File events |
| `OnLoadRotation(wxCommandEvent&)` | method | `void` | public | — |
| `OnImport(wxCommandEvent&)` | method | `void` | public | — |
| `OnExport(wxCommandEvent&)` | method | `void` | public | — |
| `OnSaveAllData(wxCommandEvent&)` | method | `void` | public | — |
| `OnExit(wxCommandEvent&)` | method | `void` | public | — |
| `OnReconstructTime(wxCommandEvent&)` | method | `void` | public | Reconstruct events |
| `OnReconstructPresent(wxCommandEvent&)` | method | `void` | public | — |
| `OnReconstructAnimation(wxCommandEvent&)` | method | `void` | public | — |
| `OnHelpAbout(wxCommandEvent&)` | method | `void` | public | Help events |
| `OnZoomIn(wxCommandEvent&)` | method | `void` | public | Toolbar events |
| `OnZoomOut(wxCommandEvent&)` | method | `void` | public | — |
| `OnZoomReset(wxCommandEvent&)` | method | `void` | public | — |
| `SetCurrentTime(const GPlatesGlobal::fpdata_t &t)` | method | `void` | public | Set the current geological time (as displayed in the status bar) to t. |
| `SetCurrentZoom(unsigned z)` | method | `void` | public | Set the current zoom (as displayed in the status bar) to z percent. |
| `SetCurrentGlobePosOffGlobe()` | method | `void` | public | Set the current position on the globe (as displayed in the status bar) to "(off globe)". |
| `SetCurrentGlobePos(const GPlatesGlobal::fpdata_t &lat, const GPlatesGlobal::fpdata_t &lon)` | method | `void` | public | Set the current position on the globe (as displayed in the status bar) to (lat, lon). |
| `SetOpModeToAnimation()` | method | `void` | public | Set the current mode of operation to 'animation'. |
| `ReturnOpModeToNormal()` | method | `void` | public | Return the current mode of operation to 'normal'. |
| `StopAnimation(bool interrupted)` | method | `void` | public | Notify this main window that the animation has been stopped. |
| `DEFAULT_WINDOWID` | field | `wxWindowID` | private | XXX: DEFAULT\_WINDOWID should be available to the entire GUI system. |
| `_menu_bar` | field | `wxMenuBar` | private | Gui components contained within this window. |
| `_tool_bar` | field | `wxToolBar` | private | — |
| `_status_bar` | field | `wxStatusBar` | private | — |
| `_canvas` | field | `GLCanvas` | private | — |
| `_last_load_dir` | field | `wxString` | private | For opening and saving files |
| `_last_save_dir` | field | `wxString` | private | For opening and saving files |
| `_last_start_time` | field | `GPlatesGlobal::fpdata_t` | private | For animations |
| `_last_end_time` | field | `GPlatesGlobal::fpdata_t` | private | — |
| `_last_time_delta` | field | `GPlatesGlobal::fpdata_t` | private | — |
| `_last_finish_on_end` | field | `bool` | private | — |
| `CreateMenuBar(long style = 0)` | method | `wxMenuBar` | private | Create a new wxMenuBar and return it. |
| `CreateToolBar_(long style = 0)` | method | `wxToolBar` | private | Create a new wxToolBar and return it. 2006-08-30: Appended an underscore to the end of the function name so that it doesn't hide the virtual function of the same name in the base class. |
| `DefaultAccelTab()` | method | `wxAcceleratorTable` | private | — |
| `operation_modes` | enum | `None` | private | — |
| `_operation_mode` | field | `enum operation_modes` | private | The current mode of operation. |
| `DECLARE_EVENT_TABLE()` | method | `None` | private | Declare a wxWindows event table. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `CreateFileMenu()` | function | `wxMenu` | — |
| `CreateViewMenu()` | function | `wxMenu` | — |
| `CreateReconstructMenu()` | function | `wxMenu` | — |
| `CreateHelpMenu()` | function | `wxMenu` | — |
| `INSTANCES` | variable | `MenuInstance` | The menu instances. |
| `WIDTHS` | variable | `int` | The widths of the statusbar fields. |
| `_GPLATES_GUI_MAINWINDOW_H_` | macro | `None` | — |

## Notes

Mode switching between `NORMAL_MODE` and `ANIMATION_MODE` manipulates the event handler stack and replaces the accelerator table; in animation mode, all menus are disabled and the Escape key stops the animation. The window owns the `_menu_bar`, `_tool_bar`, `_status_bar`, and `_canvas` pointers. The status bar contains four fields with fixed widths except the first (info) field which is variable-width. Animation parameters (`_last_start_time`, `_last_end_time`, `_last_time_delta`, `_last_finish_on_end`) are cached across dialog invocations, and the Reconstruct menu items are currently if-0-ed out.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/deprecated/GLCanvas](GLCanvas.md) | gui | 9 |
| [qt-widgets/VisualLayerWidget](../../qt-widgets/VisualLayerWidget.md) | qt-widgets | 2 |
| [gui/deprecated/GPlatesApp](GPlatesApp.md) | gui | 1 |
| [maths/deprecated/PolylineIntersections_test](../../maths/deprecated/PolylineIntersections_test.md) | maths | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/deprecated/MainWindow.h
python scripts/gpq.py def GPlatesGui::MainWindow --body
python scripts/gpq.py uses MainWindow --kind class
python scripts/gpq.py hier MainWindow
```

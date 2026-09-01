# MainWindow

[Book TOC](../../../TOC.md) · [gui](../../../components/gui.md) · cluster Community 287 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/deprecated/MainWindow.h` | C++ | 186 |
| `src/gui/deprecated/MainWindow.cc` | C++ | 781 |

## Overview

[[[PROSE overview unit=gui/deprecated/MainWindow tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=gui/deprecated/MainWindow tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

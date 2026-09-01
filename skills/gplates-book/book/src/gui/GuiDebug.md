# GuiDebug

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 505 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/GuiDebug.h` | C++ | 150 |
| `src/gui/GuiDebug.cc` | C++ | 316 |

## Overview

A debug utility class that creates a Debug menu in the main window when instantiated (via the `--debug-gui` command-line flag). The class uses Qt introspection to automatically discover all slots with the `debug_` prefix and adds them as menu items. It provides utility functions for introspecting and manipulating the GUI at runtime: printing menu structure, examining font metrics, checking system paths, testing unsaved changes functionality, and a catch-all debug action (Ctrl-Alt-/) for rapid testing.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::GuiDebug`](#gplatesguiguidebug) | class | `QObject` | — | 0 | This GUI class creates a 'Debug' menu that developers can use to assist them in debugging GUI problems and testing code that does not yet have a working UI. |

## Members

### `GPlatesGui::GuiDebug`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GuiDebug( GPlatesQtWidgets::ViewportWindow &viewport_window_, GPlatesPresentation::ViewState &view_state_, GPlatesAppLogic::ApplicationState &app_state_, QObject *parent_)` | constructor | `None` | public | — |
| `~GuiDebug()` | destructor | `None` | public | — |
| `handle_gui_debug_action()` | method | `void` | private | Respond to the all-purpose 'Debug Action' hotkey, Ctrl-Alt-/ |
| `debug_set_all_files_clean()` | method | `void` | private | For testing Unsaved Changes functionality. |
| `debug_menu_structure()` | method | `void` | private | So I can fix the documentation. |
| `debug_font_metrics()` | method | `void` | private | To use when fonts aren't behaving. |
| `debug_system_paths()` | method | `void` | private | So we know what the QStandardPaths::writableLocation actually map to on each platform. |
| `create_menu()` | method | `void` | private | Adds menus and connects to actions, etc. |
| `find_child_qobject( QString name)` | method | `QObject` | private | Finds child of ViewportWindow with given objectName dynamically, by traversing the widget hierarchy. |
| `d_viewport_window_ptr` | field | `GPlatesQtWidgets::ViewportWindow` | private | Pointer to the ViewportWindow so we can access all manner of things. |
| `d_view_state_ptr` | field | `GPlatesPresentation::ViewState` | private | Pointer to the ViewState so we can access all manner of things. |
| `d_app_state_ptr` | field | `GPlatesAppLogic::ApplicationState` | private | Pointer to the ApplicationState so we can access all manner of things. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `add_slots_to_menu( const QObject *object, QString prefix, QMenu *menu)` | function | `void` | Given a QObject, introspect it for slots that take no arguments (and optionally only ones that start with a given prefix), and add a menu entry for each slot to the supplied menu. |
| `add_debug_slots_to_menu( const QObject *object, QMenu *menu)` | function | `void` | Convenience version of add\_slots\_to\_menu that only adds slots with the prefix 'debug\_'. |
| `add_slots_as_submenu( const QObject *object, QString prefix, QMenu *menu)` | function | `void` | Convenience version of add\_slots\_to\_menu that adds menu items under a submenu with the class name of the object. |
| `print_menu_structure( QWidget *menu, QString prefix = "* ", QString indentation = "")` | function | `void` | Recursively print out our menu structure. |
| `GPLATES_GUI_GUIDEBUG_H` | macro | `None` | — |

## Notes

Uses Qt's `QMetaObject` introspection to automatically discover and add menu items for slots with the `debug_` prefix; only slots with no parameters are eligible. The Debug menu is only created when GuiDebug is instantiated, which occurs only when the `--debug-gui` command-line flag is present, keeping it out of production builds.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 3 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `action_Gui_Debug_Action` | `triggered()` | `this` | `handle_gui_debug_action()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/GuiDebug.h
python scripts/gpq.py def GPlatesGui::GuiDebug --body
python scripts/gpq.py uses GuiDebug --kind class
python scripts/gpq.py hier GuiDebug
```

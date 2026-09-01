# SessionMenu

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 753 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/SessionMenu.h` | C++ | 136 |
| `src/gui/SessionMenu.cc` | C++ | 168 |

## Overview

[[[PROSE overview unit=gui/SessionMenu tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::SessionMenu`](#gplatesguisessionmenu) | class | `QObject` | — | 0 | This class is responsible for providing the user interface to SessionManagement. |

## Members

### `GPlatesGui::SessionMenu`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SessionMenu( GPlatesAppLogic::ApplicationState &app_state_, GPlatesPresentation::ViewState &view_state_, GPlatesGui::FileIOFeedback &file_io_feedback_, QObject *parent_ = NULL)` | constructor | `None` | public | — |
| `~SessionMenu()` | destructor | `None` | public | — |
| `init( QMenu &menu_)` | method | `void` | public | Does Menu Action initialisation, which must wait until after ViewportWindow has called setupUi(). menu\_ - the QMenu to mess with. |
| `regenerate_menu()` | method | `void` | public | Relabels and shows/hides appropriate Menu Actions to match the current Recent Sessions List as returned by GPlatesAppLogic::SessionManagement. |
| `open_previous_session( int session_slot_to_load = 0)` | method | `void` | public | — |
| `handle_action_triggered( QAction *act)` | method | `void` | private | — |
| `d_session_management_ptr` | field | `GPlatesPresentation::SessionManagement` | private | Pointer to the session management, to get session info. |
| `d_file_io_feedback_ptr` | field | `GPlatesGui::FileIOFeedback` | private | Pointer to FileIOFeedback, to initiate change while trapping exceptions. |
| `d_menu_ptr` | field | `QPointer<QMenu>` | private | Guarded pointer to the QMenu we are allowed to mess with. |
| `d_no_sessions_action` | field | `QPointer<QAction>` | private | The "No sessions to load" placeholder Action. |
| `d_recent_session_actions` | field | `QList<QPointer<QAction> >` | private | One QAction for each potential session to restore, in order. |
| `d_recent_session_action_group` | field | `QActionGroup` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `create_tooltip_from_session( const GPlatesPresentation::SessionManagement::InternalSessionInfo &session)` | function | `QString` | — |
| `create_statustip_from_session( const GPlatesPresentation::SessionManagement::InternalSessionInfo &session)` | function | `QString` | — |
| `GPLATES_GUI_SESSIONMENU_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/SessionMenu tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 20 |

## Related

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_session_management_ptr` | `session_list_updated()` | `this` | `regenerate_menu()` |
| `&d_recent_session_action_group` | `triggered(QAction *)` | `this` | `handle_action_triggered(QAction *)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/SessionMenu.h
python scripts/gpq.py def GPlatesGui::SessionMenu --body
python scripts/gpq.py uses SessionMenu --kind class
python scripts/gpq.py hier SessionMenu
```

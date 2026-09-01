# SessionMenu

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 753 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/SessionMenu.h` | C++ | 136 |
| `src/gui/SessionMenu.cc` | C++ | 168 |

## Overview

`GPlatesGui::SessionMenu` builds and maintains the "recent sessions" submenu shown by `ViewportWindow`, translating the session list kept by `presentation/SessionManagement` into `QAction`s the user can click. `init()` must be called only after the owning `QMenu` has been created by `setupUi()`; it then populates a fixed pool of 24 placeholder actions (plus one disabled "no sessions" placeholder) rather than adding and removing actions per session, which keeps the signal/slot bookkeeping simple. `regenerate_menu()` is a slot connected to `SessionManagement::session_list_updated()`; each time the list changes it relabels, shows or hides the fixed actions to match, and sets each visible action's tooltip and status tip from `create_tooltip_from_session()`/`create_statustip_from_session()`, which join the session's loaded file paths.

Clicking any action fires the shared `QActionGroup`'s `triggered()` signal, which `handle_action_triggered()` turns into a session slot index (stored in the action's `QVariant` data) and forwards to `open_previous_session()`. That method simply delegates to `GPlatesGui::FileIOFeedback::open_previous_session()`, which is where the actual file loading and exception handling happen.

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

The menu action pool is fixed at 24 slots; a recent-sessions list longer than that would have no menu entries for the overflow. `d_menu_ptr` is a `QPointer`, so it safely becomes null if the menu is destroyed, but `init()` must still be called exactly once, after `setupUi()`, before any of the pooled actions exist.

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

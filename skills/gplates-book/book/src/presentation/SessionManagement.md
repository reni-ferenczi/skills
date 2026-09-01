# SessionManagement

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 166 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/SessionManagement.h` | C++ | 596 |
| `src/presentation/SessionManagement.cc` | C++ | 720 |

## Overview

`GPlatesPresentation::SessionManagement` is the `QObject` that owns the "which files were loaded and what did the Layers system look like" behaviour of GPlates: recent-session persistence via `UserPreferences`, and the newer project-file (`.gproj`) mechanism, both built on top of `Session`/`InternalSession`/`ProjectSession`. It exposes three lightweight, read-only wrapper classes — `SessionInfo`, `InternalSessionInfo` and `ProjectInfo` — so callers such as the Recent Sessions menu can inspect a past session's description, timestamp and files without holding a reference to the underlying `InternalSession`/`ProjectSession` object itself.

The public surface splits into the recent-sessions path (`get_recent_session_list()`, `load_previous_session()`, `save_session()`) and the project path (`is_current_session_a_project()`, `load_project()`, `save_project()`), which converge on shared private helpers — `clear_session_state()`, `load_session_state()`, `save_session_state()` — that actually unload/reload files, layers and application state. `clear_session()` and `close_event_hook()` are the entry points used respectively when the user asks to start fresh and when GPlates is shutting down and needs to remember the current file set for next time.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::SessionManagement`](#gplatespresentationsessionmanagement) | class | `QObject`<br>`boost::noncopyable` | — | 0 | As a first-cut implementation of a Projects system, get GPlates to remember which files were loaded and the state of the Layers system between sessions, by storing session data via UserPreferences. |

## Members

### `GPlatesPresentation::SessionManagement`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SessionInfo` | class | `None` | public | Information about a session such as time created, description and loaded files. |
| `InternalSessionInfo` | class | `None` | public | Information about an internal session. |
| `ProjectInfo` | class | `None` | public | Information about a project session such as project filename and existence of absolute file paths in project (versus file paths relative to the project file if the project file has moved location). |
| `SessionManagement( GPlatesAppLogic::ApplicationState &app_state, GPlatesPresentation::ViewState &view_state)` | constructor | `None` | public | Constructor. |
| `~SessionManagement()` | destructor | `None` | public | — |
| `initialise()` | method | `void` | public | Initialise the session management once the entire application has started up. |
| `get_recent_session_list()` | method | `QList<InternalSessionInfo>` | public | Returns a list of all session information objects that are currently in persistent storage. |
| `clear_session( bool save_current_session)` | method | `void` | public | Clear the current session so there's no files loaded and no auto-created or user-created layers left. |
| `get_previous_session_info( int session_slot = 0)` | method | `boost::optional<InternalSessionInfo>` | public | Retrieves the session information from the most recent session (default), or specified session slot, from user preference storage. |
| `load_previous_session( const InternalSessionInfo &session, bool save_current_session)` | method | `void` | public | Loads the specified session from user preference storage. |
| `save_session()` | method | `bool` | public | Save information about which files are currently loaded to persistent storage and the entire application state. |
| `is_current_session_a_project()` | method | `boost::optional<ProjectInfo>` | public | Returns the project information if the current session is a project session, otherwise returns none. |
| `is_current_session_a_project_with_unsaved_changes()` | method | `bool` | public | Returns true if the current session is a project session and it has unsaved session state changes since it was last saved or restored. |
| `get_project_info( const QString &project_filename)` | method | `ProjectInfo` | public | Retrieves the project information from the specified project file. |
| `load_project( const ProjectInfo &project, bool save_current_session)` | method | `void` | public | Loads a project session from the specified project (similar to load\_previous\_session but not loading from the recent sessions list). |
| `save_project( const QString &project_filename)` | method | `void` | public | Saves the current session state to the specified project file. |
| `close_event_hook()` | method | `void` | public | GPlates is closing and we are to remember the current loaded file set (if that is what the user wants us to do in this situation according to user preferences). |
| `debug_session_state()` | method | `void` | public | — |
| `session_list_updated()` | method | `void` | public | Emitted when we write a new session list to persistent storage, so that menus can be updated. |
| `changed_project_filename( boost::optional<QString> project_filename)` | method | `void` | public | Emitted when a project filename has changed. project\_filename is boost::none when the current session no longer corresponds to a project. |
| `unload_all_files()` | method | `void` | private | Clear out all loaded files (in preparation for loading some new session) |
| `unload_all_unnamed_files()` | method | `void` | private | Clear out all feature collections which do not correspond to a file on disk, i.e. |
| `set_project( boost::optional<ProjectInfo> project)` | method | `void` | private | Sets the current project (or unsets it). |
| `clear_session_state( bool preserve_current_view_time)` | method | `void` | private | Clear the current session state so there's no files loaded and no auto-created or user-created layers left. |
| `load_session_state( const SessionInfo &session_to_load, bool save_current_session)` | method | `void` | private | Load files (and re-link Layer relationships) corresponding to the stored session. |
| `save_session_state()` | method | `boost::optional<InternalSession::non_null_ptr_type>` | private | Save information about which files are currently loaded to persistent storage and the entire application state. |
| `store_recent_session_list( const QList<InternalSessionInfo> &session_list)` | method | `void` | private | Save the list of sessions to persistent storage. |
| `d_app_state_ptr` | field | `QPointer<GPlatesAppLogic::ApplicationState>` | private | Guarded pointer back to ApplicationState so we can interact with the rest of GPlates. |
| `d_view_state_ptr` | field | `QPointer<GPlatesPresentation::ViewState>` | private | Guarded pointer back to ViewState so we can interact with the rest of GPlates. |
| `d_clear_session_state` | field | `boost::optional<InternalSession::non_null_ptr_to_const_type>` | private | The session state that represents GPlates at application startup (with no files loaded). |
| `d_project` | field | `boost::optional<ProjectInfo>` | private | The currently loaded project (if any). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PRESENTATION_SESSIONMANAGEMENT_H` | macro | `None` | — |

## Notes

- "Saving" a session records only the list of loaded files and application/layer state, never feature data itself — the files must still exist on disk (or be remapped, see `InternalSessionInfo::set_remapped_file_paths()`) for a saved session to be restorable.
- Loading a session (`load_session_state()`) blocks `ApplicationState::reconstruct` signals and groups layer removals for the duration of the switch, to avoid triggering a cascade of intermediate reconstructions while the old layers are torn down and the new ones built; if loading the requested session fails, it falls back to restoring the session that was current beforehand (saved just before the switch began) rather than leaving GPlates in a partially-loaded state.
- `unload_all_files()`/`clear_session_state()` remove auto-created layers as a side effect of unloading their input files, but user-created layers are not removed automatically and must be deleted explicitly, or they would otherwise accumulate across repeated session switches.
- `d_app_state_ptr` and `d_view_state_ptr` are `QPointer`s rather than owned references, reflecting that `SessionManagement` does not own `ApplicationState`/`ViewState` and must tolerate them (in principle) being destroyed first.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 9 |
| [gui/SessionMenu](../gui/SessionMenu.md) | gui | 6 |
| [gui/UnsavedChangesTracker](../gui/UnsavedChangesTracker.md) | gui | 5 |
| [presentation/ViewState](ViewState.md) | presentation | 4 |
| [gui/GuiDebug](../gui/GuiDebug.md) | gui | 1 |
| [presentation/Application](Application.md) | presentation | 1 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/SessionManagement.h
python scripts/gpq.py def GPlatesPresentation::SessionManagement --body
python scripts/gpq.py uses SessionManagement --kind class
python scripts/gpq.py hier SessionManagement
```

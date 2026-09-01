# ProjectSession

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 679 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/ProjectSession.h` | C++ | 273 |
| `src/presentation/ProjectSession.cc` | C++ | 547 |

## Overview

[[[PROSE overview unit=presentation/ProjectSession tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::ProjectSession`](#gplatespresentationprojectsession) | class | [`Session`](Session.md) | — | 0 | A project file session of GPlates (saved to an archive file). |

## Members

### `GPlatesPresentation::ProjectSession`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ProjectSession>` | public | Convenience typedefs for a shared pointer to a ProjectSession. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ProjectSession>` | public | — |
| `create_restore_session( QString project_filename)` | method | `non_null_ptr_type` | public | Create a ProjectSession object, from the specified project file, that can be used to restore a session. |
| `save_session( QString project_filename)` | method | `non_null_ptr_type` | public | Saves the current session to the specified project file and returns the session in a ProjectSession object. |
| `restore_session()` | method | `void` | public | Restores the session state, contained within, to GPlates. |
| `get_project_filename()` | method | `QString` | public | Returns the project filename (passed into create\_restore\_session or save\_session). |
| `get_num_file_paths()` | method | `int` | public | Returns the number of file paths transcribed via the TranscribeUtils::FilePath API. |
| `has_project_file_moved()` | method | `bool` | public | Returns true if the project file being loaded has moved from where it was saved. |
| `get_absolute_file_paths( QStringList &existing_absolute_file_paths, QStringList &missing_absolute_file_paths)` | method | `void` | public | Returns unique sorted lists of all absolute file paths of transcribed files that currently exist and are currently missing. |
| `get_relative_file_paths( QStringList &existing_relative_file_paths, QStringList &missing_relative_file_paths)` | method | `void` | public | Returns unique sorted lists of all relative file paths of transcribed files that currently exist and are currently missing. |
| `set_load_relative_file_paths( bool load_relative_file_paths = true)` | method | `void` | public | Specify whether to use file paths that are relative to the project file when loading data files (when restore\_session is called) - see get\_relative\_file\_paths. |
| `set_remapped_file_paths( boost::optional< QMap<QString/*missing*/, QString/*existing*/> > file_path_remapping)` | method | `void` | public | Specify whether to remap missing file paths to existing file paths. |
| `has_session_state_changed()` | method | `bool` | public | Compare the current session state with the last saved or restored session state to see if the session state has changed. |
| `d_project_filename` | field | `QString` | private | The name of the project file containing the session state. |
| `d_project_filename_when_saved` | field | `QString` | private | The project filename when the project was saved. |
| `d_all_file_paths_when_saved` | field | `QStringList` | private | A unique sorted list of all transcribed filenames (transcribed via the TranscribeUtils::FilePath API) when the project was saved. |
| `d_load_files_relative_to_project` | field | `boost::optional< std::pair< QString/*project_file_path_when_saved*/, QString/*project_file_path_when_loaded*/> >` | private | Whether to use file paths that are relative to the loaded project file location when loading data files (rather than relative to the location the project file was saved). |
| `d_file_path_remapping` | field | `boost::optional< QMap<QString/*missing*/, QString/*existing*/> >` | private | Whether to remap missing file paths to existing file paths. |
| `d_last_saved_or_restored_session_state` | field | `boost::optional<GPlatesScribe::Transcription::non_null_ptr_to_const_type>` | private | Record the last session state saved or restored by this project file. |
| `ProjectSession( const QString &project_filename_, const QString &project_filename_when_saved_, const QDateTime &time_, const QStringList &filenames_, const QStringList &all_file_paths_when_saved_, boost::optional<GPlatesScribe::Transcription::non_null_ptr_to_const_type> last_saved_or_restored_session_state = boost::non ...` | constructor | `None` | private | Construct a new ProjectSession object. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PRESENTATION_PROJECTSESSION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=presentation/ProjectSession tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/SessionManagement](SessionManagement.md) | presentation | 12 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/ProjectSession.h
python scripts/gpq.py def GPlatesPresentation::ProjectSession --body
python scripts/gpq.py uses ProjectSession --kind class
python scripts/gpq.py hier ProjectSession
```

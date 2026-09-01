# InternalSession

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 1001 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/InternalSession.h` | C++ | 230 |
| `src/presentation/InternalSession.cc` | C++ | 603 |

## Overview

`InternalSession` is the `Session` subclass used for sessions saved to and
restored from the user preferences store (as opposed to a project file saved
to disk). Its job is to hide three generations of on-disk representation
behind one interface: `GPLATES_1_4_OR_BEFORE_FORMAT` (pre-`Scribe`, delegated
to `DeprecatedSessionRestore`), `GPLATES_1_5_FORMAT` (a single `Scribe` text
archive holding both metadata and data transcriptions) and `CURRENT_FORMAT` (a
`Scribe` binary archive, with metadata and data stored under separate keys so
the session list can be populated without deserialising the full data). Each
format is distinguished purely by which keys are present in the
`UserPreferences::KeyValueMap`, tested newest-first in `get_session_format()`
since the current format also carries the 1.5-format key for backward
compatibility.

`create_restore_session()` reads only the metadata transcription — the
save time and the loaded/all file paths, via
`GPlatesScribe::TranscribeUtils::load_file_paths` — so the session list in the
GUI can be built cheaply; the actual state (layers, features, view settings)
is transcribed by `TranscribeSession` and only decoded when
`restore_session()` is later called. `save_session()` similarly delegates the
real transcription work to `TranscribeSession::save()`, additionally
recording every file path touched via a `TranscribeUtils::FilePath`
transcribe context so `get_file_paths()` can later report which files still
exist.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::InternalSession`](#gplatespresentationinternalsession) | class | [`Session`](Session.md) | — | 0 | An internal session of GPlates (saved to the user preferences store). |

## Members

### `GPlatesPresentation::InternalSession`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<InternalSession>` | public | Convenience typedefs for a shared pointer to a InternalSession. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const InternalSession>` | public | — |
| `has_valid_session_keys( const GPlatesAppLogic::UserPreferences::KeyValueMap &session_state)` | method | `bool` | public | Returns true if there are keys in session\_state that are recognised as session keys. |
| `create_restore_session( const GPlatesAppLogic::UserPreferences::KeyValueMap &session_state)` | method | `non_null_ptr_type` | public | Create a InternalSession object, from the specified session state, that can be used to restore a session. |
| `save_session()` | method | `non_null_ptr_type` | public | Saves the current session and returns it in a InternalSession object. |
| `restore_session()` | method | `void` | public | Restores the session state, contained within, to GPlates. |
| `get_file_paths( QStringList &existing_file_paths, QStringList &missing_file_paths)` | method | `void` | public | Returns unique sorted lists of all (absolute) file paths of transcribed files that currently exist and are currently missing. |
| `set_remapped_file_paths( boost::optional< QMap<QString/*missing*/, QString/*existing*/> > file_path_remapping)` | method | `void` | public | Specify whether to remap missing file paths to existing file paths. |
| `SessionFormat` | enum | `None` | private | An enumeration that determines what format a session was saved in. |
| `CURRENT_FORMAT_SESSION_METADATA_KEY` | field | `QString` | private | Session state key for session 'metadata'. |
| `CURRENT_FORMAT_SESSION_DATA_KEY` | field | `QString` | private | Session state key for session 'data'. |
| `GPLATES_1_5_FORMAT_SESSION_STATE_KEY` | field | `QString` | private | Session state key for GPlates 1.5 session state. |
| `d_session_key_value_map` | field | `GPlatesAppLogic::UserPreferences::KeyValueMap` | private | The entire session state including all key/value pairs stored in the session state map. |
| `d_all_file_paths` | field | `QStringList` | private | A unique sorted list of all transcribed filenames (transcribed via the TranscribeUtils::FilePath API). |
| `d_file_path_remapping` | field | `boost::optional< QMap<QString/*missing*/, QString/*existing*/> >` | private | Whether to remap missing file paths to existing file paths. |
| `get_session_format( const GPlatesAppLogic::UserPreferences::KeyValueMap &session_state)` | method | `SessionFormat` | private | Determines the session format from the session state (key/value map). |
| `InternalSession( const GPlatesAppLogic::UserPreferences::KeyValueMap &session_key_value_map_, const QDateTime &time_, const QStringList &filenames_, const QStringList &all_file_paths_)` | constructor | `None` | private | Construct a new InternalSession object. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `CURRENT_FORMAT_SESSION_METADATA_KEY` | variable | `QString` | — |
| `CURRENT_FORMAT_SESSION_DATA_KEY` | variable | `QString` | — |
| `GPLATES_1_5_FORMAT_SESSION_STATE_KEY` | variable | `QString` | — |
| `GPLATES_PRESENTATION_INTERNALSESSION_H` | macro | `None` | — |

## Notes

`has_valid_session_keys()` must return true before `create_restore_session()`
is called; the latter asserts (throwing `TranscribeSession::UnsupportedVersion`)
if the format is unrecognised, and again if required metadata fields fail to
load or the metadata transcription is left incomplete. `get_file_paths()`
reports paths from `d_all_file_paths`, which for `GPLATES_1_5_FORMAT` sessions
falls back to the loaded-files list because that older format never recorded
the full set of touched files. `set_remapped_file_paths()` only stores the
remapping for later use by `restore_session()`; it does not itself touch any
files. `restore_session()` on a `GPLATES_1_4_OR_BEFORE_FORMAT` session bypasses
`Scribe` entirely and goes through `DeprecatedSessionRestore` instead.

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/SessionManagement](SessionManagement.md) | presentation | 66 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 3 |
| [gui/SessionMenu](../gui/SessionMenu.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/InternalSession.h
python scripts/gpq.py def GPlatesPresentation::InternalSession --body
python scripts/gpq.py uses InternalSession --kind class
python scripts/gpq.py hier InternalSession
```

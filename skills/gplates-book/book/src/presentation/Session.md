# Session

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 1236 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/Session.h` | C++ | 161 |
| `src/presentation/Session.cc` | C++ | 174 |

## Overview

`GPlatesPresentation::Session` is the abstract base for a saved GPlates session: a timestamp, the set of loaded file paths, and a textual description for session/recent-file menus. It is deliberately thin — it does not itself know how to restore anything; `restore_session()` is pure virtual, left to the two concrete subclasses, `InternalSession` (session state kept as a text archive in `UserPreferences`) and `ProjectSession` (a binary archive in a standalone project file). `SessionManagement` and the GUI menus that list past sessions work in terms of this base class so they do not need to distinguish an ordinary auto-saved session from a project.

The free functions `common_base_dir()` and `strip_empty_entries()` are description-building helpers: they derive a short, human-readable summary of a file set (e.g. a common directory) for `get_description()`, and guard against blank filenames that could otherwise corrupt a saved session's file list.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::Session`](#gplatespresentationsession) | class | [`GPlatesUtils::ReferenceCount<Session>`](../utils/ReferenceCount.md) | — | 2 | Base class encapsulates a session of GPlates including files loaded and the layers state. |

## Members

### `GPlatesPresentation::Session`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<Session>` | public | Convenience typedefs for a shared pointer to a Session. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const Session>` | public | — |
| `~Session()` | destructor | `None` | public | — |
| `get_description()` | method | `QString` | public | Textual description suitable for menus, e.g. "5 files on Mon Nov 1, 5:57 PM" |
| `get_time` | field | `QDateTime` | public | The time when the session was saved; usually the time GPlates last quit while these files were active. |
| `get_loaded_files()` | method | `QList<QString>` | public | Which files were active when the session was saved. |
| `is_empty()` | method | `bool` | public | It is possible to have an 'empty' session without any files. |
| `has_same_loaded_files_as( const Session &other)` | method | `bool` | public | Comparing two Session together should ignore the datestamp and focus on whether the list of files match; this is so that GPlates can be a bit smarter about how the Recent Sessions menu operates w.r.t. people loading/saving prior sessions. |
| `restore_session()` | method | `void` | public | Restores the session state, contained within, to GPlates. |
| `Session( const QDateTime &time_, const QStringList &files_)` | constructor | `None` | protected | Construct a new Session object to represent a specific collection of files that were loaded in GPlates at some time. files\_ is a collection of absolute path names, obtained via QFileInfo::absoluteFilePath(). |
| `d_time` | field | `QDateTime` | private | The time when the session was saved; usually the time GPlates last quit while these files were active. |
| `d_loaded_files` | field | `QSet<QString>` | private | Which files were active when the session was saved. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `common_base_dir( const QString &a, const QString &b)` | function | `QString` | — |
| `common_base_dir( const QSet<QString> &filenames)` | function | `QString` | — |
| `strip_empty_entries( QStringList list)` | function | `QSet<QString>` | Removes any "" entries from a QStringList, to avoid potential bugs with incorrectly saved Sessions. |
| `GPLATES_PRESENTATION_SESSION_H` | macro | `None` | — |

## Notes

- `has_same_loaded_files_as()` deliberately ignores the timestamp and compares only the loaded-file set, so that the Recent Sessions menu can recognise "the same session reloaded" rather than treating every save as distinct.
- The constructor is `protected`; instances are only ever created through the concrete `InternalSession`/`ProjectSession` subclasses, reached via `GPlatesUtils::ReferenceCount`-managed `non_null_ptr_type`s.

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/InternalSession](InternalSession.md) | presentation | 5 |
| [presentation/SessionManagement](SessionManagement.md) | presentation | 4 |
| [presentation/ProjectSession](ProjectSession.md) | presentation | 3 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 1 |
| [gui/SessionMenu](../gui/SessionMenu.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/Session.h
python scripts/gpq.py def GPlatesPresentation::Session --body
python scripts/gpq.py uses Session --kind class
python scripts/gpq.py hier Session
```

# TranscribeUtils

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 495 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeUtils.h` | C++ | 693 |
| `src/scribe/TranscribeUtils.cc` | C++ | 499 |

## Overview

This unit collects the utilities `Scribe` clients need for two recurring, non-generic problems: transcribing file paths portably, and bridging pointer-representation changes across archive versions. `FilePath` is the wrapper actually written to archives: it splits a path on `/` and transcribes each path segment as a separate string, which lets the underlying transcription format share common directory prefixes across many saved paths and keeps archives smaller. Its companion `TranscribeContext<TranscribeUtils::FilePath>` specialisation is how a caller (`presentation::ProjectSession` and related session code, per the "Used by" table) opts into two loading-time behaviours: rewriting each loaded path to be relative to wherever the project file was actually opened from — via `convert_file_path_relative_to_project()`, which walks the saved and loaded project directories to find their common ancestor and re-roots the path underneath the new project location — and remapping known-missing files to files the user has since relocated. `convert_file_path()` and `is_resource_file_path_or_empty_path()` handle the lower-level cross-platform concern: adding or stripping a Windows drive letter or UNC share name so a path saved on one operating system still resolves sensibly when the project is reopened on another, while leaving Qt resource paths (`:/...`) and empty paths untouched. `save_file_path`/`load_file_path` and their sequence-oriented overloads are the convenience entry points most callers actually use instead of touching `FilePath` directly.

The pointer-bridging half of the header — `load_smart_pointer_from_raw_pointer()` and `load_raw_pointer_and_object_from_smart_pointer()` — exists purely for archive backward compatibility: because `Scribe` transcribes raw pointers and smart pointers with the same wire representation, these functions let current code load an old archive that recorded a member using the other pointer style than the one the class now uses, converting between an owned/tracked pointer and a raw pointer plus its pointed-to object as needed.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::TranscribeUtils::FilePath`](#gplatesscribetranscribeutilsfilepath) | class | — | — | 0 | Transcribing a FilePath created from a file path QString containing '/' directory separators results in smaller archives/transcriptions since each path between these separators is transcribed as a separate string - and this promotes ... |
| [`GPlatesScribe::TranscribeContext<TranscribeUtils::FilePath>`](#gplatesscribetranscribecontexttranscribeutilsfilepath) | class | — | `<>` | 0 | Used to record transcribed FilePath objects. |

## Members

### `GPlatesScribe::TranscribeUtils::FilePath`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FilePath( const QString file_path)` | constructor | `None` | public | Conversion from a QString file path (containing '/' directory separators). |
| `FilePath()` | constructor | `None` | public | — |
| `set_file_path( const QString &file_path)` | method | `void` | public | Set the QString file path (containing '/' directory separators). |
| `get_file_path( bool convert = true)` | method | `QString` | public | Access QString file path (contains '/' directory separators). |
| `d_split_paths` | field | `QStringList` | private | — |
| `transcribe( Scribe &scribe, bool transcribed_construct_data)` | method | `TranscribeResult` | private | — |

### `GPlatesScribe::TranscribeContext<TranscribeUtils::FilePath>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `set_load_relative_file_paths( const std::pair< QString/*project_file_path_when_saved*/, QString/*project_file_path_when_loaded*/> &load_relative_file_paths)` | method | `void` | public | In the loading path, convert transcribed file paths to be relative to the loaded project file rather than relative to the location of the project file when it was saved. |
| `set_load_file_path_remapping( boost::optional< QMap<QString/*missing*/, QString/*existing*/> > load_file_path_remapping)` | method | `void` | public | In the loading path, rename any files in the specified mapping. |
| `get_file_paths( bool convert = true, bool exclude_resource_and_empty_file_paths = true)` | method | `QStringList` | public | Returns a unique sorted list of all file paths (FilePath) transcribed. |
| `d_file_paths` | field | `QStringList` | private | — |
| `d_load_relative_file_paths` | field | `boost::optional< std::pair< QString/*project_file_path_when_saved*/, QString/*project_file_path_when_loaded*/> >` | private | — |
| `d_load_file_path_remapping` | field | `boost::optional< QMap<QString/*missing*/, QString/*existing*/> >` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `WINDOWS_DRIVE_LETTER_REGEXP` | variable | `QRegExp` | Regular expression for a Windows drive letter (eg, "C:/"). |
| `WINDOWS_SHARE_NAME_REGEXP` | variable | `QRegExp` | Regular expression for a Windows share name (eg, "//sharename/"). |
| `get_dir_path( QString file_path, boost::optional<QString &> file_name = boost::none)` | function | `QStringList` | Returns the directory path of the specified file path. |
| `GPLATES_SCRIBE_TRANSCRIBEUTILS_H` | macro | `None` | — |
| `save_file_path( Scribe &scribe, const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here const QString &file_path, const ObjectTag &file_path_tag)` | function | `void` | Convenience function to save a file path using FilePath. |
| `load_file_path( Scribe &scribe, const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here const ObjectTag &file_path_tag, bool convert = true)` | function | `boost::optional<QString>` | Convenience function to load a file path using FilePath. |
| `save_file_paths( Scribe &scribe, const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here const QStringList &file_paths, const ObjectTag &file_paths_tag)` | function | `void` | Convenience function to save a sequence of file paths (sequence of QString) using FilePath. |
| `save_file_paths( Scribe &scribe, const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here FilePathsIter file_paths_begin, FilePathsIter file_paths_end, const ObjectTag &file_paths_tag)` | function | `void` | Same as other overload of save\_file\_paths, except can be used with any container with 'begin' and 'end' iterators (eg, std::vector). |
| `load_file_paths( Scribe &scribe, const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here const ObjectTag &file_paths_tag, bool convert = true)` | function | `boost::optional<QStringList>` | Convenience function to load a sequence of file paths (sequence of QString) using FilePath. |
| `convert_file_path( const QString &file_path)` | function | `QString` | Convert a file path to a path appropriate for the runtime operating system. |
| `convert_file_path_relative_to_project( const QString &file_path_when_saved, const QString &project_file_path_when_saved, const QString &project_file_path_when_loaded)` | function | `QString` | Convert a file path (transcribed into the project file) to be relative to the location of the project file being loaded (instead of the location the project file was saved to). |
| `is_resource_file_path_or_empty_path( const QString &file_path)` | function | `bool` | Returns true if file path is a resource file or empty path. |
| `load_smart_pointer_from_raw_pointer( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here Scribe &scribe, SmartPtrType &smart_ptr, const ObjectTag &raw_ptr_tag, bool track)` | function | `Scribe::Bool` | Load a saved object raw pointer into a smart pointer. |
| `load_smart_pointer_from_raw_pointer( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here Scribe &scribe, const ObjectTag &raw_ptr_tag, bool track)` | function | `LoadRef<SmartPtrType>` | An overload of load\_smart\_pointer\_from\_raw\_pointer that returns a LoadRef\<\>. |
| `load_raw_pointer_and_object_from_smart_pointer( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here Scribe &scribe, ObjectType &object, ObjectRawPtrType &object_raw_ptr, const ObjectTag &smart_ptr_tag, bool track)` | function | `Scribe::Bool` | Load a saved smart pointer into a raw pointer and its pointed-to object. |
| `load_raw_pointer_and_object_from_smart_pointer( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here Scribe &scribe, ObjectRawPtrType &object_raw_ptr, const ObjectTag &smart_ptr_tag, bool track)` | function | `LoadRef<ObjectType>` | An overload of load\_raw\_pointer\_and\_object\_from\_smart\_pointer that returns a LoadRef\<\> for the object pointed to by the raw pointer. |
| `save_file_paths( Scribe &scribe, const GPlatesUtils::CallStack::Trace &transcribe_source, FilePathsIter file_paths_begin, FilePathsIter file_paths_end, const ObjectTag &file_paths_tag)` | function | `void` | — |
| `load_smart_pointer_from_raw_pointer( const GPlatesUtils::CallStack::Trace &transcribe_source, Scribe &scribe, SmartPtrType &smart_ptr, const ObjectTag &raw_ptr_tag, bool track)` | function | `Scribe::Bool` | — |
| `load_smart_pointer_from_raw_pointer( const GPlatesUtils::CallStack::Trace &transcribe_source, Scribe &scribe, const ObjectTag &raw_ptr_tag, bool track)` | function | `LoadRef<SmartPtrType>` | — |
| `load_raw_pointer_and_object_from_smart_pointer( const GPlatesUtils::CallStack::Trace &transcribe_source, Scribe &scribe, ObjectType &object, ObjectRawPtrType &object_raw_ptr, const ObjectTag &smart_ptr_tag, bool track)` | function | `Scribe::Bool` | — |
| `load_raw_pointer_and_object_from_smart_pointer( const GPlatesUtils::CallStack::Trace &transcribe_source, Scribe &scribe, ObjectRawPtrType &object_raw_ptr, const ObjectTag &smart_ptr_tag, bool track)` | function | `LoadRef<ObjectType>` | — |

## Notes

- `FilePath::transcribe()` deliberately keeps its wire format as a raw indexed sequence of strings, not the `TranscribeSequenceProtocol` sequence tag, purely to stay bit-compatible with archives written before that protocol was standardised; do not "clean it up" to use the shared sequence helpers without breaking old project files.
- `get_file_paths()` on `TranscribeContext<FilePath>` deduplicates and sorts, so its order has no relationship to the order paths were transcribed.
- `convert_file_path_relative_to_project()` falls back to returning the (platform-converted) originally-saved path unchanged whenever no relative path can be formed — e.g. the saved file and saved project were on different drives, or on different drives/share names when reopened — so callers must not assume the result is actually relative to the new project location.
- `load_raw_pointer_and_object_from_smart_pointer()` requires the loaded archive's dynamic type to exactly match `ObjectType`; a different derived type causes the load to fail rather than slice or convert.

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/ProjectSession](../presentation/ProjectSession.md) | presentation | 19 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 17 |
| [presentation/InternalSession](../presentation/InternalSession.md) | presentation | 13 |
| [scribe/ScribeExportExternal](ScribeExportExternal.md) | scribe | 1 |
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/TranscribeUtils.h
python scripts/gpq.py def GPlatesScribe::TranscribeContext<TranscribeUtils::FilePath> --body
python scripts/gpq.py uses TranscribeContext<TranscribeUtils::FilePath> --kind class
python scripts/gpq.py hier TranscribeContext<TranscribeUtils::FilePath>
```

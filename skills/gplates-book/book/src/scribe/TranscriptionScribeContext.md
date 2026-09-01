# TranscriptionScribeContext

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 91 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscriptionScribeContext.h` | C++ | 467 |
| `src/scribe/TranscriptionScribeContext.cc` | C++ | 1500 |

## Overview

`TranscriptionScribeContext` is the layer between `Scribe`, which drives the object graph traversal that application code sees, and `Transcription`, the in-memory tree of tagged composite and primitive objects that is actually the archive. `Scribe` never touches a `Transcription::CompositeObject` directly; it calls `push_transcribed_object()`/`pop_transcribed_object()` to move into and back out of the object currently being transcribed, and `transcribe_object_id()`/`transcribe()` to read or write the child identified by an `ObjectTag` relative to whatever object is on top of that stack. `push_transcribed_object()` is called with a freshly allocated id (via `allocate_save_object_id()`) when saving, or with an id already present in the loaded `Transcription` when loading, and the constructor seeds the stack with an emulated `ROOT_OBJECT_ID` composite purely so that top-level `transcribe()` calls have somewhere to record their tag.

Internally, an `ObjectTag` is a sequence of sections — plain tag/version pairs, array indices, or an array's size — and `is_in_transcription()` / `transcribe_object_id()` walk those sections one at a time, descending into a fresh `CompositeObject` after each non-final section and resolving the actual child object id only at the final section. Each section's tag name and version are converted to a `Transcription::object_key_type` via `Transcription::get_object_key()` (loading) or `get_or_create_object_key()` (saving); a lookup failure at any section — an unknown key, or a key with zero or more than one matching child — simply returns `false`/`boost::none` rather than throwing, which is how `Scribe` detects `TRANSCRIBE_INCOMPATIBLE` conditions such as tags that don't exist in an older or newer archive. The primitive `transcribe()` overloads are the leaf case: they write a value directly into whatever composite/tag/array slot the id stack currently identifies, with 64-bit integers narrowed to `long`/`unsigned long` (and vice versa) via `boost::numeric_cast`, throwing `Exceptions::ScribeUserError` if a value doesn't fit — the only reason this indirection exists is that a `long` is 32-bit on Windows but 64-bit on Mac/Linux.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::TranscriptionScribeContext`](#gplatesscribetranscriptionscribecontext) | class | — | — | 0 | A TranscriptionScribeContext is used by class Scribe to transcribe the object network to/from a Transcription. |

## Members

### `GPlatesScribe::TranscriptionScribeContext`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `object_id_type` | typedef | `Transcription::object_id_type` | public | Typedef for an integer identifier for a transcribed object. |
| `NULL_POINTER_OBJECT_ID` | field | `object_id_type` | public | A value of 0 is used to identify NULL pointers. |
| `ROOT_OBJECT_ID` | field | `object_id_type` | public | The object id of the root object used to store root-level transcribe calls. |
| `TranscriptionScribeContext( const Transcription::non_null_ptr_type &transcription, bool is_saving_)` | constructor | `None` | public | Transcribe using the specified transcription. |
| `is_saving()` | method | `bool` | public | Is saving state (that can be written to an archive). |
| `is_loading()` | method | `bool` | public | Is loading state (that was read from an archive). |
| `allocate_save_object_id()` | method | `object_id_type` | public | Allocate the next available object id. |
| `is_in_transcription( const ObjectTag &object_tag)` | method | `boost::optional<object_id_type>` | public | Determines whether the specified object tag exists in the transcription (transcription is either being written to, on save path, or read from, on load path). |
| `transcribe_object_id( object_id_type &object_id, const ObjectTag &object_tag)` | method | `bool` | public | Transcribe the (child) object ID associated with the object tag that is relative to the currently pushed transcribed (parent) object (see push\_transcribed\_object). |
| `push_transcribed_object( object_id_type object_id)` | method | `void` | public | All subsequent transcribe and transcribe\_object\_id calls will now be relative to the specified object (object\_id). |
| `pop_transcribed_object()` | method | `void` | public | — |
| `transcribe( std::string &object)` | method | `bool` | public | Transcribe a std::string primitive. |
| `transcribe( bool &object)` | method | `bool` | public | Transcribe integral and floating-point primitives. |
| `transcribe( char &object)` | method | `bool` | public | Apparently 'char', 'signed char' and 'unsigned char' are three distinct types (unlike integer types). |
| `transcribe( signed char &object)` | method | `bool` | public | — |
| `transcribe( unsigned char &object)` | method | `bool` | public | — |
| `transcribe( short &object)` | method | `bool` | public | — |
| `transcribe( unsigned short &object)` | method | `bool` | public | — |
| `transcribe( int &object)` | method | `bool` | public | — |
| `transcribe( unsigned int &object)` | method | `bool` | public | — |
| `transcribe( long &object)` | method | `bool` | public | — |
| `transcribe( unsigned long &object)` | method | `bool` | public | — |
| `transcribe( ObjectType &object)` | method | `typename boost::enable_if< boost::mpl::and_< boost::is_same<ObjectType, boost::int64_t>, boost::mpl::not_<boost::is_same<ObjectType, long> > >, bool>::type` | public | — |
| `transcribe( float &object)` | method | `bool` | public | — |
| `transcribe( double &object)` | method | `bool` | public | — |
| `transcribe( long double &object)` | method | `bool` | public | — |
| `TranscribedObject` | struct | `None` | private | Used to keep track of the object currently being transcribed. |
| `transcribed_object_stack_type` | typedef | `std::stack<TranscribedObject>` | private | — |
| `d_is_saving` | field | `bool` | private | Whether transcription was read from an archive or will be written to one. |
| `d_next_save_object_id` | field | `unsigned int` | private | The next available object id for the \*save\* path. |
| `d_transcription` | field | `Transcription::non_null_ptr_type` | private | — |
| `d_transcribed_object_stack` | field | `transcribed_object_stack_type` | private | — |
| `save_tag_section( const std::string &tag_name, unsigned int tag_version, Transcription::CompositeObject *&section_composite_object, boost::optional<object_id_type &> object_id)` | method | `void` | private | — |
| `load_tag_section( const std::string &tag_name, unsigned int tag_version, Transcription::CompositeObject *&section_composite_object, boost::optional<object_id_type &> object_id)` | method | `bool` | private | — |
| `save_array_index_section( const std::string &array_item_tag_name, unsigned int array_item_tag_version, unsigned int array_index, Transcription::CompositeObject *&section_composite_object, boost::optional<object_id_type &> object_id)` | method | `void` | private | — |
| `load_array_index_section( const std::string &array_item_tag_name, unsigned int array_item_tag_version, unsigned int array_index, Transcription::CompositeObject *&section_composite_object, boost::optional<object_id_type &> object_id)` | method | `bool` | private | — |
| `save_array_size_section( const std::string &array_size_tag_name, unsigned int array_size_tag_version, Transcription::CompositeObject *&section_composite_object, boost::optional<object_id_type &> object_id)` | method | `void` | private | — |
| `load_array_size_section( const std::string &array_size_tag_name, unsigned int array_size_tag_version, Transcription::CompositeObject *&section_composite_object, boost::optional<object_id_type &> object_id)` | method | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_TRANSCRIPTIONSCRIBECONTEXT_H` | macro | `None` | — |

## Notes

- `push_transcribed_object()`/`pop_transcribed_object()` must be balanced by the caller (`Scribe`); `pop_transcribed_object()` asserts (`Exceptions::ScribeLibraryError`) that the emulated root object is never popped off the stack.
- On save, popping an object that never had anything transcribed into it (e.g. an empty base class) still creates an empty composite object in the `Transcription`, so that the parent's reference to it resolves rather than dangling.
- `object_id_type` value `0` is reserved for null pointers and `1` for the emulated root object; real transcribed objects are allocated starting at `2` on the save path.
- A missing or ambiguous object key (absent tag, or more than one child sharing a key — which should already have been prevented when the transcription was written) is treated as ordinary transcription failure, not a thrown exception; only structurally-impossible states (e.g. failed invariants about the transcribed-object stack or tag-section shape) raise `Exceptions::ScribeLibraryError`.
- 64-bit integer transcription throws `Exceptions::ScribeUserError` if a value on the save path does not fit in a `long`/`unsigned long`, which effectively caps transcribable integers at 32 bits on platforms (Windows) where `long` is 32-bit.

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/Scribe](Scribe.md) | scribe | 5 |
| [scribe/ScribeInternalAccess](ScribeInternalAccess.md) | scribe | 2 |
| [scribe/ScribeInternalUtils](ScribeInternalUtils.md) | scribe | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/TranscriptionScribeContext.h
python scripts/gpq.py def GPlatesScribe::TranscriptionScribeContext --body
python scripts/gpq.py uses TranscriptionScribeContext --kind class
python scripts/gpq.py hier TranscriptionScribeContext
```

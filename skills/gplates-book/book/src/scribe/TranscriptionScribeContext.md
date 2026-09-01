# TranscriptionScribeContext

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 91 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscriptionScribeContext.h` | C++ | 467 |
| `src/scribe/TranscriptionScribeContext.cc` | C++ | 1500 |

## Overview

[[[PROSE overview unit=scribe/TranscriptionScribeContext tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=scribe/TranscriptionScribeContext tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

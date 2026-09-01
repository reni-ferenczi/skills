# Transcription

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 34 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/Transcription.h` | C++ | 590 |
| `src/scribe/Transcription.cc` | C++ | 1082 |

## Overview

[[[PROSE overview unit=scribe/Transcription tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::Transcription`](#gplatesscribetranscription) | class | [`GPlatesUtils::ReferenceCount<Transcription>`](../utils/ReferenceCount.md)<br>`boost::equality_comparable<Transcription>` | — | 0 | The transcribed state of the object network in its most essential and accessible form. |

## Members

### `GPlatesScribe::Transcription`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<Transcription>` | public | Convenience typedefs for a shared pointer to a Transcription. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const Transcription>` | public | — |
| `object_id_type` | typedef | `unsigned int` | public | Typedef for an integer identifier for a transcribed object. |
| `object_tag_version_type` | typedef | `unsigned int` | public | Typedef for an integer object tag version. |
| `object_tag_name_type` | typedef | `std::string` | public | Typedef for a unique object tag name (string). |
| `object_tag_name_id_type` | typedef | `unsigned int` | public | Typedef for integer object tag name identifier that indexes into the sequence returned by get\_object\_tag\_name. |
| `object_key_type` | typedef | `std::pair<object_tag_name_id_type, object_tag_version_type>` | public | Typedef for an object key used to lookup a child object id in CompositeObject. |
| `CompositeObject` | class | `None` | public | A composite object contains child object ids indexed by object\_key\_type (object tag name/version). |
| `ObjectType` | enum | `None` | public | The types of transcribed objects. |
| `int32_type` | typedef | `boost::int32_t` | public | Typedefs for signed/unsigned 32-bit integer types. |
| `uint32_type` | typedef | `boost::uint32_t` | public | — |
| `create()` | method | `non_null_ptr_type` | public | Creates an empty transcription. |
| `get_num_object_ids()` | method | `object_id_type` | public | Returns the number of object ids (including unused ids). |
| `get_object_type( object_id_type object_id)` | method | `ObjectType` | public | Returns the type of the transcribed object with the specified object id. object\_id must be less than get\_num\_object\_ids. |
| `get_signed_integer( object_id_type object_id)` | method | `int32_type` | public | — |
| `add_signed_integer( object_id_type object_id, int32_type value)` | method | `void` | public | — |
| `set_signed_integer( object_id_type object_id, int32_type value)` | method | `void` | public | Changes an \*existing\* object's value. |
| `get_unsigned_integer( object_id_type object_id)` | method | `uint32_type` | public | — |
| `add_unsigned_integer( object_id_type object_id, uint32_type value)` | method | `void` | public | — |
| `set_unsigned_integer( object_id_type object_id, uint32_type value)` | method | `void` | public | Changes an \*existing\* object's value. |
| `get_float( object_id_type object_id)` | method | `float` | public | — |
| `add_float( object_id_type object_id, float value)` | method | `void` | public | — |
| `get_double( object_id_type object_id)` | method | `double` | public | — |
| `add_double( object_id_type object_id, const double &value)` | method | `void` | public | — |
| `get_string( object_id_type object_id)` | method | `std::string` | public | — |
| `add_string( object_id_type object_id, const std::string &value)` | method | `void` | public | — |
| `get_composite_object` | field | `CompositeObject` | public | — |
| `add_composite_object` | field | `CompositeObject` | public | — |
| `get_num_object_tags()` | method | `unsigned int` | public | Returns the number of unique object tags. |
| `get_object_tag_name` | field | `object_tag_name_type` | public | Returns the unique object tag name identified by object\_tag\_name\_id. |
| `add_object_tag_name( const object_tag_name_type &object_tag_name)` | method | `object_tag_name_id_type` | public | Adds a unique object tag name. |
| `get_num_unique_string_objects()` | method | `unsigned int` | public | Returns the number of unique string objects. |
| `get_unique_string_object` | field | `std::string` | public | Returns the unique string object identified by a unique string index. |
| `add_unique_string_object( const std::string &unique_string_object)` | method | `unsigned int` | public | Adds a unique string object. |
| `get_string_object( object_id_type object_id)` | method | `unsigned int` | public | Returns the string object identified by object\_id. |
| `add_string_object( object_id_type object_id, unsigned int unique_string_index)` | method | `void` | public | Adds a string object. |
| `get_object_key( const object_tag_name_type &object_tag_name, object_tag_version_type object_tag_version)` | method | `boost::optional<object_key_type>` | public | Returns the specified object tag name/version as an object key. |
| `get_or_create_object_key( const object_tag_name_type &object_tag_name, object_tag_version_type object_tag_version)` | method | `object_key_type` | public | Returns the specified object tag name/version as an object key if it already exists, or creates a new object key if needed. |
| `is_complete( object_id_type null_pointer_object_id, bool emit_warnings = true)` | method | `bool` | public | Returns true if the transcription is complete. |
| `operator==( const Transcription &other)` | operator | `bool` | public | Equality comparison operator ('!=' provided by boost::equality\_comparable). |
| `object_tag_name_id_map_type` | typedef | `std::map<object_tag_name_type, object_tag_name_id_type>` | private | Typedef for mapping unique object tag names to tag name ids (indices into object\_tag\_seq\_type). |
| `string_object_index_map_type` | typedef | `std::map<std::string, unsigned int>` | private | Typedef for mapping unique string objects to indices (into string\_object\_seq\_type). |
| `ObjectLocation` | struct | `None` | private | Info on where to find a primitive/composite object. |
| `object_location_seq_type` | typedef | `std::vector<ObjectLocation>` | private | — |
| `composite_object_pool_type` | typedef | `boost::object_pool<CompositeObject>` | private | Typedef for a pool allocator of CompositeObject. |
| `UNUSED_OBJECT_ID` | field | `object_id_type` | private | Used to identify holes in arrays (eg, when a child is added to a composite object at index 2 leaving holes at indices 0 and 1 that client will later need to fill). |
| `d_object_tag_names` | field | `std::vector<object_tag_name_type>` | private | Keep track of unique object tag names (strings) and map them to integer tag name ids. |
| `d_object_tag_name_id_map` | field | `object_tag_name_id_map_type` | private | — |
| `d_object_locations` | field | `object_location_seq_type` | private | Info on where to find the primitive/composite objects. |
| `d_signed_integer_objects` | field | `std::vector<int32_type>` | private | Primitive integral/float objects. |
| `d_unsigned_integer_objects` | field | `std::vector<uint32_type>` | private | — |
| `d_float_objects` | field | `std::vector<float>` | private | — |
| `d_double_objects` | field | `std::vector<double>` | private | — |
| `d_unique_string_objects` | field | `std::vector<std::string>` | private | Primitive string objects. |
| `d_string_objects` | field | `std::vector<unsigned int>` | private | — |
| `d_string_object_index_map` | field | `string_object_index_map_type` | private | — |
| `d_composite_object_pool` | field | `composite_object_pool_type` | private | Composite objects. |
| `d_composite_objects` | field | `std::vector<CompositeObject *>` | private | — |
| `Transcription()` | constructor | `None` | private | — |
| `get_object_location` | field | `ObjectLocation` | private | — |
| `add_object_location` | field | `ObjectLocation` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `are_almost_equal( const double value1, const double value2, const double max_relative_error)` | function | `bool` | Returns true if two floating-point numbers are almost equal. |
| `UNUSED_OBJECT_ID` | variable | `GPlatesScribe::Transcription::object_id_type` | Using the maximum integer value since it is too high to ever get used by client. |
| `operator==( const Transcription &other)` | operator | `bool` | — |
| `GPLATES_SCRIBE_TRANSCRIPTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=scribe/Transcription tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/Scribe](Scribe.md) | scribe | 322 |
| [scribe/TranscriptionScribeContext](TranscriptionScribeContext.md) | scribe | 296 |
| [scribe/ScribeTextArchiveWriter](ScribeTextArchiveWriter.md) | scribe | 67 |
| [scribe/ScribeBinaryArchiveWriter](ScribeBinaryArchiveWriter.md) | scribe | 57 |
| [scribe/ScribeXmlArchiveWriter](ScribeXmlArchiveWriter.md) | scribe | 50 |
| [scribe/ScribeTextArchiveReader](ScribeTextArchiveReader.md) | scribe | 44 |
| [scribe/ScribeAccess](ScribeAccess.md) | scribe | 39 |
| [scribe/ScribeInternalAccess](ScribeInternalAccess.md) | scribe | 39 |
| [scribe/ScribeXmlArchiveReader](ScribeXmlArchiveReader.md) | scribe | 30 |
| [scribe/ScribeBinaryArchiveReader](ScribeBinaryArchiveReader.md) | scribe | 29 |
| [scribe/ScribeSaveLoadConstructObject](ScribeSaveLoadConstructObject.md) | scribe | 22 |
| [scribe/ScribeInternalUtils](ScribeInternalUtils.md) | scribe | 21 |
| [scribe/TranscribeImpl](TranscribeImpl.md) | scribe | 21 |
| [utils/ObjectPool](../utils/ObjectPool.md) | utils | 18 |
| [scribe/TranscribeUtils](TranscribeUtils.md) | scribe | 16 |
| [scribe/ScribeLoadRefImpl](ScribeLoadRefImpl.md) | scribe | 15 |
| [presentation/ProjectSession](../presentation/ProjectSession.md) | presentation | 9 |
| [scribe/ScribeInternalUtilsImpl](ScribeInternalUtilsImpl.md) | scribe | 8 |
| [scribe/Transcribe](Transcribe.md) | scribe | 8 |
| [scribe/ScribeConstructObject](ScribeConstructObject.md) | scribe | 7 |

*... and 9 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/Transcription.h
python scripts/gpq.py def GPlatesScribe::Transcription --body
python scripts/gpq.py uses Transcription --kind class
python scripts/gpq.py hier Transcription
```

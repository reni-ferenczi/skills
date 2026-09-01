# Transcription

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 34 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/Transcription.h` | C++ | 590 |
| `src/scribe/Transcription.cc` | C++ | 1082 |

## Overview

A `Transcription` is the neutral middle of the serialisation pipeline: the transcribed state
of an object network, held in memory and addressable at random. It sits between two very
different consumers. `Scribe` writes and reads it through `TranscriptionScribeContext` while
walking a live object graph; the archive readers and writers stream it to and from a file,
where the representation is sequential and compressed. Keeping the two apart is what lets
the same session state be written as binary, text or XML without the transcribing code
knowing which, and what lets a project be loaded into a `Transcription` before any GPlates
object is built from it.

The model is deliberately small. Every transcribed object is an integer object id indexing
`d_object_locations`, and each entry says which kind it is — signed integer, unsigned
integer, float, double, string, composite, or `UNUSED` — and where in the corresponding
`std::vector` its value lives. So the whole graph reduces to five primitive pools plus a
pool of `CompositeObject`s. A `CompositeObject` is a node: it maps an `object_key_type`
(an interned tag-name id paired with a tag version) to one or more child object ids, and a
child id may in turn name a primitive or another composite. That "one or more" is how arrays
and sequences are represented — several children under a single key, indexed — and
`set_child()` deliberately tolerates being filled out of order, marking absent slots with
`UNUSED_OBJECT_ID` until they are set.

Two forms of interning keep the memory down, and both are exposed as separate APIs for
archive readers and writers. Tag names are stored once in `d_object_tag_names`, and every
composite refers to them by index. String values are stored once in
`d_unique_string_objects`, with a string object holding only the index — so an archive
writer emits the unique-string table and the indices, not the strings. A `CompositeObject`
goes further and packs its keys, child counts and child ids into a single flat
`std::vector<unsigned int>` (`d_encoding`), which is searched linearly; the class is a
compact encoding, not a map. `is_complete()` is the validator over all of this: it verifies
that every child id a composite references actually exists, that no slot was left as a
hole, and that all children under one key share a type — a `Scribe` load constructor refuses
a transcription that fails it.

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

**Object ids and types are write-once.** `add_object_location()` throws
`ScribeLibraryError` if the slot for an id is anything other than `UNUSED`, and every
accessor asserts that the requested kind matches the recorded one — asking for a signed
integer where a string was stored is an error, not a conversion. Only
`set_signed_integer()` and `set_unsigned_integer()` may overwrite, and only a value that
already exists. Likewise `CompositeObject::set_child()` refuses to overwrite a slot that has
already been filled, which is what turns a duplicated object tag into a diagnosable failure.

**`UNUSED_OBJECT_ID` is `numeric_limits<unsigned int>::max()`, not zero.** Zero is a
perfectly valid object id — `Scribe` reserves it for null pointers via
`TranscriptionScribeContext::NULL_POINTER_OBJECT_ID`, which is why `is_complete()` takes the
null-pointer id as a parameter rather than assuming one. Holes left by an out-of-order
`set_child()` are `UNUSED_OBJECT_ID`, and `has_valid_child()` is the way to test for them;
`get_child()` throws on one.

**`CompositeObject` search is linear.** `find_key()`, `get_num_keys()` and `get_key()` all
walk `d_encoding` from the start, so lookups and key enumeration are O(keys) and building a
composite with many distinct keys is quadratic. `set_child()` at a new index calls
`std::vector::insert` in the middle of the encoding, moving everything after it. This is a
size-over-speed trade; it is fine for the fan-out real objects have and would not be for a
composite with thousands of keys.

**Objects are pool-allocated and the class is noncopyable in practice.**
`CompositeObject`s come from a `boost::object_pool` and `d_composite_objects` holds raw
pointers into it, precisely to avoid copying their vectors during reallocation. The
`Transcription` is reference counted (`GPlatesUtils::ReferenceCount`) and always handed
around as `non_null_ptr_type`; its constructor is private, so `create()` is the only way in.

**`operator==` compares transcriptions, not object graphs.** It requires the same tag table,
the same unique-string table and the same object ids in the same order, so two runs only
compare equal if they transcribed the same state through the same code path — the intended
use is detecting whether session state changed between two saves. Floating-point values are
compared with a relative tolerance (1e-5 for `float`, 1e-12 for `double`, with explicit
infinity and NaN handling), so equality here is not bitwise.

**`is_complete()` is a diagnostic as well as a check.** With `emit_warnings` it names, via
`qWarning`, the parent object id, the tag and the child index for each dangling or
mistyped reference; that output is often the only usable evidence when a project or session
file fails to load.

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

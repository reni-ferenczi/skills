# Scribe

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 46 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/Scribe.h` | C++ | 5650 |
| `src/scribe/Scribe.cc` | C++ | 1778 |

## Overview

[[[PROSE overview unit=scribe/Scribe tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::Scribe::Bool::CheckDeleter`](#gplatesscribescribeboolcheckdeleter) | struct | — | — | 0 | — |
| [`GPlatesScribe::Scribe`](#gplatesscribescribe) | class | `boost::noncopyable` | — | 0 | Class scribe is the main access point for transcribing object graphs (networks of interconnected objects). |
| [`UnsupportedPointerType`](#unsupportedpointertype) | struct | `boost::mpl::eval_if< boost::is_pointer<ObjectType>, UnsupportedPointerType<typename boost::remove_pointer<ObjectType>::type, Dim+1>, boost::mpl::false_>` | `<typename ObjectType, int Dim=0>` | 0 | A metafunction used to catch (at compile-time) any transcribed objects that are pointers with a dimension greater than 'GPLATES\_SCRIBE\_MAX\_POINTER\_DIMENSION'. |
| [`UnsupportedPointerType<ObjectType, GPLATES_SCRIBE_MAX_POINTER_DIMENSION+1>`](#unsupportedpointertypeobjecttype-gplates_scribe_max_pointer_dimension1) | struct | `boost::mpl::true_` | `<typename ObjectType>` | 0 | — |
| [`StreamPrimitiveTag`](#streamprimitivetag) | struct | — | — | 0 | — |
| [`StreamTranscribeTag`](#streamtranscribetag) | struct | — | — | 0 | — |
| [`shared_ptr_map_type`](#shared_ptr_map_type) | typedef | — | — | 0 | Typedef for a map of shared pointers searched by the pointed-to object address. |

## Members

### `GPlatesScribe::Scribe::Bool::CheckDeleter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CheckDeleter( const GPlatesUtils::CallStack::Trace &transcribe_source_, bool require_check_)` | method | `None` | public | — |
| `operator()( bool *bool_ptr)` | operator | `void` | public | — |
| `transcribe_source` | field | `GPlatesUtils::CallStack::Trace` | public | — |
| `require_check` | field | `bool` | public | — |
| `has_been_checked` | field | `bool` | public | — |

### `GPlatesScribe::Scribe`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Scribe()` | constructor | `None` | public | Creates a Scribe to \*save\* to a transcription. |
| `Scribe( const Transcription::non_null_ptr_type &transcription)` | constructor | `None` | public | Creates a Scribe to \*load\* from the specified transcription. |
| `is_saving()` | method | `bool` | public | Is the scribe saving objects to an archive. |
| `is_loading()` | method | `bool` | public | Is the scribe loading objects from an archive. |
| `Bool` | class | `None` | public | Boolean result for transcribe methods. |
| `transcribe( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here ObjectType &object, const ObjectTag &object_tag, unsigned int options = 0)` | method | `Bool` | public | } container.append(a); } ...which will work fine if no other objects/pointers reference 'container's items (if they do then they won't be able to link up with it since cannot find untracked items). |
| `transcribe_base( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here DerivedType &derived_object, const ObjectTag &base_object_tag)` | method | `Bool` | public | return scribe.get\_transcribe\_result(); } return GPlatesScribe::TRANSCRIBE\_SUCCESS; } }; class B : public A { public: int b; virtual void do(); private: //! |
| `transcribe_base( const GPlatesUtils::CallStack::Trace &transcribe_source/* Use 'TRANSCRIBE_SOURCE' here */)` | method | `Bool` | public | public: int b; virtual void do(); private: //! |
| `save( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here const ObjectType &object, const ObjectTag &object_tag, unsigned int options = 0)` | method | `void` | public | Saves the specified object to the archive. |
| `load( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here const ObjectTag &object_tag, unsigned int options = 0)` | method | `LoadRef<ObjectType>` | public | if (scribe.is\_saving()) { scribe.save(TRANSCRIBE\_SOURCE, a-\>d\_x, "x", GPlatesScribe::TRACK); } else // loading { GPlatesScribe::LoadRef\<X\> x = scribe.load\<X\>(TRANSCRIBE\_SOURCE, "x", GPlatesScribe::TRACK); if (!x.is\_valid()) { return ... |
| `save_reference( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here ObjectType &object_reference, const ObjectTag &object_tag)` | method | `void` | public | If the reference is a data member of a class then you'll likely need to specialise or overload 'transcribe\_construct\_data()' or implement a static class method 'ObjectType::transcribe\_construct\_data()' - see "Transcribe.h". |
| `load_reference( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here const ObjectTag &object_tag)` | method | `LoadRef<ObjectType>` | public | 'ObjectType::transcribe\_construct\_data()' - see "Transcribe.h". |
| `get_transcribe_result()` | method | `TranscribeResult` | public | Returns the result of transcribing the most recently transcribed object in the \*load\* path. |
| `relocated( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here ObjectFirstQualifiedType &relocated_object, ObjectSecondQualifiedType &transcribed_object)` | method | `void` | public | if (scribe.is\_saving()) { scribe.transcribe(TRANSCRIBE\_SOURCE, container.at(0), "item", GPlatesScribe::TRACK); scribe.transcribe(TRANSCRIBE\_SOURCE, container.at(1), "item", GPlatesScribe::TRACK); } else // scribe.is\_loading() { A a; // ... |
| `relocated( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here ObjectFirstQualifiedType &relocated_object, LoadRef<ObjectSecondQualifiedType> transcribed_object)` | method | `void` | public | A convenient overload of relocated when the transcribed object is a LoadRef. |
| `has_been_transcribed( ObjectType &object)` | method | `bool` | public | Used to determine if the specified (tracked) object has been transcribed. |
| `is_in_transcription( const ObjectTag &object_tag)` | method | `bool` | public | Determines whether the specified object tag exists in the transcription (transcription is either being written to, on save path, or read from, on load path). |
| `push_transcribe_context( TranscribeContext<ObjectType> &transcribe_context)` | method | `void` | public | Pushes a reference to a transcribe context (for the object type 'ObjectType'). |
| `get_transcribe_context()` | method | `boost::optional<TranscribeContext<ObjectType> &>` | public | public: TranscribeContext(Y &y\_) : y(y\_) { } Y &y; }; GPlatesScribe::TranscribeResult transcribe\_construct\_data( GPlatesScribe::Scribe &scribe, GPlatesScribe::ConstructObject\<A\> &a) { if (scribe.is\_saving()) { ... |
| `pop_transcribe_context()` | method | `void` | public | Pops the most recently pushed transcribe context for the object type 'ObjectType'. |
| `ScopedTranscribeContextGuard` | class | `None` | public | A convenience RAII class that ensures a pushed transcribe context is popped on scope exit. |
| `get_transcribe_incompatible_call_stack()` | method | `std::vector<GPlatesUtils::CallStack::Trace>` | public | Returns the call stack trace at the last point the transcribe was incompatible. |
| `get_current_scribe_version()` | method | `unsigned int` | public | Returns the current version of the Scribe library/system. |
| `is_transcription_complete( bool emit_warnings = true)` | method | `bool` | public | Returns true if transcription is complete. |
| `get_transcription()` | method | `Transcription::non_null_ptr_to_const_type` | public | Returns the transcription. |
| `transcribe_context_stack_type` | typedef | `std::stack<void *>` | private | Typedef for a stack of 'void' references of transcribe contexts. |
| `class_id_type` | typedef | `unsigned int` | private | Typedef for an integer identifier for a class (or type). |
| `ClassInfo` | struct | `None` | private | Information associated with each registered class (or type). |
| `class_info_pool_type` | typedef | `boost::object_pool<ClassInfo>` | private | Typedef for a pool allocator of class infos. |
| `class_type_to_id_map_type` | typedef | `std::map<const std::type_info *, class_id_type, InternalUtils::SortTypeInfoPredicate>` | private | Typedef for a mapping from registered type to integer class identifier. |
| `class_info_seq_type` | typedef | `std::vector<ClassInfo *>` | private | Typedef for a sequence of class info structure pointers. |
| `object_id_type` | typedef | `TranscriptionScribeContext::object_id_type` | private | Typedef for an integer identifier for a transcribed object. |
| `object_ids_list_type` | typedef | `GPlatesUtils::SmartNodeLinkedList<object_id_type>` | private | Typedef for a linked list of object ids. |
| `object_ids_list_node_pool_type` | typedef | `boost::object_pool<object_ids_list_type::Node>` | private | Typedef for a pool of object id linked list nodes. |
| `transcribe_call_stack_type` | typedef | `std::vector<GPlatesUtils::CallStack::Trace>` | private | Typedef for a call stack (sequence of traces). |
| `ObjectInfo` | struct | `None` | private | Information associated with each transcribed object. |
| `object_info_pool_type` | typedef | `boost::object_pool<ObjectInfo>` | private | Typedef for a pool allocator of object infos. |
| `object_address_type` | typedef | `InternalUtils::ObjectAddress` | private | Typedef for an identifier for an object address that uses the address and the object type. |
| `tracked_object_address_to_id_map_type` | typedef | `std::map<object_address_type, object_id_type, InternalUtils::SortObjectAddressPredicate>` | private | Typedef for a mapping from tracked object address to integer object identifier. |
| `object_info_seq_type` | typedef | `std::vector<ObjectInfo *>` | private | Typedef for a sequence of object info structure pointers. |
| `transcribed_object_stack_type` | typedef | `std::stack<object_id_type>` | private | Typedef for a stack of object ids to track parent-to-sub-object transcribe relationships. |
| `CURRENT_SCRIBE_VERSION` | field | `unsigned int` | private | Increment this version number when modifications are made to the scribe library/system break forward compatibility (when newly created archives cannot be read by older Scribe versions built into older versions of GPlates). |
| `NULL_POINTER_OBJECT_ID` | field | `object_id_type` | private | The object ID used to identify NULL pointers. |
| `POINTS_TO_OBJECT_TAG` | field | `ObjectTag` | private | An object tag used to transcribe the id of an object pointed-to by a pointer. |
| `POINTS_TO_CLASS_TAG` | field | `ObjectTag` | private | An object tag used to transcribe the class name of an object pointed-to by a pointer. |
| `d_is_saving` | field | `bool` | private | Whether the transcription was read from an archive or will be written to one. |
| `d_transcription` | field | `Transcription::non_null_ptr_type` | private | The transcription contains the transcribed state. |
| `d_transcription_context` | field | `TranscriptionScribeContext` | private | Used to save/load to/from the transcription. |
| `d_void_cast_registry` | field | `VoidCastRegistry` | private | Used to cast a derived class 'void \*' to a base class 'void \*' or vice versa. |
| `d_transcribed_object_stack` | field | `transcribed_object_stack_type` | private | Keeps track of parent-to-sub-object relationships as objects are transcribed. |
| `d_object_ids_list_node_pool` | field | `object_ids_list_node_pool_type` | private | Pool allocator for object id linked list nodes. |
| `d_object_info_pool` | field | `object_info_pool_type` | private | Pool allocator for object info structures. |
| `d_object_infos` | field | `object_info_seq_type` | private | Information about each object, indexed by object id. |
| `d_tracked_object_address_to_id_map` | field | `tracked_object_address_to_id_map_type` | private | Maps addresses of tracked objects to their integer object ids. |
| `d_class_type_to_id_map` | field | `class_type_to_id_map_type` | private | Maps addresses of registered classes (or types) to their integer class ids. |
| `d_class_info_pool` | field | `class_info_pool_type` | private | Pool allocator for class info structures. |
| `d_class_infos` | field | `class_info_seq_type` | private | Information about each class, indexed by class id. |
| `d_transcribe_result` | field | `TranscribeResult` | private | The result of transcribing the last transcribed object. |
| `d_transcribe_incompatible_call_stack` | field | `transcribe_call_stack_type` | private | The call stack trace when an incompatible transcribe is first detected. |
| `d_exported_registered_classes` | field | `Access::export_registered_classes_type` | private | This is only here to force 'ScribeAccess.o' object file to get referenced and included by linker. |
| `transcribe_smart_pointer_object( \ const_cast<ObjectType unqualified_pointer() &>(object), \ shared_owner)` | method | `bool` | private | — |

### `UnsupportedPointerType`

*None.*

### `UnsupportedPointerType<ObjectType, GPLATES_SCRIBE_MAX_POINTER_DIMENSION+1>`

*None.*

### `StreamPrimitiveTag`

*None.*

### `StreamTranscribeTag`

*None.*

### `shared_ptr_map_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `POINTS_TO_OBJECT_TAG` | variable | `GPlatesScribe::ObjectTag` | We give names that are unlikely to conflict with names used by scribe clients. |
| `POINTS_TO_CLASS_TAG` | variable | `GPlatesScribe::ObjectTag` | — |
| `GPLATES_SCRIBE_SCRIBE_H` | macro | `None` | — |
| `GPLATES_SCRIBE_MAX_POINTER_DIMENSION` | macro | `2` | The maximum dimension of transcribable multi-level pointers. |
| `GPLATES_SCRIBE_MAX_ARRAY_DIMENSION` | macro | `3` | The maximum dimension of transcribable native arrays. |
| `TRANSCRIBE_SOURCE` | macro | `GPlatesUtils::CallStack::Trace(__FILE__, __LINE__)` | — |
| `GPLATES_SCRIBE_POW2_PRED` | macro_function | `BOOST_PP_TUPLE_ELEM(2, 1, state) \` | Predicate for GPLATES\_SCRIBE\_POW2. |
| `GPLATES_SCRIBE_POW2_MUL_BY_2` | macro_function | `( \ BOOST_PP_MUL_D(d, BOOST_PP_TUPLE_ELEM(2, 0, state), 2), \ BOOST_PP_DEC(BOOST_PP_TUPLE_ELEM(2, 1, state)) \ ) \` | Operation for GPLATES\_SCRIBE\_POW2. |
| `GPLATES_SCRIBE_POW2` | macro_function | `BOOST_PP_TUPLE_ELEM( \ 2, \ 0, \ BOOST_PP_WHILE( \ GPLATES_SCRIBE_POW2_PRED, \ GPLATES_SCRIBE_POW2_MUL_BY_2, \ (1, n)) \ ) \` | This is just pow(2,n) implemented as 1\*2\*2\*2\*, ie, repeated 'n' times... |
| `GPLATES_SCRIBE_ARRAY_INDICES_PRED` | macro_function | `BOOST_PP_TUPLE_ELEM(2, 1, state) \` | Predicate tests if array dimension decremented to zero. |
| `GPLATES_SCRIBE_ARRAY_INDICES_OP` | macro_function | `( \ BOOST_PP_INC(BOOST_PP_TUPLE_ELEM(2, 0, state)), \ BOOST_PP_DEC(BOOST_PP_TUPLE_ELEM(2, 1, state)) \ ) \` | Increment array index and decrements predicate counter. |
| `GPLATES_SCRIBE_ARRAY_TEMPLATE_INDICES_MACRO` | macro_function | `[BOOST_PP_CAT(N, BOOST_PP_TUPLE_ELEM(2, 0, state))] \` | Returns array template index as, eg, '\[N3\]'. |
| `GPLATES_SCRIBE_ARRAY_TEMPLATE_INDICES` | macro_function | `BOOST_PP_FOR( \ (1, array_dim), \ GPLATES_SCRIBE_ARRAY_INDICES_PRED, \ GPLATES_SCRIBE_ARRAY_INDICES_OP, \ GPLATES_SCRIBE_ARRAY_TEMPLATE_INDICES_MACRO) \` | Array template template indices (eg, '\[N1\] \[N2\] \[N3\]'). |
| `GPLATES_SCRIBE_ARRAY_TEMPLATE_PARAMETER_INDICES_MACRO` | macro_function | `(BOOST_PP_CAT(int N, BOOST_PP_TUPLE_ELEM(2, 0, state))) \` | Returns array template parameter index as, eg, '(int N3)'. |
| `GPLATES_SCRIBE_ARRAY_TEMPLATE_PARAMETER_INDICES` | macro_function | `BOOST_PP_FOR( \ (1, array_dim), \ GPLATES_SCRIBE_ARRAY_INDICES_PRED, \ GPLATES_SCRIBE_ARRAY_INDICES_OP, \ GPLATES_SCRIBE_ARRAY_TEMPLATE_PARAMETER_INDICES_MACRO) \` | Array template parameter indices returned as a sequence (eg, '(int N1) (int N2) (int N3)'). |
| `GPLATES_SCRIBE_QUALIFIED_OBJECT` | macro_function | `BOOST_PP_EXPR_IIF( \ BOOST_PP_MOD(index, 2), \ const) \` | Returns 'const' if least-significant bit of 'index' is set, otherwise nothing. |
| `GPLATES_SCRIBE_PRINT` | macro_function | `text` | / |
| `GPLATES_SCRIBE_UNQUALIFIED_POINTER` | macro_function | `BOOST_PP_CAT(BOOST_PP_REPEAT_,z)(pointer_level, GPLATES_SCRIBE_PRINT, *) \` | Repeat '\*' character 'pointer\_level' times. |
| `GPLATES_SCRIBE_QUALIFIED_POINTER_PRED` | macro_function | `BOOST_PP_TUPLE_ELEM(3, 2, state) \` | Predicate tests if pointer-level counter is zero. |
| `GPLATES_SCRIBE_QUALIFIED_POINTER_OP` | macro_function | `( \ BOOST_PP_DIV(BOOST_PP_TUPLE_ELEM(3, 0, state), 2), \ BOOST_PP_MOD(BOOST_PP_TUPLE_ELEM(3, 0, state), 2), \ BOOST_PP_DEC(BOOST_PP_TUPLE_ELEM(3, 2, state)) \ ) \` | Right shifts by one bit and tests the least-significant bit (that was shifted out). |
| `GPLATES_SCRIBE_QUALIFIED_POINTER_MACRO` | macro_function | `BOOST_PP_IIF( \ BOOST_PP_TUPLE_ELEM(3, 1, state), \ *const, \ *) \` | Return '\*const' or '\*' depending on the state. |
| `GPLATES_SCRIBE_QUALIFIED_POINTER` | macro_function | `BOOST_PP_FOR( \ ( \ BOOST_PP_DIV(index, 2), \ BOOST_PP_MOD(index, 2), \ pointer_level \ ), \ GPLATES_SCRIBE_QUALIFIED_POINTER_PRED, \ GPLATES_SCRIBE_QUALIFIED_POINTER_OP, \ GPLATES ...` | Repeat '\*const' or '\*' character 'pointer\_level' times depending on 'pointer\_level' number of bit flags in 'index'. |
| `GPLATES_SCRIBE_DELEGATE_SINGLE_ARG_FUNCTIONS_NON_ARRAY_CALL` | macro_function | `template <typename ObjectType> \ bool \ transcribe_const_cast( \ qualified_object() ObjectType qualified_pointer() &object, \ const ObjectTag &object_tag, \ unsigned int options) \ ...` | Generates single argument function delegate overloads for \*non-arrays\* for a specific multi-level pointer level. |
| `untrack_const_cast` | variable | `void` | — |
| `save_reference_const_cast` | variable | `void` | — |
| `GPLATES_SCRIBE_DELEGATE_SINGLE_ARG_FUNCTIONS_ARRAY_CALL` | macro_function | `template <typename ObjectType, BOOST_PP_SEQ_ENUM(array_template_parameter_indices)> \ bool \ transcribe_const_cast( \ qualified_object() ObjectType (qualified_pointer() &array) arr ...` | Generates single argument function delegate overloads for native \*arrays\* for a specific multi-level pointer level. |
| `has_been_transcribed_const_cast( \ qualified_object() ObjectType (qualified_pointer() &array) array_template_indices)` | function | `bool` | — |
| `untrack_const_cast( \ qualified_object() ObjectType (qualified_pointer() &array) array_template_indices, \ bool discard)` | function | `void` | — |
| `save_reference_const_cast( \ qualified_object() ObjectType (qualified_pointer() &array_reference) array_template_indices, \ const ObjectTag &object_tag)` | function | `void` | — |
| `GPLATES_SCRIBE_DELEGATE_SINGLE_ARG_FUNCTIONS_ARRAY` | macro_function | `GPLATES_SCRIBE_DELEGATE_SINGLE_ARG_FUNCTIONS_ARRAY_CALL( \` | Generates single argument function delegate overloads for native \*arrays\* for a specific multi-level pointer level. |
| `GPLATES_SCRIBE_DELEGATE_SINGLE_ARG_FUNCTIONS_CALL` | macro_function | `GPLATES_SCRIBE_DELEGATE_SINGLE_ARG_FUNCTIONS_NON_ARRAY_CALL( \` | Generates single argument function delegate overloads for a specific multi-level pointer level. |
| `GPLATES_SCRIBE_DELEGATE_SINGLE_ARG_FUNCTIONS_INDEX` | macro_function | `GPLATES_SCRIBE_DELEGATE_SINGLE_ARG_FUNCTIONS_CALL( \ z, \` | Generates single argument function delegate overloads for a multi-level pointer of dimension 'pointer\_level'. |
| `GPLATES_SCRIBE_DELEGATE_SINGLE_ARG_FUNCTIONS` | macro_function | `BOOST_PP_CAT(BOOST_PP_REPEAT_,z)( \ GPLATES_SCRIBE_POW2(BOOST_PP_INC(pointer_level)), \ GPLATES_SCRIBE_DELEGATE_SINGLE_ARG_FUNCTIONS_INDEX, \ pointer_level) \` | Iterate over half-open range \[ 0, 2\*pow(2,pointer\_level) ) and generate all const/non-const multi-level pointer combinations for a particular pointer-level. |
| `GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_FUNCTIONS_NON_ARRAY_CALL` | macro_function | `template <typename ObjectType> \ void \ relocated_const_cast( \ qualified_object() ObjectType qualified_pointer() &relocated_object, \ qualified_object() ObjectType qualified_point ...` | Generates double argument function delegate overloads for \*non-arrays\* for a specific multi-level pointer level. |
| `GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_FUNCTIONS_ARRAY_CALL` | macro_function | `template <typename ObjectType, BOOST_PP_SEQ_ENUM(array_template_parameter_indices)> \ void \ relocated_const_cast( \ qualified_object() ObjectType (qualified_pointer() &relocated_a ...` | Generates double argument function delegate overloads for native \*arrays\* for a specific multi-level pointer level. |
| `relocated_const_cast` | variable | `void` | — |
| `GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_NON_POINTER_FUNCTIONS_ARRAY` | macro_function | `GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_FUNCTIONS_ARRAY_CALL( \` | Generates double \*non-pointer\* argument function delegate overloads for native \*arrays\*. |
| `GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_NON_POINTER_FUNCTIONS` | macro_function | `GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_FUNCTIONS_NON_ARRAY_CALL( \` | Double \*non-pointer\* argument function delegates. |
| `GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_POINTER_FUNCTIONS_ARRAY` | macro_function | `GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_FUNCTIONS_ARRAY_CALL( \` | Generates double pointer argument function delegate overloads for native \*arrays\* for a specific multi-level pointer level. |
| `GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_POINTER_FUNCTIONS_CALL` | macro_function | `GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_FUNCTIONS_NON_ARRAY_CALL( \` | Generates double pointer argument function delegate overloads for a specific multi-level pointer level. |
| `GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_POINTER_FUNCTIONS_INDEX` | macro_function | `GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_POINTER_FUNCTIONS_CALL( \ z, \` | Generates double argument pointer function delegate overloads for a multi-level pointer of dimension 'pointer\_level'. |
| `GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_POINTER_FUNCTIONS` | macro_function | `BOOST_PP_CAT(BOOST_PP_REPEAT_,z)( \ GPLATES_SCRIBE_POW2(pointer_level), \ GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_POINTER_FUNCTIONS_INDEX, \ pointer_level) \` | Double \*pointer\* argument function delegates. |
| `untrack( ObjectType &object, bool discard)` | function | `void` | Untrack a tracked object. |
| `transcribe_construct( ConstructObject<ObjectType> &object, const ObjectTag &object_tag, unsigned int options)` | function | `bool` | A version of transcribe that accepts a un-initialised object that needs to be constructed. |
| `transcribe_construct( ConstructObject<ObjectType> &object, object_id_type object_id, unsigned int options)` | function | `bool` | An overload of transcribe\_construct that accepts an object id instead of object tag name/version. |
| `transcribe_smart_pointer( ObjectType *&object_ptr, bool shared_owner)` | function | `bool` | Transcribe a pointer-owned object according to the smart pointer protocol. |
| `transcribe_delegate( ObjectType &object)` | function | `bool` | A transcribed object type has delegated transcribing to another object type. |
| `save_delegate( const ObjectType &object)` | function | `void` | A transcribed object type has delegated transcribing to another object type. |
| `load_delegate( const GPlatesUtils::CallStack::Trace &transcribe_source)` | function | `LoadRef<ObjectType>` | A transcribed object type has delegated transcribing to another object type. |
| `transcribe_delegate_const_cast( ObjectType &object)` | function | `bool` | Delegates to transcribe\_delegate\_object. |
| `transcribe_delegate_const_cast( const ObjectType &object)` | function | `bool` | Delegates to transcribe\_delegate\_object. |
| `transcribe_delegate_object( ObjectType &object)` | function | `bool` | A transcribed object type has delegated transcribing to another object type. |
| `transcribe_delegate_construct_const_cast( ConstructObject<ObjectType> &construct_object)` | function | `bool` | Delegates to transcribe\_delegate\_construct\_object. |
| `transcribe_delegate_construct_const_cast( ConstructObject<const ObjectType> &construct_object)` | function | `bool` | Delegates to transcribe\_delegate\_construct\_object. |
| `transcribe_delegate_construct_object( ConstructObject<ObjectType> &construct_object)` | function | `bool` | A transcribed object type has delegated transcribing to another object type. |
| `transcribe_base_const_cast( DerivedType &derived_object, const ObjectTag &base_object_tag)` | function | `bool` | Delegates to transcribe\_base\_object. |
| `transcribe_base_const_cast( const DerivedType &derived_object, const ObjectTag &base_object_tag)` | function | `bool` | Delegates to transcribe\_base\_object. |
| `transcribe_base_const_cast()` | function | `bool` | Delegates to transcribe\_base\_object. |
| `transcribe_object( ObjectType &object, const ObjectTag &object_tag, unsigned int options)` | function | `bool` | Transcribe a \*non-pointer\* object. |
| `transcribe_object( ObjectType &object, object_id_type object_id, unsigned int options)` | function | `bool` | Transcribe a \*non-pointer\* object. |
| `transcribe_construct_object( ConstructObject<ObjectType> &construct_object, const ObjectTag &object_tag, unsigned int options)` | function | `bool` | Transcribe a \*non-pointer\* ConstructObject object wrapper. |
| `transcribe_construct_object( ConstructObject<ObjectType> &construct_object, object_id_type object_id, unsigned int options)` | function | `bool` | Transcribe a \*non-pointer\* ConstructObject object wrapper. |
| `transcribe_object( ObjectType *&object_ptr, const ObjectTag &object_tag, unsigned int options)` | function | `bool` | Transcribe a \*pointer\* object and possibly transcribe the pointed-to object depending on ownership options. |
| `transcribe_object( ObjectType *&object_ptr, const object_id_type object_id, unsigned int options)` | function | `bool` | Transcribe a \*pointer\* object and possibly transcribe the pointed-to object depending on ownership options. |
| `transcribe_construct_object( ConstructObject<ObjectType *> &construct_object_ptr, const ObjectTag &object_tag, unsigned int options)` | function | `bool` | Transcribe a \*pointer\* object, in ConstructObject wrapper, and possibly transcribe the pointed-to object depending on ownership options. |
| `transcribe_construct_object( ConstructObject<ObjectType *> &construct_object_ptr, object_id_type object_id, unsigned int options)` | function | `bool` | Transcribe a \*pointer\* object, in ConstructObject wrapper, and possibly transcribe the pointed-to object depending on ownership options. |
| `transcribe_smart_pointer_object( ObjectType *&object_ptr, bool shared_ownership)` | function | `bool` | Transcribe a pointer-owned object according to the smart pointer protocol. |
| `transcribe_pointer_owned_object( ObjectType *&object_ptr, bool shared_ownership, boost::optional<object_id_type &> return_object_id = boost::none)` | function | `bool` | Transcribe the object owned by the pointer. |
| `pre_transcribe( object_id_type object_id, class_id_type class_id, const object_address_type &object_address)` | function | `void` | Setup an object prior to streaming/initialisation. |
| `post_transcribe( object_id_type object_id, unsigned int options, bool discard, bool is_object_initialised = true)` | function | `void` | Finish up after an object was streamed/initialised. |
| `transcribe_base_object( DerivedType &derived_object, const ObjectTag &base_object_tag)` | function | `bool` | Transcribe the base object part of the specified derived object. |
| `transcribe_base_object()` | function | `bool` | Transcribe the BaseType/DerivedType inheritance relationship only. |
| `save_object_reference( ObjectType &object_reference, const ObjectTag &object_tag)` | function | `void` | Save a \*reference\* to an object. |
| `load_object_reference( const GPlatesUtils::CallStack::Trace &transcribe_source, const ObjectTag &object_tag)` | function | `LoadRef<ObjectType>` | Load a \*reference\* to an object. |
| `relocated_transcribed_object( ObjectType &relocated_object, ObjectType &transcribed_object)` | function | `void` | A previously transcribed (loaded) object has been moved to a new memory location. |
| `relocated_address( object_id_type transcribed_object_id, const object_address_type &transcribed_object_address, const object_address_type &relocated_object_address, std::size_t relocation_pointer_offset, bool is_relocation_pointer_offset_positive)` | function | `void` | The non-template implementation of relocated\_object. |
| `has_object_been_transcribed( ObjectType &object)` | function | `bool` | Determines if the specified object has been transcribed (client has called transcribe() on it). |
| `untrack_object( ObjectType &object, bool discard)` | function | `void` | Untrack a tracked object. |
| `transcribe_object_id( const object_address_type &save_object_address, const ObjectTag &object_tag, boost::optional<object_id_type &> return_object_id = boost::none)` | function | `bool` | Obtain and transcribe the object id for the specified object address. |
| `transcribe_class_name( const std::type_info *save_class_type_info, boost::optional<const ExportClassType &> &export_class_type)` | function | `bool` | Obtain and transcribe the class name for the specified class type info. |
| `transcribe_pointed_to_class_name_if_polymorphic( ObjectType *object_ptr, boost::optional< boost::intrusive_ptr<const InternalUtils::TranscribeOwningPointer> &> owns = boost::none)` | function | `bool` | Obtain and transcribe the class name for the object pointed to by object\_ptr if 'ObjectType' is polymorphic. |
| `transcribe_pointed_to_class_name_if_polymorphic( ObjectType *object_ptr, boost::optional< boost::intrusive_ptr<const InternalUtils::TranscribeOwningPointer> &> owns, boost::mpl::true_/*'ObjectType' is polymorphic*/)` | function | `bool` | — |
| `transcribe_pointed_to_class_name_if_polymorphic( ObjectType *object_ptr, boost::optional< boost::intrusive_ptr<const InternalUtils::TranscribeOwningPointer> &> owns, boost::mpl::false_/*'ObjectType' is *not* polymorphic*/)` | function | `bool` | — |
| `set_transcribe_result( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here TranscribeResult transcribe_result)` | function | `void` | Set the current transcribe result. |
| `register_object_type()` | function | `class_id_type` | Registers the object type 'ObjectType' by creating a new class id for it (if necessary) and initialising the associated class info. |
| `register_instantiable_class_info( ClassInfo &class_info, boost::mpl::true_/*'ObjectType' is instantiable*/)` | function | `void` | Initialise ClassInfo data members only if 'ObjectType' is instantiable. |
| `register_instantiable_class_info( ClassInfo &class_info, boost::mpl::false_/*'ObjectType' is not instantiable*/)` | function | `void` | Initialise ClassInfo data members only if 'ObjectType' is \*not\* instantiable. |
| `get_or_create_save_object_id_and_map_tracked_object_address( const object_address_type &object_address)` | function | `object_id_type` | Gets the object id associated with the specified tracked object address. |
| `get_or_create_load_object_info( object_id_type object_id)` | function | `void` | If the object id is not found then a new object info is created and associated with it. |
| `map_tracked_load_object_address_to_object_id( const object_address_type &object_address, object_id_type object_id)` | function | `void` | Map the tracked load object address with the specified object id. |
| `unmap_tracked_object_address_to_object_id( object_id_type object_id, bool discard)` | function | `void` | Unmap tracked object address associated with the specified object id and unmap all child-object addresses recursively. |
| `get_object_info` | variable | `ObjectInfo` | Returns the ObjectInfo associated with the specified object id. |
| `get_object_address( object_id_type object_id)` | function | `object_address_type` | Returns the object address of the specified object. |
| `find_object_address( object_id_type object_id)` | function | `boost::optional<object_address_type>` | Returns the object address of the specified object (if any). |
| `get_object_id( const object_address_type &object_address)` | function | `object_id_type` | Returns the object id of the object at the specified object address. |
| `find_object_id( const object_address_type &object_address)` | function | `boost::optional<object_id_type>` | Returns the object id of the object at the specified object address (if any). |
| `push_transcribed_object( object_id_type transcribed_object_id)` | function | `void` | Starting transcribing a new object. |
| `pop_transcribed_object( object_id_type transcribed_object_id)` | function | `void` | Finished transcribing the current object. |
| `get_current_transcribed_object()` | function | `boost::optional<ObjectInfo &>` | Returns the object currently being transcribed (or boost::none if none). |
| `is_child_object_inside_parent_object_memory( object_id_type child_object_id, object_id_type parent_object_id)` | function | `bool` | Returns true if the address of the specified child object is contained inline within its parent object (specified as parent\_object\_id). |
| `add_child_as_sub_object_if_inside_parent( object_id_type child_object_id)` | function | `void` | Adds the specified child object as a sub-object of its parent if it lies \*inside\* the memory area of its parent. |
| `remove_child_as_sub_object_if_outside_parent( object_id_type child_object_id)` | function | `void` | Removes the specified child object as a sub-object of its parent if it lies \*outside\* the memory area of its parent. |
| `add_or_remove_relocated_child_as_sub_object_if_inside_or_outside_parent( object_id_type relocated_object_id)` | function | `void` | Adds, or removes, the specified relocated object as a sub-object of its parent if it lies inside, or outside, the memory area of its parent (if it's not already the case). |
| `remove_parent_object_from_children( object_id_type parent_object_id)` | function | `void` | Removes the specified parent object from its child objects. |
| `add_child_object_to_parent( object_id_type child_object_id)` | function | `void` | Adds the specified child object to its parent. |
| `remove_child_object_from_parent( object_id_type child_object_id)` | function | `void` | Removes the specified child object from its parent's child/sub/base lists (if has a parent). |
| `add_pointer_referencing_object( object_id_type object_id, object_id_type pointer_object_id)` | function | `void` | Add a pointer to the list of pointers that reference a pointed-to object. |
| `remove_pointer_referencing_object( object_id_type pointer_object_id)` | function | `void` | Remove a pointer from the list of pointers that reference a pointed-to object. |
| `resolve_pointers_referencing_object( object_id_type object_id)` | function | `void` | Sets all pointers (referencing the specified object) to point to the object's address. |
| `resolve_pointer_reference_to_object( object_id_type object_id, object_id_type pointer_object_id)` | function | `void` | Set the pointer to point to the object (in the load path). |
| `unresolve_pointers_referencing_object( object_id_type object_id)` | function | `void` | Sets all pointers (referencing the specified object) to NULL. |
| `unresolve_pointer_reference_to_object( object_id_type pointer_object_id)` | function | `void` | Sets pointer (referencing the specified object) to NULL. |
| `set_pointer_to_object( object_id_type object_id, void *object_address, ObjectType *&object_ptr)` | function | `bool` | Set the pointer to point to the object (in the load path). |
| `get_or_create_class_id( const std::type_info &class_type)` | function | `class_id_type` | Gets, or creates, the class id associated with the specified class type. |
| `create_new_class_info()` | function | `class_id_type` | Creates a new ClassInfo using the next available class id and returns that id. |
| `get_class_info` | variable | `ClassInfo` | Returns the ClassInfo associated with the specified class id. |
| `get_class_info_from_object` | variable | `ClassInfo` | Returns the ClassInfo associated with the specified \*object\* id. |
| `get_transcribe_context_stack( const std::type_info &class_type_info)` | function | `boost::optional<transcribe_context_stack_type &>` | Returns the transcribe context stack associated with the specified class type, or boost::none if a ClassInfo has not already been created for the specified class type (eg, by object type registration or by pushing a transcribe context). |
| `stream_construct_object( ConstructObject<ObjectType> &construct_object)` | function | `bool` | Save/load construct and transcribe an object. |
| `stream_object( ObjectType &object)` | function | `bool` | Transcribe an object (with no save/load construction). |
| `stream( ObjectType &object, bool transcribed_construct_data)` | function | `bool` | — |
| `stream( ObjectType &object, bool transcribed_construct_data, StreamPrimitiveTag)` | function | `bool` | Stream primitives directly to archive. |
| `stream( ObjectType &object, bool transcribed_construct_data, StreamTranscribeTag)` | function | `bool` | Catch-all stream object using 'transcribe()' specialisation or overload. |
| `reset( boost::shared_ptr<T> &shared_ptr_object, T *raw_ptr)` | function | `void` | Helper function for transcribing boost::shared\_ptr. |
| `reset( boost::shared_ptr<const T> &shared_ptr_object, const T *raw_ptr)` | function | `void` | Const overload for helper function for transcribing boost::shared\_ptr. |
| `reset_impl( boost::shared_ptr<T> &shared_ptr_object, NonConstT *raw_ptr)` | function | `void` | Helper function for transcribing boost::shared\_ptr. |
| `d_shared_ptr_map` | variable | `shared_ptr_map_type` | — |
| `ScribeInternalAccess` | variable | `friend` | Give friend access class ScribeInternalAccess in order to limit the access to our internals. |
| `transcribe_ADL( Scribe &scribe, ObjectType &object, bool transcribed_construct_data)` | function | `TranscribeResult` | In order to get Argument Dependent Lookup (ADL) for the non-member 'transcribe()' function, based on the namespace in which 'ObjectType' is declared, we need to use a non-member helper function to avoid the clash with same-named member ... |

## Notes

[[[PROSE notes unit=scribe/Scribe tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 720 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 263 |
| [scribe/TranscriptionScribeContext](TranscriptionScribeContext.md) | scribe | 214 |
| [gui/BuiltinColourPalettes](../gui/BuiltinColourPalettes.md) | gui | 108 |
| [view-operations/ScalarField3DRenderParameters](../view-operations/ScalarField3DRenderParameters.md) | view-operations | 77 |
| [scribe/TranscribeUtils](TranscribeUtils.md) | scribe | 59 |
| [scribe/TranscribeBoost](TranscribeBoost.md) | scribe | 51 |
| [gui/BuiltinColourPaletteType](../gui/BuiltinColourPaletteType.md) | gui | 46 |
| [scribe/TranscribeQt](TranscribeQt.md) | scribe | 46 |
| [model/TranscribeQualifiedXmlName](../model/TranscribeQualifiedXmlName.md) | model | 32 |
| [scribe/TranscribeStd](TranscribeStd.md) | scribe | 32 |
| [scribe/ScribeExceptions](ScribeExceptions.md) | scribe | 31 |
| [app-logic/TopologyNetworkParams](../app-logic/TopologyNetworkParams.md) | app-logic | 30 |
| [scribe/ScribeXmlArchiveReader](ScribeXmlArchiveReader.md) | scribe | 29 |
| [data-mining/CoRegConfigurationTable](../data-mining/CoRegConfigurationTable.md) | data-mining | 26 |
| [model/TranscribeStringContentTypeGenerator](../model/TranscribeStringContentTypeGenerator.md) | model | 24 |
| [presentation/ProjectSession](../presentation/ProjectSession.md) | presentation | 24 |
| [data-mining/RegionOfInterestFilter](../data-mining/RegionOfInterestFilter.md) | data-mining | 22 |
| [gui/Symbol](../gui/Symbol.md) | gui | 22 |
| [presentation/InternalSession](../presentation/InternalSession.md) | presentation | 21 |

*... and 30 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/Scribe.h
python scripts/gpq.py def GPlatesScribe::Scribe --body
python scripts/gpq.py uses Scribe --kind class
python scripts/gpq.py hier Scribe
```

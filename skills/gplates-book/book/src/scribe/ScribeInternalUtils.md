# ScribeInternalUtils

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 28 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeInternalUtils.h` | C++ | 520 |

## Overview

[[[PROSE overview unit=scribe/ScribeInternalUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::InternalUtils::object_id_type`](#gplatesscribeinternalutilsobject_id_type) | typedef | — | — | 0 | Typedef for an integer identifier for a transcribed object. |
| [`GPlatesScribe::InternalUtils::SortTypeInfoPredicate`](#gplatesscribeinternalutilssorttypeinfopredicate) | struct | — | — | 0 | Used to order std::type\_info objects in a std::map. |
| [`GPlatesScribe::InternalUtils::ObjectAddress`](#gplatesscribeinternalutilsobjectaddress) | struct | — | — | 0 | An identifier for an object address that uses the address and the object type. |
| [`GPlatesScribe::InternalUtils::SortObjectAddressPredicate`](#gplatesscribeinternalutilssortobjectaddresspredicate) | struct | — | — | 0 | Used to order ObjectAddress keys in a std::map. |
| [`GPlatesScribe::InternalUtils::TranscribeOwningPointer`](#gplatesscribeinternalutilstranscribeowningpointer) | class | [`GPlatesUtils::ReferenceCount<TranscribeOwningPointer>`](../utils/ReferenceCount.md) | — | 1 | Interface for loading/saving an object, allocated on the heap, via its pointer. |
| [`GPlatesScribe::InternalUtils::TranscribeOwningPointerTemplate`](#gplatesscribeinternalutilstranscribeowningpointertemplate) | class | [`TranscribeOwningPointer`](ScribeInternalUtils.md) | `<typename ObjectType>` | 0 | Load/save an object, allocated on the heap, via its pointer. |
| [`GPlatesScribe::InternalUtils::Relocated`](#gplatesscribeinternalutilsrelocated) | class | [`GPlatesUtils::ReferenceCount<Relocated>`](../utils/ReferenceCount.md) | — | 1 | Interface for responding to a relocation of a loaded object (to keep object tracking intact). |
| [`GPlatesScribe::InternalUtils::RelocatedTemplate`](#gplatesscribeinternalutilsrelocatedtemplate) | class | [`Relocated`](ScribeInternalUtils.md) | `<typename ObjectType>` | 0 | Delegates response (to a relocation of a loaded object) to the appropriate specialisation or overload (for 'ObjectType') of the non-member function 'relocated()'. |

## Members

### `GPlatesScribe::InternalUtils::object_id_type`

*None.*

### `GPlatesScribe::InternalUtils::SortTypeInfoPredicate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SortTypeInfoPredicate()` | constructor | `None` | public | — |
| `operator()( const std::type_info *lhs, const std::type_info *rhs)` | operator | `bool` | public | — |

### `GPlatesScribe::InternalUtils::ObjectAddress`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ObjectAddress()` | constructor | `None` | public | Default constructor sets the NULL 'void' pointer. |
| `ObjectAddress( const std::type_info &type_)` | constructor | `None` | public | — |
| `ObjectAddress( void *address_, const std::type_info &type_)` | constructor | `None` | public | — |
| `operator==( const ObjectAddress &other)` | operator | `bool` | public | — |
| `operator!=( const ObjectAddress &other)` | operator | `bool` | public | — |
| `address` | field | `void` | public | — |
| `type` | field | `std::type_info` | public | Note that std::type\_info is not copy-constructable so we use pointers instead of references... |

### `GPlatesScribe::InternalUtils::SortObjectAddressPredicate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SortObjectAddressPredicate()` | constructor | `None` | public | — |
| `operator()( const ObjectAddress &lhs, const ObjectAddress &rhs)` | operator | `bool` | public | — |

### `GPlatesScribe::InternalUtils::TranscribeOwningPointer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<TranscribeOwningPointer>` | public | Convenience typedefs for a shared pointer to a TranscribeOwningPointer. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const TranscribeOwningPointer>` | public | — |
| `~TranscribeOwningPointer()` | destructor | `None` | public | — |
| `save_object( Scribe &scribe, void *object_ptr, object_id_type object_id, unsigned int options)` | method | `void` | public | Saves the specified object (on the heap) to the archive. |
| `load_object( Scribe &scribe, object_id_type object_id, unsigned int options)` | method | `bool` | public | Creates a new object on the heap and loads it from the archive using object\_id. |

### `GPlatesScribe::InternalUtils::TranscribeOwningPointerTemplate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `this_type` | typedef | `TranscribeOwningPointerTemplate<ObjectType>` | public | — |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<this_type>` | public | Convenience typedefs for a shared pointer to a 'TranscribeOwningPointerTemplate\<ObjectType\>'. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const this_type>` | public | — |
| `create()` | method | `non_null_ptr_type` | public | Creates an instance of 'TranscribeOwningPointerTemplate\<ObjectType\>'. |
| `save_object( Scribe &scribe, void *object_ptr, object_id_type object_id, unsigned int options)` | method | `void` | public | Saves the specified object of type 'ObjectType' (on the heap) to the archive. |
| `load_object( Scribe &scribe, object_id_type object_id, unsigned int options)` | method | `bool` | public | Creates a new object on the heap and loads it from the archive using object\_id. |
| `TranscribeOwningPointerTemplate()` | constructor | `None` | private | — |

### `GPlatesScribe::InternalUtils::Relocated`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<Relocated>` | public | Convenience typedefs for a shared pointer to a Relocated. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const Relocated>` | public | — |
| `~Relocated()` | destructor | `None` | public | — |
| `relocated( Scribe &scribe, const void *relocated_object, const void *transcribed_object)` | method | `void` | public | Notification from the Scribe that a previously transcribed (loaded) object has been moved to a new memory location. |

### `GPlatesScribe::InternalUtils::RelocatedTemplate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `this_type` | typedef | `RelocatedTemplate<ObjectType>` | public | — |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<this_type>` | public | Convenience typedefs for a shared pointer to a 'RelocatedTemplate\<ObjectType\>'. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const this_type>` | public | — |
| `create()` | method | `non_null_ptr_type` | public | Creates an instance of 'RelocatedTemplate\<ObjectType\>'. |
| `relocated( Scribe &scribe, const void *relocated_object, const void *transcribed_object)` | method | `void` | public | Notification from the Scribe that a previously transcribed (loaded) object has been moved to a new memory location. |
| `RelocatedTemplate()` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBEINTERNALUTILS_H` | macro | `None` | — |
| `get_object_address( ObjectType *object_address, boost::mpl::true_/*is_polymorphic*/)` | function | `ObjectAddress` | Overload for polymorphic types - returns address of the entire (dynamic) object. |
| `get_object_address( ObjectType *object_address, boost::mpl::false_/*is_polymorphic*/)` | function | `ObjectAddress` | Overload for non-polymorphic types - just returns the address passed in. |
| `get_dynamic_object_address( ObjectType *object_address)` | function | `ObjectAddress` | Returns the actual address associated with the specified object's address. |
| `get_static_object_address( ObjectType *object_address)` | function | `ObjectAddress` | Returns the static address - static cast to 'void \*'. |
| `shared_ptr_cast( const boost::shared_ptr<U> &ptr, boost::mpl::true_)` | function | `boost::shared_ptr<T>` | — |
| `shared_ptr_cast( const boost::shared_ptr<U> &ptr, boost::mpl::false_)` | function | `boost::shared_ptr<T>` | — |
| `shared_ptr_cast( const boost::shared_ptr<U> &ptr)` | function | `boost::shared_ptr<T>` | Cast a boost::shared\_ptr using dynamic\_cast for polymorphic types, otherwise static\_cast. |
| `relocated_ADL( Scribe &scribe, const ObjectType &relocated_object, const ObjectType &transcribed_object)` | function | `void` | In order to get Argument Dependent Lookup (ADL) for the non-member 'relocated()' function, based on the namespace in which 'ObjectType' is declared, we use a non-member helper function to avoid the clash with same-named member function ... |

## Notes

[[[PROSE notes unit=scribe/ScribeInternalUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/Scribe](Scribe.md) | scribe | 98 |
| [scribe/ScribeExportRegistry](ScribeExportRegistry.md) | scribe | 12 |
| [scribe/ScribeVoidCastRegistry](ScribeVoidCastRegistry.md) | scribe | 9 |
| [scribe/ScribeInternalAccess](ScribeInternalAccess.md) | scribe | 3 |
| [scribe/ScribeInternalUtilsImpl](ScribeInternalUtilsImpl.md) | scribe | 3 |
| [scribe/ScribeLoadRefImpl](ScribeLoadRefImpl.md) | scribe | 1 |
| [scribe/ScribeTextArchiveReader](ScribeTextArchiveReader.md) | scribe | 1 |
| [scribe/ScribeXmlArchiveReader](ScribeXmlArchiveReader.md) | scribe | 1 |
| [scribe/TranscriptionScribeContext](TranscriptionScribeContext.md) | scribe | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeInternalUtils.h
python scripts/gpq.py def GPlatesScribe::InternalUtils::TranscribeOwningPointerTemplate --body
python scripts/gpq.py uses TranscribeOwningPointerTemplate --kind class
python scripts/gpq.py hier TranscribeOwningPointerTemplate
```

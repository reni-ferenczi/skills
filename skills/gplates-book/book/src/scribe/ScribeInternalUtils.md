# ScribeInternalUtils

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 28 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeInternalUtils.h` | C++ | 520 |

## Overview

Internal plumbing for the Scribe library itself, not part of its public API. It solves two problems that the templated `Scribe` transcribe functions cannot solve on their own: identifying an object's true address when pointers and references to it may alias, and erasing an object's concrete type so it can be saved or loaded through a common interface.

`ObjectAddress` pairs a `void *` with a `std::type_info *` (kept as a pointer because `std::type_info` is not copy-constructible) so that two objects at the same memory address but of different types — for example a base sub-object and the derived object that contains it — are not confused with each other. `get_dynamic_object_address()` resolves this correctly for polymorphic types by `dynamic_cast`-ing to the complete object, since under multiple inheritance a base sub-object's address can differ from the derived object's; `get_static_object_address()` instead keeps the address as given. `shared_ptr_cast()` picks `dynamic_pointer_cast` or `static_pointer_cast` for a `boost::shared_ptr` based on the same polymorphism check.

`TranscribeOwningPointer` and its `TranscribeOwningPointerTemplate<ObjectType>` subclass let `Scribe` save and load a heap-allocated object through a pointer without the calling code needing to know `ObjectType` — the template captures the type once, at the point the pointer is registered, and the type-erased base is what the rest of the Scribe machinery stores and calls through. The template's `save_object()`/`load_object()` bodies live in `ScribeInternalUtilsImpl.h` rather than here, so that including this header does not pull in `Scribe.h`. `Relocated` and `RelocatedTemplate<ObjectType>` follow the same type-erasure pattern for the opposite direction: when the `Scribe` moves a previously loaded object to a new address, `RelocatedTemplate` finds and calls a non-member `relocated()` function for `ObjectType` via argument-dependent lookup, so client code can supply that hook in its own namespace instead of in `GPlatesScribe`.

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

`TranscribeOwningPointerTemplate` and `RelocatedTemplate` have private constructors and must be created through their `create()` factory methods, which return a `non_null_intrusive_ptr` — this keeps every instance reference-counted via `GPlatesUtils::ReferenceCount`. `relocated_ADL()` deliberately calls `relocated()` unqualified so ADL can find a client-namespace overload instead of recursing into `RelocatedTemplate::relocated()`; a `relocated()` overload placed in `GPlatesScribe` itself would be found preferentially and break that dispatch.

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

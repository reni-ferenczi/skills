# ScribeSaveLoadConstructObject

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 1222 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeSaveLoadConstructObject.h` | C++ | 201 |

## Overview

The three concrete `ConstructObject<ObjectType>` implementations that back constructor transcription — the mechanism Scribe uses to support types with no default constructor, where the constructor's arguments must themselves be loaded from the archive before the object can be created. `SaveConstructObject` wraps an already-existing object so the save path can go through the same `ConstructObject` interface the load path uses, keeping the two paths mirror images of each other. `LoadConstructObjectOnStack` and `LoadConstructObjectOnHeap` instead start from raw, uninitialised storage — respectively an inline `boost::aligned_storage` buffer sized and aligned for `ObjectType`, and a heap block obtained with a raw placement-`new`-style `operator new` — and defer actual construction to `ConstructObject`'s own `construct_object()`, which placement-constructs `ObjectType` into that storage once its constructor arguments have all been loaded.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::SaveConstructObject`](#gplatesscribesaveconstructobject) | class | [`ConstructObject<ObjectType>`](ScribeConstructObject.md) | `<typename ObjectType>` | 0 | Used when saving a ConstructObject to an archive. |
| [`GPlatesScribe::LoadConstructObjectOnStack`](#gplatesscribeloadconstructobjectonstack) | class | [`ConstructObject<ObjectType>`](ScribeConstructObject.md) | `<typename ObjectType>` | 0 | Used when loading a ConstructObject from an archive onto the C runtime stack. |
| [`GPlatesScribe::LoadConstructObjectOnHeap`](#gplatesscribeloadconstructobjectonheap) | class | [`ConstructObject<ObjectType>`](ScribeConstructObject.md) | `<typename ObjectType>` | 0 | Used when loading a ConstructObject from an archive onto the memory heap. |

## Members

### `GPlatesScribe::SaveConstructObject`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SaveConstructObject( const ObjectType &object)` | constructor | `None` | public | — |

### `GPlatesScribe::LoadConstructObjectOnStack`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LoadConstructObjectOnStack()` | constructor | `None` | public | — |
| `~LoadConstructObjectOnStack()` | destructor | `None` | public | Destructs the internal object of type ObjectType if it has been constructed. |
| `uninitialised_object_storage_type` | typedef | `boost::aligned_storage< sizeof(ObjectType), boost::alignment_of<ObjectType>::value>` | private | Typedef for uninitialised storage for the object of type 'ObjectType'. |
| `d_uninitialised_object_storage` | field | `uninitialised_object_storage_type` | private | — |
| `address()` | method | `ObjectType` | private | Returns address of internal object. |

### `GPlatesScribe::LoadConstructObjectOnHeap`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LoadConstructObjectOnHeap()` | constructor | `None` | public | — |
| `~LoadConstructObjectOnHeap()` | destructor | `None` | public | Releases allocated memory of the internal object if it was never constructed. |
| `release()` | method | `ObjectType` | public | Release ownership of the internal object (must be initialised). |
| `d_released` | field | `bool` | private | — |
| `allocate_object()` | method | `ObjectType` | private | Allocates space for the internal object on the heap. |
| `deallocate_object( ObjectType *object_ptr)` | method | `void` | private | Deallocates the internal object from the heap. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBESAVELOADCONSTRUCTOBJECT_H` | macro | `None` | — |

## Notes

Both loader classes track initialisation state and clean up correctly whichever way construction ends: `LoadConstructObjectOnStack`'s destructor calls `~ObjectType()` only if the object was actually constructed; `LoadConstructObjectOnHeap`'s destructor deletes the constructed object if it was never `release()`d, or just deallocates the raw memory (without calling a destructor) if construction never happened at all — the two failure/success paths use different cleanup (`delete` vs. plain `operator delete`) because only one of them has a live object to destroy. `LoadConstructObjectOnHeap::release()` asserts (`Exceptions::ScribeLibraryError`) that the object is initialised, and afterwards ownership passes entirely to the caller — the caller must `delete` the returned pointer, since the destructor no longer will.

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/Scribe](Scribe.md) | scribe | 5 |
| [scribe/ScribeInternalUtilsImpl](ScribeInternalUtilsImpl.md) | scribe | 3 |
| [scribe/TranscribeUtils](TranscribeUtils.md) | scribe | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeSaveLoadConstructObject.h
python scripts/gpq.py def GPlatesScribe::LoadConstructObjectOnHeap --body
python scripts/gpq.py uses LoadConstructObjectOnHeap --kind class
python scripts/gpq.py hier LoadConstructObjectOnHeap
```

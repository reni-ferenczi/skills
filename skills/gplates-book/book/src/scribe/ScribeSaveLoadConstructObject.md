# ScribeSaveLoadConstructObject

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 1222 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeSaveLoadConstructObject.h` | C++ | 201 |

## Overview

[[[PROSE overview unit=scribe/ScribeSaveLoadConstructObject tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=scribe/ScribeSaveLoadConstructObject tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

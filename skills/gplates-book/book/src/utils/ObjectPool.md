# ObjectPool

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1181 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/ObjectPool.h` | C++ | 534 |

## Overview

[[[PROSE overview unit=utils/ObjectPool tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::ObjectPool`](#gplatesutilsobjectpool) | class | `boost::noncopyable` | `<typename ObjectType>` | 0 | And it uses up to an extra 8 bytes per object above boost::object\_pool (4 bytes extra per object if don't call release). |

## Members

### `GPlatesUtils::ObjectPool`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ObjectWrapper` | struct | `None` | private | Wraps an 'ObjectType' in a boost::optional purely to give us the ability to destroy the object when it gets returned to the pool. |
| `ObjectPtr` | class | `None` | public | Pointer to an object obtained from the pool. |
| `object_ptr_type` | typedef | `ObjectPtr` | public | Typedef for a non-owning pointer to an object. |
| `shared_object_ptr_type` | typedef | `boost::shared_ptr<ObjectType>` | public | Typedef for a shared owning pointer to an object - see add\_with\_auto\_release. |
| `ObjectPool()` | constructor | `None` | public | Default constructor. |
| `empty()` | method | `bool` | public | Returns true if there are any objects currently in this pool. |
| `size()` | method | `unsigned int` | public | Returns the number of objects currently in this pool. |
| `clear()` | method | `void` | public | Destroys all objects and releases all memory allocated. |
| `add( const ObjectType &object)` | method | `object_ptr_type` | public | Copies object to a fixed memory address and returns a pointer to the copy. |
| `add( const InPlaceFactoryType &in_place_factory)` | method | `object_ptr_type` | public | Constructs a new object, using the constructor parameters transported by in\_place\_factory, at a fixed memory address in this pool and returns a pointer to it. |
| `add_with_auto_release( const ObjectType &object)` | method | `shared_object_ptr_type` | public | A convenience wrapper around add and release. |
| `add_with_auto_release( const InPlaceFactoryType &in_place_factory)` | method | `shared_object_ptr_type` | public | A convenience wrapper around add and release. |
| `release( object_ptr_type object_ptr)` | method | `void` | public | Makes the specified object available for reuse by a subsequent call to add. |
| `ReturnObjectToPoolDeleter` | struct | `None` | private | Custom boost::shared\_ptr deleter to return an object to its pool when all clients have finished with it. |
| `FreeListNode` | struct | `None` | private | A node in the linked list of free objects that stores a pointer to an object that is available for reuse. |
| `free_list_type` | typedef | `IntrusiveSinglyLinkedList<FreeListNode>` | private | Typedef for a linked list of free objects. |
| `free_list_node_pool_type` | typedef | `boost::object_pool<FreeListNode>` | private | Typedef for a pool of linked list nodes. |
| `object_pool_type` | typedef | `boost::object_pool<ObjectWrapper>` | private | Typedef for a pool of objects. |
| `d_object_free_list` | field | `free_list_type` | private | List of objects available for reuse. |
| `d_free_list_node_free_list` | field | `free_list_type` | private | List of linked list nodes available for reuse in the linked list of free objects. |
| `d_object_pool` | field | `boost::scoped_ptr<object_pool_type>` | private | Pool of objects. |
| `d_free_list_node_pool` | field | `boost::scoped_ptr<free_list_node_pool_type>` | private | Pool of linked list nodes. |
| `d_num_objects` | field | `unsigned int` | private | The number of objects currently in this pool. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_OBJECTPOOL_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=utils/ObjectPool tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLStateSetStore](../opengl/GLStateSetStore.md) | opengl | 45 |
| [api/PythonRunner](../api/PythonRunner.md) | api | 23 |
| [scribe/Scribe](../scribe/Scribe.md) | scribe | 21 |
| [api/PyFeature](../api/PyFeature.md) | api | 20 |
| [opengl/GLStateSets](../opengl/GLStateSets.md) | opengl | 18 |
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 18 |
| [opengl/GLMultiResolutionRaster](../opengl/GLMultiResolutionRaster.md) | opengl | 17 |
| [qt-widgets/HellingerThread](../qt-widgets/HellingerThread.md) | qt-widgets | 16 |
| [maths/CubeQuadTree](../maths/CubeQuadTree.md) | maths | 14 |
| [utils/LatLonAreaSampling](LatLonAreaSampling.md) | utils | 13 |
| [api/PyApplication](../api/PyApplication.md) | api | 10 |
| [gui/PythonConfiguration](../gui/PythonConfiguration.md) | gui | 10 |
| [opengl/GLFilledPolygonsMapView](../opengl/GLFilledPolygonsMapView.md) | opengl | 10 |
| [utils/ObjectCache](ObjectCache.md) | utils | 10 |
| [gui/DrawStyleAdapters](../gui/DrawStyleAdapters.md) | gui | 9 |
| [gui/PythonManager](../gui/PythonManager.md) | gui | 9 |
| [api/CoReg](../api/CoReg.md) | api | 8 |
| [opengl/GLProgramObject](../opengl/GLProgramObject.md) | opengl | 8 |
| [opengl/GLState](../opengl/GLState.md) | opengl | 8 |
| [api/ConsoleReader](../api/ConsoleReader.md) | api | 7 |

*... and 48 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/ObjectPool.h
python scripts/gpq.py def GPlatesUtils::ObjectPool --body
python scripts/gpq.py uses ObjectPool --kind class
python scripts/gpq.py hier ObjectPool
```

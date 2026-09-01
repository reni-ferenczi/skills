# ObjectCache

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1068 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/ObjectCache.h` | C++ | 936 |

## Overview

`ObjectCache<ObjectType>` maintains a bounded but expandable pool of objects that can be recycled between requests instead of freed and reallocated. It supports two usage patterns. Non-volatile allocation behaves like an object pool except that returned objects are *not* destructed or have their memory released — the client gets back the same live object and is responsible for resetting its state before reuse, which suits objects that own expensive heap-allocated resources. Volatile allocation goes further: a `VolatileObject` holds what amounts to a weak reference to a cached object, and the cache is free to steal (recycle) that object for a different request before the original client has explicitly released it. The client must call `VolatileObject::get_cached_object()` before each use and fall back to `recycle_an_unused_object()` or `set_cached_object()` if it returns null, because the underlying object may have been reassigned elsewhere.

The cache tracks two `SmartNodeLinkedList<ObjectInfo>` sequences, in-use and not-in-use, both ordered least- to most-recently touched, so recycling always steals the least-recently-used unused object once `d_min_num_objects` has been reached. Custom `boost::shared_ptr` deleters (`ObjectDeleter` for cached objects, `ReturnVolatileObjectToPoolDeleter` for `VolatileObject`s) intercept the last reference going out of scope and route the object back onto the not-in-use list rather than deleting it, unless the cache itself has already been destroyed. This design is intended for situations with many possible objects but only a small "working set" active at once — GPU-resident render caches (`GLMultiResolutionRaster`, `GLScalarField3D`, and related OpenGL classes) are the dominant users, where allocation is expensive enough that avoiding it, even at the cost of recycling churn, is worthwhile.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::ObjectCache`](#gplatesutilsobjectcache) | class | `boost::enable_shared_from_this< ObjectCache<ObjectType> >`<br>`boost::noncopyable` | `<typename ObjectType>` | 0 | 3) If that fails then create a new object (and add it to the cache). |

## Members

### `GPlatesUtils::ObjectCache`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `object_cache_type` | typedef | `ObjectCache<ObjectType>` | public | Typedef for this class. |
| `shared_ptr_type` | typedef | `boost::shared_ptr<object_cache_type>` | public | A convenience typedef for a shared pointer to a object\_cache\_type. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const object_cache_type>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<object_cache_type>` | public | A convenience typedef for a weak pointer to a object\_cache\_type. |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const object_cache_type>` | public | — |
| `object_type` | typedef | `ObjectType` | public | Typedef for the object type managed by this cache. |
| `object_shared_ptr_type` | typedef | `boost::shared_ptr<object_type>` | public | Typedef for a shared pointer to the object type managed by this cache. |
| `return_object_to_cache_function_type` | typedef | `boost::function<void (object_type &)>` | public | Typedef for a function to call on a 'object\_type' object when it is returned to the cache. |
| `create( std::size_t min_num_objects = 1)` | method | `shared_ptr_type` | public | Creates a ObjectCache object. min\_num\_objects is the minimum number of objects in the cache before any objects can be recycled. |
| `get_min_num_objects()` | method | `std::size_t` | public | Returns the minimum number of objects in the cache before recycling can happen. |
| `set_min_num_objects( std::size_t min_num_objects)` | method | `void` | public | Sets the minimum number of objects in the cache before recycling can happen. |
| `get_current_num_objects_in_use()` | method | `std::size_t` | public | Returns the number of cached objects that are currently being used. |
| `object_weak_ptr_type` | typedef | `boost::weak_ptr<object_type>` | private | Typedef for a shared pointer to the object type managed by this cache. |
| `object_seq_type` | typedef | `GPlatesUtils::SmartNodeLinkedList<ObjectInfo>` | private | Typedef for a list of object infos. |
| `ObjectDeleter` | class | `None` | private | Custom boost::shared\_ptr deleter to either: - return an object to the unused list of objects, if clients are finished with it, or - to delete the object when the object cache is destroyed. |
| `ObjectInfo` | struct | `None` | private | Contains information about the state of a cached object - whether it's in use or not. |
| `VolatileObject` | class | `None` | public | A volatile object allocated from the object cache - it is volatile because the object it references can be recycled, by the object cache, for another request. |
| `volatile_object_type` | typedef | `VolatileObject` | public | Typedef for a volatile object managed by this cache. |
| `volatile_object_ptr_type` | typedef | `boost::shared_ptr<volatile_object_type>` | public | Typedef for a pointer to a volatile object managed by this cache. |
| `allocate_volatile_object()` | method | `volatile_object_ptr_type` | public | Allocates a new volatile object that can be used to reference a cached object. |
| `allocate_object()` | method | `boost::optional<object_shared_ptr_type>` | public | Returns a direct reference to an unused object. |
| `allocate_object( std::unique_ptr<object_type> new_object, const return_object_to_cache_function_type &return_object_to_cache_function = return_object_to_cache_function_type())` | method | `object_shared_ptr_type` | public | Adds the specified newly created object to the cache and returns a shared\_ptr to the same object that will release the object for reuse when all copies of the shared\_ptr are destroyed. |
| `volatile_object_pool_type` | typedef | `GPlatesUtils::ObjectPool<volatile_object_type>` | private | Typedef for a pool of volatile objects. |
| `ReturnVolatileObjectToPoolDeleter` | struct | `None` | private | Custom boost::shared\_ptr deleter to return an object to its pool when all clients have finished with it. |
| `object_seq_node_pool_type` | typedef | `boost::object_pool<typename object_seq_type::Node>` | private | Typedef for a pool of list nodes for the object linked list. |
| `d_volatile_object_pool` | field | `volatile_object_pool_type` | private | Used to allocate volatile objects. |
| `d_object_seq_node_pool` | field | `object_seq_node_pool_type` | private | Used to allocate linked list nodes for the object list. |
| `d_objects_in_use` | field | `object_seq_type` | private | List of cached objects that are currently being used (ie, clients have shared pointers to them) - these are ordered from least-recently to most-recently requested. |
| `d_objects_not_in_use` | field | `object_seq_type` | private | List of cached objects that are \*not\* currently being used - these are also ordered from least-recently to most-recently returned. |
| `d_num_objects_allocated` | field | `std::size_t` | private | — |
| `d_min_num_objects` | field | `std::size_t` | private | — |
| `d_num_objects_in_use` | field | `std::size_t` | private | The current number of objects in use by clients (volatile references). |
| `ObjectCache( std::size_t min_num_objects)` | constructor | `None` | private | Constructor. |
| `recycle_an_unused_object()` | method | `typename object_seq_type::Node` | private | Returns true if we were able to recycle an existing object. |
| `return_cached_object_to_client( typename object_seq_type::Node &cached_object_iter)` | method | `object_shared_ptr_type` | private | — |
| `return_cached_object_from_clients( const object_shared_ptr_type &cached_object, typename object_seq_type::Node *cached_object_iter)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_OBJECTCACHE_H` | macro | `None` | — |

## Notes

- Not thread-safe: there is no internal locking, so a cache (and its `VolatileObject`s) must not be shared across threads without external synchronization.
- A `VolatileObject`'s reference can be invalidated at any time by another allocation stealing its object; always re-check `get_cached_object()` before use rather than caching the returned pointer across calls.
- `ObjectCache` owns itself via `enable_shared_from_this`, and `VolatileObject` deliberately holds a raw (not shared) pointer back to it to avoid an ownership cycle — the cache outlives its cached objects' custom deleters via a weak reference instead.
- With the default `min_num_objects = 1`, the cache never recycles until at least one object is allocated and returned; recycling only starts once the object count would otherwise exceed `min_num_objects`.
- Exceptions thrown from an optional `return_object_to_cache_function` callback are caught and logged with `qWarning()` inside `ObjectDeleter`, not propagated, since they fire from a destructor path.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLAgeGridMaskSource](../opengl/GLAgeGridMaskSource.md) | opengl | 29 |
| [opengl/GLMultiResolutionRaster](../opengl/GLMultiResolutionRaster.md) | opengl | 29 |
| [opengl/GLContext](../opengl/GLContext.md) | opengl | 22 |
| [opengl/GLVisualRasterSource](../opengl/GLVisualRasterSource.md) | opengl | 17 |
| [opengl/GLMultiResolutionCubeRaster](../opengl/GLMultiResolutionCubeRaster.md) | opengl | 14 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](../opengl/GLMultiResolutionCubeReconstructedRaster.md) | opengl | 14 |
| [scribe/TranscriptionScribeContext](../scribe/TranscriptionScribeContext.md) | scribe | 12 |
| [opengl/GLCubeSubdivisionCache](../opengl/GLCubeSubdivisionCache.md) | opengl | 10 |
| [opengl/GLNormalMapSource](../opengl/GLNormalMapSource.md) | opengl | 5 |
| [opengl/GLStateStore](../opengl/GLStateStore.md) | opengl | 4 |
| [scribe/Transcription](../scribe/Transcription.md) | scribe | 3 |
| [opengl/GLLight](../opengl/GLLight.md) | opengl | 1 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](../opengl/GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 1 |
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 1 |
| [opengl/GLScalarFieldDepthLayersSource](../opengl/GLScalarFieldDepthLayersSource.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/ObjectCache.h
python scripts/gpq.py def GPlatesUtils::ObjectCache --body
python scripts/gpq.py uses ObjectCache --kind class
python scripts/gpq.py hier ObjectCache
```

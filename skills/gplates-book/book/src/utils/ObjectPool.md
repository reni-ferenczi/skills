# ObjectPool

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1181 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/ObjectPool.h` | C++ | 534 |

## Overview

A header-only wrapper around `boost::object_pool` that exists for one reason:
`boost::object_pool::destroy()` is O(N), because boost keeps its free list ordered
by address so the pool destructor can tell which slots the client already freed.
That makes `boost::object_pool` a fine bump allocator but a poor one to return
objects to individually. `ObjectPool` keeps boost's fast allocation and adds an
O(1) `release()`. The class comment carries the profiling that drove the design —
the older hand-written implementation allocated at 60 cycles versus boost's 20,
which is why this is a wrapper today rather than a from-scratch allocator.

The trick is that `release()` never gives memory back to `boost::object_pool` at
all. Each slot is an `ObjectWrapper`, which is nothing but a
`boost::optional<ObjectType>`; releasing sets that optional to `boost::none` —
running the object's destructor — and pushes the still-allocated slot onto an
intrusive free list, where the next `add()` will reuse it. The `boost::optional`
is also what lets `ObjectType` be neither copy-constructible nor
copy-assignable: `add(boost::in_place(a, b, c))` forwards constructor arguments
straight into the slot, on both the fresh-allocation path (placement new under a
`Loki::ScopeGuard`) and the reuse path (`optional`'s in-place-factory
assignment). `ObjectPtr` exists purely to hide that optional; it is the size of a
raw pointer, non-owning, and `SafeBool`-testable.

The heaviest consumer is `GPlatesOpenGL::GLStateSetStore`, which holds one
`ObjectPool` per `GLStateSet` subclass — roughly seventy of them — and
`GPlatesOpenGL::GLState` allocates from them via `add_with_auto_release` on the
per-draw-call path, which is exactly the workload the O(1) release was written
for. `GPlatesUtils::ObjectCache` is a good illustration of the boundary: it uses
`ObjectPool` for its volatile-object handles, which are released individually,
but drops to `boost::object_pool` directly for its list nodes with a comment
saying so, since those are only ever freed en masse.

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

- **`ObjectPtr` does not own anything.** It dangles the moment the pool is
  destroyed, `clear()` is called, or the object is `release()`d. The pool must
  outlive every pointer handed out — and for `add_with_auto_release`, every
  `shared_ptr`, since `ReturnObjectToPoolDeleter` stores a raw `ObjectPool *` and
  will call `release()` on a dead pool otherwise. `clear()` is worse than the
  destructor here: it leaves the pool alive and reusable while silently
  invalidating every outstanding pointer.
- **`release()` validates almost nothing.** The only check is that
  `d_num_objects != 0`. It does not verify that the pointer came from this pool,
  nor that it has not already been released. A double release pushes the same
  slot onto the free list twice, and two later `add()` calls then hand out
  pointers to the same object.
- **That check is a `GPlatesGlobal::Assert`, which aborts in debug builds and
  throws `PreconditionViolationError` otherwise** — from a path reachable inside
  a `shared_ptr` deleter, and therefore potentially inside a destructor.
- **Allocation failure in `release()` is swallowed on purpose.** If the free-list
  node cannot be allocated, the comment explains that the release request is
  silently ignored rather than throwing from a possible destructor. The object is
  destroyed and `d_num_objects` decremented, but the slot never returns to the
  free list.
- **The reuse path in `add()` is not exception-safe.** The fresh-allocation path
  is guarded by `Loki::ScopeGuard`, but on the reuse path the node is popped off
  `d_object_free_list` (and pushed to `d_free_list_node_free_list`) *before*
  `free_list_object->object = in_place_factory`. If `ObjectType`'s constructor
  throws there, the slot is off both lists and unreachable until the pool is
  cleared or destroyed.
- **The two free lists share the same `next` pointers**, since `FreeListNode`
  inherits `IntrusiveSinglyLinkedList<FreeListNode>::Node`. That is why `add()`
  must pop from one list before pushing to the other; reordering those two lines
  corrupts both lists. The in-line comment says as much.
- **`size()` counts live objects, not memory.** Released slots stay allocated and
  are not reflected in `size()` or `empty()`, so a pool that reports empty may
  still be holding every slot it ever allocated. Only `clear()` or destruction
  returns memory.
- **Not thread safe.** No synchronisation, and `boost::object_pool` provides
  none either. A pool must belong to one thread.
- **Space cost:** 4 bytes per object for the `boost::optional` flag, plus a
  `FreeListNode` per released slot — the "up to an extra 8 bytes" in the class
  comment.
- `ObjectPtr::operator*`, `operator->` and `get()` dereference without a null
  check; only `get_ptr()` tolerates a default-constructed pointer.

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

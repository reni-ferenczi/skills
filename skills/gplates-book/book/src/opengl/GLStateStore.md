# GLStateStore

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1289 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLStateStore.h` | C++ | 126 |
| `src/opengl/GLStateStore.cc` | C++ | 72 |

## Overview

`GLStateStore` manages a pool of `GLState` objects, which snapshot the global OpenGL render state at a point in time. It reuses recycled instances when possible and creates new ones on demand, reducing allocation pressure. When a `GLState` object is deallocated, `clear()` is called on it and it returns to the pool for reuse.

The store optimizes memory across potentially thousands of `GLState` instances by sharing constant `SharedData` — which holds capabilities information and state-set metadata — so each instance only tracks which state sets it has modified, not the entire static configuration. This significantly reduces per-object memory overhead.

`GLStateStore` is owned by `GLContext` and used by `GLRenderer` to snapshot OpenGL state during rendering operations.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLStateStore`](#gplatesopenglglstatestore) | class | `boost::enable_shared_from_this<GLStateStore>`<br>`boost::noncopyable` | — | 0 | Manages allocation of derived GLState classes using an object cache. |

## Members

### `GPlatesOpenGL::GLStateStore`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GLStateStore>` | public | A convenience typedef for a shared pointer to a GLStateStore. |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GLStateStore>` | public | — |
| `weak_ptr_type` | typedef | `boost::weak_ptr<GLStateStore>` | public | A convenience typedef for a weak pointer to a GLStateStore. |
| `weak_ptr_to_const_type` | typedef | `boost::weak_ptr<const GLStateStore>` | public | — |
| `create( const GLCapabilities &capabilities, const GLStateSetStore::non_null_ptr_type &state_set_store, const GLStateSetKeys::non_null_ptr_to_const_type &state_set_keys)` | method | `shared_ptr_type` | public | Creates a GLStateStore object. |
| `allocate_state()` | method | `GLState::shared_ptr_type` | public | Allocates a GLState object (that contains no state sets). |
| `state_cache_type` | typedef | `GPlatesUtils::ObjectCache<GLState>` | private | Typedef for an object cache of GLState objects. |
| `d_state_set_store` | field | `GLStateSetStore::non_null_ptr_type` | private | Used by GLState objects to efficiently allocate its state-set objects. |
| `d_state_set_keys` | field | `GLStateSetKeys::non_null_ptr_to_const_type` | private | Used by GLState objects to determine state-set slots. |
| `d_state_shared_data` | field | `GLState::SharedData::shared_ptr_type` | private | Constant data shared by instances of GLState allocated by us. |
| `d_state_cache` | field | `state_cache_type::shared_ptr_type` | private | Cache of GLState objects. |
| `GLStateStore( const GLCapabilities &capabilities, const GLStateSetStore::non_null_ptr_type &state_set_store, const GLStateSetKeys::non_null_ptr_to_const_type &state_set_keys)` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLSTATESTORE_H` | macro | `None` | — |

## Notes

`SharedData` is immutable and shared across all `GLState` instances allocated by a store to reduce memory consumption. When all shared pointers to a `GLState` object are destroyed, the cache invokes `GLState::clear()` before returning it to the pool, resetting it for reuse.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRenderer](GLRenderer.md) | opengl | 6 |
| [opengl/GLState](GLState.md) | opengl | 2 |
| [opengl/GLContext](GLContext.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLStateStore.h
python scripts/gpq.py def GPlatesOpenGL::GLStateStore --body
python scripts/gpq.py uses GLStateStore --kind class
python scripts/gpq.py hier GLStateStore
```

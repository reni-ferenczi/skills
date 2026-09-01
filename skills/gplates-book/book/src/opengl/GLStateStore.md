# GLStateStore

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1289 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLStateStore.h` | C++ | 126 |
| `src/opengl/GLStateStore.cc` | C++ | 72 |

## Overview

[[[PROSE overview unit=opengl/GLStateStore tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=opengl/GLStateStore tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

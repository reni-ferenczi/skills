# GLStateSet

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 11 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLStateSet.h` | C++ | 134 |

## Overview

[[[PROSE overview unit=opengl/GLStateSet tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLStateSet`](#gplatesopenglglstateset) | class | `boost::noncopyable` | — | 44 | Base class for setting any OpenGL \*global\* state - together all the individual state sets form the complete OpenGL global state. |

## Members

### `GPlatesOpenGL::GLStateSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~GLStateSet()` | destructor | `None` | public | — |
| `apply_state( const GLCapabilities &capabilities, const GLStateSet &last_applied_state_set, GLState &last_applied_state)` | method | `void` | public | Applies the internal state (of derived class instance) directly to OpenGL if a state change is detected when compared to last\_applied\_state\_set. |
| `apply_from_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | Applies the internal state (of derived class instance) directly to OpenGL \*from\* the default OpenGL state. |
| `apply_to_default_state( const GLCapabilities &capabilities, GLState &last_applied_state)` | method | `void` | public | Applies the \*default\* state directly to OpenGL \*from\* the internal state (of this derived class instance). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLSTATESET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLStateSet tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLStateSets](GLStateSets.md) | opengl | 272 |
| [opengl/GLState](GLState.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLStateSet.h
python scripts/gpq.py def GPlatesOpenGL::GLStateSet --body
python scripts/gpq.py uses GLStateSet --kind class
python scripts/gpq.py hier GLStateSet
```

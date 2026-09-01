# GLStateSet

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 11 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLStateSet.h` | C++ | 134 |

## Overview

`GLStateSet` is the abstract base for every piece of OpenGL *global* state the `opengl` module tracks — its 44 subclasses (see [`GLStateSets`](GLStateSets.md)) each represent one orthogonal slice of global state (e.g. whether `GL_BLEND` is enabled, which texture unit is active), and together they compose the complete tracked OpenGL state managed by `GLState`. It exists so that state changes can be diffed and minimised rather than reapplied wholesale on every draw call: `apply_state()` compares against the previously-applied state set of the same derived type and only issues OpenGL calls if something actually changed (or unconditionally, when detecting the difference isn't worth the cost — a redundant call is harmless). `apply_from_default_state()` and `apply_to_default_state()` handle the two directions of transitioning to and from OpenGL's built-in default for that piece of state, which matters when entering or leaving a scope that assumes a known baseline.

Deliberately out of scope here is state that lives on bindable OpenGL objects themselves (textures, buffers, etc) — that is set directly on the object, with only the *binding* of such an object to the context treated as global state and thus represented by a `GLStateSet`.

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

- All three `apply_*` methods are `const`: a `GLStateSet` instance never mutates itself when applying, so re-applying it later reproduces the same OpenGL state.
- `apply_state()`'s `last_applied_state_set` is guaranteed by the caller to be the same derived type as `this`, so implementations downcast it without a runtime type check.
- `apply_from_default_state()`/`apply_to_default_state()` each assume OpenGL is already in a specific state before the call (default, or this instance's state, respectively) — the caller, not `GLStateSet`, is responsible for that precondition holding.

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

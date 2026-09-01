# GLDepthRange

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1348 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLDepthRange.h` | C++ | 95 |

## Overview

`GLDepthRange` is a small value type holding the `glDepthRange` near/far parameters (`z_near`, `z_far`), used by `GLState`/`GLStateSets` and `GLRenderer` to track and compare depth-range state as part of the render framework's compiled state objects. Storing the values as `GPlatesMaths::real_t` rather than raw `GLclampd` gives `operator==` (and the derived `operator!=`, from `boost::equality_comparable`) an epsilon comparison instead of exact floating-point equality, so state comparisons used to decide whether a state change needs to be applied are robust to tiny floating-point differences.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLDepthRange`](#gplatesopenglgldepthrange) | class | `boost::equality_comparable<GLDepthRange>` | — | 0 | OpenGL depth range parameters. |

## Members

### `GPlatesOpenGL::GLDepthRange`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLDepthRange( GLclampd z_near = 0.0, GLclampd z_far = 1.0)` | constructor | `None` | public | Constructor. |
| `set_depth_range( GLclampd z_near = 0.0, GLclampd z_far = 1.0)` | method | `void` | public | Sets the depth range parameters. |
| `get_z_near()` | method | `GLclampd` | public | — |
| `get_z_far()` | method | `GLclampd` | public | — |
| `operator==( const GLDepthRange &other)` | operator | `bool` | public | Equality operator - and operator!= provided by boost::equality\_comparable. |
| `d_z_near` | field | `GPlatesMaths::real_t` | private | — |
| `d_z_far` | field | `GPlatesMaths::real_t` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLDEPTHRANGE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLStateSets](GLStateSets.md) | opengl | 12 |
| [opengl/GLRenderer](GLRenderer.md) | opengl | 4 |
| [opengl/GLState](GLState.md) | opengl | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLDepthRange.h
python scripts/gpq.py def GPlatesOpenGL::GLDepthRange --body
python scripts/gpq.py uses GLDepthRange --kind class
python scripts/gpq.py hier GLDepthRange
```

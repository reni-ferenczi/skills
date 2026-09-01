# PreconditionViolationError

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 3 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/global/PreconditionViolationError.h` | C++ | 63 |

## Overview

[[[PROSE overview unit=global/PreconditionViolationError tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::PreconditionViolationError`](#gplatesglobalpreconditionviolationerror) | class | [`Exception`](GPlatesException.md) | — | 14 | This is the base class of all exceptions in GPlates which are used to report that erroneous parameters were supplied to a function, violating the precondition of that function. |

## Members

### `GPlatesGlobal::PreconditionViolationError`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PreconditionViolationError( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `~PreconditionViolationError()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_PRECONDITIONVIOLATIONERROR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=global/PreconditionViolationError tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLStateSets](../opengl/GLStateSets.md) | opengl | 38 |
| [maths/PolygonOnSphere](../maths/PolygonOnSphere.md) | maths | 35 |
| [opengl/GLProgramObject](../opengl/GLProgramObject.md) | opengl | 26 |
| [app-logic/Layer](../app-logic/Layer.md) | app-logic | 24 |
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 23 |
| [opengl/GLStreamPrimitives](../opengl/GLStreamPrimitives.md) | opengl | 22 |
| [opengl/GLBufferObject](../opengl/GLBufferObject.md) | opengl | 20 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 18 |
| [app-logic/ScalarCoverageEvolution](../app-logic/ScalarCoverageEvolution.md) | app-logic | 10 |
| [gui/FeedbackOpenGLToQPainter](../gui/FeedbackOpenGLToQPainter.md) | gui | 10 |
| [opengl/GLContext](../opengl/GLContext.md) | opengl | 10 |
| [maths/DateLineWrapper](../maths/DateLineWrapper.md) | maths | 9 |
| [opengl/GLFrameBufferObject](../opengl/GLFrameBufferObject.md) | opengl | 9 |
| [opengl/GLBuffer](../opengl/GLBuffer.md) | opengl | 8 |
| [opengl/GLRenderer](../opengl/GLRenderer.md) | opengl | 8 |
| [app-logic/ReconstructGraph](../app-logic/ReconstructGraph.md) | app-logic | 7 |
| [app-logic/ReconstructGraphImpl](../app-logic/ReconstructGraphImpl.md) | app-logic | 7 |
| [app-logic/TimeSpanUtils](../app-logic/TimeSpanUtils.md) | app-logic | 7 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 7 |
| [maths/PolylineOnSphere](../maths/PolylineOnSphere.md) | maths | 7 |

*... and 138 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/PreconditionViolationError.h
python scripts/gpq.py def GPlatesGlobal::PreconditionViolationError --body
python scripts/gpq.py uses PreconditionViolationError --kind class
python scripts/gpq.py hier PreconditionViolationError
```

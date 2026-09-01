# PreconditionViolationError

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 3 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/global/PreconditionViolationError.h` | C++ | 63 |

## Overview

One of the two branch points in the GPlates exception tree. `AssertionFailureException` means the program's own internal state is broken; `PreconditionViolationError` means a caller handed a function arguments it documented as unacceptable. The distinction is purely one of intent — the class adds nothing to `Exception` except the name it returns from `exception_name()`, and it does not override `write_message`, so the base's empty default applies and the printed text is just `PreconditionViolationError:` plus the call-stack trace.

Its value is as a base class, and the subclasses show what "precondition" means in practice: geometry constructors rejecting inputs that cannot form a valid shape (`GPlatesMaths::InvalidPointsForPolylineConstructionError`, `InvalidPointsForPolygonConstructionError`, `InsufficientPointsForMultiPointConstructionError`), coordinates out of range (`GPlatesMaths::InvalidLatLonException`), degenerate maths cases (`IndeterminateArcRotationAxisException`, `UnableToIntersectEquivalentGreatCirclesException`), a time period whose begin follows its end (`GPlatesPropertyValues::GmlTimePeriod::BeginTimeLaterThanEndTimeException`), misuse of the OpenGL renderer API (`GPlatesOpenGL::GLRenderer::GLRendererAPIError`), and dereferencing a null `non_null_intrusive_ptr` (`GPlatesUtils::NullNonNullIntrusivePointerException`). Several carry extra state and override `write_message` to print it — `InvalidPointsForPolylineConstructionError` stores the `PolylineOnSphere::ConstructionParameterValidity` code that says *why* the points were rejected.

Reach for it when adding a check that validates what came in, and derive a named subclass if the caller could plausibly want to catch that specific failure and recover. Some of these genuinely are: `GPlatesMaths::InvalidLatLonException` is caught in `EditGeometryWidget`, `Dialogs` and the Python bindings to reject a coordinate the user typed, rather than being left to reach the top-level handler. Throwing the base class directly is legal but tells a handler nothing beyond the category.

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

- **`Assert` and `throw` are not interchangeable here.** `GPlatesGlobal::Assert<SomeSubclass>(...)` aborts instead of throwing on `GPLATES_DEBUG` builds, so a precondition failure that callers are expected to catch and recover from must be thrown directly — `throw InvalidPointsForPolylineConstructionError(GPLATES_EXCEPTION_SOURCE, v)`, as `PolylineOnSphere` does. Route a check through `Assert` only when reaching it is a bug that should stop a developer's build.
- Unlike `AssertionFailureException`, this class does not override `write_message`, so the base's empty default runs: with no override in your own subclass, the printed message is the exception name and the call-stack trace and nothing more.
- Unlike its sibling `AssertionFailureException`, this unit has no `.cc` — the whole class is header-inline. Adding a `write_message` that needs `<ostream>` would mean either a new translation unit or pushing the include into a header that hundreds of files pull in.
- Subclass constructors must take `const GPlatesUtils::CallStack::Trace &` first, and should declare `~Subclass() throw() {}` to match the base's exception specification.
- Every construction pays for a call-stack trace snapshot (see `GPlatesException`), so these are for rejecting bad input at an API boundary, not for routine validation inside a loop.

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

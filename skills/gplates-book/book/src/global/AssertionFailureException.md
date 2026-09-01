# AssertionFailureException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 6 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/global/AssertionFailureException.h` | C++ | 69 |
| `src/global/AssertionFailureException.cc` | C++ | 36 |

## Overview

This is the default exception type for `GPlatesGlobal::Assert`, and that is essentially all it is: a two-line subclass of `Exception` whose `write_message` writes the fixed text `"Assertion failure"`. The information that makes an assertion failure useful does not live in the class — it is the `GPlatesUtils::CallStack::Trace` that the caller passes through `GPLATES_ASSERTION_SOURCE`, which `Exception`'s constructor turns into a stored call-stack trace string. The class exists so that `Assert<AssertionFailureException>(condition, GPLATES_ASSERTION_SOURCE)` has something to instantiate, and so that the thrown object is distinguishable by type from an ordinary error.

It sits at the "the program is broken" end of the `global` exception hierarchy, opposite `PreconditionViolationError` ("the caller passed something wrong") and alongside `AbortException` (thrown by `GPlatesGlobal::Abort`). None of these are meant to be caught by name: on release builds they propagate to the `try_catch` wrapper in `GPlatesGui::GPlatesQApplication`, which catches `GPlatesGlobal::Exception`, shows the message and the recorded trace in a `QMessageBox`, logs it, and calls `qFatal`. On debug builds `Assert` never constructs this type at all — it calls `Abort`, which fires `qFatal` directly so the native debugger keeps the real stack.

You would touch this file only to change the wording of the message or to add state to assertion failures; in practice new exception types derive from `Exception` or `PreconditionViolationError` instead, and this one is used unmodified from several hundred call sites.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::AssertionFailureException`](#gplatesglobalassertionfailureexception) | class | [`Exception`](GPlatesException.md) | — | 1 | Base GPlatesGlobal::Exception class which should be used for assertion failures; these exceptions indicate something is seriously wrong with the internal state of the program. |

## Members

### `GPlatesGlobal::AssertionFailureException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AssertionFailureException( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_ASSERTIONFAILUREEXCEPTION_H` | macro | `None` | — |

## Notes

- The constructor signature is not free to change. `GPlatesGlobal::Assert` forwards `assert_location` as the first constructor argument of whatever exception type it is given, so every class in this hierarchy must take `const GPlatesUtils::CallStack::Trace &` first and any extra arguments after it.
- The huge fan-in shown below is misleading as a coupling measure. Almost all of it is `#include "global/AssertionFailureException.h"` plus repeated `Assert<AssertionFailureException>(...)` calls; nothing depends on the class's interface beyond that one constructor.
- On a `GPLATES_DEBUG` build (CMake `DEBUG` and `RELWITHDEBINFO` configurations) no instance is ever created, so anything you add here — extra state, a richer message — is invisible in exactly the builds a developer debugs with.
- `write_message` is deliberately defined in the `.cc` rather than inline, which keeps `<ostream>` out of the header; `Exception::write_string_message` exists for the same reason.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 102 |
| [opengl/GLStateSets](../opengl/GLStateSets.md) | opengl | 80 |
| [opengl/GLMultiResolutionRaster](../opengl/GLMultiResolutionRaster.md) | opengl | 62 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 61 |
| [opengl/GLRenderer](../opengl/GLRenderer.md) | opengl | 59 |
| [qt-widgets/ScalarField3DLayerOptionsWidget](../qt-widgets/ScalarField3DLayerOptionsWidget.md) | qt-widgets | 59 |
| [app-logic/FeatureCollectionFileState](../app-logic/FeatureCollectionFileState.md) | app-logic | 58 |
| [gui/Mipmapper](../gui/Mipmapper.md) | gui | 57 |
| [opengl/GLFrameBufferObject](../opengl/GLFrameBufferObject.md) | opengl | 57 |
| [app-logic/Layer](../app-logic/Layer.md) | app-logic | 54 |
| [opengl/GLProgramObject](../opengl/GLProgramObject.md) | opengl | 50 |
| [opengl/GLStreamPrimitives](../opengl/GLStreamPrimitives.md) | opengl | 46 |
| [file-io/MipmappedRasterFormatWriter](../file-io/MipmappedRasterFormatWriter.md) | file-io | 44 |
| [opengl/GLBufferObject](../opengl/GLBufferObject.md) | opengl | 44 |
| [maths/GeometryInterpolation](../maths/GeometryInterpolation.md) | maths | 43 |
| [view-operations/GeometryBuilder](../view-operations/GeometryBuilder.md) | view-operations | 43 |
| [gui/TreeWidgetBuilder](../gui/TreeWidgetBuilder.md) | gui | 40 |
| [maths/DateLineWrapper](../maths/DateLineWrapper.md) | maths | 40 |
| [app-logic/ScalarCoverageEvolution](../app-logic/ScalarCoverageEvolution.md) | app-logic | 37 |
| [file-io/GdalRasterReader](../file-io/GdalRasterReader.md) | file-io | 35 |

*... and 238 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/AssertionFailureException.h
python scripts/gpq.py def GPlatesGlobal::AssertionFailureException --body
python scripts/gpq.py uses AssertionFailureException --kind class
python scripts/gpq.py hier AssertionFailureException
```

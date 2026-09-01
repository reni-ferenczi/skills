# GPlatesAssert

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 958 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/global/GPlatesAssert.h` | C++ | 210 |
| `src/global/GPlatesAssert.cc` | C++ | 57 |

## Overview

GPlates does not use C `assert`. Every internal consistency check in the codebase goes through `GPlatesGlobal::Assert<ExceptionType>(condition, GPLATES_ASSERTION_SOURCE, ...)`, and the point of the design is that one written check has two behaviours. On a `GPLATES_DEBUG` build (CMake gives that define to the `DEBUG` and `RELWITHDEBINFO` configurations, in `src/CMakeLists.txt`) a failed check calls `Abort`, which prints the manually tracked `GPlatesUtils::CallStack` trace through `qFatal` so the process traps in the debugger with its real native stack. On a release build the same check throws `ExceptionType`, constructed with the failure location as its first argument, and that exception travels up to the `try_catch` wrapper in `GPlatesGui::GPlatesQApplication::notify`, which reports it to the user and exits. A shipped GPlates therefore fails an assertion with a dialog and a log entry rather than a silent crash, and a developer's build stops at the failure.

The condition is a deduced template parameter rather than `bool` on purpose. Boost made `operator bool` explicit on `boost::optional`, `shared_ptr` and friends under C++11, which broke the implicit conversion callers had relied on; feeding the value straight into an `if` restores it, since that context permits explicit conversion. The `ExceptionType` parameter comes first and `AssertionConditionType` last precisely so callers only ever name the exception type and let the rest deduce. The five extra overloads exist because the exception being constructed may need more than a location — the trailing `arg1 … arg5` are forwarded verbatim to its constructor, which is why every class under `GPlatesGlobal::Exception` must order its constructor arguments with `CallStack::Trace` first.

`Abort` is the same fork without a condition: `[[noreturn]]`, `qFatal` with the call-stack trace on debug builds, `throw AbortException(abort_location)` otherwise. `GPLATES_ASSERTION_SOURCE` expands to exactly the same `CallStack::Trace(__FILE__, __LINE__)` as `GPLATES_EXCEPTION_SOURCE` in `GPlatesException.h`; the two names are a readability convention, not a functional distinction.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_GLOBAL_ASSERT_H_` | macro | `None` | — |
| `GPLATES_ASSERTION_SOURCE` | macro | `GPlatesUtils::CallStack::Trace(__FILE__, __LINE__)` | — |
| `Abort( const GPlatesUtils::CallStack::Trace &abort_location)` | function | `void` | Outputs the call stack contained in CallStack and then calls std::abort (if the current GPlates build is considered a debug build) or an instance of AbortException is instantiated and thrown. |
| `Assert( const AssertionConditionType &assertion, const GPlatesUtils::CallStack::Trace &assert_location)` | function | `void` | This is our new favourite Assert() statement. |
| `Assert( const AssertionConditionType &assertion, const GPlatesUtils::CallStack::Trace &assert_location, const A1 &arg1)` | function | `void` | Overloaded Assert taking one additional argument to the ExceptionType constructor. |
| `Assert( const AssertionConditionType &assertion, const GPlatesUtils::CallStack::Trace &assert_location, const A1 &arg1, const A2 &arg2)` | function | `void` | Overloaded Assert taking two additional arguments to the ExceptionType constructor. |
| `Assert( const AssertionConditionType &assertion, const GPlatesUtils::CallStack::Trace &assert_location, const A1 &arg1, const A2 &arg2, const A3 &arg3)` | function | `void` | Overloaded Assert taking three additional arguments to the ExceptionType constructor. |
| `Assert( const AssertionConditionType &assertion, const GPlatesUtils::CallStack::Trace &assert_location, const A1 &arg1, const A2 &arg2, const A3 &arg3, const A4 &arg4)` | function | `void` | Overloaded Assert taking four additional arguments to the ExceptionType constructor. |
| `Assert( const AssertionConditionType &assertion, const GPlatesUtils::CallStack::Trace &assert_location, const A1 &arg1, const A2 &arg2, const A3 &arg3, const A4 &arg4, const A5 &arg5)` | function | `void` | Overloaded Assert taking five additional arguments to the ExceptionType constructor. |

## Notes

- **Assertions are never compiled out.** `Assert` is a function, not a macro, so the condition — and every extra argument you pass for the exception constructor — is evaluated on every call in every build configuration. Do not put an expensive check, and never put a side effect, inside the condition or the arguments on the assumption that release builds skip it. In debug builds the arguments are evaluated and then discarded with `(void)`.
- **The exception type is ignored in debug builds.** `Assert<Foo>(...)` aborts rather than throwing when `GPLATES_DEBUG` is defined, so any code that catches `Foo` and recovers is dead in debug and live in release. This also means `RELWITHDEBINFO` behaves like debug here, not like release — a failing assertion aborts a `RELWITHDEBINFO` build.
- **Interaction with the top-level handler.** `GPlatesQApplication`'s `try_catch` deliberately does *not* catch (apart from `NeedExitException`) under `GPLATES_DEBUG`, so the two halves line up: debug builds neither throw from `Assert` nor swallow anything else.
- The `ExceptionType` template argument is not constrained. Anything constructible from `(CallStack::Trace, args...)` compiles, but only classes derived from `GPlatesGlobal::Exception` will be recognised by the top-level handler and carry a call-stack trace.
- `Abort`'s Doxygen says it "calls `std::abort`"; the code calls Qt's `qFatal`, which routes through the installed message handler before terminating.
- The debug path builds its trace from the manually maintained `GPlatesUtils::CallStack` singleton, which only contains frames explicitly marked with `TRACK_CALL_STACK()`. Expect a very sparse trace, not a real stack.
- Header guard is `_GPLATES_GLOBAL_ASSERT_H_`, which does not match the `GPLATES_GLOBAL_*` convention used by the rest of the module.

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/Scribe](../scribe/Scribe.md) | scribe | 163 |
| [maths/PolygonOnSphere](../maths/PolygonOnSphere.md) | maths | 127 |
| [opengl/GLRenderer](../opengl/GLRenderer.md) | opengl | 90 |
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 87 |
| [opengl/GLStateSets](../opengl/GLStateSets.md) | opengl | 85 |
| [scribe/Transcription](../scribe/Transcription.md) | scribe | 85 |
| [scribe/TranscriptionScribeContext](../scribe/TranscriptionScribeContext.md) | scribe | 64 |
| [opengl/GLFrameBufferObject](../opengl/GLFrameBufferObject.md) | opengl | 57 |
| [app-logic/Layer](../app-logic/Layer.md) | app-logic | 54 |
| [opengl/GLBufferObject](../opengl/GLBufferObject.md) | opengl | 52 |
| [opengl/GLProgramObject](../opengl/GLProgramObject.md) | opengl | 52 |
| [opengl/GLMultiResolutionRaster](../opengl/GLMultiResolutionRaster.md) | opengl | 46 |
| [opengl/GLContext](../opengl/GLContext.md) | opengl | 45 |
| [opengl/GLStreamPrimitives](../opengl/GLStreamPrimitives.md) | opengl | 45 |
| [qt-widgets/ScalarField3DLayerOptionsWidget](../qt-widgets/ScalarField3DLayerOptionsWidget.md) | qt-widgets | 45 |
| [gui/FeedbackOpenGLToQPainter](../gui/FeedbackOpenGLToQPainter.md) | gui | 42 |
| [gui/Mipmapper](../gui/Mipmapper.md) | gui | 41 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 41 |
| [app-logic/FeatureCollectionFileState](../app-logic/FeatureCollectionFileState.md) | app-logic | 40 |
| [maths/DateLineWrapper](../maths/DateLineWrapper.md) | maths | 40 |

*... and 338 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/GPlatesAssert.h
```

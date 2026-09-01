# GPlatesAssert

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 958 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/global/GPlatesAssert.h` | C++ | 210 |
| `src/global/GPlatesAssert.cc` | C++ | 57 |

## Overview

[[[PROSE overview unit=global/GPlatesAssert tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=global/GPlatesAssert tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

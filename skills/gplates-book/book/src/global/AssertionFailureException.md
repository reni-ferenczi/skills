# AssertionFailureException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 6 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/global/AssertionFailureException.h` | C++ | 69 |
| `src/global/AssertionFailureException.cc` | C++ | 36 |

## Overview

[[[PROSE overview unit=global/AssertionFailureException tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=global/AssertionFailureException tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

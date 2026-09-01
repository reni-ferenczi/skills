# NullIntrusivePointerHandler

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1400 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/NullIntrusivePointerHandler.h` | C++ | 47 |
| `src/utils/NullIntrusivePointerHandler.cc` | C++ | 43 |

## Overview

`NullIntrusivePointerHandler` is a stateless functor that reports an attempt
to construct or assign a null value into a non-nullable intrusive-pointer
type such as `non_null_intrusive_ptr`. Calling `operator()()` is the "you
tried to make me null" hook that such a smart pointer's implementation
invokes instead of silently accepting a null raw pointer; the handler's job
is only to fail loudly, not to do anything with a pointer value itself, which
is why it takes no arguments and holds no state. This is the failure policy
half of the intrusive-pointer machinery that most of the codebase's
`non_null_ptr_to_const_type`/`non_null_ptr_type` typedefs are built on, which
explains why it is referenced from so many otherwise unrelated units.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::NullIntrusivePointerHandler`](#gplatesutilsnullintrusivepointerhandler) | class | — | — | 0 | — |

## Members

### `GPlatesUtils::NullIntrusivePointerHandler`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NullIntrusivePointerHandler()` | constructor | `None` | public | — |
| `~NullIntrusivePointerHandler()` | destructor | `None` | public | — |
| `operator()()` | operator | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator()()` | operator | `void` | — |
| `GPLATES_UTILS_NULLINTRUSIVEPOINTERHANDLER_H` | macro | `None` | — |

## Notes

`operator()()`'s behaviour depends on the build: in a `GPLATES_DEBUG` build it
calls `GPlatesGlobal::Abort` so the failure shows up as a live stack trace in
a debugger, while in a release build it instead throws
`NullNonNullIntrusivePointerException`. Code that calls this handler must
therefore be prepared for either an abort or a C++ exception depending on the
build configuration, not just one of the two.

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/FiniteRotation](../maths/FiniteRotation.md) | maths | 12 |
| [file-io/GpmlFeatureReaderImpl](../file-io/GpmlFeatureReaderImpl.md) | file-io | 11 |
| [gui/deprecated/FeatureWeakRefSequence](../gui/deprecated/FeatureWeakRefSequence.md) | gui | 7 |
| [model/XmlNode](../model/XmlNode.md) | model | 7 |
| [maths/ProximityHitDetail](../maths/ProximityHitDetail.md) | maths | 5 |
| [app-logic/MultiPointVectorField](../app-logic/MultiPointVectorField.md) | app-logic | 4 |
| [maths/GeometryOnSphere](../maths/GeometryOnSphere.md) | maths | 4 |
| [property-values/Georeferencing](../property-values/Georeferencing.md) | property-values | 4 |
| [app-logic/ReconstructMethodFiniteRotation](../app-logic/ReconstructMethodFiniteRotation.md) | app-logic | 3 |
| [app-logic/ReconstructionGraph](../app-logic/ReconstructionGraph.md) | app-logic | 3 |
| [app-logic/ReconstructionTree](../app-logic/ReconstructionTree.md) | app-logic | 3 |
| [model/PropertyValue](../model/PropertyValue.md) | model | 3 |
| [model/TopLevelProperty](../model/TopLevelProperty.md) | model | 3 |
| [opengl/GLCompiledDrawState](../opengl/GLCompiledDrawState.md) | opengl | 3 |
| [opengl/GLObjectResource](../opengl/GLObjectResource.md) | opengl | 3 |
| [opengl/GLTransform](../opengl/GLTransform.md) | opengl | 3 |
| [presentation/VisualLayerParams](../presentation/VisualLayerParams.md) | presentation | 3 |
| [property-values/CoordinateTransformation](../property-values/CoordinateTransformation.md) | property-values | 3 |
| [property-values/SpatialReferenceSystem](../property-values/SpatialReferenceSystem.md) | property-values | 3 |
| [app-logic/ReconstructMethodByPlateId](../app-logic/ReconstructMethodByPlateId.md) | app-logic | 2 |

*... and 38 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/NullIntrusivePointerHandler.h
python scripts/gpq.py def GPlatesUtils::NullIntrusivePointerHandler --body
python scripts/gpq.py uses NullIntrusivePointerHandler --kind class
python scripts/gpq.py hier NullIntrusivePointerHandler
```

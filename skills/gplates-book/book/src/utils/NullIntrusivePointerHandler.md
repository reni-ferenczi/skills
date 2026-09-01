# NullIntrusivePointerHandler

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1400 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/NullIntrusivePointerHandler.h` | C++ | 47 |
| `src/utils/NullIntrusivePointerHandler.cc` | C++ | 43 |

## Overview

[[[PROSE overview unit=utils/NullIntrusivePointerHandler tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=utils/NullIntrusivePointerHandler tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

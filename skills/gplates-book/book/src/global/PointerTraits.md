# PointerTraits

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 138 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/global/PointerTraits.h` | C++ | 89 |

## Overview

[[[PROSE overview unit=global/PointerTraits tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::PointerTraitsInternal::PointerTraitsBase`](#gplatesglobalpointertraitsinternalpointertraitsbase) | struct | — | `<class T>` | 1 | — |
| [`GPlatesGlobal::PointerTraits`](#gplatesglobalpointertraits) | struct | [`PointerTraitsInternal::PointerTraitsBase<T>`](PointerTraits.md) | `<class T>` | 0 | PointerTraits provides type information about smart pointers to GPlates objects. |

## Members

### `GPlatesGlobal::PointerTraitsInternal::PointerTraitsBase`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<T>` | public | — |

### `GPlatesGlobal::PointerTraits`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_POINTERTRAITS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=global/PointerTraits tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [model/BasicHandle](../model/BasicHandle.md) | model | 46 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 25 |
| [model/FeatureHandle](../model/FeatureHandle.md) | model | 23 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 20 |
| [property-values/RawRasterUtils](../property-values/RawRasterUtils.md) | property-values | 17 |
| [model/TopLevelPropertyRef](../model/TopLevelPropertyRef.md) | model | 16 |
| [model/BasicRevision](../model/BasicRevision.md) | model | 15 |
| [model/HandleTraits](../model/HandleTraits.md) | model | 15 |
| [file-io/RasterBandReader](../file-io/RasterBandReader.md) | file-io | 13 |
| [model/TopLevelPropertyInline](../model/TopLevelPropertyInline.md) | model | 13 |
| [app-logic/DependentTopologicalSectionLayers](../app-logic/DependentTopologicalSectionLayers.md) | app-logic | 11 |
| [model/FeatureRevision](../model/FeatureRevision.md) | model | 10 |
| [qt-widgets/GlobeAndMapWidget](../qt-widgets/GlobeAndMapWidget.md) | qt-widgets | 10 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 8 |
| [feature-visitors/FromQvariantConverter](../feature-visitors/FromQvariantConverter.md) | feature-visitors | 8 |
| [opengl/GLMultiResolutionRaster](../opengl/GLMultiResolutionRaster.md) | opengl | 8 |
| [opengl/GLOffScreenContext](../opengl/GLOffScreenContext.md) | opengl | 8 |
| [property-values/GpmlTimeSample](../property-values/GpmlTimeSample.md) | property-values | 8 |
| [property-values/GpmlTimeWindow](../property-values/GpmlTimeWindow.md) | property-values | 8 |
| [qt-widgets/CreateFeaturePropertiesPage](../qt-widgets/CreateFeaturePropertiesPage.md) | qt-widgets | 7 |

*... and 78 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/PointerTraits.h
python scripts/gpq.py def GPlatesGlobal::PointerTraits --body
python scripts/gpq.py uses PointerTraits --kind struct
python scripts/gpq.py hier PointerTraits
```

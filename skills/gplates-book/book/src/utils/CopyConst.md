# CopyConst

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 12 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/CopyConst.h` | C++ | 52 |

## Overview

`GPlatesUtils::CopyConst<SrcType, DstType>` is a small compile-time trait
that transfers the const-qualification of `SrcType` onto `DstType`: its
`::type` member is `DstType` with any `const` stripped, unless `SrcType` is
itself `const`, in which case the partial specialisation adds `const` to
`DstType` instead. It is the standard trick for writing a single template
that generates both a const and non-const variant of a visitor or accessor —
most visibly the const/non-const pairs of `FeatureVisitor`,
`ReconstructionGeometryVisitor` and `LayerProxyVisitor`, where a shared
template parameter for "the type being visited" needs to propagate its
const-ness into the visitor's return or parameter types without duplicating
the whole class.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::CopyConst`](#gplatesutilscopyconst) | struct | — | `<class SrcType, class DstType>` | 0 | CopyConst takes the const-ness of SrcType and applies it to DstType. |
| [`GPlatesUtils::CopyConst<const SrcType, DstType>`](#gplatesutilscopyconstconst-srctype-dsttype) | struct | — | `<class SrcType, class DstType>` | 0 | — |

## Members

### `GPlatesUtils::CopyConst`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `typename boost::remove_const<DstType>::type` | public | — |

### `GPlatesUtils::CopyConst<const SrcType, DstType>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `typename boost::add_const<DstType>::type` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_COPYCONST_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructionGeometryVisitor](../app-logic/ReconstructionGeometryVisitor.md) | app-logic | 75 |
| [app-logic/ReconstructionGeometryUtils](../app-logic/ReconstructionGeometryUtils.md) | app-logic | 49 |
| [model/FeatureVisitor](../model/FeatureVisitor.md) | model | 45 |
| [app-logic/LayerProxyVisitor](../app-logic/LayerProxyVisitor.md) | app-logic | 37 |
| [utils/SmartNodeLinkedList_test](SmartNodeLinkedList_test.md) | utils | 18 |
| [maths/CubeQuadTree](../maths/CubeQuadTree.md) | maths | 12 |
| [file-io/FeatureCollectionFileFormatConfiguration](../file-io/FeatureCollectionFileFormatConfiguration.md) | file-io | 9 |
| [presentation/LayerOutputRenderer](../presentation/LayerOutputRenderer.md) | presentation | 9 |
| [feature-visitors/PropertyValueFinder](../feature-visitors/PropertyValueFinder.md) | feature-visitors | 8 |
| [maths/CubeQuadTreePartition](../maths/CubeQuadTreePartition.md) | maths | 8 |
| [opengl/GLCubeSubdivisionCache](../opengl/GLCubeSubdivisionCache.md) | opengl | 8 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 7 |
| [app-logic/CoRegistrationLayerProxy](../app-logic/CoRegistrationLayerProxy.md) | app-logic | 6 |
| [app-logic/CoRegistrationLayerTask](../app-logic/CoRegistrationLayerTask.md) | app-logic | 6 |
| [app-logic/ReconstructMethodHalfStageRotation](../app-logic/ReconstructMethodHalfStageRotation.md) | app-logic | 6 |
| [app-logic/ReconstructionLayerProxy](../app-logic/ReconstructionLayerProxy.md) | app-logic | 6 |
| [app-logic/ResolvedTopologicalBoundary](../app-logic/ResolvedTopologicalBoundary.md) | app-logic | 6 |
| [app-logic/FlowlineUtils](../app-logic/FlowlineUtils.md) | app-logic | 5 |
| [app-logic/LayerProxy](../app-logic/LayerProxy.md) | app-logic | 5 |
| [app-logic/ReconstructMethodVirtualGeomagneticPole](../app-logic/ReconstructMethodVirtualGeomagneticPole.md) | app-logic | 5 |

*... and 26 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/CopyConst.h
python scripts/gpq.py def GPlatesUtils::CopyConst --body
python scripts/gpq.py uses CopyConst --kind struct
python scripts/gpq.py hier CopyConst
```

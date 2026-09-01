# ResolvedScalarField3D

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1475 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ResolvedScalarField3D.h` | C++ | 148 |
| `src/app-logic/ResolvedScalarField3D.cc` | C++ | 67 |

## Overview

[[[PROSE overview unit=app-logic/ResolvedScalarField3D tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ResolvedScalarField3D`](#gplatesapplogicresolvedscalarfield3d) | class | [`ReconstructionGeometry`](ReconstructionGeometry.md)<br>[`GPlatesModel::WeakObserver<GPlatesModel::FeatureHandle>`](../model/WeakObserver.md) | — | 0 | A type of ReconstructionGeometry representing a 3D scalar field. |

## Members

### `GPlatesAppLogic::ResolvedScalarField3D`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ResolvedScalarField3D>` | public | A convenience typedef for a shared pointer to a non-const ResolvedScalarField3D. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ResolvedScalarField3D>` | public | A convenience typedef for a shared pointer to a non-const ResolvedScalarField3D. |
| `WeakObserverType` | typedef | `GPlatesModel::WeakObserver<GPlatesModel::FeatureHandle>` | public | A convenience typedef for the WeakObserver base class of this class. |
| `create( GPlatesModel::FeatureHandle &feature_handle, const double &reconstruction_time, const ScalarField3DLayerProxy::non_null_ptr_type &scalar_field_layer_proxy)` | method | `non_null_ptr_type` | public | Create a ResolvedScalarField3D. |
| `accept_visitor( ConstReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ConstReconstructionGeometryVisitor instance. |
| `accept_visitor( ReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ReconstructionGeometryVisitor instance. |
| `accept_weak_observer_visitor( GPlatesModel::WeakObserverVisitor<GPlatesModel::FeatureHandle> &visitor)` | method | `void` | public | Accept a WeakObserverVisitor instance. |
| `ResolvedScalarField3D( GPlatesModel::FeatureHandle &feature_handle, const double &reconstruction_time, const ScalarField3DLayerProxy::non_null_ptr_type &scalar_field_layer_proxy)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_reconstruction_time` | field | `double` | private | The reconstruction time at which scalar field is resolved/reconstructed. |
| `d_scalar_field_layer_proxy` | field | `ScalarField3DLayerProxy::non_null_ptr_type` | private | The scalar field layer proxy. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RESOLVEDSCALARFIELD3D_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ResolvedScalarField3D tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 11 |
| [view-operations/RenderedResolvedScalarField3D](../view-operations/RenderedResolvedScalarField3D.md) | view-operations | 4 |
| [view-operations/RenderedGeometryFactory](../view-operations/RenderedGeometryFactory.md) | view-operations | 2 |
| [app-logic/ScalarField3DLayerProxy](ScalarField3DLayerProxy.md) | app-logic | 1 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 1 |
| [presentation/LayerOutputRenderer](../presentation/LayerOutputRenderer.md) | presentation | 1 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ResolvedScalarField3D.h
python scripts/gpq.py def GPlatesAppLogic::ResolvedScalarField3D --body
python scripts/gpq.py uses ResolvedScalarField3D --kind class
python scripts/gpq.py hier ResolvedScalarField3D
```

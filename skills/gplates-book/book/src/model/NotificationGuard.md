# NotificationGuard

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 1207 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/NotificationGuard.h` | C++ | 113 |
| `src/model/NotificationGuard.cc` | C++ | 92 |

## Overview

`NotificationGuard` is the RAII handle for `Model`'s notification-batching
mechanism: acquiring one increments the model's guard count, and releasing one
(explicitly via `release_guard()`, or implicitly in the destructor) decrements
it. While the count is above zero, `Handle`-derived objects in the model queue
their modification, deactivation and reactivation notifications instead of
firing them straight away, and repeated notifications of the same kind from the
same handle collapse into one — so code that makes several related edits (for
example, modifying a feature and adding another to the same collection) wraps
them in a guard to have listeners see one merged update instead of several.

The `boost::optional<Model&>` constructor exists because many model-data query
functions already carry an optional model reference; passing `boost::none`
through makes the guard a no-op rather than forcing every caller to branch on
whether a model is present. `acquire_guard()`/`release_guard()` are idempotent —
calling either while already in that state does nothing — which lets a caller
temporarily lift the block (to let queued notifications flow before a small
section of code) and then reinstate it with the same object.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::NotificationGuard`](#gplatesmodelnotificationguard) | class | `boost::noncopyable` | — | 0 | NotificationGuard is a RAII class that blocks notifications from model Handles while active. |

## Members

### `GPlatesModel::NotificationGuard`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NotificationGuard( Model &model)` | constructor | `None` | public | — |
| `NotificationGuard( boost::optional<Model &> model)` | constructor | `None` | public | Constructor provided as a convenience since a lot of model data queries supply an optional model. |
| `~NotificationGuard()` | destructor | `None` | public | — |
| `release_guard()` | method | `void` | public | Releases this guard early. |
| `acquire_guard()` | method | `void` | public | Acquires this guard (if it has been released). |
| `d_model` | field | `boost::optional<Model &>` | private | — |
| `d_guard_released` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_NOTIFICATIONGUARD_H` | macro | `None` | — |

## Notes

Notifications about a handle's impending C++ destruction are always sent
immediately, regardless of any active guard. The destructor calls
`release_guard()` inside a `try`/`catch(...)` that swallows any exception, since a
destructor must not let one escape — so a failure while flushing queued
notifications is silently dropped rather than propagated. The class is
noncopyable, since copying would leave two guards independently tracking the
same acquire/release state against one model.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/AssignReconstructionPlateIdsDialog](../qt-widgets/AssignReconstructionPlateIdsDialog.md) | qt-widgets | 5 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 4 |
| [qt-widgets/ApplyReconstructionPoleAdjustmentDialog](../qt-widgets/ApplyReconstructionPoleAdjustmentDialog.md) | qt-widgets | 3 |
| [view-operations/SplitFeatureUndoCommand](../view-operations/SplitFeatureUndoCommand.md) | view-operations | 3 |
| [app-logic/ApplicationState](../app-logic/ApplicationState.md) | app-logic | 2 |
| [app-logic/AssignPlateIds](../app-logic/AssignPlateIds.md) | app-logic | 2 |
| [app-logic/GenericPartitionFeatureTask](../app-logic/GenericPartitionFeatureTask.md) | app-logic | 2 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 2 |
| [file-io/GpmlFormatDeformationExport](../file-io/GpmlFormatDeformationExport.md) | file-io | 2 |
| [file-io/GpmlFormatMultiPointVectorFieldExport](../file-io/GpmlFormatMultiPointVectorFieldExport.md) | file-io | 2 |
| [file-io/GpmlFormatReconstructedScalarCoverageExport](../file-io/GpmlFormatReconstructedScalarCoverageExport.md) | file-io | 2 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 2 |
| [qt-widgets/CreateSmallCircleFeatureDialog](../qt-widgets/CreateSmallCircleFeatureDialog.md) | qt-widgets | 2 |
| [qt-widgets/CreateVGPDialog](../qt-widgets/CreateVGPDialog.md) | qt-widgets | 2 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 2 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 2 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 2 |
| [view-operations/CloneOperation](../view-operations/CloneOperation.md) | view-operations | 2 |
| [app-logic/FeatureCollectionFileIO](../app-logic/FeatureCollectionFileIO.md) | app-logic | 1 |
| [app-logic/FeatureCollectionFileState](../app-logic/FeatureCollectionFileState.md) | app-logic | 1 |

*... and 6 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/NotificationGuard.h
python scripts/gpq.py def GPlatesModel::NotificationGuard --body
python scripts/gpq.py uses NotificationGuard --kind class
python scripts/gpq.py hier NotificationGuard
```

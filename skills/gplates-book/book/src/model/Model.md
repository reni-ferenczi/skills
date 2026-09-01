# Model

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 781 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/Model.h` | C++ | 180 |
| `src/model/Model.cc` | C++ | 129 |

## Overview

[[[PROSE overview unit=model/Model tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::Model`](#gplatesmodelmodel) | class | — | — | 0 | The interface to the Model tier of GPlates. |

## Members

### `GPlatesModel::Model`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Model()` | constructor | `None` | public | Create a new instance of the Model, which contains an empty feature store. |
| `~Model()` | destructor | `None` | public | Destructor. |
| `root()` | method | `WeakReference<FeatureStoreRootHandle>` | public | Returns a (non-const) weak-ref to the model's feature store root. |
| `has_notification_guard()` | method | `bool` | public | Returns true if there are any NotificationGuard instances currently attached to the model. |
| `current_changeset_handle()` | method | `ChangesetHandle` | public | Returns the current ChangesetHandle registered with this model, or NULL if there is no current ChangesetHandle. |
| `increment_notification_guard_count()` | method | `void` | private | Increments the count of NotificationGuard instances attached to the model. |
| `decrement_notification_guard_count()` | method | `void` | private | Decrements the count of NotificationGuard instances attached to the model. |
| `register_changeset_handle( ChangesetHandle *changeset_handle)` | method | `void` | private | Registers the ChangesetHandle with this model. |
| `unregister_changeset_handle( ChangesetHandle *changeset_handle)` | method | `void` | private | Unregisters the ChangesetHandle with this model. |
| `d_root` | field | `GPlatesGlobal::PointerTraits<FeatureStoreRootHandle>::non_null_ptr_type` | private | A persistent handle to the root of the feature store, which contains all loaded feature collections and their features. |
| `d_current_changeset_handle` | field | `ChangesetHandle` | private | The current ChangesetHandle registered with this model. |
| `d_notification_guard_count` | field | `unsigned int` | private | A count of the number of NotificationGuard instances attached to this model. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_MODEL_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=model/Model tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/FeatureCollectionFileIO](../app-logic/FeatureCollectionFileIO.md) | app-logic | 6 |
| [model/BasicHandle](BasicHandle.md) | model | 6 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 5 |
| [app-logic/FeatureCollectionFileState](../app-logic/FeatureCollectionFileState.md) | app-logic | 4 |
| [model/ChangesetHandle](ChangesetHandle.md) | model | 3 |
| [model/NotificationGuard](NotificationGuard.md) | model | 3 |
| [view-operations/SplitFeatureUndoCommand](../view-operations/SplitFeatureUndoCommand.md) | view-operations | 3 |
| [file-io/File](../file-io/File.md) | file-io | 2 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 2 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 2 |
| [qt-widgets/CreateSmallCircleFeatureDialog](../qt-widgets/CreateSmallCircleFeatureDialog.md) | qt-widgets | 2 |
| [qt-widgets/CreateVGPDialog](../qt-widgets/CreateVGPDialog.md) | qt-widgets | 2 |
| [qt-widgets/GenerateVelocityDomainCitcomsDialog](../qt-widgets/GenerateVelocityDomainCitcomsDialog.md) | qt-widgets | 2 |
| [qt-widgets/GenerateVelocityDomainLatLonDialog](../qt-widgets/GenerateVelocityDomainLatLonDialog.md) | qt-widgets | 2 |
| [qt-widgets/GenerateVelocityDomainTerraDialog](../qt-widgets/GenerateVelocityDomainTerraDialog.md) | qt-widgets | 2 |
| [unit-test/FeatureHandleTest](../unit-test/FeatureHandleTest.md) | unit-test | 2 |
| [app-logic/FlowlineUtils](../app-logic/FlowlineUtils.md) | app-logic | 1 |
| [app-logic/MotionPathUtils](../app-logic/MotionPathUtils.md) | app-logic | 1 |
| [app-logic/PlateVelocityUtils](../app-logic/PlateVelocityUtils.md) | app-logic | 1 |
| [app-logic/TopologyGeometryResolver](../app-logic/TopologyGeometryResolver.md) | app-logic | 1 |

*... and 20 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/Model.h
python scripts/gpq.py def GPlatesModel::Model --body
python scripts/gpq.py uses Model --kind class
python scripts/gpq.py hier Model
```

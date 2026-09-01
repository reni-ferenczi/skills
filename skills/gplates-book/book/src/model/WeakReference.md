# WeakReference

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 803 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/WeakReference.h` | C++ | 453 |

## Overview

[[[PROSE overview unit=model/WeakReference tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::WeakReference`](#gplatesmodelweakreference) | class | [`WeakObserver<H>`](WeakObserver.md)<br>[`GPlatesUtils::SafeBool<WeakReference<H> >`](../utils/SafeBool.md) | `<typename H>` | 0 | collected at any time. |

## Members

### `GPlatesModel::WeakReference`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `handle_type` | typedef | `H` | public | This is the type of the handle. |
| `WeakReference()` | constructor | `None` | public | Default constructor. |
| `WeakReference( handle_type &handle)` | constructor | `None` | public | Construct a reference to handle. |
| `~WeakReference()` | destructor | `None` | public | — |
| `handle_ptr()` | method | `handle_type` | public | Return the pointer to the handle. |
| `is_valid()` | method | `bool` | public | Return whether this pointer is valid to be dereferenced, and also whether the handle is active (i.e. not conceptually deleted). |
| `boolean_test()` | method | `bool` | public | Return whether this pointer is valid to be deferenced. |
| `references( const handle_type &that_handle)` | method | `bool` | public | Return whether this weak-reference references that\_handle. |
| `operator==( const WeakReference &other)` | operator | `bool` | public | Return whether this instance is equal to other. |
| `operator!=( const WeakReference &other)` | operator | `bool` | public | Return whether this instance is not equal to other. |
| `operator->()` | operator | `handle_type` | public | The pointer-indirection-member-access operator. |
| `accept_weak_observer_visitor( WeakObserverVisitor<H> &visitor)` | method | `void` | public | Accept a WeakObserverVisitor instance. |
| `attach_callback( typename WeakReferenceCallback<H>::maybe_null_ptr_type callback_)` | method | `void` | public | Attach a callback to this WeakReference. |
| `callback()` | method | `typename WeakReferenceCallback<H>::maybe_null_ptr_type` | public | Gets the callback attached to this WeakReference, if any. |
| `unattach_callback()` | method | `void` | public | Unattaches the callback, if any, from this WeakReference. |
| `publisher_modified( typename WeakReferencePublisherModifiedEvent<H>::Type type)` | method | `void` | public | Notify the callback that the publisher has been modified. |
| `publisher_added( const typename WeakReferencePublisherAddedEvent<H>::new_children_container_type &new_children)` | method | `void` | public | Notify the callback that the publisher has added new children. |
| `publisher_deactivated()` | method | `void` | public | Notify the callback that the publisher has been deactivated (conceptually deleted). |
| `publisher_reactivated()` | method | `void` | public | Notify the callback that the publisher has been reactivated (conceptually undeleted). |
| `publisher_about_to_be_destroyed()` | method | `void` | public | Notify the callback that the publisher is about to be destroyed (in the C++ sense). |
| `operator<( const WeakReference<H> &other)` | operator | `bool` | public | — |
| `d_callback` | field | `typename WeakReferenceCallback<H>::maybe_null_ptr_type` | private | An optional callback to use when publisher is modified or about to be deleted. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_WEAKREFERENCE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=model/WeakReference tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [model/WeakReferenceVisitors](WeakReferenceVisitors.md) | model | 6 |
| [model/RevisionAwareIterator](RevisionAwareIterator.md) | model | 5 |
| [app-logic/FeatureCollectionFileIO](../app-logic/FeatureCollectionFileIO.md) | app-logic | 3 |
| [app-logic/FeatureCollectionFileState](../app-logic/FeatureCollectionFileState.md) | app-logic | 3 |
| [model/ModelUtils](ModelUtils.md) | model | 3 |
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 3 |
| [api/PyCoregistrationLayerProxy](../api/PyCoregistrationLayerProxy.md) | api | 2 |
| [api/PyFeature](../api/PyFeature.md) | api | 2 |
| [app-logic/CoRegistrationLayerProxy](../app-logic/CoRegistrationLayerProxy.md) | app-logic | 2 |
| [data-mining/DataMiningUtils](../data-mining/DataMiningUtils.md) | data-mining | 2 |
| [gui/FeatureFocus](../gui/FeatureFocus.md) | gui | 2 |
| [qt-widgets/KinematicGraphsDialog](../qt-widgets/KinematicGraphsDialog.md) | qt-widgets | 2 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 2 |
| [app-logic/ApplicationState](../app-logic/ApplicationState.md) | app-logic | 1 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 1 |
| [app-logic/ReconstructGraph](../app-logic/ReconstructGraph.md) | app-logic | 1 |
| [app-logic/ReconstructGraphImpl](../app-logic/ReconstructGraphImpl.md) | app-logic | 1 |
| [app-logic/ReconstructionGeometryUtils](../app-logic/ReconstructionGeometryUtils.md) | app-logic | 1 |
| [app-logic/ScalarField3DLayerProxy](../app-logic/ScalarField3DLayerProxy.md) | app-logic | 1 |
| [data-mining/deprecated/RegionOfInterestAssociationOperator](../data-mining/deprecated/RegionOfInterestAssociationOperator.md) | data-mining | 1 |

*... and 19 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/WeakReference.h
python scripts/gpq.py def GPlatesModel::WeakReference --body
python scripts/gpq.py uses WeakReference --kind class
python scripts/gpq.py hier WeakReference
```

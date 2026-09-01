# WeakReferenceCallback

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 12 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/WeakReferenceCallback.h` | C++ | 270 |

## Overview

[[[PROSE overview unit=model/WeakReferenceCallback tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::WeakReferencePublisherModifiedEvent`](#gplatesmodelweakreferencepublishermodifiedevent) | class | — | `<typename H>` | 0 | Parameter of publisher\_modified() function in WeakReferenceCallback\<H\>. |
| [`GPlatesModel::WeakReferencePublisherAddedEvent`](#gplatesmodelweakreferencepublisheraddedevent) | class | — | `<typename H>` | 0 | Parameter of publisher\_added() function in WeakReferenceCallback\<H\>. |
| [`GPlatesModel::WeakReferencePublisherDeactivatedEvent`](#gplatesmodelweakreferencepublisherdeactivatedevent) | class | — | `<typename H>` | 0 | Parameter of publisher\_deactivated() function in WeakReferenceCallback\<H\>. |
| [`GPlatesModel::WeakReferencePublisherReactivatedEvent`](#gplatesmodelweakreferencepublisherreactivatedevent) | class | — | `<typename H>` | 0 | Parameter of publisher\_reactivated() function in WeakReferenceCallback\<H\>. |
| [`GPlatesModel::WeakReferencePublisherAboutToBeDestroyedEvent`](#gplatesmodelweakreferencepublisherabouttobedestroyedevent) | class | — | `<typename H>` | 0 | Parameter of publisher\_about\_to\_be\_destroyed() function in WeakReferenceCallback\<H\>. |
| [`GPlatesModel::WeakReferenceCallback`](#gplatesmodelweakreferencecallback) | class | [`GPlatesUtils::ReferenceCount<WeakReferenceCallback<H> >`](../utils/ReferenceCount.md) | `<typename H>` | 9 | WeakReferenceCallback instances can be attached to WeakReference instances to enable the owner of a WeakReference to receive callbacks when the WeakReference's publisher is modified, deactivated, reactivated and about to be destroyed. |

## Members

### `GPlatesModel::WeakReferencePublisherModifiedEvent`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Type` | enum | `None` | public | — |
| `WeakReferencePublisherModifiedEvent( Type type_)` | constructor | `None` | public | — |
| `type()` | method | `Type` | public | — |
| `d_type` | field | `Type` | private | — |

### `GPlatesModel::WeakReferencePublisherAddedEvent`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Traits` | struct | `None` | private | Helper traits class to choose appropriate const-ness for added children. |
| `Traits<const T>` | struct | `None` | private | — |
| `new_children_container_type` | typedef | `std::vector<typename Traits<H>::iterator>` | public | — |
| `WeakReferencePublisherAddedEvent( const new_children_container_type &new_children_)` | constructor | `None` | public | — |
| `d_new_children` | field | `new_children_container_type` | private | — |

### `GPlatesModel::WeakReferencePublisherDeactivatedEvent`

*None.*

### `GPlatesModel::WeakReferencePublisherReactivatedEvent`

*None.*

### `GPlatesModel::WeakReferencePublisherAboutToBeDestroyedEvent`

*None.*

### `GPlatesModel::WeakReferenceCallback`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `weak_reference_type` | typedef | `WeakReference<H>` | public | A convenience typedef for weak reference. |
| `maybe_null_ptr_type` | typedef | `boost::intrusive_ptr<WeakReferenceCallback<H> >` | public | A convenience typedef for boost::intrusive\_ptr\<WeakReferenceCallback\<H\> \>. |
| `modified_event_type` | typedef | `WeakReferencePublisherModifiedEvent<H>` | public | — |
| `added_event_type` | typedef | `WeakReferencePublisherAddedEvent<H>` | public | — |
| `deactivated_event_type` | typedef | `WeakReferencePublisherDeactivatedEvent<H>` | public | — |
| `reactivated_event_type` | typedef | `WeakReferencePublisherReactivatedEvent<H>` | public | — |
| `about_to_be_destroyed_event_type` | typedef | `WeakReferencePublisherAboutToBeDestroyedEvent<H>` | public | — |
| `~WeakReferenceCallback()` | destructor | `None` | public | Virtual destructor. |
| `publisher_modified( const weak_reference_type &reference, const modified_event_type &event)` | method | `void` | public | Called by WeakReference when its publisher is modified. |
| `publisher_added( const weak_reference_type &reference, const added_event_type &event)` | method | `void` | public | Called by WeakReference when its publisher has added new children. |
| `publisher_deactivated( const weak_reference_type &reference, const deactivated_event_type &event)` | method | `void` | public | Called by WeakReference when its publisher is deactivated. |
| `publisher_reactivated( const weak_reference_type &reference, const reactivated_event_type &event)` | method | `void` | public | Called by WeakReference when its publisher is reactivated. |
| `publisher_about_to_be_destroyed( const weak_reference_type &reference, const about_to_be_destroyed_event_type &event)` | method | `void` | public | Called by WeakReference when its publisher is about to be destroyed (in the C++ sense). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_WEAKREFERENCECALLBACK_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=model/WeakReferenceCallback tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [model/FeatureVisitor](FeatureVisitor.md) | model | 44 |
| [model/WeakReference](WeakReference.md) | model | 18 |
| [model/BasicHandle](BasicHandle.md) | model | 15 |
| [app-logic/FeatureCollectionFileState](../app-logic/FeatureCollectionFileState.md) | app-logic | 14 |
| [gui/UnsavedChangesTracker](../gui/UnsavedChangesTracker.md) | gui | 10 |
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 10 |
| [model/WeakReferenceVisitors](WeakReferenceVisitors.md) | model | 9 |
| [app-logic/ApplicationState](../app-logic/ApplicationState.md) | app-logic | 4 |
| [app-logic/ReconstructGraph](../app-logic/ReconstructGraph.md) | app-logic | 4 |
| [app-logic/ReconstructGraphImpl](../app-logic/ReconstructGraphImpl.md) | app-logic | 4 |
| [gui/ColourSchemeDelegator](../gui/ColourSchemeDelegator.md) | gui | 4 |
| [gui/FeatureFocus](../gui/FeatureFocus.md) | gui | 4 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 4 |
| [gui/GPlatesQApplication](../gui/GPlatesQApplication.md) | gui | 3 |
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 3 |
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 2 |
| [api/PythonRunner](../api/PythonRunner.md) | api | 1 |
| [model/FeatureCollectionHandle](FeatureCollectionHandle.md) | model | 1 |
| [model/ModelUtils](ModelUtils.md) | model | 1 |
| [qt-widgets/EditEnumerationWidget](../qt-widgets/EditEnumerationWidget.md) | qt-widgets | 1 |

*... and 2 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/WeakReferenceCallback.h
python scripts/gpq.py def GPlatesModel::WeakReferenceCallback --body
python scripts/gpq.py uses WeakReferenceCallback --kind class
python scripts/gpq.py hier WeakReferenceCallback
```

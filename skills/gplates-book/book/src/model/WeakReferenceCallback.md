# WeakReferenceCallback

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 12 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/WeakReferenceCallback.h` | C++ | 270 |

## Overview

This header defines the model's change-notification interface — the one place where
code outside `GPlatesModel` learns that a feature or a feature collection was edited,
deleted, undeleted or destroyed, without polling and without Qt signals. You
subclass `WeakReferenceCallback<H>` for `H` = `FeatureHandle` or
`FeatureCollectionHandle` (or their `const` forms), override only the events you care
about, and hand an instance to `WeakReference<H>::attach_callback`. Every override
has an empty default body, so a subclass that only wants deactivation ignores the
rest. The concrete subclasses are small local classes that forward into a larger
object: `FeatureFocus` unfocuses a feature that was deactivated,
`UnsavedChangesTracker` marks the document dirty on modification, and
`ApplicationState`, `ReconstructGraph` and `FeatureCollectionFileState` each keep a
nested callback that reacts to feature-collection changes.

The delivery path runs the other way round from the registration. `BasicHandle`
raises an event by constructing one of the `WeakReferencePublisher*Visitor` classes
in `WeakReferenceVisitors.h` and passing it to
`WeakObserverPublisher::apply_weak_observer_visitor`, which walks the intrusive chain
of `WeakObserver` links. Each `WeakReference` in that chain is visited, and only then
does it check whether it carries a callback and, if so, build the matching event
object and invoke the virtual. So a callback is reached through *its* weak reference:
if the weak reference goes out of scope, the callback is never called again, and the
`reference` argument passed to every override is the weak reference through which the
notification arrived.

The five event types are almost entirely empty — they exist to give each virtual a
distinct, extensible parameter type rather than to carry data. Only two say
anything. `WeakReferencePublisherModifiedEvent` carries a bit-pair distinguishing a
change to the publisher itself from a change to one of its children, and
`WeakReferencePublisherAddedEvent` carries the iterators of the newly added children,
using its private `Traits` specialisation to pick `const_iterator` when `H` is const.
Note the vocabulary difference the model relies on: *deactivated* means conceptually
deleted but still present for undo, while *about to be destroyed* means the C++
object is going away, typically because the undo stack was purged.

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

- **Ownership.** `WeakReferenceCallback` derives from
  `GPlatesUtils::ReferenceCount` and is held by `WeakReference` through a
  `boost::intrusive_ptr`, so the weak reference co-owns the callback and a callback
  outlives the scope it was created in. The callbacks in the tree are typically
  file-local classes holding a raw pointer or reference to a long-lived owner
  (`FeatureFocus`, `UnsavedChangesTracker`); nothing stops that owner from dying
  first, so the weak reference and its owner must have the same lifetime.
- **The callback is shared, not cloned, on copy.** `WeakReference::operator=` copies
  the `intrusive_ptr`, so two weak references end up invoking the same callback
  object — usually harmless, occasionally a surprise if the callback assumes it has
  one subscriber. The `WeakReference<H>` to `WeakReference<const H>` conversion
  operator, by contrast, deliberately drops the callback.
- **Do not store the event objects.** They are stack temporaries built inside
  `WeakReference::publisher_*` and passed by const reference; worse,
  `WeakReferencePublisherAddedEvent` holds `d_new_children` as a *reference* to a
  container owned by the caller. Copy what you need out of the event before
  returning.
- **`NotificationGuard` changes what you receive, not just when.** While a guard is
  held, `BasicHandle` accumulates notifications and `flush_pending_notifications`
  replays a coalesced version: separate publisher and child modifications arrive as a
  single `PUBLISHER_AND_CHILD_MODIFIED`, additions arrive as one batch, and a
  deactivation followed by a reactivation cancels out entirely. A callback that
  counts events, or that expects `publisher_added` once per child, will be wrong
  under a guard. `publisher_about_to_be_destroyed` is the exception — it is always
  sent immediately, guard or not.
- **State during destruction.** `BasicHandle::~BasicHandle` sends
  `publisher_about_to_be_destroyed` as its first act, so `reference.handle_ptr()` is
  still non-NULL while the derived handle is already partly destroyed. Treat that
  callback as "let go of this handle now", not as a chance to read it.
- Overrides must match the base signatures exactly, including the `const`s; because
  the bases are non-pure with empty bodies, a mistyped override compiles cleanly and
  simply never fires.
- No synchronisation: callbacks run synchronously, on the thread that performed the
  model edit, inside the mutating call.

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

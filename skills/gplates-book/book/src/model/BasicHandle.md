# BasicHandle

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 39 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/BasicHandle.h` | C++ | 1161 |
| `src/model/BasicHandle.cc` | C++ | 108 |

## Overview

[[[PROSE overview unit=model/BasicHandle tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::BasicHandle`](#gplatesmodelbasichandle) | class | [`WeakObserverPublisher<HandleType>`](WeakObserverPublisher.md)<br>[`HandleTraits<HandleType>::unsaved_changes_flag_policy`](HandleTraits.md) | `<class HandleType>` | 3 | BasicHandle contains functionality common to all Handle classes. |

## Members

### `GPlatesModel::BasicHandle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `handle_type` | typedef | `HandleType` | public | Get typedefs from HandleTraits. |
| `non_null_ptr_type` | typedef | `typename HandleTraits<handle_type>::non_null_ptr_type` | public | — |
| `non_null_ptr_to_const_type` | typedef | `typename HandleTraits<handle_type>::non_null_ptr_to_const_type` | public | — |
| `weak_ref` | typedef | `typename HandleTraits<handle_type>::weak_ref` | public | — |
| `const_weak_ref` | typedef | `typename HandleTraits<handle_type>::const_weak_ref` | public | — |
| `iterator` | typedef | `typename HandleTraits<handle_type>::iterator` | public | — |
| `const_iterator` | typedef | `typename HandleTraits<handle_type>::const_iterator` | public | — |
| `revision_type` | typedef | `typename HandleTraits<handle_type>::revision_type` | public | — |
| `parent_type` | typedef | `typename HandleTraits<handle_type>::parent_type` | public | — |
| `child_type` | typedef | `typename HandleTraits<handle_type>::child_type` | public | — |
| `unsaved_changes_flag_policy_type` | typedef | `typename HandleTraits<handle_type>::unsaved_changes_flag_policy` | public | — |
| `this_type` | typedef | `BasicHandle<handle_type>` | public | The type of this class. |
| `~BasicHandle()` | destructor | `None` | public | Destructor. |
| `reference()` | method | `const_weak_ref` | public | Returns a const-weak-ref to this Handle instance. |
| `begin()` | method | `const_iterator` | public | Returns the "begin" const-iterator to iterate over the collection of children. |
| `end()` | method | `const_iterator` | public | Returns the "end" const-iterator used during iteration over the collection of children. |
| `size()` | method | `container_size_type` | public | Returns the number of children elements this Handle contains as of the current revision. |
| `add( typename GPlatesGlobal::PointerTraits<child_type>::non_null_ptr_type new_child)` | method | `iterator` | public | Adds new\_child to the collection. new\_child must be a pointer to a child\_type that has not already been added to a feature\_collection. |
| `remove( const_iterator iter)` | method | `typename GPlatesGlobal::PointerTraits<child_type>::non_null_ptr_type` | public | Removes the child indicated by iter in the collection. |
| `remove_from_parent()` | method | `typename GPlatesGlobal::PointerTraits<handle_type>::non_null_ptr_type` | public | If this handle has a parent, removes this handle from the parent's collection. |
| `set_parent_ptr( parent_type *new_ptr, container_size_type new_index)` | method | `void` | public | Sets the pointer to the parent object that contains this feature. |
| `parent_ptr()` | method | `parent_type` | public | Gets a (non-const) pointer to the parent object that contains this feature. |
| `index_in_container()` | method | `container_size_type` | public | Returns the index of this Handle in its parent container. |
| `model_ptr()` | method | `Model` | public | Returns a (non-const) pointer to the Model to which this Handle belongs. |
| `is_active()` | method | `bool` | public | Returns true if the Handle is active and in the current state of the model. |
| `set_active( bool active = true)` | method | `void` | public | Sets whether this Handle is active or not. |
| `handle_child_modified()` | method | `void` | public | This function should be called by a child when the child is modified. |
| `flush_pending_notifications()` | method | `void` | public | Flushes pending notifications that were held up due to an active NotificationGuard. |
| `current_revision()` | method | `typename GPlatesGlobal::PointerTraits<const revision_type>::non_null_ptr_type` | protected | Accesses the current revision of the conceptual object accessed by this Handle. |
| `BasicHandle( handle_type *handle_ptr_, typename GPlatesGlobal::PointerTraits<revision_type>::non_null_ptr_type revision)` | constructor | `None` | protected | Constructor, given a particular revision object. |
| `notify_listeners_of_modification( bool publisher_modified, bool child_modified)` | method | `void` | protected | Notify our listeners of the modification of this Handle. |
| `current_changeset_handle_ptr()` | method | `ChangesetHandle` | protected | If model\_ptr() does not return NULL and there is a current ChangesetHandle registered with our model, returns a pointer to that current ChangesetHandle; otherwise, returns NULL. |
| `get( container_size_type index)` | method | `typename GPlatesGlobal::PointerTraits<child_type>::non_null_ptr_type` | private | Gets the child at the specified index, which must be valid. |
| `actual_add( typename GPlatesGlobal::PointerTraits<child_type>::non_null_ptr_type new_child)` | method | `container_size_type` | private | Does the actual job of adding the child to the revision's container. |
| `set_child_active( const_iterator iter, bool active)` | method | `void` | private | Sets the active flag in a particular child of this Handle. |
| `set_children_active( bool active)` | method | `void` | private | Sets the active flag in children of this Handle. |
| `notify_parent_of_modification()` | method | `void` | private | Notifies our parent of our modification (or a modification in one of our children). |
| `actual_notify_listeners_of_modification( bool publisher_modified, bool child_modified)` | method | `void` | private | Does the job of notify\_listeners\_of\_modification() without the guard checks. |
| `notify_listeners_of_addition( iterator new_child)` | method | `void` | private | Notify our listeners of the addition of a new child. |
| `actual_notify_listeners_of_addition( const std::vector<iterator> &new_children)` | method | `void` | private | Does the job of notify\_listeners\_of\_addition() without the guard checks. |
| `remove_child_from_pending_notification( iterator removed_child)` | method | `void` | private | Removes removed\_child from d\_pending\_addition\_notifications if it is there. |
| `notify_listeners_of_deactivation()` | method | `void` | private | Notify our listeners of deactivation (conceptual deletion) of this Handle. |
| `actual_notify_listeners_of_deactivation()` | method | `void` | private | Does the job of notify\_listeners\_of\_deactivation() without the guard checks. |
| `notify_listeners_of_reactivation()` | method | `void` | private | Notify our listeners of reactivation (conceptual undeletion) of this Handle. |
| `actual_notify_listeners_of_reactivation()` | method | `void` | private | Does the job of notify\_listeners\_of\_reactivation() without the guard checks. |
| `notify_listeners_of_impending_destruction()` | method | `void` | private | Notify our listeners of the impending destruction of this Handle in the C++ sense. |
| `flush_children_pending_notifications()` | method | `void` | private | Calls flush\_pending\_notifications() in children objects. |
| `remove_child_parent_pointers()` | method | `void` | private | Set the parent pointers of our children to NULL (eg, we're being destroyed). |
| `BasicHandle( const this_type &other)` | constructor | `None` | private | This constructor should not be defined, because we don't want to be able to copy construct one of these objects. |
| `operator=` | field | `this_type` | private | This should not be defined, because we don't want to be able to copy one of these objects. |
| `d_current_revision` | field | `typename GPlatesGlobal::PointerTraits<revision_type>::non_null_ptr_type` | private | The current revision of the conceptual object managed by this Handle. |
| `d_handle_ptr` | field | `handle_type` | private | A pointer to an instance of the template parameter Handle type. |
| `d_parent_ptr` | field | `parent_type` | private | The parent that contains the Handle. |
| `d_index_in_container` | field | `container_size_type` | private | The position of this element in its parent's container. |
| `d_is_active` | field | `bool` | private | If true, the Handle is active and in the current state of the model. |
| `d_has_pending_publisher_modification_notification` | field | `bool` | private | Used for holding notifications while a NotificationGuard is active. |
| `d_has_pending_child_modification_notification` | field | `bool` | private | — |
| `d_was_active_before_pending_notifications` | field | `bool` | private | — |
| `d_pending_addition_notifications` | field | `boost::scoped_ptr<std::vector<iterator> >` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_BASICHANDLE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=model/BasicHandle tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 440 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 280 |
| [model/ModelUtils](ModelUtils.md) | model | 198 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 137 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 135 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 128 |
| [app-logic/TopologyUtils](../app-logic/TopologyUtils.md) | app-logic | 126 |
| [app-logic/TopologyReconstruct](../app-logic/TopologyReconstruct.md) | app-logic | 122 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 120 |
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 120 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 116 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 112 |
| [app-logic/TopologyGeometryResolverLayerProxy](../app-logic/TopologyGeometryResolverLayerProxy.md) | app-logic | 102 |
| [app-logic/ReconstructUtils](../app-logic/ReconstructUtils.md) | app-logic | 93 |
| [file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport](../file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport.md) | file-io | 86 |
| [app-logic/TopologyNetworkResolverLayerProxy](../app-logic/TopologyNetworkResolverLayerProxy.md) | app-logic | 84 |
| [app-logic/PlateVelocityUtils](../app-logic/PlateVelocityUtils.md) | app-logic | 82 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 82 |
| [file-io/GmapReader](../file-io/GmapReader.md) | file-io | 78 |
| [app-logic/ReconstructLayerProxy](../app-logic/ReconstructLayerProxy.md) | app-logic | 75 |

*... and 382 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/BasicHandle.h
python scripts/gpq.py def GPlatesModel::BasicHandle --body
python scripts/gpq.py uses BasicHandle --kind class
python scripts/gpq.py hier BasicHandle
```

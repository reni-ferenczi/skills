# BasicHandle

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 39 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/BasicHandle.h` | C++ | 1161 |
| `src/model/BasicHandle.cc` | C++ | 108 |

## Overview

The model is a four-level tree — `Model` owns a `FeatureStoreRootHandle`, which
contains `FeatureCollectionHandle`s, which contain `FeatureHandle`s, which contain
`TopLevelProperty` objects. Each of the three handle levels needs the same
machinery: a container of children that lives in a separate revision object, a
parent pointer, a conceptual-deletion flag, and a way to tell observers that
something changed. `BasicHandle` is that machinery, written once as a template
and mixed into each level by inheritance (`FeatureHandle` derives from
`BasicHandle<FeatureHandle>`). Everything that varies between the levels — the
revision type, the parent type, the child type, the iterator and weak-ref
typedefs, and whether the level carries an unsaved-changes flag — is supplied by
`HandleTraits<HandleType>`, so the same code compiles into three different
positions in the tree. The two ends of the tree do not fit the generic pattern
and are handled by explicit template specialisations in `BasicHandle.cc`:
`BasicHandle<FeatureStoreRootHandle>` treats its parent pointer as a pointer to
the `Model` itself, and `BasicHandle<FeatureHandle>` disables the parent-pointer,
active-flag and notification logic for its children, because `TopLevelProperty`
has none of those things.

The central design idea is that identity is separate from content. A handle is
the permanent identity of a feature (or collection); its children live in a
`BasicRevision` subclass held through `d_current_revision`. Because the handle
address never changes when the content is edited, other tiers can hold
`WeakReference`s and `RevisionAwareIterator`s into the model and survive edits.
`WeakReference` deliberately does not keep the handle alive — the app-logic tier
must not override the model's own lifetime control, in particular because a
`FeatureHandle` keeps its feature ID registered for as long as it exists — so
instead of ref-counting, every observer registers itself on the handle through
`WeakObserverPublisher<HandleType>`, and `BasicHandle` pushes events at them.
Modification, addition, deactivation, reactivation and impending destruction each
have their own `WeakObserverVisitor` subclass (`WeakReferencePublisherModifiedVisitor`
and friends in `WeakReferenceVisitors.h`), applied to both the const and non-const
observer lists.

The rest of the class is about when those events are delivered. Every
modification bubbles up the parent chain via `notify_parent_of_modification()` so
that a change to a property registers as a change to the enclosing collection,
which is what drives the unsaved-changes flag. When a `NotificationGuard` is
active on the `Model`, modification and addition events are not delivered but
recorded in per-handle pending flags, and `flush_pending_notifications()` later
walks the subtree and emits one coalesced event per handle — this is how a bulk
edit avoids emitting thousands of individual notifications. `add()` and `remove()`
also open a `ChangesetHandle` on the model and register the touched handles with
whichever changeset is outermost, so that a group of fine-grained model
transactions can be presented to the user as a single undoable operation — the
plumbing is in place but the collected handles are currently discarded when the
changeset is destroyed.

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

**The revisioning is not yet copy-on-write.** `d_current_revision` is set in the
constructor and never reassigned anywhere in the tree; `add()`, `remove()` and
property edits mutate the single revision object in place. The revision-aware
plumbing — `RevisionAwareIterator` re-reading the current revision on every
dereference, the `RevisionId` on `FeatureRevision`, and the explicit FIXME on
`FeatureRevision::update_revision_id()` — exists in anticipation of a scheme that
creates a new revision per edit. Do not write code that assumes an old revision
is still reachable after a modification.

**`remove()` does not shrink the container.** It deactivates the child and NULLs
its slot in the revision, so `end()` and the indices of every other child are
unchanged, but `size()` (live children) and `container_size()` (slots) diverge.
Iterating and indexing must tolerate empty slots.

**`add()` may clone its argument, and always for `FeatureHandle`.** The
`BasicHandle<FeatureHandle>` specialisation deep-clones the `TopLevelProperty`
before inserting it, because property objects inside the model must not be
modified directly through a caller-held pointer. The object you passed in is not
the object in the model — use the returned iterator.

**Ownership and lifetime.** Children are owned by the revision through
`boost::intrusive_ptr`; the parent pointer is raw and back-pointing. The
destructor first notifies weak observers of impending destruction and then NULLs
its children's parent pointers, because clients can still hold owning pointers to
children after the parent is gone. Weak references never keep a handle alive:
always check `is_valid()` before every dereference, since the referent may have
been destroyed or merely deactivated.

**Deletion is conceptual and recursive.** `set_active(false)` deactivates the
whole subtree and can be reversed; the C++ object is untouched. Removing a child
also deactivates it, so a removed feature's weak refs report invalid rather than
dangling.

**Detached handles behave differently.** `model_ptr()` walks up parent pointers
and returns NULL if any link is missing, so a handle not yet attached to the
model has no changeset and no notification guard — its edits notify immediately
and are never batched.

**Notification-guard corner cases.** The unsaved-changes flag and the parent
notification are always applied immediately, guard or not; only the observer
events are deferred. Impending-destruction events are also never deferred, so a
handle can be destroyed while notifications for it are still pending. The
deactivation/reactivation pair is coalesced through
`d_was_active_before_pending_notifications`: toggling active twice under a guard
emits nothing. `flush_pending_notifications()` recurses into children first, and
delivering a batched event can itself trigger further model changes, so listeners
run while the tree is mid-flush.

**`remove_child_from_pending_notification()` is broken.** It calls the two-argument
`std::find(first, last)` with no value to search for, which does not compile as
written; the function is dead code today, but any change that starts calling it
must fix the call.

**Not copyable**, by declared-but-undefined copy constructor and assignment
operator, so misuse fails at link time rather than compile time. The class also
relies on `dynamic_cast` to reach `BasicHandle<parent_type>` and
`BasicHandle<child_type>` from a bare handle pointer, so the handle types must
stay polymorphic.

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

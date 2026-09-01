# FeatureHandle

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 1185 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/FeatureHandle.h` | C++ | 331 |
| `src/model/FeatureHandle.cc` | C++ | 237 |

## Overview

The bottom handle level of the model tree, and the class most of GPlates actually
manipulates. A feature is a `FeatureType` plus a `FeatureId` plus a list of
`TopLevelProperty` objects; the properties are the revisioned part and live in a
`FeatureRevision`, while the handle keeps the identity and the two attributes that
are meant to outlive every edit. All the container machinery — iteration, the
active flag, weak-reference notification, bubbling modifications up to the
enclosing `FeatureCollectionHandle` — comes from `BasicHandle<FeatureHandle>`.
What is written here is the feature-specific part: the factories, the clone
family, and the mutators that need to touch the revision ID.

Properties inside the model are treated as immutable, and that assumption is
enforced at every entry point. `add()` inserts a `deep_clone()` of what you pass
(the specialisation of `BasicHandle<FeatureHandle>::actual_add` in
`BasicHandle.cc`), and `set()` likewise deep-clones the replacement, so the object
you handed in is never the object in the model — use the returned iterator.
Dereferencing a non-const iterator does not give you a mutable property either: it
yields a `TopLevelPropertyRef` proxy that only exposes `const TopLevelProperty`,
and whose `operator=` routes back through `FeatureHandle::set` so that the
notification and revision-ID bookkeeping cannot be bypassed. This immutability is
also why `clone()` can be shallow — the clone shares property objects with the
original, and any later edit to either replaces the pointer rather than the
pointee.

The revision ID is bumped by `add()`, `remove()` and `set()`, but only if this
handle is not already registered in the current `ChangesetHandle`. So the revision
ID advances once per changeset — per user-visible edit — rather than once per
atomic model transaction. Note also that `clone()` always mints a fresh
`FeatureId`; to reproduce a feature with its original identity you have to go
through `create()` with an explicit `FeatureId`, which is what the file readers
do.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::FeatureHandle`](#gplatesmodelfeaturehandle) | class | [`BasicHandle<FeatureHandle>`](BasicHandle.md)<br>[`GPlatesUtils::ReferenceCount<FeatureHandle>`](../utils/ReferenceCount.md) | — | 0 | A feature handle acts as a persistent handle to the revisioned content of a conceptual feature. |

## Members

### `GPlatesModel::FeatureHandle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `this_type` | typedef | `FeatureHandle` | public | The type of this class. |
| `property_predicate_type` | typedef | `boost::function<bool (const GPlatesGlobal::PointerTraits<const TopLevelProperty>::non_null_ptr_type &)>` | public | Typedef for a function that accepts a pointer to a property and returns a boolean. |
| `create( const FeatureType &feature_type_, const FeatureId &feature_id_ = FeatureId(), const RevisionId &revision_id_ = RevisionId())` | method | `non_null_ptr_type` | public | Creates a new FeatureHandle instance with feature\_type\_ and optional feature\_id\_ and revision\_id\_. |
| `create( const WeakReference<FeatureCollectionHandle> &feature_collection, const FeatureType &feature_type_, const FeatureId &feature_id_ = FeatureId(), const RevisionId &revision_id_ = RevisionId())` | method | `weak_ref` | public | Creates a new FeatureHandle instance with feature\_type\_ and optional feature\_id\_ and revision\_id\_. |
| `clone()` | method | `non_null_ptr_type` | public | Makes a clone of this feature. |
| `clone( const WeakReference<FeatureCollectionHandle> &feature_collection)` | method | `weak_ref` | public | Makes a clone of this feature. |
| `clone( const property_predicate_type &clone_properties_predicate)` | method | `non_null_ptr_type` | public | Makes a clone of this feature (but only the property values for which the given predicate clone\_properties\_predicate returns true). |
| `clone( const WeakReference<FeatureCollectionHandle> &feature_collection, const property_predicate_type &clone_properties_predicate)` | method | `weak_ref` | public | Makes a clone of this feature (but only the property values for which the given predicate clone\_properties\_predicate returns true). |
| `add( GPlatesGlobal::PointerTraits<TopLevelProperty>::non_null_ptr_type new_child)` | method | `iterator` | public | BasicHandle\<FeatureHandle\>::add. |
| `remove( const_iterator iter)` | method | `void` | public | BasicHandle\<FeatureHandle\>::remove. |
| `set( iterator iter, child_type::non_null_ptr_to_const_type new_child)` | method | `void` | public | Changes the child pointed to by iterator iter into new\_child. |
| `remove_properties_by_name( const PropertyName &property_name)` | method | `void` | public | Removes all children properties that have the given property\_name. |
| `set_feature_type( const FeatureType &feature_type_)` | method | `void` | public | Changes the feature type of this feature to feature\_type\_. |
| `revision_id` | field | `RevisionId` | public | Returns the revision ID of the current revision of this feature. |
| `creation_time()` | method | `time_t` | public | Returns the time of creation of this instance. |
| `FeatureHandle( const FeatureType &feature_type_, const FeatureId &feature_id_, GPlatesGlobal::PointerTraits<revision_type>::non_null_ptr_type revision_)` | constructor | `None` | private | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `FeatureHandle( const this_type &other)` | constructor | `None` | private | This constructor should not be defined, because we don't want to be able to copy construct one of these objects. |
| `operator=` | field | `this_type` | private | This should not be defined, because we don't want to be able to copy one of these objects. |
| `d_feature_type` | field | `FeatureType` | private | The type of this feature. |
| `d_feature_id` | field | `FeatureId` | private | The unique feature ID of this feature. |
| `d_creation_time` | field | `time_t` | private | The time of creation of this instance. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `new_child_equals_existing( const GPlatesModel::TopLevelProperty::non_null_ptr_to_const_type &new_child, const boost::intrusive_ptr<GPlatesModel::TopLevelProperty> &existing_child)` | function | `bool` | — |
| `GPLATES_MODEL_FEATUREHANDLE_H` | macro | `None` | — |

## Notes

**The feature type is not actually immutable.** The class comment says the handle
holds "the properties of a feature which can never change: the feature type and
the feature ID", but `set_feature_type()` exists and rewrites `d_feature_type` in
place. Only the feature ID is genuinely fixed — it has no setter by design. Code
that caches anything keyed on feature type must listen for modification events
rather than reading the type once.

**The constructor registers the feature in a global ID table.** `FeatureId` is an
`IdTypeGenerator` over a process-wide `IdStringSet`, and the constructor calls
`d_feature_id.set_back_ref_target(*this)` so that the ID resolves to this handle.
That registration lasts as long as the object does, which is precisely why
`WeakReference` must not keep features alive: a feature kept alive by a stray
strong reference keeps its ID resolving, and re-reading the same file would then
register the same ID against two different handles.

**`add()` and `remove()` shadow the base-class members, they do not override
them.** They are non-virtual, so calling through a `BasicHandle<FeatureHandle>&`
skips the revision-ID update. `remove()` also narrows the base signature to return
`void`, discarding the removed property that `BasicHandle::remove()` hands back —
if you need it, read it through the iterator first.

**`set()` silently does nothing** when the slot is empty or when the new property
compares equal to the existing one, so no notification is emitted and the revision
ID does not move. It also reports the change as a *child* modification, whereas
`set_feature_type()` reports a *publisher* modification; listeners that
distinguish the two see property edits and feature-type edits differently.

**Removing while iterating is safe here.** `remove()` leaves a NULL slot rather
than shifting the container, and `RevisionAwareIterator` skips NULL slots on
construction and on increment, so `remove_properties_by_name()`'s
remove-during-iteration loop is correct. The same property of the container means
indices and `end()` are stable across removals, but `size()` and
`container_size()` diverge.

**Ownership and validity.** A feature is reference-counted and owned by the
`FeatureCollectionRevision` holding it; a `weak_ref` neither keeps it alive nor
stays valid across deactivation, so check `is_valid()` before every dereference.
A feature made by the detached `create()` or `clone()` overload has no parent, so
`model_ptr()` is NULL for it: its edits are not batched by a `NotificationGuard`
and never bump the revision ID, because there is no changeset to consult. Deleting
a feature through the UI deactivates it rather than destroying it, so the handle
address — and its feature ID registration — persists until the model is flushed.

**`creation_time()` is wall-clock `time(NULL)` at construction**, not a model
timestamp, and it is per-object: a clone and a reload both get a fresh value.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/PlatesFormatUtils](../file-io/PlatesFormatUtils.md) | file-io | 150 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 81 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 77 |
| [model/ModelUtils](ModelUtils.md) | model | 68 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 60 |
| [app-logic/TopologyUtils](../app-logic/TopologyUtils.md) | app-logic | 48 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 45 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 42 |
| [app-logic/ReconstructedFeatureGeometry](../app-logic/ReconstructedFeatureGeometry.md) | app-logic | 41 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 41 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 41 |
| [qt-widgets/ChoosePropertyWidget](../qt-widgets/ChoosePropertyWidget.md) | qt-widgets | 36 |
| [app-logic/ReconstructContext](../app-logic/ReconstructContext.md) | app-logic | 35 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 32 |
| [app-logic/DependentTopologicalSectionLayers](../app-logic/DependentTopologicalSectionLayers.md) | app-logic | 28 |
| [app-logic/TopologyGeometryResolverLayerProxy](../app-logic/TopologyGeometryResolverLayerProxy.md) | app-logic | 27 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 27 |
| [app-logic/TRSUtils](../app-logic/TRSUtils.md) | app-logic | 26 |
| [app-logic/ReconstructScalarCoverageLayerProxy](../app-logic/ReconstructScalarCoverageLayerProxy.md) | app-logic | 24 |
| [file-io/GpmlFeatureReaderImpl](../file-io/GpmlFeatureReaderImpl.md) | file-io | 23 |

*... and 225 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/FeatureHandle.h
python scripts/gpq.py def GPlatesModel::FeatureHandle --body
python scripts/gpq.py uses FeatureHandle --kind class
python scripts/gpq.py hier FeatureHandle
```

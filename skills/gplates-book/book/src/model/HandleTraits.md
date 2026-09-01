# HandleTraits

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 515 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/HandleTraits.h` | C++ | 310 |

## Overview

This header is the single declaration of the model's containment tree, expressed
as types. The model is a three-level hierarchy — `Model` owns a
`FeatureStoreRootHandle`, which contains `FeatureCollectionHandle`s, which
contain `FeatureHandle`s, which contain `TopLevelProperty` objects — and each
handle also has a matching revision class (`FeatureRevision`,
`FeatureCollectionRevision`, `FeatureStoreRootRevision`) holding its actual
children. `HandleTraits` states, for one handle type, what its parent, its
child, its revision, its owning pointer, its weak reference and its iterator
are. `BasicHandle<HandleType>` then pulls every one of those typedefs out of
the traits and implements `add`, `remove`, `begin`/`end`, `reference`,
`set_active` and the notification machinery once, generically, for all three
handles.

The reason it is a separate header, and the reason the file forward-declares
everything rather than including anything, is stated in the class comment: you
can learn a handle's associated types without including that handle's header.
That matters because the participants are mutually recursive —
`RevisionAwareIterator` needs its handle's revision type and value type,
`WeakReference` needs its handle type, `TopLevelPropertyRef` is constructed
from `HandleTraits<FeatureHandle>::iterator`, and each handle contains the one
below it. Routing all of that through this one dependency-free header is what
keeps the include graph acyclic. Its only include is `global/PointerTraits.h`,
which supplies the `non_null_ptr_type` spelling.

The `unsaved_changes_flag_policy` typedef is a policy in the classic sense, not
just a description: `BasicHandle` derives from
`HandleTraits<HandleType>::unsaved_changes_flag_policy` and pulls
`set_unsaved_changes` into scope with a `using` declaration. `BasicHandle` can
therefore call `set_unsaved_changes()` on every mutation without asking which
handle it is; on `FeatureHandle` and `FeatureStoreRootHandle` the call compiles
to nothing, and only `FeatureCollectionHandle` — the granularity at which
GPlates decides a file is dirty — actually carries the bool and exposes
`contains_unsaved_changes()` / `clear_unsaved_changes()`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::HandleTraitsInternals::HandleTraitsBase`](#gplatesmodelhandletraitsinternalshandletraitsbase) | struct | — | `<class HandleType>` | 3 | Contains typedefs common to all HandleTraits. |
| [`GPlatesModel::HandleTraitsInternals::WithUnsavedChangesFlag`](#gplatesmodelhandletraitsinternalswithunsavedchangesflag) | class | — | — | 0 | A policy class that indicates that a handle type stores an unsaved changes flag. |
| [`GPlatesModel::HandleTraitsInternals::WithoutUnsavedChangesFlag`](#gplatesmodelhandletraitsinternalswithoutunsavedchangesflag) | class | — | — | 0 | A policy class that indicates that a handle type does not store an unsaved changes flag. |
| [`GPlatesModel::HandleTraits`](#gplatesmodelhandletraits) | struct | — | `<class HandleType>` | 3 | HandleTraits is a traits class to provide type information about FeatureHandle, FeatureCollectionHandle and FeatureStoreRootHandle. |
| [`GPlatesModel::HandleTraits<FeatureHandle>`](#gplatesmodelhandletraitsfeaturehandle) | struct | [`HandleTraitsInternals::HandleTraitsBase<FeatureHandle>`](HandleTraits.md) | `<>` | 0 | Specialisation of HandleTraits for FeatureHandle. |
| [`GPlatesModel::HandleTraits<const FeatureHandle>`](#gplatesmodelhandletraitsconst-featurehandle) | struct | [`HandleTraits<FeatureHandle>`](HandleTraits.md) | `<>` | 0 | — |
| [`GPlatesModel::HandleTraits<FeatureCollectionHandle>`](#gplatesmodelhandletraitsfeaturecollectionhandle) | struct | [`HandleTraitsInternals::HandleTraitsBase<FeatureCollectionHandle>`](HandleTraits.md) | `<>` | 0 | Specialisation of HandleTraits for FeatureCollectionHandle. |
| [`GPlatesModel::HandleTraits<const FeatureCollectionHandle>`](#gplatesmodelhandletraitsconst-featurecollectionhandle) | struct | [`HandleTraits<FeatureCollectionHandle>`](HandleTraits.md) | `<>` | 0 | — |
| [`GPlatesModel::HandleTraits<FeatureStoreRootHandle>`](#gplatesmodelhandletraitsfeaturestoreroothandle) | struct | [`HandleTraitsInternals::HandleTraitsBase<FeatureStoreRootHandle>`](HandleTraits.md) | `<>` | 0 | Specialisation of HandleTraits for FeatureStoreRootHandle. |
| [`GPlatesModel::HandleTraits<const FeatureStoreRootHandle>`](#gplatesmodelhandletraitsconst-featurestoreroothandle) | struct | [`HandleTraits<FeatureStoreRootHandle>`](HandleTraits.md) | `<>` | 0 | — |

## Members

### `GPlatesModel::HandleTraitsInternals::HandleTraitsBase`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `typename GPlatesGlobal::PointerTraits<HandleType>::non_null_ptr_type` | public | Typedef for GPlatesGlobal::PointerTraits\<HandleType\>::non\_null\_ptr\_type. |
| `non_null_ptr_to_const_type` | typedef | `typename GPlatesGlobal::PointerTraits<const HandleType>::non_null_ptr_type` | public | Typedef for GPlatesGlobal::PointerTraits\<const HandleType\>::non\_null\_ptr\_type. |
| `weak_ref` | typedef | `WeakReference<HandleType>` | public | Typedef for WeakReference\<HandleType\>. |
| `const_weak_ref` | typedef | `WeakReference<const HandleType>` | public | Typedef for WeakReference\<const HandleType\>. |
| `iterator` | typedef | `RevisionAwareIterator<HandleType>` | public | Typedef for RevisionAwareIterator\<HandleType\>. |
| `const_iterator` | typedef | `RevisionAwareIterator<const HandleType>` | public | Typedef for RevisionAwareIterator\<const HandleType\>. |

### `GPlatesModel::HandleTraitsInternals::WithUnsavedChangesFlag`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `contains_unsaved_changes()` | method | `bool` | public | — |
| `clear_unsaved_changes()` | method | `void` | public | — |
| `WithUnsavedChangesFlag()` | constructor | `None` | protected | — |
| `~WithUnsavedChangesFlag()` | destructor | `None` | protected | — |
| `set_unsaved_changes()` | method | `void` | protected | — |
| `d_contains_unsaved_changes` | field | `bool` | private | — |

### `GPlatesModel::HandleTraitsInternals::WithoutUnsavedChangesFlag`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `WithoutUnsavedChangesFlag()` | constructor | `None` | protected | — |
| `~WithoutUnsavedChangesFlag()` | destructor | `None` | protected | — |
| `set_unsaved_changes()` | method | `void` | protected | — |

### `GPlatesModel::HandleTraits`

*None.*

### `GPlatesModel::HandleTraits<FeatureHandle>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `revision_type` | typedef | `FeatureRevision` | public | Typedef for FeatureRevision, the corresponding revision type to FeatureHandle. |
| `parent_type` | typedef | `FeatureCollectionHandle` | public | Typedef for FeatureCollectionHandle, the type one level above FeatureHandle in the tree of nodes. |
| `child_type` | typedef | `TopLevelProperty` | public | Typedef for TopLevelProperty, the type one level below FeatureHandle in the tree of nodes. |
| `iterator_value_type` | typedef | `TopLevelPropertyRef` | public | Typedef for TopLevelPropertyRef, the type returned on dereference of the FeatureHandle non-const iterator. |
| `const_iterator_value_type` | typedef | `GPlatesGlobal::PointerTraits<const TopLevelProperty>::non_null_ptr_type` | public | Typedef for PointerTraits\<const TopLevelProperty\>::non\_null\_ptr\_type, the type returned on dereference of the FeatureHandle const iterator. |
| `unsaved_changes_flag_policy` | typedef | `HandleTraitsInternals::WithoutUnsavedChangesFlag` | public | FeatureHandles don't have an unsaved changes flag. |

### `GPlatesModel::HandleTraits<const FeatureHandle>`

*None.*

### `GPlatesModel::HandleTraits<FeatureCollectionHandle>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `revision_type` | typedef | `FeatureCollectionRevision` | public | Typedef for FeatureCollectionRevision, the corresponding revision type to FeatureCollectionHandle. |
| `parent_type` | typedef | `FeatureStoreRootHandle` | public | Typedef for FeatureStoreRootHandle, the type one level above FeatureCollectionHandle in the tree of nodes. |
| `child_type` | typedef | `FeatureHandle` | public | Typedef for FeatureHandle, the type one level below FeatureCollectionHandle in the tree of nodes. |
| `iterator_value_type` | typedef | `GPlatesGlobal::PointerTraits<FeatureHandle>::non_null_ptr_type` | public | Typedef for PointerTraits\<FeatureHandle\>::non\_null\_ptr\_type, the type returned on dereference of the FeatureCollectionHandle non-const iterator. |
| `const_iterator_value_type` | typedef | `GPlatesGlobal::PointerTraits<const FeatureHandle>::non_null_ptr_type` | public | Typedef for PointerTraits\<const FeatureHandle\>::non\_null\_ptr\_type, the type returned on dereference of the FeatureCollectionHandle const iterator. |
| `unsaved_changes_flag_policy` | typedef | `HandleTraitsInternals::WithUnsavedChangesFlag` | public | FeatureCollectionHandles have an unsaved changes flag. |

### `GPlatesModel::HandleTraits<const FeatureCollectionHandle>`

*None.*

### `GPlatesModel::HandleTraits<FeatureStoreRootHandle>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `revision_type` | typedef | `FeatureStoreRootRevision` | public | Typedef for FeatureStoreRootRevision, the corresponding revision type to FeatureStoreRootHandle. |
| `parent_type` | typedef | `Model` | public | Typedef for Model, the type one level above FeatureStoreRootHandle in the tree of nodes. |
| `child_type` | typedef | `FeatureCollectionHandle` | public | Typedef for FeatureCollectionHandle, the type one level below FeatureStoreRootHandle in the tree of nodes. |
| `iterator_value_type` | typedef | `GPlatesGlobal::PointerTraits<FeatureCollectionHandle>::non_null_ptr_type` | public | Typedef for PointerTraits\<FeatureCollectionHandle\>::non\_null\_ptr\_type, the type returned on dereference of the FeatureStoreRootHandle non-const iterator. |
| `const_iterator_value_type` | typedef | `GPlatesGlobal::PointerTraits<const FeatureCollectionHandle>::non_null_ptr_type` | public | Typedef for PointerTraits\<const FeatureCollectionHandle\>::non\_null\_ptr\_type, the type returned on dereference of the FeatureStoreRoothandle const iterator. |
| `unsaved_changes_flag_policy` | typedef | `HandleTraitsInternals::WithoutUnsavedChangesFlag` | public | FeatureStoreRootHandles don't have an unsaved changes flag. |

### `GPlatesModel::HandleTraits<const FeatureStoreRootHandle>`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_HANDLETRAITS_H` | macro | `None` | — |

## Notes

The `const` specialisations do not add const anywhere. `HandleTraits<const
FeatureHandle>` simply inherits `HandleTraits<FeatureHandle>`, so
`HandleTraits<const FeatureHandle>::iterator` is still
`RevisionAwareIterator<FeatureHandle>` and its `weak_ref` is still
`WeakReference<FeatureHandle>`. They exist so that a template instantiated on
`const H` still compiles; choosing const-ness is the caller's job, done by
naming the `const_`-prefixed member. `RevisionAwareIterator` shows the intended
pattern — its internal `Traits<const HandleType>` partial specialisation strips
the const and then reads `const_iterator_value_type` and `const_weak_ref` from
`HandleTraits<HandleType>`.

`iterator_value_type` is deliberately asymmetric, and this is the one place the
copy-on-write design leaks into a typedef. Dereferencing a
`FeatureCollectionHandle` or `FeatureStoreRootHandle` iterator, or a *const*
`FeatureHandle` iterator, yields an owning pointer to the child. Dereferencing a
non-const `FeatureHandle` iterator yields a `TopLevelPropertyRef` proxy instead,
whose assignment operator clones the current `FeatureRevision`, clones the
assigned property into the new revision and commits a transaction. That is how
property writes are captured for the unsaved-changes flag and for undo/redo;
pointers obtained before such an assignment point at the superseded revision.

The base class supplies no `revision_type`, `parent_type`, `child_type` or
`unsaved_changes_flag_policy` — those come only from the specialisations, and the
primary template is empty. Instantiating `HandleTraits` on anything other than
the three handle types (or their const forms) therefore fails at the point of
use with a missing-typedef error rather than a clear one. Adding a fourth level
to the model tree means adding a specialisation here first; nothing else needs
to change for `BasicHandle`, `RevisionAwareIterator` and `WeakReference` to work
on it.

The two policy classes have non-virtual protected destructors, which is correct
for a base that is only ever destroyed through the derived handle, but means
they must never be deleted polymorphically.

## Used by

| Unit | Component | References |
|---|---|---|
| [model/ModelUtils](ModelUtils.md) | model | 36 |
| [model/BasicHandle](BasicHandle.md) | model | 30 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 22 |
| [model/FeatureVisitor](FeatureVisitor.md) | model | 13 |
| [model/FeatureHandle](FeatureHandle.md) | model | 11 |
| [model/RevisionAwareIterator](RevisionAwareIterator.md) | model | 11 |
| [qt-widgets/CreateFeaturePropertiesPage](../qt-widgets/CreateFeaturePropertiesPage.md) | qt-widgets | 11 |
| [model/TopLevelPropertyRef](TopLevelPropertyRef.md) | model | 9 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 9 |
| [app-logic/ExtractRasterFeatureProperties](../app-logic/ExtractRasterFeatureProperties.md) | app-logic | 8 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 8 |
| [feature-visitors/GeometryTypeFinder](../feature-visitors/GeometryTypeFinder.md) | feature-visitors | 8 |
| [model/NotificationGuard](NotificationGuard.md) | model | 7 |
| [model/WeakReferenceVisitors](WeakReferenceVisitors.md) | model | 6 |
| [qt-widgets/EditWidgetGroupBox](../qt-widgets/EditWidgetGroupBox.md) | qt-widgets | 6 |
| [model/TopLevelPropertyInline](TopLevelPropertyInline.md) | model | 5 |
| [qt-widgets/EditTotalReconstructionSequenceWidget](../qt-widgets/EditTotalReconstructionSequenceWidget.md) | qt-widgets | 5 |
| [app-logic/ReconstructMethodVirtualGeomagneticPole](../app-logic/ReconstructMethodVirtualGeomagneticPole.md) | app-logic | 4 |
| [gui/FeaturePropertyTableModel](../gui/FeaturePropertyTableModel.md) | gui | 4 |
| [model/Model](Model.md) | model | 4 |

*... and 37 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/HandleTraits.h
python scripts/gpq.py def GPlatesModel::HandleTraits<FeatureHandle> --body
python scripts/gpq.py uses HandleTraits<FeatureHandle> --kind struct
python scripts/gpq.py hier HandleTraits<FeatureHandle>
```

# HandleTraits

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 515 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/HandleTraits.h` | C++ | 310 |

## Overview

[[[PROSE overview unit=model/HandleTraits tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=model/HandleTraits tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

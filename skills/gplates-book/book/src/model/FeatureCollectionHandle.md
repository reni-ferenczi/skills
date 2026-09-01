# FeatureCollectionHandle

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 39 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/FeatureCollectionHandle.h` | C++ | 170 |
| `src/model/FeatureCollectionHandle.cc` | C++ | 71 |

## Overview

The middle level of the model tree: a `FeatureCollectionHandle` is contained by
the `FeatureStoreRootHandle` and contains `FeatureHandle`s, and it is the unit
that is loaded, saved or unloaded in one operation — roughly one data file, though
nothing forces that. Almost all of its behaviour comes from
`BasicHandle<FeatureCollectionHandle>`: the child container, iteration, add and
remove, the active flag, weak-reference notification. What is actually declared
here is only what the collection level adds on top — the two factory functions and
the `tags` map.

The class exists at all, rather than being folded into its revision, because
identity and content are deliberately split. The handle stays at one memory
address for the whole life of the conceptual collection while its content lives in
a `FeatureCollectionRevision`, so `WeakReference<FeatureCollectionHandle>` held by
the app-logic and GUI tiers survive every edit. Because a handle must never be
copied or live on the stack, construction is private and goes through
`create()`; the no-argument overload builds a detached collection that the caller
must add to a `FeatureStoreRootHandle` itself, while the overload taking a
`WeakReference<FeatureStoreRootHandle>` adds it and hands back a weak-ref to the
collection now inside the model.

`tags` is an escape hatch: an untyped `std::map<std::string, boost::any>` for
per-collection metadata that has no home in the data model proper. It is not
decoration — `GpmlReader` records the GPGIM version it parsed under
`GpgimVersion::FEATURE_COLLECTION_TAG` and `GpmlOutputVisitor` reads it back when
writing, and `FeatureCollectionFileFormat` stores the shapefile
model-to-attribute mapping there. The header itself notes that a tag common to
most collections would be better promoted to a real member.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::FeatureCollectionHandle`](#gplatesmodelfeaturecollectionhandle) | class | [`BasicHandle<FeatureCollectionHandle>`](BasicHandle.md)<br>[`GPlatesUtils::ReferenceCount<FeatureCollectionHandle>`](../utils/ReferenceCount.md) | — | 0 | A feature collection handle acts as a persistent handle to the revisioned content of a conceptual feature collection. |

## Members

### `GPlatesModel::FeatureCollectionHandle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `this_type` | typedef | `FeatureCollectionHandle` | public | The type of this class. |
| `tags_type` | typedef | `std::map<std::string, boost::any>` | public | The type of the collection of metadata. |
| `create()` | method | `non_null_ptr_type` | public | Creates a new FeatureCollectionHandle instance. |
| `create( const WeakReference<FeatureStoreRootHandle> &feature_store_root)` | method | `weak_ref` | public | Creates a new FeatureCollectionHandle instance. |
| `tags` | field | `tags_type` | public | Returns the collection of miscellaneous metadata associated with this feature collection. |
| `FeatureCollectionHandle()` | constructor | `None` | private | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `FeatureCollectionHandle( const this_type &other)` | constructor | `None` | private | This constructor should not be defined, because we don't want to be able to copy construct one of these objects. |
| `operator=` | field | `this_type` | private | This should not be defined, because we don't want to be able to copy one of these objects. |
| `d_tags` | field | `tags_type` | private | A miscellaneous collection of metadata associated with this feature collection. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_FEATURECOLLECTIONHANDLE_H` | macro | `None` | — |

## Notes

**This is the only handle level that carries an unsaved-changes flag.**
`HandleTraits<FeatureCollectionHandle>` selects the `WithUnsavedChangesFlag`
policy, whereas `FeatureHandle` and `FeatureStoreRootHandle` select the do-nothing
`WithoutUnsavedChangesFlag`. `contains_unsaved_changes()` and
`clear_unsaved_changes()` are inherited from that policy, which is why they do not
appear in the table above. The flag is set by `BasicHandle` on every
notification of modification, and because modifications bubble up the parent
chain, editing a property deep inside a feature marks its collection dirty. It is
set immediately even under a `NotificationGuard`. Nothing clears it automatically
— saving code must call `clear_unsaved_changes()`.

**Ownership.** A collection is reference-counted through
`GPlatesUtils::ReferenceCount` and owned by the `FeatureStoreRootRevision` that
contains it. A weak-ref does not keep it alive; check `is_valid()` before every
dereference. A collection created by `create()` with no arguments has no parent,
so `model_ptr()` returns NULL for it and for every feature inside it: its edits
are neither batched by a notification guard nor recorded in a changeset until it
is added to the store root.

**`tags` is untyped and unchecked.** Values are `boost::any`, so a reader
storing one type and a writer expecting another fails at `boost::any_cast` at
runtime, not at compile time. `tags()` returns a mutable reference, so a caller
can rewrite the map behind the collection's back without any modification
notification being emitted.

**Unloading is not destruction.** `set_active(false)` deactivates the collection
and every feature in it; the objects survive and can be reactivated. Weak-refs to
a deactivated collection report `is_valid()` false, so "gone" and "unloaded" are
indistinguishable to a plain validity check.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 88 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 64 |
| [app-logic/ReconstructUtils](../app-logic/ReconstructUtils.md) | app-logic | 30 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 30 |
| [app-logic/ReconstructMethodVirtualGeomagneticPole](../app-logic/ReconstructMethodVirtualGeomagneticPole.md) | app-logic | 29 |
| [app-logic/AppLogicUtils](../app-logic/AppLogicUtils.md) | app-logic | 27 |
| [app-logic/AssignPlateIds](../app-logic/AssignPlateIds.md) | app-logic | 27 |
| [feature-visitors/FeatureClassifier](../feature-visitors/FeatureClassifier.md) | feature-visitors | 25 |
| [app-logic/ReconstructContext](../app-logic/ReconstructContext.md) | app-logic | 24 |
| [app-logic/TopologyUtils](../app-logic/TopologyUtils.md) | app-logic | 23 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 23 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 21 |
| [file-io/File](../file-io/File.md) | file-io | 20 |
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 19 |
| [app-logic/TopologyNetworkResolverLayerProxy](../app-logic/TopologyNetworkResolverLayerProxy.md) | app-logic | 18 |
| [app-logic/deprecated/PropertyValuePropogator](../app-logic/deprecated/PropertyValuePropogator.md) | app-logic | 16 |
| [feature-visitors/PropertyValueFinder](../feature-visitors/PropertyValueFinder.md) | feature-visitors | 16 |
| [app-logic/FeatureCollectionFileState](../app-logic/FeatureCollectionFileState.md) | app-logic | 15 |
| [app-logic/RasterLayerTask](../app-logic/RasterLayerTask.md) | app-logic | 15 |
| [app-logic/ScalarField3DLayerTask](../app-logic/ScalarField3DLayerTask.md) | app-logic | 15 |

*... and 143 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/FeatureCollectionHandle.h
python scripts/gpq.py def GPlatesModel::FeatureCollectionHandle --body
python scripts/gpq.py uses FeatureCollectionHandle --kind class
python scripts/gpq.py hier FeatureCollectionHandle
```

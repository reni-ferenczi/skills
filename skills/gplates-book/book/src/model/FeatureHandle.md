# FeatureHandle

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 1185 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/FeatureHandle.h` | C++ | 331 |
| `src/model/FeatureHandle.cc` | C++ | 237 |

## Overview

[[[PROSE overview unit=model/FeatureHandle tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=model/FeatureHandle tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

# FeatureCollectionHandle

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 39 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/FeatureCollectionHandle.h` | C++ | 170 |
| `src/model/FeatureCollectionHandle.cc` | C++ | 71 |

## Overview

[[[PROSE overview unit=model/FeatureCollectionHandle tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=model/FeatureCollectionHandle tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

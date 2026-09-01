# PyFeatureCollection

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 1675 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PyFeatureCollection.h` | C++ | 85 |
| `src/api/PyFeatureCollection.cc` | C++ | 53 |

## Overview

`FeatureCollection` is a Python wrapper around `FeatureCollectionHandle` that provides safe access to feature collections from Python. It allows iteration over features with the `features()` method and querying the collection size with `size()`. The wrapper manages validity checking internally, returning empty results if the underlying handle becomes invalid — a critical capability given that feature collections can be unloaded or deleted during application use.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::FeatureCollection`](#gplatesapifeaturecollection) | class | — | — | 0 | Wrapper around FeatureCollectionHandle for exposing to Python. |

## Members

### `GPlatesApi::FeatureCollection`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( GPlatesModel::FeatureCollectionHandle::weak_ref feature_collection)` | method | `FeatureCollection` | public | — |
| `size()` | method | `std::size_t` | public | — |
| `features()` | method | `boost::python::list` | public | — |
| `FeatureCollection( GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | constructor | `None` | private | — |
| `d_feature_collection` | field | `GPlatesModel::FeatureCollectionHandle::weak_ref` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `export_feature_collection()` | function | `void` | — |
| `GPLATES_API_FEATURECOLLECTION_H` | macro | `None` | — |

## Notes

The wrapper holds a weak reference to the feature collection, so it safely handles the case where the collection is unloaded. Calls to `size()` and `features()` return zero-length results if the handle is no longer valid.

## Used by

| Unit | Component | References |
|---|---|---|
| [api/PyApplication](PyApplication.md) | api | 6 |
| [app-logic/LayerProxyUtils](../app-logic/LayerProxyUtils.md) | app-logic | 4 |

## Related

**Python bindings**

| Python name | Kind | Owner | C++ |
|---|---|---|---|
| `FeatureCollection` | class | — | `GPlatesApi::FeatureCollection` |
| `size` | attribute | `FeatureCollection` | `&GPlatesApi::FeatureCollection::size` |
| `size` | method | `FeatureCollection` | `&GPlatesApi::FeatureCollection::size` |
| `features` | method | `FeatureCollection` | `&GPlatesApi::FeatureCollection::features` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/PyFeatureCollection.h
python scripts/gpq.py def GPlatesApi::FeatureCollection --body
python scripts/gpq.py uses FeatureCollection --kind class
python scripts/gpq.py hier FeatureCollection
```

# PyFeatureCollection

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 1675 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PyFeatureCollection.h` | C++ | 85 |
| `src/api/PyFeatureCollection.cc` | C++ | 53 |

## Overview

[[[PROSE overview unit=api/PyFeatureCollection tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=api/PyFeatureCollection tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

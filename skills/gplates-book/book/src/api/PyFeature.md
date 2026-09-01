# PyFeature

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 301 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PyFeature.h` | C++ | 139 |
| `src/api/PyFeature.cc` | C++ | 279 |

## Overview

[[[PROSE overview unit=api/PyFeature tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::Feature`](#gplatesapifeature) | class | — | — | 0 | — |

## Members

### `GPlatesApi::Feature`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Feature()` | constructor | `None` | public | — |
| `Feature(GPlatesModel::FeatureHandle::weak_ref w_ref)` | constructor | `None` | public | — |
| `get_properties()` | method | `bp::list` | public | Return all properties in boost::python::list. |
| `get_properties_by_name( bp::object prop_name = bp::str())` | method | `bp::list` | public | Return all properties with given name in boost::python::list. |
| `feature_id()` | method | `bp::object` | public | — |
| `valid_time()` | method | `bp::tuple` | public | — |
| `begin_time()` | method | `bp::object` | public | — |
| `end_time()` | method | `bp::object` | public | — |
| `feature_type()` | method | `bp::object` | public | — |
| `plate_id()` | method | `unsigned long` | public | — |
| `get_all_property_names()` | method | `bp::list` | public | protected: |
| `get_property(bp::object name_)` | method | `bp::object` | public | — |
| `d_handle` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `export_feature()` | function | `void` | — |
| `GPLATES_API_FEATURE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=api/PyFeature tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/DrawStyleAdapters](../gui/DrawStyleAdapters.md) | gui | 17 |
| [api/PyFeatureCollection](PyFeatureCollection.md) | api | 7 |
| [api/PyViewportWindow](PyViewportWindow.md) | api | 4 |
| [api/PyCoregistrationLayerProxy](PyCoregistrationLayerProxy.md) | api | 2 |
| [api/PyTopologyTools](PyTopologyTools.md) | api | 2 |
| [api/PyColour](PyColour.md) | api | 1 |

## Related

**Python bindings**

| Python name | Kind | Owner | C++ |
|---|---|---|---|
| `Feature` | class | — | `GPlatesApi::Feature` |
| `get_properties` | method | `Feature` | `&GPlatesApi::Feature::get_properties` |
| `get_properties_by_name` | method | `Feature` | `&GPlatesApi::Feature::get_properties_by_name` |
| `plate_id` | method | `Feature` | `&GPlatesApi::Feature::plate_id` |
| `feature_id` | method | `Feature` | `&GPlatesApi::Feature::feature_id` |
| `feature_type` | method | `Feature` | `&GPlatesApi::Feature::feature_type` |
| `valid_time` | method | `Feature` | `&GPlatesApi::Feature::valid_time` |
| `begin_time` | method | `Feature` | `&GPlatesApi::Feature::begin_time` |
| `end_time` | method | `Feature` | `&GPlatesApi::Feature::end_time` |
| `get_all_property_names` | method | `Feature` | `&GPlatesApi::Feature::get_all_property_names` |
| `feature_id` | attribute | `Feature` | `&GPlatesApi::Feature::feature_id` |
| `feature_type` | attribute | `Feature` | `&GPlatesApi::Feature::feature_type` |
| `valid_time` | attribute | `Feature` | `&GPlatesApi::Feature::valid_time` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/PyFeature.h
python scripts/gpq.py def GPlatesApi::Feature --body
python scripts/gpq.py uses Feature --kind class
python scripts/gpq.py hier Feature
```

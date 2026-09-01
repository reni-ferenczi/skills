# PyFeature

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 301 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PyFeature.h` | C++ | 139 |
| `src/api/PyFeature.cc` | C++ | 279 |

## Overview

`GPlatesApi::Feature` is the Python-facing wrapper around a single
`GPlatesModel::FeatureHandle::weak_ref`, exposed to Python by `export_feature()`
as the `Feature` class. It translates the model's feature representation into
plain Python values: `feature_id()` and `feature_type()` return strings,
`valid_time()`/`begin_time()`/`end_time()` return the feature's time range as
numbers, and `plate_id()` resolves the reconstruction plate ID via
`GPlatesUtils::get_recon_plate_id_as_int`, defaulting to `0` when none is set.
Every accessor first checks `d_handle.is_valid()` and returns an empty
Python object (or `0`) if the underlying feature has since been destroyed,
since a `weak_ref` does not keep the feature alive.

Property access goes through `get_all_property_names()` and
`get_properties_by_name()` rather than exposing the property value objects
directly. `get_all_property_names()` walks the feature's top-level properties
and, for shapefile-imported features, unpacks the `shapefileAttributes`
`GpmlKeyValueDictionary` into individual `"shapefileAttributes:<key>"` names.
`get_properties_by_name()` reverses that: given a name, it either converts the
property value to a Python object with `GetPropertyAsPythonObjVisitor`, or,
for a shapefile attribute name, looks it up with
`GPlatesFeatureVisitors::ShapefileAttributeFinder` and converts the matching
`QVariant` by hand. `get_properties()` is just `get_all_property_names()`
combined with a `get_properties_by_name()` call per name.

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

`d_handle` is a `weak_ref`, not an owning reference: every method must (and
does) check `is_valid()` before dereferencing it, because the underlying
`FeatureHandle` can be destroyed while a `Feature` wrapper is still held on the
Python side. `get_property()` is declared under a `//protected:` comment but is
actually public — the access-control comment does not match the code.
`export_feature()` binds `feature_id`, `feature_type` and `valid_time` only as
methods; the commented-out `add_property` calls for the same names were never
enabled, so they must be called as `feature.feature_id()`, not accessed as
attributes, despite the "attribute" rows shown in Related above.

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

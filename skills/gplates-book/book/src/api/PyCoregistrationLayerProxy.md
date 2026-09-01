# PyCoregistrationLayerProxy

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 1240 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PyCoregistrationLayerProxy.h` | C++ | 74 |
| `src/api/PyCoregistrationLayerProxy.cc` | C++ | 143 |

## Overview

`PyCoregistrationLayerProxy` is a Python wrapper around `GPlatesAppLogic::CoRegistrationLayerProxy` that exposes the results of the co-registration layer to Python scripts. It provides access to seed features, association configurations, and tabular coregistration data. The `get_coregistration_data()` methods retrieve the computed data table for a specified time (or use the current reconstruction time), making the results of spatio-temporal data mining operations available to Python.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::PyCoregistrationLayerProxy`](#gplatesapipycoregistrationlayerproxy) | class | — | — | 0 | Wrapper around CoregistrationLayerProxy. |

## Members

### `GPlatesApi::PyCoregistrationLayerProxy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PyCoregistrationLayerProxy( GPlatesAppLogic::CoRegistrationLayerProxy::non_null_ptr_type proxy)` | constructor | `None` | public | — |
| `get_all_seed_features()` | method | `bp::list` | public | — |
| `get_associations()` | method | `bp::list` | public | — |
| `get_coregistration_data( float time)` | method | `bp::list` | public | — |
| `get_coregistration_data()` | method | `bp::list` | public | — |
| `d_proxy` | field | `GPlatesAppLogic::CoRegistrationLayerProxy::non_null_ptr_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `export_coregistration_layer_proxy()` | function | `void` | — |
| `GPLATES_API_COREGISTRATIONPROXY_H` | macro | `None` | — |

## Notes

The `get_coregistration_data()` methods require an active OpenGL context and renderer for computing the data table. The wrapper deduplicates seed features by tracking handles to avoid returning the same feature multiple times.

## Used by

*Nothing in the tree references this unit.*

## Related

**Python bindings**

| Python name | Kind | Owner | C++ |
|---|---|---|---|
| `CoregistrationLayerProxy` | class | — | `PyCoregistrationLayerProxy` |
| `get_all_seed_features` | method | `CoregistrationLayerProxy` | `&PyCoregistrationLayerProxy::get_all_seed_features` |
| `get_associations` | method | `CoregistrationLayerProxy` | `&PyCoregistrationLayerProxy::get_associations` |
| `get_coregistration_data` | method | `CoregistrationLayerProxy` | `get_current_coreg_data` |
| `get_coregistration_data` | method | `CoregistrationLayerProxy` | `get_coreg_data` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/PyCoregistrationLayerProxy.h
python scripts/gpq.py def GPlatesApi::PyCoregistrationLayerProxy --body
python scripts/gpq.py uses PyCoregistrationLayerProxy --kind class
python scripts/gpq.py hier PyCoregistrationLayerProxy
```

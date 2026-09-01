# PyCoregistrationLayerProxy

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 1240 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PyCoregistrationLayerProxy.h` | C++ | 74 |
| `src/api/PyCoregistrationLayerProxy.cc` | C++ | 143 |

## Overview

[[[PROSE overview unit=api/PyCoregistrationLayerProxy tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=api/PyCoregistrationLayerProxy tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

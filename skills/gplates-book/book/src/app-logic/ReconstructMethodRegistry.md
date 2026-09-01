# ReconstructMethodRegistry

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 416 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructMethodRegistry.h` | C++ | 249 |
| `src/app-logic/ReconstructMethodRegistry.cc` | C++ | 329 |

## Overview

`ReconstructMethodRegistry` decouples feature reconstruction from any single `ReconstructMethodInterface` implementation: each `ReconstructMethod::Type` is registered as a pair of `boost::function` callbacks — one to test whether a feature qualifies (`can_reconstruct_feature_function_type`), one to construct the method (`create_reconstruct_method_function_type`) — stored in `d_reconstruct_method_info_map`. By default the constructor calls `register_default_reconstruct_method_types`, which wires up the built-in methods (`BY_PLATE_ID`, `HALF_STAGE_ROTATION`, `VIRTUAL_GEOMAGNETIC_POLE`, `FLOWLINE`, `MOTION_PATH`, `SMALL_CIRCLE`) bound to their respective classes' static `can_reconstruct_feature`/`create` functions.

`get_reconstruct_method_type` and `create_reconstruct_method` pick the matching method for a feature by scanning `ReconstructMethod::Type` values from the highest enumerator down, so any specialised method registered with a higher enum value is preferred over `BY_PLATE_ID` when both can handle the same feature — `BY_PLATE_ID` is deliberately the catch-all, tried last. The `_or_default` variants exist because callers usually want a reconstruct method unconditionally; they fall back to `BY_PLATE_ID` rather than propagating `boost::none`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructMethodRegistry`](#gplatesapplogicreconstructmethodregistry) | class | `boost::noncopyable` | — | 0 | Registry for information required to find and create ReconstructMethodInterface objects. |

## Members

### `GPlatesAppLogic::ReconstructMethodRegistry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `can_reconstruct_feature_function_type` | typedef | `boost::function<bool (const GPlatesModel::FeatureHandle::const_weak_ref &)>` | public | Convenience typedef for a function that determines if a reconstruct method can reconstruct a feature. |
| `create_reconstruct_method_function_type` | typedef | `boost::function< ReconstructMethodInterface::non_null_ptr_type ( const GPlatesModel::FeatureHandle::weak_ref &, const ReconstructMethodInterface::Context &)>` | public | Convenience typedef for a function that creates a ReconstructMethodInterface. |
| `ReconstructMethodRegistry( bool register_default_reconstruct_method_types_ = true)` | constructor | `None` | public | Constructor. |
| `register_default_reconstruct_method_types()` | method | `void` | public | Registers information about the default reconstruct method types. |
| `register_reconstruct_method( ReconstructMethod::Type reconstruct_method_type, const can_reconstruct_feature_function_type &can_reconstruct_feature_function_, const create_reconstruct_method_function_type &create_reconstruct_method_function_)` | method | `void` | public | Registers information about the given reconstruct\_method\_type. |
| `unregister_reconstruct_method( ReconstructMethod::Type reconstruct_method_type)` | method | `void` | public | Unregisters the specified reconstruct method. |
| `get_registered_reconstruct_methods()` | method | `std::vector<ReconstructMethod::Type>` | public | Returns a list of reconstruct method types of all registered reconstruct methods. |
| `can_reconstruct_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref)` | method | `bool` | public | Returns true if the specified feature can be reconstructed by \*any\* registered reconstruct methods. |
| `can_reconstruct_feature( ReconstructMethod::Type reconstruct_method_type, const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref)` | method | `bool` | public | Returns true if the specified feature can be reconstructed by the specified reconstruct method. |
| `get_reconstruct_method_type( const GPlatesModel::FeatureHandle::weak_ref &feature_ref)` | method | `boost::optional<ReconstructMethod::Type>` | public | Returns the first reconstruct method type that can reconstruct the specified feature. |
| `create_reconstruct_method( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const ReconstructMethodInterface::Context &reconstruct_method_context)` | method | `boost::optional<ReconstructMethodInterface::non_null_ptr_type>` | public | Creates a reconstruct method of the first type that can reconstruct the specified feature. |
| `get_reconstruct_method_or_default_type( const GPlatesModel::FeatureHandle::weak_ref &feature_ref)` | method | `ReconstructMethod::Type` | public | Same as get\_reconstruct\_method\_type but returns a 'BY\_PLATE\_ID' reconstruct method type if no reconstruct method types could be found. |
| `create_reconstruct_method_or_default( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const ReconstructMethodInterface::Context &reconstruct_method_context)` | method | `ReconstructMethodInterface::non_null_ptr_type` | public | Same as create\_reconstruct\_method but creates a 'BY\_PLATE\_ID' reconstruct method if no reconstruct method types could be found. reconstruct\_method\_context is the context in which the reconstruct method performs reconstructions. |
| `create_reconstruct_method( const ReconstructMethodInterface &reconstruct_method, const ReconstructMethodInterface::Context &reconstruct_method_context)` | method | `ReconstructMethodInterface::non_null_ptr_type` | public | Creates a new reconstruct method of the same type, and associated with the same feature, as the specified reconstruct method but with the specified context data. |
| `create_reconstruct_method( ReconstructMethod::Type reconstruct_method_type, const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const ReconstructMethodInterface::Context &reconstruct_method_context)` | method | `ReconstructMethodInterface::non_null_ptr_type` | public | Creates a new reconstruct method of the specified type, and associated with the specified feature, but with the context data specified. |
| `ReconstructMethodInfo` | struct | `None` | private | — |
| `reconstruct_method_info_map_type` | typedef | `std::map<ReconstructMethod::Type, ReconstructMethodInfo>` | private | — |
| `d_reconstruct_method_info_map` | field | `reconstruct_method_info_map_type` | private | Stores a struct of information for each reconstruct method type. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTMETHODREGISTRY_H` | macro | `None` | — |

## Notes

- `can_reconstruct_feature(ReconstructMethod::Type, ...)`, `create_reconstruct_method_or_default` and the type-taking overload of `create_reconstruct_method` throw `PreconditionViolationError` if the given `reconstruct_method_type` (or, for the default case, `BY_PLATE_ID`) was never registered.
- The type-taking `create_reconstruct_method` does not verify that the given type actually matches the feature; the caller is expected to have already established that with `get_reconstruct_method_type`.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/FeatureCollectionFileFormatClassify](../file-io/FeatureCollectionFileFormatClassify.md) | file-io | 10 |
| [app-logic/ReconstructContext](ReconstructContext.md) | app-logic | 4 |
| [app-logic/ReconstructUtils](ReconstructUtils.md) | app-logic | 4 |
| [api/PyFunctions](../api/PyFunctions.md) | api | 1 |
| [app-logic/ApplicationState](ApplicationState.md) | app-logic | 1 |
| [app-logic/GeometryCookieCutter](GeometryCookieCutter.md) | app-logic | 1 |
| [app-logic/PartitionFeatureUtils](PartitionFeatureUtils.md) | app-logic | 1 |
| [app-logic/ReconstructLayerTask](ReconstructLayerTask.md) | app-logic | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructMethodRegistry.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructMethodRegistry --body
python scripts/gpq.py uses ReconstructMethodRegistry --kind class
python scripts/gpq.py hier ReconstructMethodRegistry
```

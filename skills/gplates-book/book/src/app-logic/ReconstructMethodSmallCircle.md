# ReconstructMethodSmallCircle

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 81 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructMethodSmallCircle.h` | C++ | 121 |
| `src/app-logic/ReconstructMethodSmallCircle.cc` | C++ | 217 |

## Overview

This is a reconstruction method for small circle features, which are circles on a sphere defined by a centre point and a radius. `ReconstructMethodSmallCircle` inherits from `ReconstructMethodInterface` and implements feature reconstruction by rotating the centre point according to a plate circuit. The centre is stored as a `GmlPoint` property and reconstructed using the feature's reconstruction plate ID via `SmallCircleGeometryPopulator`. If no reconstruction plate ID is present, the method defaults to plate ID 0 (the spin axis), which may still apply rotations if an anchor plate is defined.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::(anonymous)::CanReconstructFeature`](#gplatesapplogicanonymouscanreconstructfeature) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Used to determine if can reconstruct a feature. |
| [`GPlatesAppLogic::(anonymous)::GetPresentDayGeometries`](#gplatesapplogicanonymousgetpresentdaygeometries) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Finds the present day geometries of a feature. |
| [`GPlatesAppLogic::ReconstructMethodSmallCircle`](#gplatesapplogicreconstructmethodsmallcircle) | class | [`ReconstructMethodInterface`](ReconstructMethodInterface.md) | — | 0 | Reconstructs a virtual geomagnetic pole feature. |

## Members

### `GPlatesAppLogic::(anonymous)::CanReconstructFeature`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CanReconstructFeature()` | constructor | `None` | public | — |
| `can_reconstruct()` | method | `bool` | public | Returns true any features visited by us can be reconstructed. |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | private | — |
| `d_can_reconstruct` | field | `bool` | private | — |

### `GPlatesAppLogic::(anonymous)::GetPresentDayGeometries`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GetPresentDayGeometries( std::vector<ReconstructMethodInterface::Geometry> &present_day_geometries)` | constructor | `None` | public | — |
| `visit_gml_point( GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `d_present_day_geometries` | field | `std::vector<ReconstructMethodInterface::Geometry>` | private | — |

### `GPlatesAppLogic::ReconstructMethodSmallCircle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructMethodSmallCircle>` | public | Convenience typedefs for a shared pointer to a ReconstructMethodVirtualGeomagneticPole. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructMethodSmallCircle>` | public | — |
| `can_reconstruct_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature_weak_ref)` | method | `bool` | public | Returns true if can reconstruct the specified feature. |
| `create( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const Context &context)` | method | `ReconstructMethodSmallCircle::non_null_ptr_type` | public | Creates a ReconstructMethodSmallCircle object associated with the specified feature. |
| `get_present_day_feature_geometries( std::vector<Geometry> &present_day_geometries)` | method | `void` | public | Returns the present day geometries of the feature associated with this reconstruct method. |
| `reconstruct_feature_geometries( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const ReconstructHandle::type &reconstruct_handle, const Context &context, const double &reconstruction_time)` | method | `void` | public | Reconstructs the feature associated with this reconstruct method to the specified reconstruction time and returns one or more reconstructed feature geometries. |
| `reconstruct_geometry( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry, const Context &context, const double &reconstruction_time, bool reverse_reconstruct)` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | Reconstructs the specified geometry from present day to the specified reconstruction time - unless reverse\_reconstruct is true in which case the geometry is assumed to be the reconstructed geometry (at the reconstruction time) and the ... |
| `ReconstructMethodSmallCircle( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const Context &context)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTMETHODSMALLCIRCLE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructMethodRegistry](ReconstructMethodRegistry.md) | app-logic | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructMethodSmallCircle.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructMethodSmallCircle --body
python scripts/gpq.py uses ReconstructMethodSmallCircle --kind class
python scripts/gpq.py hier ReconstructMethodSmallCircle
```

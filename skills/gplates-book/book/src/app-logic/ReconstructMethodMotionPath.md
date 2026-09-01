# ReconstructMethodMotionPath

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 44 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructMethodMotionPath.h` | C++ | 122 |
| `src/app-logic/ReconstructMethodMotionPath.cc` | C++ | 177 |

## Overview

A `ReconstructMethodInterface` that reconstructs motion path features by reconstructing the path a point traces through time under plate motion. The method extracts present-day seed points and reconstructs them at various times using a `MotionPathGeometryPopulator` to generate the full motion path geometries.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::(anonymous)::GetPresentDayGeometries`](#gplatesapplogicanonymousgetpresentdaygeometries) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Finds the present day geometries of a MotionPath feature. |
| [`GPlatesAppLogic::ReconstructMethodMotionPath`](#gplatesapplogicreconstructmethodmotionpath) | class | [`ReconstructMethodInterface`](ReconstructMethodInterface.md) | — | 0 | Reconstructs a MotionPath feature. |

## Members

### `GPlatesAppLogic::(anonymous)::GetPresentDayGeometries`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GetPresentDayGeometries( std::vector<ReconstructMethodInterface::Geometry> &present_day_geometries)` | constructor | `None` | public | — |
| `visit_gml_multi_point( GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | private | — |
| `visit_gml_point( GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `d_present_day_geometries` | field | `std::vector<ReconstructMethodInterface::Geometry>` | private | — |

### `GPlatesAppLogic::ReconstructMethodMotionPath`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructMethodMotionPath>` | public | Convenience typedefs for a shared pointer to a ReconstructMethodMotionPath. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructMethodMotionPath>` | public | — |
| `can_reconstruct_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature_weak_ref)` | method | `bool` | public | Returns true if can reconstruct the specified feature. |
| `create( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const Context &context)` | method | `ReconstructMethodMotionPath::non_null_ptr_type` | public | Creates a ReconstructMethodMotionPath object associated with the specified feature. |
| `get_present_day_feature_geometries( std::vector<Geometry> &present_day_geometries)` | method | `void` | public | Returns the present day geometries of the feature associated with this reconstruct method. |
| `reconstruct_feature_geometries( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const ReconstructHandle::type &reconstruct_handle, const Context &context, const double &reconstruction_time)` | method | `void` | public | Reconstructs the feature associated with this reconstruct method to the specified reconstruction time and returns one or more reconstructed feature geometries. |
| `reconstruct_geometry( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry, const Context &context, const double &reconstruction_time, bool reverse_reconstruct)` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | Reconstructs the specified geometry from present day to the specified reconstruction time - unless reverse\_reconstruct is true in which case the geometry is assumed to be the reconstructed geometry (at the reconstruction time) and the ... |
| `ReconstructMethodMotionPath( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const Context &context)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTMETHODMOTIONPATH_H` | macro | `None` | — |

## Notes

Motion path features are designed to represent a single path through time; present-day geometries are the seed points or multipoints used to initialize motion path reconstruction.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructMethodRegistry](ReconstructMethodRegistry.md) | app-logic | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructMethodMotionPath.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructMethodMotionPath --body
python scripts/gpq.py uses ReconstructMethodMotionPath --kind class
python scripts/gpq.py hier ReconstructMethodMotionPath
```

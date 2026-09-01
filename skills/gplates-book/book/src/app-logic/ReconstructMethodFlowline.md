# ReconstructMethodFlowline

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 81 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructMethodFlowline.h` | C++ | 138 |
| `src/app-logic/ReconstructMethodFlowline.cc` | C++ | 307 |

## Overview

A `ReconstructMethodInterface` that reconstructs flowline features by reconstructing the path a single point (the seed point) traces as it moves through time under plate motion. The method extracts present-day seed points (points or multipoints) and reconstructs them to past times using a `FlowlineGeometryPopulator`. It also supports velocity calculations at reconstructed positions.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::(anonymous)::GetPresentDayGeometries`](#gplatesapplogicanonymousgetpresentdaygeometries) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Finds the present day geometries of a flowline feature. |
| [`GPlatesAppLogic::ReconstructMethodFlowline`](#gplatesapplogicreconstructmethodflowline) | class | [`ReconstructMethodInterface`](ReconstructMethodInterface.md) | — | 0 | Reconstructs a flowline feature. |

## Members

### `GPlatesAppLogic::(anonymous)::GetPresentDayGeometries`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GetPresentDayGeometries( std::vector<ReconstructMethodInterface::Geometry> &present_day_geometries)` | constructor | `None` | public | — |
| `visit_gml_multi_point( GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | private | — |
| `visit_gml_point( GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `d_present_day_geometries` | field | `std::vector<ReconstructMethodInterface::Geometry>` | private | — |

### `GPlatesAppLogic::ReconstructMethodFlowline`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructMethodFlowline>` | public | Convenience typedefs for a shared pointer to a ReconstructMethodFlowline. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructMethodFlowline>` | public | — |
| `can_reconstruct_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature_weak_ref)` | method | `bool` | public | Returns true if can reconstruct the specified feature. |
| `create( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const Context &context)` | method | `ReconstructMethodFlowline::non_null_ptr_type` | public | Creates a ReconstructMethodFlowline object associated with the specified feature. |
| `get_present_day_feature_geometries( std::vector<Geometry> &present_day_geometries)` | method | `void` | public | Returns the present day geometries of the feature associated with this reconstruct method. |
| `reconstruct_feature_geometries( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const ReconstructHandle::type &reconstruct_handle, const Context &context, const double &reconstruction_time)` | method | `void` | public | Reconstructs the feature associated with this reconstruct method to the specified reconstruction time and returns one or more reconstructed feature geometries. |
| `reconstruct_feature_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &reconstructed_feature_velocities, const ReconstructHandle::type &reconstruct_handle, const Context &context, const double &reconstruction_time, const double &velocity_delta_time, VelocityDeltaTime::Type velocity_delta_time_type)` | method | `void` | public | Calculates velocities at the positions of the reconstructed feature geometries, of the feature associated with this reconstruct method, at the specified reconstruction time and returns one or more reconstructed feature \*velocities\*. |
| `reconstruct_geometry( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry, const Context &context, const double &reconstruction_time, bool reverse_reconstruct)` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | Reconstructs the specified geometry from present day to the specified reconstruction time - unless reverse\_reconstruct is true in which case the geometry is assumed to be the reconstructed geometry (at the reconstruction time) and the ... |
| `ReconstructMethodFlowline( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const Context &context)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTMETHODFLOWLINE_H` | macro | `None` | — |

## Notes

Flowlines are designed to represent a single path through time; present-day geometries are the seed points or multipoints used to initialize the flow.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructMethodRegistry](ReconstructMethodRegistry.md) | app-logic | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructMethodFlowline.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructMethodFlowline --body
python scripts/gpq.py uses ReconstructMethodFlowline --kind class
python scripts/gpq.py hier ReconstructMethodFlowline
```

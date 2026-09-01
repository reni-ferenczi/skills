# ReconstructMethodHalfStageRotation

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 190 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructMethodHalfStageRotation.h` | C++ | 140 |
| `src/app-logic/ReconstructMethodHalfStageRotation.cc` | C++ | 698 |

## Overview

A `ReconstructMethodInterface` that reconstructs features using a half-stage rotation defined by left and right plate IDs. The method extracts the feature's present-day geometry and rotates it using a finite rotation derived from the left/right plate plate circuit. It delegates geometry reconstruction to inner visitor classes and supports velocity calculations at reconstructed positions.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::(anonymous)::Transform`](#gplatesapplogicanonymoustransform) | class | [`ReconstructMethodFiniteRotation`](ReconstructMethodFiniteRotation.md) | — | 0 | The transform used to reconstruct by half-stage-rotation of left/right plate ids. |
| [`GPlatesAppLogic::(anonymous)::CanReconstructFeature`](#gplatesapplogicanonymouscanreconstructfeature) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Used to determine if can reconstruct a feature. |
| [`GPlatesAppLogic::(anonymous)::GetPresentDayGeometries`](#gplatesapplogicanonymousgetpresentdaygeometries) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Finds the present day geometries of a feature. |
| [`GPlatesAppLogic::(anonymous)::ReconstructFeature`](#gplatesapplogicanonymousreconstructfeature) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Reconstructs a feature using its present day geometry and left/right plate Ids. |
| [`GPlatesAppLogic::ReconstructMethodHalfStageRotation`](#gplatesapplogicreconstructmethodhalfstagerotation) | class | [`ReconstructMethodInterface`](ReconstructMethodInterface.md) | — | 0 | Reconstructs a feature using its present day geometry and a half-stage rotation defined by its left and right plate id. |

## Members

### `GPlatesAppLogic::(anonymous)::Transform`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<Transform>` | public | Convenience typedefs for a shared pointer to a Transform. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const Transform>` | public | — |
| `create( const GPlatesMaths::FiniteRotation &finite_rotation, GPlatesModel::integer_plate_id_type left_plate_id, GPlatesModel::integer_plate_id_type right_plate_id)` | method | `non_null_ptr_type` | public | Create a transform if have a left/right plate ids. |
| `create()` | method | `non_null_ptr_type` | public | Create an identity transform if do \*not\* have a left/right plate ids. |
| `d_left_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `d_right_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `Transform( const GPlatesMaths::FiniteRotation &finite_rotation, GPlatesModel::integer_plate_id_type left_plate_id, GPlatesModel::integer_plate_id_type right_plate_id)` | constructor | `None` | private | — |
| `Transform()` | constructor | `None` | private | — |
| `less_than_compare_finite_rotation_parameters( const ReconstructMethodFiniteRotation &rhs_base)` | method | `bool` | private | — |

### `GPlatesAppLogic::(anonymous)::CanReconstructFeature`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CanReconstructFeature()` | constructor | `None` | public | — |
| `can_reconstruct()` | method | `bool` | public | Returns true any features visited by us can be reconstructed. |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | private | — |
| `finalise_post_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | private | — |
| `visit_gml_line_string( const GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | private | — |
| `visit_gml_multi_point( const GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | private | — |
| `visit_gml_orientable_curve( const GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | private | — |
| `visit_gml_point( const GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gml_polygon( const GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | private | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `d_can_reconstruct` | field | `bool` | private | — |
| `d_has_geometry` | field | `bool` | private | — |

### `GPlatesAppLogic::(anonymous)::GetPresentDayGeometries`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GetPresentDayGeometries( std::vector<ReconstructMethodInterface::Geometry> &present_day_geometries)` | constructor | `None` | public | — |
| `visit_gml_line_string( GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | private | — |
| `visit_gml_multi_point( GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | private | — |
| `visit_gml_orientable_curve( GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | private | — |
| `visit_gml_point( GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gml_polygon( GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | private | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `d_present_day_geometries` | field | `std::vector<ReconstructMethodInterface::Geometry>` | private | — |

### `GPlatesAppLogic::(anonymous)::ReconstructFeature`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ReconstructFeature( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const ReconstructHandle::type &reconstruct_handle, const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree, const ReconstructionTreeCreator &reconstruction_tree_creator)` | constructor | `None` | public | — |
| `initialise_pre_feature_properties( GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | protected | — |
| `visit_gml_line_string( GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | protected | — |
| `visit_gml_multi_point( GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | protected | — |
| `visit_gml_orientable_curve( GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | protected | — |
| `visit_gml_point( GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | protected | — |
| `visit_gml_polygon( GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | protected | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | protected | — |
| `d_reconstruct_handle` | field | `ReconstructHandle::type` | private | — |
| `d_reconstruction_tree` | field | `ReconstructionTree::non_null_ptr_to_const_type` | private | — |
| `d_reconstruction_tree_creator` | field | `ReconstructionTreeCreator` | private | — |
| `d_reconstruction_params` | field | `ReconstructionFeatureProperties` | private | — |
| `d_reconstruction_rotation` | field | `boost::optional<Transform::non_null_ptr_type>` | private | — |
| `d_reconstructed_feature_geometries` | field | `std::vector<ReconstructedFeatureGeometry::non_null_ptr_type>` | private | The ReconstructedFeatureGeometry objects generated during reconstruction. |

### `GPlatesAppLogic::ReconstructMethodHalfStageRotation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructMethodHalfStageRotation>` | public | Convenience typedefs for a shared pointer to a ReconstructMethodHalfStageRotation. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructMethodHalfStageRotation>` | public | — |
| `can_reconstruct_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature_weak_ref)` | method | `bool` | public | Returns true if can reconstruct the specified feature. |
| `create( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const Context &context)` | method | `ReconstructMethodHalfStageRotation::non_null_ptr_type` | public | Creates a ReconstructMethodHalfStageRotation object associated with the specified feature. |
| `get_present_day_feature_geometries( std::vector<Geometry> &present_day_geometries)` | method | `void` | public | Returns the present day geometries of the feature associated with this reconstruct method. |
| `reconstruct_feature_geometries( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const ReconstructHandle::type &reconstruct_handle, const Context &context, const double &reconstruction_time)` | method | `void` | public | Reconstructs the feature associated with this reconstruct method to the specified reconstruction time and returns one or more reconstructed feature geometries. |
| `reconstruct_feature_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &reconstructed_feature_velocities, const ReconstructHandle::type &reconstruct_handle, const Context &context, const double &reconstruction_time, const double &velocity_delta_time, VelocityDeltaTime::Type velocity_delta_time_type)` | method | `void` | public | Calculates velocities at the positions of the reconstructed feature geometries, of the feature associated with this reconstruct method, at the specified reconstruction time and returns one or more reconstructed feature \*velocities\*. |
| `reconstruct_geometry( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry, const Context &context, const double &reconstruction_time, bool reverse_reconstruct)` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | Reconstructs the specified geometry from present day to the specified reconstruction time - unless reverse\_reconstruct is true in which case the geometry is assumed to be the reconstructed geometry (at the reconstruction time) and the ... |
| `ReconstructMethodHalfStageRotation( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const Context &context)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTMETHODHALFSTAGEROTATION_H` | macro | `None` | — |

## Notes

The reconstruction method requires features to have a "HalfStageRotation" reconstruction method property and left and right plate properties; features matching these criteria can be reconstructed.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructMethodRegistry](ReconstructMethodRegistry.md) | app-logic | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructMethodHalfStageRotation.h
python scripts/gpq.py def GPlatesAppLogic::(anonymous)::ReconstructFeature --body
python scripts/gpq.py uses ReconstructFeature --kind class
python scripts/gpq.py hier ReconstructFeature
```

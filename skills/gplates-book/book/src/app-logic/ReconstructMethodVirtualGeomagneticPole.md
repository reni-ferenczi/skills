# ReconstructMethodVirtualGeomagneticPole

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 401 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructMethodVirtualGeomagneticPole.h` | C++ | 122 |
| `src/app-logic/ReconstructMethodVirtualGeomagneticPole.cc` | C++ | 440 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructMethodVirtualGeomagneticPole tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::(anonymous)::Transform`](#gplatesapplogicanonymoustransform) | class | [`ReconstructMethodFiniteRotation`](ReconstructMethodFiniteRotation.md) | — | 0 | The transform used to reconstruct by plate id. |
| [`GPlatesAppLogic::(anonymous)::CanReconstructFeature`](#gplatesapplogicanonymouscanreconstructfeature) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Used to determine if can reconstruct a feature. |
| [`GPlatesAppLogic::(anonymous)::GetPresentDayGeometries`](#gplatesapplogicanonymousgetpresentdaygeometries) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Finds the present day geometries of a feature. |
| [`GPlatesAppLogic::(anonymous)::ReconstructFeature`](#gplatesapplogicanonymousreconstructfeature) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Reconstructs a feature using its present day geometry and left/right plate Ids. |
| [`GPlatesAppLogic::ReconstructMethodVirtualGeomagneticPole`](#gplatesapplogicreconstructmethodvirtualgeomagneticpole) | class | [`ReconstructMethodInterface`](ReconstructMethodInterface.md) | — | 0 | Reconstructs a virtual geomagnetic pole feature. |

## Members

### `GPlatesAppLogic::(anonymous)::Transform`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<Transform>` | public | Convenience typedefs for a shared pointer to a Transform. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const Transform>` | public | — |
| `create( const GPlatesMaths::FiniteRotation &finite_rotation, GPlatesModel::integer_plate_id_type reconstruction_plate_id)` | method | `non_null_ptr_type` | public | Create a transform if have a reconstruction plate id. |
| `create()` | method | `non_null_ptr_type` | public | Create an identity transform if do \*not\* have a reconstruction plate id. |
| `d_reconstruction_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `Transform( const GPlatesMaths::FiniteRotation &finite_rotation, GPlatesModel::integer_plate_id_type reconstruction_plate_id)` | constructor | `None` | private | — |
| `Transform()` | constructor | `None` | private | — |
| `less_than_compare_finite_rotation_parameters( const ReconstructMethodFiniteRotation &rhs)` | method | `bool` | private | — |

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

### `GPlatesAppLogic::(anonymous)::ReconstructFeature`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ReconstructFeature( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const ReconstructHandle::type &reconstruct_handle, const ReconstructParams &reconstruct_params, const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree, const ReconstructionTreeCreator & ...` | constructor | `None` | public | — |
| `initialise_pre_feature_properties( GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | protected | — |
| `finalise_post_feature_properties( GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | protected | — |
| `visit_gml_point( GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | protected | — |
| `visit_xs_double( GPlatesPropertyValues::XsDouble &xs_double)` | method | `void` | protected | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | protected | — |
| `d_reconstruct_handle` | field | `ReconstructHandle::type` | private | — |
| `d_reconstruction_tree` | field | `ReconstructionTree::non_null_ptr_to_const_type` | private | — |
| `d_reconstruction_tree_creator` | field | `ReconstructionTreeCreator` | private | — |
| `d_reconstruct_params` | field | `ReconstructParams` | private | — |
| `d_reconstruction_params` | field | `ReconstructionFeatureProperties` | private | — |
| `d_VGP_params` | field | `ReconstructedVirtualGeomagneticPoleParams` | private | — |
| `d_reconstruction_rotation` | field | `boost::optional<Transform::non_null_ptr_type>` | private | — |
| `d_reconstructed_feature_geometries` | field | `std::vector<ReconstructedFeatureGeometry::non_null_ptr_type>` | private | The ReconstructedFeatureGeometry objects generated during reconstruction. |

### `GPlatesAppLogic::ReconstructMethodVirtualGeomagneticPole`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructMethodVirtualGeomagneticPole>` | public | Convenience typedefs for a shared pointer to a ReconstructMethodVirtualGeomagneticPole. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructMethodVirtualGeomagneticPole>` | public | — |
| `can_reconstruct_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature_weak_ref)` | method | `bool` | public | Returns true if can reconstruct the specified feature. |
| `create( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const Context &context)` | method | `ReconstructMethodVirtualGeomagneticPole::non_null_ptr_type` | public | Creates a ReconstructMethodHalfStageRotation object associated with the specified feature. |
| `get_present_day_feature_geometries( std::vector<Geometry> &present_day_geometries)` | method | `void` | public | Returns the present day geometries of the feature associated with this reconstruct method. |
| `reconstruct_feature_geometries( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const ReconstructHandle::type &reconstruct_handle, const Context &context, const double &reconstruction_time)` | method | `void` | public | Reconstructs the feature associated with this reconstruct method to the specified reconstruction time and returns one or more reconstructed feature geometries. |
| `reconstruct_geometry( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry, const Context &context, const double &reconstruction_time, bool reverse_reconstruct)` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | Reconstructs the specified geometry from present day to the specified reconstruction time - unless reverse\_reconstruct is true in which case the geometry is assumed to be the reconstructed geometry (at the reconstruction time) and the ... |
| `ReconstructMethodVirtualGeomagneticPole( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const Context &context)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTMETHODVIRTUALGEOMAGNETICPOLE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructMethodVirtualGeomagneticPole tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructMethodRegistry](ReconstructMethodRegistry.md) | app-logic | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructMethodVirtualGeomagneticPole.h
python scripts/gpq.py def GPlatesAppLogic::(anonymous)::ReconstructFeature --body
python scripts/gpq.py uses ReconstructFeature --kind class
python scripts/gpq.py hier ReconstructFeature
```

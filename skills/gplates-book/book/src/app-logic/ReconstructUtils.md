# ReconstructUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 2 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructUtils.h` | C++ | 472 |
| `src/app-logic/ReconstructUtils.cc` | C++ | 398 |

## Overview

`ReconstructUtils` is the free-function entry point for reconstructing feature geometry to a palaeo time; the sibling `RotationUtils` header holds the pure-rotation helpers that don't touch geometry. Its `reconstruct` overloads drive the whole `ReconstructMethodRegistry`/`ReconstructMethodInterface` machinery: given a set of reconstructable feature collections, a set of reconstruction feature collections (or a `ReconstructionTreeCreator` already built from them), a reconstruction time and an anchor plate ID, they pick the right `ReconstructMethodInterface` for each feature and produce either `ReconstructedFeatureGeometry`, `ReconstructContext::Reconstruction` or `ReconstructContext::ReconstructedFeature` objects, tagging every result with one freshly-allocated `ReconstructHandle::type`. A `ReconstructionTreeCreator` rather than a single `ReconstructionTree` is threaded through because some reconstruct methods (flowlines, half-stage rotation) need reconstruction trees at times other than the target time.

`reconstruct_geometry` reconstructs (or reverse-reconstructs) a single geometry using the properties of one feature as the source of reconstruction parameters, without touching that feature's own stored geometry — the documented use case is round-tripping an edited geometry back to present day before writing it into a feature, since features store present-day geometry. `reconstruct_by_plate_id`, `reconstruct_as_half_stage` (two overloads) are templated on `GeometryType` and apply a `FiniteRotation` directly via `operator*`, forming the low-level primitives that the `ReconstructMethodByPlateId` and half-stage-rotation reconstruct methods build on; `is_reconstruction_feature`/`is_reconstructable_feature` and their `has_*` collection-level counterparts classify features as rotation-sequence sources versus geometry to be reconstructed.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTUTILS_H` | macro | `None` | — |
| `is_reconstruction_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref)` | function | `bool` | Returns true if feature\_ref is a reconstruction feature. |
| `has_reconstruction_features( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection)` | function | `bool` | Returns true if feature\_collection contains any features that pass the is\_reconstruction\_feature test. |
| `is_reconstructable_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref, const ReconstructMethodRegistry &reconstruct_method_registry)` | function | `bool` | Returns true if feature\_ref is reconstructable. |
| `is_reconstructable_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref)` | function | `bool` | Same as other overload of is\_reconstructable\_feature but creates a temporary ReconstructMethodRegistry object internally. |
| `has_reconstructable_features( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection, const ReconstructMethodRegistry &reconstruct_method_registry)` | function | `bool` | Returns true if feature\_collection contains any features that pass the is\_reconstructable\_feature test. reconstruct\_method\_registry used to determined if the features are reconstructable. |
| `has_reconstructable_features( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection)` | function | `bool` | Same as other overload of is\_reconstructable\_feature but creates a temporary ReconstructMethodRegistry object internally. |
| `reconstruct( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const double &reconstruction_time, const ReconstructMethodRegistry &reconstruct_method_registry, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &reconstructable_features_collection, const Rec ...` | function | `ReconstructHandle::type` | Generate ReconstructedFeatureGeometry objects by reconstructing feature geometries in reconstructable\_features\_collection using reconstruction trees obtained from reconstruction\_tree\_creator. |
| `reconstruct( std::vector<ReconstructContext::Reconstruction> &reconstructions, const double &reconstruction_time, const ReconstructMethodRegistry &reconstruct_method_registry, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &reconstructable_features_collection, const ReconstructionTreeCreator &recons ...` | function | `ReconstructHandle::type` | Same as reconstruct overload for ReconstructedFeatureGeometry except generates ReconstructContext::Reconstruction instances instead. |
| `reconstruct( std::vector<ReconstructContext::ReconstructedFeature> &reconstructed_features, const double &reconstruction_time, const ReconstructMethodRegistry &reconstruct_method_registry, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &reconstructable_features_collection, const ReconstructionTreeCr ...` | function | `ReconstructHandle::type` | Same as reconstruct overload for ReconstructedFeatureGeometry except generates ReconstructContext::ReconstructedFeature instances instead. |
| `reconstruct( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const double &reconstruction_time, GPlatesModel::integer_plate_id_type anchor_plate_id, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &reconstructable_features_collection, const std::vector< ...` | function | `ReconstructHandle::type` | Same as other overload of reconstruct but creates temporary ReconstructMethodRegistry and cached reconstruction tree creator objects internally. |
| `reconstruct( std::vector<ReconstructContext::Reconstruction> &reconstructions, const double &reconstruction_time, GPlatesModel::integer_plate_id_type anchor_plate_id, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &reconstructable_features_collection, const std::vector<GPlatesModel::FeatureCollectio ...` | function | `ReconstructHandle::type` | Same as reconstruct overload for ReconstructedFeatureGeometry except generates ReconstructContext::Reconstruction instances instead. |
| `reconstruct( std::vector<ReconstructContext::ReconstructedFeature> &reconstructed_features, const double &reconstruction_time, GPlatesModel::integer_plate_id_type anchor_plate_id, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &reconstructable_features_collection, const std::vector<GPlatesModel::Fea ...` | function | `ReconstructHandle::type` | Same as reconstruct overload for ReconstructedFeatureGeometry except generates ReconstructContext::ReconstructedFeature instances instead. |
| `reconstruct_geometry( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry, const ReconstructMethodRegistry &reconstruct_method_registry, const GPlatesModel::FeatureHandle::weak_ref &reconstruction_properties, const double &reconstruction_time, const ReconstructMethodInterface::Context &reconstruc ...` | function | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | Reconstructs the specified geometry from present day to the specified reconstruction time - unless reverse\_reconstruct is true in which case the geometry is assumed to be the reconstructed geometry (at the reconstruction time) and the ... |
| `reconstruct_geometry( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry, const ReconstructMethodRegistry &reconstruct_method_registry, const GPlatesModel::FeatureHandle::weak_ref &reconstruction_properties, const double &reconstruction_time, const ReconstructionTreeCreator &reconstruction_tree_ ...` | function | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | Same as other overload of reconstruct\_geometry but creates a temporary ReconstructMethodInterface::Context internally using reconstruction\_tree\_creator and reconstruct\_params. |
| `reconstruct_geometry( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry, const GPlatesModel::FeatureHandle::weak_ref &reconstruction_properties, const double &reconstruction_time, GPlatesModel::integer_plate_id_type anchor_plate_id, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ ...` | function | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | Same as other overload of reconstruct\_geometry but creates temporary ReconstructMethodRegistry and cached reconstruction tree creator objects internally. |
| `reconstruct_by_plate_id( const GeometryType &geometry, const GPlatesModel::integer_plate_id_type reconstruction_plate_id, const ReconstructionTree &reconstruction_tree, bool reverse_reconstruct = false)` | function | `GeometryType` | Reconstructs a present day geometry using reconstruction\_tree that rotates from present day to the reconstruction time for which reconstruction\_tree was generated. geometry can be any type supported by GPlatesMaths::FiniteRotation as in: ... |
| `reconstruct_as_half_stage( const GeometryType &geometry, const double &reconstruction_time, const ReconstructionFeatureProperties &reconstruction_params, const ReconstructionTreeCreator &reconstruction_tree_creator, bool reverse_reconstruct = false)` | function | `GeometryType` | Reconstruct a present day geometry to the specified reconstruction time using the specified reconstruction properties. geometry can be any type supported by GPlatesMaths::FiniteRotation as in: operator\*(GPlatesMaths::FiniteRotation, ... |
| `reconstruct_as_half_stage( const GeometryType &geometry, const GPlatesModel::integer_plate_id_type left_plate_id, const GPlatesModel::integer_plate_id_type right_plate_id, const double &reconstruction_time, const ReconstructionTreeCreator &reconstruction_tree_creator, const double &spreading_asymmetry = 0.0, const doub ...` | function | `GeometryType` | Reconstructs a present day geometry using reconstruction\_tree that rotates from present day to the reconstruction time for which reconstruction\_tree was generated, using the half-stage rotation reconstruction method. geometry can be any ... |

## Notes

- `reconstruct_by_plate_id`/`reconstruct_as_half_stage` with `reverse_reconstruct=true` interpret `geometry` as already being at the reconstruction time the given `ReconstructionTree`/`ReconstructionTreeCreator` was built for, and reverse-rotate it back to present day — passing a present-day geometry with `reverse_reconstruct=true` silently produces the wrong result rather than an error.
- `reconstruct_geometry` deliberately ignores any topological-reconstruction (deformation) information present in the passed `ReconstructMethodInterface::Context`, since it reconstructs using only the given feature's own properties (e.g. plate ID), not by tracking positions through resolved topologies.
- The overloads that take an `anchor_plate_id` and raw feature collections build their own internal `ReconstructMethodRegistry` and reconstruction-tree cache per call; `extend_total_reconstruction_poles_to_distant_past`, when true, extends moving-plate sequences into the distant past so reconstructed geometries don't snap back to present-day positions outside a rotation sequence's defined time range — see `create_reconstruction_graph`.

## Used by

| Unit | Component | References |
|---|---|---|
| [api/CoReg](../api/CoReg.md) | api | 4 |
| [app-logic/CoRegistrationLayerProxy](CoRegistrationLayerProxy.md) | app-logic | 3 |
| [app-logic/GeometryCookieCutter](GeometryCookieCutter.md) | app-logic | 3 |
| [app-logic/ReconstructLayerTask](ReconstructLayerTask.md) | app-logic | 3 |
| [app-logic/ReconstructMethodByPlateId](ReconstructMethodByPlateId.md) | app-logic | 3 |
| [app-logic/ReconstructMethodHalfStageRotation](ReconstructMethodHalfStageRotation.md) | app-logic | 3 |
| [app-logic/ReconstructMethodMotionPath](ReconstructMethodMotionPath.md) | app-logic | 3 |
| [app-logic/ReconstructMethodSmallCircle](ReconstructMethodSmallCircle.md) | app-logic | 3 |
| [app-logic/ReconstructMethodVirtualGeomagneticPole](ReconstructMethodVirtualGeomagneticPole.md) | app-logic | 3 |
| [app-logic/ReconstructionLayerTask](ReconstructionLayerTask.md) | app-logic | 3 |
| [app-logic/deprecated/PropertyValuePropogator](deprecated/PropertyValuePropogator.md) | app-logic | 3 |
| [cli/CliReconstructCommand](../cli/CliReconstructCommand.md) | cli | 3 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 3 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 3 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 3 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 3 |
| [view-operations/FocusedFeatureGeometryManipulator](../view-operations/FocusedFeatureGeometryManipulator.md) | view-operations | 3 |
| [view-operations/SplitFeatureUndoCommand](../view-operations/SplitFeatureUndoCommand.md) | view-operations | 3 |
| [api/PyFunctions](../api/PyFunctions.md) | api | 2 |
| [app-logic/AssignPlateIds](AssignPlateIds.md) | app-logic | 2 |

*... and 16 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructUtils.h
```

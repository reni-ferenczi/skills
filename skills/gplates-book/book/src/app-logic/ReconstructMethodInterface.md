# ReconstructMethodInterface

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 44 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructMethodInterface.h` | C++ | 338 |
| `src/app-logic/ReconstructMethodInterface.cc` | C++ | 142 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructMethodInterface tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructMethodInterface`](#gplatesapplogicreconstructmethodinterface) | class | [`GPlatesUtils::ReferenceCount<ReconstructMethodInterface>`](../utils/ReferenceCount.md) | — | 6 | Interface for reconstructing feature geometries (derived classes handle different methods of reconstruction). |

## Members

### `GPlatesAppLogic::ReconstructMethodInterface`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructMethodInterface>` | public | Convenience typedefs for a shared pointer to a ReconstructMethodInterface. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructMethodInterface>` | public | — |
| `geometry_type` | typedef | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | Typedef for a geometry type. |
| `Geometry` | struct | `None` | public | Associates a present day or resolved geometry with its geometry property iterator. |
| `TopologyReconstructedGeometryTimeSpan` | struct | `None` | public | Associate a topology reconstructed geometry's time span with its feature's geometry property. |
| `topology_reconstructed_geometry_time_span_sequence_type` | typedef | `std::vector<TopologyReconstructedGeometryTimeSpan>` | public | Typedef for a sequence of topology reconstructed geometries. |
| `Context` | struct | `None` | public | Extrinsic reconstruction state that features are reconstructed with - this is information that is "passed into" a reconstruct method during reconstruction (and initialisation). |
| `~ReconstructMethodInterface()` | destructor | `None` | public | — |
| `get_reconstruction_method_type()` | method | `ReconstructMethod::Type` | public | Returns the type of 'this' reconstruct method. |
| `get_present_day_feature_geometries( std::vector<Geometry> &present_day_geometries)` | method | `void` | public | The same as get\_resolved\_feature\_geometries with a reconstruction time of zero except there \*must\* be one geometry for \*each\* geometry property in the feature (associated with this reconstruct method) that is reconstructable when ... |
| `get_resolved_feature_geometries( std::vector<Geometry> &resolved_geometries, const double &reconstruction_time)` | method | `void` | public | Returns the resolved geometries for the geometry properties of the feature associated with this reconstruct method, to the specified reconstruction time. |
| `reconstruct_feature_geometries( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const ReconstructHandle::type &reconstruct_handle, const Context &context, const double &reconstruction_time)` | method | `void` | public | Reconstructs the feature associated with this reconstruct method to the specified reconstruction time and returns one or more reconstructed feature geometries. |
| `reconstruct_feature_velocities( std::vector<MultiPointVectorField::non_null_ptr_type> &reconstructed_feature_velocities, const ReconstructHandle::type &reconstruct_handle, const Context &context, const double &reconstruction_time, const double &velocity_delta_time, VelocityDeltaTime::Type velocity_delta_time_type)` | method | `void` | public | Calculates velocities at the positions of the reconstructed feature geometries, of the feature associated with this reconstruct method, at the specified reconstruction time and returns one or more reconstructed feature \*velocities\*. |
| `reconstruct_geometry( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry, const Context &context, const double &reconstruction_time, bool reverse_reconstruct)` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | Reconstructs the specified geometry from present day to the specified reconstruction time - unless reverse\_reconstruct is true in which case the geometry is assumed to be the reconstructed geometry (at the reconstruction time) and the ... |
| `get_topology_reconstructed_geometry_time_spans( topology_reconstructed_geometry_time_span_sequence_type &topology_reconstructed_geometry_time_spans, const Context &context)` | method | `void` | public | Returns any topology-reconstructed geometry time spans. |
| `ReconstructMethodInterface( ReconstructMethod::Type reconstruction_method_type, const GPlatesModel::FeatureHandle::weak_ref &feature_weak_ref)` | constructor | `None` | protected | Constructor associates a feature with this (derived) reconstruct method instance. |
| `reconstruct_feature_velocities_by_plate_id( std::vector<MultiPointVectorField::non_null_ptr_type> &reconstructed_feature_velocities, const ReconstructHandle::type &reconstruct_handle, const Context &context, const double &reconstruction_time, const double &velocity_delta_time, VelocityDeltaTime::Type velocity_delta_tim ...` | method | `void` | protected | The default method of calculating velocities that is suitable for some derived classes. |
| `d_reconstruction_method_type` | field | `ReconstructMethod::Type` | private | — |
| `d_feature_weak_ref` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTMETHODINTERFACE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructMethodInterface tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructMethodByPlateId](ReconstructMethodByPlateId.md) | app-logic | 75 |
| [app-logic/ReconstructContext](ReconstructContext.md) | app-logic | 47 |
| [app-logic/ReconstructMethodHalfStageRotation](ReconstructMethodHalfStageRotation.md) | app-logic | 36 |
| [app-logic/ReconstructMethodFlowline](ReconstructMethodFlowline.md) | app-logic | 33 |
| [app-logic/ReconstructMethodRegistry](ReconstructMethodRegistry.md) | app-logic | 32 |
| [app-logic/ReconstructMethodSmallCircle](ReconstructMethodSmallCircle.md) | app-logic | 23 |
| [app-logic/ReconstructMethodMotionPath](ReconstructMethodMotionPath.md) | app-logic | 21 |
| [app-logic/ReconstructMethodVirtualGeomagneticPole](ReconstructMethodVirtualGeomagneticPole.md) | app-logic | 21 |
| [app-logic/AssignPlateIds](AssignPlateIds.md) | app-logic | 19 |
| [app-logic/PartitionFeatureUtils](PartitionFeatureUtils.md) | app-logic | 16 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 16 |
| [app-logic/ReconstructUtils](ReconstructUtils.md) | app-logic | 13 |
| [app-logic/MotionPathGeometryPopulator](MotionPathGeometryPopulator.md) | app-logic | 12 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 11 |
| [api/PyFunctions](../api/PyFunctions.md) | api | 9 |
| [app-logic/GenericPartitionFeatureTask](GenericPartitionFeatureTask.md) | app-logic | 8 |
| [app-logic/VgpPartitionFeatureTask](VgpPartitionFeatureTask.md) | app-logic | 4 |
| [qt-widgets/AssignReconstructionPlateIdsDialog](../qt-widgets/AssignReconstructionPlateIdsDialog.md) | qt-widgets | 4 |
| [app-logic/PartitionFeatureTask](PartitionFeatureTask.md) | app-logic | 3 |
| [cli/CliAssignPlateIdsCommand](../cli/CliAssignPlateIdsCommand.md) | cli | 2 |

*... and 2 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructMethodInterface.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructMethodInterface --body
python scripts/gpq.py uses ReconstructMethodInterface --kind class
python scripts/gpq.py hier ReconstructMethodInterface
```

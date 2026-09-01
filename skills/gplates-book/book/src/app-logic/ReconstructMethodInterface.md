# ReconstructMethodInterface

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 44 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructMethodInterface.h` | C++ | 338 |
| `src/app-logic/ReconstructMethodInterface.cc` | C++ | 142 |

## Overview

This is the polymorphic core of reconstruction: one instance per feature,
knowing how *that* feature's geometry moves through time. The six
implementations cover reconstruction by plate ID, by half-stage rotation
(left/right plate pair), flowlines, motion paths, small circles and virtual
geomagnetic poles. `ReconstructMethodRegistry` decides which one a given feature
gets and constructs it; `ReconstructContext` then holds the instances and drives
them. Above that sit `ReconstructLayerProxy` and the layer system.

The design splits reconstruction state in two, and the split is what makes the
caching upstream work. *Intrinsic* state — plate IDs, geometry properties,
begin/end times — belongs to the feature and is captured once, at construction,
in the derived instance. *Extrinsic* state travels in a `Context`: the
`ReconstructParams`, a `ReconstructionTreeCreator` and, when features are being
deformed rather than rigidly rotated, a `TopologyReconstruct`. Because `Context`
is passed to each call rather than stored, one instance can serve many
reconstruction times; because it is fixed at construction time for
initialisation purposes, the header states plainly that a *changed* context
requires a new reconstruct method instance. That is exactly the rule
`ReconstructLayerProxy` implements when it keys its reconstruct context states
on `ReconstructParams`.

Note that the interface deliberately hands out a `ReconstructionTreeCreator`
rather than a single `ReconstructionTree` for the requested time: flowlines and
motion paths integrate over many times, so they need trees at times other than
the one being asked for, and routing through the creator lets those lookups hit
the tree cache. The `reverse_reconstruct` flag on `reconstruct_geometry` serves
the editing path — a geometry edited at some past time must be rotated back to
present day before it can be stored on the feature, since features hold
present-day geometry.

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

**Contract when implementing a new method.** All output parameters are appended
to, never assigned. `get_present_day_feature_geometries` must return one
`Geometry` for *every* reconstructable geometry property of the feature,
including properties that are not active at present day — order is free, but
completeness is required, because callers index into that sequence. Any
`ReconstructedFeatureGeometry` or `MultiPointVectorField` you create must be
stamped with the `reconstruct_handle` your caller passed in; that handle is how
the results are later found again among a feature's weak observers.

**Two of the virtuals are optional.**
`reconstruct_feature_velocities` defaults to
`reconstruct_feature_velocities_by_plate_id`, which is correct for the methods
whose motion really is a single plate rotation. Override it where it is not.
`get_topology_reconstructed_geometry_time_spans` defaults to doing nothing and
is currently overridden only by `ReconstructMethodByPlateId` — that is, only
plate-ID reconstruction participates in topological deformation.

**`get_resolved_feature_geometries` is not part of the interface.** It is
`#if 0`-ed out in the header even though the Doxygen for
`get_present_day_feature_geometries` still refers to it. The comment describing
the difference (a resolved geometry that is inactive at the requested time is
simply absent, whereas the present-day call returns everything) is the
specification of the surviving method, not of a second one you can call.

**`d_feature_weak_ref` is weak.** The instance does not keep its feature alive.
An instance outliving its feature is a real possibility when caches hold on to
context state, so treat the feature reference as needing an `is_valid()` check;
the default velocity implementation dereferences it directly.

**The default velocity path has two documented rough edges.** When the feature
has no reconstruction plate ID it silently falls back to plate 0, which still
yields a non-identity rotation whenever the anchored plate is non-zero. And it
converts every present-day geometry to a `MultiPointOnSphere` domain, so the
resulting `MultiPointVectorField` can carry a property iterator pointing at a
non-multipoint property — the source calls this "slightly dodgy". It also
fabricates a throwaway `ReconstructedFeatureGeometry` purely so the velocity
arrows have a reconstruction geometry to colour by.

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

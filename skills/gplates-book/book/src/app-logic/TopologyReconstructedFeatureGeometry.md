# TopologyReconstructedFeatureGeometry

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 706 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TopologyReconstructedFeatureGeometry.h` | C++ | 251 |
| `src/app-logic/TopologyReconstructedFeatureGeometry.cc` | C++ | 91 |

## Overview

`TopologyReconstructedFeatureGeometry` is the `ReconstructedFeatureGeometry` subclass used when a feature's geometry was carried through the topology reconstruction pipeline rather than reconstructed by a single rigid rotation. Unlike a plain reconstructed geometry, its points can be subducted going forward in time or consumed by a mid-ocean ridge going backward in time, and each point can accumulate deformation from passing through resolved deforming networks.

All of the actual work is delegated to the `TopologyReconstruct::GeometryTimeSpan` held in `d_topology_reconstruct_geometry_time_span`: `reconstructed_geometry()` and `get_geometry_data()` simply ask the time span for the geometry, per-point topology locations, strain rates and total strains at the current reconstruction time. This class itself is a thin, visitable wrapper that plugs that per-point history into the `ReconstructionGeometryVisitor` / weak-observer machinery shared by all reconstruction geometries.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::TopologyReconstructedFeatureGeometry`](#gplatesapplogictopologyreconstructedfeaturegeometry) | class | [`ReconstructedFeatureGeometry`](ReconstructedFeatureGeometry.md) | — | 0 | A feature geometry that has been reconstructed using topologies (rigid plates and deforming networks). |

## Members

### `GPlatesAppLogic::TopologyReconstructedFeatureGeometry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<TopologyReconstructedFeatureGeometry>` | public | A convenience typedef for a non-null shared pointer to a non-const TopologyReconstructedFeatureGeometry. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const TopologyReconstructedFeatureGeometry>` | public | A convenience typedef for a non-null shared pointer to a const TopologyReconstructedFeatureGeometry. |
| `point_location_seq_type` | typedef | `std::vector<TopologyPointLocation>` | public | Typedef for a sequence of per-geometry-point locations in resolved topologies. |
| `point_deformation_strain_rate_seq_type` | typedef | `std::vector<DeformationStrainRate>` | public | Typedef for a sequence of per-geometry-point deformation instantaneous strain rates. |
| `point_deformation_total_strain_seq_type` | typedef | `std::vector<DeformationStrain>` | public | Typedef for a sequence of per-geometry-point deformation accumulated/total strains. |
| `create( const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree, const ReconstructionTreeCreator &reconstruction_tree_creator, GPlatesModel::FeatureHandle &feature_handle, GPlatesModel::FeatureHandle::iterator property_iterator, const TopologyReconstruct::GeometryTimeSpan::non_null_ptr_type &topology_ ...` | method | `non_null_ptr_type` | public | Create a TopologyReconstructedFeatureGeometry instance. |
| `reconstructed_geometry()` | method | `geometry_ptr_type` | public | Returns the reconstructed geometry. |
| `get_reconstructed_points( point_seq_type &reconstructed_points)` | method | `void` | public | Returns the reconstructed geometry points in reconstructed\_geometry. |
| `get_reconstructed_point_locations( point_location_seq_type &reconstructed_point_locations)` | method | `void` | public | Returns the per-geometry-point locations in resolved topologies. |
| `get_point_deformation_strain_rates( point_deformation_strain_rate_seq_type &strain_rates)` | method | `void` | public | Returns the per-geometry-point deformation strain rates. |
| `get_point_deformation_total_strains( point_deformation_total_strain_seq_type &total_strains)` | method | `void` | public | Returns the per-geometry-point deformation (total) strains. |
| `get_geometry_data( boost::optional<point_seq_type &> reconstructed_points = boost::none, boost::optional<point_location_seq_type&> reconstructed_point_locations = boost::none, boost::optional<point_deformation_strain_rate_seq_type &> strain_rates = boost::none, boost::optional<point_deformation_total_strain_seq_type &> ...` | method | `void` | public | Combines get\_reconstructed\_points, get\_reconstructed\_point\_locations, get\_point\_deformation\_strain\_rates and get\_point\_deformation\_total\_strains (for more efficient access). |
| `get_time_range()` | method | `TimeSpanUtils::TimeRange` | public | Returns the time range over which this reconstructed feature was reconstructed using topologies. |
| `accept_visitor( ConstReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ConstReconstructionGeometryVisitor instance. |
| `accept_visitor( ReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ReconstructionGeometryVisitor instance. |
| `accept_weak_observer_visitor( GPlatesModel::WeakObserverVisitor<GPlatesModel::FeatureHandle> &visitor)` | method | `void` | public | Accept a WeakObserverVisitor instance. |
| `d_topology_reconstruct_geometry_time_span` | field | `TopologyReconstruct::GeometryTimeSpan::non_null_ptr_type` | private | The source of our geometry and deformation strain rates and total strains. |
| `TopologyReconstructedFeatureGeometry( const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree_, const ReconstructionTreeCreator &reconstruction_tree_creator, GPlatesModel::FeatureHandle &feature_handle, GPlatesModel::FeatureHandle::iterator property_iterator, const TopologyReconstruct::GeometryTimeSpa ...` | constructor | `None` | private | Instantiate a topology reconstructed feature geometry. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_TOPOLOGYRECONSTRUCTEDFEATUREGEOMETRY_H` | macro | `None` | — |

## Notes

Every accessor asserts (via `GPlatesGlobal::Assert<PreconditionViolationError>`) that the geometry time span is valid at the object's current reconstruction time. An instance must therefore only ever be created for a reconstruction time within the time range covered by its `TopologyReconstruct::GeometryTimeSpan` — the constructor is private and creation goes only through `create()`, but callers building the time span still need to keep the two in sync. The constructor is private specifically to prevent stack allocation; instances are always managed through `non_null_ptr_type`.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GMTFormatDeformationExport](../file-io/GMTFormatDeformationExport.md) | file-io | 9 |
| [file-io/GpmlFormatDeformationExport](../file-io/GpmlFormatDeformationExport.md) | file-io | 9 |
| [file-io/GMTFormatReconstructedScalarCoverageExport](../file-io/GMTFormatReconstructedScalarCoverageExport.md) | file-io | 7 |
| [file-io/GpmlFormatReconstructedScalarCoverageExport](../file-io/GpmlFormatReconstructedScalarCoverageExport.md) | file-io | 7 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 6 |
| [app-logic/ReconstructMethodByPlateId](ReconstructMethodByPlateId.md) | app-logic | 1 |
| [app-logic/ReconstructScalarCoverageLayerProxy](ReconstructScalarCoverageLayerProxy.md) | app-logic | 1 |
| [app-logic/ReconstructedScalarCoverage](ReconstructedScalarCoverage.md) | app-logic | 1 |
| [app-logic/ReconstructionGeometryVisitor](ReconstructionGeometryVisitor.md) | app-logic | 1 |
| [app-logic/ScalarCoverageTimeSpan](ScalarCoverageTimeSpan.md) | app-logic | 1 |
| [app-logic/TopologyInternalUtils](TopologyInternalUtils.md) | app-logic | 1 |
| [file-io/DeformationExport](../file-io/DeformationExport.md) | file-io | 1 |
| [gui/ExportDeformationAnimationStrategy](../gui/ExportDeformationAnimationStrategy.md) | gui | 1 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 1 |
| [model/WeakObserverVisitor](../model/WeakObserverVisitor.md) | model | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/TopologyReconstructedFeatureGeometry.h
python scripts/gpq.py def GPlatesAppLogic::TopologyReconstructedFeatureGeometry --body
python scripts/gpq.py uses TopologyReconstructedFeatureGeometry --kind class
python scripts/gpq.py hier TopologyReconstructedFeatureGeometry
```

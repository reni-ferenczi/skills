# ReconstructParams

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 269 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructParams.h` | C++ | 314 |
| `src/app-logic/ReconstructParams.cc` | C++ | 310 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructParams tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructParams`](#gplatesapplogicreconstructparams) | class | `boost::less_than_comparable<ReconstructParams>`<br>`boost::equality_comparable<ReconstructParams>` | — | 0 | ReconstructParams is used to store additional parameters for reconstructing features into ReconstructedFeatureGeometry objects. |

## Members

### `GPlatesAppLogic::ReconstructParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ReconstructParams()` | constructor | `None` | public | — |
| `set_reconstruct_by_plate_id_outside_active_time_period( bool reconstruct_outside_active_time_period)` | method | `void` | public | Sets whether we reconstruct by-plate-id outside the feature's active time period. |
| `get_reconstruct_by_plate_id_outside_active_time_period()` | method | `bool` | public | — |
| `get_reconstruct_using_topologies()` | method | `bool` | public | — |
| `set_reconstruct_using_topologies( bool reconstruct_using_topologies)` | method | `void` | public | — |
| `get_topology_reconstruction_end_time()` | method | `double` | public | Methods for topology-reconstructed parameters. |
| `set_topology_reconstruction_end_time( double deformation_end_time)` | method | `void` | public | — |
| `get_topology_reconstruction_begin_time()` | method | `double` | public | — |
| `set_topology_reconstruction_begin_time( double deformation_begin_time)` | method | `void` | public | — |
| `get_topology_reconstruction_time_increment()` | method | `double` | public | — |
| `set_topology_reconstruction_time_increment( double time_inc)` | method | `void` | public | — |
| `get_topology_deformation_use_natural_neighbour_interpolation()` | method | `bool` | public | — |
| `set_topology_deformation_use_natural_neighbour_interpolation( bool use_natural_neighbour_interpolation)` | method | `void` | public | — |
| `get_topology_reconstruction_use_time_of_appearance()` | method | `bool` | public | Use a feature's time of appearance instead of its 'gpml:geometryImportTime' as the starting time for topology reconstruction. |
| `set_topology_reconstruction_use_time_of_appearance( bool use_time_of_appearance)` | method | `void` | public | — |
| `get_topology_reconstruction_enable_line_tessellation()` | method | `bool` | public | — |
| `set_topology_reconstruction_enable_line_tessellation( bool enable_line_tessellation)` | method | `void` | public | — |
| `set_topology_reconstruction_line_tessellation_degrees( const double &line_tessellation_degrees)` | method | `void` | public | — |
| `get_topology_reconstruction_enable_lifetime_detection()` | method | `bool` | public | — |
| `set_topology_reconstruction_enable_lifetime_detection( bool enable_lifetime_detection)` | method | `void` | public | — |
| `set_topology_reconstruction_lifetime_detection_threshold_velocity_delta( const double &lifetime_detection_threshold_velocity_delta)` | method | `void` | public | — |
| `set_topology_reconstruction_lifetime_detection_threshold_distance_to_boundary( const double &lifetime_detection_threshold_distance_to_boundary)` | method | `void` | public | — |
| `get_topology_reconstruction_deactivate_points_that_fall_outside_a_network()` | method | `bool` | public | — |
| `set_topology_reconstruction_deactivate_points_that_fall_outside_a_network( bool deactivate_points_that_fall_outside_a_network)` | method | `void` | public | — |
| `operator==( const ReconstructParams &rhs)` | operator | `bool` | public | Equality comparison operator. |
| `operator<( const ReconstructParams &rhs)` | operator | `bool` | public | Less than comparison operator. |
| `INITIAL_TIME_RANGE_END` | field | `double` | private | — |
| `INITIAL_TIME_RANGE_BEGIN` | field | `double` | private | — |
| `INITIAL_TIME_RANGE_INCREMENT` | field | `double` | private | — |
| `INITIAL_LINE_TESSELLATION_DEGREES` | field | `double` | private | — |
| `d_reconstruct_by_plate_id_outside_active_time_period` | field | `bool` | private | Do we reconstruct by-plate-id outside the feature's active time period. |
| `d_reconstruct_using_topologies` | field | `bool` | private | Whether to reconstruct using topologies. |
| `d_topology_reconstruction_end_time` | field | `GPlatesMaths::real_t` | private | Topology reconstruction parameters. |
| `d_topology_reconstruction_begin_time` | field | `GPlatesMaths::real_t` | private | — |
| `d_topology_reconstruction_time_increment` | field | `GPlatesMaths::real_t` | private | — |
| `d_topology_deformation_use_natural_neighbour_interpolation` | field | `bool` | private | — |
| `d_topology_reconstruction_use_time_of_appearance` | field | `bool` | private | — |
| `d_topology_reconstruction_enable_line_tessellation` | field | `bool` | private | — |
| `d_topology_reconstruction_line_tessellation_degrees` | field | `GPlatesMaths::real_t` | private | — |
| `d_topology_reconstruction_enable_lifetime_detection` | field | `bool` | private | — |
| `d_topology_reconstruction_lifetime_detection_threshold_velocity_delta` | field | `GPlatesMaths::real_t` | private | — |
| `d_topology_reconstruction_lifetime_detection_threshold_distance_to_boundary` | field | `GPlatesMaths::real_t` | private | — |
| `d_topology_reconstruction_deactivate_points_that_fall_outside_a_network` | field | `bool` | private | — |
| `transcribe( GPlatesScribe::Scribe &scribe, bool transcribed_construct_data)` | method | `GPlatesScribe::TranscribeResult` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `INITIAL_TIME_RANGE_END` | variable | `double` | Topology reconstruction parameters. |
| `INITIAL_TIME_RANGE_BEGIN` | variable | `double` | — |
| `INITIAL_TIME_RANGE_INCREMENT` | variable | `double` | — |
| `INITIAL_LINE_TESSELLATION_DEGREES` | variable | `double` | — |
| `operator==( const ReconstructParams &rhs)` | operator | `bool` | — |
| `operator<( const ReconstructParams &rhs)` | operator | `bool` | — |
| `GPLATES_APP_LOGIC_RECONSTRUCTPARAMS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructParams tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructUtils](ReconstructUtils.md) | app-logic | 25 |
| [qt-widgets/SetTopologyReconstructionParametersDialog](../qt-widgets/SetTopologyReconstructionParametersDialog.md) | qt-widgets | 24 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 11 |
| [cli/CliStageRotationCommand](../cli/CliStageRotationCommand.md) | cli | 8 |
| [app-logic/ReconstructMethodByPlateId](ReconstructMethodByPlateId.md) | app-logic | 7 |
| [qt-widgets/ReconstructLayerOptionsWidget](../qt-widgets/ReconstructLayerOptionsWidget.md) | qt-widgets | 7 |
| [cli/CliRelativeTotalRotation](../cli/CliRelativeTotalRotation.md) | cli | 6 |
| [app-logic/ReconstructLayerParams](ReconstructLayerParams.md) | app-logic | 5 |
| [cli/CliEquivalentTotalRotation](../cli/CliEquivalentTotalRotation.md) | cli | 5 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 5 |
| [app-logic/ReconstructMethodInterface](ReconstructMethodInterface.md) | app-logic | 4 |
| [app-logic/ReconstructContext](ReconstructContext.md) | app-logic | 2 |
| [app-logic/ReconstructMethodVirtualGeomagneticPole](ReconstructMethodVirtualGeomagneticPole.md) | app-logic | 2 |
| [api/PyFunctions](../api/PyFunctions.md) | api | 1 |
| [app-logic/AssignPlateIds](AssignPlateIds.md) | app-logic | 1 |
| [app-logic/CoRegistrationLayerProxy](CoRegistrationLayerProxy.md) | app-logic | 1 |
| [cli/CliReconstructCommand](../cli/CliReconstructCommand.md) | cli | 1 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 1 |
| [qt-widgets/SetVGPVisibilityDialog](../qt-widgets/SetVGPVisibilityDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructParams.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructParams --body
python scripts/gpq.py uses ReconstructParams --kind class
python scripts/gpq.py hier ReconstructParams
```

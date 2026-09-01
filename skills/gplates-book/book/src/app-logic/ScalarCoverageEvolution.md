# ScalarCoverageEvolution

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 143 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ScalarCoverageEvolution.h` | C++ | 417 |
| `src/app-logic/ScalarCoverageEvolution.cc` | C++ | 1713 |

## Overview

[[[PROSE overview unit=app-logic/ScalarCoverageEvolution tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ScalarCoverageEvolution`](#gplatesapplogicscalarcoverageevolution) | class | [`GPlatesUtils::ReferenceCount<ScalarCoverageEvolution>`](../utils/ReferenceCount.md) | — | 0 | Evolve the scalar values (in a scalar coverage) as a result of deformation. |

## Members

### `GPlatesAppLogic::ScalarCoverageEvolution`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ScalarCoverageEvolution>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ScalarCoverageEvolution>` | public | — |
| `EvolvedScalarType` | enum | `None` | public | Type of evolved scalar (note: not all scalar types are evolved scalar types affected by deformation). |
| `scalar_type_type` | typedef | `GPlatesPropertyValues::ValueObjectType` | public | Typedef for scalar type. |
| `InitialEvolvedScalarCoverage` | class | `None` | public | Initial scalar values (to be evolved). |
| `DEFAULT_INITIAL_CRUSTAL_THICKNESS_KMS` | field | `double` | public | The default initial crustal thickness (in km) to use when no initial scalar values are provided for it. |
| `get_scalar_type( EvolvedScalarType evolved_scalar_type)` | method | `scalar_type_type` | public | Returns the scalar type associated with the specified evolved scalar type enumeration. |
| `is_evolved_scalar_type( const scalar_type_type &scalar_type)` | method | `boost::optional<EvolvedScalarType>` | public | Returns the evolved scalar type enumeration associated with the specified scalar type, otherwise returns none. |
| `create( const InitialEvolvedScalarCoverage &initial_scalar_coverage, const double &initial_time, TopologyReconstruct::GeometryTimeSpan::non_null_ptr_type geometry_time_span)` | method | `non_null_ptr_type` | public | Evolve scalar values over time (starting with the initial scalar values) and store them in the returned scalar coverage time span. |
| `get_scalar_values( EvolvedScalarType evolved_scalar_type, const double &reconstruction_time, std::vector<double> &scalar_values, std::vector<bool> &scalar_values_are_active)` | method | `void` | public | Returns the scalar values at \*all\* points at the specified time (including inactive points). |
| `get_num_scalar_values()` | method | `unsigned int` | public | Returns number of scalar values (per scalar type). |
| `EvolvedScalarCoverage` | class | `None` | private | A snapshot in time of the evolved scalar values (associated with points in a geometry). |
| `time_span_type` | typedef | `TimeSpanUtils::TimeWindowSpan<EvolvedScalarCoverage::non_null_ptr_type>` | private | Typedef for a time span of evolved scalar coverages. |
| `d_geometry_time_span` | field | `TopologyReconstruct::GeometryTimeSpan::non_null_ptr_type` | private | — |
| `d_initial_scalar_coverage` | field | `InitialEvolvedScalarCoverage` | private | — |
| `d_initial_time` | field | `double` | private | — |
| `d_num_scalar_values` | field | `unsigned int` | private | — |
| `d_scalar_coverage_time_span` | field | `time_span_type::non_null_ptr_type` | private | — |
| `d_have_initialised_tectonic_subsidence` | field | `bool` | private | Tectonic subsidence is initialised only when/if it is first requested since it's relatively expensive. |
| `ScalarCoverageEvolution( const InitialEvolvedScalarCoverage &initial_scalar_coverage, const double &initial_time, TopologyReconstruct::GeometryTimeSpan::non_null_ptr_type geometry_time_span)` | constructor | `None` | private | — |
| `initialise()` | method | `void` | private | — |
| `evolve_time_steps( unsigned int start_time_slot, unsigned int end_time_slot)` | method | `void` | private | — |
| `evolve_time_step( EvolvedScalarCoverage::State &current_scalar_coverage_state, const std::vector< boost::optional<DeformationStrainRate> > &current_deformation_strain_rates, const std::vector< boost::optional<DeformationStrainRate> > &next_deformation_strain_rates, const double &current_time, const double &next_time)` | method | `void` | private | Evolves the current scalar values from the current time to the next time. |
| `initialise_tectonic_subsidence()` | method | `void` | private | Initialise tectonic subsidence from crustal stretching and lithospheric thermal cooling. |
| `evolve_lithospheric_temperature( std::vector<bool> &have_started_evolving_lithospheric_temperature, double *const lithospheric_temperature_integrated_over_depth_kms, double *current_temperature_depth, double *next_temperature_depth, unsigned int scalar_values_start_index, unsigned int scalar_values_end_index)` | method | `void` | private | — |
| `evolve_lithospheric_temperature_time_step( const double &time_increment, const std::vector< boost::optional<DeformationStrainRate> > &current_deformation_strain_rates, const std::vector< boost::optional<DeformationStrainRate> > &next_deformation_strain_rates, const EvolvedScalarCoverage::State &current_scalar_coverage_ ...` | method | `void` | private | — |
| `evolve_tectonic_subsidence( const double *const lithospheric_temperature_integrated_over_depth_kms, unsigned int scalar_values_start_index, unsigned int scalar_values_end_index)` | method | `void` | private | — |
| `evolve_tectonic_subsidence_time_steps( const double *const lithospheric_temperature_integrated_over_depth_kms, unsigned int start_time_slot, unsigned int end_time_slot, unsigned int scalar_values_start_index, unsigned int scalar_values_end_index)` | method | `void` | private | — |
| `evolve_tectonic_subsidence_time_step( const EvolvedScalarCoverage::State &current_scalar_coverage_state, EvolvedScalarCoverage::State &next_scalar_coverage_state, const double *const current_lithospheric_temperature_integrated_over_depth_kms, const double *const next_lithospheric_temperature_integrated_over_depth_kms, ...` | method | `void` | private | Each lithospheric-temperature-integrated-over-depth array contains 'scalar\_values\_end\_index - scalar\_values\_start\_index' values... |
| `create_time_span_rigid_sample( const double &reconstruction_time, const double &closest_younger_sample_time, const EvolvedScalarCoverage::non_null_ptr_type &closest_younger_sample)` | method | `EvolvedScalarCoverage::non_null_ptr_type` | private | The sample \*creator\* function for TimeSpanUtils::TimeWindowSpan\<EvolvedScalarCoverage\>. |
| `interpolate_time_span_samples( const double &interpolate_position, const double &first_geometry_time, const double &second_geometry_time, const EvolvedScalarCoverage::non_null_ptr_type &first_sample, const EvolvedScalarCoverage::non_null_ptr_type &second_sample)` | method | `EvolvedScalarCoverage::non_null_ptr_type` | private | The sample \*interpolator\* function for TimeSpanUtils::TimeWindowSpan\<EvolvedScalarCoverage\>. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `THERMAL_ALPHA` | variable | `double` | Thermal expansion coefficient \[1/C\]. |
| `THERMAL_CONDUCTIVITY` | variable | `double` | Thermal conductivity \[W/C/m\]. |
| `TEMPERATURE_ASTHENOSPHERE` | variable | `double` | Asthenosphere temperature \[C\]. |
| `DENSITY_WATER` | variable | `double` | Sea water density \[kg/m^3\]. |
| `DENSITY_MANTLE` | variable | `double` | Mantle density at 0 degrees \[kg/m^3\]. |
| `DENSITY_CRUST` | variable | `double` | Crust density \[kg/m^3\]. |
| `DENSITY_ASTHENOSPHERE` | variable | `double` | Asthenosphere density \[kg/m^3\]. |
| `SPECIFIC_HEAT` | variable | `double` | Specific heat per unit mass \[W.s/kg/C\]. |
| `THERMAL_DIFFUSIVITY` | variable | `double` | Thermal diffusivity \[m^2/s\]. |
| `LITHOSPHERIC_THICKNESS_KMS` | variable | `double` | Thickness of lithosphere (in km). |
| `LITHOSPHERIC_THICKNESS` | variable | `double` | ...and in metres. |
| `NUM_TEMPERATURE_DIFFUSION_DEPTH_INTERVALS` | variable | `unsigned int` | Depth resolution to use when solving the 1D temperature advection-diffusion equation for each surface point. |
| `NUM_TEMPERATURE_DIFFUSION_DEPTH_SAMPLES` | variable | `unsigned int` | — |
| `INVERSE_NUM_TEMPERATURE_DIFFUSION_DEPTH_INTERVALS` | variable | `double` | — |
| `TEMPERATURE_DIFFISION_DEPTH_RESOLUTION_KMS` | variable | `double` | The depth spacing between temperature diffusion depth samples (in km). |
| `TEMPERATURE_DIFFISION_DEPTH_RESOLUTION` | variable | `double` | ...and in metres. |
| `NUM_POINTS_IN_TEMPERATURE_DIFFUSION_GROUP` | variable | `unsigned int` | Limit the number of surface points to solve temperature diffusion at the same time (in a group) in order to minimise memory usage for storing temperature depth profile and also, to a lesser extent, to minimise CPU cache misses (when ... |
| `GPLATES_APP_LOGIC_SCALARCOVERAGEEVOLUTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ScalarCoverageEvolution tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ScalarCoverageTimeSpan](ScalarCoverageTimeSpan.md) | app-logic | 37 |
| [app-logic/ReconstructScalarCoverageLayerProxy](ReconstructScalarCoverageLayerProxy.md) | app-logic | 10 |
| [app-logic/ReconstructScalarCoverageLayerParams](ReconstructScalarCoverageLayerParams.md) | app-logic | 4 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 3 |
| [file-io/GMTFormatReconstructedScalarCoverageExport](../file-io/GMTFormatReconstructedScalarCoverageExport.md) | file-io | 1 |
| [file-io/GpmlFormatReconstructedScalarCoverageExport](../file-io/GpmlFormatReconstructedScalarCoverageExport.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ScalarCoverageEvolution.h
python scripts/gpq.py def GPlatesAppLogic::ScalarCoverageEvolution --body
python scripts/gpq.py uses ScalarCoverageEvolution --kind class
python scripts/gpq.py hier ScalarCoverageEvolution
```

# ScalarCoverageTimeSpan

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 314 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ScalarCoverageTimeSpan.h` | C++ | 346 |
| `src/app-logic/ScalarCoverageTimeSpan.cc` | C++ | 406 |

## Overview

[[[PROSE overview unit=app-logic/ScalarCoverageTimeSpan tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ScalarCoverageTimeSpan`](#gplatesapplogicscalarcoveragetimespan) | class | [`GPlatesUtils::ReferenceCount<ScalarCoverageTimeSpan>`](../utils/ReferenceCount.md) | — | 0 | Builds and keeps track of scalar values (associated with points in a geometry) over a time span. |

## Members

### `GPlatesAppLogic::ScalarCoverageTimeSpan`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ScalarCoverageTimeSpan>` | public | A convenience typedef for a shared pointer to a non-const ScalarCoverageTimeSpan. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ScalarCoverageTimeSpan>` | public | A convenience typedef for a shared pointer to a const ScalarCoverageTimeSpan. |
| `scalar_type_type` | typedef | `GPlatesPropertyValues::ValueObjectType` | public | Typedef for scalar type. |
| `initial_scalar_coverage_type` | typedef | `std::map<scalar_type_type, std::vector<double>>` | public | Typedef for the initial scalar values associated with scalar types. |
| `ScalarCoverage` | class | `None` | public | Scalar values (associated with points in a geometry) for all scalar types in the range associated with the domain geometry. |
| `create( const initial_scalar_coverage_type &initial_scalar_coverage)` | method | `non_null_ptr_type` | public | Creates an \*empty\* scalar coverage time span containing only the specified initial scalar coverage. |
| `create( const initial_scalar_coverage_type &initial_scalar_coverage, TopologyReconstruct::GeometryTimeSpan::non_null_ptr_type geometry_time_span)` | method | `non_null_ptr_type` | public | Creates a scalar coverage time span containing the time progression of a scalar coverage. |
| `is_valid( const double &reconstruction_time)` | method | `bool` | public | Returns true if the scalar values are active at the specified reconstruction time. |
| `get_scalar_coverage( const double &reconstruction_time)` | method | `boost::optional<ScalarCoverage>` | public | Returns the scalar coverage at the specified time. |
| `contains_scalar_type( const scalar_type_type &scalar_type)` | method | `bool` | public | Returns true if this scalar coverage (time span) contains the specified scalar type. |
| `get_scalar_types( std::vector<scalar_type_type> &scalar_types)` | method | `void` | public | Returns all contained scalar types. |
| `get_scalar_values( const scalar_type_type &scalar_type, const double &reconstruction_time, std::vector<double> &scalar_values)` | method | `bool` | public | Returns the scalar values at the specified time. |
| `get_all_scalar_values( const scalar_type_type &scalar_type, const double &reconstruction_time, std::vector<double> &scalar_values, std::vector<bool> &scalar_values_are_active)` | method | `bool` | public | Returns the scalar values at \*all\* points at the specified time (including inactive points). |
| `get_are_scalar_values_active( const double &reconstruction_time, std::vector<bool> &scalar_values_are_active)` | method | `bool` | public | Returns whether each scalar value, of \*all\* scalar values (regardless of scalar type) at the specified time, is active or not. |
| `get_num_all_scalar_values()` | method | `unsigned int` | public | Returns the number of scalar values returned by get\_all\_scalar\_values. |
| `get_geometry_time_span()` | method | `boost::optional<TopologyReconstruct::GeometryTimeSpan::non_null_ptr_type>` | public | Returns optional geometry time span if one was used (to obtain deformation info to evolve scalar values, or to deactivate points/scalars, or both). |
| `non_evolved_scalar_coverage_type` | typedef | `std::map<scalar_type_type, std::vector<double>>` | private | Typedef for the non-envolved scalar values associated with scalar types. |
| `d_geometry_time_span` | field | `boost::optional<TopologyReconstruct::GeometryTimeSpan::non_null_ptr_type>` | private | Optional geometry time span if one was used to obtain deformation info to evolve scalar values. |
| `d_evolved_scalar_coverage_time_span` | field | `boost::optional<ScalarCoverageEvolution::non_null_ptr_type>` | private | Optional evolved scalar coverage time span. |
| `d_non_evolved_scalar_coverage` | field | `non_evolved_scalar_coverage_type` | private | All scalar values corresponding to scalar types that do \*not\* evolve over time (due to deformation). |
| `d_scalar_import_time` | field | `double` | private | — |
| `d_num_all_scalar_values` | field | `unsigned int` | private | The number of scalar values (active and inactive) per scalar type. |
| `ScalarCoverageTimeSpan( const initial_scalar_coverage_type &initial_scalar_coverage)` | constructor | `None` | private | — |
| `ScalarCoverageTimeSpan( const initial_scalar_coverage_type &initial_scalar_coverage, TopologyReconstruct::GeometryTimeSpan::non_null_ptr_type geometry_time_span)` | constructor | `None` | private | — |
| `create_import_scalar_values( const std::vector<double> &scalar_values, TopologyReconstruct::GeometryTimeSpan::non_null_ptr_type geometry_time_span)` | method | `std::vector<double>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_SCALARCOVERAGETIMESPAN_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ScalarCoverageTimeSpan tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructedScalarCoverage](ReconstructedScalarCoverage.md) | app-logic | 6 |
| [app-logic/ReconstructScalarCoverageLayerProxy](ReconstructScalarCoverageLayerProxy.md) | app-logic | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ScalarCoverageTimeSpan.h
python scripts/gpq.py def GPlatesAppLogic::ScalarCoverageTimeSpan --body
python scripts/gpq.py uses ScalarCoverageTimeSpan --kind class
python scripts/gpq.py hier ScalarCoverageTimeSpan
```

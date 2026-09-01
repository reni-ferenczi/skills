# CalculateVelocity

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 850 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/CalculateVelocity.h` | C++ | 180 |
| `src/maths/CalculateVelocity.cc` | C++ | 277 |

## Overview

Turns a pair of `FiniteRotation`s at two nearby reconstruction times into a
plate velocity at a point, in centimetres per year. `calculate_stage_rotation`
first derives the stage rotation between the two absolute rotations `fr_t1`
and `fr_t2` (t1 more recent than t2), taking care to pick the shorter of the
two quaternion paths between them since a quaternion and its negation
represent the same rotation; `calculate_velocity_vector` then converts that
stage rotation's angle and axis, divided by `delta_time`, into an angular
velocity and cross-multiplies it with the point's position and the Earth's
radius (`GPlatesUtils::Earth::EQUATORIAL_RADIUS_KMS`) to get a Cartesian
velocity vector. `calculate_velocity_vector_and_omega` additionally exposes
the angular velocity itself.

The remaining free functions convert a velocity `Vector3D` between the
geocentric (x, y, z) frame and a local frame at the point, using
`CartesianConvMatrix3D` to build the change-of-basis matrix: colatitude/longitude
components (`VectorColatitudeLongitude`, `convert_vector_from_xyz_to_colat_lon`
and its inverse) and magnitude/angle or magnitude/azimuth pairs
(`calculate_vector_components_magnitude_angle`,
`calculate_vector_components_magnitude_and_azimuth`). These are the functions
that produce the north/east-referenced velocities used by the velocity file
exporters and the kinematics plots.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::VectorColatitudeLongitude`](#gplatesmathsvectorcolatitudelongitude) | class | — | — | 0 | Vector in colatitude/longitude form. |

## Members

### `GPlatesMaths::VectorColatitudeLongitude`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VectorColatitudeLongitude( const GPlatesMaths::real_t &vector_colatitude, const GPlatesMaths::real_t &vector_longitude)` | constructor | `None` | public | — |
| `d_vector_colatitude` | field | `GPlatesMaths::real_t` | private | — |
| `d_vector_longitude` | field | `GPlatesMaths::real_t` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_MATHS_CV_H_` | macro | `None` | — |
| `calculate_velocity_vector( const PointOnSphere &point, const FiniteRotation &fr_t1, const FiniteRotation &fr_t2, const double &delta_time)` | function | `Vector3D` | Calculate the velocity of a PointOnSphere point undergoing rotation. |
| `calculate_stage_rotation( const FiniteRotation &fr_t1, const FiniteRotation &fr_t2)` | function | `FiniteRotation` | Similar to calculate\_velocity\_vector but returns the stage rotation. |
| `calculate_velocity_vector( const PointOnSphere &point, const FiniteRotation &stage_rotation, const double &delta_time)` | function | `Vector3D` | Similar to calculate\_velocity\_vector but uses a stage rotation instead of two equivalent rotations. |
| `calculate_velocity_vector_and_omega( const PointOnSphere &point, const FiniteRotation &fr_t1, const FiniteRotation &fr_t2, const double &delta_time)` | function | `std::pair<Vector3D,real_t /*omega (angular velocity) */>` | calculate\_velocity\_vector\_and\_omega - as calculate\_velocity\_vector but returns the angular velocity (radians per Ma) in addition to the velocity vector. |
| `convert_vector_from_xyz_to_colat_lon( const PointOnSphere &point, const Vector3D &vector_xyz)` | function | `VectorColatitudeLongitude` | Convert a vector from X Y Z space to North East Down space and return Colatitudinal and Longitudinal components of the vector ( Colat is -North , and Lon is East ) |
| `convert_vector_from_colat_lon_to_xyz( const PointOnSphere &point, const VectorColatitudeLongitude &vector_colat_lon)` | function | `Vector3D` | Convert a vector from North East Down space to a vector from X Y Z space. |
| `calculate_vector_components_magnitude_angle( const PointOnSphere &point, const Vector3D &velocity_vector)` | function | `std::pair< real_t/*magnitude*/, real_t/*angle*/ >` | Convert a vector from X Y Z space to North East Down space and return Magnitude and Angle components of the vector. |
| `calculate_vector_components_magnitude_and_azimuth( const GPlatesMaths::PointOnSphere &point, const Vector3D &vector_xyz)` | function | `std::pair< real_t/*magnitude*/, real_t/*azimuth*/ >` | Convert a vector from X Y Z space to North East Down space and return Magnitude and Azimuth components of the vector. |

## Notes

`calculate_velocity_vector` returns `Vector3D(0, 0, 0)` if the stage rotation
is the identity, rather than dividing by a zero angle. The angular velocity
`omega` returned by `calculate_velocity_vector_and_omega` is always positive:
because a stage rotation's pole/angle pair is only defined up to a
simultaneous negation of both, the sign is not physically meaningful and was
deliberately normalised away — the earlier sign, tied to whether the rotation
was clockwise or counter-clockwise about a particular choice of pole, is
documented in the header as a past source of confusion. Callers must pass
`t1` more recent than `t2` and `delta_time = t2 - t1` for the sign
conventions in the rest of the module to hold.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ResolvedVertexSourceInfo](../app-logic/ResolvedVertexSourceInfo.md) | app-logic | 44 |
| [app-logic/PlateVelocityUtils](../app-logic/PlateVelocityUtils.md) | app-logic | 24 |
| [file-io/GMTFormatMultiPointVectorFieldExport](../file-io/GMTFormatMultiPointVectorFieldExport.md) | file-io | 23 |
| [app-logic/NetRotationUtils](../app-logic/NetRotationUtils.md) | app-logic | 21 |
| [file-io/CitcomsFormatVelocityVectorFieldExport](../file-io/CitcomsFormatVelocityVectorFieldExport.md) | file-io | 20 |
| [file-io/GpmlFormatMultiPointVectorFieldExport](../file-io/GpmlFormatMultiPointVectorFieldExport.md) | file-io | 9 |
| [app-logic/ResolvedTriangulationDelaunay2](../app-logic/ResolvedTriangulationDelaunay2.md) | app-logic | 6 |
| [file-io/TerraFormatVelocityVectorFieldExport](../file-io/TerraFormatVelocityVectorFieldExport.md) | file-io | 5 |
| [qt-widgets/KinematicGraphsDialog](../qt-widgets/KinematicGraphsDialog.md) | qt-widgets | 4 |
| [app-logic/ReconstructMethodHalfStageRotation](../app-logic/ReconstructMethodHalfStageRotation.md) | app-logic | 2 |
| [app-logic/ReconstructMethodInterface](../app-logic/ReconstructMethodInterface.md) | app-logic | 1 |
| [app-logic/ResolvedTopologicalBoundary](../app-logic/ResolvedTopologicalBoundary.md) | app-logic | 1 |
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 1 |
| [app-logic/TopologyReconstruct](../app-logic/TopologyReconstruct.md) | app-logic | 1 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/CalculateVelocity.h
python scripts/gpq.py def GPlatesMaths::VectorColatitudeLongitude --body
python scripts/gpq.py uses VectorColatitudeLongitude --kind class
python scripts/gpq.py hier VectorColatitudeLongitude
```

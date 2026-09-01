# DeformationStrainRate

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 124 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/DeformationStrainRate.h` | C++ | 271 |
| `src/app-logic/DeformationStrainRate.cc` | C++ | 87 |

## Overview

`DeformationStrainRate` is a small value type holding the instantaneous rate of
deformation at one point on a `TopologyNetworkResolver`-resolved deforming network, in
the local (theta, phi) tangent-plane basis. It stores the raw velocity spatial gradient
tensor `L` (`VelocitySpatialGradient`) and derives the symmetric rate-of-deformation
tensor `D = (L + transpose(L)) / 2` (`RateOfDeformation`) on demand, following the
continuum-mechanics treatment in Malvern's *Introduction to the Mechanics of a
Continuous Medium*. From `D` it exposes three scalar invariants consumers actually
plot or export: `get_strain_rate_dilatation()` (`trace(D)`, the instantaneous
fractional rate of volume change), `get_strain_rate_second_invariant()`
(`sqrt(trace(D^2))`, a magnitude of deformation), and `get_strain_rate_style()` (the
Kreemer et al. 2014 style ratio distinguishing extensional/compressional/strike-slip
regimes from the tensor's principal values).

It is a pure math type with no dependency on the reconstruction machinery: instances
are produced by strain-rate calculations in `TopologyNetworkResolver`/`ResolvedTriangulationDelaunay2`
and integrated over time into accumulated `DeformationStrain` by `ScalarCoverageEvolution`
and `TopologyReconstruct`, then consumed by the deformation exporters
(`GMTFormatDeformationExport`, `GpmlFormatDeformationExport`) and by
`presentation/ReconstructionGeometryRenderer` for colouring.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::DeformationStrainRate`](#gplatesapplogicdeformationstrainrate) | class | — | — | 0 | Stores the spatial gradients of velocity L from which the rate-of-deformation symmetric tensor D is obtained via: D = (L + transpose(L)) / 2 Both L and D are in units of (1/second). |

## Members

### `GPlatesAppLogic::DeformationStrainRate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VelocitySpatialGradient` | struct | `None` | public | Spatial gradients of velocity L. |
| `RateOfDeformation` | struct | `None` | public | Rate-of-deformation symmetric tensor D. |
| `DeformationStrainRate()` | constructor | `None` | public | Zero strain rate (non-deforming). |
| `DeformationStrainRate( const double &velocity_gradient_theta_theta, const double &velocity_gradient_theta_phi, const double &velocity_gradient_phi_theta, const double &velocity_gradient_phi_phi)` | constructor | `None` | public | Specify the (theta, theta), (theta, phi), (phi, theta) and (phi, phi) components of the velocity spatial gradient tensor L. |
| `get_rate_of_deformation()` | method | `RateOfDeformation` | public | Return the rate-of-deformation symmetric tensor D. |
| `get_strain_rate_dilatation()` | method | `double` | public | Return the strain rate dilatation. |
| `get_strain_rate_second_invariant()` | method | `double` | public | Return the strain rate second invariant. |
| `get_strain_rate_style()` | method | `double` | public | Return the strain rate style. |
| `d_velocity_spatial_gradient` | field | `VelocitySpatialGradient` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_DEFORMATION_STRAIN_RATE_H` | macro | `None` | — |

## Notes

`get_strain_rate_style()` divides by the larger-magnitude principal component of `D`
and returns NaN when the strain rate is exactly zero (0/0), since both principal
components are then zero; callers must guard against this for non-deforming regions.
The result is not clamped to [-1, 1] as in Kreemer et al. 2014 — callers that need the
clamped range must do it themselves. Both `L` and `D` are in units of 1/second.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 24 |
| [app-logic/ScalarCoverageEvolution](ScalarCoverageEvolution.md) | app-logic | 15 |
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 14 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 12 |
| [app-logic/DeformationStrain](DeformationStrain.md) | app-logic | 9 |
| [app-logic/ResolvedTriangulationDelaunay2](ResolvedTriangulationDelaunay2.md) | app-logic | 6 |
| [file-io/ReconstructedScalarCoverageExport](../file-io/ReconstructedScalarCoverageExport.md) | file-io | 4 |
| [file-io/GMTFormatDeformationExport](../file-io/GMTFormatDeformationExport.md) | file-io | 3 |
| [file-io/GpmlFormatDeformationExport](../file-io/GpmlFormatDeformationExport.md) | file-io | 3 |
| [file-io/GMTFormatReconstructedScalarCoverageExport](../file-io/GMTFormatReconstructedScalarCoverageExport.md) | file-io | 2 |
| [file-io/GpmlFormatReconstructedScalarCoverageExport](../file-io/GpmlFormatReconstructedScalarCoverageExport.md) | file-io | 2 |
| [app-logic/ScalarCoverageTimeSpan](ScalarCoverageTimeSpan.md) | app-logic | 1 |
| [app-logic/TopologyReconstructedFeatureGeometry](TopologyReconstructedFeatureGeometry.md) | app-logic | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/DeformationStrainRate.h
python scripts/gpq.py def GPlatesAppLogic::DeformationStrainRate --body
python scripts/gpq.py uses DeformationStrainRate --kind class
python scripts/gpq.py hier DeformationStrainRate
```

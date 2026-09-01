# DeformationStrain

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 124 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/DeformationStrain.h` | C++ | 246 |
| `src/app-logic/DeformationStrain.cc` | C++ | 303 |

## Overview

A small immutable value type holding one 2x2 deformation gradient tensor F, in the
local surface frame at a point: the axes are co-latitude (theta, pointing South)
and longitude (phi, pointing East), with no depth component. F answers "how has
the infinitesimal patch of crust around this point been stretched and sheared
since it started deforming". It is the *finite*, accumulated counterpart of
`DeformationStrainRate`, which holds the instantaneous velocity spatial gradient L
in the same frame; this unit and that one are deliberately the same shape, four
doubles and nothing else.

The reason both exist is the integration in `accumulate_strain`. A point carried
through a deforming network by
`TopologyReconstruct::GeometryTimeSpan` picks up a strain *rate* at each time step
from the network it happens to be inside; the total strain is the solution of
dF/dt = L·F along that point's path. `accumulate_strain` advances one step of that
ODE with a central-difference (trapezoidal) scheme, using both the previous and
the current L, which in matrix form is a 2x2 inversion and two multiplications.
`TopologyReconstruct::GeometryTimeSpan::initialise_deformation_total_strains` is
its only caller in the tree, and it walks the time span in order, feeding each
sample's F forward into the next. So a `DeformationStrain` is never computed
standalone — it is always a partial sum along a trajectory.

The two accessors are where the tensor becomes something a user sees.
`get_strain_dilatation` is `|det(F)| - 1`, the fractional area change of the patch
(the header derives it from the parallelepiped volume ratio and explains why the
2-D determinant gives the same answer as the 3-D one when there is no strain in
depth). `get_strain_principal` diagonalises the Cauchy deformation tensor
c = transpose(F⁻¹)·F⁻¹ to give the two principal engineering strains and the angle
of their axes. Those are what the deformation exporters
(`GMTFormatDeformationExport`, `GpmlFormatDeformationExport`, `DeformationExport`),
the scalar-coverage path (`ScalarCoverageTimeSpan`,
`ReconstructScalarCoverageLayerProxy`) and the strain-arrow rendering in
`ReconstructionGeometryRenderer` consume — none of them touch F directly.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::DeformationStrain`](#gplatesapplogicdeformationstrain) | class | — | — | 0 | Stores the deformation gradient tensor which can be used to get the strain tensor (also known as total strain or just strain) and its principal components. |

## Members

### `GPlatesAppLogic::DeformationStrain`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DeformationGradient` | struct | `None` | public | The deformation gradient tensor F. |
| `StrainPrincipal` | struct | `None` | public | — |
| `DeformationStrain()` | constructor | `None` | public | Identity strain. |
| `DeformationStrain( const DeformationGradient &deformation_gradient)` | constructor | `None` | public | — |
| `get_strain_dilatation()` | method | `double` | public | Essentially an initial parallelepiped of volume dV formed by parallel edge vectors dX1, dX2, dX2 is deformed into a parallelepiped of volume dv formed by parallel edge vectors dx1, dx2, dx2. |
| `get_strain_principal()` | method | `StrainPrincipal` | public | Return the principal strain. |
| `d_deformation_gradient` | field | `DeformationGradient` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_DEFORMATION_STRAIN_H` | macro | `None` | — |
| `accumulate_strain( const DeformationStrain &previous_strain, const DeformationStrainRate &previous_strain_rate, const DeformationStrainRate &current_strain_rate, const double &time_increment)` | function | `DeformationStrain` | Accumulate the previous strain using both the previous and current strain rates (units in 1/second) over a time increment (units in seconds). |
| `interpolate_strain( const DeformationStrain &first_strain, const DeformationStrain &second_strain, const double &position)` | function | `DeformationStrain` | Linearly interpolate between two strains. interpreted as where the returned strain lies in the range between the first strain and the second strain. |

## Notes

**Units are seconds and 1/second, not million years.** `accumulate_strain` documents
its strain rates as 1/second and its time increment as seconds, which is not the Ma
convention used almost everywhere else in app-logic — the caller in
`TopologyReconstruct` converts explicitly (`time_increment_in_seconds`). Nothing
checks this, and a wrong scale just produces plausible-looking wrong strain.

**Both degenerate paths fail silently.** If the implicit matrix
`I - L(n+1)·dt/2` has a determinant within `GPlatesMaths::EPSILON` of zero,
`accumulate_strain` returns the *previous* strain unchanged. If `det(F) <= 0`,
`get_strain_principal` returns `StrainPrincipal(0, 0, 0)`. Neither throws or
signals, so zero principal strain is indistinguishable from "F was not invertible",
and a stalled accumulation looks like a step with no deformation. Both are
commented as should-not-happen cases.

**The default constructors mean "not deforming", and they differ between the two
types.** `DeformationStrain()` is the *identity* F, whereas `DeformationStrainRate()`
is the *zero* L. `TopologyReconstruct` relies on exactly this when a point has no
recorded strain or strain rate yet.

**`get_strain_principal` normalises the ordering, and the angle follows it.**
`principal1` is always the larger (positive is extension, negative compression);
when the raw eigenvalues come out the other way the code swaps them *and* adds
90 degrees to the angle, because the angle is specified relative to `principal1`.
The angle is counter-clockwise viewed from outside the globe, since x is
co-latitude and y is longitude. If you consume the angle, do not assume it lies in
`atan2`'s original half-range — the swap can push it past it.

**`interpolate_strain` interpolates F, not strain.** It blends the four tensor
components linearly. Dilatation and principal strains are non-linear functions of
those components, so interpolating a strain and then asking for its dilatation is
not the same as interpolating the two dilatations. That is deliberate — F is the
quantity that composes — but it means you cannot substitute one for the other.
The function also does not clamp `position`; feeding it a value outside [0, 1]
extrapolates.

**Cheap, copyable, and treated as immutable.** Four doubles, no virtuals, no
allocation. `TopologyReconstruct` allocates them from a pool and, when a step
produces no change, shares a single instance's pointer between successive geometry
samples — so mutating one in place would corrupt other samples. There is no
mutating API, and it should stay that way. The whole unit is stateless free
functions plus a value type, so there is nothing to synchronise across threads.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructScalarCoverageLayerProxy](ReconstructScalarCoverageLayerProxy.md) | app-logic | 26 |
| [file-io/GMTFormatDeformationExport](../file-io/GMTFormatDeformationExport.md) | file-io | 25 |
| [app-logic/ReconstructMethodRegistry](ReconstructMethodRegistry.md) | app-logic | 20 |
| [presentation/LayerOutputRenderer](../presentation/LayerOutputRenderer.md) | presentation | 18 |
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 17 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 17 |
| [file-io/GMTFormatReconstructedScalarCoverageExport](../file-io/GMTFormatReconstructedScalarCoverageExport.md) | file-io | 15 |
| [app-logic/ReconstructionGeometryVisitor](ReconstructionGeometryVisitor.md) | app-logic | 11 |
| [app-logic/ReconstructionLayerTask](ReconstructionLayerTask.md) | app-logic | 11 |
| [app-logic/ScalarCoverageTimeSpan](ScalarCoverageTimeSpan.md) | app-logic | 11 |
| [file-io/DeformationExport](../file-io/DeformationExport.md) | file-io | 11 |
| [app-logic/ReconstructParams](ReconstructParams.md) | app-logic | 8 |
| [app-logic/TopologyReconstructedFeatureGeometry](TopologyReconstructedFeatureGeometry.md) | app-logic | 8 |
| [file-io/GpmlFormatDeformationExport](../file-io/GpmlFormatDeformationExport.md) | file-io | 8 |
| [model/WeakObserverVisitor](../model/WeakObserverVisitor.md) | model | 7 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 7 |
| [app-logic/ReconstructedScalarCoverage](ReconstructedScalarCoverage.md) | app-logic | 6 |
| [cli/CliReconstructCommand](../cli/CliReconstructCommand.md) | cli | 4 |
| [qt-widgets/TotalReconstructionPolesDialog](../qt-widgets/TotalReconstructionPolesDialog.md) | qt-widgets | 4 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 2 |

*... and 1 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/DeformationStrain.h
python scripts/gpq.py def GPlatesAppLogic::DeformationStrain --body
python scripts/gpq.py uses DeformationStrain --kind class
python scripts/gpq.py hier DeformationStrain
```

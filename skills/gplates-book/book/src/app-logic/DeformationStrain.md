# DeformationStrain

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 124 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/DeformationStrain.h` | C++ | 246 |
| `src/app-logic/DeformationStrain.cc` | C++ | 303 |

## Overview

[[[PROSE overview unit=app-logic/DeformationStrain tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=app-logic/DeformationStrain tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

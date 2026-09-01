# ReconstructMethodFiniteRotation

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 597 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructMethodFiniteRotation.h` | C++ | 158 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructMethodFiniteRotation tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructMethodFiniteRotation`](#gplatesapplogicreconstructmethodfiniterotation) | class | [`GPlatesUtils::ReferenceCount<ReconstructMethodFiniteRotation>`](../utils/ReferenceCount.md)<br>`boost::equivalent<ReconstructMethodFiniteRotation>` | — | 3 | Base class for representing a finite rotation reconstruction for a particular 'ReconstructMethod::Type' reconstruct method type. |

## Members

### `GPlatesAppLogic::ReconstructMethodFiniteRotation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructMethodFiniteRotation>` | public | Convenience typedefs for a shared pointer to a ReconstructMethodFiniteRotation. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructMethodFiniteRotation>` | public | — |
| `~ReconstructMethodFiniteRotation()` | destructor | `None` | public | — |
| `transform( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry)` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | Transforms (reconstructs) the specified geometry. |
| `ReconstructMethodFiniteRotation( ReconstructMethod::Type reconstruct_method_type, const GPlatesMaths::FiniteRotation &finite_rotation)` | constructor | `None` | protected | Constructor instantiated by derived class. |
| `less_than_compare_finite_rotation_parameters( const ReconstructMethodFiniteRotation &rhs)` | method | `bool` | protected | Derived classes implement this method to compare parameters used to generate the finite rotation - these parameters are compared instead of the finite rotation because it is cheaper (eg, comparing a plate id versus comparing each double in ... |
| `d_reconstruct_method_type` | field | `ReconstructMethod::Type` | private | — |
| `d_finite_rotation` | field | `GPlatesMaths::FiniteRotation` | private | The finite rotation - note that it is \*not\* used in the comparison. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTMETHODFINITEROTATION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructMethodFiniteRotation tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/GeometryCookieCutter](GeometryCookieCutter.md) | app-logic | 57 |
| [app-logic/TopologyInternalUtils](TopologyInternalUtils.md) | app-logic | 39 |
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 34 |
| [app-logic/ResolvedTopologicalSubSegmentImpl](ResolvedTopologicalSubSegmentImpl.md) | app-logic | 31 |
| [opengl/GLReconstructedStaticPolygonMeshes](../opengl/GLReconstructedStaticPolygonMeshes.md) | opengl | 28 |
| [file-io/OgrFormatResolvedTopologicalGeometryExport](../file-io/OgrFormatResolvedTopologicalGeometryExport.md) | file-io | 19 |
| [view-operations/GeometryBuilder](../view-operations/GeometryBuilder.md) | view-operations | 17 |
| [app-logic/ReconstructedFeatureGeometry](ReconstructedFeatureGeometry.md) | app-logic | 15 |
| [app-logic/TopologyPointLocation](TopologyPointLocation.md) | app-logic | 15 |
| [file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport](../file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport.md) | file-io | 15 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 15 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 13 |
| [file-io/GpmlFormatReconstructedScalarCoverageExport](../file-io/GpmlFormatReconstructedScalarCoverageExport.md) | file-io | 13 |
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 11 |
| [view-operations/MoveVertexGeometryOperation](../view-operations/MoveVertexGeometryOperation.md) | view-operations | 11 |
| [app-logic/TopologyGeometryResolver](TopologyGeometryResolver.md) | app-logic | 10 |
| [app-logic/LayerProxyUtils](LayerProxyUtils.md) | app-logic | 9 |
| [file-io/OgrFormatReconstructedFeatureGeometryExport](../file-io/OgrFormatReconstructedFeatureGeometryExport.md) | file-io | 9 |
| [file-io/GpmlFormatDeformationExport](../file-io/GpmlFormatDeformationExport.md) | file-io | 8 |
| [file-io/OgrFormatFlowlineExport](../file-io/OgrFormatFlowlineExport.md) | file-io | 8 |

*... and 24 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructMethodFiniteRotation.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructMethodFiniteRotation --body
python scripts/gpq.py uses ReconstructMethodFiniteRotation --kind class
python scripts/gpq.py hier ReconstructMethodFiniteRotation
```

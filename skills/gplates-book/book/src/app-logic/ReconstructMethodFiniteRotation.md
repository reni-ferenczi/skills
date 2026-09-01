# ReconstructMethodFiniteRotation

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 597 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructMethodFiniteRotation.h` | C++ | 158 |

## Overview

A `GPlatesMaths::FiniteRotation` that remembers *why* it is that rotation, so
that two of them can be compared cheaply. Comparing finite rotations directly
means comparing several doubles with an epsilon; comparing the parameters they
were derived from usually means comparing one plate ID. This class carries the
rotation plus a `ReconstructMethod::Type` tag, and delegates the actual
comparison to the derived class through
`less_than_compare_finite_rotation_parameters`. `boost::equivalent` then derives
`operator==` from that ordering, and the rotation itself is never looked at
during a comparison.

The three subclasses are all called `Transform` and all live in anonymous
namespaces inside the corresponding reconstruct method's `.cc`
(`ReconstructMethodByPlateId`, `ReconstructMethodHalfStageRotation`,
`ReconstructMethodVirtualGeomagneticPole`), so this header is the only public
face of them. The by-plate-ID one, for example, holds a
`boost::optional<integer_plate_id_type>` and compares on that alone.

The pay-off is downstream. A `ReconstructedFeatureGeometry` that was produced by
a rigid rotation exposes a `FiniteRotationReconstruction` holding one of these
alongside the *unreconstructed* geometry, which lets consumers defer or skip the
transform entirely. `GLReconstructedStaticPolygonMeshes` is the clearest case:
it keys a `std::map` on `boost::reference_wrapper<const ReconstructMethodFiniteRotation>`
to bucket every reconstructed polygon mesh sharing a rotation into one transform
group, then uploads a single matrix per group to the GPU. That grouping is only
affordable because equality here is a plate-ID comparison rather than a
floating-point one. `ReconstructLayerProxy` exploits the same property when
inserting into its spatial partitions.

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

**The contract a subclass must uphold:** equal parameters must imply an equal
finite rotation. `operator<` compares `d_reconstruct_method_type` first and only
calls the virtual comparison when the types match, so a subclass may
`dynamic_cast` `rhs` to its own type without checking — but that is safe only
while exactly one class exists per `ReconstructMethod::Type`. Introducing a
second subclass under an existing tag would make that cast throw. If two objects
compare equal but hold different rotations, consumers that group by transform
(`GLReconstructedStaticPolygonMeshes`) will silently render geometries with the
wrong matrix.

**Not every reconstruction has one.** Reconstruct methods that do not reduce to
a rigid rotation — deformation via topologies in particular — produce no
`ReconstructMethodFiniteRotation` at all, and
`ReconstructedFeatureGeometry::finite_rotation_reconstruction()` returns
`boost::none`. Code that wants the fast path must handle that case; the pattern
in the tree is to fall back to the already-reconstructed geometry.

Instances are reference-counted (`GPlatesUtils::ReferenceCount`) and immutable
after construction, so sharing one across transform groups and spatial
partitions is intended. When storing them in an associative container, note that
comparison is defined on the object and not on the pointer, so a
`reference_wrapper` (or an explicit comparator) is required — comparing
`non_null_ptr_type` values compares addresses instead and defeats the grouping.

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

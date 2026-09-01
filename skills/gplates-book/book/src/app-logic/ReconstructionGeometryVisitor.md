# ReconstructionGeometryVisitor

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 2 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionGeometryVisitor.h` | C++ | 324 |
| `src/app-logic/ReconstructionGeometryVisitor.cc` | C++ | 113 |

## Overview

This is the Visitor half of the double dispatch that `ReconstructionGeometry` exposes through its two `accept_visitor` overloads. It is written once as a template over the visited type rather than twice for const and non-const: `GPlatesUtils::CopyConst` propagates the const-ness of the template argument onto every concrete reconstruction-geometry type, so a single class body serves both `ReconstructionGeometryVisitor` and `ConstReconstructionGeometryVisitor`. Only those two instantiations exist — the `.cc` instantiates them explicitly and nothing else will link.

Every `visit` overload has a default body, so a concrete visitor overrides only the cases it cares about, but the defaults come in two kinds and the difference is the important part. For the eight types that derive directly from `ReconstructionGeometry` the default is empty and inline. For the seven that derive from another visitable type the default is defined in the `.cc` and `static_pointer_cast`s the argument up to its base before re-dispatching: `ReconstructedFlowline`, `ReconstructedMotionPath`, `ReconstructedSmallCircle`, `ReconstructedVirtualGeomagneticPole` and `TopologyReconstructedFeatureGeometry` all fall through to the `ReconstructedFeatureGeometry` overload, and `ResolvedTopologicalBoundary` and `ResolvedTopologicalLine` fall through to `ResolvedTopologicalGeometry`. A visitor that overrides only `visit(...reconstructed_feature_geometry_type...)` therefore sees flowlines, motion paths, small circles, VGPs and topology-reconstructed geometries too, unless it also overrides the specific overload and stops the delegation. `ReconstructionGeometryUtils::ReconstructionGeometryDerivedTypeFinder` is built entirely on that behaviour, and so are the property-extraction visitors in the same file.

Adding a new `ReconstructionGeometry` subclass means touching this header: forward-declare it, add its `CopyConst` typedef, add the `visit` overload, and — if it derives from an existing visitable type rather than from `ReconstructionGeometry` directly — add the delegating default to the `.cc`, which needs the full class definition for the cast and so includes each such header.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructionGeometryVisitor`](#gplatesapplogicreconstructiongeometryvisitor) | typedef | — | — | 0 | Typedef for visitor over non-const ReconstructionGeometry objects. |
| [`GPlatesAppLogic::ConstReconstructionGeometryVisitor`](#gplatesapplogicconstreconstructiongeometryvisitor) | typedef | — | — | 0 | Typedef for visitor over const ReconstructionGeometry objects. |
| [`GPlatesAppLogic::ReconstructionGeometryVisitorBase`](#gplatesapplogicreconstructiongeometryvisitorbase) | class | — | `<class ReconstructionGeometryType>` | 1 | This class defines an abstract interface for a Visitor to visit reconstruction geometries. |

## Members

### `GPlatesAppLogic::ReconstructionGeometryVisitor`

*None.*

### `GPlatesAppLogic::ConstReconstructionGeometryVisitor`

*None.*

### `GPlatesAppLogic::ReconstructionGeometryVisitorBase`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `co_registration_data_type` | typedef | `typename GPlatesUtils::CopyConst< ReconstructionGeometryType, CoRegistrationData>::type` | public | Typedef for CoRegistrationData of appropriate const-ness. |
| `multi_point_vector_field_type` | typedef | `typename GPlatesUtils::CopyConst< ReconstructionGeometryType, MultiPointVectorField>::type` | public | Typedef for MultiPointVectorField of appropriate const-ness. |
| `reconstructed_feature_geometry_type` | typedef | `typename GPlatesUtils::CopyConst< ReconstructionGeometryType, ReconstructedFeatureGeometry>::type` | public | Typedef for ReconstructedFeatureGeometry of appropriate const-ness. |
| `reconstructed_flowline_type` | typedef | `typename GPlatesUtils::CopyConst< ReconstructionGeometryType, ReconstructedFlowline>::type` | public | Typedef for ReconstructedFlowline of appropriate const-ness. |
| `reconstructed_motion_path_type` | typedef | `typename GPlatesUtils::CopyConst< ReconstructionGeometryType, ReconstructedMotionPath>::type` | public | Typedef for ReconstructedMotionPath of appropriate const-ness. |
| `reconstructed_scalar_coverage_type` | typedef | `typename GPlatesUtils::CopyConst< ReconstructionGeometryType, ReconstructedScalarCoverage>::type` | public | Typedef for ReconstructedScalarCoverage of appropriate const-ness. |
| `reconstructed_small_circle_type` | typedef | `typename GPlatesUtils::CopyConst< ReconstructionGeometryType, ReconstructedSmallCircle>::type` | public | Typedef for ReconstructedSmallCircle of appropriate const-ness. |
| `reconstructed_virtual_geomagnetic_pole_type` | typedef | `typename GPlatesUtils::CopyConst< ReconstructionGeometryType, ReconstructedVirtualGeomagneticPole>::type` | public | Typedef for ReconstructedFeatureGeometry of appropriate const-ness. |
| `resolved_raster_type` | typedef | `typename GPlatesUtils::CopyConst< ReconstructionGeometryType, ResolvedRaster>::type` | public | Typedef for ResolvedRaster of appropriate const-ness. |
| `resolved_scalar_field_3d_type` | typedef | `typename GPlatesUtils::CopyConst< ReconstructionGeometryType, ResolvedScalarField3D>::type` | public | Typedef for ResolvedScalarField3D of appropriate const-ness. |
| `resolved_topological_boundary_type` | typedef | `typename GPlatesUtils::CopyConst< ReconstructionGeometryType, ResolvedTopologicalBoundary>::type` | public | Typedef for ResolvedTopologicalBoundary of appropriate const-ness. |
| `resolved_topological_geometry_type` | typedef | `typename GPlatesUtils::CopyConst< ReconstructionGeometryType, ResolvedTopologicalGeometry>::type` | public | Typedef for ResolvedTopologicalGeometry of appropriate const-ness. |
| `resolved_topological_line_type` | typedef | `typename GPlatesUtils::CopyConst< ReconstructionGeometryType, ResolvedTopologicalLine>::type` | public | Typedef for ResolvedTopologicalLine of appropriate const-ness. |
| `resolved_topological_network_type` | typedef | `typename GPlatesUtils::CopyConst< ReconstructionGeometryType, ResolvedTopologicalNetwork>::type` | public | Typedef for ResolvedTopologicalNetwork of appropriate const-ness. |
| `topology_reconstructed_feature_geometry_type` | typedef | `typename GPlatesUtils::CopyConst< ReconstructionGeometryType, TopologyReconstructedFeatureGeometry>::type` | public | Typedef for TopologyReconstructedFeatureGeometry of appropriate const-ness. |
| `~ReconstructionGeometryVisitorBase()` | destructor | `None` | public | We'll make this function pure virtual so that the class is abstract. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<co_registration_data_type> &crd)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<multi_point_vector_field_type> &mpvf)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_feature_geometry_type> &rfg)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_flowline_type> &rf)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_motion_path_type> &rmp)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_scalar_coverage_type> &rsc)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_small_circle_type> &rsc)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_virtual_geomagnetic_pole_type> &rvgp)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_raster_type> &rr)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_scalar_field_3d_type> &rsf)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_boundary_type> &rtb)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_geometry_type> &rtg)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_line_type> &rtl)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_network_type> &rtn)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<topology_reconstructed_feature_geometry_type> &trfg)` | method | `void` | public | Override this function in your own derived class. |
| `operator=` | field | `ReconstructionGeometryVisitorBase` | private | This operator should never be defined, because we don't want to allow copy-assignment. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTIONGEOMETRYVISITOR_H` | macro | `None` | — |

## Notes

`visit` is an overload set, so a derived visitor that declares any `visit` of its own hides all fifteen inherited ones. Every visitor in the tree opens with `using base_class_type::visit;` (or `using ConstReconstructionGeometryVisitor::visit;`) for exactly this reason; leaving it out does not fail loudly — the delegating defaults stop being reachable and the visitor quietly stops seeing derived types.

The destructor is pure virtual purely to make the class abstract, since every other member has a definition; its out-of-line inline body at the bottom of the header is what keeps that legal. Copy-assignment is declared private and never defined.

`ReconstructionGeometryVisitor` and `ConstReconstructionGeometryVisitor` are also typedef'd, identically, in `ReconstructionGeometry.h` so that the base class need not include this header. Both copies have to change together.

The header comment asks that the overloads be kept in alphabetical order by visited type; it is worth honouring, because the only way to see whether a type is handled is to read the list.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 91 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 40 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 36 |
| [app-logic/GeometryCookieCutter](GeometryCookieCutter.md) | app-logic | 28 |
| [app-logic/TopologyGeometryResolver](TopologyGeometryResolver.md) | app-logic | 18 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 18 |
| [app-logic/ResolvedTopologicalSubSegmentImpl](ResolvedTopologicalSubSegmentImpl.md) | app-logic | 17 |
| [app-logic/TopologyPointLocation](TopologyPointLocation.md) | app-logic | 15 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 13 |
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 13 |
| [app-logic/ScalarField3DLayerProxy](ScalarField3DLayerProxy.md) | app-logic | 11 |
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 11 |
| [app-logic/TopologyReconstructedFeatureGeometry](TopologyReconstructedFeatureGeometry.md) | app-logic | 11 |
| [app-logic/ResolvedTopologicalBoundary](ResolvedTopologicalBoundary.md) | app-logic | 10 |
| [app-logic/ResolvedTopologicalLine](ResolvedTopologicalLine.md) | app-logic | 10 |
| [app-logic/TopologyInternalUtils](TopologyInternalUtils.md) | app-logic | 8 |
| [app-logic/ResolvedTopologicalNetwork](ResolvedTopologicalNetwork.md) | app-logic | 7 |
| [view-operations/VisibleReconstructionGeometryExport](../view-operations/VisibleReconstructionGeometryExport.md) | view-operations | 7 |
| [app-logic/LayerProxyUtils](LayerProxyUtils.md) | app-logic | 6 |
| [file-io/GMTFormatDeformationExport](../file-io/GMTFormatDeformationExport.md) | file-io | 6 |

*... and 35 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructionGeometryVisitor.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructionGeometryVisitorBase --body
python scripts/gpq.py uses ReconstructionGeometryVisitorBase --kind class
python scripts/gpq.py hier ReconstructionGeometryVisitorBase
```

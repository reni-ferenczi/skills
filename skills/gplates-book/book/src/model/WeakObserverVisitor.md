# WeakObserverVisitor

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 213 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/WeakObserverVisitor.h` | C++ | 283 |
| `src/model/WeakObserverVisitor.cc` | C++ | 97 |

## Overview

[[[PROSE overview unit=model/WeakObserverVisitor tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::WeakObserverVisitor`](#gplatesmodelweakobservervisitor) | class | — | `<typename H>` | 7 | This class defines an abstract interface for a Visitor to visit weak observers. |
| [`GPlatesModel::WeakObserverVisitor<FeatureHandle>`](#gplatesmodelweakobservervisitorfeaturehandle) | class | — | `<>` | 0 | This class defines an abstract interface for a Visitor to visit weak observers. |

## Members

### `GPlatesModel::WeakObserverVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~WeakObserverVisitor()` | destructor | `None` | public | — |
| `visit_revision_aware_iterator( RevisionAwareIterator<H> &rai)` | method | `void` | public | Override this function in your own derived class. |
| `visit_weak_reference( WeakReference<H> &wr)` | method | `void` | public | Override this function in your own derived class. |
| `operator=` | field | `WeakObserverVisitor` | private | This operator should never be defined, because we don't want to allow copy-assignment. |

### `GPlatesModel::WeakObserverVisitor<FeatureHandle>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~WeakObserverVisitor()` | destructor | `None` | public | — |
| `visit_multi_point_vector_field( GPlatesAppLogic::MultiPointVectorField &mpvf)` | method | `void` | public | Override this function in your own derived class. |
| `visit_reconstructed_feature_geometry( GPlatesAppLogic::ReconstructedFeatureGeometry &rfg)` | method | `void` | public | Override this function in your own derived class. |
| `visit_reconstructed_flowline( GPlatesAppLogic::ReconstructedFlowline &rf)` | method | `void` | public | Override this function in your own derived class. |
| `visit_reconstructed_motion_path( GPlatesAppLogic::ReconstructedMotionPath &rmp)` | method | `void` | public | Override this function in your own derived class. |
| `visit_reconstructed_scalar_coverage( GPlatesAppLogic::ReconstructedScalarCoverage &rsc)` | method | `void` | public | Override this function in your own derived class. |
| `visit_reconstructed_small_circle( GPlatesAppLogic::ReconstructedSmallCircle &rsc)` | method | `void` | public | Override this function in your own derived class. |
| `visit_reconstructed_virtual_geomagnetic_pole( GPlatesAppLogic::ReconstructedVirtualGeomagneticPole &rvgp)` | method | `void` | public | Override this function in your own derived class. |
| `visit_resolved_raster( GPlatesAppLogic::ResolvedRaster &rr)` | method | `void` | public | Override this function in your own derived class. |
| `visit_resolved_scalar_field_3d( GPlatesAppLogic::ResolvedScalarField3D &rsf)` | method | `void` | public | Override this function in your own derived class. |
| `visit_resolved_topological_boundary( GPlatesAppLogic::ResolvedTopologicalBoundary &rtb)` | method | `void` | public | Override this function in your own derived class. |
| `visit_resolved_topological_geometry( GPlatesAppLogic::ResolvedTopologicalGeometry &rtg)` | method | `void` | public | Override this function in your own derived class. |
| `visit_resolved_topological_line( GPlatesAppLogic::ResolvedTopologicalLine &rtl)` | method | `void` | public | Override this function in your own derived class. |
| `visit_resolved_topological_network( GPlatesAppLogic::ResolvedTopologicalNetwork &rtn)` | method | `void` | public | Override this function in your own derived class. |
| `visit_topology_reconstructed_feature_geometry( GPlatesAppLogic::TopologyReconstructedFeatureGeometry &rtfg)` | method | `void` | public | Override this function in your own derived class. |
| `visit_revision_aware_iterator( RevisionAwareIterator<H> &rai)` | method | `void` | public | Override this function in your own derived class. |
| `visit_weak_reference( WeakReference<FeatureHandle> &wr)` | method | `void` | public | Override this function in your own derived class. |
| `operator=` | field | `WeakObserverVisitor` | private | This operator should never be defined, because we don't want to allow copy-assignment. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_WEAKOBSERVERVISITOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=model/WeakObserverVisitor tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructedMotionPath](../app-logic/ReconstructedMotionPath.md) | app-logic | 6 |
| [app-logic/ReconstructedVirtualGeomagneticPole](../app-logic/ReconstructedVirtualGeomagneticPole.md) | app-logic | 6 |
| [app-logic/ReconstructionGeometryFinder](../app-logic/ReconstructionGeometryFinder.md) | app-logic | 5 |
| [qt-widgets/deprecated/CreateTopologyWidget](../qt-widgets/deprecated/CreateTopologyWidget.md) | qt-widgets | 4 |
| [app-logic/ReconstructedFeatureGeometry](../app-logic/ReconstructedFeatureGeometry.md) | app-logic | 2 |
| [app-logic/ResolvedRaster](../app-logic/ResolvedRaster.md) | app-logic | 2 |
| [app-logic/ResolvedScalarField3D](../app-logic/ResolvedScalarField3D.md) | app-logic | 2 |
| [app-logic/ResolvedTopologicalBoundary](../app-logic/ResolvedTopologicalBoundary.md) | app-logic | 2 |
| [app-logic/ResolvedTopologicalGeometry](../app-logic/ResolvedTopologicalGeometry.md) | app-logic | 2 |
| [app-logic/ResolvedTopologicalLine](../app-logic/ResolvedTopologicalLine.md) | app-logic | 2 |
| [app-logic/ResolvedTopologicalNetwork](../app-logic/ResolvedTopologicalNetwork.md) | app-logic | 2 |
| [model/WeakReference](WeakReference.md) | model | 2 |
| [app-logic/MultiPointVectorField](../app-logic/MultiPointVectorField.md) | app-logic | 1 |
| [app-logic/ReconstructedFeatureGeometryFinder](../app-logic/ReconstructedFeatureGeometryFinder.md) | app-logic | 1 |
| [app-logic/ReconstructedScalarCoverage](../app-logic/ReconstructedScalarCoverage.md) | app-logic | 1 |
| [model/WeakObserverPublisher](WeakObserverPublisher.md) | model | 1 |
| [model/WeakReferenceVisitors](WeakReferenceVisitors.md) | model | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/WeakObserverVisitor.h
python scripts/gpq.py def GPlatesModel::WeakObserverVisitor<FeatureHandle> --body
python scripts/gpq.py uses WeakObserverVisitor<FeatureHandle> --kind class
python scripts/gpq.py hier WeakObserverVisitor<FeatureHandle>
```

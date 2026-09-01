# ReconstructedMotionPath

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 798 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructedMotionPath.h` | C++ | 204 |
| `src/app-logic/ReconstructedMotionPath.cc` | C++ | 55 |

## Overview

`ReconstructedMotionPath` is the `ReconstructedFeatureGeometry` specialisation for motion tracks: a single `motion_path_points` polyline traced by a seed point as it moves under a fixed `reconstruction_plate_id`, together with the seed point's present-day and reconstructed positions. Structurally it mirrors `ReconstructedFlowline` but tracks one plate's motion rather than two plates diverging from a spreading point, and as with flowlines the base class's reconstructed geometry deliberately holds *all* seed points so geometry-editing tools like move-vertex keep working.

Instances are created only through the private constructor via `create()`, so a `ReconstructedMotionPath` always lives behind `non_null_ptr_type` rather than on the stack.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructedMotionPath`](#gplatesapplogicreconstructedmotionpath) | class | [`ReconstructedFeatureGeometry`](ReconstructedFeatureGeometry.md) | — | 0 | A reconstructed motion track. |

## Members

### `GPlatesAppLogic::ReconstructedMotionPath`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructedMotionPath>` | public | A convenience typedef for a non-null shared pointer to a non-const ReconstructedMotionPath. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructedMotionPath>` | public | A convenience typedef for a non-null shared pointer to a const ReconstructedMotionPath. |
| `maybe_null_ptr_type` | typedef | `boost::intrusive_ptr<ReconstructedMotionPath>` | public | A convenience typedef for boost::intrusive\_ptr\<ReconstructedMotionPath\>. |
| `maybe_null_ptr_to_const_type` | typedef | `boost::intrusive_ptr<const ReconstructedMotionPath>` | public | A convenience typedef for boost::intrusive\_ptr\<const ReconstructedMotionPath\>. |
| `seed_point_type` | typedef | `GPlatesMaths::PointOnSphere` | public | A convenience typedef for a PointOnSphere. |
| `feature_geom_ptr_type` | typedef | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | A convenience typedef for a GeometryOnSphere::non\_null\_ptr\_to\_const type. |
| `motion_path_geom_ptr_type` | typedef | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | public | A convenience typedef for a PointOnSphere::non\_null\_ptr\_to\_const type. |
| `create( const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree, const ReconstructionTreeCreator &reconstruction_tree_creator, const seed_point_type &present_day_seed_point, const seed_point_type &reconstructed_seed_point, const motion_path_geom_ptr_type &motion_path_points, const GPlatesModel::intege ...` | method | `non_null_ptr_type` | public | Create a ReconstructedMotionPath instance with an optional reconstruction plate ID and an optional time of formation. |
| `accept_visitor( ConstReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ConstReconstructionGeometryVisitor instance. |
| `accept_visitor( ReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ReconstructionGeometryVisitor instance. |
| `accept_weak_observer_visitor( GPlatesModel::WeakObserverVisitor<GPlatesModel::FeatureHandle> &visitor)` | method | `void` | public | Accept a WeakObserverVisitor instance. |
| `motion_path_points()` | method | `motion_path_geom_ptr_type` | public | — |
| `ReconstructedMotionPath( const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree_, const ReconstructionTreeCreator &reconstruction_tree_creator, const seed_point_type &present_day_seed_point, const seed_point_type &reconstructed_seed_point, const motion_path_geom_ptr_type &motion_path_points_, const G ...` | constructor | `None` | private | Instantiate a reconstructed motion path. |
| `d_present_day_seed_point` | field | `GPlatesMaths::PointOnSphere` | private | — |
| `d_reconstructed_seed_point` | field | `GPlatesMaths::PointOnSphere` | private | — |
| `d_motion_path_points` | field | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTEDMOTIONPATH_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GMTFormatMotionPathExport](../file-io/GMTFormatMotionPathExport.md) | file-io | 10 |
| [file-io/OgrFormatMotionPathExport](../file-io/OgrFormatMotionPathExport.md) | file-io | 6 |
| [file-io/ReconstructedMotionPathExport](../file-io/ReconstructedMotionPathExport.md) | file-io | 4 |
| [app-logic/MotionPathGeometryPopulator](MotionPathGeometryPopulator.md) | app-logic | 2 |
| [model/WeakObserverVisitor](../model/WeakObserverVisitor.md) | model | 2 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 2 |
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 1 |
| [app-logic/ReconstructionGeometryVisitor](ReconstructionGeometryVisitor.md) | app-logic | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructedMotionPath.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructedMotionPath --body
python scripts/gpq.py uses ReconstructedMotionPath --kind class
python scripts/gpq.py hier ReconstructedMotionPath
```

# ReconstructedFlowline

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 695 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructedFlowline.h` | C++ | 231 |
| `src/app-logic/ReconstructedFlowline.cc` | C++ | 52 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructedFlowline tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructedFlowline`](#gplatesapplogicreconstructedflowline) | class | [`ReconstructedFeatureGeometry`](ReconstructedFeatureGeometry.md) | — | 0 | — |

## Members

### `GPlatesAppLogic::ReconstructedFlowline`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructedFlowline>` | public | A convenience typedef for a non-null shared pointer to a non-const ReconstructedFlowline. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructedFlowline>` | public | A convenience typedef for a non-null shared pointer to a const ReconstructedFlowline. |
| `maybe_null_ptr_type` | typedef | `boost::intrusive_ptr<ReconstructedFlowline>` | public | A convenience typedef for boost::intrusive\_ptr\<ReconstructedFlowline\>. |
| `maybe_null_ptr_to_const_type` | typedef | `boost::intrusive_ptr<const ReconstructedFlowline>` | public | A convenience typedef for boost::intrusive\_ptr\<const ReconstructedFlowline\>. |
| `seed_point_type` | typedef | `GPlatesMaths::PointOnSphere` | public | A convenience typedef for a PointOnSphere type. |
| `feature_geom_ptr_type` | typedef | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | A convenience typedef for a GeometryOnSphere::non\_null\_ptr\_to\_const type. |
| `flowline_geom_ptr_type` | typedef | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | public | A convenience typedef for a PointOnSphere::non\_null\_ptr\_to\_const type. |
| `create( const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree, const ReconstructionTreeCreator &reconstruction_tree_creator, const seed_point_type &present_day_seed_point, const seed_point_type &reconstructed_seed_point, const flowline_geom_ptr_type &left_flowline_points, const flowline_geom_ptr_typ ...` | method | `non_null_ptr_type` | public | Create a ReconstructedFlowline instance with an optional reconstruction plate ID and an optional time of formation. |
| `accept_visitor( ConstReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ConstReconstructionGeometryVisitor instance. |
| `accept_visitor( ReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ReconstructionGeometryVisitor instance. |
| `accept_weak_observer_visitor( GPlatesModel::WeakObserverVisitor<GPlatesModel::FeatureHandle> &visitor)` | method | `void` | public | Accept a WeakObserverVisitor instance. |
| `left_flowline_points()` | method | `flowline_geom_ptr_type` | public | — |
| `right_flowline_points()` | method | `flowline_geom_ptr_type` | public | — |
| `left_plate_id()` | method | `GPlatesModel::integer_plate_id_type` | public | — |
| `right_plate_id()` | method | `GPlatesModel::integer_plate_id_type` | public | — |
| `ReconstructedFlowline( const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree_, const ReconstructionTreeCreator &reconstruction_tree_creator, const seed_point_type &present_day_seed_point, const seed_point_type &reconstructed_seed_point, const flowline_geom_ptr_type &left_flowline_points_, const flow ...` | constructor | `None` | private | Instantiate a reconstructed flowline. |
| `d_present_day_seed_point` | field | `seed_point_type` | private | — |
| `d_reconstructed_seed_point` | field | `seed_point_type` | private | — |
| `d_left_flowline_points` | field | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | private | — |
| `d_right_flowline_points` | field | `GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type` | private | — |
| `d_left_plate_id` | field | `GPlatesModel::integer_plate_id_type` | private | Left/Right plate ids are here purely for colouring. |
| `d_right_plate_id` | field | `GPlatesModel::integer_plate_id_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTEDFLOWLINE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructedFlowline tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GMTFormatFlowlineExport](../file-io/GMTFormatFlowlineExport.md) | file-io | 13 |
| [file-io/OgrFormatFlowlineExport](../file-io/OgrFormatFlowlineExport.md) | file-io | 7 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 6 |
| [file-io/ReconstructedFlowlineExport](../file-io/ReconstructedFlowlineExport.md) | file-io | 4 |
| [app-logic/FlowlineGeometryPopulator](FlowlineGeometryPopulator.md) | app-logic | 3 |
| [model/WeakObserverVisitor](../model/WeakObserverVisitor.md) | model | 2 |
| [app-logic/MotionPathGeometryPopulator](MotionPathGeometryPopulator.md) | app-logic | 1 |
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 1 |
| [app-logic/ReconstructionGeometryVisitor](ReconstructionGeometryVisitor.md) | app-logic | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructedFlowline.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructedFlowline --body
python scripts/gpq.py uses ReconstructedFlowline --kind class
python scripts/gpq.py hier ReconstructedFlowline
```

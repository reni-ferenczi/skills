# ReconstructionTree

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 356 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionTree.h` | C++ | 474 |
| `src/app-logic/ReconstructionTree.cc` | C++ | 445 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructionTree tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructionTree`](#gplatesapplogicreconstructiontree) | class | [`GPlatesUtils::ReferenceCount<ReconstructionTree>`](../utils/ReferenceCount.md) | — | 0 | A reconstruction tree represents the plate-reconstruction hierarchy of total reconstruction poles at an instant in time. |

## Members

### `GPlatesAppLogic::ReconstructionTree`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructionTree>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructionTree>` | public | — |
| `edge_list_base_hook_type` | typedef | `boost::intrusive::slist_base_hook< // Turn off safe linking (the default link mode) because it asserts if we destroy // an edge before removing it from a list (eg, a child list of ...` | public | Some setup needed for an intrusive list of edges. |
| `edge_list_type` | typedef | `boost::intrusive::slist<Edge, boost::intrusive::base_hook<edge_list_base_hook_type> >` | public | Typedef for a list of edges. |
| `Edge` | class | `None` | public | Represents the relative rotation from a fixed plate to a moving plate. |
| `edge_map_type` | typedef | `std::map<GPlatesModel::integer_plate_id_type, const Edge *>` | public | Typedef for mapping moving plate IDs to Edge objects. |
| `create( ReconstructionGraph::non_null_ptr_to_const_type reconstruction_graph, const double &reconstruction_time, GPlatesModel::integer_plate_id_type anchor_plate_id)` | method | `non_null_ptr_type` | public | Create a new ReconstructionTree instance from the ReconstructionGraph instance graph, building a tree-structure which has anchor\_plate\_id as the anchor plate. |
| `created_from_same_graph_with_same_parameters( const ReconstructionTree &other)` | method | `bool` | public | Returns true if the other reconstruction tree is equivalent to 'this', in that it was created from the same ReconstructionGraph using the same reconstruction time and anchor plate. |
| `get_reconstruction_graph()` | method | `ReconstructionGraph::non_null_ptr_to_const_type` | public | Return the ReconstructionGraph that this reconstruction tree was created from. |
| `get_anchor_plate_id()` | method | `GPlatesModel::integer_plate_id_type` | public | Returns the plate id of the anchor plate that all rotations are calculated relative to. |
| `get_reconstruction_time()` | method | `double` | public | Return the reconstruction time of this tree. |
| `get_edge( GPlatesModel::integer_plate_id_type moving_plate_id)` | method | `boost::optional<const Edge &>` | public | Return the Edge associated with the specified moving plate ID (or none if this tree does not contain the moving plate ID). |
| `get_composed_absolute_rotation_or_none( GPlatesModel::integer_plate_id_type moving_plate_id)` | method | `boost::optional<GPlatesMaths::FiniteRotation>` | public | Get the composed absolute rotation which describes the motion of @a moving\_plate\_id relative to the anchor plate ID. |
| `get_composed_absolute_rotation( GPlatesModel::integer_plate_id_type moving_plate_id)` | method | `GPlatesMaths::FiniteRotation` | public | Get the composed absolute rotation which describes the motion of @a moving\_plate\_id relative to the anchor plate ID. |
| `d_reconstruction_graph` | field | `ReconstructionGraph::non_null_ptr_to_const_type` | private | We maintain a shared reference to the graph since we reference its graph nodes and edges (because we build the absolute rotations at each plate ID as needed, as an optimisation). |
| `d_reconstruction_time_instant` | field | `GPlatesPropertyValues::GeoTimeInstant` | private | This is the reconstruction time of the total reconstruction poles in this tree. |
| `d_anchor_plate_id` | field | `GPlatesModel::integer_plate_id_type` | private | The anchor (root-most) plate of this reconstruction tree. |
| `d_edge_pool` | field | `boost::object_pool<Edge>` | private | Storage for the edges. |
| `d_anchor_plate_edges` | field | `edge_list_type` | private | Edges whose fixed plate ID equals the anchor plate ID. |
| `d_all_edges` | field | `edge_map_type` | private | This is a mapping of moving plate IDs to edges. |
| `ReconstructionTree( ReconstructionGraph::non_null_ptr_to_const_type reconstruction_graph, const GPlatesPropertyValues::GeoTimeInstant &reconstruction_time_instant, GPlatesModel::integer_plate_id_type anchor_plate_id)` | constructor | `None` | private | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `create_sub_trees_from_graph_plate( const ReconstructionGraph::Plate &graph_plate, Edge *parent_tree_edge, edge_list_type &tree_edges)` | method | `void` | private | Create zero, one or more sub-trees emanating from a plate. |
| `create_sub_tree_from_graph_edge( const ReconstructionGraph::Edge &graph_edge, Edge *parent_tree_edge, edge_list_type &tree_edges, bool reverse_tree_edge)` | method | `bool` | private | Create a sub-tree by following the specified graph edge in the forward direction (or reverse direction if reverse\_tree\_edge is true). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTIONTREE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructionTree tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/TotalReconstructionPolesDialog](../qt-widgets/TotalReconstructionPolesDialog.md) | qt-widgets | 36 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 25 |
| [gui/ExportStageRotationAnimationStrategy](../gui/ExportStageRotationAnimationStrategy.md) | gui | 22 |
| [app-logic/RotationUtils](RotationUtils.md) | app-logic | 19 |
| [app-logic/ReconstructionTreeCreator](ReconstructionTreeCreator.md) | app-logic | 16 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 16 |
| [cli/CliStageRotationCommand](../cli/CliStageRotationCommand.md) | cli | 15 |
| [app-logic/ReconstructedFeatureGeometry](ReconstructedFeatureGeometry.md) | app-logic | 14 |
| [app-logic/FlowlineUtils](FlowlineUtils.md) | app-logic | 13 |
| [app-logic/FlowlineGeometryPopulator](FlowlineGeometryPopulator.md) | app-logic | 11 |
| [qt-widgets/MovePoleWidget](../qt-widgets/MovePoleWidget.md) | qt-widgets | 11 |
| [app-logic/MotionPathGeometryPopulator](MotionPathGeometryPopulator.md) | app-logic | 10 |
| [gui/ExportTotalRotationAnimationStrategy](../gui/ExportTotalRotationAnimationStrategy.md) | gui | 9 |
| [app-logic/ReconstructionLayerProxy](ReconstructionLayerProxy.md) | app-logic | 8 |
| [app-logic/PlateVelocityUtils](PlateVelocityUtils.md) | app-logic | 7 |
| [cli/CliEquivalentTotalRotation](../cli/CliEquivalentTotalRotation.md) | cli | 7 |
| [qt-widgets/KinematicGraphsDialog](../qt-widgets/KinematicGraphsDialog.md) | qt-widgets | 7 |
| [app-logic/ReconstructMethodVirtualGeomagneticPole](ReconstructMethodVirtualGeomagneticPole.md) | app-logic | 6 |
| [app-logic/ResolvedTriangulationNetwork](ResolvedTriangulationNetwork.md) | app-logic | 6 |
| [cli/CliRelativeTotalRotation](../cli/CliRelativeTotalRotation.md) | cli | 6 |

*... and 58 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructionTree.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructionTree --body
python scripts/gpq.py uses ReconstructionTree --kind class
python scripts/gpq.py hier ReconstructionTree
```

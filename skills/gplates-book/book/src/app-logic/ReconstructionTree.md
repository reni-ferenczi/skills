# ReconstructionTree

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 356 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionTree.h` | C++ | 474 |
| `src/app-logic/ReconstructionTree.cc` | C++ | 445 |

## Overview

A `ReconstructionTree` is one *snapshot* of the plate circuit: a `ReconstructionGraph` — the whole set of total reconstruction sequences loaded from rotation files — collapsed into a rooted, acyclic tree for a single reconstruction time and a single anchor plate. Everything downstream that needs "where was plate N at time t, relative to the anchor" ultimately asks a tree built here. The graph is not a tree: each graph edge is a *sequence* spanning a time range, and crossovers (a moving plate switching fixed plates at some time) put cycles in it. `create()` is where that cycle-bearing graph becomes a usable hierarchy.

The traversal in `create_sub_trees_from_graph_plate()` / `create_sub_tree_from_graph_edge()` starts at the graph's `Plate` for the anchor ID and walks outward. A graph edge is followed only if the tree's reconstruction time lies inside its `[get_begin_time(), get_end_time()]` range, and only if its resulting moving plate is not the anchor and has not already been claimed by another tree edge — the insertion into `d_all_edges` is both the duplicate test and the registration, which is what makes the result acyclic. Outgoing graph edges may all be followed; incoming ones (traversed *upwards*, producing a tree edge whose fixed and moving plates are swapped relative to the rotation file — `Edge::is_reversed()`) are restricted to at most one per plate, and only when the parent tree edge is itself reversed. The long comment in the `.cc` explains why: taking both branches up through a crossover would let some plates be reached by a much longer circuit than the rotation-file author intended. This matters only for a non-zero anchor plate; with anchor 0 the traversal is purely downward.

Rotations are not computed during construction. Each `Edge` holds a reference to its `ReconstructionGraph::Edge` and computes its relative rotation lazily, interpolating that graph edge's `PoleSample` list at the tree's time via `GPlatesMaths::interpolate` (reversing it with `GPlatesMaths::get_reverse` if the tree edge is reversed), then composing up the parent chain for the absolute rotation. Both results are memoised. This is the reason the tree keeps a shared reference to the graph rather than copying poles out of it, and it means building a tree over a large rotation model is cheap while the per-plate cost is paid only for the plates actually queried. `ReconstructionTreeCreator` sits directly on top of this, caching trees per reconstruction time so callers do not re-run the traversal for every feature.

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

**Lifetime.** The tree owns every `Edge` in a `boost::object_pool` and hands out bare pointers and references to them (`get_edge()`, `get_all_edges()`, `Edge::get_parent_edge()`, `Edge::get_child_edges()`). Those are valid only while the tree itself is alive; nothing else keeps them up. The intrusive edge lists deliberately use `normal_link` rather than the default `safe_link`, so edges are never unlinked from their parent's child list — the whole tree is destroyed in one go and unlinking would be wasted work. Do not try to remove or re-parent an edge. Each `Edge` also holds a raw `const ReconstructionGraph::Edge &`; that is safe only because the tree holds a counted reference to the graph for its whole life.

**Anchor plate not in the graph is not an error.** `create()` silently returns an empty tree, and an empty tree answers every query with the identity rotation. Likewise `get_composed_absolute_rotation()` returns identity for any plate the tree does not describe — use `get_composed_absolute_rotation_or_none()` if you need to tell "no rotation" apart from "no such plate". The anchor plate itself is never the moving plate of an edge, so it is special-cased to identity.

**Compare trees with `created_from_same_graph_with_same_parameters()`, never by pointer.** Tree creators cache trees and can evict them, so a logically identical tree may be a fresh instance at any time.

**Thread safety.** The lazy rotation caches are `mutable` members written from `const` methods with no synchronisation, so concurrent `get_relative_rotation()` / `get_composed_absolute_rotation()` calls on the same tree race. Treat a tree as single-threaded even through a `non_null_ptr_to_const_type`.

**Pole edge cases.** The oldest pole sample may be at the distant past and the youngest at the distant future; `calculate_graph_edge_relative_rotation()` clamps to the adjacent finite sample instead of interpolating against an infinity. The code relies on `ReconstructionGraph` guaranteeing at least two pole samples per edge and on the reconstruction time already lying within the edge's bounds — it falls through to `pole.back()` otherwise.

**Non-determinism at crossover times.** When two graph edges are equally eligible (a crossover time, or a sequence split across two rotation files), which one becomes a tree edge depends on the order of edges in the graph, hence on the order in the rotation file. The resulting rotations agree only if the crossover is properly synchronised; an unsynchronised crossover will produce a silently different answer.

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

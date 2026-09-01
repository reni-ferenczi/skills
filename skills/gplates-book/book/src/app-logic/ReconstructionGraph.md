# ReconstructionGraph

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 203 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionGraph.h` | C++ | 362 |

## Overview

This is the in-memory form of a rotation model: every total reconstruction sequence loaded from rotation features or `.rot` files, held as a graph whose nodes are plate IDs and whose edges are fixed-plate-to-moving-plate sequences, each carrying its own list of time-sampled finite rotations. Crucially it is *time-independent*. One graph covers all reconstruction times, and a `ReconstructionTree` is produced from it by choosing an anchor plate and a time and walking outward; `ReconstructionTreeCreator` then caches trees per time over a single shared graph. This is the split that makes changing the reconstruction time cheap — the rotation data is parsed and assembled once, and only the per-time tree is rebuilt.

The graph can contain cycles, and that is the reason it is a graph rather than a tree. An edge represents a whole sequence spanning a time range, so a moving plate that switches fixed plates at a crossover ends up with more than one incoming edge, and a plate can be reachable by more than one path. `ReconstructionTree::create` resolves this into an acyclic hierarchy rooted at the anchor plate by taking exactly one path through each crossover and traversing at most one edge *upwards* per plate; at a crossover time either path is available, and which one is chosen falls out of the order of the edges in the plate's list, which is the rotation file order reversed (the builder uses `push_front`). More than one edge between the same fixed/moving pair is also normal, arising when a sequence is split across files or time ranges.

Nothing outside `ReconstructionGraphBuilder` can build or modify a graph: the constructor, `create()` and all of the node internals are private with the builder as the sole friend. The builder inserts sequences one at a time, optionally extends each moving plate's oldest sequence back to the distant past so that reconstructed geometry does not snap back to present-day positions beyond the end of the rotation data, and `build_graph()` hands back a `non_null_ptr_to_const_type` and starts a fresh graph for any subsequent inserts. Storage is three `boost::object_pool` allocators — one each for plates, edges and pole samples — with the connections expressed as intrusive singly-linked lists, so building the graph costs no per-node heap allocation and the whole structure is released in one go.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructionGraph`](#gplatesapplogicreconstructiongraph) | class | [`GPlatesUtils::ReferenceCount<ReconstructionGraph>`](../utils/ReferenceCount.md) | — | 0 | A reconstruction graph represents a plate circuit rotation hierarchy. |

## Members

### `GPlatesAppLogic::ReconstructionGraph`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructionGraph>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructionGraph>` | public | — |
| `pole_sample_list_base_hook_type` | typedef | `boost::intrusive::slist_base_hook< // Turn off safe linking (the default link mode) because it asserts if we destroy // a pole sample before removing it from a list (eg, a list ins ...` | public | Some setup needed for an intrusive list of pole samples. |
| `PoleSample` | class | `None` | public | Represents the finite rotation value of a pole at a specific time instant. |
| `pole_sample_list_type` | typedef | `boost::intrusive::slist<PoleSample, boost::intrusive::base_hook<pole_sample_list_base_hook_type>, boost::intrusive::cache_last<true>/*enable push_back() and back()*/>` | public | Typedef for a list of pole samples. |
| `PlateIncomingEdgeTag` | class | `None` | public | Some setup needed for an intrusive list of plate \*incoming\* edges. |
| `plate_incoming_edge_list_base_hook_type` | typedef | `boost::intrusive::slist_base_hook< boost::intrusive::tag<PlateIncomingEdgeTag>, // Turn off safe linking (the default link mode) because it asserts if we destroy // an edge before ...` | public | — |
| `PlateOutgoingEdgeTag` | class | `None` | public | Some setup needed for an intrusive list of plate \*outgoing\* edges. |
| `plate_outgoing_edge_list_base_hook_type` | typedef | `boost::intrusive::slist_base_hook< boost::intrusive::tag<PlateOutgoingEdgeTag>, // Turn off safe linking (the default link mode) because it asserts if we destroy // an edge before ...` | public | — |
| `Edge` | class | `None` | public | Represents the relative rotation from a fixed Plate to a moving Plate. |
| `plate_incoming_edge_list_type` | typedef | `boost::intrusive::slist<Edge, boost::intrusive::base_hook<plate_incoming_edge_list_base_hook_type> >` | public | Typedef for a list of edges going \*into\* a plate (edge direction is from fixed plate to moving plate). |
| `plate_outgoing_edge_list_type` | typedef | `boost::intrusive::slist<Edge, boost::intrusive::base_hook<plate_outgoing_edge_list_base_hook_type> >` | public | Typedef for a list of edges going \*out\* of a plate (edge direction is from fixed plate to moving plate). |
| `Plate` | class | `None` | public | Represents a plate (ID). |
| `get_plate( GPlatesModel::integer_plate_id_type plate_id)` | method | `boost::optional<const Plate &>` | public | Return the Plate associated with the specified plate ID. |
| `create()` | method | `non_null_ptr_type` | private | — |
| `ReconstructionGraph()` | constructor | `None` | private | — |
| `plate_map_type` | typedef | `std::map<GPlatesModel::integer_plate_id_type, Plate *>` | private | Typedef for mapping plate IDs to Plate objects. |
| `d_pole_sample_pool` | field | `boost::object_pool<PoleSample>` | private | Storage for the pole samples, edges and plates. |
| `d_edge_pool` | field | `boost::object_pool<Edge>` | private | — |
| `d_plate_pool` | field | `boost::object_pool<Plate>` | private | — |
| `d_plate_map` | field | `plate_map_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTIONGRAPH_H` | macro | `None` | — |

## Notes

**Everything the graph exposes is a reference into its object pools.** `get_plate` returns `boost::optional<const Plate &>`, and `Plate`, `Edge` and `PoleSample` are linked by raw pointers into the pools. None of them may outlive the `ReconstructionGraph` that owns them, and none of them is reference-counted individually — hold the graph's `non_null_ptr_to_const_type` for as long as you hold anything reached from it.

**Graph identity is load-bearing.** `ReconstructionTree::created_from_same_graph_with_same_parameters` compares graph pointers, precisely because tree caches can evict and recreate an equivalent tree. Rebuilding a graph from unchanged rotation data therefore makes every previously created tree compare unequal to the new ones. Reuse the graph rather than rebuilding it.

**`get_begin_time` and `get_end_time` read against list order, not with it.** Pole samples are stored youngest to oldest, matching the rotation file; so the *begin* time is `back()` (the oldest sample) and the *end* time is `front()` (the youngest). Both dereference unconditionally, which is safe only because `ReconstructionGraphBuilder::insert_total_reconstruction_sequence` discards any sequence with fewer than two samples — every edge in a finished graph has at least two.

**Traversal must not assume one edge.** A plate may have several incoming edges (crossovers) and several edges to the same neighbour (a sequence split across files). Code that walks the graph has to handle both, and has to pick among them by the reconstruction time falling inside an edge's range.

**The intrusive lists use `normal_link`, not the default `safe_link`.** Destroying a linked element does not assert, which the header comments justify on the grounds that the graph is always destroyed wholesale — and they recommend switching back to `safe_link` while debugging a lifetime problem here.

**Immutable after `build_graph`.** The builder detaches the finished graph and allocates a new one, so a returned graph is never mutated again; combined with the atomic reference count in `GPlatesUtils::ReferenceCount`, that makes a built graph safe to share. There is no way to remove or edit a plate, edge or sample — a change to the rotation data means building a whole new graph.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructionGraphBuilder](ReconstructionGraphBuilder.md) | app-logic | 79 |
| [app-logic/ReconstructionTree](ReconstructionTree.md) | app-logic | 69 |
| [qt-widgets/MovePoleWidget](../qt-widgets/MovePoleWidget.md) | qt-widgets | 26 |
| [app-logic/FlowlineUtils](FlowlineUtils.md) | app-logic | 25 |
| [app-logic/ReconstructionTreeCreator](ReconstructionTreeCreator.md) | app-logic | 22 |
| [feature-visitors/TotalReconstructionSequenceRotationInserter](../feature-visitors/TotalReconstructionSequenceRotationInserter.md) | feature-visitors | 8 |
| [cli/CliEquivalentTotalRotation](../cli/CliEquivalentTotalRotation.md) | cli | 7 |
| [cli/CliStageRotationCommand](../cli/CliStageRotationCommand.md) | cli | 7 |
| [qt-widgets/deprecated/CreateTopologyWidget](../qt-widgets/deprecated/CreateTopologyWidget.md) | qt-widgets | 7 |
| [app-logic/deprecated/PaleomagUtils](deprecated/PaleomagUtils.md) | app-logic | 5 |
| [cli/CliRelativeTotalRotation](../cli/CliRelativeTotalRotation.md) | cli | 5 |
| [qt-widgets/ApplyReconstructionPoleAdjustmentDialog](../qt-widgets/ApplyReconstructionPoleAdjustmentDialog.md) | qt-widgets | 5 |
| [app-logic/RotationUtils](RotationUtils.md) | app-logic | 4 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 3 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 3 |
| [qt-widgets/TotalReconstructionPolesDialog](../qt-widgets/TotalReconstructionPolesDialog.md) | qt-widgets | 3 |
| [app-logic/ReconstructContext](ReconstructContext.md) | app-logic | 2 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 2 |
| [gui/ExportStageRotationAnimationStrategy](../gui/ExportStageRotationAnimationStrategy.md) | gui | 1 |
| [qt-widgets/InsertVGPReconstructionPoleDialog](../qt-widgets/InsertVGPReconstructionPoleDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructionGraph.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructionGraph --body
python scripts/gpq.py uses ReconstructionGraph --kind class
python scripts/gpq.py hier ReconstructionGraph
```

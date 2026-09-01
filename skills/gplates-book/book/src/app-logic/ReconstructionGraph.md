# ReconstructionGraph

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 203 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionGraph.h` | C++ | 362 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructionGraph tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=app-logic/ReconstructionGraph tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

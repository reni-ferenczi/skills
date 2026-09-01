# ReconstructionGraphBuilder

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 743 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionGraphBuilder.h` | C++ | 117 |
| `src/app-logic/ReconstructionGraphBuilder.cc` | C++ | 253 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructionGraphBuilder tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructionGraphBuilder`](#gplatesapplogicreconstructiongraphbuilder) | class | `boost::noncopyable` | — | 0 | Build a reconstruction graph by first inserting total reconstruction sequences and then building the graph. |

## Members

### `GPlatesAppLogic::ReconstructionGraphBuilder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `total_reconstruction_pole_time_sample_type` | typedef | `std::pair< GPlatesPropertyValues::GeoTimeInstant, GPlatesMaths::FiniteRotation>` | public | Typedef for the value of a total reconstruction pole at a particular time instant. |
| `total_reconstruction_pole_type` | typedef | `std::vector<total_reconstruction_pole_time_sample_type>` | public | Typedef for the value of a time-dependent total reconstruction pole (a sequence of time samples). |
| `ReconstructionGraphBuilder( bool extend_total_reconstruction_poles_to_distant_past_ = false)` | constructor | `None` | public | Create a ReconstructionGraphBuilder in order to build a ReconstructionGraph in order to create a ReconstructionTree at any reconstruction time. |
| `insert_total_reconstruction_sequence( GPlatesModel::integer_plate_id_type fixed_plate_id, GPlatesModel::integer_plate_id_type moving_plate_id, const total_reconstruction_pole_type &pole)` | method | `void` | public | Insert a total reconstruction sequence for the specified fixed/moving plate pair. |
| `build_graph()` | method | `ReconstructionGraph::non_null_ptr_to_const_type` | public | Return the graph created from previous calls to insert\_total\_reconstruction\_sequence. |
| `d_reconstruction_graph` | field | `ReconstructionGraph::non_null_ptr_type` | private | — |
| `d_extend_total_reconstruction_poles_to_distant_past` | field | `bool` | private | — |
| `extend_total_reconstruction_poles_to_distant_past()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTIONGRAPHBUILDER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructionGraphBuilder tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructionGraphPopulator](ReconstructionGraphPopulator.md) | app-logic | 16 |
| [app-logic/ReconstructionTreeCreator](ReconstructionTreeCreator.md) | app-logic | 3 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructionGraphBuilder.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructionGraphBuilder --body
python scripts/gpq.py uses ReconstructionGraphBuilder --kind class
python scripts/gpq.py hier ReconstructionGraphBuilder
```

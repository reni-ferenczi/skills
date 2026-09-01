# ReconstructionGraphBuilder

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 743 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionGraphBuilder.h` | C++ | 117 |
| `src/app-logic/ReconstructionGraphBuilder.cc` | C++ | 253 |

## Overview

`ReconstructionGraphBuilder` is the incremental constructor for a `ReconstructionGraph`: callers feed it one fixed/moving plate pair and its time-dependent pole at a time via `insert_total_reconstruction_sequence`, and `build_graph()` hands back the finished, immutable graph. A sequence with fewer than two enabled pole time samples is silently dropped, since a single sample cannot define a pole valid away from present day. More than one edge can exist between the same fixed and moving plate — this is how a rotation sequence split across files (for example 0-250Ma in one file, 250-410Ma in another) is represented — and the builder does not attempt to order or merge them.

The optional `extend_total_reconstruction_poles_to_distant_past` constructor argument addresses a specific artefact: without it, a moving plate's rotation is undefined before the oldest time sample of its oldest incoming edge, which causes reconstructed geometries to snap back to their present-day position once the reconstruction time exceeds that edge's range. When enabled, `build_graph()` calls `extend_total_reconstruction_poles_to_distant_past()`, which finds each plate's oldest incoming edge and, unless it already reaches the distant past, adds a further edge from that edge's oldest pole sample out to `GeoTimeInstant::create_distant_past()` holding the same finite rotation — effectively freezing the plate's motion beyond the data's actual time range instead of letting it collapse.

Calling `build_graph()` also resets the builder's internal graph to a fresh, empty one, so a single `ReconstructionGraphBuilder` can be reused to build a second, independent graph from a new set of inserted sequences without the two graphs interfering.

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

- Edge, plate and pole-sample objects are allocated from `ReconstructionGraph`'s own object pools; a pool allocation failure is reported by throwing `std::bad_alloc` rather than by any richer error path.
- The order in which edges are attached to a plate's incoming/outgoing lists is not currently significant to how a `ReconstructionTree` is later generated, including at crossovers — see the comment in `insert_total_reconstruction_sequence` for what would have to change (both forward and reverse graph propagation) if that ever became necessary.

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

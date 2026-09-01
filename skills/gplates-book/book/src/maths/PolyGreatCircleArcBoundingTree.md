# PolyGreatCircleArcBoundingTree

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 248 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/PolyGreatCircleArcBoundingTree.h` | C++ | 743 |

## Overview

`PolyGreatCircleArcBoundingTree` is a header-only, iterator-based binary bounding-small-circle tree over a linear sequence of `GreatCircleArc`s, shared by `PolylineOnSphere` and `PolygonOnSphere` to speed up queries such as intersection and distance testing (`GeometryIntersect`, `GeometryDistance`). It is templated on the arc iterator type so it can be built directly over a polyline's or polygon's own const-iterator range without copying arcs; `RequireRandomAccessIterator` defaults to true and is enforced with a `BOOST_STATIC_ASSERT`, since the tree relies on `std::advance` being cheap.

The tree is built by recursively bisecting the arc range in half at `create_node`, bottoming out into leaf nodes once a subrange falls at or below `max_num_node_great_circle_arcs_per_leaf_node`, with each node's `BoundingSmallCircle` computed from its arcs' centroid. Polygons pass `partition_separators` so that the exterior ring and each interior ring — which are spatially disconnected — get their own sub-tree; `initialise_partitions` then merges these sub-trees pairwise, repeatedly combining the two adjacent partitions with the fewest arcs so the smaller partitions end up deeper in the final tree, until one root remains. A caller walks the tree by fetching `get_root_node()` and descending through `get_child_node()`, checking `Node::is_leaf_node()`/`is_internal_node()`, and consulting `Node::get_bounding_small_circle()` to prune whole subtrees of arcs from consideration.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::PolyGreatCircleArcBoundingTree`](#gplatesmathspolygreatcirclearcboundingtree) | class | `boost::noncopyable` | `< typename GreatCircleArcConstIteratorType, bool RequireRandomAccessIterator = true>` | 0 | — |

## Members

### `GPlatesMaths::PolyGreatCircleArcBoundingTree`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NodeImpl` | struct | `None` | private | A binary tree node containing implementation details not needed by the client. |
| `node_impl_seq_type` | typedef | `std::vector<NodeImpl>` | private | — |
| `great_circle_arc_const_iterator_type` | typedef | `GreatCircleArcConstIteratorType` | public | — |
| `DEFAULT_MAX_NUM_NODE_GREAT_CIRCLE_ARCS_PER_LEAF_NODE` | field | `unsigned int` | public | The default value for the maximum number of great circles arcs to bound at leaf nodes. |
| `Node` | class | `None` | public | A node of the binary bounding tree. |
| `node_type` | typedef | `Node` | public | Typedef for bounding tree node. |
| `partition_separator_type` | typedef | `GreatCircleArcConstIteratorType` | public | Typedef for a separator between partitions sub-ranges great circle arcs. |
| `partition_separator_seq_type` | typedef | `std::vector<partition_separator_type>` | public | Typedef for sequence of partition separators. |
| `PolyGreatCircleArcBoundingTree( GreatCircleArcConstIteratorType begin_great_circle_arcs, GreatCircleArcConstIteratorType end_great_circle_arcs, boost::optional<const partition_separator_seq_type &> partition_separators = boost::none, boost::optional<GeometryOnSphere::non_null_ptr_to_const_type> shared_reference_to_geom ...` | constructor | `None` | public | Constructs a binary bounding tree over the specified iteration sequence of great circle arcs. |
| `get_root_node()` | method | `node_type` | public | Returns the root node of the binary bounding tree. |
| `get_child_node( const node_type &parent_node, unsigned int child_offset)` | method | `node_type` | public | Returns the specified child node of the specified parent node. |
| `SortPartitionsByNumBoundedArcs` | class | `None` | private | Used to sort partitions by their number of bounded arcs. |
| `INVALID_NODE_INDEX` | field | `int` | private | Index used to test if a node has children or not. |
| `d_nodes` | field | `node_impl_seq_type` | private | — |
| `d_root_node_index` | field | `unsigned int` | private | — |
| `d_begin_great_circle_arcs` | field | `great_circle_arc_const_iterator_type` | private | — |
| `d_geometry_shared_pointer` | field | `boost::optional<GeometryOnSphere::non_null_ptr_to_const_type>` | private | A reference to ensure the owner of the great circle arcs stays alive because we are storing iterators into its internal structures. |
| `initialise( GreatCircleArcConstIteratorType begin_great_circle_arcs, GreatCircleArcConstIteratorType end_great_circle_arcs, boost::optional<const partition_separator_seq_type &> partition_separators, unsigned int max_num_node_great_circle_arcs_per_leaf_node)` | method | `void` | private | — |
| `initialise_partitions( GreatCircleArcConstIteratorType begin_great_circle_arcs, GreatCircleArcConstIteratorType end_great_circle_arcs, const partition_separator_seq_type &partition_separators, unsigned int max_num_node_great_circle_arcs_per_leaf_node)` | method | `void` | private | — |
| `create_node( unsigned int begin_node_great_circle_arcs_index, unsigned int num_node_great_circle_arcs, unsigned int max_num_node_great_circle_arcs_per_leaf_node)` | method | `unsigned int` | private | — |
| `add_internal_node( unsigned int first_child_node_index, unsigned int second_child_node_index)` | method | `unsigned int` | private | — |
| `add_leaf_node( unsigned int begin_node_great_circle_arcs_index, unsigned int num_node_great_circle_arcs)` | method | `unsigned int` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_POLYGREATCIRCLEARCBOUNDINGTREE_H` | macro | `None` | — |

## Notes

- The constructor throws `GPlatesGlobal::PreconditionViolationError` if the arc range is empty, if `max_num_node_great_circle_arcs_per_leaf_node` is zero, or if `partition_separators` is given but is empty, out of order, or produces an empty partition.
- `d_geometry_shared_pointer` is `boost::none` by default and is only set when the caller explicitly passes `shared_reference_to_geometry`; `PolylineOnSphere`/`PolygonOnSphere` deliberately leave it unset when they build a tree over their own arcs, since they already hold the tree and setting it would create a reference cycle (and a leak). Any other caller that keeps the tree past the lifetime of its source arcs must either pass this reference or otherwise guarantee the arcs stay alive.
- Merging across partitions is not spatially optimal — disconnected rings can end up adjacent in the tree even if they are far apart on the sphere — but is cheap and works well in practice because arcs within a partition retain spatial locality.

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/GeometryDistance](GeometryDistance.md) | maths | 70 |
| [maths/GeometryIntersect](GeometryIntersect.md) | maths | 29 |
| [maths/PolygonOnSphere](PolygonOnSphere.md) | maths | 3 |
| [maths/PolylineOnSphere](PolylineOnSphere.md) | maths | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/PolyGreatCircleArcBoundingTree.h
python scripts/gpq.py def GPlatesMaths::PolyGreatCircleArcBoundingTree --body
python scripts/gpq.py uses PolyGreatCircleArcBoundingTree --kind class
python scripts/gpq.py hier PolyGreatCircleArcBoundingTree
```

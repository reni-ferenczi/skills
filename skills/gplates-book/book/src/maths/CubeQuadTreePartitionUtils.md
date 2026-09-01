# CubeQuadTreePartitionUtils

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 658 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/CubeQuadTreePartitionUtils.h` | C++ | 949 |

## Overview

[[[PROSE overview unit=maths/CubeQuadTreePartitionUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::CubeQuadTreePartitionUtils::CubeQuadTreePartitionIntersectingNodes`](#gplatesmathscubequadtreepartitionutilscubequadtreepartitionintersectingnodes) | class | — | `<typename ElementType, class CubeQuadTreePartitionType = const CubeQuadTreePartition<ElementType> >` | 1 | A utility class to use during traversal of a spatial partition to determine those 'loose' nodes of another spatial partition that intersect it. |
| [`GPlatesMaths::CubeQuadTreePartitionUtils::CubeQuadTreeIntersectingNodes`](#gplatesmathscubequadtreepartitionutilscubequadtreeintersectingnodes) | class | [`CubeQuadTreePartitionIntersectingNodes<ElementType, CubeQuadTreePartitionType>`](CubeQuadTreePartitionUtils.md) | `<typename ElementType, class CubeQuadTreePartitionType = const CubeQuadTreePartition<ElementType> >` | 0 | A utility class to use during traversal of a regular cube quad tree (not a spatial partition, eg, a multi-resolution raster) to determine those 'loose' nodes of a spatial partition that intersect it. |
| [`GPlatesMaths::CubeQuadTreePartitionUtils::Implementation::element_iterator`](#gplatesmathscubequadtreepartitionutilsimplementationelement_iterator) | alias | — | `<typename ElementType>` | 0 | — |
| [`GPlatesMaths::CubeQuadTreePartitionUtils::Implementation::element_range_type`](#gplatesmathscubequadtreepartitionutilsimplementationelement_range_type) | alias | — | `<typename ElementType>` | 0 | — |
| [`GPlatesMaths::CubeQuadTreePartitionUtils::Implementation::node_reference_type`](#gplatesmathscubequadtreepartitionutilsimplementationnode_reference_type) | alias | — | `<typename ElementType>` | 0 | — |
| [`GPlatesMaths::CubeQuadTreePartitionUtils::Implementation::neighbour_nodes_type`](#gplatesmathscubequadtreepartitionutilsimplementationneighbour_nodes_type) | alias | — | `<typename ElementType>` | 0 | — |
| [`GPlatesMaths::CubeQuadTreePartitionUtils::Implementation::ElementRangeListNode`](#gplatesmathscubequadtreepartitionutilsimplementationelementrangelistnode) | struct | [`GPlatesUtils::IntrusiveSinglyLinkedList<ElementRangeListNode<ElementType>>::Node`](CubeQuadTree.md) | `<typename ElementType>` | 0 | A linked list node that references a list of elements (either the root elements or elements in a node). |
| [`GPlatesMaths::CubeQuadTreePartitionUtils::Implementation::element_range_list_type`](#gplatesmathscubequadtreepartitionutilsimplementationelement_range_list_type) | alias | — | `<typename ElementType>` | 0 | We use our own intrusive singly linked list (instead of boost::slist) since it supports tail-sharing (where multiple lists can share their tail ends). |
| [`GPlatesMaths::CubeQuadTreePartitionUtils::Implementation::element_range_list_const_iterator_type`](#gplatesmathscubequadtreepartitionutilsimplementationelement_range_list_const_iterator_type) | alias | — | `<typename ElementType>` | 0 | — |

## Members

### `GPlatesMaths::CubeQuadTreePartitionUtils::CubeQuadTreePartitionIntersectingNodes`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `cube_quad_tree_partition_type` | typedef | `CubeQuadTreePartitionType` | public | Typedef for the spatial partition we are traversing. |
| `cube_quad_tree_partition_node_reference_type` | typedef | `typename boost::mpl::if_< boost::is_const<CubeQuadTreePartitionType>, typename cube_quad_tree_partition_type::const_node_reference_type, typename cube_quad_tree_partition_type::nod ...` | public | Typedef for the node reference type. |
| `IntersectingNodesType` | class | `None` | public | Contains node references of intersecting nodes of the spatial partition. |
| `intersecting_nodes_type` | typedef | `IntersectingNodesType<9>` | public | Typedef for a sequence of intersecting nodes at the current traversal depth. |
| `CubeQuadTreePartitionIntersectingNodes( cube_quad_tree_partition_type &spatial_partition, CubeCoordinateFrame::CubeFaceType cube_face)` | constructor | `None` | public | Constructor for the root node of a spatial partition (ie, of a face of the cube). spatial\_partition is the spatial partition that we track intersections with as the client traverses another another spatial partition - the client traverses ... |
| `CubeQuadTreePartitionIntersectingNodes( const CubeQuadTreePartitionIntersectingNodes &parent, unsigned int child_x_offset, unsigned int child_y_offset)` | constructor | `None` | public | Constructor for a child node of the specified parent quad tree node. |
| `d_node_location` | field | `CubeQuadTreeLocation` | protected | — |
| `d_intersecting_nodes` | field | `intersecting_nodes_type` | protected | — |
| `CubeQuadTreePartitionIntersectingNodes( const CubeQuadTreeLocation &node_location)` | constructor | `None` | protected | Constructor for derived class. |
| `find_intersecting_nodes( const IntersectingNodesType<max_num_parent_nodes> &parent_intersecting_nodes)` | method | `void` | protected | Find those child nodes of the parent intersecting nodes that intersect 'this' child. |

### `GPlatesMaths::CubeQuadTreePartitionUtils::CubeQuadTreeIntersectingNodes`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `cube_quad_tree_partition_type` | typedef | `typename CubeQuadTreePartitionIntersectingNodes<ElementType, CubeQuadTreePartitionType> ::cube_quad_tree_partition_type` | public | Typedef for the cube quad tree partition. |
| `cube_quad_tree_partition_node_reference_type` | typedef | `typename CubeQuadTreePartitionIntersectingNodes<ElementType, CubeQuadTreePartitionType> ::cube_quad_tree_partition_node_reference_type` | public | Typedef for the node reference type. |
| `parent_intersecting_nodes_type` | typedef | `typename CubeQuadTreePartitionIntersectingNodes<ElementType, CubeQuadTreePartitionType> ::template IntersectingNodesType<4>` | public | Typedef for a sequence of intersecting nodes at the parent traversal depth. |
| `CubeQuadTreeIntersectingNodes( cube_quad_tree_partition_type &spatial_partition, CubeCoordinateFrame::CubeFaceType cube_face)` | constructor | `None` | public | Constructor for the root node of a cube quad tree (ie, of a face of the cube). spatial\_partition is the spatial partition that we track intersections with as the client traverses a cube quad tree - the client traverses by instantiating ... |
| `CubeQuadTreeIntersectingNodes( const CubeQuadTreeIntersectingNodes &parent, unsigned int child_x_offset, unsigned int child_y_offset)` | constructor | `None` | public | Constructor for a child node of the specified parent quad tree node. |
| `d_parent_intersecting_nodes` | field | `parent_intersecting_nodes_type` | private | — |

### `GPlatesMaths::CubeQuadTreePartitionUtils::Implementation::element_iterator`

*None.*

### `GPlatesMaths::CubeQuadTreePartitionUtils::Implementation::element_range_type`

*None.*

### `GPlatesMaths::CubeQuadTreePartitionUtils::Implementation::node_reference_type`

*None.*

### `GPlatesMaths::CubeQuadTreePartitionUtils::Implementation::neighbour_nodes_type`

*None.*

### `GPlatesMaths::CubeQuadTreePartitionUtils::Implementation::ElementRangeListNode`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ElementRangeListNode( const element_range_type<ElementType> &element_range_)` | constructor | `None` | public | — |
| `ElementRangeListNode( const element_iterator<ElementType> &element_range_begin_, const element_iterator<ElementType> &element_range_end_)` | constructor | `None` | public | — |
| `element_range` | field | `element_range_type<ElementType>` | public | — |

### `GPlatesMaths::CubeQuadTreePartitionUtils::Implementation::element_range_list_type`

*None.*

### `GPlatesMaths::CubeQuadTreePartitionUtils::Implementation::element_range_list_const_iterator_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_CUBEQUADTREEPARTITIONUTILS_H` | macro | `None` | — |
| `merge_root_element( CubeQuadTreePartition<ElementType> &dst_spatial_partition, const ElementType &src_root_element)` | function | `void` | — |
| `merge_node_element( CubeQuadTreePartition<ElementType> &dst_spatial_partition, typename CubeQuadTreePartition<ElementType>::node_reference_type dst_node, const ElementType &src_element)` | function | `void` | — |
| `merge( CubeQuadTreePartition<ElementType> &dst_spatial_partition, const CubeQuadTreePartition<ElementType> &src_spatial_partition)` | function | `void` | — |
| `mirror_quad_tree( CubeQuadTreePartition<DstElementType> &dst_spatial_partition, const CubeQuadTreePartition<SrcElementType> &src_spatial_partition, typename CubeQuadTreePartition<DstElementType>::node_reference_type dst_node, typename CubeQuadTreePartition<SrcElementType>::const_node_reference_type src_node, const Mirr ...` | function | `void` | — |
| `mirror( CubeQuadTreePartition<DstElementType> &dst_spatial_partition, const CubeQuadTreePartition<SrcElementType> &src_spatial_partition, const MirrorRootElementFunctionType &mirror_root_element_function, const MirrorNodeElementFunctionType &mirror_node_element_function)` | function | `void` | — |
| `visit_potentially_intersecting_element_range( const element_range_type<ElementType> &element_range, const element_range_list_type<ElementType> &neighbour_element_range_list, const element_range_list_const_iterator_type<ElementType> &sibling_ancestor_neighbour_boundary_element_range_iterator, const VisitElementPairFunct ...` | function | `void` | — |
| `visit_potentially_intersecting_elements_quad_tree( CubeQuadTreePartition<ElementType> &spatial_partition, const element_range_list_type<ElementType> &ancestor_neighbour_element_range_list, const node_reference_type<ElementType> &node_reference, const neighbour_nodes_type<ElementType> &sibling_neighbour_nodes, const Vis ...` | function | `void` | — |
| `visit_potentially_intersecting_elements( CubeQuadTreePartition<ElementType> &spatial_partition, const VisitElementPairFunctionType &visit_element_pair_function)` | function | `void` | — |

## Notes

[[[PROSE notes unit=maths/CubeQuadTreePartitionUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 13 |
| [opengl/GLFilledPolygonsGlobeView](../opengl/GLFilledPolygonsGlobeView.md) | opengl | 11 |
| [app-logic/ReconstructLayerProxy](../app-logic/ReconstructLayerProxy.md) | app-logic | 3 |
| [view-operations/RenderedGeometryLayer](../view-operations/RenderedGeometryLayer.md) | view-operations | 3 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](../opengl/GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 1 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/CubeQuadTreePartitionUtils.h
python scripts/gpq.py def GPlatesMaths::CubeQuadTreePartitionUtils::CubeQuadTreePartitionIntersectingNodes --body
python scripts/gpq.py uses CubeQuadTreePartitionIntersectingNodes --kind class
python scripts/gpq.py hier CubeQuadTreePartitionIntersectingNodes
```

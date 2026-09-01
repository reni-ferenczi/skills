# CubeQuadTree

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1128 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/CubeQuadTree.h` | C++ | 901 |

## Overview

[[[PROSE overview unit=maths/CubeQuadTree tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::CubeQuadTree`](#gplatesmathscubequadtree) | class | [`GPlatesUtils::ReferenceCount< CubeQuadTree<ElementType> >`](../utils/ReferenceCount.md) | `<typename ElementType>` | 0 | Boilerplate code for creating and traversing a cube quad tree - a cube with each face containing a quad tree. |

## Members

### `GPlatesMaths::CubeQuadTree`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `element_type` | typedef | `ElementType` | public | Typedef for the element type. |
| `this_type` | typedef | `CubeQuadTree<ElementType>` | public | Typedef for this class type. |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<this_type>` | public | A convenience typedef for a shared pointer to a non-const CubeQuadTree. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const this_type>` | public | A convenience typedef for a shared pointer to a const CubeQuadTree. |
| `create()` | method | `non_null_ptr_type` | public | Creates a CubeQuadTree object. |
| `Node` | class | `None` | public | A node in a quad tree. |
| `node_type` | typedef | `Node` | public | Typedef for the quad tree node type. |
| `location_type` | typedef | `CubeQuadTreeLocation` | public | Typedef for a location in the cube quad tree. |
| `Iterator` | class | `None` | public | Iterator over the cube quad tree. 'ElementQualifiedType' can be either 'element\_type' or 'const element\_type'. |
| `iterator` | typedef | `Iterator<element_type>` | public | Typedef for iterator. |
| `const_iterator` | typedef | `Iterator<const element_type>` | public | Typedef for const iterator. |
| `get_iterator()` | method | `iterator` | public | Returns a non-const iterator over the elements of this cube quad tree. |
| `get_root_element()` | method | `ElementType` | public | Returns the root element if it exists, otherwise NULL. |
| `get_or_create_root_element` | field | `ElementType` | public | Gets the root element. |
| `set_root_element( const ElementType &root_element)` | method | `void` | public | Sets the root element. |
| `empty()` | method | `bool` | public | Returns true if there are any elements currently in this cube quad tree (including the root element). |
| `size()` | method | `unsigned int` | public | Returns the number of elements currently in this cube quad tree (including the root element). |
| `clear()` | method | `void` | public | Clears the entire cube quad tree including the root element. |
| `get_quad_tree_root_node( CubeCoordinateFrame::CubeFaceType cube_face)` | method | `Node` | public | Returns the root quad tree node of the specified cube face if it exists, otherwise NULL. |
| `get_or_create_quad_tree_root_node` | field | `Node` | public | Gets the root node of the specified cube face (quad tree). |
| `remove_quad_tree_root_node( CubeCoordinateFrame::CubeFaceType cube_face)` | method | `void` | public | Removes the specified root node, if it exists, and recursively removes any descendants. |
| `get_or_create_child_node` | field | `Node` | public | Gets the child node of the specified parent node. |
| `remove_child_node( Node &parent_node, unsigned int child_x_offset, unsigned int child_y_offset)` | method | `void` | public | Removes the child of the specified parent node, if it exists, and recursively removes any descendants. |
| `create_node( const ElementType &element)` | method | `typename Node::ptr_type` | public | Creates a 'dangling' quad tree node containing a copy of 'element'. |
| `release_node( typename Node::ptr_type node)` | method | `void` | public | Releases a 'dangling' quad tree node - should only be used if you created node with create\_node and decided not to attach it to 'this' cube quad tree (eg, an exception was thrown after create\_node but before it could be attached). |
| `set_quad_tree_root_node( CubeCoordinateFrame::CubeFaceType cube_face, typename Node::ptr_type root_node)` | method | `void` | public | An alternative to the other overload of this method that uses create\_node. |
| `set_child_node( Node &parent_node, unsigned int child_x_offset, unsigned int child_y_offset, typename Node::ptr_type child_node)` | method | `void` | public | An alternative to the other overload of this method that uses create\_node. |
| `QuadTree` | struct | `None` | private | Each cube face has a quad tree. |
| `quad_tree_node_pool_type` | typedef | `GPlatesUtils::ObjectPool<Node>` | private | Typedef for an object pool for type Node. |
| `d_quad_tree_node_pool` | field | `quad_tree_node_pool_type` | private | All quad tree nodes, except the root nodes, are stored in this pool. |
| `d_root_element` | field | `boost::optional<ElementType>` | private | The root element of the entire cube. |
| `d_quad_trees` | field | `QuadTree` | private | A quad tree for each cube face. |
| `CubeQuadTree()` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_CUBEQUADTREE_H` | macro | `None` | — |
| `ROOT_ELEMENT_LOCATION` | variable | `typename CubeQuadTree<ElementType>::location_type` | Iterator implementation |

## Notes

[[[PROSE notes unit=maths/CubeQuadTree tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLReconstructedStaticPolygonMeshes](../opengl/GLReconstructedStaticPolygonMeshes.md) | opengl | 102 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](../opengl/GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 75 |
| [opengl/GLMultiResolutionCubeRaster](../opengl/GLMultiResolutionCubeRaster.md) | opengl | 55 |
| [opengl/GLMultiResolutionMapCubeMesh](../opengl/GLMultiResolutionMapCubeMesh.md) | opengl | 45 |
| [opengl/GLFilledPolygonsGlobeView](../opengl/GLFilledPolygonsGlobeView.md) | opengl | 40 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](../opengl/GLMultiResolutionCubeReconstructedRaster.md) | opengl | 37 |
| [view-operations/RenderedGeometryLayer](../view-operations/RenderedGeometryLayer.md) | view-operations | 33 |
| [opengl/GLMultiResolutionCubeMesh](../opengl/GLMultiResolutionCubeMesh.md) | opengl | 23 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 21 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 19 |
| [maths/CubeQuadTreePartitionUtils](CubeQuadTreePartitionUtils.md) | maths | 15 |
| [maths/CubeQuadTreePartition](CubeQuadTreePartition.md) | maths | 13 |
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 11 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 10 |
| [opengl/GLCubeSubdivisionCache](../opengl/GLCubeSubdivisionCache.md) | opengl | 6 |
| [presentation/LayerOutputRenderer](../presentation/LayerOutputRenderer.md) | presentation | 5 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 4 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 3 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 3 |
| [data-mining/DataSelector](../data-mining/DataSelector.md) | data-mining | 2 |

*... and 5 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/CubeQuadTree.h
python scripts/gpq.py def GPlatesMaths::CubeQuadTree --body
python scripts/gpq.py uses CubeQuadTree --kind class
python scripts/gpq.py hier CubeQuadTree
```

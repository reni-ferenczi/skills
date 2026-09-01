# CubeQuadTree

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1128 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/CubeQuadTree.h` | C++ | 901 |

## Overview

The generic container behind every "subdivide the globe recursively" structure in
GPlates: six quad trees, one per cube face of `CubeCoordinateFrame`, plus a
single element at the root of the cube itself, with an arbitrary `ElementType`
stored in each node. It is deliberately only structure — it knows nothing about
geometry, bounding circles or which node a point belongs in. Callers decide where
to descend and this class hands out, creates and removes nodes. That is why it is
instantiated on wildly different payloads: raster tiles
(`GLMultiResolutionCubeRaster`), per-node polygon-mesh membership
(`GLReconstructedStaticPolygonMeshes`), cached subdivision transforms held as
object-cache volatile pointers (`GLCubeSubdivisionCache`), mesh drawables
(`GLMultiResolutionCubeMesh`), and in
`GLMultiResolutionStaticPolygonReconstructedRaster` three separate trees at once
— tiles, per-render traversal state and a client-side cache handed back to the
caller. Note that the related `CubeQuadTreePartition` is a different class: it is
the *spatial* structure built on the same idea, and the code that reaches for
`CubeQuadTreePartition` or a bare `CubeQuadTreeLocation` — `GLFilledPolygonsGlobeView`,
`RenderedGeometryLayer` — is not using this template at all.

Two construction styles are offered and they are not interchangeable in feel.
The `get_or_create_*` family walks down from a face root creating
default-constructed elements as it goes, which is the natural top-down build; the
`create_node()` / `set_child_node(..., ptr_type)` family lets a caller build a
subtree in isolation and graft it on afterwards, which is what the raster and
mesh generators do when a subtree is produced by a recursive helper that returns
a node. The root element is separate from all six quad trees and exists for
things that belong to no face at all — `CubeQuadTreePartition` uses it for
geometries too large to fit inside any one face's loose bounds.

Traversal comes in two forms. Ordinary structural recursion goes through
`Node::get_child_node()`, which returns `NULL` for an absent child, so a "tree"
here is really a sparse tree — most nodes have fewer than four children.
`Iterator` is the flat alternative for when order does not matter: it holds an
explicit stack of `NodeLocation` records, visits the cube root element first and
then each face in enum order, and reports a `CubeQuadTreeLocation` alongside each
element so that the caller can still tell where in the cube it is. Storage is a
`GPlatesUtils::ObjectPool<Node>`, chosen for its O(1) individual `release()`;
the class is `ReferenceCount`-derived and handed around as
`non_null_ptr_type`.

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

**The pool owns every node; nothing else does.** `Node::ptr_type` is
`ObjectPool<Node>::object_ptr_type`, a raw pool handle with no reference counting
— removing a node from the tree and releasing it to the pool are the same act,
and the pool may hand the same storage back on the next `create_node()`. So any
`Node *` or `Node &` a caller is holding is invalidated by
`remove_child_node()`, `remove_quad_tree_root_node()`, `clear()`, and by
`set_quad_tree_root_node()` and `set_child_node()` — *both* overloads of each,
which recursively remove the existing subtree before attaching the new one. The
`ptr_type` overloads are where that removal actually happens
(CubeQuadTree.h:622-633 and 676-688); the `const ElementType &` overloads inherit
it by delegating to them after a `create_node()`. Destroying the `CubeQuadTree`
destroys the pool and hence every node, attached or not.

**`create_node()` without an attach is a leak until destruction.** The header is
explicit about this: a node created and never attached is not reclaimed until the
tree is destroyed, unless `release_node()` is called. The mirror-image mistake is
worse — calling `release_node()` on a node that *is* in the tree returns live
storage to the free list and corrupts the tree, with the parent still pointing at
it. There is no check for either case.

**Element requirements are implicit and split across methods.** The class comment
requires `ElementType` to be copy-constructible and copy-assignable. On top of
that, every `get_or_create_*` method default-constructs an element, so
instantiating the template with a type lacking a default constructor still
compiles until one of those methods is used — an easy trap when only the
`create_node()` / `set_*_node(ptr_type)` path is exercised in one translation
unit.

**`size()` and `empty()` count pool occupancy.** They are `d_quad_tree_node_pool`
plus the presence of the root element, so a node created with `create_node()` and
not yet attached is already counted. They are not a count of reachable elements.

**Indices are unchecked and the location is not validated against the tree.**
Child offsets index a `[2][2]` array directly and `cube_face` indexes a
six-element array directly; there are no assertions. Separately, the
`CubeQuadTreeLocation` an `Iterator` reports is a pure coordinate — it is not a
node reference and does not keep the node alive.

**Iterators are invalidated by any structural change.** The traversal stack holds
raw node pointers and a `std::vector` of `NodeLocation`; adding or removing nodes
during iteration leaves both stale. `reset()` restarts a used iterator, but it
does not make one safe across mutations. Nothing here is thread-safe for
concurrent mutation — the pool allocates on `add()` — though concurrent
read-only traversal with independent iterators touches no shared mutable state.

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

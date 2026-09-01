# CubeQuadTreePartition

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 270 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/CubeQuadTreePartition.h` | C++ | 2036 |

## Overview

The spatial index for geometries on the globe. Structurally it is a
`CubeQuadTree<ElementList>` — the same six-faces-of-a-cube subdivision — but each
face's quad tree is *loose*: a node's bounding square is twice the node's own
size, in the sense of Thatcher Ulrich's loose octrees. That one change is the
whole design. In a strict quad tree a small object straddling the root's
splitting line has to be stored at the root, and enough such objects destroy the
index; with doubled bounds an object is stored at the level determined by its
*size* alone, and its position only picks which node at that level. Insertion
therefore has an O(1) target depth (a log2 of the bounding radius, implemented as
a descent loop because the interior nodes have to be created anyway), which
matters because this index is rebuilt for every geometry on the globe at every
reconstruction time.

The public surface is dominated by `add()` overloads, but they are three
mechanisms wearing many hats. The primitive ones take a `UnitVector3D` point, or
a bounding small circle as centre plus `AngularExtent`. Everything else funnels
into them: the `PolylineOnSphere` / `PolygonOnSphere` / `MultiPointOnSphere`
overloads pull `get_bounding_small_circle()` off the geometry, the
`GeometryOnSphere` overloads dispatch through `ConstGeometryOnSphereVisitor`
subclasses (`AddGeometryOnSphere` and friends) to reach those, and the
region-of-interest variants simply add the extent to the bounding circle before
inserting — which is what makes a proximity query into an overlap test. The
`FiniteRotation` variants exist purely so that reconstructing a geometry does not
mean re-deriving its bounds: only the bounding circle *centre* is rotated, since
a rigid rotation cannot change the radius.

The other half of the interface is for building a partition top-down rather than
spatially: `get_or_create_quad_tree_root_node()` / `get_or_create_child_node()`
hand back a `NodeReference`, and `add(element, node_reference_type)` drops an
element straight in. `add(element, const location_type &)` does the same from a
`CubeQuadTreeLocation`. Both exist for mirroring one partition into another —
`CubeQuadTreePartitionUtils` builds derived partitions this way, and
`GLRasterCoRegistration` and `GLFilledPolygonsGlobeView` walk a partition
alongside a cube-quad-tree raster of the same shape. Elements too large to fit
inside any face's loose root bound are not rejected: they go into the cube's own
root element, reachable through `begin_root_elements()` and `end_root_elements()`,
and every traversal has to remember to look there.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::CubeQuadTreePartition`](#gplatesmathscubequadtreepartition) | class | [`GPlatesUtils::ReferenceCount< CubeQuadTreePartition<ElementType> >`](../utils/ReferenceCount.md) | `<typename ElementType>` | 0 | containing a 'loose' quad tree. |

## Members

### `GPlatesMaths::CubeQuadTreePartition`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ElementListNode` | class | `None` | private | Linked list wrapper node around an element that has been added to a quad tree node. |
| `element_list_impl_type` | typedef | `typename GPlatesUtils::IntrusiveSinglyLinkedList<ElementListNode>` | private | Typedef for the internal list of elements. |
| `ElementList` | class | `None` | private | A list of elements that belong to a single node in a quad tree. |
| `cube_quad_tree_type` | typedef | `CubeQuadTree<ElementList>` | private | Typedef for the 'loose' cube quad tree with nodes containing the type ElementList. |
| `cube_quad_tree_node_type` | typedef | `typename cube_quad_tree_type::node_type` | private | Typedef for a node of the cube quad tree. |
| `element_type` | typedef | `ElementType` | public | Typedef for the element type. |
| `this_type` | typedef | `CubeQuadTreePartition<ElementType>` | public | Typedef for this class type. |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<this_type>` | public | A convenience typedef for a shared pointer to a non-const CubeQuadTreePartition. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const this_type>` | public | A convenience typedef for a shared pointer to a const CubeQuadTreePartition. |
| `ElementIterator` | class | `None` | public | Iterator over the elements in cube quad tree node. 'ElementQualifiedType' can be either 'element\_type' or 'const element\_type'. |
| `element_const_iterator` | typedef | `ElementIterator<const element_type>` | public | Typedef for element const iterator. |
| `element_iterator` | typedef | `ElementIterator<element_type>` | public | Typedef for element non-const iterator. |
| `NodeReference` | class | `None` | public | A reference, or handle, to a node of this spatial partition. |
| `node_reference_type` | typedef | `NodeReference<cube_quad_tree_node_type>` | public | Typedef for a non-const reference to a node of this spatial partition. |
| `const_node_reference_type` | typedef | `NodeReference<const cube_quad_tree_node_type>` | public | Typedef for a const reference to a node of this spatial partition. |
| `location_type` | typedef | `CubeQuadTreeLocation` | public | Typedef for a location in the cube quad tree. |
| `Iterator` | class | `None` | public | Iterator over the spatial partition. 'ElementQualifiedType' can be either 'element\_type' or 'const element\_type'. |
| `iterator` | typedef | `Iterator<element_type>` | public | Typedef for iterator. |
| `const_iterator` | typedef | `Iterator<const element_type>` | public | Typedef for const iterator. |
| `create( unsigned int maximum_quad_tree_depth)` | method | `non_null_ptr_type` | public | Creates a CubeQuadTreePartition object. |
| `get_maximum_quad_tree_depth()` | method | `unsigned int` | public | Returns the maximum depth of this spatial partition (see create). |
| `empty()` | method | `bool` | public | Returns true if any elements have been added to this spatial partition. |
| `size()` | method | `unsigned int` | public | Returns the number of elements that have been added to this spatial partition so far. |
| `begin_root_elements()` | method | `element_const_iterator` | public | Returns the begin iterator for elements in the root of the spatial partition. |
| `end_root_elements()` | method | `element_const_iterator` | public | Returns the end iterator for elements in the root of the spatial partition. |
| `get_quad_tree_root_node( CubeCoordinateFrame::CubeFaceType cube_face)` | method | `const_node_reference_type` | public | Gets the root node of the specified cube face (quad tree), if it exists. |
| `get_child_node( const_node_reference_type parent_node, unsigned int child_x_offset, unsigned int child_y_offset)` | method | `const_node_reference_type` | public | Gets the child node of the specified parent node, if it exists. |
| `get_child_node( node_reference_type parent_node, unsigned int child_x_offset, unsigned int child_y_offset)` | method | `node_reference_type` | public | Gets the non-const child node of the specified parent node, if it exists. |
| `get_iterator()` | method | `iterator` | public | Returns a non-const iterator over the elements of this spatial partition. |
| `clear()` | method | `void` | public | Clears the entire spatial partition. |
| `add( const ElementType &element, const UnitVector3D &point_geometry, location_type *location_added = NULL)` | method | `void` | public | Add an element, to the spatial partition, that is associated with a point geometry. |
| `add( const ElementType &element, const UnitVector3D &point_geometry, const FiniteRotation &finite_rotation, location_type *location_added = NULL)` | method | `void` | public | Same as the above overload of add but location of insertion is the \*rotated\* point geometry. |
| `add( const ElementType &element, const UnitVector3D &bounding_circle_centre, const AngularExtent &bounding_circle_extent, location_type *location_added = NULL)` | method | `void` | public | Add an element, to the spatial partition, that has a finite spatial extent. |
| `add( const ElementType &element, const UnitVector3D &bounding_circle_centre, const AngularExtent &bounding_circle_extent, const FiniteRotation &finite_rotation, location_type *location_added = NULL)` | method | `void` | public | Same as the above overload of add but location of insertion is the \*rotated\* bounding circle centre. |
| `add( const ElementType &element, const GeometryOnSphere &geometry, location_type *location_added = NULL)` | method | `void` | public | Add an element, to the spatial partition, using the spatial extent of the specified GeometryOnSphere object. |
| `add( const ElementType &element, const GeometryOnSphere &geometry, const FiniteRotation &finite_rotation, location_type *location_added = NULL)` | method | `void` | public | Same as the above overload of add but location of insertion is the \*rotated\* geometry. |
| `add( const ElementType &element, const GeometryOnSphere &geometry, const AngularExtent &region_of_interest, location_type *location_added = NULL)` | method | `void` | public | Add an element, to the spatial partition, using the \*expanded\* (by region-of-interest) spatial extent of the specified GeometryOnSphere object. |
| `add( const ElementType &element, const GeometryOnSphere &geometry, const AngularExtent &region_of_interest, const FiniteRotation &finite_rotation, location_type *location_added = NULL)` | method | `void` | public | Same as the above overload of add but location of insertion is the \*rotated\* geometry. |
| `add( const ElementType &element, const PointOnSphere &point_on_sphere, location_type *location_added = NULL)` | method | `void` | public | Add an element, to the spatial partition, using the specified PointOnSphere. |
| `add( const ElementType &element, const PointOnSphere &point_on_sphere, const FiniteRotation &finite_rotation, location_type *location_added = NULL)` | method | `void` | public | Same as the above overload of add but location of insertion is the \*rotated\* point. |
| `add( const ElementType &element, const PointOnSphere &point_on_sphere, const AngularExtent &region_of_interest, location_type *location_added = NULL)` | method | `void` | public | Add an element, to the spatial partition, using the specified PointOnSphere but also using the finite bounding extent specified by region\_of\_interest (instead of a point insertion). |
| `add( const ElementType &element, const PointOnSphere &point_on_sphere, const AngularExtent &region_of_interest, const FiniteRotation &finite_rotation, location_type *location_added = NULL)` | method | `void` | public | Same as the above overload of add but location of insertion is the \*rotated\* point. |
| `add( const ElementType &element, const MultiPointOnSphere &multi_point_on_sphere, location_type *location_added = NULL)` | method | `void` | public | Add an element, to the spatial partition, using the spatial extent of the specified MultiPointOnSphere object. |
| `add( const ElementType &element, const MultiPointOnSphere &multi_point_on_sphere, const FiniteRotation &finite_rotation, location_type *location_added = NULL)` | method | `void` | public | Same as the above overload of add but location of insertion is the \*rotated\* geometry. |
| `add( const ElementType &element, const MultiPointOnSphere &multi_point_on_sphere, const AngularExtent &region_of_interest, location_type *location_added = NULL)` | method | `void` | public | Add an element, to the spatial partition, using the \*expanded\* (by region-of-interest) spatial extent of the specified MultiPointOnSphere object. |
| `add( const ElementType &element, const MultiPointOnSphere &multi_point_on_sphere, const AngularExtent &region_of_interest, const FiniteRotation &finite_rotation, location_type *location_added = NULL)` | method | `void` | public | Same as the above overload of add but location of insertion is the \*rotated\* geometry. |
| `add( const ElementType &element, const PolylineOnSphere &polyline_on_sphere, location_type *location_added = NULL)` | method | `void` | public | Add an element, to the spatial partition, using the spatial extent of the specified PolylineOnSphere object. |
| `add( const ElementType &element, const PolylineOnSphere &polyline_on_sphere, const FiniteRotation &finite_rotation, location_type *location_added = NULL)` | method | `void` | public | Same as the above overload of add but location of insertion is the \*rotated\* geometry. |
| `add( const ElementType &element, const PolylineOnSphere &polyline_on_sphere, const AngularExtent &region_of_interest, location_type *location_added = NULL)` | method | `void` | public | Add an element, to the spatial partition, using the \*expanded\* (by region-of-interest) spatial extent of the specified PolylineOnSphere object. |
| `add( const ElementType &element, const PolylineOnSphere &polyline_on_sphere, const AngularExtent &region_of_interest, const FiniteRotation &finite_rotation, location_type *location_added = NULL)` | method | `void` | public | Same as the above overload of add but location of insertion is the \*rotated\* geometry. |
| `add( const ElementType &element, const PolygonOnSphere &polygon_on_sphere, location_type *location_added = NULL)` | method | `void` | public | Add an element, to the spatial partition, using the spatial extent of the specified PolygonOnSphere object. |
| `add( const ElementType &element, const PolygonOnSphere &polygon_on_sphere, const FiniteRotation &finite_rotation, location_type *location_added = NULL)` | method | `void` | public | Same as the above overload of add but location of insertion is the \*rotated\* geometry. |
| `add( const ElementType &element, const PolygonOnSphere &polygon_on_sphere, const AngularExtent &region_of_interest, location_type *location_added = NULL)` | method | `void` | public | Add an element, to the spatial partition, using the \*expanded\* (by region-of-intereset) spatial extent of the specified PolygonOnSphere object. |
| `add( const ElementType &element, const PolygonOnSphere &polygon_on_sphere, const AngularExtent &region_of_interest, const FiniteRotation &finite_rotation, location_type *location_added = NULL)` | method | `void` | public | Same as the above overload of add but location of insertion is the \*rotated\* geometry. |
| `add( const ElementType &element, const location_type &location, location_type *location_added = NULL)` | method | `void` | public | Add an element, to the spatial partition, at the location specified. location\_added can be different than location if the latter is the location in another spatial partition and it is deeper than the maximum depth of this spatial ... |
| `add_unpartitioned( const ElementType &element, location_type *location_added = NULL)` | method | `void` | public | Add an element, to the spatial partition, at the root of the entire cube quad tree. |
| `get_or_create_quad_tree_root_node( CubeCoordinateFrame::CubeFaceType cube_face)` | method | `node_reference_type` | public | Gets, or creates if does not exist, the root node of the specified cube face (quad tree). |
| `get_or_create_child_node( node_reference_type parent_node, unsigned int child_x_offset, unsigned int child_y_offset)` | method | `node_reference_type` | public | Gets, or creates if does not exist, the child node of the specified parent node. |
| `add( const ElementType &element, node_reference_type cube_quad_tree_node)` | method | `void` | public | Add an element, to the spatial partition, at the node location specified. get\_or\_create\_quad\_tree\_root\_node or get\_or\_create\_child\_node. |
| `element_list_node_pool_type` | typedef | `boost::object_pool<ElementListNode>` | private | Typedef for an object pool for type ElementListNode. |
| `AddGeometryOnSphere` | struct | `None` | private | Add GeometryOnSphere derived objects to this spatial partition. |
| `AddRotatedGeometryOnSphere` | struct | `None` | private | Add GeometryOnSphere derived objects to this spatial partition in at their \*rotated\* locations. |
| `AddRegionOfInterestGeometryOnSphere` | struct | `None` | private | Add GeometryOnSphere derived objects (with extended bounding circles) to this spatial partition. |
| `AddRegionOfInterestRotatedGeometryOnSphere` | struct | `None` | private | Add GeometryOnSphere derived objects (with extended bounding circles) to this spatial partition in at their \*rotated\* locations. |
| `d_element_list_node_pool` | field | `boost::scoped_ptr<element_list_node_pool_type>` | private | All element linked list nodes are stored in this pool. |
| `d_cube_quad_tree` | field | `typename cube_quad_tree_type::non_null_ptr_type` | private | The cube quad tree. |
| `d_maximum_quad_tree_depth` | field | `unsigned int` | private | The maximum depth of any quad tree. |
| `d_num_elements` | field | `unsigned int` | private | The number of elements that have been added to this spatial partition. |
| `d_dummy_empty_element_list_impl` | field | `element_list_impl_type` | private | Used solely for the purpose of returning an empty iteration range when clients request the root elements but there are none. |
| `CubeQuadTreePartition( unsigned int maximum_quad_tree_depth)` | constructor | `None` | private | Constructor. |
| `add( const ElementType &element, ElementList &element_list)` | method | `void` | private | NOTE: All adds should go through here to keep track of whether the spatial partition is empty or not. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_CUBEQUADTREEPARTITION_H` | macro | `None` | — |

## Notes

**This is an insert-only structure.** There is no way to remove an element or a
node — only `clear()`, which throws away the whole thing. That is a deliberate
choice, stated in the comments on both pools: because nothing is ever returned,
element list nodes use `boost::object_pool` directly rather than
`GPlatesUtils::ObjectPool`, and the underlying `CubeQuadTree` never needs its
release path. The intended lifecycle is build-once-per-reconstruction-time,
traverse, discard.

**Elements are copied in, and iteration order within a node is reverse
insertion.** `add()` copies the element into a pool-allocated `ElementListNode`
and `push_front`s it, so `ElementType` must be copy-constructible and the
elements of one node come back last-added-first. Nothing preserves insertion
order.

**The cube root is not a quad tree node and is easy to miss.** Elements whose
bounding circle will not fit inside the loose root bound of any cube face are
placed at the root of the cube instead, via three separate escape hatches in the
bounding-circle `add()`: an extent at or beyond a hemisphere, a circle whose
projection onto its nearest cube face is not well defined, and a projected radius
exceeding the face half-width. `add_unpartitioned()` puts an element there
explicitly. Traversal code that walks only the six quad trees silently drops
these, and a partition can be non-`empty()` while every quad tree root is null.

**`maximum_quad_tree_depth` bounds only the spatial `add()` path.** The top-down
`get_or_create_child_node()` path can descend past it — the `create()` comment
says so — while `add(element, const location_type &)` clamps a too-deep location
by right-shifting its offsets. Two partitions built by different routes can
therefore disagree about their real depth. Note also that memory is
`6 * 4^depth`-ish in the worst case, so raising the depth is not free.

**`NodeReference` is a bare pointer with no ownership and no provenance check.**
It is pointer-sized and cheap to copy, tests as a boolean via
`GPlatesUtils::SafeBool`, and is null when the node does not exist — the header
warns to check it after `get_quad_tree_root_node()` and `get_child_node()`, while
the `get_or_create_*` results are always valid. It does not keep the partition
alive, and it is invalidated by `clear()`. `add(element, node_reference_type)`
documents that passing a node from a *different* partition is undefined
behaviour, and nothing detects it.

**`NodeReference::operator!=` is written as `return lhs != rhs;`** — it calls
itself and will recurse until the stack is exhausted. Use `!(a == b)`.
`operator==` is correct.

**Everything is unsynchronised.** `add()` allocates from a `boost::object_pool`
and creates quad tree nodes on the fly, so concurrent insertion into one
partition is a race; concurrent read-only traversal is fine. Any `add()` also
invalidates outstanding iterators — they hold raw list and node pointers.

**Numerical fudge factors are load-bearing.** The insertion path is peppered with
tolerances (`0.5 - 1e-6` on the node offsets, `1 - 1e-6` on the node half-width,
`1e-4` and `1e-6` on the projection tests) whose job is to keep computed offsets
inside `[0, 2^depth)` and to reject projections that are near-degenerate. They
are not cosmetic — removing one produces out-of-range child offsets that index
the `[2][2]` child array out of bounds. The comments also record deliberate
micro-optimisations (hand-coded `fabs`, `int` rather than `unsigned int` casts
for Visual Studio) because this code runs once per geometry per reconstruction.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 227 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 74 |
| [maths/CubeQuadTreePartitionUtils](CubeQuadTreePartitionUtils.md) | maths | 53 |
| [opengl/GLFilledPolygonsGlobeView](../opengl/GLFilledPolygonsGlobeView.md) | opengl | 49 |
| [opengl/GLReconstructedStaticPolygonMeshes](../opengl/GLReconstructedStaticPolygonMeshes.md) | opengl | 45 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](../opengl/GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 35 |
| [data-mining/LookupReducer](../data-mining/LookupReducer.md) | data-mining | 16 |
| [app-logic/ReconstructLayerProxy](../app-logic/ReconstructLayerProxy.md) | app-logic | 15 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 12 |
| [view-operations/RenderedGeometryLayer](../view-operations/RenderedGeometryLayer.md) | view-operations | 9 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 8 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 6 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 5 |
| [app-logic/ReconstructGraph](../app-logic/ReconstructGraph.md) | app-logic | 4 |
| [unit-test/CoregTest](../unit-test/CoregTest.md) | unit-test | 4 |
| [app-logic/AssignPlateIds](../app-logic/AssignPlateIds.md) | app-logic | 3 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 3 |
| [app-logic/CoRegistrationLayerProxy](../app-logic/CoRegistrationLayerProxy.md) | app-logic | 2 |
| [app-logic/RasterLayerTask](../app-logic/RasterLayerTask.md) | app-logic | 2 |
| [app-logic/ScalarField3DLayerTask](../app-logic/ScalarField3DLayerTask.md) | app-logic | 2 |

*... and 11 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/CubeQuadTreePartition.h
python scripts/gpq.py def GPlatesMaths::CubeQuadTreePartition --body
python scripts/gpq.py uses CubeQuadTreePartition --kind class
python scripts/gpq.py hier CubeQuadTreePartition
```

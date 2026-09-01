# CubeQuadTreeLocation

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 199 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/CubeQuadTreeLocation.h` | C++ | 245 |
| `src/maths/CubeQuadTreeLocation.cc` | C++ | 301 |

## Overview

[[[PROSE overview unit=maths/CubeQuadTreeLocation tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::CubeQuadTreeLocation`](#gplatesmathscubequadtreelocation) | class | — | — | 0 | Specifies the location in a cube quad tree. |

## Members

### `GPlatesMaths::CubeQuadTreeLocation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NodeLocation` | struct | `None` | public | The location of a node in a quad tree (if applicable, ie, if not the root of the cube). x\_node\_offset\_ and y\_node\_offset\_ are in the range \[0, 2^quad\_tree\_depth). |
| `CubeQuadTreeLocation()` | constructor | `None` | public | Default constructor places location at the root of the cube (not in any quad tree). |
| `CubeQuadTreeLocation( CubeCoordinateFrame::CubeFaceType cube_face)` | constructor | `None` | public | This constructor places the location at the root node of the specified \*quad tree\*. |
| `CubeQuadTreeLocation( const CubeQuadTreeLocation &parent_location, unsigned int child_x_offset, unsigned int child_y_offset)` | constructor | `None` | public | This constructor creates a child node of the specified parent \*quad tree node\* location. |
| `CubeQuadTreeLocation( CubeCoordinateFrame::CubeFaceType cube_face, unsigned int quad_tree_depth, unsigned int x_node_offset, unsigned int y_node_offset)` | constructor | `None` | public | This constructor places the location at a specific node in one of the six quad trees. x\_node\_offset and y\_node\_offset are in the range \[0, 2^quad\_tree\_depth). |
| `CubeQuadTreeLocation( const NodeLocation &node_location)` | constructor | `None` | public | This convenience constructor places the location at a specific node in one of the six quad trees. |
| `is_root_of_cube()` | method | `bool` | public | Returns true if 'this' location refers to the root of the cube (not in any quad tree). |
| `get_child_node_location( unsigned int child_x_offset, unsigned int child_y_offset)` | method | `CubeQuadTreeLocation` | public | Creates a child node of the specified parent \*quad tree node\* location. |
| `d_node_location` | field | `boost::optional<NodeLocation>` | private | Is true if the location is a node in any of the six quad trees, otherwise it's false (location is at the root of the cube - not in any quad tree). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_CUBEQUADTREELOCATION_H` | macro | `None` | — |
| `do_same_depth_nodes_intersect( const CubeQuadTreeLocation &location_1, const CubeQuadTreeLocation &location_2)` | function | `bool` | Returns true if both locations are quad tree nodes, at the same quad tree depth, that intersect. |
| `intersect_loose_quad_tree_node_with_regular_quad_tree_node_at_parent_child_depths( const CubeQuadTreeLocation &loose_quad_tree_location_at_parent_depth, const CubeQuadTreeLocation &regular_quad_tree_location_at_child_depth)` | function | `bool` | Returns true if both locations are quad tree nodes that intersect and loose\_quad\_tree\_location\_at\_parent\_depth is at one depth closer to the root than regular\_quad\_tree\_location\_at\_child\_depth. |
| `intersect_loose_cube_quad_tree_location_with_regular_cube_quad_tree_location( const CubeQuadTreeLocation &loose_quad_tree_location, const CubeQuadTreeLocation &regular_quad_tree_location)` | function | `bool` | Returns true if the specified loose cube quad tree location intersects the specified regular one. |
| `intersect_loose_cube_quad_tree_location_with_loose_cube_quad_tree_location( const CubeQuadTreeLocation &loose_quad_tree_location_1, const CubeQuadTreeLocation &loose_quad_tree_location_2)` | function | `bool` | Returns true if the specified loose cube quad tree locations intersect each other. |

## Notes

[[[PROSE notes unit=maths/CubeQuadTreeLocation tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLMultiResolutionMapCubeMesh](../opengl/GLMultiResolutionMapCubeMesh.md) | opengl | 14 |
| [maths/CubeQuadTreePartitionUtils](CubeQuadTreePartitionUtils.md) | maths | 13 |
| [maths/CubeQuadTreePartition](CubeQuadTreePartition.md) | maths | 11 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](../opengl/GLMultiResolutionCubeReconstructedRaster.md) | opengl | 11 |
| [opengl/GLMultiResolutionCubeMesh](../opengl/GLMultiResolutionCubeMesh.md) | opengl | 8 |
| [view-operations/RenderedGeometryLayer](../view-operations/RenderedGeometryLayer.md) | view-operations | 8 |
| [opengl/GLFilledPolygonsGlobeView](../opengl/GLFilledPolygonsGlobeView.md) | opengl | 6 |
| [app-logic/ReconstructLayerProxy](../app-logic/ReconstructLayerProxy.md) | app-logic | 5 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 5 |
| [maths/CubeQuadTree](CubeQuadTree.md) | maths | 4 |
| [maths/CubeCoordinateFrame](CubeCoordinateFrame.md) | maths | 3 |
| [opengl/GLReconstructedStaticPolygonMeshes](../opengl/GLReconstructedStaticPolygonMeshes.md) | opengl | 2 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/CubeQuadTreeLocation.h
python scripts/gpq.py def GPlatesMaths::CubeQuadTreeLocation --body
python scripts/gpq.py uses CubeQuadTreeLocation --kind class
python scripts/gpq.py hier CubeQuadTreeLocation
```

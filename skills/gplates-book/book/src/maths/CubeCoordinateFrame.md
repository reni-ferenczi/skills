# CubeCoordinateFrame

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 627 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/CubeCoordinateFrame.h` | C++ | 297 |
| `src/maths/CubeCoordinateFrame.cc` | C++ | 568 |

## Overview

[[[PROSE overview unit=maths/CubeCoordinateFrame tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::CubeCoordinateFrame::(anonymous)::CoordinateTransform`](#gplatesmathscubecoordinateframeanonymouscoordinatetransform) | struct | — | — | 0 | Used to look up a component of the untransformed vector (in global coord frame). |
| [`GPlatesMaths::CubeCoordinateFrame::(anonymous)::CubeEdgeInfo`](#gplatesmathscubecoordinateframeanonymouscubeedgeinfo) | struct | — | — | 0 | Used to look up a component of the untransformed vector (in global coord frame). |
| [`GPlatesMaths::CubeCoordinateFrame::(anonymous)::CubeQuadTreeNodeLocationTransform`](#gplatesmathscubecoordinateframeanonymouscubequadtreenodelocationtransform) | struct | — | — | 0 | Used to transform cube quad tree node locations from one cube face to another. |
| [`GPlatesMaths::CubeCoordinateFrame::CubeFaceType`](#gplatesmathscubecoordinateframecubefacetype) | enum | — | — | 0 | Identifies a face of the cube. |
| [`GPlatesMaths::CubeCoordinateFrame::CubeFaceCoordinateFrameAxis`](#gplatesmathscubecoordinateframecubefacecoordinateframeaxis) | enum | — | — | 0 | Identifies each axis in the \*local\* right-handed coordinate frame of a cube face. |
| [`GPlatesMaths::CubeCoordinateFrame::cube_corner_index_type`](#gplatesmathscubecoordinateframecube_corner_index_type) | typedef | — | — | 0 | An index into an array of cube corner points (eight points). |
| [`GPlatesMaths::CubeCoordinateFrame::cube_edge_index_type`](#gplatesmathscubecoordinateframecube_edge_index_type) | typedef | — | — | 0 | An index into an array of cube edges (twelve edges). |

## Members

### `GPlatesMaths::CubeCoordinateFrame::(anonymous)::CoordinateTransform`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `component_offset` | field | `CubeFaceCoordinateFrameAxis` | public | — |
| `component_sign` | field | `float` | public | — |

### `GPlatesMaths::CubeCoordinateFrame::(anonymous)::CubeEdgeInfo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `cube_edge_index` | field | `cube_edge_index_type` | public | — |
| `is_local_axis_direction_opposite_edge_direction` | field | `bool` | public | — |

### `GPlatesMaths::CubeCoordinateFrame::(anonymous)::CubeQuadTreeNodeLocationTransform`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `transform( int &transform_to_x_node_offset, int &transform_to_y_node_offset, unsigned int transform_from_quad_tree_depth, unsigned int transform_from_x_node_offset, unsigned int transform_from_y_node_offset)` | method | `void` | public | — |
| `x_translation` | field | `int` | public | — |
| `xx` | field | `int` | public | — |
| `xy` | field | `int` | public | — |
| `y_translation` | field | `int` | public | — |
| `yx` | field | `int` | public | — |
| `yy` | field | `int` | public | — |

### `GPlatesMaths::CubeCoordinateFrame::CubeFaceType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `POSITIVE_X` | enumerator | `None` | — | — |
| `NEGATIVE_X` | enumerator | `None` | — | — |
| `POSITIVE_Y` | enumerator | `None` | — | — |
| `NEGATIVE_Y` | enumerator | `None` | — | — |
| `POSITIVE_Z` | enumerator | `None` | — | — |
| `NEGATIVE_Z` | enumerator | `None` | — | — |
| `NUM_FACES` | enumerator | `None` | — | — |

### `GPlatesMaths::CubeCoordinateFrame::CubeFaceCoordinateFrameAxis`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `X_AXIS` | enumerator | `None` | — | — |
| `Y_AXIS` | enumerator | `None` | — | — |
| `Z_AXIS` | enumerator | `None` | — | — |
| `NUM_AXES` | enumerator | `None` | — | — |

### `GPlatesMaths::CubeCoordinateFrame::cube_corner_index_type`

*None.*

### `GPlatesMaths::CubeCoordinateFrame::cube_edge_index_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `OPPOSING_CUBE_FACE` | variable | `CubeFaceType` | The cube face opposite each cube face. |
| `CUBE_FACE_COORDINATES_FRAMES` | variable | `UnitVector3D` | These directions are the standard directions used by 3D graphics APIs for cube map textures so we'll adopt the same convention. |
| `CUBE_FACE_COORDINATE_TRANSFORMS` | variable | `CoordinateTransform` | Easy way to transform a vector from global coord frame to the local coord frame of a cube face. |
| `CUBE_CORNER_INDICES` | variable | `cube_corner_index_type` | The indices of corner points for each face of the cube. |
| `CUBE_CORNERS` | variable | `Vector3D` | The corner points of the cube as an indexable array. |
| `PROJECTED_CUBE_CORNERS` | variable | `UnitVector3D` | The projected corner points of the cube, projected onto the sphere, as an indexable array. |
| `CUBE_EDGE_INDICES` | variable | `CubeEdgeInfo` | The indices of cube edges for each face of the cube. |
| `CUBE_EDGE_DIRECTIONS` | variable | `UnitVector3D` | The edge directions of the edges of the cube as an indexable array. |
| `CUBE_EDGE_START_POINTS` | variable | `cube_edge_index_type` | The edge start points as indices into the cube corners. |
| `CUBE_EDGE_END_POINTS` | variable | `cube_edge_index_type` | The edge end points as indices into the cube corners. |
| `CUBE_QUAD_TREE_NODE_LOCATIONS_TRANSFORMS` | variable | `CubeQuadTreeNodeLocationTransform` | Transforms (for cube quad tree node locations) for all combinations of cube face pairs. |
| `GPLATES_MATHS_CUBECOORDINATEFRAME_H` | macro | `None` | — |
| `NUM_CUBE_CORNERS` | variable | `unsigned int` | The number of corners in a cube. |
| `NUM_CUBE_EDGES` | variable | `unsigned int` | The number of edges in a cube. |
| `get_cube_face_opposite( CubeFaceType cube_face)` | function | `CubeFaceType` | Returns the cube face opposite the specified cube face. |
| `get_cube_face_coordinate_frame_axis` | variable | `UnitVector3D` | Returns the specified axis in the \*local\* coordinate frame of the specified cube face. |
| `transform_into_cube_face_coordinate_frame( CubeFaceType cube_face, const UnitVector3D &position)` | function | `UnitVector3D` | Returns the specified position (which is in the global coordinate frame) to a vector in the local coordinate frame of the specified cube face. |
| `get_cube_face_and_transformed_position( const UnitVector3D &position, double &position_x_in_cube_face_coordinate_frame, double &position_y_in_cube_face_coordinate_frame, double &position_z_in_cube_face_coordinate_frame)` | function | `CubeFaceType` | Determines which cube face the specified position projects into and returns the position transformed into the local coordinate frame of that cube face. |
| `get_cube_corner_index( CubeFaceType cube_face, bool positive_x_axis, bool positive_y_axis)` | function | `cube_corner_index_type` | Returns an index that can be used to index into any array of size eight (representing the eight corner points of the cube). |
| `get_cube_corner` | variable | `Vector3D` | Returns the corner point of the specified cube corner index. |
| `get_projected_cube_corner` | variable | `UnitVector3D` | Returns the corner point, projected onto the sphere, of the specified cube corner index. |
| `get_cube_edge_index( CubeFaceType cube_face, bool x_axis, bool positive_orthogonal_axis, bool &reverse_edge_direction)` | function | `cube_edge_index_type` | Returns an index that can be used to index into any array of size twelve (representing the twelve edges of the cube). |
| `get_cube_edge_direction` | variable | `UnitVector3D` | Returns the edge direction of the specified cube edge index from the edge start point to the edge end point. |
| `get_cube_edge_start_point( cube_edge_index_type cube_edge_index)` | function | `cube_corner_index_type` | Returns the start point of the edge of the specified cube edge index. |
| `get_cube_edge_end_point( cube_edge_index_type cube_edge_index)` | function | `cube_corner_index_type` | Returns the end point of the edge of the specified cube edge index. |
| `get_cube_quad_tree_node_location_relative_to_cube_face( int &transform_to_x_node_offset, int &transform_to_y_node_offset, CubeFaceType transform_to_cube_face, CubeFaceType transform_from_cube_face, unsigned int transform_from_quad_tree_depth, unsigned int transform_from_x_node_offset, unsigned int transform_from_y_node ...` | function | `void` | Transforms the x and y cube quad tree node offsets from one cube face to another. |

## Notes

[[[PROSE notes unit=maths/CubeCoordinateFrame tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLCubeMeshGenerator](../opengl/GLCubeMeshGenerator.md) | opengl | 120 |
| [opengl/GLCubeSubdivision](../opengl/GLCubeSubdivision.md) | opengl | 71 |
| [opengl/GLMultiResolutionCubeMesh](../opengl/GLMultiResolutionCubeMesh.md) | opengl | 41 |
| [opengl/GLMapCubeMeshGenerator](../opengl/GLMapCubeMeshGenerator.md) | opengl | 34 |
| [opengl/GLMultiResolutionMapCubeMesh](../opengl/GLMultiResolutionMapCubeMesh.md) | opengl | 30 |
| [maths/CubeQuadTree](CubeQuadTree.md) | maths | 27 |
| [maths/CubeQuadTreePartitionUtils](CubeQuadTreePartitionUtils.md) | maths | 24 |
| [maths/CubeQuadTreeLocation](CubeQuadTreeLocation.md) | maths | 20 |
| [maths/CubeQuadTreePartition](CubeQuadTreePartition.md) | maths | 15 |
| [opengl/GLReconstructedStaticPolygonMeshes](../opengl/GLReconstructedStaticPolygonMeshes.md) | opengl | 11 |
| [opengl/GLCubeSubdivisionCache](../opengl/GLCubeSubdivisionCache.md) | opengl | 10 |
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 9 |
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 7 |
| [opengl/GLScalarField3DGenerator](../opengl/GLScalarField3DGenerator.md) | opengl | 7 |
| [opengl/GLMultiResolutionCubeRaster](../opengl/GLMultiResolutionCubeRaster.md) | opengl | 6 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 4 |
| [opengl/GLMultiResolutionCubeRasterInterface](../opengl/GLMultiResolutionCubeRasterInterface.md) | opengl | 4 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](../opengl/GLMultiResolutionCubeReconstructedRaster.md) | opengl | 3 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 2 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 2 |

*... and 5 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/CubeCoordinateFrame.h
python scripts/gpq.py def GPlatesMaths::CubeCoordinateFrame::(anonymous)::CubeQuadTreeNodeLocationTransform --body
python scripts/gpq.py uses CubeQuadTreeNodeLocationTransform --kind struct
python scripts/gpq.py hier CubeQuadTreeNodeLocationTransform
```

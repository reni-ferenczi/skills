# CubeCoordinateFrame

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 627 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/CubeCoordinateFrame.h` | C++ | 297 |
| `src/maths/CubeCoordinateFrame.cc` | C++ | 568 |

## Overview

GPlates covers the globe by inscribing the unit sphere in a cube and attaching a
quad tree to each of the six faces. This namespace is the single definition of
what that cube *is*: which face is which, which way its local x and y axes point,
where its eight corners and twelve edges are, and how a node in one face's quad
tree is addressed from a neighbouring face's frame. It is a convention rather
than an algorithm, and it exists precisely so there is only one of it — raster
tiling (`GLCubeSubdivision`, `GLMultiResolutionCubeMesh`, `GLCubeMeshGenerator`)
and geometry partitioning (`CubeQuadTreePartition`, `CubeQuadTreeLocation`) must
agree face-for-face and axis-for-axis, or a query such as "which reconstructed
polygons cover this raster tile" silently indexes into the wrong part of the
globe. The axis directions are the ones 3D graphics APIs use for cube map
textures, so the same frame serves both the CPU-side partition and the GPU-side
cube map.

Everything is implemented as constant lookup tables in an anonymous namespace in
the `.cc`, behind free functions that do nothing but index them. The three
structs listed above are those tables' element types — they are file-local, not
API. `transform_into_cube_face_coordinate_frame()` is a permutation of the three
components with a sign flip, driven by `CUBE_FACE_COORDINATE_TRANSFORMS`, rather
than a 3x3 matrix multiply, and `get_cube_face_and_transformed_position()` goes
further: it picks the face from the largest absolute component and then writes
the permutation out by hand in each of the eight branches, because that beat
going through the table when profiled. Because a signed permutation preserves
length, the result is fed into `UnitVector3D` with the validity check disabled.

The corner and edge tables give every corner and every edge one global index
shared by all the faces that touch it, so code walking a face boundary
(mesh generation, loose-node intersection) can identify the *same* corner from
either side. Note that the corners are on the cube — side length two, so it
bounds the unit sphere — not on the sphere; `get_projected_cube_corner()` is the
normalised version. `get_cube_quad_tree_node_location_relative_to_cube_face()`
sits at the other end of the file and is a different kind of thing: a 2x3 integer
affine transform per ordered face pair (36 of them) that re-expresses a quad tree
node offset in a neighbouring face's frame, which is what lets a spatial
partition test loose nodes for intersection across a cube edge. It works on node
*centres* — offsets are doubled and incremented to `2n+1` before the transform
and arithmetic-shifted back afterwards — which is why the result is signed and
may legitimately be negative or beyond the face's own node range.

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

**The tables are mutually redundant and nothing checks them.** Almost every array
in the `.cc` carries a comment saying it must be kept in sync with another one.
`CUBE_FACE_COORDINATES_FRAMES` (the axis vectors) and
`CUBE_FACE_COORDINATE_TRANSFORMS` (the same information as a component index plus
a sign) encode the same six frames twice; `CUBE_CORNER_INDICES`,
`CUBE_EDGE_INDICES` and `CUBE_QUAD_TREE_NODE_LOCATIONS_TRANSFORMS` are all
derived from that choice of frames, and `PROJECTED_CUBE_CORNERS` from
`CUBE_CORNERS`. There is no assertion, no unit test in this file and no
compile-time link between them: changing one axis direction and not the other
four tables produces code that runs and gives wrong answers only at cube face
boundaries. Treat the whole `.cc` as one artefact.

**The local z-axis is the negative of the face normal.** It points from the face
centre back towards the origin, so that the frame stays right-handed and matches
the OpenGL convention of looking down negative z. This is why
`get_cube_face_normal()` is implemented as the `Z_AXIS` of the *opposite* face,
and it is the single easiest thing to get wrong when reading this code.

**No bounds checking anywhere.** Every accessor indexes a fixed-size array
directly with its argument. `NUM_FACES`, `NUM_AXES`, `NUM_CUBE_CORNERS` and
`NUM_CUBE_EDGES` are counts, not valid values — passing `NUM_FACES` as a
`CubeFaceType`, or an index computed from untrusted data, reads out of bounds
without complaint.

**Inputs must genuinely be unit vectors.**
`transform_into_cube_face_coordinate_frame()` constructs its result with
`check_validity` false, on the grounds that permuting and negating components
cannot change the magnitude. A non-normalised input therefore propagates into a
`UnitVector3D` that violates its own invariant.

**Face selection on a boundary is arbitrary but deterministic.**
`get_cube_face_and_transformed_position()` compares absolute components with
strict `>`, so a position exactly on a cube edge or corner resolves to whichever
branch the tie falls through to. Callers that partition data by face must accept
that a point may sit on a face boundary and still land in exactly one face; they
must not assume the choice matches any other geometric test.

The tables are `const` and the functions are pure, so everything here is safe to
call from multiple threads. `PROJECTED_CUBE_CORNERS` is dynamically initialised
(it calls `Vector3D::get_normalisation()`), so as with any namespace-scope object
do not read it from another translation unit's static initialiser.

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

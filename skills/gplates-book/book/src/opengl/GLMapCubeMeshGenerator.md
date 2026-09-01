# GLMapCubeMeshGenerator

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 211 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLMapCubeMeshGenerator.h` | C++ | 163 |
| `src/opengl/GLMapCubeMeshGenerator.cc` | C++ | 206 |

## Overview

`GLMapCubeMeshGenerator` adapts the sphere-space cube subdivision mesh (built by `GLCubeMeshGenerator`) to a 2D map view by projecting each cube-face grid point through a `GPlatesGui::MapProjection`, producing a `Point` that carries both the original `UnitVector3D` position on the sphere and its map-projected `Point2D` coordinate. It exists because `GLMultiResolutionMapCubeMesh` and related map-view rendering need the same cube-subdivision tiling the globe view uses, but expressed in projected map coordinates instead of 3D positions.

Rather than generate a whole cube face at once, `create_cube_face_quadrant_mesh_vertices` works one quadrant at a time: a cube face is split into four quadrants specifically so the antimeridian (dateline) only ever falls on a quadrant edge rather than cutting across a quadrant's interior, since a map projection is generally discontinuous there. `create_pole_mesh_vertex` handles the north/south pole cases separately, because a pole's pre-projection longitude is degenerate and must be resolved from context (which quadrant, and which side of the dateline) rather than read off the sphere position directly.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLMapCubeMeshGenerator`](#gplatesopenglglmapcubemeshgenerator) | class | `boost::noncopyable` | — | 0 | Generates points for a cube subdivision mesh that are projected onto a 2D map. |

## Members

### `GPlatesOpenGL::GLMapCubeMeshGenerator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Point2D` | struct | `None` | public | A 2D map-projected point. |
| `Point` | struct | `None` | public | The 2D map-projected point and its associated position on the sphere. |
| `GLMapCubeMeshGenerator( const GPlatesGui::MapProjection &map_projection, unsigned int cube_face_dimension)` | constructor | `None` | public | Uses the specified map projection to project cube mesh points (on the sphere) onto the 2D map. cube\_face\_dimension specifies the density of mesh points along the side of a cube face. |
| `get_cube_face_quadrant_dimension_in_vertex_spacing()` | method | `unsigned int` | public | Returns the power-of-two dimension of the side of a \*quadrant\* of a cube face in terms of mesh vertex spacing. |
| `get_cube_face_quadrant_dimension_in_vertex_samples()` | method | `unsigned int` | public | Returns the number of mesh vertices along the side of a \*quadrant\* of a cube face. |
| `create_cube_face_quadrant_mesh_vertices( std::vector<Point> &cube_face_quadrant_mesh_vertices, GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face, unsigned int quadrant_x_offset, unsigned int quadrant_y_offset)` | method | `void` | public | Create all map-projected mesh vertices for the specified \*quadrant\* of the specified cube face. |
| `create_pole_mesh_vertex( const double &pole_longitude, bool north_pole)` | method | `Point` | public | Create a map-projected mesh vertex at the north or south pole with the specified longitude. |
| `d_cube_mesh_generator` | field | `GLCubeMeshGenerator` | private | Used to generate the cube mesh positions on the sphere. |
| `d_map_projection` | field | `GPlatesGui::MapProjection` | private | Used to project points on the sphere onto a 2D map. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLMAPCUBEMESHGENERATOR_H` | macro | `None` | — |

## Notes

- The `map_projection` reference passed to the constructor must outlive the `GLMapCubeMeshGenerator` — it is stored by reference, not copied.
- `cube_face_dimension` must be a power of two.
- `quadrant_x_offset`/`quadrant_y_offset` must each be 0 or 1; the vertex-indexing formula documented on `create_cube_face_quadrant_mesh_vertices` depends on that and on the quadrant sizes from `get_cube_face_quadrant_dimension_in_vertex_spacing`/`_samples`.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLMultiResolutionMapCubeMesh](GLMultiResolutionMapCubeMesh.md) | opengl | 70 |
| [qt-widgets/MapView](../qt-widgets/MapView.md) | qt-widgets | 12 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLMapCubeMeshGenerator.h
python scripts/gpq.py def GPlatesOpenGL::GLMapCubeMeshGenerator --body
python scripts/gpq.py uses GLMapCubeMeshGenerator --kind class
python scripts/gpq.py hier GLMapCubeMeshGenerator
```

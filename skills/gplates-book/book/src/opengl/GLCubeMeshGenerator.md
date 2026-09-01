# GLCubeMeshGenerator

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1038 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLCubeMeshGenerator.h` | C++ | 128 |
| `src/opengl/GLCubeMeshGenerator.cc` | C++ | 305 |

## Overview

`GLCubeMeshGenerator` builds the vertex grid used to tessellate one face of the cube used by GPlates' cube-subdivision rendering scheme, projecting a regular grid of `GPlatesMaths::UnitVector3D` points onto the sphere via `GPlatesMaths::CubeCoordinateFrame`. `create_cube_face_mesh_vertices` produces a whole face at the requested vertex density, while `create_mesh_vertices` produces just a sub-rectangle of it (indexed the same way a `CubeQuadTreeLocation` addresses a tile), so callers such as `GLMultiResolutionCubeMesh` and `GLMapCubeMeshGenerator` can generate only the vertices needed for a given quad-tree tile.

The constructor precomputes and caches the vertices along the cube's twelve edges before any face is meshed. This ensures that two adjacent cube faces, meshed independently, share identical vertex positions along their common edge, avoiding rendering seams that floating-point differences would otherwise introduce.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLCubeMeshGenerator`](#gplatesopenglglcubemeshgenerator) | class | `boost::noncopyable` | — | 0 | Generates points for a cube subdivision mesh (on the sphere) that is gridded along the cube subdivision tiles. |

## Members

### `GPlatesOpenGL::GLCubeMeshGenerator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLCubeMeshGenerator( unsigned int cube_face_dimension)` | constructor | `None` | public | Constructor. cube\_face\_dimension specifies the density of mesh points along the side of a cube face. |
| `get_cube_face_dimension_in_vertex_spacing()` | method | `unsigned int` | public | Returns the power-of-two dimension of the side of a cube face in terms of mesh vertex spacing. |
| `get_cube_face_dimension_in_vertex_samples()` | method | `unsigned int` | public | Returns the number of mesh vertices along the side of a cube face. |
| `create_cube_face_mesh_vertices( std::vector<GPlatesMaths::UnitVector3D> &cube_face_mesh_vertices, GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face)` | method | `void` | public | Create all mesh vertices for the specified cube face. |
| `create_mesh_vertices( std::vector<GPlatesMaths::UnitVector3D> &mesh_vertices, GPlatesMaths::CubeCoordinateFrame::CubeFaceType cube_face, unsigned int rect_x_offset, unsigned int rect_y_offset, unsigned int rect_width_in_samples, unsigned int rect_height_in_samples)` | method | `void` | public | Create a subset of the mesh vertices for the specified cube face. |
| `d_cube_face_dimension` | field | `unsigned int` | private | — |
| `d_cube_edge_vertices_array` | field | `std::vector<GPlatesMaths::UnitVector3D>` | private | The vertices along the twelve edges of the cube. |
| `create_cube_edge_vertices( const GPlatesMaths::UnitVector3D cube_corner_vertices[])` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLCUBEMESHGENERATOR_H` | macro | `None` | — |

## Notes

- `cube_face_dimension` must be a power of two; the constructor asserts this via `GPlatesGlobal::Assert` and throws `PreconditionViolationError` otherwise.
- The shared cube-edge vertices are computed once in the constructor, so a single `GLCubeMeshGenerator` instance should be reused across faces/tiles rather than reconstructed per call, both for performance and to guarantee seam-free adjacent faces.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLMapCubeMeshGenerator](GLMapCubeMeshGenerator.md) | opengl | 8 |
| [opengl/GLMultiResolutionCubeMesh](GLMultiResolutionCubeMesh.md) | opengl | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLCubeMeshGenerator.h
python scripts/gpq.py def GPlatesOpenGL::GLCubeMeshGenerator --body
python scripts/gpq.py uses GLCubeMeshGenerator --kind class
python scripts/gpq.py hier GLCubeMeshGenerator
```

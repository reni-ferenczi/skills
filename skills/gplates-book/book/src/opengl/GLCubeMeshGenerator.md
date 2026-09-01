# GLCubeMeshGenerator

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1038 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLCubeMeshGenerator.h` | C++ | 128 |
| `src/opengl/GLCubeMeshGenerator.cc` | C++ | 305 |

## Overview

[[[PROSE overview unit=opengl/GLCubeMeshGenerator tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=opengl/GLCubeMeshGenerator tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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

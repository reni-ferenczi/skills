# SmallCircleCoverageMesh

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 996 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/SmallCircleCoverageMesh.h` | C++ | 124 |
| `src/maths/SmallCircleCoverageMesh.cc` | C++ | 114 |

## Overview

`SmallCircleCoverageMesh` holds the output of a coverage calculation: a vector of triangles that completely cover a region bounded by a small circle. `SmallCircleCoverageMeshBuilder` is the builder that generates this mesh by recursively traversing a hierarchical triangular mesh and collecting triangles from a specified depth that overlap the small circle bounds. The builder uses the visitor pattern, integrating with `SphericalSubdivision::HierarchicalTriangularMeshTraversal` to traverse the mesh efficiently and avoid testing triangles that are known to be completely outside the small circle region.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::SmallCircleCoverageMesh`](#gplatesmathssmallcirclecoveragemesh) | class | — | — | 0 | The generated mesh that completely covers the region bounded by a small circle. |
| [`GPlatesMaths::SmallCircleCoverageMeshBuilder`](#gplatesmathssmallcirclecoveragemeshbuilder) | class | — | — | 0 | Used to recurse into a hierarchical triangular mesh and generate a triangle mesh that completely covers the region bounded by a small circle. |

## Members

### `GPlatesMaths::SmallCircleCoverageMesh`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Triangle` | struct | `None` | public | A mesh triangle. |
| `mesh` | field | `std::vector<Triangle>` | public | The mesh triangles. |

### `GPlatesMaths::SmallCircleCoverageMeshBuilder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SmallCircleCoverageMeshBuilder( SmallCircleCoverageMesh &coverage_mesh, const BoundingSmallCircle &small_circle_bounds, unsigned int depth_to_generate_mesh)` | constructor | `None` | public | Constructor. |
| `add_coverage_triangles()` | method | `void` | public | Adds coverage mesh triangles that completely cover the small circle bounds passed into constructor - triangles are added to the coverage mesh passed into constructor. |
| `RecursionContext` | struct | `None` | private | Keeps track of the recursion depth and whether we need to test child triangles against the small circle bounds (don't have to if parent is completely inside). |
| `d_coverage_mesh` | field | `SmallCircleCoverageMesh` | private | The target for the generated mesh. |
| `d_small_circle_bounds` | field | `BoundingSmallCircle` | private | Defines the small circle region that the coverage mesh will overlap. |
| `d_depth_to_generate_mesh` | field | `unsigned int` | private | The depth at which to generate mesh triangles. |
| `visit( const SphericalSubdivision::HierarchicalTriangularMeshTraversal::Triangle &triangle, const RecursionContext &recursion_context)` | method | `void` | public | Visits a triangle in the hierarchical triangular mesh. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_SMALLCIRCLECOVERAGEMESH_H` | macro | `None` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/SmallCircleCoverageMesh.h
python scripts/gpq.py def GPlatesMaths::SmallCircleCoverageMeshBuilder --body
python scripts/gpq.py uses SmallCircleCoverageMeshBuilder --kind class
python scripts/gpq.py hier SmallCircleCoverageMeshBuilder
```

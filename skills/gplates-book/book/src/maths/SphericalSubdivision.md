# SphericalSubdivision

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 130 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/SphericalSubdivision.h` | C++ | 452 |
| `src/maths/SphericalSubdivision.cc` | C++ | 81 |

## Overview

[[[PROSE overview unit=maths/SphericalSubdivision tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::SphericalSubdivision::HierarchicalTriangularMeshTraversal`](#gplatesmathssphericalsubdivisionhierarchicaltriangularmeshtraversal) | class | — | — | 0 | Allows clients to recursively traverse a Hierarchical Triangular Mesh. |
| [`GPlatesMaths::SphericalSubdivision::RhombicTriacontahedronTraversal`](#gplatesmathssphericalsubdivisionrhombictriacontahedrontraversal) | class | — | — | 0 | Allows clients to recursively traverse a subdivided Rhombic Triacontahedron in a quad-tree manner. |

## Members

### `GPlatesMaths::SphericalSubdivision::HierarchicalTriangularMeshTraversal`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HierarchicalTriangularMeshTraversal()` | constructor | `None` | public | Default constructor. |
| `Triangle` | class | `None` | public | A spherical triangle in the Hierarchical Triangular Mesh. |
| `visit( VisitorType &visitor, RecursionContextType &recursion_context)` | method | `void` | public | Visits the eight top-level spherical triangles that cover the sphere. |
| `vertex0` | field | `UnitVector3D` | private | — |
| `vertex1` | field | `UnitVector3D` | private | — |
| `vertex2` | field | `UnitVector3D` | private | — |
| `vertex3` | field | `UnitVector3D` | private | — |
| `vertex4` | field | `UnitVector3D` | private | — |
| `vertex5` | field | `UnitVector3D` | private | — |

### `GPlatesMaths::SphericalSubdivision::RhombicTriacontahedronTraversal`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RhombicTriacontahedronTraversal()` | constructor | `None` | public | Default constructor. |
| `Quad` | class | `None` | public | A quad patch in the subdivided Rhombic Triacontahedron. |
| `visit( VisitorType &visitor, RecursionContextType &recursion_context)` | method | `void` | public | Visits the thirty top-level quad faces that cover the sphere. |
| `normalise( const double &x, const double &y, const double &z)` | method | `UnitVector3D` | private | — |
| `normalise( const Vector3D &v)` | method | `UnitVector3D` | private | — |
| `GOLDEN_RATIO` | field | `double` | private | — |
| `GOLDEN_RATIO_2` | field | `double` | private | — |
| `GOLDEN_RATIO_3` | field | `double` | private | — |
| `vertex2` | field | `UnitVector3D` | private | — |
| `vertex4` | field | `UnitVector3D` | private | — |
| `vertex6` | field | `UnitVector3D` | private | — |
| `vertex8` | field | `UnitVector3D` | private | — |
| `vertex11` | field | `UnitVector3D` | private | — |
| `vertex12` | field | `UnitVector3D` | private | — |
| `vertex13` | field | `UnitVector3D` | private | — |
| `vertex16` | field | `UnitVector3D` | private | — |
| `vertex17` | field | `UnitVector3D` | private | — |
| `vertex18` | field | `UnitVector3D` | private | — |
| `vertex20` | field | `UnitVector3D` | private | — |
| `vertex23` | field | `UnitVector3D` | private | — |
| `vertex27` | field | `UnitVector3D` | private | — |
| `vertex28` | field | `UnitVector3D` | private | — |
| `vertex30` | field | `UnitVector3D` | private | — |
| `vertex31` | field | `UnitVector3D` | private | — |
| `vertex33` | field | `UnitVector3D` | private | — |
| `vertex34` | field | `UnitVector3D` | private | — |
| `vertex36` | field | `UnitVector3D` | private | — |
| `vertex37` | field | `UnitVector3D` | private | — |
| `vertex38` | field | `UnitVector3D` | private | — |
| `vertex41` | field | `UnitVector3D` | private | — |
| `vertex45` | field | `UnitVector3D` | private | — |
| `vertex46` | field | `UnitVector3D` | private | — |
| `vertex47` | field | `UnitVector3D` | private | — |
| `vertex50` | field | `UnitVector3D` | private | — |
| `vertex51` | field | `UnitVector3D` | private | — |
| `vertex52` | field | `UnitVector3D` | private | — |
| `vertex54` | field | `UnitVector3D` | private | — |
| `vertex56` | field | `UnitVector3D` | private | — |
| `vertex58` | field | `UnitVector3D` | private | — |
| `vertex60` | field | `UnitVector3D` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GOLDEN_RATIO` | variable | `double` | — |
| `GOLDEN_RATIO_2` | variable | `double` | — |
| `GOLDEN_RATIO_3` | variable | `double` | — |
| `GPLATES_MATHS_SPHERICALSUBDIVISION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/SphericalSubdivision tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/GeneratePoints](GeneratePoints.md) | maths | 23 |
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 13 |
| [maths/SmallCircleCoverageMesh](SmallCircleCoverageMesh.md) | maths | 8 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/SphericalSubdivision.h
python scripts/gpq.py def GPlatesMaths::SphericalSubdivision::RhombicTriacontahedronTraversal --body
python scripts/gpq.py uses RhombicTriacontahedronTraversal --kind class
python scripts/gpq.py hier RhombicTriacontahedronTraversal
```

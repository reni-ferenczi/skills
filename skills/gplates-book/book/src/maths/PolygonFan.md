# PolygonFan

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 701 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/PolygonFan.h` | C++ | 229 |
| `src/maths/PolygonFan.cc` | C++ | 227 |

## Overview

`PolygonFan` builds a triangular fan mesh whose apex sits at a polygon's centroid, with one triangle per boundary edge connecting the apex to that edge's two endpoints. It can also be built from a `PolylineOnSphere` (closing the gap between first and last vertex) or a `MultiPointOnSphere` (treating point order as a boundary), via the visitor `CreatePolygonFanFromGeometryOnSphere` that the `create(GeometryOnSphere...)` overload dispatches through.

Unlike `PolygonMesh`, which triangulates only the true interior fill region, a fan mesh triangle can lie outside the polygon's interior when the polygon is concave, and triangles can overlap. That trade-off is deliberate: the fan is cheap to build (no triangulation library involved) and is meant to be rendered with the graphics hardware's stencil buffer, inverting each pixel's mask on every triangle drawn, so the overlaps and outside-region triangles cancel out correctly to leave the true fill region — the same visual result as `PolygonMesh` at a fraction of the construction cost.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::(anonymous)::CreatePolygonFanFromGeometryOnSphere`](#gplatesmathsanonymouscreatepolygonfanfromgeometryonsphere) | class | [`ConstGeometryOnSphereVisitor`](ConstGeometryOnSphereVisitor.md) | — | 0 | Creates a PolygonFan from a GeometryOnSphere. |
| [`GPlatesMaths::PolygonFan`](#gplatesmathspolygonfan) | class | [`GPlatesUtils::ReferenceCount<PolygonFan>`](../utils/ReferenceCount.md) | — | 0 | A triangular fan mesh with apex at the centroid of a polygon. |

## Members

### `GPlatesMaths::(anonymous)::CreatePolygonFanFromGeometryOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_polygon_fan()` | method | `boost::optional<PolygonFan::non_null_ptr_to_const_type>` | public | Returns the optionally created PolygonFan after visiting a GeometryOnSphere. |
| `visit_multi_point_on_sphere( MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | public | — |
| `visit_point_on_sphere( PointGeometryOnSphere::non_null_ptr_to_const_type /*point_on_sphere*/)` | method | `void` | public | — |
| `visit_polygon_on_sphere( PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | public | — |
| `visit_polyline_on_sphere( PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | public | — |
| `d_polygon_fan` | field | `boost::optional<PolygonFan::non_null_ptr_to_const_type>` | private | — |

### `GPlatesMaths::PolygonFan`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<PolygonFan>` | public | A convenience typedef for a shared pointer to a non-const PolygonFan. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const PolygonFan>` | public | A convenience typedef for a shared pointer to a const PolygonFan. |
| `Triangle` | class | `None` | public | A fan mesh triangle. |
| `Vertex` | class | `None` | public | A fan mesh vertex. |
| `create( const PolygonOnSphere::non_null_ptr_to_const_type &polygon)` | method | `non_null_ptr_to_const_type` | public | Creates a PolygonFan object from a PolygonOnSphere. |
| `create( const PolylineOnSphere::non_null_ptr_to_const_type &polyline)` | method | `boost::optional<non_null_ptr_to_const_type>` | public | Creates a PolygonFan object from a PolylineOnSphere. |
| `create( const MultiPointOnSphere::non_null_ptr_to_const_type &multi_point)` | method | `boost::optional<non_null_ptr_to_const_type>` | public | Creates a PolygonFan object from a MultiPointOnSphere. |
| `create( const GeometryOnSphere::non_null_ptr_to_const_type &geometry_on_sphere)` | method | `boost::optional<non_null_ptr_to_const_type>` | public | Creates a PolygonFan object from a GeometryOnSphere. |
| `d_triangles` | field | `std::vector<Triangle>` | private | The fan mesh triangles. |
| `d_vertices` | field | `std::vector<Vertex>` | private | The fan mesh vertices. |
| `PolygonFan()` | constructor | `None` | private | Default constructor starts off with no triangles or vertices. |
| `add_fan_ring( const PointOnSphereForwardIter ring_points_begin, const unsigned int num_ring_points, const GPlatesMaths::UnitVector3D &centroid)` | method | `void` | private | Adds a fan ring to this fan mesh using the specified range of points as the ring boundary. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_POLYGONFAN_H` | macro | `None` | — |

## Notes

- `create(GeometryOnSphere...)` returns `boost::none` for a `PointOnSphere` (a single point cannot form a fan) and for a polyline or multipoint with fewer than three vertices; `create(PolygonOnSphere...)` never fails, since a `PolygonOnSphere` already guarantees at least three boundary vertices.
- A polygon's interior rings each become their own separate fan ring sharing the same overall mesh, rather than being subtracted from the exterior ring's fan.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLReconstructedStaticPolygonMeshes](../opengl/GLReconstructedStaticPolygonMeshes.md) | opengl | 23 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/PolygonFan.h
python scripts/gpq.py def GPlatesMaths::PolygonFan --body
python scripts/gpq.py uses PolygonFan --kind class
python scripts/gpq.py hier PolygonFan
```

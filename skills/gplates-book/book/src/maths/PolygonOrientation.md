# PolygonOrientation

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 644 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/PolygonOrientation.h` | C++ | 90 |
| `src/maths/PolygonOrientation.cc` | C++ | 274 |

## Overview

`PolygonOrientation` determines whether a `PolygonOnSphere` ring winds `CLOCKWISE` or `COUNTERCLOCKWISE` as seen from above the globe at that point. Because "above" only makes sense locally on a sphere, orientation is computed from the sign of a projected 2D signed area: the ring is projected onto a tangent plane with `GnomonicProjection` and `calculate_polygon_ring_projected_signed_area` sums the signed area of the projected vertices, which is much cheaper than a true spherical-area calculation. If the projection fails — the ring spans more than `MAXIMUM_PROJECTION_ANGLE_DEGREES` from its centroid, too big to fit on one tangent plane — the function falls back to a genuine spherical area calculation instead.

`calculate_polygon_orientation` reports the orientation of the whole polygon (dominated by the exterior ring, though a sufficiently large combined interior-ring area can flip it, even with interior rings of arbitrary orientation), while `calculate_polygon_exterior_ring_orientation` and `calculate_polygon_interior_ring_orientation` test one ring in isolation. This unit is a building block for `PolygonPartitioner` and the various GMT/OGR topology exporters, which need consistent, predictable ring winding regardless of how a feature's geometry happened to be digitised.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::PolygonOrientation::Orientation`](#gplatesmathspolygonorientationorientation) | enum | — | — | 0 | Orientation of a polygon. |

## Members

### `GPlatesMaths::PolygonOrientation::Orientation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CLOCKWISE` | enumerator | `None` | — | — |
| `COUNTERCLOCKWISE` | enumerator | `None` | — | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `MAXIMUM_PROJECTION_ANGLE_DEGREES` | variable | `double` | If any 3D point (in polygon) is further than this angle from the polygon centroid then the gnomonic projection fails. |
| `calculate_polygon_ring_projected_signed_area( const PolygonOnSphere::ring_vertex_const_iterator &ring_vertex_begin, const PolygonOnSphere::ring_vertex_const_iterator &ring_vertex_end, const GnomonicProjection &gnomonic_projection)` | function | `boost::optional<real_t>` | Iterate through the vertices of the polygon ring and project onto the plane and calculate the signed area of the projected ring. |
| `GPLATES_MATHS_POLYGONORIENTATION_H` | macro | `None` | — |
| `calculate_polygon_orientation( const PolygonOnSphere &polygon)` | function | `Orientation` | Calculates the orientation of the vertices of polygon when viewed from above the globe (looking down on the globe's surface). |
| `calculate_polygon_exterior_ring_orientation( const PolygonOnSphere &polygon)` | function | `Orientation` | Calculates the orientation of the exterior ring of the specified polygon when viewed from above the globe (looking down on the globe's surface). |
| `calculate_polygon_interior_ring_orientation( const PolygonOnSphere &polygon, unsigned int interior_ring_index)` | function | `Orientation` | Calculates the orientation of the interior ring at the specified interior ring index of the specified polygon when viewed from above the globe (looking down on the globe's surface). |

## Notes

The gnomonic-projection fast path only applies when every ring vertex is within 45 degrees (`MAXIMUM_PROJECTION_ANGLE_DEGREES`) of the ring's centroid; beyond that it transparently falls back to summing signed spherical triangle areas, so callers never need to check which path was taken.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportResolvedTopologyOptionsWidget](../qt-widgets/ExportResolvedTopologyOptionsWidget.md) | qt-widgets | 22 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 17 |
| [maths/PolygonOnSphere](PolygonOnSphere.md) | maths | 13 |
| [maths/PolygonPartitioner](PolygonPartitioner.md) | maths | 11 |
| [file-io/ResolvedTopologicalGeometryExport](../file-io/ResolvedTopologicalGeometryExport.md) | file-io | 8 |
| [gui/ExportResolvedTopologyAnimationStrategy](../gui/ExportResolvedTopologyAnimationStrategy.md) | gui | 7 |
| [file-io/GMTFormatResolvedTopologicalGeometryExport](../file-io/GMTFormatResolvedTopologicalGeometryExport.md) | file-io | 6 |
| [view-operations/VisibleReconstructionGeometryExport](../view-operations/VisibleReconstructionGeometryExport.md) | view-operations | 6 |
| [file-io/OgrFormatResolvedTopologicalGeometryExport](../file-io/OgrFormatResolvedTopologicalGeometryExport.md) | file-io | 5 |
| [gui/ConfigModel](../gui/ConfigModel.md) | gui | 2 |
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 2 |
| [gui/FeaturePropertyTableModel](../gui/FeaturePropertyTableModel.md) | gui | 2 |
| [gui/FeatureTableModel](../gui/FeatureTableModel.md) | gui | 2 |
| [qt-widgets/deprecated/CreateFeatureIdListModel](../qt-widgets/deprecated/CreateFeatureIdListModel.md) | qt-widgets | 2 |
| [qt-widgets/CoRegistrationResultTableDialog](../qt-widgets/CoRegistrationResultTableDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/PolygonOrientation.h
python scripts/gpq.py def GPlatesMaths::PolygonOrientation::Orientation --body
python scripts/gpq.py uses Orientation --kind enum
```
